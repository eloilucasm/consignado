#!/usr/bin/env python3
"""gerar_extrato_ficticio.py - cria um PDF FICTÍCIO no formato de células do Histórico de Empréstimo Consignado.

Serve só para testar scripts/extrato.py. Todo dado é inventado. Escreve um PDF mínimo (Helvetica, WinAnsi) em que
cada célula é uma operação de texto separada, na ordem que o extrator espera. Não usa bibliotecas externas.

Uso: python3 gerar_extrato_ficticio.py saida.pdf
"""
import sys

DATA_EMISSAO = "28/10/2026 09:30:00"
LINHAS_ATIVO = [
    # contrato, banco, tipo, início, fim, qtde, parcela, situação, origem, inclusão, liberado
    ["00555111222", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "09/2024", "08/2031", "84", "R$ 120,00",
     "Ativo", "Averbação Banco", "05/09/24", "R$ 4.200,00"],
]
LINHAS_EXCLUIDO = [
    # ... + exclusão e motivo
    ["00123456789", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "03/2019", "11/2021", "60", "R$ 142,50",
     "Excluído", "Averbação Banco", "20/02/19", "R$ 4.800,00", "15/12/21", "Exclusão Banco"],
    ["00987654321", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "05/2022", "02/2024", "72", "R$ 98,30",
     "Excluído", "Averbação Banco", "12/04/22", "R$ 3.100,00", "03/03/24", "Exclusão INSS"],
]


def esc(t):
    return t.replace("\\", "\\\\").replace("(", r"\(").replace(")", r"\)")


def montar():
    ops = []
    y = [800]

    def texto(x, s, tam=8):
        ops.append(f"BT /F1 {tam} Tf {x} {y[0]} Td ({esc(s)}) Tj ET")

    def linha(cels, tam=7):
        x = 20
        for c in cels:
            texto(x, c, tam)
            x += 42 if len(c) < 12 else 70
        y[0] -= 14

    texto(20, "HISTÓRICO DE EMPRÉSTIMO CONSIGNADO", 11); y[0] -= 16
    texto(20, f"Emitido em {DATA_EMISSAO}", 8); y[0] -= 12
    texto(20, "Benefício NB 999.999.999-9 Espécie 41 - Aposentadoria por idade (DADOS FICTÍCIOS)", 8); y[0] -= 20
    texto(20, "CONTRATOS ATIVOS E SUSPENSOS", 9); y[0] -= 14
    for r in LINHAS_ATIVO:
        for c in r:
            texto(20, c, 7); y[0] -= 0
        y[0] -= 14
    y[0] -= 10
    texto(20, "CONTRATOS EXCLUÍDOS E ENCERRADOS", 9); y[0] -= 14
    for r in LINHAS_EXCLUIDO:
        for c in r:
            texto(20, c, 7)
        y[0] -= 14
    y[0] -= 10
    texto(20, "CARTÃO DE CRÉDITO", 9); y[0] -= 14
    texto(20, "Nenhum cartão consignado registrado.", 7)
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
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    open(sys.argv[1], "wb").write(pdf(montar()))
    print("ok:", sys.argv[1])
