"""Coleta jurisprudência qualificada e confere cada fonte contra uma segunda.

Derivado de `scripts/baixar_jurisprudencia.py` do repositório ctresb/leis (MIT; ver NOTICE.md), com
outra arquitetura: o texto e a situação vêm da fonte mais atual e a fonte oficial em arquivo
(caderno em PDF, CSV de dados abertos) entra como conferência e como origem dos campos que a
primeira não tem. Mudanças em relação ao original:

- `pdftotext -enc UTF-8` explícito e leitura estrita. O original lê com `errors="replace"`: onde o
  `pdftotext` emite Latin-1 (Windows) os acentos viram o caractere de substituição (U+FFFD) sem aviso.
- Rodapé de página ("Página 185 de 2847") sai do texto; o original o deixava dentro do enunciado.
- Súmulas do STJ: o caderno oficial é de maio de 2021 (termina na súmula 649) e traz as súmulas
  antigas em MAIÚSCULAS e SEM ACENTO. O texto e a situação vêm do BNP/CNJ (676 súmulas, com
  situação); o caderno dá data da decisão, órgão, publicação, referências e histórico de redação.
- Cada fonte é cruzada com a outra e o resultado é relatado (`RELATORIO.md`); divergência real
  derruba o código de saída.
- Qualquer órgão e espécie do BNP (TJBA, TRF1, TNU, STF...) pelo mesmo caminho: `bnp:TJBA:SUM,IAC`.

    python -I coletar_jurisprudencia.py --saida PASTA stj-temas stj-sumulas
    python -I coletar_jurisprudencia.py --saida PASTA bnp:TJBA:SUM,IAC bnp:TNU:PUIL
    python -I coletar_jurisprudencia.py --bnp-listar TJBA TRF01 STF
    python -I coletar_jurisprudencia.py --saida PASTA stj-temas --conferir-acervo ../../jurisprudencia

Requer `pdftotext` (poppler) para as súmulas do STJ. Nada é gravado fora de `--saida`.
"""
import argparse
import csv
import datetime as dt
import difflib
import hashlib
import html
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import Limitador  # noqa: E402

UA = "Mozilla/5.0 (compatible; acervo-md/1.0)"
CKAN = "https://dadosabertos.web.stj.jus.br/api/3/action/package_show?id=precedentes-qualificados"
CADERNO_STJ = "https://www.stj.jus.br/docs_internet/SumulasSTJ.pdf"
BNP = "https://pangeabnp.pdpj.jus.br/api/v1/precedentes"
HOJE = dt.date.today().isoformat()

# espécie do BNP -> (pasta, prefixo do arquivo, nome por extenso)
ESPECIES = {
    "SUM": ("sumulas", "sumula", "Súmula"), "SV": ("sumulas-vinculantes", "sumula-vinculante", "Súmula vinculante"),
    "RG": ("repercussao-geral", "tema", "Tema de repercussão geral"), "RR": ("repetitivos", "tema", "Tema repetitivo"),
    "IRR": ("repetitivos", "irr", "Incidente de recurso repetitivo"), "CT": ("controversias", "controversia", "Controvérsia"),
    "IAC": ("iac", "iac", "Incidente de assunção de competência"), "IRDR": ("irdr", "irdr", "IRDR"),
    "SIRDR": ("sirdr", "sirdr", "Suspensão em IRDR"), "PUIL": ("uniformizacao", "puil", "Pedido de uniformização de interpretação de lei"),
    "NT": ("notas-tecnicas", "nt", "Nota técnica"), "ADI": ("controle-concentrado", "adi", "ADI"),
    "ADPF": ("controle-concentrado", "adpf", "ADPF"), "ADC": ("controle-concentrado", "adc", "ADC"),
    "ADO": ("controle-concentrado", "ado", "ADO"),
}


# ----------------------------------------------------------------------------------------- infra
class Coleta:
    """Cliente HTTP com limite de taxa e retentativa, pasta de saída e manifesto das fontes baixadas."""

    def __init__(self, saida, rps):
        self.saida, self.limite, self.manifesto, self.relatorio, self.falhas = saida, Limitador(rps), [], [], 0

    def pedir(self, url, dados=None, cab=None, tentativas=4, timeout=120):
        req = urllib.request.Request(url, data=dados, headers={"User-Agent": UA, **(cab or {})})
        ultimo = None
        for n in range(tentativas):
            self.limite.esperar()
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return r.status, r.read(), {"last_modified": r.headers.get("Last-Modified"),
                                                "etag": r.headers.get("ETag")}
            except urllib.error.HTTPError as e:
                if e.code in (400, 401, 403, 404, 410):
                    return e.code, e.read(), {}
                ultimo = e
            except Exception as e:  # rede, timeout, leitura incompleta
                ultimo = e
            time.sleep(2 * (n + 1) ** 2)
        raise RuntimeError(f"falhou após {tentativas} tentativas: {url}: {ultimo}")

    def guardar(self, relativo, bruto, url, info=None):
        caminho = os.path.join(self.saida, "_fonte", relativo)
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        with open(caminho, "wb") as f:
            f.write(bruto)
        self.manifesto.append({"arquivo": relativo.replace("\\", "/"), "url": url, "bytes": len(bruto),
                               "sha256": hashlib.sha256(bruto).hexdigest(), "baixado_em": HOJE, **(info or {})})
        return caminho

    def gravar(self, relativo, texto):
        texto = texto.replace("\r\n", "\n").replace("\r", "\n")  # células do CSV do STJ trazem CRLF no meio do texto
        caminho = os.path.join(self.saida, relativo)
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        with open(caminho + ".tmp", "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        os.replace(caminho + ".tmp", caminho)

    def registrar(self, fonte, ok, linhas):
        """Anota o resultado de uma fonte no relatório; ok=False derruba o código de saída."""
        self.relatorio.append((fonte, ok, linhas))
        self.falhas += not ok
        print(f"{fonte}: {'APROVADA' if ok else 'REPROVADA'}", flush=True)
        for l in linhas[:12]:
            print("   " + l[:200], flush=True)


def yaml_str(v):
    return json.dumps("" if v is None else v, ensure_ascii=False)


TAG = re.compile(r"</?[a-zA-Z][a-zA-Z0-9]*(?:\s[^<>]*)?/?>")
LIMITE_BNP = 3900  # o BNP corta 'tese' perto de 4.000 caracteres (temas 905 e 1124 do STJ chegam cortados)


def texto_de_html(s):
    s = s or ""
    for _ in range(2):  # o BNP às vezes entrega o HTML escapado duas vezes (<span style=...> como texto)
        s = re.sub(r"</(?:p|div|li|h\d)>|<br\s*/?>", "\n\n", s, flags=re.I)
        s = html.unescape(TAG.sub("", s))
    return re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t\xa0]+", " ", s)).strip()


def truncada(r):
    return len(r.get("tese") or "") >= LIMITE_BNP


def fold(w):
    """Minúsculas, sem acento e sem pontuação: compara conteúdo e ignora grafia/aspas."""
    w = "".join(c for c in unicodedata.normalize("NFKD", w.casefold()) if not unicodedata.combining(c))
    return re.sub(r"[^0-9a-z]", "", w)


def palavras(s):
    return [p for p in (fold(x) for x in re.sub(r"\s+", " ", s or "").split()) if p]


def iso(d):
    m = re.fullmatch(r"\s*(\d{2})/(\d{2})/(\d{4})\s*", d or "")
    return f"{m[3]}-{m[2]}-{m[1]}" if m else ""


# ------------------------------------------------------------------------------------------- BNP
def bnp_filtro(orgao, tipos, pagina, tam=50):
    return {"buscaGeral": "", "todasPalavras": "", "quaisquerPalavras": "", "semPalavras": "", "trechoExato": "",
            "atualizacaoDesde": "", "atualizacaoAte": "", "cancelados": True, "ordenacao": "Text", "nr": "",
            "pagina": pagina, "tamanhoPagina": tam, "orgaos": [orgao], "tipos": tipos}


def bnp_pagina(c, orgao, tipos, pagina, tam=50):
    corpo = json.dumps({"filtro": bnp_filtro(orgao, tipos, pagina, tam)}).encode()
    status, bruto, info = c.pedir(BNP, corpo, {"Content-Type": "application/json", "Accept": "application/json"})
    if status != 200:
        raise RuntimeError(f"BNP HTTP {status} para {orgao} {tipos}")
    d = json.loads(bruto)
    if not isinstance(d.get("resultados"), list) or not isinstance(d.get("total"), int):
        raise RuntimeError("BNP sem o esquema esperado (resultados/total)")
    return d, bruto


def bnp_todos(c, orgao, tipos):
    """Todos os registros de (órgão, espécies), com as checagens de integridade da paginação."""
    regs, pagina, brutos = [], 1, []
    while True:
        d, bruto = bnp_pagina(c, orgao, tipos, pagina)
        brutos.append(bruto)
        for r in d["resultados"]:
            if r["orgao"] != orgao or r["tipo"] not in tipos:
                raise RuntimeError(f"BNP devolveu registro fora do filtro: {r.get('id')}")
        regs += d["resultados"]
        if not d["resultados"] or len(regs) >= d["total"]:
            break
        pagina += 1
    erros = []
    if len(regs) != d["total"]:
        erros.append(f"BNP informou {d['total']} registros e entregou {len(regs)}")
    ids = [r["id"] for r in regs]
    if len(set(ids)) != len(ids):
        erros.append(f"{len(ids) - len(set(ids))} registro(s) repetido(s) entre páginas")
    nome = f"bnp/{orgao}-{'-'.join(sorted(tipos))}.json"
    c.guardar(nome, json.dumps(regs, ensure_ascii=False).encode(), BNP, {"registros": len(regs)})
    return regs, erros


def vazio_bnp(s):
    t = texto_de_html(s).strip().lower()
    return not t or t in ("não informado", "nao informado")


def enunciado_em_questao(r):
    """No STF (súmulas e súmulas vinculantes) o BNP guarda o enunciado em 'questao' e põe 'não informado' em 'tese'."""
    return r["tipo"] in ("SUM", "SV") and vazio_bnp(r.get("tese")) and not vazio_bnp(r.get("questao"))


def md_bnp(r):
    pasta, prefixo, nome = ESPECIES.get(r["tipo"], (r["tipo"].lower(), r["tipo"].lower(), r["tipo"]))
    titulo = f"{nome} nº {r['nr']} do {r['orgao']}"
    cab = ["---", f"titulo: {yaml_str(titulo)}", f"tribunal: {yaml_str(r['orgao'])}", f"tipo: {yaml_str(nome)}",
           f"numero: {yaml_str(str(r['nr']))}", f"situacao: {yaml_str(r.get('situacao'))}",
           f"atualizacao_fonte: {yaml_str(r.get('ultimaAtualizacao'))}", f"id_bnp: {yaml_str(r['id'])}",
           'versao_texto: "Banco Nacional de Precedentes do CNJ"', f"fonte: {yaml_str(BNP)}",
           f"tese_possivelmente_truncada: {'true' if truncada(r) else 'false'}",
           f"baixado_em: {HOJE}", "---", "", f"# {titulo}", ""]
    if enunciado_em_questao(r):
        cab += ["## Enunciado", "", texto_de_html(r["questao"]), ""]
    else:
        if not vazio_bnp(r.get("questao")):
            cab += ["## Questão", "", texto_de_html(r["questao"]), ""]
        if vazio_bnp(r.get("tese")):
            cab += ["## Tese / enunciado", "", "*Sem tese na fonte.*", ""]
        else:
            cab += ["## Tese / enunciado", "", texto_de_html(r["tese"]), ""]
            if truncada(r):
                cab += [f"> **Atenção:** o BNP limita o texto a cerca de 4.000 caracteres e este registro tem {len(r['tese'])}; "
                        "a tese pode estar cortada no fim. Conferir na fonte do tribunal.", ""]
    cab += [f"**Situação:** {r.get('situacao') or '—'}", "", "## Registro original do CNJ", "", "```json",
            json.dumps(r, ensure_ascii=False, indent=2), "```", ""]
    return pasta, prefixo, "\n".join(cab)


def fonte_bnp(c, orgao, tipos):
    regs, erros = bnp_todos(c, orgao, tipos)
    erros = list(erros)
    for r in regs:
        pasta, prefixo, texto = md_bnp(r)
        c.gravar(f"{orgao.lower()}/{pasta}/{prefixo}-{r['nr']}.md", texto)
    por_pasta = {}
    for r in regs:
        pasta = md_bnp(r)[0]
        corpo = r["questao"] if enunciado_em_questao(r) or vazio_bnp(r.get("tese")) else r["tese"]
        por_pasta.setdefault(pasta, []).append((str(r["nr"]), r.get("situacao") or "—",
                                                re.sub(r"\s+", " ", texto_de_html(corpo))[:150]))
    for pasta, itens in por_pasta.items():
        itens.sort(key=lambda x: (len(x[0]), x[0]))
        c.gravar(f"{orgao.lower()}/{pasta}/INDEX.md", "\n".join(
            [f"# {orgao} — {pasta}: índice", "", f"BNP/CNJ; coleta de {HOJE}.", "",
             "| nº | situação | início do texto |", "|---|---|---|"] +
            [f"| {n} | {s} | {t.replace('|', '/')} |" for n, s, t in itens]) + "\n")
    # releitura: o JSON do arquivo tem de ser idêntico ao registro da API, e a tese tem de estar no texto
    for r in regs:
        pasta, prefixo, _ = md_bnp(r)
        with open(os.path.join(c.saida, orgao.lower(), pasta, f"{prefixo}-{r['nr']}.md"), encoding="utf-8") as f:
            lido = f.read()
        blocos = re.findall(r"```json\n(.*?)\n```", lido, re.S)
        if len(blocos) != 1 or json.loads(blocos[0]) != r:
            erros.append(f"{r['id']}: JSON do arquivo difere do registro da API")
        elif enunciado_em_questao(r):
            if palavras(texto_de_html(r["questao"])) != palavras(lido.split("## Enunciado", 1)[1].split("**Situação:**", 1)[0]):
                erros.append(f"{r['id']}: enunciado do arquivo difere da API")
        else:
            if not vazio_bnp(r.get("questao")) and palavras(texto_de_html(r["questao"])) != palavras(
                    lido.split("## Questão", 1)[1].split("\n## ", 1)[0]):
                erros.append(f"{r['id']}: questão do arquivo difere da API")
            if not vazio_bnp(r.get("tese")) and palavras(texto_de_html(r["tese"])) != palavras(
                    lido.split("## Tese / enunciado", 1)[1].split("**Situação:**", 1)[0].split("> **Atenção:**", 1)[0]):
                erros.append(f"{r['id']}: tese do arquivo difere da API")
    sem_texto = [r["id"] for r in regs if vazio_bnp(r.get("tese")) and vazio_bnp(r.get("questao"))]
    por_sit = {}
    for r in regs:
        por_sit[r.get("situacao")] = por_sit.get(r.get("situacao"), 0) + 1
    cortadas = [r["id"] for r in regs if truncada(r)]
    aviso = [f"AVISO {len(cortadas)} registro(s) com tese possivelmente truncada pelo BNP (limite ~4.000 caracteres): "
             f"{cortadas[:8]}"] if cortadas else []
    sem = [f"AVISO {len(sem_texto)} registro(s) sem texto algum na fonte (tese e questão vazias): {sem_texto[:8]}"] if sem_texto else []
    c.registrar(f"bnp:{orgao}:{','.join(tipos)}", not erros,
                [f"{len(regs)} registros; situações: {por_sit}"] + aviso + sem + erros)
    return regs


def bnp_listar(c, orgaos):
    for o in orgaos:
        d, _ = bnp_pagina(c, o, ["SUM"], 1, 1)
        print(f"{o}: {sum(x['total'] for x in d['aggsEspecies'])} registros; espécies:",
              {x["tipo"]: x["total"] for x in d["aggsEspecies"]})


# ------------------------------------------------------------------------------- STJ: temas (CSV)
TIPOS_TEMAS = {"Tema": ("temas", "tema", "Tema repetitivo"), "IAC": ("iac", "iac", "Incidente de assunção de competência"),
               "SIRDR": ("sirdr", "sirdr", "Suspensão em IRDR"), "PUIL": ("puil", "puil", "Pedido de uniformização de interpretação de lei")}
CAMPOS_TOPO = ("sequencialPrecedente", "tipoPrecedente", "numeroPrecedente", "situacao", "questaoSubmetidaAJulgamento",
               "teseFirmada")


def dicionario_temas(bruto):
    saida = {}
    for linha in bruto.decode("utf-8-sig").splitlines()[1:]:
        partes = linha.split(";", 2)
        if len(partes) == 3:
            saida[partes[0].strip()] = partes[1].strip()
    return saida


def alfanum(s):
    return "".join(palavras(s))


def sem_tese(t):
    t = (t or "").strip()
    return not t or t.startswith("*Aguardando")


def comparar_com_bnp(linha_csv, b):
    """(situação confere?, classe da tese). O BNP fala 'Transitado em julgado' onde o CSV fala 'Trânsito em Julgado'."""
    chave = lambda s: alfanum(s).replace("transitado", "transito")  # noqa: E731
    ca, cb = chave(linha_csv["situacao"]), chave(b.get("situacao"))
    situacao_ok = ca == cb or ca.startswith(cb) or cb.startswith(ca)
    tese_b = texto_de_html(b.get("tese") or "")
    # só os caracteres alfanuméricos: o CSV e o BNP divergem em espaço depois de ':' e ')'
    a, bb = alfanum(linha_csv["teseFirmada"]), alfanum(tese_b)
    if a == bb:
        classe = "igual"
    elif sem_tese(linha_csv["teseFirmada"]) or sem_tese(tese_b):
        classe = "uma fonte sem tese"
    elif a.startswith(bb) and truncada(b):
        classe = "BNP truncado"
    else:
        classe = "diferente"
    return situacao_ok, classe


def fonte_stj_temas(c):
    status, bruto, _ = c.pedir(CKAN)
    pacote = json.loads(bruto)["result"]
    c.guardar("stj/ckan-precedentes-qualificados.json", bruto, CKAN)
    rec = {r["name"].lower(): r for r in pacote["resources"]}
    arqs = {}
    for nome in ("temas.csv", "dicionario-temas.csv"):
        st, b, info = c.pedir(rec[nome]["url"])
        if st != 200:
            raise RuntimeError(f"HTTP {st}: {rec[nome]['url']}")
        c.guardar("stj/" + nome, b, rec[nome]["url"], {"fonte_atualizada_em": rec[nome].get("last_modified")})
        arqs[nome] = b
    rotulos = dicionario_temas(arqs["dicionario-temas.csv"])
    # valores com quebra de linha entre aspas exigem newline="" na leitura
    linhas = list(csv.DictReader(io.StringIO(arqs["temas.csv"].decode("utf-8-sig"), newline="")))
    if not linhas or "tipoPrecedente" not in linhas[0]:
        raise RuntimeError("CSV de temas sem o esquema esperado")
    grupos, ignorados = {}, {}
    for l in linhas:
        if l["tipoPrecedente"] in TIPOS_TEMAS:
            if not l["numeroPrecedente"].isdigit():
                raise RuntimeError(f"precedente sem número válido: {l['sequencialPrecedente']}")
            grupos.setdefault((l["tipoPrecedente"], l["numeroPrecedente"]), []).append(l)
        else:
            ignorados[l["tipoPrecedente"] or "(sem tipo)"] = ignorados.get(l["tipoPrecedente"] or "(sem tipo)", 0) + 1
    atualizado = rec["temas.csv"].get("last_modified")
    erros, info = [], []
    try:  # segunda fonte (repetitivos do STJ no BNP); sem ela a coleta sai reprovada, mas os arquivos são gravados
        regs_bnp, e_bnp = bnp_todos(c, "STJ", ["RR"])
        erros += e_bnp
    except Exception as e:
        regs_bnp = []
        erros.append(f"conferência com o BNP não realizada: {e}")
    bnp = {int(r["nr"]): r for r in regs_bnp}
    indice = {k: [] for k in TIPOS_TEMAS}
    for (tipo, numero), hist in sorted(grupos.items(), key=lambda kv: (kv[0][0], int(kv[0][1]))):
        pasta, prefixo, nome = TIPOS_TEMAS[tipo]
        hist.sort(key=lambda r: int(r["sequencialPrecedente"]), reverse=True)
        atual = hist[0]
        tese = (atual["teseFirmada"] or "").strip()
        tese_publicada = bool(tese) and not tese.startswith("*Aguardando")
        titulo = f"{nome} nº {numero} do STJ"
        cab = ["---", f"titulo: {yaml_str(titulo)}", 'tribunal: "STJ"', f"tipo: {yaml_str(nome)}",
               f"numero: {yaml_str(numero)}", f"situacao: {yaml_str(atual['situacao'])}",
               f"data_julgamento: {atual['dataJulgamento']}", f"data_publicacao_acordao: {atual['dataPublicacaoAcordao']}",
               f"tese_publicada: {'true' if tese_publicada else 'false'}", f"orgao_julgador: {yaml_str(atual['orgaoJulgador'])}",
               'versao_texto: "dados abertos do STJ (Precedentes qualificados, Temas.csv)"',
               f"fonte: {yaml_str(rec['temas.csv']['url'])}", f"fonte_atualizada_em: {yaml_str(atualizado)}",
               f"baixado_em: {HOJE}", "---", "", f"# {titulo}", "", f"**Situação:** {atual['situacao']}", ""]
        for campo, rotulo in (("questaoSubmetidaAJulgamento", "Questão submetida a julgamento"), ("teseFirmada", "Tese firmada")):
            cab += [f"## {rotulo}", "", texto_de_html(atual[campo]) if atual[campo].strip() else "*Sem conteúdo na fonte.*", ""]
        b = bnp.get(int(numero)) if tipo == "Tema" else None
        if b:
            situacao_ok, classe = comparar_com_bnp(atual, b)
            avisos = []
            if not situacao_ok:
                avisos.append(f"- Situação no BNP/CNJ: **{b['situacao']}** (atualização {b.get('ultimaAtualizacao')}); "
                              f"no CSV: {atual['situacao']}. O BNP costuma estar à frente do CSV: conferir no site do STJ.")
            if classe == "uma fonte sem tese" and not sem_tese(texto_de_html(b.get("tese") or "")):
                avisos.append("- O BNP/CNJ já traz tese e o CSV não:\n\n  " + texto_de_html(b["tese"]).replace("\n", "\n  "))
            if classe == "diferente":
                avisos.append("- A tese do BNP/CNJ difere da do CSV; conferir no site do STJ.")
            if avisos:
                cab += ["## Divergência com o BNP/CNJ", ""] + avisos + [""]
        resto = [(k, v) for k, v in atual.items() if v.strip() and k not in CAMPOS_TOPO]
        if resto:
            cab += ["## Demais campos da fonte", ""]
            for k, v in resto:
                cab += [f"### {rotulos.get(k, k)}", "", texto_de_html(v), ""]
        if len(hist) > 1:
            cab += [f"## Registros anteriores ({len(hist) - 1})", ""]
            cab += [f"- sequencial {h['sequencialPrecedente']}: {h['situacao']} (julgamento {h['dataJulgamento'] or '—'})" for h in hist[1:]] + [""]
        cab += ["## Registro original (CSV)", ""]
        for h in hist:
            cab += ["```json", json.dumps(h, ensure_ascii=False, indent=2), "```", ""]
        c.gravar(f"stj/{pasta}/{prefixo}-{numero}.md", "\n".join(cab))
        indice[tipo].append((numero, atual["situacao"], atual["dataJulgamento"], tese_publicada,
                             re.sub(r"\s+", " ", texto_de_html(atual["questaoSubmetidaAJulgamento"]))[:150]))
    for tipo, itens in indice.items():
        if itens:
            pasta = TIPOS_TEMAS[tipo][0]
            l = [f"# STJ — {TIPOS_TEMAS[tipo][2]}: índice", "", f"Fonte: {rec['temas.csv']['url']} (atualizada em {atualizado}); "
                 f"coleta de {HOJE}.", "", "| nº | situação | julgamento | tese | questão |", "|---|---|---|---|---|"]
            l += [f"| {n} | {s} | {d or '—'} | {'sim' if t else 'não'} | {q.replace('|', '/')} |" for n, s, d, t, q in itens]
            c.gravar(f"stj/{pasta}/INDEX.md", "\n".join(l) + "\n")

    # --- conferência ---
    for (tipo, numero), hist in grupos.items():
        pasta, prefixo, _ = TIPOS_TEMAS[tipo]
        with open(os.path.join(c.saida, "stj", pasta, f"{prefixo}-{numero}.md"), encoding="utf-8") as f:
            lido = f.read()
        blocos = [json.loads(b) for b in re.findall(r"```json\n(.*?)\n```", lido, re.S)]
        esperado = sorted(hist, key=lambda r: int(r["sequencialPrecedente"]), reverse=True)
        if blocos != esperado:
            erros.append(f"{tipo} {numero}: JSON do arquivo difere das linhas do CSV")
    total_linhas = sum(len(h) for h in grupos.values())
    info.append(f"{len(grupos)} precedentes ({total_linhas} linhas do CSV) gravados; fora do escopo: {ignorados}")
    # segunda fonte: BNP (repetitivos do STJ)
    csv_temas = {int(n): hist[0] for (t, n), hist in grupos.items() if t == "Tema"}
    so_csv, so_bnp = sorted(set(csv_temas) - set(bnp)), sorted(set(bnp) - set(csv_temas))
    info.append(f"BNP tem {len(bnp)} repetitivos; só no CSV: {len(so_csv)} {so_csv[:8]}; só no BNP: {len(so_bnp)} {so_bnp[:8]}")
    classes, dif_situacao = {"igual": [], "uma fonte sem tese": [], "BNP truncado": [], "diferente": []}, []
    for n in sorted(set(csv_temas) & set(bnp)):
        situacao_ok, classe = comparar_com_bnp(csv_temas[n], bnp[n])
        classes[classe].append(n)
        if not situacao_ok:
            dif_situacao.append((n, csv_temas[n]["situacao"], bnp[n]["situacao"]))
    info.append(f"tese CSV x BNP: igual={len(classes['igual'])}; BNP truncado (CSV completo)={len(classes['BNP truncado'])} "
                f"{classes['BNP truncado']}; só uma fonte tem tese={len(classes['uma fonte sem tese'])} "
                f"{classes['uma fonte sem tese'][:8]}; DIFERENTE={len(classes['diferente'])} {classes['diferente'][:8]}")
    info.append(f"situação diferente entre CSV e BNP: {len(dif_situacao)} {dif_situacao[:5]} (o BNP costuma estar à frente)")
    if classes["diferente"]:
        erros.append(f"tese com conteúdo diferente entre CSV e BNP: {classes['diferente'][:10]}")
    c.registrar("stj-temas", not erros, info + erros)
    return grupos


def conferir_acervo_temas(c, grupos, pasta_acervo):
    """Compara a situação oficial com o que cada ficha do acervo declara. Não altera o acervo."""
    linhas = ["| tema | situação oficial | tese publicada | ficha do acervo menciona a situação? |", "|---|---|---|---|"]
    for nome in sorted(os.listdir(pasta_acervo)):
        m = re.fullmatch(r"tema-(\d+)-stj\.md", nome)
        if not m or ("Tema", m[1]) not in grupos:
            continue
        atual = max(grupos[("Tema", m[1])], key=lambda r: int(r["sequencialPrecedente"]))
        with open(os.path.join(pasta_acervo, nome), encoding="utf-8") as f:
            ficha = fold(f.read())
        sit = atual["situacao"]
        casa = fold(sit) in ficha or fold(sit.replace("Trânsito em Julgado", "trânsito em julgado")) in ficha
        tese = bool(atual["teseFirmada"].strip()) and not atual["teseFirmada"].startswith("*Aguardando")
        linhas.append(f"| {m[1]} | {sit} | {'sim' if tese else 'não'} | {'sim' if casa else 'NÃO — conferir'} |")
    c.relatorio.append(("conferência do acervo", True, linhas))
    print("\n".join(linhas))


# ---------------------------------------------------------------------- STJ: súmulas (BNP + PDF)
ROTULOS_CADERNO = ("Enunciado", "Órgão Julgador", "Data da Decisão", "Fonte", "Referências Legislativas",
                   "Excerto dos Precedentes Originários")


def pdf_para_texto(caminho):
    with tempfile.TemporaryDirectory() as tmp:
        saida = os.path.join(tmp, "saida.txt")
        subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", caminho, saida], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with open(saida, encoding="utf-8") as f:  # estrito: um U+FFFD aqui seria perda de acento
            return f.read()


def ler_caderno(texto):
    texto = texto.replace("\x0c", "")
    texto = re.sub(r"^[ \t]*P[áa]gina \d+ de \d+[ \t]*$\n?", "", texto, flags=re.M)
    texto = re.sub(r"^[ \t]*Súmulas do Superior Tribunal de Justiça[ \t]*$\n?", "", texto, flags=re.M)
    marcas = [(m.start(), int(m[1])) for m in re.finditer(r"^[ \t]*Súmula[ \t]+(\d+)[ \t]*$", texto, re.M)]
    blocos = {}
    for i, (pos, n) in enumerate(marcas):
        if n in blocos:
            raise RuntimeError(f"súmula {n} aparece duas vezes no caderno")
        blocos[n] = texto[pos:marcas[i + 1][0] if i + 1 < len(marcas) else len(texto)]
    saida = {}
    for n, b in blocos.items():
        achados = {}
        for rot in ROTULOS_CADERNO:
            m = re.search(r"^[ \t]*" + re.escape(rot) + r"[ \t]*$", b, re.M)
            if m:
                achados[rot] = m
        ordem = sorted(achados.items(), key=lambda kv: kv[1].start())
        campos = {}
        for k, (rot, m) in enumerate(ordem):
            fim = ordem[k + 1][1].start() if k + 1 < len(ordem) else len(b)
            campos[rot] = b[m.end():fim].strip()
        campos["_assunto"] = b[:achados["Enunciado"].start()].split("\n", 1)[-1].strip() if "Enunciado" in achados else ""
        saida[n] = campos
    return saida


def separar_notas(secao, texto_bnp):
    """Divide a seção 'Enunciado' do caderno em (enunciado, notas) usando o texto do BNP como régua."""
    alvo = palavras(texto_bnp)
    n, fim = 0, None
    for m in re.finditer(r"\S+", secao):
        w = fold(m.group())
        if not w:
            continue  # '(*)', '.', '-' soltos
        if n >= len(alvo) or w != alvo[n]:
            break
        n += 1
        if n == len(alvo):
            fim = m.end()
            break
    if fim is None:  # o texto do BNP não é prefixo da seção: divergência de conteúdo
        return re.sub(r"\s+", " ", secao).strip(), [], False
    resto = re.sub(r"^[\s().*\-]+", "", secao[fim:])  # tira a marca '(*)' que fecha o enunciado
    return re.sub(r"\s+", " ", secao[:fim]).strip(), ([re.sub(r"\s+", " ", resto).strip()] if resto.strip() else []), True


def fonte_stj_sumulas(c, excertos=False):
    regs, erros = bnp_todos(c, "STJ", ["SUM"])
    erros = list(erros)
    bnp = {int(r["nr"]): r for r in regs}
    maximo = max(bnp)
    if sorted(bnp) != list(range(1, maximo + 1)):
        erros.append(f"BNP com lacuna na numeração: {[n for n in range(1, maximo + 1) if n not in bnp][:10]}")
    status, bruto, info = c.pedir(CADERNO_STJ, timeout=300)
    if status != 200 or not bruto.startswith(b"%PDF"):
        raise RuntimeError(f"caderno do STJ indisponível (HTTP {status})")
    pdf = c.guardar("stj/SumulasSTJ.pdf", bruto, CADERNO_STJ, info)
    caderno = ler_caderno(pdf_para_texto(pdf))
    ultimo_caderno = max(caderno)
    if sorted(caderno) != list(range(1, ultimo_caderno + 1)):
        erros.append("caderno com lacuna na numeração")
    for n, campos in caderno.items():
        faltam = [r for r in ("Enunciado", "Órgão Julgador", "Data da Decisão", "Fonte") if r not in campos]
        if faltam:
            erros.append(f"súmula {n}: campos ausentes no caderno {faltam}")
        elif re.search(r"P[áa]gina \d+ de \d+", campos["Enunciado"]):
            erros.append(f"súmula {n}: rodapé de página dentro do enunciado")
    linhas_info = [f"BNP: {len(bnp)} súmulas (1 a {maximo}); caderno: 1 a {ultimo_caderno}, "
                   f"Last-Modified {info.get('last_modified')}, última decisão "
                   f"{iso(caderno[ultimo_caderno].get('Data da Decisão'))}"]
    if ultimo_caderno < maximo:
        linhas_info.append(f"AVISO caderno defasado: faltam as súmulas {ultimo_caderno + 1} a {maximo} "
                           "(data da decisão, órgão e publicação não constam das fontes; só texto e situação do BNP)")
    iguais = cosmeticas = reais = 0
    cosmeticas_l, reais_l, so_pdf_canc, so_bnp_canc = [], [], [], []
    indice = []
    for n in sorted(bnp):
        r = bnp[n]
        tese = texto_de_html(r["tese"])
        cad = caderno.get(n)
        notas, diverg = [], None
        if cad and "Enunciado" in cad:
            texto_pdf, notas, confere = separar_notas(cad["Enunciado"], tese)
            if confere and re.sub(r"\s+", " ", texto_pdf).strip() == re.sub(r"\s+", " ", tese).strip():
                iguais += 1
            elif confere:
                cosmeticas += 1
                cosmeticas_l.append(n)
                diverg = ("Grafia diferente no caderno do STJ (caixa, acento ou pontuação); o texto acima é o do BNP", texto_pdf)
            else:
                reais += 1
                reais_l.append(n)
                diverg = ("DIVERGÊNCIA DE CONTEÚDO entre o BNP e o caderno do STJ; conferir no site do STJ", texto_pdf)
        canc_pdf = any(re.search(r"CANCELAMENTO\s+d[ao]\s+s[úu]mula", p, re.I) for p in notas)
        canc_bnp = r["situacao"] != "Vigente"
        if canc_pdf and not canc_bnp:
            erros.append(f"súmula {n}: caderno registra cancelamento e o BNP a dá como '{r['situacao']}'")
        if canc_bnp and cad and not canc_pdf:
            so_bnp_canc.append(n)
        data = iso(cad.get("Data da Decisão")) if cad else ""
        titulo = f"Súmula nº {n} do STJ"
        cab = ["---", f"titulo: {yaml_str(titulo)}", 'tribunal: "STJ"', 'tipo: "Súmula"', f"numero: {yaml_str(str(n))}",
               f"situacao: {yaml_str(r['situacao'])}", f"data_decisao: {data}",
               f"orgao_julgador: {yaml_str(re.sub(chr(10), ' ', cad['Órgão Julgador']) if cad else '')}",
               f"revogada: {'true' if canc_bnp else 'false'}",
               'versao_texto: "texto e situação: BNP/CNJ; data, órgão, publicação e histórico: caderno do STJ"',
               f"fonte: {yaml_str(BNP)}", f"fonte_caderno: {yaml_str(CADERNO_STJ if cad else '')}",
               f"baixado_em: {HOJE}", "---", "", f"# {titulo}", ""]
        if cad and cad.get("_assunto"):
            cab += [f"*{re.sub(chr(10), ' ', cad['_assunto'])}*", ""]
        cab += [f"**Situação:** {r['situacao']} (BNP/CNJ, atualização {r.get('ultimaAtualizacao')})", "", "## Enunciado", "", tese, ""]
        if cad:
            cab += ["## Dados do julgamento (caderno do STJ)", "",
                    f"- Órgão julgador: {re.sub(chr(10), ' ', cad['Órgão Julgador'])}",
                    f"- Data da decisão: {cad['Data da Decisão']}",
                    f"- Publicação: {'; '.join(x.strip() for x in cad['Fonte'].splitlines() if x.strip())}"]
            if cad.get("Referências Legislativas"):
                cab += ["- Referências legislativas (codificação do STJ):", "", "  ```text"] + [
                    "  " + x for x in cad["Referências Legislativas"].splitlines() if x.strip()] + ["  ```"]
            cab += [""]
        else:
            cab += ["## Dados do julgamento", "", f"Súmula posterior ao caderno do STJ de {info.get('last_modified') or '2021'}: "
                    "data da decisão, órgão e publicação não constam das fontes consultadas.", ""]
        if notas:
            cab += ["## Histórico de redação (notas do caderno do STJ)", ""] + [f"> {p}" for p in notas] + [""]
        if diverg:
            cab += ["## Divergência com o caderno", "", diverg[0] + ".", "", f"Caderno: {diverg[1]}", ""]
        if excertos and cad and cad.get("Excerto dos Precedentes Originários"):
            cab += ["## Excerto dos precedentes originários (caderno do STJ)", "", cad["Excerto dos Precedentes Originários"], ""]
        cab += ["## Registro original do CNJ", "", "As datas de `historico` descrevem a admissão do registro no BNP, "
                "não o julgamento da súmula.", "", "```json", json.dumps(r, ensure_ascii=False, indent=2), "```", ""]
        c.gravar(f"stj/sumulas/sumula-{n}.md", "\n".join(cab))
        indice.append((n, r["situacao"], data, re.sub(r"\s+", " ", tese)[:150]))
    c.gravar("stj/sumulas/INDEX.md", "\n".join(
        ["# STJ — Súmulas: índice", "", f"Texto e situação: BNP/CNJ; data: caderno do STJ (até a súmula {ultimo_caderno}). Coleta de {HOJE}.",
         "", "| nº | situação | decisão | enunciado |", "|---|---|---|---|"] +
        [f"| {n} | {s} | {d or '—'} | {e.replace('|', '/')} |" for n, s, d, e in indice]) + "\n")
    # releitura dos arquivos: o enunciado gravado tem de ser o do BNP
    for n in bnp:
        with open(os.path.join(c.saida, "stj", "sumulas", f"sumula-{n}.md"), encoding="utf-8") as f:
            lido = f.read()
        gravado = lido.split("## Enunciado", 1)[1].split("\n## ", 1)[0]
        if palavras(gravado) != palavras(texto_de_html(bnp[n]["tese"])):
            erros.append(f"súmula {n}: enunciado gravado difere do BNP")
    linhas_info.append(f"texto PDF x BNP: idêntico={iguais}; só grafia/aspas/pontuação={cosmeticas}; CONTEÚDO DIFERENTE={reais} {reais_l[:10]}")
    if cosmeticas_l:
        linhas_info.append(f"  grafia diferente no caderno (BNP prevalece): {cosmeticas_l[:12]}")
    linhas_info.append(f"canceladas no BNP sem nota de cancelamento no caderno: {len(so_bnp_canc)} {so_bnp_canc[:12]} "
                       "(canceladas depois do caderno ou nota com outra redação)")
    if reais:
        erros.append(f"{reais} súmula(s) com conteúdo diferente entre BNP e caderno: {reais_l[:10]}")
    c.registrar("stj-sumulas", not erros, linhas_info + erros)
    return bnp


# -------------------------------------------------------------------------------------------- CLI
# --------------------------------------------------------------------------- STF: súmulas (BNP + PDF)
CADERNO_STF = ("https://www.stf.jus.br/arquivo/cms/jurisprudenciaSumula/anexo/"
               "Enunciados_Sumulas_STF_1_a_736_Completo.pdf")
MARCA_STF = re.compile(r"\s*\((Revogada|Cancelada|Superada)\)\s*$")
FIM_STF = re.compile(r"\s*(\((?:Revogada|Cancelada|Superada)\)|\(\d{1,2}\))\s*$")  # marca de situação ou nº de nota
SITUACAO_STF = {"APROVADO": "Vigente", "Cancelado": "Cancelada", "Superado": "Superada", "ALTERADO": "Alterada"}
SO_NAO_VIGENTES_STF = {"Cancelada", "Revogada", "Superada"}
# Divergências de conteúdo entre o BNP e o caderno, lidas uma a uma em 30/10/2026: vale o texto do caderno.
# Divergência nova, fora desta lista, reprova a coleta.
DIVERGENCIAS_STF = {
    6: "o BNP traz 'antes de 7 por aquele Tribunal' onde o caderno traz 'antes de aprovada por aquele Tribunal'",
    534: "o BNP traz 'Ddecreto-lei' onde o caderno traz 'Decreto-lei'",
}
ROTULOS_STF = (("data", r"Data de Aprovação[ \t]*$"), ("fonte", r"Fonte de Publicação[ \t]*$"),
               ("referencia", r"Referência Legislativa[ \t]*$"), ("precedentes", r"Precedentes\b.*$"),
               ("observacao", r"Observação[ \t]*$"))


def sem_marcas_stf(t):
    while True:
        novo = FIM_STF.sub("", t)
        if novo == t:
            return t.strip()
        t = novo


def ler_caderno_stf(texto):
    """-> ({número: campos}, 'Atualizado em ...'). Entrada do sumário (sem 'Data de Aprovação') é descartada."""
    atualizado = (re.search(r"Atualizado em ([^\n]+)", texto) or [None, ""])[1].strip()
    texto = texto.replace("\x0c", "")
    texto = re.sub(r"^[ \t]*\d{1,4}[ \t]*$\n?", "", texto, flags=re.M)  # número de página solto
    marcas = [(m.start(), int(m[1])) for m in re.finditer(r"^[ \t]*SÚMULA[ \t]+(\d+)[ \t]*$", texto, re.M)]
    blocos = {}
    for i, (pos, n) in enumerate(marcas):
        b = texto[pos:marcas[i + 1][0] if i + 1 < len(marcas) else len(texto)]
        if not re.search(r"^[ \t]*Data de Aprovação[ \t]*$", b, re.M):
            continue
        if n in blocos:
            raise RuntimeError(f"súmula {n} com dois blocos completos no caderno")
        blocos[n] = b
    saida = {}
    for n, b in blocos.items():
        achados = {}
        for nome, pat in ROTULOS_STF:
            m = re.search(r"^[ \t]*" + pat, b, re.M)
            if m:
                achados[nome] = m
        if "data" not in achados or "fonte" not in achados:
            raise RuntimeError(f"súmula {n}: campos ausentes no caderno {sorted({'data', 'fonte'} - set(achados))}")
        ordem = sorted(achados.items(), key=lambda kv: kv[1].start())
        if ordem[0][0] != "data":
            raise RuntimeError(f"súmula {n}: o primeiro campo do caderno não é a data de aprovação")
        campos = {"_enunciado": re.sub(r"\s+", " ", b[:ordem[0][1].start()].split("\n", 1)[1]).strip()}
        for k, (nome, m) in enumerate(ordem):
            fim = ordem[k + 1][1].start() if k + 1 < len(ordem) else len(b)
            campos[nome] = b[(m.start() + len("Precedentes")) if nome == "precedentes" else m.end():fim].strip()
        saida[n] = campos
    return saida, atualizado


def fonte_stf_sumulas(c, excertos=False):
    regs, erros = bnp_todos(c, "STF", ["SUM"])
    erros = list(erros)
    bnp = {int(r["nr"]): r for r in regs}
    status, bruto, info = c.pedir(CADERNO_STF, timeout=300)
    if status != 200 or not bruto.startswith(b"%PDF"):
        raise RuntimeError(f"caderno do STF indisponível (HTTP {status})")
    pdf = c.guardar("stf/SumulasSTF.pdf", bruto, CADERNO_STF, info)
    caderno, atualizado = ler_caderno_stf(pdf_para_texto(pdf))
    ultimo = max(caderno)
    if sorted(caderno) != list(range(1, ultimo + 1)):
        erros.append(f"caderno com lacuna na numeração: {[n for n in range(1, ultimo + 1) if n not in caderno][:10]}")
    maximo = max(ultimo, max(bnp))
    linhas_info = [f"BNP: {len(bnp)} súmulas; caderno do STF: 1 a {ultimo} ({atualizado}; Last-Modified {info.get('last_modified')})"]
    iguais, conhecidas, reais, so_cad, so_bnp, status_bnp, indice = 0, [], [], [], [], [], []
    for n in range(1, maximo + 1):
        cad, r = caderno.get(n), bnp.get(n)
        if cad is None and r is None:
            erros.append(f"súmula {n}: em nenhuma das fontes")
            continue
        marca = MARCA_STF.search(cad["_enunciado"]) if cad else None
        enun_cad = MARCA_STF.sub("", cad["_enunciado"]).strip() if cad else None
        texto_bnp = sem_marcas_stf(texto_de_html(r["questao"]).replace('""', '"')) if r else None
        diverg = None
        if cad and r:
            if alfanum(enun_cad) == alfanum(texto_bnp):
                iguais += 1
                texto = texto_bnp
            else:
                texto = enun_cad
                if n in DIVERGENCIAS_STF:
                    conhecidas.append(n)
                    diverg = (f"{DIVERGENCIAS_STF[n]}. Vale o caderno", texto_bnp)
                else:
                    reais.append(n)
                    diverg = ("DIVERGÊNCIA DE CONTEÚDO entre o BNP e o caderno do STF; conferir no site do STF", texto_bnp)
        elif r:
            texto = texto_bnp
            so_bnp.append(n)
        else:
            texto = enun_cad
            so_cad.append(n)
        sit_bnp = r["situacao"] if r else None
        if r:
            situacao = SITUACAO_STF.get(sit_bnp, sit_bnp)
        elif marca:
            situacao = marca[1]
        else:
            situacao = "Sem situação no BNP; o caderno de 2017 não a marca como revogada"
        if marca and sit_bnp == "APROVADO":
            erros.append(f"súmula {n}: o caderno a marca '{marca[1]}' e o BNP a dá como APROVADO")
        if r and sit_bnp != "APROVADO" and not marca:
            status_bnp.append((n, sit_bnp))
        revogada = situacao in SO_NAO_VIGENTES_STF
        data = ""
        if cad:
            m = re.search(r"(\d{2})/(\d{2})/(\d{4})", cad["data"])
            data = f"{m[3]}-{m[2]}-{m[1]}" if m else ""
            if not data:
                erros.append(f"súmula {n}: data de aprovação ilegível no caderno")
        titulo = f"Súmula nº {n} do STF"
        cab = ["---", f"titulo: {yaml_str(titulo)}", 'tribunal: "STF"', 'tipo: "Súmula"', f"numero: {yaml_str(str(n))}",
               f"situacao: {yaml_str(situacao)}", f"situacao_bnp: {yaml_str(sit_bnp)}", f"data_aprovacao: {data}",
               f"revogada: {'true' if revogada else 'false'}",
               'versao_texto: "texto e situação: BNP/CNJ e caderno oficial do STF (cruzados); dados do julgamento: caderno"',
               f"fonte: {yaml_str(BNP if r else CADERNO_STF)}", f"fonte_caderno: {yaml_str(CADERNO_STF if cad else '')}",
               f"baixado_em: {HOJE}", "---", "", f"# {titulo}", "", f"**Situação:** {situacao}"
               + (f" (BNP/CNJ: {sit_bnp}, atualização {r.get('ultimaAtualizacao')})" if r else " (só no caderno do STF)"), "",
               "## Enunciado", "", texto, ""]
        if cad:
            cab += [f"## Dados da súmula (caderno do STF, {atualizado.lower()})", "",
                    f"- Aprovação: {re.sub(chr(10), ' ', cad['data'])}",
                    f"- Publicação: {'; '.join(x.strip() for x in cad['fonte'].splitlines() if x.strip())}"]
            if cad.get("referencia"):
                cab += ["- Referência legislativa:", "", "  ```text"] + [
                    "  " + x.strip() for x in cad["referencia"].splitlines() if x.strip()] + ["  ```"]
            cab += [""]
            if cad.get("observacao"):
                cab += ["## Observação (caderno do STF)", "", "> " + re.sub(r"\s+", " ", cad["observacao"]), ""]
        else:
            cab += ["## Dados da súmula", "", "Súmula posterior ao caderno do STF; data, publicação e referências não constam "
                    "das fontes consultadas.", ""]
        if diverg:
            cab += ["## Divergência com o BNP/CNJ", "", diverg[0] + ".", "", f"BNP: {diverg[1]}", ""]
        if excertos and cad and cad.get("precedentes"):
            cab += ["## Precedentes (caderno do STF)", "", cad["precedentes"], ""]
        if r:
            cab += ["## Registro original do CNJ", "", "```json", json.dumps(r, ensure_ascii=False, indent=2), "```", ""]
        c.gravar(f"stf/sumulas/sumula-{n}.md", "\n".join(cab))
        indice.append((n, situacao, data, re.sub(r"\s+", " ", texto)[:150], texto))
    c.gravar("stf/sumulas/INDEX.md", "\n".join(
        ["# STF — Súmulas: índice", "", f"Texto e situação: BNP/CNJ cruzado com o caderno do STF ({atualizado}). Coleta de {HOJE}.",
         "", "| nº | situação | aprovação | enunciado |", "|---|---|---|---|"] +
        [f"| {n} | {s} | {d or '—'} | {e.replace('|', '/')} |" for n, s, d, e, _ in indice]) + "\n")
    for n, _s, _d, _e, texto in indice:  # releitura: o enunciado gravado é o esperado
        with open(os.path.join(c.saida, "stf", "sumulas", f"sumula-{n}.md"), encoding="utf-8") as f:
            gravado = f.read().split("## Enunciado", 1)[1].split("\n## ", 1)[0]
        if palavras(gravado) != palavras(texto):
            erros.append(f"súmula {n}: enunciado gravado difere do esperado")
    linhas_info.append(f"texto caderno x BNP: idêntico={iguais}; divergência conhecida (vale o caderno)={len(conhecidas)} {conhecidas}; "
                       f"DIVERGENTE NOVA={len(reais)} {reais[:10]}")
    linhas_info.append(f"só no caderno (revogadas que o BNP não lista): {len(so_cad)} {so_cad[:10]}; só no BNP: {len(so_bnp)} {so_bnp[:10]}")
    linhas_info.append(f"BNP não vigente sem marca no caderno (posterior a '{atualizado}' ou nota diferente): {status_bnp}")
    if reais:
        erros.append(f"{len(reais)} súmula(s) com conteúdo diferente entre BNP e caderno: {reais[:10]}")
    c.registrar("stf-sumulas", not erros, linhas_info + erros)
    return bnp


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fontes", nargs="*", help="stj-temas | stj-sumulas | stf-sumulas | stf | bnp:ORGAO:TIPO[,TIPO]")
    ap.add_argument("--saida", help="pasta de saída (não use _acervo/jurisprudencia sem comparar antes)")
    ap.add_argument("--rps", type=float, default=1)
    ap.add_argument("--excertos", action="store_true", help="inclui o excerto dos precedentes originários das súmulas do STJ")
    ap.add_argument("--conferir-acervo", metavar="PASTA", help="confere as fichas tema-N-stj.md da pasta com o CSV do STJ")
    ap.add_argument("--bnp-listar", nargs="+", metavar="ORGAO", help="mostra as espécies do BNP por órgão e sai")
    a = ap.parse_args()
    if a.bnp_listar:
        bnp_listar(Coleta(tempfile.gettempdir(), a.rps), a.bnp_listar)
        return 0
    if not a.saida or not a.fontes:
        ap.error("informe --saida e ao menos uma fonte")
    c = Coleta(a.saida, a.rps)
    os.makedirs(a.saida, exist_ok=True)
    for f in a.fontes:
        try:
            if f == "stj-temas":
                grupos = fonte_stj_temas(c)
                if a.conferir_acervo:
                    conferir_acervo_temas(c, grupos, a.conferir_acervo)
            elif f == "stj-sumulas":
                fonte_stj_sumulas(c, a.excertos)
            elif f == "stf-sumulas":
                fonte_stf_sumulas(c, a.excertos)
            elif f == "stf":  # súmulas (BNP + caderno), súmulas vinculantes e repercussão geral (BNP)
                fonte_stf_sumulas(c, a.excertos)
                fonte_bnp(c, "STF", ["SV", "RG"])
            elif f.startswith("bnp:"):
                _, orgao, tipos = f.split(":")
                fonte_bnp(c, orgao.upper(), [t.upper() for t in tipos.split(",")])
            else:
                ap.error(f"fonte desconhecida: {f}")
        except Exception as e:
            c.registrar(f, False, [f"erro: {e}"])
    c.gravar("_fonte/manifesto.json", json.dumps(c.manifesto, ensure_ascii=False, indent=2))
    rel = [f"# Relatório da coleta de {HOJE}", ""]
    for fonte, ok, linhas in c.relatorio:
        rel += [f"## {fonte}: {'APROVADA' if ok else 'REPROVADA'}", ""] + [f"- {l}" if not l.startswith("|") else l for l in linhas] + [""]
    c.gravar("RELATORIO.md", "\n".join(rel))
    return 1 if c.falhas else 0


if __name__ == "__main__":
    sys.exit(main())
