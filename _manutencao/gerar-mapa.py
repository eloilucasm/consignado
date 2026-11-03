#!/usr/bin/env python3
"""gerar-mapa.py - gera references/normas/MAPA.md em cada skill: um dispositivo por linha, com número da linha e o início do texto.

Para quê: achar o artigo pelo CONTEÚDO quando não se sabe o número, e em qualquer ambiente. No Cowork, o número da linha serve
para Read com offset/limit. No chat (sem execução de código e sem grep), o número do artigo e o início do texto bastam para a
leitura localizar o dispositivo no arquivo. Complementa o ESTRUTURA.md, que mapeia Parte/Livro/Título/Capítulo e é grosso nas
normas curtas ou sem divisão.

Normas muito grandes (Código Civil e CPC) entram só com os artigos que as peças usam (SELETIVO abaixo); o resto está no
ESTRUTURA.md. Não altera nenhum texto de norma.

Uso (a partir de consignado-pacote/):  python3 _manutencao/gerar-mapa.py [--skill nome]
"""
import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent
PROPRIO = re.compile(r"^(INDEX|MAPA|ESTRUTURA)\.md$")
ART = re.compile(r"^(~~)?\s*Art\.\s*(\d+(?:\.\d+)*)\s*([ºo°])?(?:\s*-\s*([A-Z]))?")
MAXTXT = 150

# Normas grandes: só os artigos usados pelas peças. Edite a lista ao incluir um artigo novo nos modelos.
SELETIVO = {
    "cc.md": {104, 157, 166, 168, 169, 182, 186, 205, 397, 398, 422},
    "cpc.md": {85, 98, 99, 105, 219, 292, 294, 300, 311, 337, 369, 373, 396, 397, 398, 399, 400, 401, 402, 403, 404,
               429, 489, 497, 505, 508, 537, 1048},
}


def rotulo(m):
    return "Art. " + m.group(2) + ("º" if m.group(3) else "") + ("-" + m.group(4) if m.group(4) else "")


def inicio(linha):
    t = re.sub(r"^(~~)?\s*Art\.\s*\d+(?:\.\d+)*\s*[ºo°]?(?:\s*-\s*[A-Z])?\s*[.º-]?\s*", "", linha.replace("~~", ""))
    t = re.sub(r"\((?:Redação dada|Incluíd[oa]|Alterad[oa]|Revogad[oa]|Vide|Vigência|Regulamento)[^)]*\)?", "", t).strip()
    t = t.replace("|", "/")
    if len(t) > MAXTXT:
        t = t[:MAXTXT].rsplit(" ", 1)[0] + "…"
    return t or "(sem texto na primeira linha)"


def mapear(arq):
    texto = arq.read_text(encoding="utf-8").replace("\r\n", "\n")
    linhas = texto.split("\n")
    titulo = (linhas[0] if linhas else "").lstrip("# ").strip()
    out = []
    for n, l in enumerate(linhas, 1):
        m = ART.match(l)
        if not m:
            continue
        num = int(m.group(2).replace(".", "")) if m.group(2).replace(".", "").isdigit() else 0
        out.append((n, rotulo(m), num, bool(m.group(1)) or "(Revogado" in l[:60] or "(Revogada" in l[:60], l))
    return titulo, len(linhas), out


def montar(skill, dir_normas):
    blocos = [f"""# Mapa de dispositivos: {skill}

Gerado por `python3 _manutencao/gerar-mapa.py` (não edite à mão). Um dispositivo por linha: número do artigo, linha do arquivo e início do texto (sem os parágrafos e incisos). Serve para achar o artigo **pelo conteúdo**. A regra é o texto do arquivo indicado, com parágrafos e incisos.

**Como usar.**
- **Cowork:** abra o arquivo só na janela indicada (`Read` com `offset` na linha do artigo) ou use `grep -n "^Art. N"`.
- **Chat, sem execução de código:** procure no arquivo o número do artigo (`Art. N`) e leia a partir dali.
- Para localizar por Livro, Título ou Capítulo, use `ESTRUTURA.md`. O que não está nas normas desta pasta está em `../../protocolo/fontes-e-limites.md`.
- Dispositivo ~~riscado~~ ou marcado (revogado) não é vigente: não o cite como vigente.
"""]
    for arq in sorted(dir_normas.glob("*.md")):
        if PROPRIO.match(arq.name):
            continue
        titulo, nlin, arts = mapear(arq)
        sel = SELETIVO.get(arq.name)
        blocos.append(f"\n## {titulo}\n\n`{arq.name}` · {nlin} linhas\n")
        if not arts:
            blocos.append("_Sem artigos numerados no texto: leia o arquivo (é curto) ou procure a expressão._\n")
            continue
        if sel is not None:
            arts = [a for a in arts if a[2] in sel]
            blocos.append(f"_Mapa seletivo: só os {len(arts)} artigos que as peças usam. Os demais estão em `ESTRUTURA.md`._\n")
        blocos.append("| Dispositivo | Linha | Início do texto |\n|---|---|---|")
        for n, rot, _, rev, l in arts:
            marca = " (revogado)" if rev else ""
            blocos.append(f"| {rot}{marca} | {n} | {inicio(l)} |")
    return "\n".join(blocos) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill")
    a = ap.parse_args()
    for d in sorted(RAIZ.iterdir()):
        nd = d / "references" / "normas"
        if not (d / "SKILL.md").exists() or not nd.exists() or (a.skill and d.name != a.skill):
            continue
        (nd / "MAPA.md").write_text(montar(d.name, nd), encoding="utf-8", newline="\n")
        print("ok:", nd / "MAPA.md")


if __name__ == "__main__":
    main()
