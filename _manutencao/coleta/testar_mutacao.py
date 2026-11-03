"""Valida o comparador por mutação: injeta defeitos conhecidos num texto e exige que sejam reprovados.

Um auditor que aprova tudo também "passa" na regressão. Aqui, para cada .md, o texto original é a
referência e cada mutante (uma palavra apagada, um parágrafo apagado, um dígito trocado, `Art.` colado ao
parágrafo anterior, parágrafo duplicado, palavra trocada, final truncado) é comparado com ela com o mesmo
`auditar_conversao.comparar` que o coletor usa. O controle negativo (texto sem mutação) tem de ser
APROVADO. Sai com 1 se algum mutante escapar ou o controle falhar.

    python -I testar_mutacao.py ../../../_coleta-pdf/res-cmn-4549-consolidada.md [outro.md ...]
"""
import argparse
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auditar_conversao as A  # noqa: E402
sys.stdout.reconfigure(encoding="utf-8")  # console do Windows grava cp1252 por padrão

CATS = ("SUB", "SOBRE", "TEXTO", "ESTRUT")  # MISTA não se aplica a PDF (sem riscado)


def corpo(texto):
    """Corpo do arquivo: depois do cabeçalho de linhas '#'/'>' (a mesma regra de palavras_md)."""
    linhas = texto.split("\n")
    k = 0
    while k < len(linhas) and (not linhas[k].strip() or linhas[k].startswith(("# ", ">"))):
        k += 1
    return linhas[:k], linhas[k:]


def mutantes(cab, linhas, rng, n):
    """Gera (nome, texto) com `n` mutantes de cada tipo. Parágrafos = linhas não vazias do corpo."""
    idx = [i for i, l in enumerate(linhas) if l.strip()]
    art = [i for i in idx if re.match(r"(Art\.|§)\s*\d", linhas[i]) and i > idx[0]]
    com_digito = [i for i in idx if re.search(r"\d", linhas[i])]
    saida = []

    def montar(novas):
        return "\n".join(cab + novas)

    for _ in range(n):
        i = rng.choice(idx)
        pal = linhas[i].split(" ")
        if len(pal) > 4:  # palavra do meio apagada
            k = rng.randrange(1, len(pal) - 1)
            novas = list(linhas)
            novas[i] = " ".join(pal[:k] + pal[k + 1:])
            saida.append(("palavra apagada", montar(novas)))
        novas = list(linhas)
        del novas[i]
        saida.append(("parágrafo apagado", montar(novas)))
        novas = list(linhas)
        novas.insert(i, linhas[i])
        saida.append(("parágrafo duplicado", montar(novas)))
        pal = linhas[i].split(" ")
        if len(pal) > 4:
            k = rng.randrange(1, len(pal) - 1)
            novas = list(linhas)
            novas[i] = " ".join(pal[:k] + ["não"] + pal[k:])
            saida.append(("palavra inserida", montar(novas)))
            novas = list(linhas)
            novas[i] = " ".join(pal[:k] + [pal[k][::-1] + "x"] + pal[k + 1:])
            saida.append(("palavra trocada", montar(novas)))
    for i in rng.sample(com_digito, min(n, len(com_digito))):
        novas = list(linhas)
        novas[i] = re.sub(r"\d", lambda m: str((int(m[0]) + 1) % 10), linhas[i], count=1)
        saida.append(("dígito trocado", montar(novas)))
    for i in rng.sample(art, min(n, len(art))):  # tira a linha em branco: dispositivo colado ao anterior
        novas = list(linhas)
        j = i - 1
        while j >= 0 and not novas[j].strip():
            j -= 1
        novas[j] = novas[j] + " " + novas[i]
        del novas[i]
        saida.append(("dispositivo colado", montar(novas)))
    corte = idx[int(len(idx) * 0.9)]
    saida.append(("final truncado", montar(linhas[:corte])))
    return saida


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("md", nargs="+")
    ap.add_argument("-n", type=int, default=8, help="mutantes de cada tipo por arquivo")
    ap.add_argument("--semente", type=int, default=1)
    a = ap.parse_args()
    falhou = False
    for caminho in a.md:
        with open(caminho, encoding="utf-8") as f:
            texto = f.read()
        cab, linhas = corpo(texto)
        ref = A.palavras_md(texto, acervo=True)
        achados, _ = A.comparar(ref, A.palavras_md(texto, acervo=True))
        controle = not any(achados[c] for c in CATS)
        por_tipo = {}
        for nome, mut in mutantes(cab, linhas, random.Random(a.semente), a.n):
            achados, _ = A.comparar(ref, A.palavras_md(mut, acervo=True))
            pego = any(achados[c] for c in CATS)
            tot, ok = por_tipo.get(nome, (0, 0))
            por_tipo[nome] = (tot + 1, ok + pego)
        escaparam = sum(t - o for t, o in por_tipo.values())
        print(f"{os.path.basename(caminho)}: controle {'APROVADO' if controle else 'FALHOU'} | "
              + " | ".join(f"{k} {o}/{t}" for k, (t, o) in por_tipo.items()))
        falhou |= (not controle) or escaparam > 0
    print("RESULTADO: " + ("REPROVADO (auditor deixa defeito passar)" if falhou else "APROVADO (todos os mutantes pegos)"))
    return 1 if falhou else 0


if __name__ == "__main__":
    sys.exit(main())
