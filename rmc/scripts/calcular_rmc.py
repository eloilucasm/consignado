#!/usr/bin/env python3
"""calcular_rmc.py - cálculo da inicial de refinanciamento de cartão consignado (RMC/RCC).

Lê o cartão e o histórico mensal do extrato do INSS (cartao.py), detecta o refinanciamento, monta a planilha acumulada,
acha o marco de 200% do capital e calcula o dobro do que foi descontado desde o refinanciamento e o valor da causa.
Todo número sai como CÁLCULO A CONFERIR.

Trava (para sem gravar): nenhum refinanciamento detectado; histórico incompleto sem --historico-extra; 200% não atingido
antes do refinanciamento; mais de um cartão no processo.
Alerta jurídico (não bloqueia; decisão do escritório de 29/10/2026): refinanciamento anterior ao fim do prazo de 90 dias
do art. 28, § 1º, da Lei 14.690/2023 (ver references/01-tese-e-roteiro.md, B2).

Uso:
  python3 calcular_rmc.py --ficha ficha.json --processo 1 --extrato extrato.pdf --data 2026-10-28 --saida pasta/
                          [--historico-extra historico.csv]
historico.csv (opcional): competências que faltam no extrato, "MM/AAAA;valor;fonte" (ex.: "03/2017;55,00;HISCRE").
Saídas: calculo.json (para o modelo) e calculo.md (planilha pronta para colar, resumo e alertas).
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cartao as CT  # noqa: E402
import escrutinio as esc  # noqa: E402
from valores import brl, brl_ext  # noqa: E402

DANO_MORAL = 20000.00
CONFERIR = "[CONFERIR]"
AQUI = HERE.parent
# Lei 14.690, art. 28, § 1º: 90 dias contados da publicação (DOU de 03/10/2023). Pela contagem simples, o prazo terminou
# em 01/01/2024. VERIFICAR ANTES DE PROTOCOLAR.
PRIMEIRA_COMPETENCIA_COM_TETO = "01/2024"


def pct(x):
    return f"{x:,.1f}%".replace(",", "X").replace(".", ",").replace("X", ".")


def num(v):
    return brl(v).replace("R$ ", "")


def data4(d):  # dd/mm/aa -> dd/mm/aaaa
    return f"{d[:6]}20{d[6:]}" if d and len(d) == 8 else d


_MSG_REU = [""]


def carregar_reu(banco):
    cod = (banco or "").split(" - ")[0].strip()
    reus = json.loads((AQUI / "references/dados/reus.json").read_text(encoding="utf-8"))["reus"]
    reu = reus.get(cod)
    if not reu:  # fora do cadastro: qualifica pelo BCB (ISPB) + Receita (CNPJ), sem pedir conferência ao advogado
        try:
            sys.path.insert(0, str(AQUI / "scripts"))
            import buscar_reu
            reu, msg = buscar_reu.resolver(cod)
            _MSG_REU[0] = msg
        except Exception as e:  # sem rede ou módulo ausente
            reu, _MSG_REU[0] = None, f"consulta indisponível ({e})"
    return reu, cod


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ficha", required=True)
    ap.add_argument("--processo", type=int, required=True)
    ap.add_argument("--extrato", required=True)
    ap.add_argument("--data", default=dt.date.today().isoformat(), help="data da peça, AAAA-MM-DD")
    ap.add_argument("--saida", required=True)
    ap.add_argument("--historico-extra")
    ap.add_argument("--rito", choices=["jec", "comum"], help="rito escolhido pelo advogado (FSC9)")
    ap.add_argument("--extrato-bancario", choices=["sim", "nao"], dest="extrato_bancario",
                    help="o cliente trouxe o extrato bancário do mês da averbação? (VF6, Súmula 42/TJBA)")
    ap.add_argument("--dossie-pre-acao", action="store_true", dest="dossie_pre_acao",
                    help="o banco entregou contrato ou trilha antes da ação (VF2, VF4, VF5)")
    a = ap.parse_args()

    ficha = json.loads(Path(a.ficha).read_text(encoding="utf-8"))
    proc = next(p for p in ficha["processos"] if p["processo"] == a.processo)
    if proc["tese"] != "RMC_REFINANCIAMENTO":
        sys.exit(f"Processo {a.processo} é da tese {proc['tese']}; esta skill atende só RMC_REFINANCIAMENTO.")
    if len(proc["contratos"]) != 1:
        sys.exit("TRAVA: um cartão por processo. Separe os cartões em processos distintos.")
    hoje = dt.date.fromisoformat(a.data)
    alertas, conferir, bloqueios = [], [], []

    reu, cod = carregar_reu(proc["reu"])
    if not reu:
        conferir.append(f"Réu {proc['reu']} (código {cod}) não está em references/dados/reus.json e a consulta pública (BCB + Receita) não resolveu ({_MSG_REU[0]}): preencher CNPJ e "
                        "endereço com fonte e acrescentar à tabela.")

    # ---- cartão e histórico
    txt = CT.texto(a.extrato)
    numero = proc["contratos"][0]["contrato"]
    cart = CT.contrato_cartao(txt, numero)
    if not cart:
        sys.exit(f"TRAVA: cartão {numero} não encontrado na seção CARTÃO DE CRÉDITO do extrato.")
    hist = CT.historico(txt, numero, cart["banco_cod"], proc.get("nb"))
    cont = CT.continuidade(hist)
    cad = CT.cadeia(txt, cart["banco_cod"], cart.get("tipo") or "RMC")
    fontes_extra = set()
    if a.historico_extra:
        conhecidas = {h["competencia"] for h in hist}
        for ln in Path(a.historico_extra).read_text(encoding="utf-8").splitlines():
            if not ln.strip() or ln.startswith("#"):
                continue
            partes = [p.strip() for p in ln.split(";")]
            comp, val = partes[0], CT.v(partes[1])
            if comp not in conhecidas:
                fonte = partes[2] if len(partes) > 2 else "histórico complementar"
                hist.append({"competencia": comp, "desconto": val, "saldo": None, "utilizado": None, "iof": None,
                             "juros_m": None, "fonte": fonte})
                fontes_extra.add(fonte)
        hist.sort(key=lambda h: CT.comp_n(h["competencia"]))
    if not hist:
        sys.exit("TRAVA: nenhuma competência do cartão na seção DESCONTOS DE CARTÃO do extrato.")
    refs = CT.detectar_refinanciamento(hist)
    if not refs:
        sys.exit("TRAVA: nenhum refinanciamento detectado (salto do 'utilizado no mês' para quase todo o saldo, com "
                 "IOF). A tese não se aplica com estes dados.")
    if len(refs) > 1:
        alertas.append(f"Mais de um refinanciamento detectado ({', '.join(r['competencia'] for r in refs)}): a peça "
                       "trata o primeiro; avaliar se cabe mencionar os demais.")
    R = refs[0]
    incl = cart["inclusao"]
    incl4 = data4(incl)
    inicio_cartao = CT.comp_n(f"{incl[3:5]}/20{incl[6:]}")
    primeira = CT.comp_n(hist[0]["competencia"])
    if primeira - inicio_cartao > 2:
        sys.exit(f"TRAVA: histórico incompleto. O cartão foi incluído em {incl4}, mas o histórico disponível começa em "
                 f"{hist[0]['competencia']} (faltam {primeira - inicio_cartao - 1} competências, de "
                 f"{CT.comp_s(inicio_cartao + 1)} a {CT.comp_s(primeira - 1)}). Sem esses descontos não se prova o "
                 "marco de 200% antes do refinanciamento. Forneça o histórico (HISCRE/faturas) em --historico-extra.")
    capital = cart["limite"]
    calc = CT.calcular(hist, capital, R["competencia"], 10 ** 6)
    marco = calc["marco_200"]
    rn = CT.comp_n(R["competencia"])
    if not marco or CT.comp_n(marco) >= rn:
        sys.exit(f"TRAVA: com o histórico disponível, os pagamentos não atingem 200% do capital ({brl(capital)}) antes "
                 f"do refinanciamento de {R['competencia']} (pago até então: {brl(calc['total_ate_refin'])}, "
                 f"{pct(calc['total_ate_refin'] / capital * 100)}). O núcleo da tese não se sustenta: avaliar com o "
                 "advogado responsável.")
    marco_linha = next(p for p in calc["planilha"] if p["competencia"] == marco)
    meses_teto = rn - CT.comp_n(marco)
    pos = calc["total_pos_refin"]
    dobro = round(2 * pos, 2)
    pos2 = round(sum(p["desconto"] or 0 for p in calc["planilha"] if CT.comp_n(p["competencia"]) >= rn), 2)  # 2ª via
    if abs(pos - pos2) > 0.005:
        alertas.append(f"As duas vias do total descontado desde o refinanciamento divergem ({pos} x {pos2}).")
    saldo_atual = next((h["saldo"] for h in reversed(calc["planilha"]) if h.get("saldo")), None) or 0.0
    total_pago = calc["total_pago"]
    custo = round(total_pago + saldo_atual, 2)
    oneros = custo / capital * 100
    saldo_ref = R["utilizado"]
    valor_causa = round(saldo_ref + dobro + DANO_MORAL, 2)
    ativo = (cart["situacao"] or "").lower().startswith("ativ")

    # ---- alertas jurídicos (references/01-tese-e-roteiro.md). Nada bloqueia: o escritório mantém a tese do teto (29/10/2026).
    if CT.comp_n(R["competencia"]) < CT.comp_n(PRIMEIRA_COMPETENCIA_COM_TETO):
        alertas.append(
            f"B2: refinanciamento em {R['competencia']}, anterior ao fim do prazo de 90 dias contado da publicação da "
            "Lei 14.690 (DOU de 03/10/2023). O banco invocará o art. 2º-D da Res. CMN 4.549. A peça mantém a tese do teto "
            "(decisão do escritório de 29/10/2026) com o argumento do trato sucessivo e [VERIFICAR ANTES DE PROTOCOLAR].")
    elif R["competencia"] == PRIMEIRA_COMPETENCIA_COM_TETO:
        alertas.append("Refinanciamento em 01/2024: conferir o DIA da operação contra o fim do prazo de 90 dias "
                       "[VERIFICAR a contagem].")
    if CT.comp_n(marco) < CT.comp_n(PRIMEIRA_COMPETENCIA_COM_TETO):
        alertas.append(f"O marco de 200% ({marco}) é anterior à vigência do teto: o banco dirá que pagamentos feitos "
                       "antes dele não entram na conta. O modelo conta todos os pagamentos; decisão do advogado.")
    alertas.append("Confirmar nas faturas e com o cliente que, no cartão, só o mínimo é descontado em folha e o restante é pago por boleto: "
                   "é a premissa pela qual o art. 4º da Res. CMN 4.549 não afasta a resolução (decisão D1 do escritório, 29/10/2026).")
    alertas.append(f"Capital = limite do cartão ({brl(capital)}), premissa: o extrato não informa o valor sacado.")
    aus = calc["ausentes"]
    if aus:
        alertas.append(f"Competências ausentes no histórico (não interpoladas): {', '.join(aus)}. O total é piso.")
    if fontes_extra:
        alertas.append(f"Histórico complementado com: {', '.join(sorted(fontes_extra))}. Juntar o documento à inicial.")
    for c_ in cont:
        if c_["variacao"] > 0.05:
            alertas.append(f"Saldo devedor NÃO é contínuo na mudança de registro {c_['de']} -> {c_['para']} "
                           f"({brl(c_['saldo_de'])} -> {brl(c_['saldo_para'])}): conferir se as linhas antigas "
                           "(código do benefício) são mesmo deste cartão.")
    anteriores = [c_ for c_ in cad if c_["numero"] != numero]
    if anteriores:
        mesmo_dia = [c_ for c_ in anteriores if c_.get("exclusao") and any(d["inclusao"] == c_["exclusao"] for d in cad)]
        alertas.append("Cadeia de cartões do mesmo banco no extrato: "
                       + "; ".join(f"{c_['numero']} ({c_['inclusao']}->{c_.get('exclusao') or 'ativo'})" for c_ in cad)
                       + (f". Em {len(mesmo_dia)} troca(s) o cartão anterior foi excluído no MESMO DIA da averbação do "
                          "seguinte: pode ser relevante para a estratégia, não vai para a peça." if mesmo_dia else "."))
    saltos = [h for h in hist if h is not R and h.get("utilizado") and h.get("saldo") and h.get("desconto")
              and h["utilizado"] >= 0.9 * h["saldo"] and h["utilizado"] >= 5 * h["desconto"]
              and CT.comp_n(h["competencia"]) < rn]
    for h in saltos:
        alertas.append(f"Outro salto do 'utilizado no mês' ~ saldo em {h['competencia']} ({brl(h['utilizado'])}), sem IOF "
                       "registrado: não tratado como refinanciamento na peça; avaliar.")
    viz = [j for j in R["juros_vizinhos"] if j]
    juros_cai = bool(viz) and R.get("juros_m") is not None and all(R["juros_m"] < 0.8 * j for j in viz)
    if viz and not juros_cai:
        alertas.append(f"Taxa de juros no refinanciamento ({R.get('juros_m')}%) não é menor que a de todos os meses "
                       f"vizinhos ({viz}): o argumento da queda da taxa foi omitido.")
    if R.get("utilizado") and abs(R["utilizado"] - R["saldo"]) >= 0.01:
        alertas.append("O 'utilizado no mês' não é idêntico ao saldo devedor do refinanciamento: o modelo diz "
                       "'praticamente idêntico'.")

    id_ref = f"{numero}{cart['banco_cod']}{R['competencia'].replace('/', '')}"
    res_esc = esc.checagem([], [], "rmc", hoje=hoje, rito=a.rito, extrato_bancario=a.extrato_bancario,
                           dossie_pre_acao=a.dossie_pre_acao)
    alertas.extend(res_esc["roteamento"])
    out = {
        "data_peca": hoje.isoformat(), "processo": a.processo, "nb": proc.get("nb"), "reu": proc["reu"],
        "reu_cadastrado": bool(reu), "caixa": cod == "104", "competencia": proc.get("competencia"),
        "cartao": {"numero": numero, "tipo": cart.get("tipo") or "RMC", "banco": cart["banco"], "limite": capital,
                   "situacao": cart["situacao"], "inclusao": incl4},
        "ativo": ativo, "tutela": ativo,
        "refinanciamento": {"competencia": R["competencia"], "id_linha": id_ref, "utilizado": saldo_ref,
                            "saldo": R["saldo"], "iof": R["iof"], "juros_m": R["juros_m"],
                            "identico_ao_saldo": abs(R["utilizado"] - R["saldo"]) < 0.01,
                            "utilizado_anteriores": [u for u in R["utilizado_vizinhos"] if u is not None]},
        "juros_cai": juros_cai, "juros_vizinhos": viz,
        "capital": capital, "dobro_capital": round(2 * capital, 2),
        "marco": {"competencia": marco, "acumulado": marco_linha["acumulado"], "pct": round(marco_linha["pct"], 1)},
        "meses_teto": meses_teto,
        "total_ate_refin": calc["total_ate_refin"], "pct_ate_refin": round(calc["total_ate_refin"] / capital * 100, 1),
        "total_pos_refin": pos, "dobro": dobro, "dobro_extenso": brl_ext(dobro),
        # nomes que o verificador do pacote exige em todo calculo.json: aqui, o descontado desde o refinanciamento
        "total_descontado": pos, "total_dobro": dobro,
        "total_pago": total_pago, "pct_pago": round(total_pago / capital * 100, 1), "saldo_atual": saldo_atual,
        "custo_total": custo, "onerosidade_pct": round(oneros, 1),
        "dano_moral": DANO_MORAL, "dano_moral_extenso": brl_ext(DANO_MORAL),
        "valor_causa": valor_causa, "valor_causa_extenso": brl_ext(valor_causa),
        "primeira": calc["primeira"], "ultima": calc["ultima"], "competencias_ausentes": aus,
        "fontes_extra": sorted(fontes_extra), "n_competencias": len(calc["planilha"]),
        "bloqueios_juridicos": bloqueios, "pode_gerar": not bloqueios,
        "alertas": alertas, "conferir": conferir, "checagem_fsc": res_esc["fsc"], "checagem_vf": res_esc["vf"], "marca": "CÁLCULO A CONFERIR",
    }
    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)
    (saida / "calculo.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")

    # ---- calculo.md: planilha pronta para colar
    por_comp = {p["competencia"]: p for p in calc["planilha"]}
    linhas = ["| Mês/ano | Desconto (R$) | Acumulado (R$) | % do capital |", "|---|---|---|---|"]
    for n in range(CT.comp_n(calc["primeira"]), CT.comp_n(calc["ultima"]) + 1):
        c = CT.comp_s(n)
        p = por_comp.get(c)
        marca = (" **REFINANCIAMENTO**" if c == R["competencia"] else "") + (" **MARCO 200%**" if c == marco else "")
        if p:
            linhas.append(f"| {c}{marca} | {num(p['desconto'] or 0)} | {num(p['acumulado'])} | {pct(p['pct'])} |")
        else:
            linhas.append(f"| {c} (ausente no extrato) | — | — | — |")
    md = [f"# Cálculo do processo {a.processo} (NB {proc.get('nb')}) — **CÁLCULO A CONFERIR**", "",
          f"Data da peça: {hoje.strftime('%d/%m/%Y')} · cartão {out['cartao']['tipo']} nº {numero} · "
          f"situação {cart['situacao']} · capital adotado (limite) {brl(capital)}", ""]
    if bloqueios:
        md += ["## BLOQUEADO PARA USO FINAL", ""] + [f"- {b}" for b in bloqueios] + [""]
    md += ["## Planilha", ""] + linhas + ["",
           "## Resumo financeiro", "",
           f"- Refinanciamento: {R['competencia']} · utilizado {brl(saldo_ref)} · saldo {brl(R['saldo'])} · IOF {brl(R['iof'])}",
           f"- Marco de 200%: {marco} ({brl(marco_linha['acumulado'])}, {pct(marco_linha['pct'])}) · {meses_teto} meses antes do refinanciamento",
           f"- Pago até o refinanciamento: {brl(calc['total_ate_refin'])} ({pct(calc['total_ate_refin'] / capital * 100)})",
           f"- Descontado desde o refinanciamento: {brl(pos)} · em dobro **{brl_ext(dobro)}**",
           f"- Total pago: {brl(total_pago)} ({pct(total_pago / capital * 100)}) · saldo atual {brl(saldo_atual)} · custo total {brl(custo)} · onerosidade {pct(oneros)}",
           f"- Dano extrapatrimonial (fixo): {brl(DANO_MORAL)}",
           f"- **Valor da causa: {brl_ext(valor_causa)}** (saldo refinanciado + dobro + dano extrapatrimonial)",
           f"- Tutela de urgência: {'SIM (cartão ativo)' if ativo else 'não'}", ""]
    if conferir:
        md += ["## Conferir antes de protocolar", ""] + [f"- {x}" for x in conferir] + [""]
    if alertas:
        md += ["## Alertas", ""] + [f"- {x}" for x in alertas] + [""]
    md += ["", esc.para_markdown(res_esc)]
    (saida / "calculo.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    emissao = re.search(r"(\d{2}/\d{2}/\d{4}) \d{2}:\d{2}:\d{2}", txt[:4000])
    fonte = f"extrato do INSS, cartão {numero}"
    ev = esc.eventos_dos_contratos([], hoje, emissao.group(1) if emissao else None)
    ev += [esc.evento(incl4, f"Averbação do cartão {numero}", fonte, f"capital adotado: limite de {brl(capital)}"),
           esc.evento(calc["primeira"], "Primeira competência do histórico do cartão", fonte, "início da planilha do marco de 200%"),
           esc.evento(PRIMEIRA_COMPETENCIA_COM_TETO, "Fim do prazo de 90 dias da Lei 14.690/2023 (publicada em 03/10/2023)",
                      "lei-14690.md", "a partir daqui vale o teto de 200% do art. 28, § 1º"),
           esc.evento(marco, "Marco de 200% do capital atingido", "planilha do cálculo", "pagamentos já somam o dobro do capital"),
           esc.evento(R["competencia"], "Refinanciamento do saldo do cartão", fonte, "início da repetição em dobro (descontos desde aqui)"),
           esc.evento(calc["ultima"], "Última competência do histórico do cartão", fonte, "fim da contagem do cálculo")]
    crono = esc.cronologia(ev)
    esc.gravar(saida, res_esc, "rmc", a.processo, hoje, out, a.extrato_bancario, a.dossie_pre_acao, crono)
    print(f"ok: {saida / 'calculo.json'} e calculo.md · valor da causa {brl(valor_causa)}"
          + (" · BLOQUEADO PARA USO FINAL" if bloqueios else ""))


if __name__ == "__main__":
    main()
