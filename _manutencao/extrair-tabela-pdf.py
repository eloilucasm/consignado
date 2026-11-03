#!/usr/bin/env python3
"""Extrai tabelas de PDF (ex.: anexo com a relação de indicadores de um sistema do órgão) em segmentos por linha de grade.

Uso:
    python extrair-tabela-pdf.py anexo.pdf saida.json [--min-colunas 5]

Requer PyMuPDF:  pip install pymupdf

Como funciona: em cada página, as linhas verticais desenhadas no PDF dão as colunas e as linhas horizontais que
cruzam a tabela inteira separam os registros. Cada registro vira um objeto {"p": página, "y": [topo, base],
"c": [texto da coluna 1, coluna 2, ...]}. Registros que continuam na página seguinte aparecem como segmentos com
a primeira coluna vazia: junte-os ao registro anterior no seu script de pós-processamento.

Depois de extrair, faça o pós-processamento do SEU caso (filtrar rodapé "Anexo ... pg.", juntar continuações,
montar o Markdown). Compare o resultado com uma segunda extração independente (por exemplo, "pdftotext -layout") antes
de gravar no pacote: no caso do Anexo V, as duas extrações bateram em todas as 209 siglas.
O texto do PDF NÃO é fonte até ser conferido: guarde a URL oficial e a data da consulta no cabeçalho do arquivo gerado.
"""
import io
import json
import sys
import collections

try:
    import pymupdf
except ImportError:  # versões antigas do pacote usam o nome fitz
    import fitz as pymupdf


def colunas_da_pagina(pagina, minimo):
    """Devolve as posições x das divisórias verticais (colunas), ou None se a página não tem tabela."""
    cont = collections.Counter()
    for d in pagina.get_drawings():
        for it in d["items"]:
            if it[0] == "l" and abs(it[1].x - it[2].x) < 0.5 and abs(it[1].y - it[2].y) > 8:
                cont[round(it[1].x)] += 1
            elif it[0] == "re" and it[1].width < 1.5 and it[1].height > 8:
                cont[round(it[1].x0)] += 1
    if not cont:
        return None
    m = max(cont.values())
    xs = sorted(x for x, c in cont.items() if c >= m / 2.5)
    fundidos = []
    for x in xs:
        if not fundidos or x - fundidos[-1] > 8:  # funde bordas duplas
            fundidos.append(x)
    return fundidos if len(fundidos) > minimo else None


def separadores_horizontais(pagina):
    """y das linhas horizontais que cobrem a maior parte da largura da tabela."""
    cobertura = {}
    for d in pagina.get_drawings():
        for it in d["items"]:
            if it[0] == "l" and abs(it[1].y - it[2].y) < 0.5:
                y, a, b = it[1].y, min(it[1].x, it[2].x), max(it[1].x, it[2].x)
            elif it[0] == "re" and it[1].height < 1.5:
                y, a, b = it[1].y0, it[1].x0, it[1].x1
            else:
                continue
            cobertura.setdefault(round(y), []).append((a, b))
    altura = pagina.rect.height
    return sorted(y for y, v in cobertura.items() if sum(b - a for a, b in v) > 400 and 0 <= y <= altura)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    entrada, saida = sys.argv[1], sys.argv[2]
    minimo = int(sys.argv[sys.argv.index("--min-colunas") + 1]) - 1 if "--min-colunas" in sys.argv else 4
    doc = pymupdf.open(entrada)
    segmentos = []
    cols_anteriores = None
    for n, pagina in enumerate(doc):
        xs = colunas_da_pagina(pagina, minimo)
        if xs is None:
            continue
        cols_anteriores = xs
        faixas = [(xs[i] - 2, xs[i + 1] - 2 if i < len(xs) - 2 else 700) for i in range(len(xs) - 1)]
        limites = [0] + separadores_horizontais(pagina) + [pagina.rect.height]
        for topo, base in zip(limites, limites[1:]):
            if base - topo < 3:
                continue
            textos = [
                pagina.get_text("text", clip=pymupdf.Rect(x0, topo + 0.6, x1, base - 0.6), sort=True)
                for x0, x1 in faixas
            ]
            segmentos.append({"p": n + 1, "y": [round(topo), round(base)], "c": textos})
    with io.open(saida, "w", encoding="utf-8") as f:
        json.dump(segmentos, f, ensure_ascii=False)
    print(f"{len(doc)} páginas | {len(segmentos)} segmentos gravados em {saida}")


if __name__ == "__main__":
    main()
