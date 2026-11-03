#!/usr/bin/env python3
"""figuras.py - padrão das figuras das peças (regras em assets/padrao-figuras.md). Arquivo do acervo: edite em _acervo/scripts.

A figura é desenhada no tamanho em que entra na peça: largura útil da página A4 da tipografia-azul (21 cm - 2 x 2 cm = 17 cm)
a 300 dpi. Os tamanhos de fonte são em pt no papel; o menor é 9 pt (corpo da peça: 12 pt). A altura acompanha o conteúdo.

Blocos: cabecalho, caixas (lado a lado, com número e sufixo destacado), seta, faixa (destaque em largura total), linha_tempo
(marcos com espaço igual e o tempo entre eles escrito), rodape. Uso típico:

    import figuras as fg
    im, dr = fg.tela()
    y = fg.cabecalho(dr, "Título", "Subtítulo") + fg.P(12)
    y = fg.faixa(dr, y, "Frase de destaque.") + fg.P(12)
    fg.fechar(im, fg.rodape(dr, y, "Fonte: ..."), "fig.png")

Requer: Pillow (pip install pillow).
"""
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("as figuras precisam do Pillow: pip install pillow")

# cores da tipografia-azul: azul-marinho para estrutura, vermelho só para o que a figura quer provar, cinza para o acessório
AZUL, AZUL_CLARO, VERMELHO, VERMELHO_CLARO, CINZA, TEXTO, FUNDO = "#1F2A44", "#E8ECF4", "#B3261E", "#FBECEB", "#6B7079", "#1B1B1B", "#FFFFFF"
DPI = 300
LARGURA_CM = 17
LARG = round(LARGURA_CM / 2.54 * DPI)  # 2008 px
PT = {"titulo": 12, "sub": 10, "caixa": 11, "numero": 13, "texto": 10, "rotulo": 10, "rodape": 9, "marco": 9}
PT_MINIMO = 9
FONTES = [  # ordem de busca; a primeira que existir é usada
    ("Lato-Regular.ttf", "Lato-Bold.ttf"), ("LatoWeb-Regular.ttf", "LatoWeb-Bold.ttf"),
    ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf"), ("arial.ttf", "arialbd.ttf"), ("Arial.ttf", "Arial Bold.ttf"),
]
PASTAS = [os.environ.get("FONTES_DIAGRAMA", ""), "C:/Windows/Fonts", "/usr/share/fonts/truetype/lato", "/usr/share/fonts/truetype/dejavu",
          "/usr/share/fonts/truetype", "/usr/share/fonts", "/Library/Fonts", "/System/Library/Fonts/Supplementary"]


def P(pt):
    """pt no papel -> px na imagem."""
    return round(pt * DPI / 72)


M = P(12)  # margem lateral


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


def _fontes():
    for reg, neg in FONTES:
        a, b = _acha(reg), _acha(neg)
        if a:
            return a, (b or a)
    return None, None


FR, FB = _fontes()


def F(tipo, negrito=False):
    """Fonte pelo papel do texto (chave de PT) ou pelo tamanho em pt; nunca abaixo de PT_MINIMO."""
    tam = P(max(PT[tipo] if isinstance(tipo, str) else tipo, PT_MINIMO))
    caminho = FB if negrito else FR
    if caminho:
        return ImageFont.truetype(caminho, tam)
    try:
        return ImageFont.load_default(size=tam)
    except TypeError:
        return ImageFont.load_default()


# ---------- textos ----------

def brl(v):
    return "R$\u00a0" + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")  # R$ não se separa do valor


def dias(n):
    return f"{n} dia" if abs(n) == 1 else f"{n} dias"


def meses(n):
    """Meses por extenso; a partir de 12, em anos e meses."""
    a, m = divmod(n, 12)
    txt = lambda k, um, varios: f"{k} {um if k == 1 else varios}"  # noqa: E731
    if not a:
        return txt(m, "mês", "meses")
    return txt(a, "ano", "anos") + (f" e {txt(m, 'mês', 'meses')}" if m else "")


def parcelas(n):
    return f"{n} parcela" if n == 1 else f"{n} parcelas"


def entre_datas(a, b, competencia=False):
    """Tempo entre duas datas: dias até 60; depois, anos e meses. competencia=True compara só mês e ano."""
    if competencia:
        k = (b.year - a.year) * 12 + b.month - a.month
        return "mesmo mês" if k == 0 else meses(k)
    k = (b - a).days
    if k > 60:
        return meses((b.year - a.year) * 12 + b.month - a.month - (b.day < a.day))
    return "mesmo dia" if k == 0 else dias(k)


def larg(dr, txt, f):
    return dr.textlength(txt, font=f)


def alt(f):
    """Altura de uma linha, com entrelinha de 1,2."""
    a, d = f.getmetrics()
    return round((a + d) * 1.2)


def quebra(dr, txt, f, maxw):
    """Linhas do texto que cabem em maxw. Só o espaço comum quebra; o inseparável (\\u00a0) não."""
    linhas, atual = [], ""
    for p in (txt or "").split(" "):
        t = f"{atual} {p}".strip()
        if atual and larg(dr, t, f) > maxw:
            linhas.append(atual)
            atual = p
        else:
            atual = t
    return linhas + ([atual] if atual else [])


def texto(dr, x, y, txt, f, cor, maxw):
    """Escreve o texto quebrado em maxw; devolve o y seguinte."""
    for ln in quebra(dr, txt, f, maxw):
        dr.text((x, y), ln, font=f, fill=cor)
        y += alt(f)
    return y


def centrado(dr, xc, y, txt, f, cor, maxw):
    """Texto quebrado em maxw e centrado em xc; devolve o y seguinte."""
    for ln in quebra(dr, txt, f, maxw):
        dr.text((xc - larg(dr, ln, f) / 2, y), ln, font=f, fill=cor)
        y += alt(f)
    return y


# ---------- tela ----------

def tela():
    im = Image.new("RGB", (LARG, 4000), FUNDO)  # recortada no fim, pela altura do conteúdo
    return im, ImageDraw.Draw(im)


def fechar(im, y, destino):
    im = im.crop((0, 0, LARG, y))
    im.save(destino, dpi=(DPI, DPI))
    return im.size


# ---------- blocos ----------

def cabecalho(dr, titulo, sub=None):
    """Faixa azul com o título em caixa alta e o subtítulo; devolve a altura."""
    ft, fs = F("titulo", True), F("sub")
    h = P(8) + alt(ft) + (alt(fs) * len(quebra(dr, sub, fs, LARG - 2 * M)) if sub else 0) + P(6)
    dr.rectangle([0, 0, LARG, h], fill=AZUL)
    dr.text((M, P(8)), titulo.upper(), font=ft, fill="#FFFFFF")
    if sub:
        texto(dr, M, P(8) + alt(ft), sub, fs, "#DDE3EE", LARG - 2 * M)
    return h


def rodape(dr, y, txt):
    """Fio e nota de fonte em 9 pt; devolve a altura final da figura.

    Na inicial, cite o documento como anexo, sem ID (o processo ainda não existe). Em peça de processo em curso, use o ID.
    """
    dr.line([M, y, LARG - M, y], fill="#D5D9E0", width=2)
    return texto(dr, M, y + P(4), txt, F("rodape"), CINZA, LARG - 2 * M) + P(4)


def faixa(dr, y, txt, cor=VERMELHO, fundo=VERMELHO_CLARO):
    """Frase de destaque em largura total, numa faixa com borda; devolve o y seguinte."""
    fn, iw = F("rotulo", True), LARG - 2 * M - 2 * P(8)
    h = 2 * P(6) + alt(fn) * len(quebra(dr, txt, fn, iw))
    dr.rounded_rectangle([M, y, LARG - M, y + h], radius=P(4), fill=fundo, outline=cor, width=3)
    texto(dr, M + P(8), y + P(6), txt, fn, cor, iw)
    return y + h


def _fonte_numero(dr, base, suf, maxw):
    """Maior fonte (13 a 10 pt) em que número e sufixo cabem na caixa."""
    for pt in range(PT["numero"], 9, -1):
        f = F(pt, True)
        if larg(dr, base + suf, f) + (P(5) if suf else 0) <= maxw:
            return f
    return F(10, True)


def _caixa_altura(dr, w, titulo, numero, linhas):
    pad = P(8)
    iw = w - 2 * pad
    ft, fx = F("caixa", True), F("texto")
    h = pad + alt(ft) * len(quebra(dr, titulo, ft, iw)) + P(3)
    if numero:
        h += alt(_fonte_numero(dr, *numero, iw)) + P(3)
    return h + sum(alt(fx) * len(quebra(dr, ln, fx, iw)) for ln in linhas) + pad


def _caixa(dr, x, y, w, h, titulo, numero, linhas):
    pad = P(8)
    iw = w - 2 * pad
    dr.rounded_rectangle([x, y, x + w, y + h], radius=P(6), fill=AZUL_CLARO, outline=AZUL, width=4)
    yy = texto(dr, x + pad, y + pad, titulo, F("caixa", True), AZUL, iw) + P(3)
    if numero:
        base, suf = numero
        fn = _fonte_numero(dr, base, suf, iw)
        dr.text((x + pad, yy), base, font=fn, fill=TEXTO)
        if suf:  # sufixo destacado em vermelho
            bx = x + pad + larg(dr, base, fn) + P(1)
            x0, y0, x1, y1 = dr.textbbox((bx + P(1.5), yy), suf, font=fn)
            dr.rounded_rectangle([x0 - P(1.5), y0 - P(1.5), x1 + P(1.5), y1 + P(1.5)], radius=P(2), fill=VERMELHO)
            dr.text((bx + P(1.5), yy), suf, font=fn, fill="#FFFFFF")
        yy += alt(fn) + P(3)
    for ln in linhas:
        yy = texto(dr, x + pad, yy, ln, F("texto"), TEXTO, iw)


def seta(dr, x1, y, x2, cor=VERMELHO):
    ponta = P(7)
    dr.line([x1, y, x2 - ponta, y], fill=cor, width=P(1.5))
    dr.polygon([(x2, y), (x2 - ponta, y - ponta * 0.6), (x2 - ponta, y + ponta * 0.6)], fill=cor)


def caixas(dr, y, itens, setas=True):
    """Caixas lado a lado, de mesma altura, ligadas por seta. itens: [(titulo, (numero, sufixo) ou None, [linhas])].

    Nada vai em cima da seta: o que liga as caixas vai numa faixa() abaixo. Devolve o y seguinte.
    """
    n, gap = len(itens), P(36)
    w = (LARG - 2 * M - gap * (n - 1)) // n
    h = max(_caixa_altura(dr, w, *it) for it in itens)
    for i, it in enumerate(itens):
        x = M + i * (w + gap)
        _caixa(dr, x, y, w, h, *it)
        if setas and i:
            seta(dr, x - gap + P(5), y + h // 2, x - P(5))
    return y + h


def linha_tempo(dr, y, marcos, trechos):
    """Marcos em ordem, com espaço igual, e o tempo entre eles escrito sobre o eixo.

    Escala proporcional ao tempo não serve: marcos que distam dias se amontoam e um período de meses ocupa o eixo inteiro.
    marcos:  [(rótulo, data como no documento, cor)]                 numerados 1, 2, 3... no eixo
    trechos: [([linhas acima do eixo], destaque)]                    um a menos que os marcos; destaque = traço vermelho
    Devolve o y seguinte.
    """
    n = len(marcos)
    cw = (LARG - 2 * M) / n
    xs = [M + cw * (i + 0.5) for i in range(n)]
    mw = cw - P(8)
    f1, f2, fm, r = F("rotulo", True), F("texto"), F("marco", True), P(8)
    nlin = lambda t: sum(len(quebra(dr, x, f2, mw)) for x in t)  # noqa: E731
    h_int = max([nlin(t) for t, _ in trechos] or [0]) * alt(f2)
    ye = y + h_int + P(6) + r
    for i, (t, dest) in enumerate(trechos):
        cor = VERMELHO if dest else CINZA
        dr.line([xs[i] + r, ye, xs[i + 1] - r, ye], fill=cor, width=P(3) if dest else P(1))
        yy = y + h_int - alt(f2) * nlin(t)
        for x in t:
            yy = centrado(dr, (xs[i] + xs[i + 1]) / 2, yy, x, f2, cor if dest else TEXTO, mw)
    yb = ye + r + P(6)
    fundo = yb
    for i, (rot, txt, cor) in enumerate(marcos):
        x = xs[i]
        dr.ellipse([x - r, ye - r, x + r, ye + r], fill=cor, outline="#FFFFFF", width=3)
        dr.text((x, ye), str(i + 1), font=fm, fill="#FFFFFF", anchor="mm")
        yy = centrado(dr, x, yb, rot, f1, cor, mw)
        fundo = max(fundo, centrado(dr, x, yy, txt or "—", f2, TEXTO, mw))
    return fundo


def frase(dr, y, txt, cor=AZUL):
    """Frase de conclusão em negrito, largura total; devolve o y seguinte."""
    return texto(dr, M, y, txt[:1].upper() + txt[1:], F("rotulo", True), cor, LARG - 2 * M)


def metadados():
    """Para o figuras.json de cada skill."""
    return {"fonte_tipografica": FR or "padrão do Pillow", "largura_cm": LARGURA_CM, "dpi": DPI, "pt_minimo": PT_MINIMO}
