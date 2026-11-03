#!/usr/bin/env python3
"""diagramas_1000.py - figuras da Tese 1000 a partir do calculo.json (decisão D28, item 14: diagramas como imagem).

Para cada contrato derivado, grava duas imagens PNG:
  fig_anatomia_<n>.png      "Anatomia da reaverbação": contrato-raiz (averbação e exclusão) e contrato derivado
                            (mesmo número-raiz + sufixo), com o intervalo entre a exclusão e a reaverbação
  fig_linha_tempo_<n>.png   "Linha do tempo": averbação da raiz, exclusão, averbação do derivado e período dos descontos
e figuras.json com a legenda de cada imagem, para a peça.

Os dados vêm só do calculo.json (que vem do extrato do INSS). A figura não introduz fato novo: reproduz o extrato.

Uso:  python3 diagramas_1000.py --calculo calculo.json --saida pasta/figuras [--fonte "ID 12, p. 3"]
Requer: Pillow (pip install pillow).
"""
import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("diagramas_1000.py precisa do Pillow: pip install pillow")

AZUL, AZUL_CLARO, VERMELHO, CINZA, TEXTO, FUNDO = "#1F2A44", "#E8ECF4", "#B3261E", "#8A8F98", "#1B1B1B", "#FFFFFF"
LARG = 1400
FONTES = [  # ordem de busca; a primeira que existir é usada
    ("Lato-Regular.ttf", "Lato-Bold.ttf"), ("LatoWeb-Regular.ttf", "LatoWeb-Bold.ttf"),
    ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf"), ("arial.ttf", "arialbd.ttf"), ("Arial.ttf", "Arial Bold.ttf"),
]
PASTAS = [os.environ.get("FONTES_DIAGRAMA", ""), "C:/Windows/Fonts", "/usr/share/fonts/truetype/lato", "/usr/share/fonts/truetype/dejavu",
          "/usr/share/fonts/truetype", "/usr/share/fonts", "/Library/Fonts", "/System/Library/Fonts/Supplementary"]


def _acha(nome):
    for d in PASTAS:
        if not d:
            continue
        p = Path(d) / nome
        if p.exists():
            return str(p)
        for q in Path(d).rglob(nome) if Path(d).exists() and d.startswith("/usr") else []:
            return str(q)
    return None


def fontes():
    for reg, neg in FONTES:
        a, b = _acha(reg), _acha(neg)
        if a:
            return a, (b or a)
    return None, None


FR, FB = fontes()


def F(tam, negrito=False):
    caminho = FB if negrito else FR
    if caminho:
        return ImageFont.truetype(caminho, tam)
    try:
        return ImageFont.load_default(size=tam)
    except TypeError:
        return ImageFont.load_default()


def data(s):
    if not s:
        return None
    for fmt in ("%d/%m/%Y", "%d/%m/%y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def comp(s):  # MM/AAAA -> primeiro dia do mês
    try:
        m, a = s.split("/")
        return dt.date(int(a), int(m), 1)
    except Exception:
        return None


def brl(v):
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def larg(dr, txt, f):
    return dr.textbbox((0, 0), txt, font=f)[2]


def cabecalho(dr, titulo, sub):
    dr.rectangle([0, 0, LARG, 74], fill=AZUL)
    dr.text((24, 12), titulo.upper(), font=F(26, True), fill="#FFFFFF")
    dr.text((24, 46), sub, font=F(16), fill="#DDE3EE")


def rodape(dr, h, fonte):
    txt = f"Fonte: Histórico de Empréstimo Consignado do INSS{(' (' + fonte + ')') if fonte else ''}. Figura elaborada a partir do extrato; não introduz fato novo."
    dr.text((24, h - 34), txt, font=F(15), fill=CINZA)


def caixa(dr, x, y, w, h, titulo, linhas, destaque=None):
    dr.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=AZUL_CLARO, outline=AZUL, width=3)
    dr.text((x + 20, y + 16), titulo, font=F(20, True), fill=AZUL)
    yy = y + 54
    for ln in linhas:
        if isinstance(ln, tuple):  # número com sufixo destacado
            base, suf = ln
            dr.text((x + 20, yy), base, font=F(26, True), fill=TEXTO)
            if suf:
                bx = x + 20 + larg(dr, base, F(26, True))
                dr.rounded_rectangle([bx + 2, yy - 2, bx + 8 + larg(dr, suf, F(26, True)), yy + 32], radius=6, fill=VERMELHO)
                dr.text((bx + 5, yy), suf, font=F(26, True), fill="#FFFFFF")
            yy += 46
        else:
            dr.text((x + 20, yy), ln, font=F(18), fill=TEXTO)
            yy += 30


def seta(dr, x1, y, x2, cor=AZUL, rotulo=None, rotulo2=None):
    dr.line([x1, y, x2 - 18, y], fill=cor, width=5)
    dr.polygon([(x2, y), (x2 - 22, y - 13), (x2 - 22, y + 13)], fill=cor)
    if rotulo:
        f = F(17, True)
        dr.text(((x1 + x2) / 2 - larg(dr, rotulo, f) / 2, y - 40), rotulo, font=f, fill=cor)
    if rotulo2:
        f = F(16)
        dr.text(((x1 + x2) / 2 - larg(dr, rotulo2, f) / 2, y + 14), rotulo2, font=f, fill=TEXTO)


def intervalo_txt(d):
    n, cat = d.get("intervalo_dias"), d.get("categoria_intervalo")
    if cat == "MESMO_DIA":
        return "reaverbado no mesmo dia da exclusão"
    if cat == "ANTES_DA_EXCLUSAO":
        return f"averbado {abs(n)} dia(s) ANTES da exclusão da raiz"
    if n is None:
        return "intervalo não apurado"
    return f"reaverbado {n} dia(s) depois da exclusão"


def anatomia(d, fonte, destino):
    h = 470
    im = Image.new("RGB", (LARG, h), FUNDO)
    dr = ImageDraw.Draw(im)
    rd = d.get("raiz_dados") or {}
    cabecalho(dr, "Anatomia da reaverbação", f"Contrato derivado nº {d['contrato']} sobre o número-raiz {d.get('raiz') or '[raiz não localizada]'}")
    caixa(dr, 40, 110, 520, 290, "Contrato-raiz", [
        (d.get("raiz") or "não localizado", ""),
        f"Averbação: {rd.get('averbacao') or '—'}",
        f"Exclusão: {rd.get('exclusao') or '—'}",
        f"Motivo: {rd.get('motivo_exclusao') or '—'}",
        f"Banco: {(rd.get('banco') or '—')[:40]}",
    ])
    caixa(dr, LARG - 560, 110, 520, 290, "Contrato derivado (sem nova contratação)", [
        (d.get("raiz") or d["contrato"], d.get("sufixo") or ""),
        f"Averbação: {d.get('primeira_averbacao') or d.get('inclusao') or '—'}",
        f"Descontos: {d.get('inicio') or '—'} a {d.get('ate_comp') or d.get('fim') or '—'}",
        f"{d.get('qtde', 0)} parcela(s) de {brl(d.get('parcela') or 0)}",
        f"Total descontado: {brl(d.get('total') or 0)}",
    ])
    seta(dr, 580, 255, LARG - 580, cor=VERMELHO, rotulo="mesmo número-raiz + sufixo " + (d.get("sufixo") or ""),
         rotulo2=intervalo_txt(d))
    rodape(dr, h, fonte)
    im.save(destino)
    return im.size


def linha_tempo(d, fonte, destino):
    h = 500
    im = Image.new("RGB", (LARG, h), FUNDO)
    dr = ImageDraw.Draw(im)
    rd = d.get("raiz_dados") or {}
    cabecalho(dr, "Linha do tempo", f"Sequência registrada no extrato do INSS para o contrato derivado nº {d['contrato']}")
    marcos = [
        (data(rd.get("averbacao")), "1", "Averbação da raiz", rd.get("averbacao"), AZUL),
        (data(rd.get("exclusao")), "2", "Exclusão da raiz", rd.get("exclusao"), AZUL),
        (data(d.get("primeira_averbacao") or d.get("inclusao")), "3", "Averbação do derivado", d.get("primeira_averbacao") or d.get("inclusao"), VERMELHO),
    ]
    ini, fim = comp(d.get("inicio")), comp(d.get("ate_comp") or d.get("fim"))
    datas = [m[0] for m in marcos if m[0]] + [x for x in (ini, fim) if x]
    if len(datas) < 2:
        dr.text((40, 200), "Datas insuficientes no extrato para a linha do tempo.", font=F(20), fill=VERMELHO)
        rodape(dr, h, fonte)
        im.save(destino)
        return im.size
    d0, d1 = min(datas), max(datas)
    span = max((d1 - d0).days, 1)
    x0, x1, y = 90, LARG - 90, 330

    def X(dd):
        return x0 + (x1 - x0) * (dd - d0).days / span

    dr.line([x0, y, x1, y], fill=CINZA, width=4)
    if ini and fim:  # período dos descontos, rótulo abaixo do eixo
        dr.rectangle([X(ini), y - 10, max(X(fim), X(ini) + 6), y + 10], fill=VERMELHO)
        t = f"4  Descontos: {d.get('inicio')} a {d.get('ate_comp') or d.get('fim')} ({d.get('qtde', 0)} × {brl(d.get('parcela') or 0)})"
        f = F(17, True)
        xt = min(max(X(ini), x0), x1 - larg(dr, t, f))
        dr.line([X(ini), y + 10, X(ini), y + 34], fill=VERMELHO, width=2)
        dr.text((xt, y + 36), t, font=f, fill=VERMELHO)
    # marcos: círculos no eixo (marcos do mesmo dia lado a lado) e rótulos acima, em faixas sem sobreposição
    pos, ultimo_x = [], None
    for dd, n, rot, txt, cor in marcos:
        if not dd:
            continue
        x = X(dd)
        if ultimo_x is not None and x - ultimo_x < 38:
            x = ultimo_x + 38
        ultimo_x = x
        pos.append((x, n, rot, txt, cor))
    faixas, rotulos = [], []  # borda direita ocupada em cada faixa; rótulos a desenhar
    f1, f2 = F(17, True), F(16)
    for x, n, rot, txt, cor in pos:
        w = max(larg(dr, rot, f1), larg(dr, txt or "", f2))
        xt = min(max(x - w / 2, 20), LARG - 20 - w)
        k = next((i for i, r in enumerate(faixas) if xt > r + 16), None)
        if k is None:
            faixas.append(0)
            k = len(faixas) - 1
        faixas[k] = xt + w
        ty = y - 78 - 58 * k
        rotulos.append((x, xt, ty, w, rot, txt, cor))
    for x, xt, ty, w, rot, txt, cor in rotulos:  # fios primeiro, rótulos por cima, com fundo branco
        dr.line([x, y - 16, x, ty + 44], fill=cor, width=2)
    for x, xt, ty, w, rot, txt, cor in rotulos:
        dr.rectangle([xt - 4, ty - 2, xt + w + 4, ty + 44], fill=FUNDO)
        dr.text((xt, ty), rot, font=f1, fill=cor)
        dr.text((xt, ty + 22), txt or "—", font=f2, fill=TEXTO)
    for x, n, rot, txt, cor in pos:
        dr.ellipse([x - 16, y - 16, x + 16, y + 16], fill=cor, outline="#FFFFFF", width=2)
        dr.text((x - larg(dr, n, F(18, True)) / 2, y - 12), n, font=F(18, True), fill="#FFFFFF")
    dr.text((x0, y + 80), intervalo_txt(d).capitalize() + ".", font=F(18, True), fill=AZUL)
    rodape(dr, h, fonte)
    im.save(destino)
    return im.size


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--calculo", required=True)
    ap.add_argument("--saida", required=True)
    ap.add_argument("--fonte", help='ID e página do extrato no processo, por exemplo "ID 12, p. 3"')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    c = json.loads(Path(a.calculo).read_text(encoding="utf-8"))
    s = Path(a.saida)
    s.mkdir(parents=True, exist_ok=True)
    figs = []
    for n, d in enumerate(c.get("derivados", []), 1):
        fa, fl = s / f"fig_anatomia_{n}.png", s / f"fig_linha_tempo_{n}.png"
        anatomia(d, a.fonte, fa)
        linha_tempo(d, a.fonte, fl)
        figs.append({"derivado": d["contrato"], "anatomia": fa.name, "linha_tempo": fl.name,
                     "legenda_anatomia": f"Anatomia da reaverbação do contrato nº {d['contrato']} (número-raiz {d.get('raiz')}).",
                     "legenda_linha_tempo": f"Linha do tempo do contrato nº {d['contrato']}, conforme o extrato do INSS."})
    (s / "figuras.json").write_text(json.dumps({"fonte": a.fonte, "fonte_tipografica": FR or "padrão do Pillow", "figuras": figs},
                                               ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    if not a.fonte:
        print("AVISO: sem --fonte; o rodapé das figuras não traz o ID e a página do extrato.")
    if not FR:
        print("AVISO: nenhuma fonte TrueType encontrada; usada a fonte padrão do Pillow (defina FONTES_DIAGRAMA).")
    print(f"ok: {len(figs) * 2} figura(s) em {s}")


if __name__ == "__main__":
    main()
