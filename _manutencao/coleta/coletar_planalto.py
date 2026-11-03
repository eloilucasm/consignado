"""Coleta do Planalto as normas do acervo, preservando o texto riscado (revogado ou superado).

Derivado de `scripts/baixar_planalto.py` do repositório ctresb/leis (MIT; ver NOTICE.md). Mudanças:
lista de normas própria (NORMAS), cabeçalho no formato do acervo (`_acervo/normas/*.md`), saída em
pasta à escolha (para comparar com o acervo antes de substituir qualquer arquivo), download com
retentativa e auditoria automática da conversão (`auditar_conversao.py`).

O texto riscado é mantido como `~~...~~`: ele pode reger fatos da sua época. O HTML original fica
em `_fonte/` (gzip), para auditar a conversão.

Cada norma é conferida, palavra a palavra, contra o HTML original. Se a conversão perder texto,
inverter riscado ou colar dispositivos, o arquivo é gravado mesmo assim, a norma sai marcada
REPROVADA e o código de saída é 1: não use um arquivo reprovado no acervo.

    python -I coletar_planalto.py --saida ../../../_coleta-teste lei-14905
    python -I coletar_planalto.py --saida ../../../_coleta-teste          # todas as normas da lista
"""
import argparse
import datetime as dt
import gzip
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import Rede, decodificar  # noqa: E402
from html2md import convert, escape_inline  # noqa: E402
import auditar_conversao  # noqa: E402

BASE = "https://www.planalto.gov.br/ccivil_03/"
UA = "Mozilla/5.0 (compatible; acervo-md/1.0)"
BRASAO = re.compile(r"<img\b[^>]*\bsrc=[\"']?[^\"'\s>]*(?:Brastra\.gif|brasao\.png)[\"']?[^>]*>", re.I)
TABELA = re.compile(r"<table\b.*?</table>", re.S | re.I)
# Lei citada em nota de alteração: "(Redação dada pela Lei nº 15.068, de 2024)" e afins.
NOTA_LEI = re.compile(
    r"\((?:[^()]*?)\b(?:Redação dada|Incluíd[oa]|Alterad[oa]|Acrescid[oa]|Revogad[oa]|Suprimid[oa]|Vetad[oa]|"
    r"Renumerad[oa]|Regulamento|Vide|Produção de efeitos|Vigência|Convertid[oa])\b[^()]*?\bLei\s+n[ºo]\s*([\d.]+)",
    re.I)

AVISO = ('Transcrição literal do texto consolidado. Trechos ~~riscados~~ estão revogados ou '
         'superados: não os cite como vigentes, mas eles podem reger fatos da sua época (ver '
         '"Texto vigente e texto revogado" no protocolo). Conferir a redação vigente ao fato '
         'gerador e eventual alteração posterior à data da consulta.')

# (arquivo, URL relativa ao ccivil_03, título do cabeçalho)
NORMAS = [
    ("lei-14905", "_ato2023-2026/2024/lei/l14905.htm", "Lei nº 14.905/2024 — Atualização monetária e juros"),
    ("lei-10820", "leis/2003/l10.820.htm", "Lei nº 10.820/2003 — Crédito consignado"),
    ("lei-9099", "leis/l9099.htm", "Lei nº 9.099/1995 — Juizados Especiais"),
    ("lei-10741", "leis/2003/l10.741.htm", "Lei nº 10.741/2003 — Estatuto da Pessoa Idosa"),
    ("cdc", "leis/l8078compilado.htm", "Lei nº 8.078/1990 — Código de Defesa do Consumidor"),
    ("cc", "leis/2002/l10406compilada.htm", "Lei nº 10.406/2002 — Código Civil"),
    ("cpc", "_ato2015-2018/2015/lei/l13105.htm", "Lei nº 13.105/2015 — Código de Processo Civil"),
    ("lgpd", "_ato2015-2018/2018/lei/l13709.htm", "Lei nº 13.709/2018 — LGPD"),
    ("lei-14690", "_ato2023-2026/2023/lei/l14690.htm", "Lei nº 14.690/2023 — Programa Desenrola Brasil"),
    ("cf88", "constituicao/constituicaocompilado.htm", "Constituição da República Federativa do Brasil de 1988"),
    ("dec-12797", "_ato2023-2026/2025/decreto/d12797.htm", "Decreto nº 12.797/2025 — Salário mínimo a partir de 1º/1/2026"),
    ("lei-14063", "_ato2019-2022/2020/lei/l14063.htm", "Lei nº 14.063/2020 — Assinaturas eletrônicas"),
    ("mp-2200-2", "mpv/antigas_2001/2200-2.htm", "Medida Provisória nº 2.200-2/2001 — ICP-Brasil"),
]

MARCAS = {"del": "\x01", "strong": "\x02", "em": "\x03"}
MARCADORES = (("\x01", "~~"), ("\x02", "**"), ("\x03", "*"))
QUEBRAM_LINHA = {"p", "br", "tr", "table", "div", "li"}


def texto_da_tabela(fragmento, linhas):
    """Tira as tags de um pedaço de tabela, mantendo riscado (~~), negrito e itálico.

    O conversor escreve tabela como HTML cru; no cabeçalho e nos índices isso só polui. Com
    `linhas`, p/br/tr viram quebra de linha; sem ele, tudo vira espaço.
    """
    saida = []
    for parte in re.split(r"(<[^>]+>)", fragmento):
        if parte.startswith("<"):
            m = re.match(r"</?\s*([A-Za-z][\w:-]*)", parte)
            nome = m[1].lower() if m else ""
            if nome in MARCAS:
                saida.append(MARCAS[nome])
            else:
                saida.append("\n" if linhas and nome in QUEBRAM_LINHA else " ")
        else:
            saida.append(escape_inline(html.unescape(parte)))
    s = re.sub(r"[ \t\xa0]+", " ", "".join(saida))
    for marca, md in MARCADORES:
        s = re.sub(marca + r"[ \t]*(.*?)[ \t]*" + marca, lambda m, md=md: md + m[1] + md if m[1].strip() else " ", s)
        s = s.replace(marca, "")
    return "\n".join(l for l in (re.sub(r" {2,}", " ", l).strip() for l in s.split("\n")) if l)


def tabela_de_uma_coluna(m):
    """Índice de uma célula por linha vira uma linha por item; as demais tabelas ficam como estão."""
    tab = m[0]
    if len(re.findall(r"<table\b", tab, re.I)) != 1:
        return tab
    if not re.sub(r"<[^>]*>|&nbsp;|\s", "", tab):
        return ""  # tabela de layout sem texto
    linhas = re.findall(r"<tr\b[^>]*>(.*?)</tr>", tab, re.S | re.I)
    if not linhas or any(len(re.findall(r"<t[dh]\b", l, re.I)) != 1 for l in linhas):
        return tab
    return "\n\n".join(t for t in (texto_da_tabela(l, False) for l in linhas) if t)


def achatar_tabelas(corpo):
    """Cabeçalho (antes do art. 1º): toda tabela vira texto. Corpo: só índice de uma coluna."""
    m = re.search(r"^(?:\*\*)?Art(?:igo)?\.?\s*1(?!\d)", corpo, re.M)
    corte = m.start() if m else 0
    cab, resto = corpo[:corte], corpo[corte:]
    cab = TABELA.sub(lambda t: "\n\n" + texto_da_tabela(t[0], True) + "\n\n", cab)
    cab = re.sub(r"\n\s*\n+", "\n\n", cab).strip() + "\n\n"
    return cab + TABELA.sub(tabela_de_uma_coluna, resto)


TITULO_DIVISAO = re.compile(r"^(?:~~)?(?:PARTE|LIVRO|TÍTULO|CAPÍTULO|SEÇÃO|SUBSEÇÃO)\b", re.I)


def formato_acervo(corpo):
    """Markdown do conversor -> formato de `_acervo/normas`: texto puro, um parágrafo por linha, linha em branco entre eles.

    É o que `gerar-mapa.py`, `gerar-estrutura.js` e `verificar-pacote.js` leem: `Art.` e `§` no início da linha,
    divisões sem '#', riscado como `~~...~~` e nenhum '**' ou '\\'.
    """
    linhas = []
    for linha in corpo.split("\n"):
        divisao = linha.startswith("#")
        l = re.sub(r"^#{1,6}\s+", "", linha)
        if divisao and TITULO_DIVISAO.match(l):
            l = l.replace(" — ", " ", 1)  # a página junta 'CAPÍTULO I' e o nome com <br>, que o acervo lê como espaço
        l = re.sub(r"(?<!\\)\*+", "", l)  # negrito e itálico; o '*' literal vem escapado
        l = re.sub(r"\\([\\*_])", r"\1", l).replace("&lt;", "<").strip()
        if l:
            linhas.append(l)
    return "\n\n".join(linhas)


def ultima_alteracao(corpo):
    numeros = [int(n.replace(".", "")) for n in NOTA_LEI.findall(corpo)]
    return f"{max(numeros):,}".replace(",", ".") if numeros else "—"


def coletar(rede, arquivo, rel, titulo, saida, recorte="texto integral", auditar=True, formato="acervo"):
    url = BASE + rel
    status, bruto, ct = rede.get(url, accept="text/html", tentativas=4, timeout=180)
    if status != 200 or len(bruto) < 3000:
        raise ValueError(f"resposta inválida (HTTP {status}, {len(bruto)} bytes): {url}")
    fonte = os.path.join(saida, "_fonte", arquivo + ".html.gz")
    os.makedirs(os.path.dirname(fonte), exist_ok=True)
    with gzip.open(fonte, "wb") as f:
        f.write(bruto)
    # Só o brasão do cabeçalho é descartado; outra imagem em tabela continua barrando a conversão.
    html_texto = BRASAO.sub("", decodificar(bruto, ct))
    corpo = achatar_tabelas(convert(html_texto))  # preserva o riscado
    if formato == "acervo":
        corpo = formato_acervo(corpo)
    if not re.search(r"\bArt(?:igo)?\.?\s*\d", corpo, re.I):
        raise ValueError(f"fonte sem corpo normativo extraível: {url}")
    cab = (f"# {titulo}\n\n> Fonte: <{url}>\n"
           f"> Consulta: {dt.date.today().isoformat()} · recorte: {recorte} · "
           f"alteração mais recente pelas notas do texto: {ultima_alteracao(corpo)}\n"
           f"> {AVISO}\n\n")
    md = os.path.join(saida, arquivo + ".md")
    texto = cab + corpo + "\n"
    with open(md + ".tmp", "w", encoding="utf-8") as f:
        f.write(texto)
    os.replace(md + ".tmp", md)
    achados = None
    if auditar:
        achados, _ = auditar_conversao.comparar(auditar_conversao.palavras_html(fonte),
                                                auditar_conversao.palavras_md(texto, acervo=(formato == "acervo")))
    return md, corpo.count("~~") // 2, len(TABELA.findall(corpo)), achados


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivos", nargs="*", help="nomes da lista NORMAS (padrão: todas)")
    ap.add_argument("--saida", required=True, help="pasta de saída (não use _acervo/normas sem comparar antes)")
    ap.add_argument("--rps", type=float, default=1)
    ap.add_argument("--sem-auditoria", action="store_true", help="não confere a conversão contra o HTML")
    ap.add_argument("--md-rico", action="store_true", help="Markdown com negrito e '#' em vez do formato de _acervo/normas")
    a = ap.parse_args()
    rede = Rede(a.rps, headers={"User-Agent": UA})
    ruins = 0
    for arq, rel, titulo in NORMAS:
        if a.arquivos and arq not in a.arquivos:
            continue
        try:
            md, riscados, tabelas, achados = coletar(rede, arq, rel, titulo, a.saida, auditar=not a.sem_auditoria,
                                                     formato="md" if a.md_rico else "acervo")
        except Exception as e:
            ruins += 1
            print(f"erro {arq}: {str(e)[:200]}", flush=True)
            continue
        if achados is None:
            veredito = "sem auditoria"
        else:
            resumo = " ".join(f"{k}={len(v)}" for k, v in achados.items())
            veredito = ("APROVADA " if not any(achados.values()) else "REPROVADA ") + resumo
            ruins += any(achados.values())
        extra = f", {tabelas} tabela(s) HTML mantida(s)" if tabelas else ""
        print(f"{arq}: {riscados} trechos riscados{extra} | {veredito} -> {md}", flush=True)
    return 1 if ruins else 0


if __name__ == "__main__":
    sys.exit(main())
