#!/usr/bin/env python3
"""valores.py - formatação de valores em reais, com extenso no estilo do escritório.

Usado por calcular.py (nao-contratado) e calcular_rmc.py (rmc). Testado contra 74 valores por extenso de petições
reais do escritório (nao-contratado/testes/casos-reais/teste_extenso.py).
"""

UN = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
      "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
DEZ = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
CEN = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
       "oitocentos", "novecentos"]


def _ate_mil(n):
    if n == 0:
        return ""
    if n == 100:
        return "cem"
    c, resto = divmod(n, 100)
    partes = [CEN[c]] if c else []
    if resto:
        partes.append(UN[resto] if resto < 20 else DEZ[resto // 10] + (f" e {UN[resto % 10]}" if resto % 10 else ""))
    return " e ".join(partes)


def inteiro_extenso(n):
    if n == 0:
        return "zero"
    milhoes, resto = divmod(n, 1_000_000)
    milhares, unidades = divmod(resto, 1000)
    partes = []  # (texto, valor do grupo)
    if milhoes:
        partes.append(("um milhão" if milhoes == 1 else f"{_ate_mil(milhoes)} milhões", milhoes))
    if milhares:
        # estilo do escritório: "um mil, duzentos…", mas "mil reais" quando o valor é exatamente 1.000
        partes.append((("um mil" if (unidades or milhoes) else "mil") if milhares == 1 else f"{_ate_mil(milhares)} mil", milhares))
    if unidades:
        partes.append((_ate_mil(unidades), unidades))
    if len(partes) == 1:
        return partes[0][0]
    ult_txt, ult_val = partes[-1]
    sep = " e " if (ult_val < 100 or ult_val % 100 == 0) else ", "
    return ", ".join(t for t, _ in partes[:-1]) + sep + ult_txt


def brl(v):
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def brl_ext(v):
    reais = int(round(v * 100)) // 100
    cent = int(round(v * 100)) % 100
    unidade = "real" if reais == 1 else ("de reais" if reais and reais % 1_000_000 == 0 else "reais")
    txt = f"{inteiro_extenso(reais)} {unidade}"
    if cent:
        txt += f" e {inteiro_extenso(cent)} {'centavo' if cent == 1 else 'centavos'}"
    return f"{brl(v)} ({txt})"
