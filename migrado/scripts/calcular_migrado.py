#!/usr/bin/env python3
"""calcular_migrado.py - cálculo da inicial de consignado MIGRADO (averbação com origem "Migrado do contrato ... CBC: ...").

Para cada contrato da ficha, localiza no extrato do INSS o registro do réu, confere a origem da averbação (migração), extrai o contrato e
o código do banco de origem, procura o mesmo número no banco anterior, conta os descontos (início a fim, inclusive; contrato ativo só até
o mês anterior à data da peça), calcula o dobro, o proveito econômico dos contratos ativos (parcelas vincendas) e o valor da causa.
Todo número sai como CÁLCULO A CONFERIR.

Troca de titularidade: se o mesmo número aparece em outro banco, o script NÃO soma os descontos registrados lá, a menos que o advogado
decida e passe --incluir-outros-bancos. Sem a flag, o total é só o do registro do réu e sai um alerta com o que ficou de fora.

Valor da causa: o campo valor_causa é dobro + R$ 20.000,00. O campo valor_causa_com_proveito soma as parcelas vincendas dos contratos
ativos (proveito econômico declaratório, usado só em Justiça Comum, por decisão do advogado).

Alerta: contrato sem origem de migração; contrato não localizado; mesmo número em outro banco; descontos com mais de 5 e 10 anos.

Uso:
  python3 calcular_migrado.py --ficha ficha.json --processo 1 --extrato extrato.pdf --data 2026-10-28 --saida pasta/
                              [--incluir-outros-bancos]
Saídas: calculo.json (para o modelo) e calculo.md (tabelas e alertas).
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import extrato as ext  # noqa: E402
import escrutinio as esc  # noqa: E402
from valores import brl, brl_ext  # noqa: E402

DANO_MORAL = 20000.00
CONFERIR = "[CONFERIR]"
AQUI = HERE.parent
VIGENCIA_IN138 = dt.date(2022, 12, 13)
RE_MIGRADO = re.compile(r"Migrado do contrato\s+(\S+?)(?:\s+CBC:?\s*(\d{3}))?\s*$", re.I)


def comp(s):
    m, a = s.split("/")
    return int(a) * 12 + int(m) - 1


def comp_str(n):
    return f"{n % 12 + 1:02d}/{n // 12}"


def data(d):  # dd/mm/aa -> date
    if not d:
        return None
    dia, mes, ano = d.split("/")
    ano = int(ano)
    return dt.date(2000 + ano if ano < 100 else ano, int(mes), int(dia))


def data4(d):  # dd/mm/aa -> dd/mm/aaaa
    return f"{d[:6]}20{d[6:]}" if d and len(d) == 8 else d


def regime_da_data(d_incl):
    """Norma aplicável pela data da averbação."""
    return "IN138" if (d_incl and d_incl >= VIGENCIA_IN138) else "IN28"


def origem_da_migracao(origem):
    """('7001001', '934') a partir de 'Migrado do contrato 7001001 CBC: 934'; (None, None) se não for migração."""
    m = RE_MIGRADO.search((origem or "").strip())
    return (m.group(1), m.group(2)) if m else (None, None)


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


def descontos(r, mes_ref):
    """(qtde, total, total pela 2ª via, até-competência, início, ativo, vincendas) de um registro do extrato."""
    ini, fim = comp(r["inicio"]), comp(r["fim"])
    ativo = r["secao"] == "ATIVO"
    ate = min(fim, mes_ref) if ativo else fim
    qtde = max(0, ate - ini + 1)
    total = round(qtde * r["parcela"], 2)
    total2 = round(sum(r["parcela"] for _ in range(ini, ate + 1)), 2) if qtde else 0.0  # segunda via
    vinc = max(0, fim - mes_ref) if ativo else 0
    return qtde, total, total2, ate, ini, ativo, vinc


def data_emissao(caminho):
    """Data de emissão do extrato do INSS (ciência dos descontos, padrão do escritório); None se não ler."""
    try:
        return ext.data_extrato(caminho)
    except Exception:
        return None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ficha", required=True)
    ap.add_argument("--processo", type=int, required=True)
    ap.add_argument("--extrato", required=True)
    ap.add_argument("--data", default=dt.date.today().isoformat(), help="data da peça, AAAA-MM-DD")
    ap.add_argument("--saida", required=True)
    ap.add_argument("--rito", choices=["jec", "comum"], help="rito escolhido pelo advogado (FSC9)")
    ap.add_argument("--extrato-bancario", choices=["sim", "nao"], dest="extrato_bancario",
                    help="o cliente trouxe o extrato bancário do mês da averbação? (VF6, Súmula 42/TJBA)")
    ap.add_argument("--dossie-pre-acao", action="store_true", dest="dossie_pre_acao",
                    help="o banco entregou contrato ou trilha antes da ação (VF2, VF4, VF5)")
    ap.add_argument("--incluir-outros-bancos", action="store_true",
                    help="soma os descontos do mesmo contrato registrados no banco anterior (troca de titularidade); decisão do advogado")
    a = ap.parse_args()

    ficha = json.loads(Path(a.ficha).read_text(encoding="utf-8"))
    proc = next(p for p in ficha["processos"] if p["processo"] == a.processo)
    if proc["tese"] != "MIGRADO":
        sys.exit(f"Processo {a.processo} é da tese {proc['tese']}; esta skill atende só MIGRADO.")
    hoje = dt.date.fromisoformat(a.data)
    mes_ref = hoje.year * 12 + hoje.month - 2  # última competência já descontada (mês anterior)
    alertas, conferir = [], []
    reu, cod = carregar_reu(proc["reu"])
    if not reu:
        conferir.append(f"Réu {proc['reu']} (código {cod}) não está em references/dados/reus.json e a consulta pública (BCB + Receita) não resolveu ({_MSG_REU[0]}): preencher CNPJ e endereço com fonte.")
    todos_ext = ext.contratos(a.extrato)
    lista = [r for r in todos_ext if r["inicio"]]
    do_banco = lambda x: x["banco"].replace(" ", "").startswith(f"{cod}-")  # noqa: E731

    linhas = []
    sel = []
    for c in proc["contratos"]:
        achados = ext.buscar(lista, c["contrato"])
        do_reu = [x for x in achados if do_banco(x)]
        outros = [x for x in achados if not do_banco(x)]
        if not do_reu:
            conferir.append(f"Contrato {c['contrato']} não localizado no extrato com o código do réu ({cod}): linha em branco.")
            continue
        r = next((x for x in do_reu if x["secao"] == "ATIVO"), do_reu[-1])
        sel.append(r)
        if len(do_reu) > 1:
            alertas.append(f"Contrato {r['contrato']} aparece {len(do_reu)}x no extrato para o réu; usada a ocorrência {'ativa' if r['secao'] == 'ATIVO' else 'mais recente'}.")
        contrato_origem, banco_origem = origem_da_migracao(r["origem_averbacao"])
        migrado = bool(contrato_origem)
        if not migrado:
            alertas.append(f"Contrato {r['contrato']}: a origem da averbação é '{r['origem_averbacao']}', e não migração. Rever a tese: pode ser não contratado comum (skill nao-contratado).")
        elif contrato_origem and re.sub(r"\W", "", contrato_origem).lstrip("0") != re.sub(r"\W", "", r["contrato"]).lstrip("0"):
            alertas.append(f"Contrato {r['contrato']}: a origem aponta outro número ({contrato_origem}); descrever os dois números e conferir no extrato.")
        qtde, total, total2, ate, ini, ativo, vinc = descontos(r, mes_ref)
        if abs(total - total2) > 0.005:
            alertas.append(f"Contrato {r['contrato']}: as duas vias do total divergem ({total} x {total2}).")

        info_outros = []
        for o in outros:
            oq, ot, _, _, _, _, _ = descontos(o, mes_ref)
            info_outros.append({"contrato": o["contrato"], "banco": o["banco"], "situacao": o["situacao"], "motivo_exclusao": o["motivo_exclusao"],
                                "origem_averbacao": o["origem_averbacao"], "inclusao": data4(o["inclusao"]), "exclusao": data4(o["exclusao"]),
                                "inicio": o["inicio"], "fim": o["fim"], "parcela": o["parcela"], "qtde": oq, "total": ot})
        qtde_reu, total_reu = qtde, total
        if outros and a.incluir_outros_bancos:
            qtde += sum(o["qtde"] for o in info_outros)
            total = round(total + sum(o["total"] for o in info_outros), 2)
        elif outros:
            alertas.append(f"TROCA DE TITULARIDADE: o contrato {r['contrato']} aparece também em {', '.join(o['banco'] for o in info_outros)}, com "
                           f"{sum(o['qtde'] for o in info_outros)} parcela(s) ({brl(sum(o['total'] for o in info_outros))}) que NÃO foram somadas. "
                           "Decisão do advogado sobre a legitimidade do réu e a extensão da restituição; para somar, rode com --incluir-outros-bancos.")
        elif migrado:
            alertas.append(f"Contrato {r['contrato']}: migrado do banco {banco_origem or CONFERIR}, mas o extrato não mostra o registro do banco anterior; conferir.")

        incl = [data(x["inclusao"]) for x in [r] + outros if x.get("inclusao")]
        d_incl = min(incl) if incl else None  # primeira averbação, em qualquer banco
        status = "ATIVO" if ativo else ("ENCERRADO" if (r["situacao"] or "").startswith("Encerr") else "EXCLUÍDO")
        vinc_valor = round(vinc * r["parcela"], 2)
        linhas.append({
            "contrato": r["contrato"], "origem_averbacao": r["origem_averbacao"], "migrado": migrado, "contrato_origem": contrato_origem,
            "banco_origem_cbc": banco_origem, "status": status, "ativo": ativo, "inclusao": data4(r["inclusao"]),
            "primeira_averbacao": d_incl.strftime("%d/%m/%Y") if d_incl else None, "regime_norma": regime_da_data(d_incl),
            "inicio": r["inicio"], "fim": r["fim"], "ate_comp": comp_str(ate) if qtde_reu else None, "parcela": r["parcela"], "prazo": r["qtde_contratada"],
            "liberado": r["liberado"], "qtde": qtde, "total": total, "dobro": round(2 * total, 2), "qtde_registro_do_reu": qtde_reu,
            "total_registro_do_reu": total_reu, "vincendas_qtde": vinc, "vincendas_valor": vinc_valor, "exclusao": data4(r["exclusao"]),
            "motivo_exclusao": r["motivo_exclusao"], "ini_n": ini, "bloco": c.get("bloco"),
            "troca_de_titularidade": bool(outros), "outros_bancos_somados": bool(outros) and a.incluir_outros_bancos, "outras_ocorrencias": info_outros,
        })
        if qtde_reu and ini < comp("04/2021"):
            alertas.append(f"Contrato {r['contrato']}: há descontos anteriores a 30/03/2021. Usar o bloco [[SE HÁ DESCONTO ANTES DE 30/03/2021]] "
                           "do tópico da dobra: o EAREsp 676.608/RS foi modulado para pagamentos posteriores; os anteriores, pelo art. 42 do CDC (decisão R7, 01/11/2026).")
        if not qtde:
            alertas.append(f"Contrato {r['contrato']}: nenhum desconto efetivo; rever o pedido de repetição.")
    if not linhas:
        sys.exit("TRAVA: nenhum contrato da ficha localizado no extrato; nada a calcular.")
    if len({l['regime_norma'] for l in linhas}) > 1:
        alertas.append("Contratos de regimes diferentes (IN 28 e IN 138) no mesmo processo: o modelo traz os dois blocos; revisar.")

    ativos = [l["contrato"] for l in linhas if l["ativo"]]
    tot_desc = round(sum(l["total"] for l in linhas), 2)
    tot_dobro = round(sum(l["dobro"] for l in linhas), 2)
    proveito = round(sum(l["vincendas_valor"] for l in linhas), 2)
    valor_causa = round(tot_dobro + DANO_MORAL, 2)
    com_desc = [l for l in linhas if l["qtde"]]
    limite5 = (hoje.year - 5) * 12 + hoje.month - 1
    prescricao = bool(com_desc) and min(l["ini_n"] for l in com_desc) < limite5
    if com_desc and min(l["ini_n"] for l in com_desc) < (hoje.year - 10) * 12 + hoje.month - 1:
        alertas.append("Há descontos com MAIS DE 10 ANOS: o tópico de prescrição não pode afirmar que todos estão no prazo decenal. Decisão do advogado.")
    for l in linhas:
        l.pop("ini_n")

    res_esc = esc.checagem(sel, todos_ext, "migrado", hoje=hoje, rito=a.rito, extrato_bancario=a.extrato_bancario,
                           dossie_pre_acao=a.dossie_pre_acao)
    alertas.extend(x for x in res_esc["roteamento"] if x not in alertas and "`nao-contratado`" not in x)
    out = {
        "data_peca": hoje.isoformat(), "processo": a.processo, "nb": proc.get("nb"), "reu": proc["reu"],
        "reu_cadastrado": bool(reu), "caixa": cod == "104", "competencia": proc.get("competencia"),
        "contratos": linhas, "ativos": ativos, "tutela": bool(ativos), "prescricao_5_anos": prescricao,
        "todos_migrados": all(l["migrado"] for l in linhas), "troca_de_titularidade": any(l["troca_de_titularidade"] for l in linhas),
        "outros_bancos_somados": a.incluir_outros_bancos, "total_descontado": tot_desc, "total_dobro": tot_dobro,
        "dano_moral": DANO_MORAL, "valor_causa": valor_causa, "valor_causa_extenso": brl_ext(valor_causa),
        "proveito_declaratorio": proveito, "valor_causa_com_proveito": round(valor_causa + proveito, 2),
        "valor_causa_com_proveito_extenso": brl_ext(round(valor_causa + proveito, 2)), "total_dobro_extenso": brl_ext(tot_dobro),
        "dano_moral_extenso": brl_ext(DANO_MORAL), "alertas": alertas, "conferir": conferir, "checagem_fsc": res_esc["fsc"], "checagem_vf": res_esc["vf"],
        "mesma_data": res_esc["mesma_data"], "marca": "CÁLCULO A CONFERIR",
    }
    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)
    (saida / "calculo.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")

    md = [f"# Cálculo do processo {a.processo} (NB {proc.get('nb')}): **CÁLCULO A CONFERIR**", "",
          f"Data da peça: {hoje.strftime('%d/%m/%Y')} · última competência de contrato ativo: {comp_str(mes_ref)}", "",
          "| Contrato | Origem da averbação | Banco de origem (CBC) | 1ª averbação | Norma | Início | Fim usado | Qtde | Parcela | Total | Dobro | Vincendas | Status |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for l in linhas:
        md.append(f"| {l['contrato']} | {l['origem_averbacao'] or CONFERIR} | {l['banco_origem_cbc'] or CONFERIR} | {l['primeira_averbacao']} | {l['regime_norma']} | "
                  f"{l['inicio']} | {l['ate_comp'] or ''} | {l['qtde']} | {brl(l['parcela'])} | {brl(l['total'])} | {brl(l['dobro'])} | "
                  f"{l['vincendas_qtde']} ({brl(l['vincendas_valor'])}) | {l['status']} |")
    md += ["", f"- Total descontado: **{brl(tot_desc)}**", f"- Restituição em dobro: **{brl_ext(tot_dobro)}**",
           f"- Dano extrapatrimonial (fixo): **{brl(DANO_MORAL)}**",
           f"- Valor da causa: **{brl_ext(valor_causa)}**" + (" (Vara Federal: valor real, sem renúncia a teto)" if cod == "104" else ""),
           f"- Proveito econômico declaratório (parcelas vincendas dos ativos, só Justiça Comum, decisão do advogado): {brl(proveito)} · valor da causa com proveito: {brl_ext(out['valor_causa_com_proveito'])}",
           f"- Tutela de urgência: {'SIM, só sobre ' + ', '.join(ativos) if ativos else 'não (sem contrato ativo)'}",
           f"- Tópico de prescrição (algum desconto com mais de 5 anos): {'SIM' if prescricao else 'não'}",
           f"- Troca de titularidade (mesmo número em outro banco): {'SIM; descontos do banco anterior ' + ('SOMADOS' if a.incluir_outros_bancos else 'NÃO somados') if out['troca_de_titularidade'] else 'não'}", ""]
    if conferir:
        md += ["## Conferir antes de protocolar", ""] + [f"- {x}" for x in conferir] + [""]
    if alertas:
        md += ["## Alertas", ""] + [f"- {x}" for x in alertas] + [""]
    md += ["", esc.para_markdown(res_esc)]
    (saida / "calculo.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    ev = esc.eventos_dos_contratos([l for l in linhas if l.get("inicio")], hoje, data_emissao(a.extrato))
    for l in linhas:
        if l.get("migrado"):
            ev.append(esc.evento(l.get("primeira_averbacao"), f"Primeira averbação do contrato {l['contrato']} (banco de origem {l.get('banco_origem_cbc') or 'não identificado'})",
                                 "extrato do INSS, registro do banco anterior", f"contratação de origem; norma do INSS da migração: {l.get('regime_norma')}"))
    if any(l.get("inclusao") for l in linhas):
        ev.append(esc.evento(esc.VIGENCIA_IN138, "Início da vigência da IN PRES/INSS 138/2022", "protocolo, \"Texto vigente e texto revogado\"",
                             "averbação até 12/12/2022 segue a IN 28/2008"))
    crono = esc.cronologia(ev)
    esc.gravar(saida, res_esc, "migrado", a.processo, hoje, out, a.extrato_bancario, a.dossie_pre_acao, crono)
    print(f"ok: {saida / 'calculo.json'} e calculo.md · valor da causa {brl(valor_causa)}")


if __name__ == "__main__":
    main()
