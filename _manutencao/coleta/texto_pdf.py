"""Texto de `pdftotext -layout` -> formato de `_acervo/normas`.

Formato: texto puro, um parágrafo por linha, linha em branco entre parágrafos, `Art.` e `§` no início da
linha. PDF não traz riscado, então não há `~~`: o revogado aparece como nota textual ("Revogado pela ...").

Passos: (1) tirar cabeçalho e rodapé de página, que se repetem com o número da página trocado; (2) juntar
as linhas quebradas pela largura da página, abrindo parágrafo novo só onde começa um dispositivo.
"""
import collections
import re

# Abre parágrafo: dispositivos e divisões. Maiúscula/minúscula importa: "art. 6º" no meio de frase não abre.
ABRE = re.compile(
    r"^(?:Art\.\s*\d|Art\s+\d|§\s*\d|Parágrafo único|[IVXLCDM]+\s*[-–—]\s|[a-z]{1,2}\)\s|\d+\.\s|"
    r"TÍTULO\b|CAPÍTULO\b|SEÇÃO\b|SUBSEÇÃO\b|LIVRO\b|PARTE\b|ANEXO\b|Seção\b|Subseção\b|Capítulo\b)")
RODAPE_PAGINA = re.compile(r"\bP[áa]gina\s+\d+\s+de\s+\d+\b", re.I)
SO_NUMERO = re.compile(r"^\d{1,3}$")
INVISIVEL = dict.fromkeys(map(ord, "﻿​‌‍­"), None)


def escaneado(texto):
    """Pouco texto por página = PDF de imagem. Sem OCR no coletor: a fonte é recusada."""
    paginas = max(1, len([p for p in texto.split("\f") if p.strip()]))
    return len(re.sub(r"\W", "", texto)) / paginas < 300


def _chave(linha):
    return re.sub(r"\d+", "#", re.sub(r"\s+", " ", linha).strip())


def sem_cabecalho_rodape(texto):
    """Remove linhas que se repetem na maioria das páginas (com o número trocado) e 'Página N de M'.

    Só a primeira e a última linha de texto de cada página são candidatas, para nunca apagar corpo.
    Devolve (texto, removidas), onde `removidas` é a lista do que foi tirado (vai para o manifesto).
    """
    paginas = [p.split("\n") for p in texto.split("\f")]
    paginas = [p for p in paginas if any(l.strip() for l in p)]
    bordas = []
    for p in paginas:
        idx = [i for i, l in enumerate(p) if l.strip()]
        bordas.append({idx[0], idx[-1]} if idx else set())
    freq = collections.Counter(_chave(p[i]) for p, b in zip(paginas, bordas) for i in b)
    limite = max(2, len(paginas) / 2)
    removidas, saida = [], []
    for p, b in zip(paginas, bordas):
        for i, l in enumerate(p):
            c = _chave(l)
            apagar = l.strip() and (
                RODAPE_PAGINA.search(l) or SO_NUMERO.match(l.strip()) and i in b
                or i in b and freq[c] >= limite and not ABRE.match(l.strip()))
            if apagar:
                removidas.append(l.strip())
            else:
                saida.append(l)
        saida.append("")  # a quebra de página separa parágrafo
    return "\n".join(saida), removidas


def para_acervo(texto):
    texto, _ = sem_cabecalho_rodape(texto.translate(INVISIVEL).replace("\r", ""))
    paras, atual = [], []

    def fecha():
        if atual:
            paras.append(re.sub(r"\s+", " ", " ".join(atual)).strip())
            atual.clear()

    for linha in texto.split("\n"):
        l = linha.strip().replace("\xa0", " ")
        if not l:
            fecha()
            continue
        if atual and ABRE.match(l):
            fecha()
        atual.append(l)
    fecha()
    return "\n\n".join(p for p in paras if p)
