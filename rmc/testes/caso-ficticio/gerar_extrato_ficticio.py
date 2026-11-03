#!/usr/bin/env python3
"""gerar_extrato_ficticio.py - cria um PDF FICTÍCIO com um cartão RMC e o histórico mensal de descontos.

Serve só para testar scripts/cartao.py e scripts/calcular_rmc.py. Todo dado é inventado. O layout (uma linha por
registro, "R$" colado ao valor) segue as expressões regulares do cartao.py herdado do AMN; NÃO é cópia de um extrato
real do INSS, e por isso não prova que o leitor funciona com o PDF verdadeiro (D18).

Variantes:
  atual   cartão incluído em 03/2022, 42 descontos de R$ 50,00 (falta 06/2024), refinanciamento em 11/2025
  antigo  as mesmas datas recuadas em 3 anos: refinanciamento em 11/2022, antes do prazo de 90 dias (bloqueio B2)

Uso: python3 gerar_extrato_ficticio.py saida.pdf [atual|antigo]
"""
import sys

DATA_EMISSAO = "28/10/2026 09:30:00"
NUMERO = "90000001"
BANCO = "318"


def competencias(deslocamento_anos):
    """Lista (competência MM/AAAA, desconto, saldo, utilizado, iof, extra) do histórico fictício."""
    linhas = []
    ano0, mes0 = 2022 + deslocamento_anos, 4  # primeira competência: abril
    n = 0
    while True:
        total = ano0 * 12 + (mes0 - 1) + n
        ano, mes = total // 12, total % 12 + 1
        if (ano, mes) > (2026 + deslocamento_anos, 9):
            break
        comp = f"{mes:02d}/{ano}"
        refin = (ano, mes) >= (2025 + deslocamento_anos, 11)
        ausente = (ano, mes) == (2024 + deslocamento_anos, 6)
        desconto = 55.00 if refin else 50.00
        if (ano, mes) == (2025 + deslocamento_anos, 11):
            saldo, utilizado, iof = 1800.00, 1800.00, 4.50
        elif refin:
            saldo, utilizado, iof = 1700.00, 30.00, 0.01
        else:
            saldo, utilizado, iof = 1000.00 + 5 * n % 300, 30.00, None
        if not ausente:
            linhas.append((comp, desconto, saldo, utilizado, iof, refin))
        n += 1
    return linhas


def brl(v):
    return "R$" + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def esc(t):
    return t.replace("\\", "\\\\").replace("(", r"\(").replace(")", r"\)")


def montar(variante):
    desl = 0 if variante == "atual" else -3
    ops = []
    y = [800]

    def texto(s, tam=7):
        ops.append(f"BT /F1 {tam} Tf 20 {y[0]} Td ({esc(s)}) Tj ET")
        y[0] -= 11

    texto("HISTÓRICO DE EMPRÉSTIMO CONSIGNADO (DADOS FICTÍCIOS)", 10)
    texto(f"Emitido em {DATA_EMISSAO}")
    texto("Benefício NB 999.999.999-9 Espécie 41 - Aposentadoria por idade")
    texto("VALORES DO BENEFÍCIO Base de cálculo R$1.621,00")
    texto("CARTÃO DE CRÉDITO", 9)
    inclusao = f"05/03/{22 + desl}"
    texto(f"{NUMERO} {BANCO} - BANCO BMG S.A. R$1.000,00Ativo Averbação Banco {inclusao} R$40,00")
    texto("Cartão de crédito (RMC)")
    texto("DESCONTOS DE CARTÃO", 9)
    for comp, desc, saldo, util, iof, refin in competencias(desl):
        id_ = f"{NUMERO}{BANCO}{comp.replace('/', '')}"
        texto(f"{id_} {BANCO} - BANCO BMG S.A. {brl(saldo)}Ativo {comp} {brl(util)}{brl(desc)}Desconto de cartão")
        if refin:
            texto(f"(RMC) {brl(iof)} 3,46 51,26 0,10 0,10")
        else:
            texto("(RMC)")
    return "\n".join(ops).encode("cp1252")


def pdf(conteudo):
    objs = []
    objs.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objs.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    objs.append(b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>")
    objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
    objs.append(b"<< /Length %d >>\nstream\n" % len(conteudo) + conteudo + b"\nendstream")
    out = bytearray(b"%PDF-1.4\n")
    pos = []
    for i, o in enumerate(objs, 1):
        pos.append(len(out))
        out += b"%d 0 obj\n" % i + o + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    for p in pos:
        out += b"%010d 00000 n \n" % p
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs) + 1, xref)
    return bytes(out)


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    variante = sys.argv[2] if len(sys.argv) == 3 else "atual"
    if variante not in ("atual", "antigo"):
        sys.exit(__doc__)
    open(sys.argv[1], "wb").write(pdf(montar(variante)))
    print("ok:", sys.argv[1])
