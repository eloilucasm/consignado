#!/usr/bin/env python3
"""extrato.py - lê os contratos de empréstimo do Histórico de Empréstimo Consignado (INSS).

Herdado da skill triagem-consignado do pacote AMN v1.4. O PDF do INSS não traz posição de coluna
utilizável, mas a ORDEM das células é estável. Cada célula pode vir quebrada em vários fragmentos
terminados em "\\n"; os fragmentos são juntados até o que não termina em quebra. Uma linha da tabela
começa na célula do contrato, seguida pela célula do banco ("NNN - ...").

Campos por contrato: contrato, banco, seção (ATIVO ou EXCLUIDO), situação, competência de início e de
fim do desconto, parcelas contratadas, valor da parcela, origem da averbação, data de inclusão e de
exclusão, valor liberado e motivo da exclusão.

Limite: a ordem das células foi validada no extrato real pelo pacote AMN; neste pacote foi testada só
com extrato fictício. Confira a primeira leitura de cada extrato novo contra o PDF.

Uso:   python3 extrato.py EXTRATO.pdf        (uma linha JSON por contrato)
Requer: pip install pypdf
"""
import json
import re
import sys

try:
    import pypdf
except ImportError:  # mensagem útil em vez de traceback
    sys.exit("Falta a biblioteca pypdf. Instale com: pip install pypdf")

SECOES = [
    ("ATIVO", re.compile(r"CONTRATOS ATIVOS E SUSPENSOS")),
    ("EXCLUIDO", re.compile(r"CONTRATOS EXCLU[IÍ]DOS E ENCERRADOS")),
    ("CARTAO", re.compile(r"CART[AÃ]O DE CR[EÉ]DITO")),
]
RE_COMP = re.compile(r"^\d{2}/\d{4}$")
RE_DATA = re.compile(r"^\d{2}/\d{2}/\d{2}$")
RE_REAL = re.compile(r"^R\$\s?[\d.]+,\d{2}$")
RE_BANCO = re.compile(r"^\d{3}\s*-\s*\S")
SITUACOES = ("Ativo", "Suspenso", "Excluído", "Encerrado", "Excluido")

MOTIVOS = {  # o PDF cola as palavras da célula; forma compacta -> texto do extrato
    "exclusãobanco": "Exclusão Banco",
    "exclusãoporrefinanciamento": "Exclusão por refinanciamento",
    "exclusãoporportabilidade": "Exclusão por portabilidade",
    "exclusãoportrocadetitularidade": "Exclusão por troca de titularidade",
    "exclusãoinss": "Exclusão INSS",
    "exclusãoporóbito": "Exclusão por óbito",
    "exclusãoporcessação": "Exclusão por cessação",
}


def celulas(caminho):
    """[(secao, texto_da_celula)] na ordem do documento."""
    out = []
    secao = None
    for pg in pypdf.PdfReader(str(caminho)).pages:
        frags = []
        pg.extract_text(visitor_text=lambda t, *a: frags.append(t) if t.strip() else None)
        buf = ""
        for f in frags:
            buf += f
            if f.endswith("\n"):
                continue
            cel = re.sub(r"\s*\n\s*", "", buf).strip()
            buf = ""
            for nome, pad in SECOES:
                if pad.search(cel):
                    secao = nome
            out.append((secao, cel))
    return out


def data_extrato(caminho):
    """Data e hora de emissão do extrato (dd/mm/aaaa), lida da primeira página."""
    p1 = pypdf.PdfReader(str(caminho)).pages[0].extract_text()
    m = re.search(r"(\d{2}/\d{2}/\d{4}) \d{2}:\d{2}:\d{2}", p1)
    return m.group(1) if m else None


def motivo_legivel(s):
    k = re.sub(r"[\s.]", "", s).lower()
    if k in MOTIVOS:
        return MOTIVOS[k]
    return re.sub(r"(?<=[a-zà-ú])(?=[A-ZÀ-Ú])", " ", s).replace("Exclusãopor", "Exclusão por").rstrip(".")


def valor(s):
    return float(s.replace("R$", "").replace(".", "").replace(",", ".").strip())


def contratos(caminho):
    cels = celulas(caminho)
    linhas = []
    for i in range(len(cels) - 1):
        sec, c = cels[i]
        if sec not in ("ATIVO", "EXCLUIDO"):
            continue
        if RE_BANCO.match(cels[i + 1][1]) and not RE_BANCO.match(c) and re.search(r"\d{4}", c):
            linhas.append(i)
    res = []
    for k, ini in enumerate(linhas):
        fim = linhas[k + 1] if k + 1 < len(linhas) else len(cels)
        bloco = [c for _, c in cels[ini:fim]]
        r = {"contrato": bloco[0], "banco": bloco[1], "secao": cels[ini][0]}
        resto = bloco[2:]
        comps = [x for x in resto if RE_COMP.match(x)]
        r["inicio"], r["fim"] = (comps + [None, None])[:2]
        # parcelas contratadas: primeiro inteiro puro depois das competências
        pos_fim = resto.index(comps[1]) if len(comps) > 1 else 0
        inteiros = [x for x in resto[pos_fim + 1:] if re.fullmatch(r"\d{1,3}", x)]
        r["qtde_contratada"] = int(inteiros[0]) if inteiros else None
        reais = [x for x in resto[pos_fim + 1:] if RE_REAL.match(x)]
        r["parcela"] = valor(reais[0]) if reais else None
        sit = next((x for x in resto if x.startswith(SITUACOES)), None)
        r["situacao"] = sit
        r["origem_averbacao"] = r["inclusao"] = r["exclusao"] = r["liberado"] = r["motivo_exclusao"] = None
        if sit:
            j = resto.index(sit)
            r["origem_averbacao"] = resto[j + 1] if j + 1 < len(resto) else None
            datas = [x for x in resto[j + 1:] if RE_DATA.match(x)]
            r["inclusao"] = datas[0] if datas else None
            r["exclusao"] = datas[1] if (len(datas) > 1 and r["secao"] == "EXCLUIDO") else None
            if r["inclusao"]:  # "liberado": valor em R$ logo após a data de inclusão, quando existe
                k2 = resto.index(r["inclusao"], j)
                if k2 + 1 < len(resto) and RE_REAL.match(resto[k2 + 1]):
                    r["liberado"] = valor(resto[k2 + 1])
            if r["exclusao"]:  # motivo: células "Exclusão ..." depois da data de exclusão
                k2 = resto.index(r["exclusao"], j)
                mot = [x for x in resto[k2 + 1:k2 + 4] if x.lower().startswith("exclus")]
                if mot:
                    r["motivo_exclusao"] = motivo_legivel(mot[0])
        res.append(r)
    return res


def norm(c):
    n = re.sub(r"[^0-9A-Z]", "", (c or "").upper())
    return n.lstrip("0") or n


def buscar(lista, numero):
    """Localiza um contrato da análise na lista do extrato. Se o mesmo número aparecer mais de uma
    vez (ex.: migrado), devolve todas as ocorrências."""
    n = norm(numero)
    return [r for r in lista if norm(r["contrato"]) == n]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # no Windows, a saída redirecionada sairia em cp1252
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    for r in contratos(sys.argv[1]):
        print(json.dumps(r, ensure_ascii=False))
