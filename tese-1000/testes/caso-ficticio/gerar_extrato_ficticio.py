#!/usr/bin/env python3
"""gerar_extrato_ficticio.py (tese-1000) - cria um PDF FICTÍCIO no formato de células do Histórico de Empréstimo Consignado.

Serve só para testar scripts/extrato.py. Todo dado é inventado. Escreve um PDF mínimo (Helvetica, WinAnsi) em que
cada célula é uma operação de texto separada, na ordem que o extrator espera. Não usa bibliotecas externas.

Uso: python3 gerar_extrato_ficticio.py saida.pdf
"""
import sys

DATA_EMISSAO = "28/10/2026 09:30:00"
LINHAS_ATIVO = [
    # contrato, banco, tipo, início, fim, qtde, parcela, situação, origem, inclusão, liberado
    ["51-000222/00002_0001", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "04/2024", "03/2031", "84", "R$ 50,00",
     "Ativo", "Averbação nova", "15/03/24", "R$ 2.100,00"],
    # processo 3: dois derivados da mesma raiz (2 dias e 79 dias depois da exclusão)
    ["51-000444/00004_0001", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "05/2023", "04/2030", "84", "R$ 40,00",
     "Ativo", "Averbação nova", "04/05/23", "R$ 1.500,00"],
    ["51-000444/00004_0002", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "08/2023", "07/2030", "84", "R$ 30,00",
     "Ativo", "Averbação nova", "20/07/23", "R$ 1.000,00"],
]
LINHAS_EXCLUIDO = [
    # ... + exclusão e motivo
    ["51-000111/00001", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "06/2015", "05/2018", "36", "R$ 33,75",
     "Excluído", "Averbação Banco", "05/05/15", "R$ 337,57", "11/08/18", "Exclusão Banco"],
    ["51-000111/00001_0001", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "09/2018", "07/2019", "33", "R$ 33,75",
     "Excluído", "Averbação nova", "11/08/18", "R$ 337,57", "15/08/19", "Exclusão Banco"],
    ["51-000222/00002", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "02/2020", "01/2024", "48", "R$ 50,00",
     "Excluído", "Averbação Banco", "10/01/20", "R$ 1.800,00", "15/03/24", "Exclusão Banco"],
    # processo 3: raiz
    ["51-000444/00004", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "11/2019", "04/2023", "42", "R$ 40,00",
     "Excluído", "Averbação Banco", "15/10/19", "R$ 1.200,00", "02/05/23", "Exclusão Banco"],
    # processo 4: troca de titularidade (raiz e derivado no banco anterior; o mesmo derivado migrado para o réu)
    ["51-000333/00003", "739 - BANCO CETELEM S.A.", "Empréstimo Pessoal", "06/2015", "05/2018", "36", "R$ 33,75",
     "Excluído", "Averbação Banco", "05/05/15", "R$ 337,57", "11/08/18", "Exclusão Banco"],
    ["51-000333/00003_0001", "739 - BANCO CETELEM S.A.", "Empréstimo Pessoal", "09/2018", "07/2019", "33", "R$ 33,75",
     "Excluído", "Averbação nova", "11/08/18", "R$ 337,57", "28/07/23", "Exclusão por troca de titularidade"],
    ["51-000333/00003_0001", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "08/2023", "08/2023", "33", "R$ 33,75",
     "Excluído", "Migrado do contrato 51-000333/00003_0001", "28/07/23", "R$ 0,00", "10/09/23", "Exclusão Banco"],
    # processo 5: derivado averbado ANTES da exclusão da raiz
    ["51-000555/00005", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "10/2020", "05/2023", "32", "R$ 20,00",
     "Excluído", "Averbação Banco", "10/09/20", "R$ 500,00", "15/06/23", "Exclusão Banco"],
    ["51-000555/00005_0001", "707 - BANCO DAYCOVAL S.A.", "Empréstimo Pessoal", "07/2023", "08/2023", "24", "R$ 20,00",
     "Excluído", "Averbação nova", "10/06/23", "R$ 400,00", "20/09/23", "Exclusão Banco"],
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
