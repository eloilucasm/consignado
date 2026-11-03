#!/usr/bin/env python3
"""calcular_1000.py - cálculo da inicial da Tese 1000 Contra (contrato derivado com sufixo sobre contrato-raiz excluído).

Para cada contrato da ficha (o derivado), localiza no extrato do INSS o derivado e o contrato-raiz (número sem o sufixo),
mede o intervalo entre a exclusão da raiz e a PRIMEIRA averbação do derivado (em qualquer banco), conta os descontos (início a
fim, inclusive; contrato ativo só até o mês anterior à data da peça), calcula o dobro e o valor da causa (dobro + R$ 20.000,00) e
escolhe a norma pela data da primeira averbação do derivado: IN INSS/PRES 28/2008 até 12/12/2022; IN 138/2022 desde 13/12/2022.
Todo número sai como CÁLCULO A CONFERIR.

Troca de titularidade: se o mesmo número do derivado aparece em outro banco (migração da carteira), o script NÃO soma os descontos
registrados nesse outro banco, a menos que o advogado decida e passe --incluir-outros-bancos. Sem a flag, o total é só o do
registro do réu e sai um alerta com o que ficou de fora.

Para sem gravar: nenhum derivado localizado no extrato.
Alerta: raiz não localizada; derivado averbado ANTES da exclusão da raiz; mais de uma raiz; mesmo número em outros bancos.

Uso:
  python3 calcular_1000.py --ficha ficha.json --processo 1 --extrato extrato.pdf --data 2026-10-28 --saida pasta/
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


def raiz_de(contrato):
    """Número-raiz e sufixo de um contrato derivado: '51-195502/15310_0001' -> ('51-195502/15310', '_0001')."""
    m = re.match(r"^(.+?)(_\d{1,4})$", contrato or "")
    return (m.group(1), m.group(2)) if m else (None, None)


def regime_da_data(d_incl):
    """Norma aplicável pela data da (primeira) averbação do derivado."""
    return "IN138" if (d_incl and d_incl >= VIGENCIA_IN138) else "IN28"


def categoria_intervalo(intervalo):
    if intervalo is None:
        return None
    if intervalo < 0:
        return "ANTES_DA_EXCLUSAO"
    if intervalo == 0:
        return "MESMO_DIA"
    return "ATE_30_DIAS" if intervalo <= 30 else "MAIS_DE_30_DIAS"


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
    """(qtde, total, até-competência, ativo) de um registro do extrato."""
    ini, fim = comp(r["inicio"]), comp(r["fim"])
    ativo = r["secao"] == "ATIVO"
    ate = min(fim, mes_ref) if ativo else fim
    qtde = max(0, ate - ini + 1)
    total = round(qtde * r["parcela"], 2)
    total2 = round(sum(r["parcela"] for _ in range(ini, ate + 1)), 2) if qtde else 0.0  # segunda via
    return qtde, total, total2, ate, ini, ativo


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
                    help="soma os descontos do mesmo derivado registrados em outro banco (troca de titularidade); decisão do advogado")
    a = ap.parse_args()

    ficha = json.loads(Path(a.ficha).read_text(encoding="utf-8"))
    proc = next(p for p in ficha["processos"] if p["processo"] == a.processo)
    if proc["tese"] != "TESE_1000":
        sys.exit(f"Processo {a.processo} é da tese {proc['tese']}; esta skill atende só TESE_1000.")
    hoje = dt.date.fromisoformat(a.data)
    mes_ref = hoje.year * 12 + hoje.month - 2  # última competência já descontada (mês anterior)
    alertas, conferir = [], []
    reu, cod = carregar_reu(proc["reu"])
    if not reu:
        conferir.append(f"Réu {proc['reu']} (código {cod}) não está em references/dados/reus.json e a consulta pública (BCB + Receita) não resolveu ({_MSG_REU[0]}): preencher CNPJ e endereço com fonte.")
    todos_ext = ext.contratos(a.extrato)
    lista = [r for r in todos_ext if r["inicio"]]
    do_banco = lambda x: x["banco"].replace(" ", "").startswith(f"{cod}-")  # noqa: E731

    derivs = []
    sel = []
    for c in proc["contratos"]:
        achados = ext.buscar(lista, c["contrato"])
        do_reu = [x for x in achados if do_banco(x)]
        outros = [x for x in achados if not do_banco(x)]
        if not do_reu:
            conferir.append(f"Derivado {c['contrato']} não localizado no extrato com o código do réu ({cod}).")
            continue
        r = next((x for x in do_reu if x["secao"] == "ATIVO"), do_reu[-1])
        sel.append(r)
        raiz_num, sufixo = raiz_de(r["contrato"])
        if not raiz_num:
            alertas.append(f"Contrato {r['contrato']} não tem sufixo numérico (_NNNN): pode não ser derivado. Avaliar se a tese é a do não contratado.")
        todas_raizes = ext.buscar(lista, raiz_num or "") if raiz_num else []
        raizes = [x for x in todas_raizes if do_banco(x)] or todas_raizes  # a raiz pode estar no banco anterior
        raiz = raizes[-1] if raizes else None
        if raiz_num and not raiz:
            conferir.append(f"Contrato-raiz {raiz_num} do derivado {r['contrato']} não localizado no extrato.")
        qtde, total, total2, ate, ini, ativo = descontos(r, mes_ref)
        if abs(total - total2) > 0.005:
            alertas.append(f"Derivado {r['contrato']}: as duas vias do total divergem ({total} x {total2}).")

        # outros bancos: o mesmo número em outra instituição (troca de titularidade)
        info_outros = []
        for o in outros:
            oq, ot, ot2, oate, oini, oativo = descontos(o, mes_ref)
            info_outros.append({"contrato": o["contrato"], "banco": o["banco"], "situacao": o["situacao"], "motivo_exclusao": o["motivo_exclusao"],
                                "origem_averbacao": o["origem_averbacao"], "inclusao": data4(o["inclusao"]), "exclusao": data4(o["exclusao"]),
                                "inicio": o["inicio"], "fim": o["fim"], "parcela": o["parcela"], "qtde": oq, "total": ot})
        migrado = bool(outros) or (r["origem_averbacao"] or "").lower().startswith("migrado")
        qtde_reu, total_reu = qtde, total
        if outros and a.incluir_outros_bancos:
            qtde += sum(o["qtde"] for o in info_outros)
            total = round(total + sum(o["total"] for o in info_outros), 2)
        elif outros:
            fora = sum(o["total"] for o in info_outros)
            alertas.append(f"FORA DO ESCOPO (TROCA DE TITULARIDADE): o derivado {r['contrato']} aparece também em {', '.join(o['banco'] for o in info_outros)}, com "
                           f"{sum(o['qtde'] for o in info_outros)} parcela(s) ({brl(fora)}) que NÃO foram somadas. Segundo o escritório (29/10/2026), na Tese 1000 o "
                           "contrato não é reaverbado por outro banco; confira se o caso é de outra tese (migrado) antes de seguir. A peça não trata da troca de titularidade.")
        elif migrado:
            alertas.append(f"Derivado {r['contrato']}: a origem da averbação indica migração ('{r['origem_averbacao']}'), mas não há registro do mesmo número em outro banco no extrato; conferir.")

        # intervalo e norma pela PRIMEIRA averbação do derivado (em qualquer banco)
        incl = [data(x["inclusao"]) for x in [r] + outros if x.get("inclusao")]
        d_incl = min(incl) if incl else None
        d_excl = data(raiz["exclusao"]) if (raiz and raiz.get("exclusao")) else None
        intervalo = (d_incl - d_excl).days if (d_incl and d_excl) else None
        cat = categoria_intervalo(intervalo)
        regime = regime_da_data(d_incl)
        status = "ATIVO" if ativo else ("ENCERRADO" if (r["situacao"] or "").startswith("Encerr") else "EXCLUÍDO")
        derivs.append({
            "contrato": r["contrato"], "raiz": raiz_num, "sufixo": sufixo, "status": status, "ativo": ativo,
            "primeira_averbacao": d_incl.strftime("%d/%m/%Y") if d_incl else None, "inclusao": data4(r["inclusao"]),
            "origem_averbacao": r["origem_averbacao"], "inicio": r["inicio"], "fim": r["fim"],
            "ate_comp": comp_str(ate) if qtde_reu else None, "parcela": r["parcela"], "prazo": r["qtde_contratada"], "liberado": r["liberado"],
            "qtde": qtde, "total": total, "dobro": round(2 * total, 2), "qtde_registro_do_reu": qtde_reu, "total_registro_do_reu": total_reu,
            "exclusao": data4(r["exclusao"]), "motivo_exclusao": r["motivo_exclusao"], "ini_n": ini, "regime_norma": regime,
            "troca_de_titularidade": migrado, "outros_bancos_somados": bool(outros) and a.incluir_outros_bancos,
            "raiz_dados": ({"banco": raiz["banco"], "averbacao": data4(raiz["inclusao"]), "exclusao": data4(raiz["exclusao"]),
                            "motivo_exclusao": raiz["motivo_exclusao"], "origem_averbacao": raiz["origem_averbacao"], "situacao": raiz["situacao"]} if raiz else None),
            "intervalo_dias": intervalo, "categoria_intervalo": cat, "outras_ocorrencias": info_outros,
        })
        if cat == "ANTES_DA_EXCLUSAO":
            alertas.append(f"Derivado {r['contrato']}: averbado ANTES da exclusão da raiz ({d_incl.strftime('%d/%m/%Y')} x {data4(raiz['exclusao'])}). "
                           "A narrativa 'reinclusão depois da exclusão' não vale: rever a tese.")
        if not qtde:
            alertas.append(f"Derivado {r['contrato']}: nenhum desconto efetivo; rever o pedido de repetição.")
        if qtde_reu and ini < comp("04/2021"):
            alertas.append(f"Derivado {r['contrato']}: há descontos anteriores a 30/03/2021. Usar o bloco [[SE HÁ DESCONTO ANTES DE 30/03/2021]] "
                           "do tópico da dobra: o EAREsp 676.608/RS foi modulado para pagamentos posteriores; os anteriores, pelo art. 42 do CDC (decisão R7, 01/11/2026).")
        if raiz and not do_banco(raiz):
            alertas.append(f"Derivado {r['contrato']}: a raiz {raiz_num} está em outro banco ({raiz['banco']}); descrever a sequência só pelo extrato.")
    if not derivs:
        sys.exit("TRAVA: nenhum contrato derivado localizado no extrato; nada a calcular.")
    if len({d['raiz'] for d in derivs}) > 1:
        alertas.append("Mais de um contrato-raiz no processo: o modelo trata uma raiz; separar em processos ou adaptar a tabela.")
    if len({d['regime_norma'] for d in derivs}) > 1:
        alertas.append("Derivados de regimes diferentes (IN 28 e IN 138) no mesmo processo: o modelo traz os dois blocos; revisar.")

    ativos = [d["contrato"] for d in derivs if d["ativo"]]
    tot_desc = round(sum(d["total"] for d in derivs), 2)
    tot_dobro = round(sum(d["dobro"] for d in derivs), 2)
    valor_causa = round(tot_dobro + DANO_MORAL, 2)
    com_desc = [d for d in derivs if d["qtde"]]
    limite5 = (hoje.year - 5) * 12 + hoje.month - 1
    prescricao = bool(com_desc) and min(d["ini_n"] for d in com_desc) < limite5
    if com_desc and min(d["ini_n"] for d in com_desc) < (hoje.year - 10) * 12 + hoje.month - 1:
        alertas.append("Há descontos com MAIS DE 10 ANOS: o tópico de prescrição não pode afirmar que todos estão no prazo decenal. Decisão do advogado.")
    for d in derivs:
        d.pop("ini_n")

    res_esc = esc.checagem(sel, todos_ext, "tese-1000", hoje=hoje, rito=a.rito, extrato_bancario=a.extrato_bancario,
                           dossie_pre_acao=a.dossie_pre_acao)
    alertas.extend(x for x in res_esc["roteamento"] if x not in alertas)
    out = {
        "data_peca": hoje.isoformat(), "processo": a.processo, "nb": proc.get("nb"), "reu": proc["reu"],
        "reu_cadastrado": bool(reu), "caixa": cod == "104", "competencia": proc.get("competencia"),
        "derivados": derivs, "ativos": ativos, "tutela": bool(ativos), "prescricao_5_anos": prescricao,
        "troca_de_titularidade": any(d["troca_de_titularidade"] for d in derivs), "outros_bancos_somados": a.incluir_outros_bancos,
        "total_descontado": tot_desc, "total_dobro": tot_dobro, "dano_moral": DANO_MORAL,
        "valor_causa": valor_causa, "valor_causa_extenso": brl_ext(valor_causa), "total_dobro_extenso": brl_ext(tot_dobro),
        "dano_moral_extenso": brl_ext(DANO_MORAL), "alertas": alertas, "conferir": conferir, "checagem_fsc": res_esc["fsc"], "checagem_vf": res_esc["vf"],
        "mesma_data": res_esc["mesma_data"], "marca": "CÁLCULO A CONFERIR",
    }
    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)
    (saida / "calculo.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")

    md = [f"# Cálculo do processo {a.processo} (NB {proc.get('nb')}): **CÁLCULO A CONFERIR**", "",
          f"Data da peça: {hoje.strftime('%d/%m/%Y')} · última competência de contrato ativo: {comp_str(mes_ref)}", "",
          "| Derivado | Raiz | Raiz: averbação → exclusão | Intervalo | 1ª averbação do derivado | Norma | Qtde | Parcela | Total | Dobro | Status |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for d in derivs:
        rd = d["raiz_dados"] or {}
        iv = {"MESMO_DIA": "mesmo dia", "ATE_30_DIAS": f"{d['intervalo_dias']} dia(s)", "MAIS_DE_30_DIAS": f"{d['intervalo_dias']} dias",
              "ANTES_DA_EXCLUSAO": f"{d['intervalo_dias']} dias (ANTES)", None: CONFERIR}[d["categoria_intervalo"]]
        md.append(f"| {d['contrato']} | {d['raiz']} | {rd.get('averbacao', CONFERIR)} → {rd.get('exclusao', CONFERIR)} | {iv} | {d['primeira_averbacao']} | {d['regime_norma']} | "
                  f"{d['qtde']} | {brl(d['parcela'])} | {brl(d['total'])} | {brl(d['dobro'])} | {d['status']} |")
    md += ["", f"- Total descontado: **{brl(tot_desc)}**", f"- Restituição em dobro: **{brl_ext(tot_dobro)}**",
           f"- Dano extrapatrimonial (fixo): **{brl(DANO_MORAL)}**",
           f"- Valor da causa: **{brl_ext(valor_causa)}**" + (" (Vara Federal: valor real, sem renúncia a teto)" if cod == "104" else ""),
           f"- Tutela de urgência: {'SIM, só sobre ' + ', '.join(ativos) if ativos else 'não (sem derivado ativo)'}",
           f"- Tópico de prescrição (algum desconto com mais de 5 anos): {'SIM' if prescricao else 'não'}",
           f"- Troca de titularidade (mesmo número em outro banco): {'SIM; descontos do outro banco ' + ('SOMADOS' if a.incluir_outros_bancos else 'NÃO somados') if out['troca_de_titularidade'] else 'não'}", ""]
    if conferir:
        md += ["## Conferir antes de protocolar", ""] + [f"- {x}" for x in conferir] + [""]
    if alertas:
        md += ["## Alertas", ""] + [f"- {x}" for x in alertas] + [""]
    md += ["", esc.para_markdown(res_esc)]
    (saida / "calculo.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    ev = esc.eventos_dos_contratos([d for d in derivs if d.get("inicio")], hoje, data_emissao(a.extrato))
    for d in derivs:
        rd = d.get("raiz_dados") or {}
        ev.append(esc.evento(rd.get("averbacao"), f"Averbação do contrato-raiz {d['raiz']}", "extrato do INSS, contrato-raiz", "contrato de origem"))
        ev.append(esc.evento(rd.get("exclusao"), f"Exclusão do contrato-raiz {d['raiz']}", "extrato do INSS, contrato-raiz",
                             "a partir daqui não há contrato a reaverbar"))
        if d.get("intervalo_dias") is not None:
            ev.append(esc.evento(d.get("primeira_averbacao"), f"Reaverbação do derivado {d['contrato']} ({d['intervalo_dias']} dia(s) depois da exclusão da raiz)",
                                 "extrato do INSS", f"categoria do intervalo: {d['categoria_intervalo']}; norma: {d.get('regime_norma')}"))
    if any(d.get("inclusao") for d in derivs):
        ev.append(esc.evento(esc.VIGENCIA_IN138, "Início da vigência da IN PRES/INSS 138/2022", "protocolo, \"Texto vigente e texto revogado\"",
                             "reaverbação até 12/12/2022 segue a IN 28/2008"))
    crono = esc.cronologia(ev)
    esc.gravar(saida, res_esc, "tese-1000", a.processo, hoje, out, a.extrato_bancario, a.dossie_pre_acao, crono)
    print(f"ok: {saida / 'calculo.json'} e calculo.md · valor da causa {brl(valor_causa)}")


if __name__ == "__main__":
    main()
