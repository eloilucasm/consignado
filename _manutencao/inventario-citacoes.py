#!/usr/bin/env python3
"""inventario-citacoes.py - inventário estático das citações jurídicas das skills de iniciais.

Só lê: faz ast.parse nos gerar.py (sem executá-los) e abre os .docx como zip. Não grava nada
além do relatório indicado em --saida.

Para cada citação encontrada (súmula, tema, acórdão, artigo, resolução, IN, lei) informa onde
aparece (arquivo:linha) e se o texto da citação consta dos arquivos de referência conferidos
(--refs). O teste é textual e aproximado: CONFERIDA = a citação normalizada aparece nas
referências; FORA = não aparece e precisa de fonte ou [VERIFICAR]. Revisão humana obrigatória.

Uso:
    python3 inventario-citacoes.py --pacote <pasta amn-iniciais-consignado> \
        --refs <pasta references do recurso> --saida INVENTARIO-ARGUMENTOS.md
"""
import argparse
import ast
import re
import sys
import unicodedata
import zipfile
from collections import defaultdict
from pathlib import Path

PADROES = [
    ("Súmula", re.compile(r"S[úu]mulas?\s+(?:n[ºo.]?\s*)?\d+(?:\s*(?:do|da|/)\s*(?:STJ|STF|TJBA|TNU))?")),
    ("Tema", re.compile(r"Tema\s+(?:Repetitivo\s+)?\d+(?:\s*(?:do|/)\s*(?:STJ|STF))?")),
    ("Acórdão", re.compile(r"(?:EAREsp|AREsp|EREsp|REsp|AgInt|AgRg|ADI|ADPF|RE)\s*(?:n[ºo.]?\s*)?\d[\d.]*(?:/[A-Z]{2})?")),
    ("Artigo", re.compile(
        r"arts?\.\s*[\d.º°o§,\sIVXparágrafounic\-–]{1,40}?\s*(?:do|da|c/c)\s*"
        r"(?:CPC|CDC|CC|CF|CPP|Código\s+(?:de\s+)?(?:Processo\s+Civil|Civil|Defesa\s+do\s+Consumidor)"
        r"|Lei(?:\s*n[ºo.]?)?\s*[\d.]+/?\d*)")),
    ("Resolução/IN/Lei", re.compile(
        r"(?:Res(?:olução)?\.?\s*(?:CMN|BCB|CNJ)\s*(?:n[ºo.]?\s*)?[\d./]+"
        r"|IN(?:\s*INSS(?:/PRES)?)?\s*(?:n[ºo.]?\s*)?[\d./]+"
        r"|Instrução Normativa[^,;.]{0,40}"
        r"|Lei(?:\s*n[ºo.]?)?\s*[\d.]+/\d{2,4}|Lei\s*[\d]+\.[\d]+"
        r"|LGPD|Lei Geral de Prote[^,;.]{0,30})")),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"codigo de processo civil", "cpc", s)
    s = re.sub(r"codigo de defesa do consumidor", "cdc", s)
    s = re.sub(r"codigo civil", "cc", s)
    s = re.sub(r"(?<![a-z])(?:do|da|c/c)(?![a-z])", " ", s)
    s = re.sub(r"(?<![a-z])n[o.]?\s*(?=\d)", " ", s)
    s = s.replace("º", "").replace("°", "")
    return re.sub(r"[^a-z0-9]", "", s)


def chaves(cit):
    """Variantes normalizadas da citação para o teste de presença nas referências."""
    base = re.sub(r"\s*(?:do|da|/)\s*(?:STJ|STF|TJBA|TNU)$", "", cit.strip())
    base = re.sub(r"\bS[úu]mulas\b", "Súmula", base)
    return {norm(cit), norm(base)}


def strings_py(caminho):
    """(linha, texto) de cada literal de string, incluindo partes de f-strings."""
    arv = ast.parse(Path(caminho).read_text(encoding="utf-8"))
    achados = []
    for no in ast.walk(arv):
        if isinstance(no, ast.Constant) and isinstance(no.value, str) and len(no.value) > 8:
            achados.append((no.lineno, no.value))
    return sorted(achados)


def paragrafos_docx(caminho):
    xml = zipfile.ZipFile(caminho).read("word/document.xml").decode("utf-8")
    saida = []
    for i, p in enumerate(re.findall(r"<w:p[ >].*?</w:p>", xml, re.S), 1):
        t = re.sub(r"<[^>]+>", "", p).strip()
        if t:
            saida.append((i, t))
    return saida


def titulos_py(caminho):
    txt = Path(caminho).read_text(encoding="utf-8")
    return [(m.group(1), m.group(2)) for m in re.finditer(r"\b(h1|h2)\(\s*f?\"([^\"]+)\"", txt)]


ARQ_NORMA = [  # (regex sobre a citação, arquivo em normas/)
    (r"\bCPC\b|Processo Civil", "cpc.md"),
    (r"\bCDC\b|Defesa do Consumidor", "cdc.md"),
    (r"\bCC\b|C[óo]digo Civil", "cc.md"),
    (r"14\.690", "lei-14690.md"),
    (r"10\.741", "lei-10741.md"),
    (r"14\.905", "lei-14905.md"),
    (r"9\.099", "lei-9099.md"),
    (r"LGPD|13\.709|Lei Geral de Prote", "lgpd.md"),
]
ARQ_ATO = [  # (regex sobre a citação, arquivo em normas/)
    (r"138/2022", "in-inss-138-2022-consolidada.md"),
    (r"\b143/2023", "in-inss-143-2023.md"),
    (r"4\.753", "res-cmn-4753-consolidada.md"),
    (r"5\.112|4\.549", "res-cmn-4549-consolidada.md"),
    (r"4\.935", "res-cmn-4935.md"),
    (r"3\.954", "res-cmn-3954-original.md"),
    (r"BCB\s*(?:n[ºo.]?\s*)?96\b", "res-bcb-96-2021.md"),
    (r"\b28/2008", "in-inss-28-2008-consolidada-2020.md"),
]


class Acervo:
    """Resolve uma citação para um arquivo do acervo (existência do artigo/ato; o conteúdo do § ou inciso não é conferido)."""

    def __init__(self, raiz):
        self.raiz = Path(raiz) if raiz else None
        self.cache = {}

    def texto(self, rel):
        if rel not in self.cache:
            p = self.raiz / rel
            self.cache[rel] = p.read_text(encoding="utf-8") if p.exists() else ""
        return self.cache[rel]

    def juris(self):
        if "J" not in self.cache:
            self.cache["J"] = "\n".join(
                p.read_text(encoding="utf-8") for p in sorted((self.raiz / "jurisprudencia").glob("*.md")))
        return self.cache["J"]

    def resolve(self, kind, cit):
        if not self.raiz:
            return None
        if kind == "Artigo":
            m = re.search(r"arts?\.\s*(\d[\d.]*)", cit)
            if not m:
                return None
            num = m.group(1).rstrip(".")
            for rx, arq in ARQ_NORMA:
                if re.search(rx, cit):
                    ok = re.search(r"(?m)^Art\. " + re.escape(num) + r"(?!\d)", self.texto("normas/" + arq))
                    return ("normas/" + arq + " (artigo existe)") if ok else None
            return None
        if kind == "Resolução/IN/Lei":
            for rx, arq in ARQ_NORMA + ARQ_ATO:
                if re.search(rx, cit):
                    return "normas/" + arq if self.texto("normas/" + arq) else None
            return None
        if kind == "Súmula":
            m = re.search(r"S[úu]mulas?\s+(?:n[ºo.]?\s*)?(\d+)", cit)
            if not m:
                return None
            arq = "sumulas-tjba-turma-uniformizacao.md" if "TJBA" in cit else "sumulas-stj.md"
            alvo = self.texto("jurisprudencia/" + arq) + self.texto("jurisprudencia/sumula-326-stj.md")
            if re.search(r"(?mi)^#+ S[úu]mula (?:n[ºo.]? ?)?0*" + m.group(1) + r"\b", alvo):
                return "jurisprudencia/" + arq
            return None
        if kind == "Tema":
            m = re.search(r"Tema\s+(?:Repetitivo\s+)?(\d+)", cit)
            if m and (self.raiz / f"jurisprudencia/tema-{m.group(1)}-stj.md").exists():
                return f"jurisprudencia/tema-{m.group(1)}-stj.md"
            return None
        if kind == "Acórdão":
            m = re.search(r"(\d[\d.]*\d)", cit)
            if m and m.group(1) in self.juris():
                return "jurisprudencia/ (número citado no texto)"
            return None
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--acervo", help="pasta _acervo (normas/ e jurisprudencia/); opcional")
    ap.add_argument("--md", nargs="*", default=[], help="arquivos Markdown (modelos ou peças) a incluir; opcional")
    ap.add_argument("--so-md", action="store_true", help="ignora os gerar.py/.docx do --pacote e lê só os --md")
    ap.add_argument("--pacote", default=".")
    ap.add_argument("--refs", required=True)
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()

    pacote, refs = Path(a.pacote), Path(a.refs)
    corpus = norm("\n".join(p.read_text(encoding="utf-8") for p in sorted(refs.glob("*.md"))))

    fontes = []
    if not a.so_md:
        for p in sorted(pacote.glob("skills/*/scripts/gerar.py")):
            fontes.append((p.parent.parent.name, p, "py"))
        for p in sorted(pacote.glob("skills/*/assets/*.docx")):
            fontes.append((p.parent.parent.name, p, "docx"))
    for p in a.md:
        fontes.append(("md", Path(p), "md"))

    ocorr = defaultdict(lambda: defaultdict(list))  # (tipo, cit) -> skill -> [local]
    titulos = {}
    for skill, caminho, tipo in fontes:
        rotulo = f"{caminho.name}"
        if tipo == "md":
            linhas_md = caminho.read_text(encoding="utf-8").splitlines()
            trechos = [(i, l) for i, l in enumerate(linhas_md, 1) if l.strip()]
            titulos[f"{skill}/{caminho.name}"] = [("h2" if l.startswith("##") else "h1", l.lstrip("# ").strip())
                                                   for l in linhas_md if l.startswith("#")]
        elif tipo == "py":
            trechos = strings_py(caminho)
            titulos[f"{skill}/{caminho.name}"] = titulos_py(caminho)
        else:
            trechos = paragrafos_docx(caminho)
            titulos[f"{skill}/{caminho.name}"] = [
                ("par", t[:110]) for _, t in trechos
                if re.match(r"^\d+(\.\d+)*\s*[-–]?\s*(DA|DO|DOS|DAS)\b", t)
            ]
        for linha, texto in trechos:
            for kind, rx in PADROES:
                for m in rx.finditer(texto):
                    cit = re.sub(r"\s+", " ", m.group(0)).strip(" ,;.")
                    ocorr[(kind, cit)][skill].append(f"{rotulo}:{linha}")

    linhas = ["# Inventário de citações das skills de iniciais (fase 1)", "",
              "Gerado por `inventario-citacoes.py`. Leitura estática; nada foi executado.",
              "Teste aproximado: CONFERIDA = a citação aparece no texto das referências conferidas do recurso; "
              "FORA = não aparece (buscar fonte ou marcar `[VERIFICAR ANTES DE PROTOCOLAR]`). "
              "As expressões regulares podem cortar ou duplicar citações: revisão humana obrigatória.", ""]

    acervo = Acervo(a.acervo)
    total = defaultdict(lambda: [0, 0, 0])  # no acervo, só nas referências, fora
    por_tipo = defaultdict(list)
    for (kind, cit), skills in ocorr.items():
        arq = acervo.resolve(kind, cit)
        if arq:
            status, idx = f"NO ACERVO: {arq}", 0
        elif any(k and k in corpus for k in chaves(cit)):
            status, idx = "só nas referências do recurso", 1
        else:
            status, idx = "**FORA**", 2
        total[kind][idx] += 1
        por_tipo[kind].append((cit, idx, status, skills))

    linhas += ["## Resumo", "", "| Tipo | No acervo | Só nas referências | Fora |", "|---|---|---|---|"]
    for kind, _ in PADROES:
        n, r, f = total[kind]
        linhas.append(f"| {kind} | {n} | {r} | {f} |")
    linhas.append("")

    for kind, _ in PADROES:
        itens = sorted(por_tipo[kind], key=lambda x: (-x[1], x[0]))
        linhas += [f"## {kind}", "", "| Citação | Status | Onde aparece |", "|---|---|---|"]
        for cit, _idx, status, skills in itens:
            onde = "; ".join(f"**{s}**: " + ", ".join(sorted(set(l))[:4]) +
                             (f" (+{len(set(l)) - 4})" if len(set(l)) > 4 else "")
                             for s, l in sorted(skills.items()))
            linhas.append(f"| {cit} | {status} | {onde} |")
        linhas.append("")

    linhas += ["## Estrutura de tópicos por gerador", ""]
    for chave, tit in titulos.items():
        linhas += [f"### {chave}", ""]
        for nivel, nome in tit:
            linhas.append(f"- {'  ' if nivel == 'h2' else ''}{nome}")
        linhas.append("")

    Path(a.saida).write_text("\n".join(linhas) + "\n", encoding="utf-8", newline="\n")
    print(f"ok: {sum(len(v) for v in por_tipo.values())} citações distintas -> {a.saida}")


if __name__ == "__main__":
    sys.exit(main())
