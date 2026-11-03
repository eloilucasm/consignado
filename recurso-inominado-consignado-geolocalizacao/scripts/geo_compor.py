#!/usr/bin/env python3
"""geo_compor.py - prepara as três imagens da Figura Ilustrativa para a peça, a partir das capturas de mapa
(geo_mapa_pmtiles.py) e da visão geral do IBGE (geo_figuras.py).

Grava, por evento, em --pasta:
  fig_evento<n>_A_visao_geral.png (malha do IBGE), fig_evento<n>_B_log.png, fig_evento<n>_C_residencia.png
  fig_evento<n>_paineis.json  (lista ordenada de {arquivo, legenda})
Entrada: figura<k>_evento<n>_captura1_log.png e ..._captura2_referencia.png (1100 x 700), fig_evento<n>_visao_geral.png
e legendas_plano_b.json (legendas de cada imagem). Imagens de outra largura são redimensionadas a 1100 px.

Uso:
    python3 geo_compor.py --pasta figuras/ --atribuicao "Mapa de fundo © OpenStreetMap contributors, Protomaps."
Dependência: Pillow.
"""
import argparse
import glob
import json
import os
import re
import sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Erro: precisa do Pillow (pip install pillow --break-system-packages).", file=sys.stderr)
    sys.exit(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasta", default="figuras")
    ap.add_argument("--atribuicao", help="troca a atribuição padrão do mapa de fundo nas legendas")
    a = ap.parse_args()
    os.makedirs(a.pasta, exist_ok=True)
    paineis_leg = {}
    lj = os.path.join(a.pasta, "legendas_plano_b.json")
    if os.path.exists(lj):
        with open(lj, encoding="utf-8") as f:
            for it in json.load(f):
                if it.get("paineis"):
                    paineis_leg[it["n"]] = it["paineis"]
    eventos = sorted({int(m.group(1)) for f in glob.glob(os.path.join(a.pasta, "figura*_evento*_captura1_log.png"))
                      for m in [re.search(r"_evento(\d+)_", f)] if m})
    if not eventos:
        print("Nenhum conjunto de capturas encontrado.", file=sys.stderr)
        return 1

    def ajusta(im, w=1100):
        return im if im.width == w else im.resize((w, round(im.height * w / im.width)))

    for n in eventos:
        def abre(nome):
            fs = glob.glob(os.path.join(a.pasta, f"figura*_evento{n}_{nome}.png"))
            return ajusta(Image.open(fs[0]).convert("RGB")) if fs else None
        c1, c2 = abre("captura1_log"), abre("captura2_referencia")
        if not (c1 and c2):
            print(f"Evento {n}: faltam as capturas do log e da residência; não composto.", file=sys.stderr)
            continue
        vg_ibge = os.path.join(a.pasta, f"fig_evento{n}_visao_geral.png")
        itens = []
        if os.path.exists(vg_ibge):
            itens.append(("A_visao_geral", ajusta(Image.open(vg_ibge).convert("RGB"))))
        else:
            print(f"Aviso: evento {n}: falta a visão geral (malha do IBGE); rode geo_figuras.py antes.", file=sys.stderr)
        itens += [("B_log", c1), ("C_residencia", c2)]
        pl = paineis_leg.get(n) or []
        if len(itens) == 2:
            pl = pl[1:]
        paineis = []
        for i, (nome, im) in enumerate(itens):
            arq = os.path.join(a.pasta, f"fig_evento{n}_{nome}.png")
            im.save(arq, dpi=(150, 150))
            leg = pl[i] if i < len(pl) else ""
            if not leg:
                print(f"Aviso: evento {n}, imagem {nome}: sem legenda.", file=sys.stderr)
            if a.atribuicao and leg:
                leg = leg.replace("Mapa de fundo © OpenStreetMap contributors.", a.atribuicao.rstrip(".") + ".")
            paineis.append({"arquivo": arq, "legenda": leg})
        with open(os.path.join(a.pasta, f"fig_evento{n}_paineis.json"), "w", encoding="utf-8") as f:
            json.dump(paineis, f, ensure_ascii=False, indent=2)
        print(f"Evento {n}: {len(paineis)} imagens, em ordem (A visão geral, B log, C residência).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
