#!/usr/bin/env python3
"""cartao.py - adaptado de triagem-consignado/scripts/cartao.py (AMN v1.4), sem alteração de lógica.
NÃO validado com extrato real do INSS neste pacote: só com o extrato fictício de rmc/testes/caso-ficticio (D18).

Leitura dos cartões consignados (RMC/RCC) do Histórico de Empréstimo Consignado
do INSS e cálculo da tese do refinanciamento compulsório (Lei 14.690/2023).

- contrato do cartão (seção "CARTÃO DE CRÉDITO - RMC/RCC"): limite, inclusão, situação;
- histórico mensal (seção "DESCONTOS DE CARTÃO"): competência, saldo devedor,
  utilizado no mês, desconto, IOF, CET e taxa de juros;
- detecção do refinanciamento: competência em que o "utilizado no mês" salta para
  (quase) todo o saldo devedor, com IOF — sinais usados na inicial de referência;
- planilha de pagamentos acumulados, marco de 200% do capital, totais e onerosidade.

Uso: python3 cartao.py EXTRATO.pdf NUMERO_DO_CARTAO
"""
import json
import re
import sys

import pypdf

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RE_REAL = r"R\$([\d.]+,\d{2})"


def v(s):
    return float(s.replace(".", "").replace(",", ".")) if s else None


def texto(caminho):
    return "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(str(caminho)).pages)


def comp_n(c):
    m, a = c.split("/")
    return int(a) * 12 + int(m) - 1


def comp_s(n):
    return f"{n % 12 + 1:02d}/{n // 12}"


def contrato_cartao(txt, numero):
    """Linha do contrato na seção CARTÃO DE CRÉDITO: limite, situação, inclusão."""
    m = re.search(rf"(?m)^{re.escape(numero)} (\d{{3}}) - (.+?) {RE_REAL}\s*(\w+)\s+(.+?)\s+(\d{{2}}/\d{{2}}/\d{{2}})\s+{RE_REAL}",
                  txt)
    if not m:
        return None
    tipo = re.search(r"\((RMC|RCC)\)", txt[m.end():m.end() + 200])
    return {"numero": numero, "banco_cod": m.group(1), "banco": m.group(2).strip(), "limite": v(m.group(3)),
            "situacao": m.group(4), "origem": m.group(5).strip(), "inclusao": m.group(6),
            "reservado": v(m.group(7)), "tipo": tipo.group(1) if tipo else None}


def _recompor(txt):
    """O PDF quebra o identificador da linha em duas: "12345678900011202" + "2 318 - BANCO..." (NB + "00" + MMAAAA). Junta."""
    return re.sub(r"(?m)^(\d{8,})\n(\d{1,6} \d{3} - )", r"\1\2", txt)


def _linhas(txt, banco_cod):
    pad = re.compile(rf"(?m)^(\d+) {banco_cod} - .+? {RE_REAL}(\w+) (\d{{2}}/\d{{4}}) {RE_REAL}{RE_REAL}"
                     rf"Descont[oe] de cart[aã]o\s*\n?\s*\((RMC|RCC)\)"
                     rf"(?: {RE_REAL} ([\d,]+) ([\d,]+) ([\d,]+) ([\d,]+))?")
    for m in pad.finditer(_recompor(txt)):
        yield {"id": m.group(1), "competencia": m.group(4), "saldo": v(m.group(2)), "situacao": m.group(3),
               "utilizado": v(m.group(5)), "desconto": v(m.group(6)), "tipo": m.group(7), "iof": v(m.group(8)),
               "cet_m": v(m.group(9)), "cet_a": v(m.group(10)), "juros_m": v(m.group(11)), "juros_a": v(m.group(12))}


def cadeia(txt, banco_cod, tipo):
    """Cartões do mesmo banco e tipo na seção CARTÃO DE CRÉDITO (ativos e excluídos), em ordem de inclusão,
    com data de exclusão quando houver."""
    out = []
    for m in re.finditer(rf"(?m)^(\d+) {banco_cod} - .+? {RE_REAL}\s*(\w+)\s+(.+?)\s+(\d{{2}}/\d{{2}}/\d{{2}})\s+"
                         rf"{RE_REAL}(?:\s+(\d{{2}}/\d{{2}}/\d{{2}}))?", txt):
        trecho = txt[m.end():m.end() + 160]
        t = re.search(r"\((RMC|RCC)\)", trecho)
        if t and t.group(1) != tipo:
            continue
        mot = re.match(r"\s*(Exclus[ãa]o\s*\n?\s*\w+)", trecho)
        out.append({"numero": m.group(1), "limite": v(m.group(2)), "situacao": m.group(3), "inclusao": m.group(5),
                    "exclusao": m.group(7), "motivo": re.sub(r"\s+", " ", mot.group(1)) if mot else None})
    data = lambda d: (int(d[6:]), int(d[3:5]), int(d[:2]))
    return sorted(out, key=lambda c: data(c["inclusao"]))


def historico(txt, numero, banco_cod, nb=None):
    """Histórico do cartão. Linhas com o número do cartão (id = cartão + banco + MMAAAA) e, quando informado o
    NB, também as linhas antigas que o INSS registrou só com o código do benefício (id = NB + "00" + MMAAAA),
    atribuídas a este cartão no período em que ele era o cartão vigente do banco (entre a sua inclusão e a
    sua exclusão/hoje), sem sobrepor competências que já tenham linha própria."""
    proprias, genericas = {}, {}
    nbd = re.sub(r"\D", "", nb or "")
    for l in _linhas(txt, banco_cod):
        mmaaaa = l["competencia"].replace("/", "")
        if l["id"] == f"{numero}{banco_cod}{mmaaaa}":
            proprias[l["competencia"]] = {**l, "origem_linha": "cartão"}
        elif nbd and l["id"] == f"{nbd}00{mmaaaa}":
            genericas[l["competencia"]] = {**l, "origem_linha": "código do benefício"}
    if genericas:
        cart = next((c for c in cadeia(txt, banco_cod, next(iter(genericas.values()))["tipo"]) if c["numero"] == numero),
                    None)
        if cart:
            ini = comp_n(f"{cart['inclusao'][3:5]}/20{cart['inclusao'][6:]}")
            fim = comp_n(f"{cart['exclusao'][3:5]}/20{cart['exclusao'][6:]}") if cart.get("exclusao") else 10 ** 6
            for c, l in genericas.items():
                if ini < comp_n(c) <= fim and c not in proprias:
                    proprias[c] = l
    return [proprias[k] for k in sorted(proprias, key=comp_n)]


def continuidade(hist):
    """Pontos em que a linha muda de origem (código do benefício -> número do cartão): compara o saldo devedor
    dos dois lados — se for contínuo, é a mesma conta do cartão."""
    pts = []
    for a, b in zip(hist, hist[1:]):
        if a.get("origem_linha") != b.get("origem_linha") and a.get("saldo") and b.get("saldo"):
            pts.append({"de": a["competencia"], "para": b["competencia"], "saldo_de": a["saldo"],
                        "saldo_para": b["saldo"], "variacao": abs(b["saldo"] - a["saldo"]) / a["saldo"]})
    return pts


def detectar_refinanciamento(hist):
    """Competências em que o utilizado no mês ≈ saldo devedor (≥ 90%), bem acima do
    desconto mensal (≥ 5x), com IOF lançado. Devolve a lista (normalmente uma)."""
    achados = []
    for i, h in enumerate(hist):
        if not (h["utilizado"] and h["saldo"] and h["desconto"]):
            continue
        if h["utilizado"] >= 0.9 * h["saldo"] and h["utilizado"] >= 5 * h["desconto"] and (h["iof"] or 0) > 0:
            vizinhos = [x["juros_m"] for x in hist[max(0, i - 3):i] + hist[i + 1:i + 4] if x.get("juros_m")]
            achados.append({**h, "juros_vizinhos": vizinhos,
                            "utilizado_vizinhos": [x["utilizado"] for x in hist[max(0, i - 2):i]]})
    return achados


def calcular(hist, capital, refin_comp, comp_ref):
    """Planilha acumulada, marco de 200% e totais."""
    plan, acum, marco = [], 0.0, None
    for h in hist:
        if comp_n(h["competencia"]) > comp_ref:
            continue
        acum = round(acum + (h["desconto"] or 0), 2)
        pct = acum / capital * 100 if capital else None
        plan.append({**h, "acumulado": acum, "pct": pct})
        if marco is None and pct is not None and pct >= 200:
            marco = h["competencia"]
    r = comp_n(refin_comp) if refin_comp else None
    ate_refin = round(sum(p["desconto"] or 0 for p in plan if r is not None and comp_n(p["competencia"]) < r), 2)
    pos_refin = round(sum(p["desconto"] or 0 for p in plan if r is not None and comp_n(p["competencia"]) >= r), 2)
    total = plan[-1]["acumulado"] if plan else 0.0
    ausentes = []
    if plan:
        presentes = {comp_n(p["competencia"]) for p in plan}
        ausentes = [comp_s(n) for n in range(comp_n(plan[0]["competencia"]), comp_n(plan[-1]["competencia"]) + 1)
                    if n not in presentes]
    return {"planilha": plan, "marco_200": marco, "total_ate_refin": ate_refin, "total_pos_refin": pos_refin,
            "total_pago": total, "ausentes": ausentes,
            "primeira": plan[0]["competencia"] if plan else None, "ultima": plan[-1]["competencia"] if plan else None}


if __name__ == "__main__":
    t = texto(sys.argv[1])
    c = contrato_cartao(t, sys.argv[2])
    print(json.dumps(c, ensure_ascii=False))
    h = historico(t, sys.argv[2], c["banco_cod"], sys.argv[3] if len(sys.argv) > 3 else None)
    print("cadeia:", json.dumps(cadeia(t, c["banco_cod"], c["tipo"] or "RMC"), ensure_ascii=False))
    print("continuidade:", continuidade(h))
    print(len(h), "competências:", h[0]["competencia"] if h else None, "→", h[-1]["competencia"] if h else None)
    ref = detectar_refinanciamento(h)
    print("refinanciamento:", json.dumps(ref, ensure_ascii=False))
    r = calcular(h, c["limite"], ref[0]["competencia"] if ref else None, 10 ** 6)
    print({k: v for k, v in r.items() if k != "planilha"})
