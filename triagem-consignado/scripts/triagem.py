#!/usr/bin/env python3
"""Triagem de consignados: cruza a Análise Jurídico-Documental com o Termo de
Responsabilidade (e, opcionalmente, com os extratos do INSS) e gera a ficha de
ajuizamento.

Uso:
  python3 triagem.py --termo TERMO.pdf --analise ANALISE.pdf [--analise OUTRA.pdf]
                     [--extrato EXTRATO.pdf ...] --saida PASTA

Regra central: o texto do termo é SEMPRE limpo antes do cruzamento — páginas
juntadas, rodapé/relatório do ZapSign removidos, números quebrados entre linhas
ou páginas recompostos. Nenhum contrato é dado como "não autorizado" sem antes
passar pela busca no texto compactado e pela busca de números parecidos.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

try:
    import pypdf
except ImportError:
    sys.exit("pypdf não instalado: pip3 install pypdf")


# ---------------------------------------------------------------- leitura

def ler_pdf(caminho):
    r = pypdf.PdfReader(str(caminho))
    return [pg.extract_text() or "" for pg in r.pages]


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


# Linhas do ZapSign / assinatura eletrônica que aparecem no meio do termo.
RODAPE_ZAPSIGN = [
    r"^\s*ZapSign\s*-\s*[0-9a-f\-]{20,}.*$",
    r"^.*Documento assinado eletronicamente, conforme MP 2\.200-2/2001.*$",
    r"^\s*Assinado (digitalmente )?via ZapSign.*$",
    r"^\s*\d+\s*/\s*\d+\s*$",  # numeração de página "1 / 5"
]
# A partir daqui é o relatório de assinaturas — não faz parte do termo.
INICIO_RELATORIO = re.compile(r"^\s*(Status:\s*Assinado|Relat[oó]rio de Assinaturas|Anexos\s*$)", re.M)


def limpar_termo(paginas):
    """Junta as páginas, remove ZapSign e recompõe números quebrados."""
    linhas = []
    for pg in paginas:
        for ln in pg.splitlines():
            if any(re.match(p, ln, re.I) for p in RODAPE_ZAPSIGN):
                continue
            linhas.append(ln)
    texto = "\n".join(linhas).replace("\xa0", " ")
    m = INICIO_RELATORIO.search(texto)
    if m:
        texto = texto[: m.start()]
    # número quebrado em hífen/barra/underline no fim da linha: "51-\n025868432/25"
    texto = re.sub(r"([0-9A-Z][\-/_])\s*\n\s*(?=[0-9])", r"\1", texto)
    # remove marcações de data que o pessoal cola junto aos números
    texto = re.sub(r"[—–-]\s*incl\.?\s*\d{2}/\d{2}/\d{2,4}", " ", texto, flags=re.I)
    texto = re.sub(r"\(\s*\d{2}/\d{2}/\d{2,4}\s*\)", " ", texto)
    return texto


# ---------------------------------------------------------------- contratos

TOKEN = re.compile(r"(?<![0-9A-Za-z])([A-Z]{0,4}\d[0-9\-/_.]*[0-9A-Z])(?![0-9A-Za-z])")
DATA = re.compile(r"^\d{2}/\d{2}/\d{2,4}$")


def norm(c):
    """Forma canônica: só letras/dígitos, maiúsculo, sem zeros à esquerda."""
    n = re.sub(r"[^0-9A-Z]", "", c.upper())
    return n.lstrip("0") or n


def tokens_contrato(texto, minimo=7):
    out = []
    for m in TOKEN.finditer(texto):
        t = m.group(1)
        if DATA.match(t):
            continue
        if re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", t):  # CPF
            continue
        if re.fullmatch(r"\d{5}-\d{3}", t):  # CEP
            continue
        if len(norm(t)) >= minimo:
            out.append(t)
    return out


def distancia(a, b):
    if abs(len(a) - len(b)) > 3:
        return 99
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


# ---------------------------------------------------------------- termo

BENEFICIOS = [
    ("PENSÃO POR MORTE", r"pens[aã]o\s+por\s+morte"),
    ("APOSENTADORIA POR IDADE", r"aposentadoria\s+por\s+idade"),
    ("APOSENTADORIA POR INVALIDEZ", r"aposentadoria\s+por\s+invalidez|incapacidade\s+permanente"),
    ("APOSENTADORIA POR TEMPO DE CONTRIBUIÇÃO", r"aposentadoria\s+por\s+tempo"),
    ("BPC/LOAS", r"\bloas\b|\bbpc\b|amparo\s+social|benef[ií]cio\s+de\s+presta[cç][aã]o\s+continuada"),
    ("AUXÍLIO", r"aux[ií]lio[\s-]+(doen[cç]a|acidente|incapacidade)"),
]


def secoes_termo(texto):
    """Divide o termo em trechos por benefício. Cada trecho pertence ao rótulo
    de benefício que o antecede; o que vier antes de qualquer rótulo fica como
    'SEM BENEFÍCIO IDENTIFICADO'."""
    marcas = []
    for nome, pad in BENEFICIOS:
        for m in re.finditer(pad, texto, re.I):
            marcas.append((m.start(), nome))
    marcas.sort()
    secoes = []
    ini, atual = 0, "SEM BENEFÍCIO IDENTIFICADO"
    for pos, nome in marcas:
        secoes.append((atual, texto[ini:pos]))
        ini, atual = pos, nome
    secoes.append((atual, texto[ini:]))
    return [(n, t) for n, t in secoes if t.strip()]


def tipo_clausula(trecho_antes):
    """Classifica a cláusula onde o contrato aparece pelo texto que o precede."""
    t = sem_acento(trecho_antes[-3000:]).lower()
    pos = {
        "RMC/RCC": max(t.rfind("rmc"), t.rfind("rcc"), t.rfind("reserva de margem")),
        "CONSIGNADO (averbação/migração)": t.rfind("averbacao e/ou migracao"),
        "CONTRATO INDIVIDUAL (ex.: Tese 1000)": t.rfind("nao reconheco o contrato"),
    }
    melhor = max(pos.items(), key=lambda kv: kv[1])
    return melhor[0] if melhor[1] >= 0 else "não identificada"


def contratos_termo(texto):
    """{norm: {original, beneficio, clausula}} — primeira ocorrência de cada."""
    out = {}
    offset = 0
    for beneficio, trecho in secoes_termo(texto):
        base = texto.find(trecho, offset)
        for m in TOKEN.finditer(trecho):
            t = m.group(1)
            if DATA.match(t) or len(norm(t)) < 7:
                continue
            if re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}|\d{5}-\d{3}", t):
                continue
            n = norm(t)
            if n in out:
                out[n]["repeticoes"] += 1
                continue
            out[n] = {
                "original": t,
                "beneficio": beneficio,
                "clausula": tipo_clausula(texto[: base + m.start()]),
                "repeticoes": 1,
            }
        offset = base + len(trecho)
    return out


def qualificacao_termo(texto):
    q = {}
    m = re.search(r"EU,\s*(.+?)\s*,", texto, re.S)
    q["nome"] = m.group(1).strip() if m else None
    m = re.search(r"CPF sob o n[ºo°]\s*([\d.\-]+)", texto)
    q["cpf"] = m.group(1) if m else None
    m = re.search(r"RG n[ºo°]\s*([^,\n]*)", texto)
    q["rg"] = (m.group(1).strip() or None) if m else None
    m = re.search(r"residente e domiciliad[oa\(\)]* (?:à|a|na)\s*(.+?CEP\s*[\d\-]+.+?/[A-Z]{2})", texto, re.S)
    q["endereco"] = re.sub(r"\s+", " ", m.group(1)).strip() if m else None
    m = re.search(r"endere[cç]o eletr[oô]nico\s*([^\s,]+@[^\s,]+)", texto)
    q["email"] = m.group(1) if m else None
    m = re.search(r"\n\s*([A-ZÀ-Úa-zà-ú ]+),\s*(\d{1,2} de \w+ de \d{4})", texto)
    q["local_data"] = f"{m.group(1).strip()}, {m.group(2)}" if m else None
    return q


# ---------------------------------------------------------------- análise

BLOCOS = [
    ("CAIXA", r"BLOCO CAIXA"),
    ("E", r"BLOCO E\b"),
    ("A", r"BLOCO A\b"),
    ("B", r"BLOCO B\b"),
    ("C", r"BLOCO C\b"),
    ("D", r"BLOCO D\b"),
]
RE_BANCO = re.compile(r"\b(\d{3})\s*-\s*([A-ZÀ-Ú0-9][A-ZÀ-Ú0-9 .,&/\-]+?)(?=\s+\d{4}\b|\s+(?:ATIVO|Ativo|Exclu|Encerr|RMC|RCC|\d+\s*$)|\n|$)")


def ler_analise(caminho):
    paginas = ler_pdf(caminho)
    linhas = []
    for pg in paginas:
        for ln in pg.splitlines():
            if re.search(r"Advogados Associados \|", ln) or re.match(r"^\s*P[aá]gina \d+\s*$", ln):
                continue
            linhas.append(ln)
    texto = "\n".join(linhas)
    cab = {}
    m = re.search(r"Titular:\s*(.+?)\s*\|", texto)
    cab["titular"] = m.group(1).strip() if m else None
    m = re.search(r"Benef[ií]cio:\s*([\d.\-]+)\s*\(([^)]+)\)", texto)
    cab["nb"], cab["especie"] = (m.group(1), m.group(2).strip()) if m else (None, None)
    m = re.search(r"TOTAL GERAL DE A[ÇC][ÕO]ES\s*\n?\s*(\d+)", texto)
    cab["total_declarado"] = int(m.group(1)) if m else None

    # posições dos blocos
    pos = []
    for nome, pad in BLOCOS:
        m = re.search(pad, texto)
        if m:
            pos.append((m.start(), nome))
    m = re.search(r"RESUMO FINAL", texto)
    fim = m.start() if m else len(texto)
    pos.sort()
    acoes = []
    for i, (ini, bloco) in enumerate(pos):
        trecho = texto[ini: pos[i + 1][0] if i + 1 < len(pos) else fim]
        # IDs das ações: "A-1" (formato antigo) ou "A1" (formato novo)
        ids = list(re.finditer(rf"(?m)^\s*({re.escape(bloco)}-?\d+)\b", trecho))
        for j, mid in enumerate(ids):
            corpo = trecho[mid.end(): ids[j + 1].start() if j + 1 < len(ids) else len(trecho)]
            acoes.append(montar_acao(bloco, mid.group(1), corpo))
    return cab, acoes, texto


def montar_acao(bloco, id_acao, corpo):
    banco = None
    mb = RE_BANCO.search(corpo)
    if mb:
        nome_banco = re.sub(r"\s+", " ", mb.group(2)).strip()
        banco = f"{mb.group(1)} - {nome_banco}"
    contratos = []
    if bloco in ("B", "C"):
        # cada contrato vem como "NÚMERO — incl. dd/mm/aaaa" ou "NÚMERO (dd/mm/aa)"
        for m in re.finditer(r"([0-9A-Z][0-9A-Z\-/_.]{5,})\s*(?:[—–-]\s*incl\.|\(\d{2}/\d{2}/\d{2,4}\))", corpo):
            contratos.append(m.group(1))
    else:
        # E, A, D, CAIXA: o primeiro número após o ID é o contrato da ação
        # (no bloco E, o contrato-raiz vem depois e é só referência)
        toks = tokens_contrato(corpo)
        if toks:
            contratos.append(toks[0])
    status = None
    if bloco in ("A", "D", "E", "CAIXA"):
        ms = re.search(r"\b(ATIVO|Ativo|Exclu[ií]do|Encerrado|Suspenso)\b", corpo)
        status = ms.group(1).upper().replace("Í", "I") if ms else None
    tipo_cartao = None
    if bloco == "D":
        mt = re.search(r"\b(RMC|RCC)\b", corpo)
        tipo_cartao = mt.group(1) if mt else None
    return {
        "id": id_acao,
        "bloco": bloco,
        "banco": banco,
        "contratos": contratos,
        "status": status,
        "tipo_cartao": tipo_cartao,
        "observacoes": re.sub(r"\s+", " ", corpo).strip()[:400],
    }


# ---------------------------------------------------------------- extrato

SECOES_EXTRATO = [
    ("ATIVO", r"CONTRATOS ATIVOS E SUSPENSOS"),
    ("EXCLUIDO", r"CONTRATOS EXCLU[IÍ]DOS E ENCERRADOS"),
    ("CARTAO", r"CART[AÃ]O DE CR[EÉ]DITO"),
]


def ler_extrato(caminho):
    paginas = ler_pdf(caminho)
    texto = "\n".join(paginas)
    p1 = paginas[0] if paginas else ""
    m_nb = re.search(r"N[ºo°] Benef[ií]cio:\s*([\d.\-]+)", p1)
    m_esp = re.search(r"Benef[ií]cio\s*\n\s*(.+)", p1)
    compacto = re.sub(r"[^0-9A-Z]", "", texto.upper())
    # texto compactado por seção, para saber se o contrato está ativo ou excluído
    marcas = sorted((m.start(), nome) for nome, pad in SECOES_EXTRATO for m in re.finditer(pad, texto))
    secoes = {"ATIVO": "", "EXCLUIDO": "", "CARTAO": ""}
    for i, (ini, nome) in enumerate(marcas):
        fim = marcas[i + 1][0] if i + 1 < len(marcas) else len(texto)
        secoes[nome] += re.sub(r"[^0-9A-Z]", "", texto[ini:fim].upper())
    return {
        "arquivo": Path(caminho).name,
        "nb": m_nb.group(1) if m_nb else None,
        "especie": m_esp.group(1).strip() if m_esp else None,
        "compacto": compacto,
        "secoes": secoes,
    }


def status_no_extrato(contrato, extrato):
    """ATIVO se o contrato está na seção de ativos/suspensos; EXCLUIDO se só na de
    excluídos/encerrados; None se não achou."""
    if not extrato:
        return None
    if no_compacto(contrato, extrato["secoes"]["ATIVO"]):
        return "ATIVO"
    if no_compacto(contrato, extrato["secoes"]["EXCLUIDO"]):
        return "EXCLUIDO"
    return None


def no_compacto(contrato, compacto):
    n = re.sub(r"[^0-9A-Z]", "", contrato.upper())
    return n in compacto or (n.lstrip("0") and n.lstrip("0") in compacto)


# ---------------------------------------------------------------- cruzamento

# Tese de cada bloco. Teses diferentes nunca vão no mesmo processo.
TESE_DO_BLOCO = {"A": "MIGRADO", "B": "NAO_CONTRATADO", "C": "NAO_CONTRATADO",
                 "CAIXA": "NAO_CONTRATADO", "E": "TESE_1000", "D": "RMC_REFINANCIAMENTO"}
MODELOS = {
    ("MIGRADO", True): "Emp. Migrados Ativos C/ Liminar",
    ("MIGRADO", False): "Emp. Migrados Inativos S/ Liminar",
    ("NAO_CONTRATADO", True): "Emp. Não Contratado — COM liminar",
    ("NAO_CONTRATADO", False): "Emp. Não Contratado S/ Liminar",
    ("TESE_1000", True): "Tese 1000 Contra",
    ("TESE_1000", False): "Tese 1000 Contra",
    ("RMC_REFINANCIAMENTO", True): "Nulidade de Refinanciamento RMC/RCC (Lei Desenrola)",
    ("RMC_REFINANCIAMENTO", False): "Nulidade de Refinanciamento RMC/RCC (Lei Desenrola)",
}
AUTORIZADOS = ("AUTORIZADO", "AUTORIZADO (conferir grafia)")


def modelo_para(acao):
    tese = TESE_DO_BLOCO.get(acao["bloco"])
    return MODELOS.get((tese, acao.get("status") == "ATIVO"), "definir") if tese else "definir"


def cruzar(acoes, termo_contr, termo_compacto, nb_analise, especie_analise):
    """Regra: só entra o contrato que está no termo. Número parecido NÃO entra —
    aparece só como observação, para o caso de erro de digitação no termo."""
    resultado = []
    usados = set()
    for a in acoes:
        linhas = []
        for c in a["contratos"]:
            n = norm(c)
            if n in termo_contr:
                info = termo_contr[n]
                usados.add(n)
                obs = []
                if especie_analise and info["beneficio"] != "SEM BENEFÍCIO IDENTIFICADO" \
                        and sem_acento(info["beneficio"]).upper().split()[0] not in sem_acento(especie_analise).upper():
                    obs.append(f"no termo está na seção de {info['beneficio']}")
                if a["bloco"] == "D" and info["clausula"] != "RMC/RCC":
                    obs.append(f"cartão autorizado em cláusula '{info['clausula']}'")
                linhas.append({"contrato": c, "status": "AUTORIZADO", "termo": info["original"],
                               "clausula": info["clausula"], "obs": "; ".join(obs)})
                continue
            # 2ª chance: texto compactado (número quebrado no meio dos dígitos)
            if no_compacto(c, termo_compacto):
                linhas.append({"contrato": c, "status": "AUTORIZADO (conferir grafia)", "termo": "texto corrido",
                               "clausula": "?", "obs": "número aparece no termo com quebra no meio"})
                continue
            # 3ª: número parecido — informativo apenas
            parecidos = sorted(
                (distancia(n, k), v["original"], v["beneficio"]) for k, v in termo_contr.items()
                if distancia(n, k) <= 3 or (len(n) >= 8 and (n[:6] == k[:6] or n[-6:] == k[-6:]))
            )
            obs = ""
            if parecidos:
                d, orig, ben = parecidos[0]
                obs = f"termo traz número parecido {orig} (seção {ben}) — não entra"
            linhas.append({"contrato": c, "status": "NÃO AUTORIZADO", "termo": "", "clausula": "", "obs": obs})
        if any(l["status"] in AUTORIZADOS for l in linhas):
            geral = "AJUIZAR" if all(l["status"] in AUTORIZADOS for l in linhas) else "AJUIZAR PARCIAL"
        else:
            geral = "NÃO AJUIZAR"
        resultado.append({**a, "nb": nb_analise, "modelo": modelo_para(a), "linhas": linhas, "decisao": geral})
    return resultado, usados


# ---------------------------------------------------------------- juízo

DADOS = Path(__file__).resolve().parent.parent / "references" / "dados"
ALIASES = {  # grafias diferentes entre TJBA, TRF1 e endereços
    "camaca": "camacan", "camacan": "camaca",
    "muquemdesaofrancisco": "muquemdosaofrancisco", "muquemdosaofrancisco": "muquemdesaofrancisco",
    "oliveiradebrejinhos": "oliveiradosbrejinhos", "oliveiradosbrejinhos": "oliveiradebrejinhos",
    "governadorlomantojunior": "barropreto", "barropretogovernadorlomantojunior": "barropreto",
    "governadorlomantojuniorbarropreto": "barropreto",
}


def chave_cidade(c):
    return re.sub(r"[^a-z]", "", sem_acento(c or "").lower())


def _busca(cidade, tabela):
    """tabela: {chave_normalizada: valor}. Retorna (valor, observação)."""
    k = chave_cidade(cidade)
    if k in tabela:
        return tabela[k], None
    if ALIASES.get(k) in tabela:
        return tabela[ALIASES[k]], f"grafia '{cidade}' casada por equivalência"
    perto = sorted((distancia(k, kk), kk) for kk in tabela if abs(len(kk) - len(k)) <= 2)
    if perto and perto[0][0] <= 2:
        return tabela[perto[0][1]], f"'{cidade}' não consta literalmente; usado o mais próximo — CONFERIR"
    return None, f"'{cidade}' não localizado na tabela — CONFERIR"


def juizo(cidade_uf, eh_caixa):
    """Endereçamento conforme as tabelas oficiais (dados/*.json).
    Caixa → Vara Federal da (Sub)Seção do TRF1; demais → comarca do TJBA (a unidade sai de enderecamentos())."""
    if not cidade_uf or "/" not in cidade_uf:
        return "NÃO DEFINIDO — cidade do autor não identificada", "cidade do autor não identificada no termo"
    cidade, uf = cidade_uf.rsplit("/", 1)
    uf = uf.strip().upper()
    if eh_caixa:
        dados = json.loads((DADOS / "trf1_jurisdicao.json").read_text(encoding="utf-8"))["municipios"]
        tab = {chave_cidade(o["municipio"]): o["subsecao"] for o in dados if o["uf"] == uf}
        if not tab:
            return f"Vara Federal — UF {uf} fora da tabela do TRF1", f"UF {uf} não está na tabela do TRF1 — CONFERIR"
        sub, obs = _busca(cidade, tab)
        if not sub:
            return "Vara Federal — subseção NÃO LOCALIZADA", obs
        return (f"Vara Federal da {sub}/{uf}" if sub.startswith("Subseção") else f"Vara Federal da {sub}"), obs
    if uf != "BA":
        return f"Vara Cível da Comarca de {cidade}/{uf}", f"UF {uf}: sem tabela de comarcas — CONFERIR"
    dados = json.loads((DADOS / "tjba_comarcas.json").read_text(encoding="utf-8"))["municipio_comarca"]
    tab = {chave_cidade(k): v for k, v in dados.items()}
    com, obs = _busca(cidade, tab)
    if not com:
        return "Vara Cível — comarca NÃO LOCALIZADA", obs
    if chave_cidade(com) != chave_cidade(cidade):
        obs = ((obs + "; ") if obs else "") + f"o município {cidade} pertence à comarca de {com}"
    return f"Comarca de {com}/BA", obs


def enderecamentos(competencia):
    """Endereçamento pronto do JEC e da Justiça Comum para a comarca (dados/tjba_unidades.json, decisão de 03/11/2026).
    Só para réu do TJBA; para a Caixa e fora da Bahia devolve (None, None, None)."""
    m = re.match(r"^Comarca de (.+)/BA$", competencia or "")
    if not m:
        return None, None, None
    arq = DADOS / "tjba_unidades.json"
    if not arq.exists():
        return None, None, "tjba_unidades.json ausente — CONFERIR o endereçamento"
    tab = json.loads(arq.read_text(encoding="utf-8"))["comarcas"]
    u = tab.get(m.group(1))
    if not u:
        return None, None, f"comarca {m.group(1)} fora de tjba_unidades.json — CONFERIR"
    obs = u.get("conferir")
    if u["jec"]["tipo"] != "vara_do_sistema":
        nota = "comarca sem Vara do Sistema dos Juizados: no JEC, dizer no preâmbulo 'pelo procedimento da Lei nº 9.099/95'"
        obs = f"{obs}; {nota}" if obs else nota
    return u["jec"]["enderecamento"], u["comum"]["enderecamento"], obs


def agrupar(resultado, extratos, cidade_uf=None):
    """Regras do escritório:
    - um processo por BENEFÍCIO + BANCO + TESE (migrado, não contratado, Tese 1000, RMC);
      anos e blocos diferentes da mesma tese juntam (B + C; Caixa é não contratado);
    - liminar só sobre os contratos ATIVOS do processo;
    - mesmo banco em outro benefício → ações separadas + tópico de ausência de
      litispendência citando o NB desta ação e o(s) do(s) outro(s)."""
    por_nb = {e["nb"]: e for e in extratos if e.get("nb")}
    grupos = {}
    for r in resultado:
        if r["decisao"] == "NÃO AJUIZAR":
            continue
        tese = TESE_DO_BLOCO.get(r["bloco"], "DEFINIR")
        cod = (r["banco"] or "?").split(" - ")[0].strip()
        g = grupos.setdefault((r.get("nb"), cod, tese), {"banco": r["banco"], "nb": r.get("nb"), "tese": tese,
                                                         "acoes_origem": [], "contratos": [], "obs": []})
        g["acoes_origem"].append(r["id"])
        if r["bloco"] == "D" and re.search(r"n[aã]o verific[aá]vel", r.get("observacoes", ""), re.I):
            g["obs"].append(f"{r['id']}: a análise marca a tese de refinanciamento como NÃO VERIFICÁVEL")
        for l in r["linhas"]:
            if l["status"] not in AUTORIZADOS:
                continue
            if r["bloco"] in ("A", "D", "E", "CAIXA") and r.get("status"):
                st = r["status"].replace("Í", "I")
                st = "ATIVO" if st.startswith("ATIVO") else "EXCLUIDO"
            else:
                st = status_no_extrato(l["contrato"], por_nb.get(r.get("nb"))) or "?"
            g["contratos"].append({"contrato": l["contrato"], "acao": r["id"], "bloco": r["bloco"],
                                   "status": st, "conferir_grafia": l["status"] != "AUTORIZADO"})
    processos = []
    ordem = {"A": 0, "B": 1, "C": 1, "CAIXA": 2, "E": 3, "D": 4}
    itens = sorted(grupos.values(), key=lambda g: (g["nb"] or "", ordem.get(g["acoes_origem"][0].split("-")[0], 9),
                                                   g["acoes_origem"][0]))
    for i, g in enumerate(itens, 1):
        ativos = [c["contrato"] for c in g["contratos"] if c["status"] == "ATIVO"]
        tem_liminar = bool(ativos)
        modelo = MODELOS.get((g["tese"], tem_liminar), "definir")
        alertas = list(g["obs"])
        if any(c["status"] == "?" for c in g["contratos"]):
            alertas.append("status (ativo/excluído) não identificado no extrato — conferir; sem isso não dá para "
                           "decidir a liminar")
        bc_ativos = [c["contrato"] for c in g["contratos"] if c["bloco"] in ("B", "C") and c["status"] == "ATIVO"]
        if bc_ativos:
            # a análise só põe contratos não ativos em B/C — se aparecer ativo, é anomalia
            alertas.append(f"ANOMALIA: contrato(s) de bloco B/C ATIVO(s) no extrato ({', '.join(bc_ativos)}) — "
                           f"a análise só deveria trazer não ativos em B/C; conferir antes de redigir")
            ativos = [a for a in ativos if a not in bc_ativos]
            tem_liminar = bool(ativos)
            modelo = MODELOS.get((g["tese"], tem_liminar), "definir")
        eh_caixa = (g["banco"] or "").startswith("104") or "CAIXA" in (g["banco"] or "").upper()
        competencia, obs_juizo = juizo(cidade_uf, eh_caixa)
        if obs_juizo:
            alertas.append(f"juízo: {obs_juizo}")
        end_jec, end_comum, obs_end = enderecamentos(competencia)
        if obs_end:
            alertas.append(f"endereçamento: {obs_end}")
        processos.append({"processo": i, "nb": g["nb"], "reu": g["banco"], "tese": g["tese"],
                          "competencia": competencia, "enderecamento_jec": end_jec, "enderecamento_comum": end_comum,
                          "acoes_origem": g["acoes_origem"], "contratos": g["contratos"], "modelo": modelo,
                          "liminar_sobre": ativos if g["tese"] in ("MIGRADO", "NAO_CONTRATADO") else ativos,
                          "litispendencia": None, "alertas": alertas})
    # mesmo banco em outro processo → tópico de ausência de litispendência:
    #  - benefício diferente: citar o NB desta ação e o(s) outro(s);
    #  - mesmo benefício, tese diferente: dizer que são contratos e teses diferentes.
    for p in processos:
        cod = (p["reu"] or "?").split(" - ")[0].strip()
        irmaos = [q for q in processos if q is not p and (q["reu"] or "?").split(" - ")[0].strip() == cod]
        outros_nb = sorted({q["nb"] for q in irmaos if q["nb"] != p["nb"]})
        outras_teses = sorted({q["tese"] for q in irmaos if q["nb"] == p["nb"] and q["tese"] != p["tese"]})
        if outros_nb or outras_teses:
            p["litispendencia"] = {"nb_desta_acao": p["nb"], "tese_desta_acao": p["tese"],
                                   "outros_beneficios": outros_nb, "outras_teses_mesmo_beneficio": outras_teses}
    return processos


# ---------------------------------------------------------------- saída

def fmt_md(cab_list, resultado, processos, sobras, qualif, alertas, extratos):
    L = []
    titular = next((c["titular"] for c in cab_list if c.get("titular")), qualif.get("nome"))
    L.append(f"# Ficha de ajuizamento — {titular}\n")
    L.append("## Qualificação (conforme termo)\n")
    for k, v in qualif.items():
        L.append(f"- **{k}**: {v if v else '⚠️ EM BRANCO'}")
    L.append("")
    for c in cab_list:
        L.append(f"- Análise: NB **{c['nb']}** ({c['especie']}) — total declarado na análise: {c['total_declarado']} ações")
    for e in extratos:
        L.append(f"- Extrato: `{e['arquivo']}` — NB **{e['nb']}** ({e['especie']})")
    L.append("")

    L.append("## Processos a ajuizar (agrupados por banco)\n")
    L.append("| # | NB | Réu | Contratos | Modelo | Liminar sobre | Juízo | Ações da análise |")
    L.append("|---|---|---|---|---|---|---|---|")
    for p in processos:
        cts = "<br>".join(f"{c['contrato']} ({c['bloco']}, {c['status'].lower()})" + (" ⚠️grafia" if c["conferir_grafia"] else "")
                          for c in p["contratos"])
        lim = "<br>".join(p["liminar_sobre"]) or "—"
        L.append(f"| {p['processo']} | {p['nb']} | {p['reu']} | {cts} | {p['modelo']} | {lim} | {p['competencia']} | {', '.join(p['acoes_origem'])} |")
    L.append("")
    ends = [p for p in processos if p.get("enderecamento_jec")]
    if ends:
        L.append("**Endereçamento** (o rito é pergunta ao advogado; `references/dados/territorial-tjba.md`):\n")
        for p in ends:
            L.append(f"- Processo {p['processo']} — JEC: {p['enderecamento_jec']} · Justiça Comum: {p['enderecamento_comum']}")
        L.append("")
    for p in processos:
        if p["litispendencia"]:
            lp = p["litispendencia"]
            partes = []
            if lp["outros_beneficios"]:
                partes.append(f"benefícios distintos (esta: NB {p['nb']}; outra(s): NB {', '.join(lp['outros_beneficios'])})")
            if lp["outras_teses_mesmo_beneficio"]:
                partes.append(f"teses distintas no mesmo benefício (esta: {p['tese']}; outra(s): "
                              f"{', '.join(lp['outras_teses_mesmo_beneficio'])})")
            L.append(f"- 📌 Processo {p['processo']} ({p['reu']}): incluir tópico de AUSÊNCIA DE LITISPENDÊNCIA — "
                     + "; ".join(partes) + ".")
        for al in p["alertas"]:
            L.append(f"- ⚠️ Processo {p['processo']} ({p['reu']}): {al}")
    L.append("")

    L.append("## Conferência por ação da análise\n")
    L.append("| Ação | Réu | Contratos | Termo | Situação |")
    L.append("|---|---|---|---|---|")
    icone = {"AJUIZAR": "✅", "AJUIZAR PARCIAL": "🟡", "NÃO AJUIZAR": "❌"}
    for r in resultado:
        cts = "<br>".join(l["contrato"] for l in r["linhas"]) or "—"
        tms = "<br>".join(l["status"] + (f" ({l['obs']})" if l["obs"] else "") for l in r["linhas"]) or "—"
        extra = f" [{r['status']}]" if r.get("status") else ""
        tc = f" {r['tipo_cartao']}" if r.get("tipo_cartao") else ""
        L.append(f"| {r['id']}{tc}{extra} | {r['banco'] or '?'} | {cts} | {tms} | {icone[r['decisao']]} {r['decisao']} |")
    L.append("")

    if sobras:
        L.append("## Contratos do termo SEM ação nesta análise\n")
        L.append("| Contrato (termo) | Seção do termo | Cláusula | Onde aparece |")
        L.append("|---|---|---|---|")
        for s in sobras:
            L.append(f"| {s['original']} | {s['beneficio']} | {s['clausula']} | {s['onde']} |")
        L.append("")

    if alertas:
        L.append("## Alertas\n")
        for a in alertas:
            L.append(f"- ⚠️ {a}")
        L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--termo", required=True)
    ap.add_argument("--analise", action="append", default=[])
    ap.add_argument("--extrato", action="append", default=[])
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()

    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)

    termo_txt = limpar_termo(ler_pdf(a.termo))
    (saida / "termo_limpo.txt").write_text(termo_txt, encoding="utf-8")
    termo_contr = contratos_termo(termo_txt)
    termo_compacto = re.sub(r"[^0-9A-Z]", "", termo_txt.upper())
    qualif = qualificacao_termo(termo_txt)

    extratos = [ler_extrato(e) for e in a.extrato]

    cab_list, resultado, usados, alertas = [], [], set(), []
    for arq in a.analise:
        cab, acoes, _ = ler_analise(arq)
        cab_list.append(cab)
        if cab["total_declarado"] is not None and cab["total_declarado"] != len(acoes):
            alertas.append(f"Análise NB {cab['nb']}: o resumo declara {cab['total_declarado']} ações, "
                           f"mas foram lidas {len(acoes)} — conferir a leitura da análise.")
        for ac in acoes:
            if not ac["contratos"]:
                if ac["bloco"] != "CAIXA":
                    alertas.append(f"{ac['id']}: nenhum contrato lido — conferir na análise.")
        res, us = cruzar(acoes, termo_contr, termo_compacto, cab["nb"], cab["especie"])
        resultado += res
        usados |= us
        if extratos and cab["nb"] and not any(e["nb"] == cab["nb"] for e in extratos):
            alertas.append(f"Análise do NB {cab['nb']} sem o extrato correspondente entre os arquivos.")

    # contratos do termo que não viraram ação
    sobras = []
    for n, info in termo_contr.items():
        if n in usados:
            continue
        # contrato-raiz citado na própria análise (ex.: raiz da Tese 1000) não é sobra
        onde = []
        for e in extratos:
            if no_compacto(info["original"], e["compacto"]):
                onde.append(f"extrato NB {e['nb']}")
        sobras.append({**info, "onde": ", ".join(onde) if onde else "não localizado nos extratos enviados"})
        if info["repeticoes"] > 1:
            alertas.append(f"Termo repete o contrato {info['original']} ({info['repeticoes']}x).")
    for n, info in termo_contr.items():
        if n in usados and info["repeticoes"] > 1:
            alertas.append(f"Termo repete o contrato {info['original']} ({info['repeticoes']}x) — "
                           f"verificar se outro número deveria estar no lugar.")

    # cada contrato da análise deve existir no extrato do mesmo NB
    for r in resultado:
        ext = [e for e in extratos if e["nb"] and any(e["nb"] == c["nb"] for c in cab_list)]
        for l in r["linhas"]:
            if ext and not any(no_compacto(l["contrato"], e["compacto"]) for e in ext):
                alertas.append(f"{r['id']}: contrato {l['contrato']} não localizado no extrato do benefício — "
                               f"conferir digitação na análise.")
    nbs_sem_analise = {e["nb"] for e in extratos} - {c["nb"] for c in cab_list}
    for nb in nbs_sem_analise:
        qtd = sum(1 for s in sobras if f"NB {nb}" in s["onde"])
        alertas.append(f"Extrato do NB {nb} enviado SEM análise: {qtd} contrato(s) autorizados no termo "
                       f"aparecem nesse extrato e ainda não foram classificados.")

    if not qualif.get("rg"):
        alertas.append("RG em branco no termo — conferir no documento pessoal antes de qualificar.")

    m_cid = re.search(r"([A-ZÀ-Úa-zà-ú' ]+)/([A-Z]{2})\s*$", qualif.get("endereco") or "")
    cidade_uf = (re.sub(r"(?i)^.*\bcidade de\s+", "", m_cid.group(1)).strip() + "/" + m_cid.group(2)) if m_cid else None
    processos = agrupar(resultado, extratos, cidade_uf)
    md = fmt_md(cab_list, resultado, processos, sobras, qualif, alertas, extratos)
    (saida / "ficha.md").write_text(md, encoding="utf-8")
    (saida / "ficha.json").write_text(json.dumps({
        "qualificacao": qualif, "analises": cab_list,
        "extratos": [{k: v for k, v in e.items() if k not in ("compacto", "secoes")} for e in extratos],
        "processos": processos, "acoes": resultado, "contratos_termo_sem_acao": sobras, "alertas": alertas,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()
