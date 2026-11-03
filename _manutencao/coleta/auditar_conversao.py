"""Audita a conversão HTML -> Markdown contra um oráculo independente.

O oráculo lê o HTML original (o `.html.gz` guardado em `_fonte/`) e monta, com árvore de elementos e
fechamento implícito de `p`, `li`, `td`, `tr`, a sequência de palavras visíveis e, para cada
caractere, se ele aparece riscado (`<s>`, `<strike>`, `<del>` ou `text-decoration: line-through` em
ele mesmo ou em um ancestral). Não usa o conversor: se os dois erram do mesmo jeito, o erro não
aparece aqui, mas a pilha plana do conversor e a árvore do oráculo falham em casos diferentes.

O Markdown é lido de volta caractere a caractere (`~~`, `**`, `*`, escapes, tags de tabela) e
alinhado palavra a palavra com o oráculo. Saída:

- SUB    palavra riscada na página e sem riscado no .md (revogado apresentado como vigente);
- SOBRE  palavra sem riscado na página e riscada no .md (vigente apresentado como revogado);
- MISTA  palavra riscada só em parte, de um lado ou de outro (ex.: `<strike>5</strike>º`);
- TEXTO  palavra que existe só de um lado (perda ou acréscimo de conteúdo);
- ESTRUT rótulo de dispositivo (Art., §, Parágrafo) que abre parágrafo na página e não abre no .md
         (dispositivo colado ao anterior).

    python -I auditar_conversao.py fonte.html.gz saida.md [outro.md ...]
    python -I auditar_conversao.py fonte.html.gz saida.md --todos

Sai com código 1 se houver SUB, SOBRE, TEXTO ou ESTRUT no primeiro .md.
"""
import argparse
import difflib
import gzip
import html
import os
import re
import sys
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import decodificar  # noqa: E402

VOID = {"br", "img", "hr", "meta", "link", "input", "col", "wbr", "area", "base", "param", "basefont", "frame"}
INLINE = {"a", "b", "i", "u", "em", "strong", "span", "font", "strike", "s", "del", "ins", "sup", "sub",
          "small", "big", "abbr", "cite", "code", "q", "tt", "label"}
SKIP = {"head", "style", "script", "title", "xml"}
FECHA_P = {"p", "ul", "ol", "dl", "div", "table", "blockquote", "pre", "hr", "center", "form", "address",
           "h1", "h2", "h3", "h4", "h5", "h6", "li", "dd", "dt"}
ESCOPO = {"table", "td", "th", "li", "ul", "ol", "dl", "div", "blockquote", "body", "html", "caption", "center"}
INVISIVEL = dict.fromkeys(map(ord, "\ufeff\u200b\u200c\u200d\u00ad"), None)
SO_PONTUACAO = re.compile(r"^[—–#|>]+$")


ROTULOS = {"Art.", "Art", "Artigo", "§", "Parágrafo"}


class Palavra:
    __slots__ = ("t", "s", "n", "ini")

    def __init__(self, t, s, n, ini=False):
        self.t, self.s, self.n, self.ini = t, s, n, ini

    @property
    def marca(self):
        return "S" if self.s == self.n else ("N" if self.s == 0 else "M")


class Oraculo(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pilha = [["#raiz", False, False]]
        self.atual = []  # [(char, riscado)]
        self.palavras = []
        self.ini = True  # a próxima palavra abre parágrafo

    def _quebra(self):
        if self.atual:
            texto = "".join(c for c, _ in self.atual)
            self.palavras.append(Palavra(texto, sum(1 for _, s in self.atual if s), len(self.atual), self.ini))
            self.atual = []
            self.ini = False

    def _bloco(self):
        self._quebra()
        self.ini = True

    def _fechar_ate(self, alvos, limites):
        for k in range(len(self.pilha) - 1, 0, -1):
            tag = self.pilha[k][0]
            if tag in alvos:
                del self.pilha[k:]
                return
            if tag in limites:
                return

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self._fechar_ate({"head"}, set())
        if tag in FECHA_P:
            self._fechar_ate({"p"}, ESCOPO)
        if tag == "li":
            self._fechar_ate({"li"}, {"ul", "ol"})
        if tag in ("td", "th"):
            self._fechar_ate({"td", "th"}, {"table", "tr"})
        if tag == "tr":
            self._fechar_ate({"tr"}, {"table"})
        if tag in ("thead", "tbody", "tfoot"):
            self._fechar_ate({"thead", "tbody", "tfoot"}, {"table"})
        if tag == "br" or (tag not in INLINE and tag not in ("html", "body") and ":" not in tag):
            self._bloco()  # html/body: o Planalto às vezes reabre <html> no meio da frase
        if tag == "br":
            return
        if tag in VOID:
            return
        estilo = (dict(attrs).get("style") or "").replace(" ", "").lower()
        pai = self.pilha[-1]
        riscado = pai[1] or tag in ("s", "strike", "del") or "line-through" in estilo
        self.pilha.append([tag, riscado, pai[2] or tag in SKIP])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        bloco = tag not in INLINE and ":" not in tag
        for k in range(len(self.pilha) - 1, 0, -1):
            t = self.pilha[k][0]
            if t == tag:
                del self.pilha[k:]
                break
            if not bloco and t not in INLINE and ":" not in t:
                break  # fim de tag inline não atravessa bloco
        if bloco and tag not in ("html", "body"):
            self._bloco()

    def handle_data(self, data):
        topo = self.pilha[-1]
        if topo[2]:
            return
        for c in data.translate(INVISIVEL):
            if c.isspace():
                self._quebra()
            else:
                self.atual.append((c, topo[1]))

    def fim(self):
        self._quebra()
        return filtrar(self.palavras)


def filtrar(palavras):
    """Tira as palavras só de pontuação (travessão de título, '#'), passando o início de parágrafo adiante."""
    saida, carrega = [], False
    for p in palavras:
        if SO_PONTUACAO.match(p.t):
            carrega = carrega or p.ini
            continue
        if carrega:
            p.ini, carrega = True, False
        saida.append(p)
    return saida


def palavras_html(caminho):
    with gzip.open(caminho) as f:
        bruto = f.read()
    p = Oraculo()
    p.feed(decodificar(bruto))
    p.close()
    return p.fim()


PONT = set("\\`*_{}[]()#+-.!~|<>$%&'\":;,/?@^=")
ENTIDADE = re.compile(r"&(#\d+|#x[0-9a-fA-F]+|\w+);")
TAG = re.compile(r"</?([A-Za-z][\w:-]*)[^>]*>")


def palavras_md(texto, acervo=False):
    """Lê o .md de volta. `acervo=True`: formato de _acervo/normas (texto puro, um parágrafo por linha), onde
    '*', '\\', '<' e '&' são literais e só '~~' marca o riscado."""
    linhas = texto.split("\n")
    k = 0
    while k < len(linhas) and (not linhas[k].strip() or linhas[k].startswith(("# ", ">"))):
        k += 1
    texto = "\n".join(linhas[k:])
    atual, palavras = [], []
    riscado, dels = False, 0
    novo = [True]  # a próxima palavra abre parágrafo

    def quebra(bloco=False):
        if atual:
            palavras.append(Palavra("".join(c for c, _ in atual), sum(1 for _, s in atual if s), len(atual), novo[0]))
            atual.clear()
            novo[0] = False
        if bloco:
            novo[0] = True

    i, n = 0, len(texto)
    inicio_linha = True
    while i < n:
        c = texto[i]
        if not acervo and inicio_linha and c == "#":
            while i < n and texto[i] == "#":
                i += 1
            continue
        inicio_linha = c == "\n"
        if not acervo and c == "\\" and i + 1 < n and texto[i + 1] in PONT:
            atual.append((texto[i + 1], riscado or dels > 0))
            i += 2
        elif texto.startswith("~~", i):
            riscado = not riscado
            i += 2
        elif not acervo and c == "*":
            i += 1
        elif not acervo and c == "<":
            m = TAG.match(texto, i)
            if m:
                if m[1].lower() == "del":
                    dels = max(0, dels + (-1 if m[0].startswith("</") else 1))
                quebra(m[1].lower() in ("p", "tr", "td", "th", "table", "br", "div", "li"))
                i = m.end()
            else:
                atual.append((c, riscado or dels > 0))
                i += 1
        elif not acervo and c == "&" and (m := ENTIDADE.match(texto, i)):
            for ch in html.unescape(m[0]).translate(INVISIVEL):
                atual.append((ch, riscado or dels > 0))
            i = m.end()
        elif c.isspace():
            quebra(c == "\n")
            i += 1
        else:
            for ch in c.translate(INVISIVEL):
                atual.append((ch, riscado or dels > 0))
            i += 1
    quebra()
    return filtrar(palavras)


def contexto(palavras, i, antes=6, depois=6):
    return " ".join(p.t for p in palavras[max(0, i - antes):i + depois])


def comparar(ref, md):
    """Devolve dict categoria -> lista de (descrição, contexto)."""
    achados = {"SUB": [], "SOBRE": [], "MISTA": [], "TEXTO": [], "ESTRUT": []}
    a, b = [p.t for p in ref], [p.t for p in md]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    iguais = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            iguais += i2 - i1
            run, cat = [], None

            def fecha():
                if run:
                    achados[cat].append((" ".join(x for x, _ in run), contexto(ref, run[0][1])))
                run.clear()
            for off in range(i2 - i1):
                if ref[i1 + off].ini and not md[j1 + off].ini and ref[i1 + off].t in ROTULOS:
                    achados["ESTRUT"].append((f"{ref[i1 + off].t} {ref[i1 + off + 1].t if i1 + off + 1 < len(ref) else ''}",
                                              contexto(ref, i1 + off)))
                ma, mb = ref[i1 + off].marca, md[j1 + off].marca
                if ma == mb:
                    novo = None
                elif ma == "S" and mb == "N":
                    novo = "SUB"
                elif ma == "N" and mb == "S":
                    novo = "SOBRE"
                else:
                    novo = "MISTA"
                if novo != cat:
                    fecha()
                    cat = novo
                if novo:
                    run.append((ref[i1 + off].t, i1 + off))
            fecha()
        else:
            achados["TEXTO"].append((f"{op}: página=[{' '.join(a[i1:i2])[:160]}] md=[{' '.join(b[j1:j2])[:160]}]",
                                     contexto(ref, i1)))
    return achados, iguais


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fonte", help="HTML original (.html.gz)")
    ap.add_argument("md", nargs="+", help="um ou mais .md convertidos; o primeiro define o código de saída")
    ap.add_argument("--todos", action="store_true", help="lista todos os achados (padrão: 8 por categoria)")
    ap.add_argument("--acervo", action="store_true", help="os .md estão no formato de _acervo/normas (texto puro)")
    a = ap.parse_args()
    ref = palavras_html(a.fonte)
    riscadas = sum(1 for p in ref if p.marca == "S")
    print(f"página: {len(ref)} palavras, {riscadas} riscadas, "
          f"{sum(1 for p in ref if p.marca == 'M')} parcialmente riscadas")
    ruim = False
    for k, caminho in enumerate(a.md):
        with open(caminho, encoding="utf-8") as f:
            md = palavras_md(f.read(), acervo=a.acervo)
        achados, iguais = comparar(ref, md)
        resumo = " ".join(f"{c}={len(v)}" for c, v in achados.items())
        print(f"\n{os.path.basename(caminho)}: {len(md)} palavras, {riscadas and sum(1 for p in md if p.marca == 'S')} "
              f"riscadas | iguais={iguais} | {resumo}")
        for cat, itens in achados.items():
            for desc, ctx in (itens if a.todos else itens[:8]):
                print(f"  {cat:5} {desc[:230]}\n        ...{ctx[:200]}")
            if not a.todos and len(itens) > 8:
                print(f"  {cat:5} (+{len(itens) - 8} omitidos; use --todos)")
        if k == 0 and (achados["SUB"] or achados["SOBRE"] or achados["TEXTO"] or achados["ESTRUT"]):
            ruim = True
    return 1 if ruim else 0


if __name__ == "__main__":
    sys.exit(main())
