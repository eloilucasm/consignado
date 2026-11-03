#!/usr/bin/env python3
"""calcular.py - tabela de descontos, restituição em dobro e valor da causa (skill nao-contratado).

Lê a ficha de ajuizamento (saída da triagem) e o extrato do INSS do NB do processo e calcula, por contrato:
quantidade de descontos, total descontado, dobro e status. Soma o dano moral fixo e o valor da causa.
Faz uma SEGUNDA VIA de conferência (enumera mês a mês e soma de novo). Não escreve a peça.

Regras do escritório (protocolo.md, "Cálculos"):
  - quantidade = meses de "Início" a "Fim" do contrato, inclusive; 0 se o fim é anterior ao início;
  - contrato ATIVO conta até a competência do mês anterior à data da peça;
  - restituição = dobro do total descontado;
  - dano moral = R$ 20.000,00 (fixo);
  - valor da causa = restituição em dobro + dano moral (Vara Federal: valor real, sem renúncia a teto).
Todo número sai como CÁLCULO A CONFERIR.

Uso:
  python3 calcular.py --ficha ficha.json --processo 1 --extrato extrato.pdf --data 2026-10-28 --saida pasta/
Saídas: calculo.json (para o modelo) e calculo.md (tabela e alertas).
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extrato as ext  # noqa: E402
import escrutinio as esc  # noqa: E402

DANO_MORAL = 20000.00
CONFERIR = "[CONFERIR]"
AQUI = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------ formatação

sys.path.insert(0, str(Path(__file__).resolve().parent))
from valores import brl, brl_ext, inteiro_extenso  # noqa: E402,F401


def comp(s):
    m, a = s.split("/")
    return int(a) * 12 + int(m) - 1


def comp_str(n):
    return f"{n % 12 + 1:02d}/{n // 12}"


def data4(d):  # dd/mm/aa -> dd/mm/aaaa
    return f"{d[:6]}20{d[6:]}" if d and len(d) == 8 else d


# ------------------------------------------------------------------ principal

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
    sys.stdout.reconfigure(encoding="utf-8")  # no Windows, a saída redirecionada sairia em cp1252
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
    a = ap.parse_args()

    ficha = json.loads(Path(a.ficha).read_text(encoding="utf-8"))
    proc = next(p for p in ficha["processos"] if p["processo"] == a.processo)
    if proc["tese"] != "NAO_CONTRATADO":
        sys.exit(f"Processo {a.processo} é da tese {proc['tese']}; esta skill atende só NAO_CONTRATADO.")
    hoje = dt.date.fromisoformat(a.data)
    mes_ref = hoje.year * 12 + hoje.month - 2  # última competência já descontada (mês anterior)
    alertas, conferir = [], []

    reu, cod = carregar_reu(proc["reu"])
    if not reu:
        conferir.append(f"Réu {proc['reu']} (código {cod}) não está em references/dados/reus.json e a consulta pública (BCB + Receita) não resolveu ({_MSG_REU[0]}): preencher CNPJ e "
                        f"endereço com fonte e acrescentar à tabela.")
    eh_caixa = cod == "104"

    todos_ext = ext.contratos(a.extrato)
    lista = [r for r in todos_ext if r["inicio"]]
    linhas = []
    sel = []
    for c in proc["contratos"]:
        achados = ext.buscar(lista, c["contrato"])
        if not achados:
            conferir.append(f"Contrato {c['contrato']} não localizado no extrato: linha da tabela em branco.")
            linhas.append({"contrato": c["contrato"], "status": CONFERIR, "qtde": 0, "total": 0.0, "dobro": 0.0,
                           "ativo": False})
            continue
        do_reu = [x for x in achados if x["banco"].replace(" ", "").startswith(f"{cod}-")]
        if do_reu:
            achados = do_reu
        else:
            alertas.append(f"Contrato {c['contrato']}: nenhuma ocorrência no extrato com o código do réu ({cod}); "
                           f"conferir o banco.")
        r = next((x for x in achados if x["secao"] == "ATIVO"), achados[-1])
        sel.append(r)
        if len(achados) > 1:
            alertas.append(f"Contrato {c['contrato']} aparece {len(achados)}x no extrato para o réu; usada a "
                           f"ocorrência {'ativa' if r['secao'] == 'ATIVO' else 'mais recente'}.")
        ini, fim = comp(r["inicio"]), comp(r["fim"])
        ativo = r["secao"] == "ATIVO"
        ate = min(fim, mes_ref) if ativo else fim
        qtde = max(0, ate - ini + 1)
        total = round(qtde * r["parcela"], 2)
        # segunda via: soma mês a mês
        total2 = round(sum(r["parcela"] for _ in range(ini, ate + 1)), 2) if qtde else 0.0
        if abs(total - total2) > 0.005:
            alertas.append(f"Contrato {r['contrato']}: as duas vias do total divergem ({total} x {total2}).")
        status = "ATIVO" if ativo else ("ENCERRADO" if (r["situacao"] or "").startswith("Encerr") else "EXCLUÍDO")
        linhas.append({
            "contrato": r["contrato"], "inclusao": data4(r["inclusao"]), "inicio": r["inicio"], "fim": r["fim"],
            "parcela": r["parcela"], "liberado": r["liberado"], "qtde": qtde, "total": total,
            "dobro": round(2 * total, 2), "status": status, "ativo": ativo, "ini_n": ini, "ate_n": ate,
            "ate_comp": comp_str(ate) if qtde else None, "bloco": c.get("bloco"),
            "motivo_exclusao": r["motivo_exclusao"], "exclusao": data4(r["exclusao"]),
        })
        if c.get("bloco") in ("B", "C") and ativo:
            alertas.append(f"ANOMALIA: contrato {r['contrato']} (bloco {c['bloco']}) está ATIVO no extrato; a análise "
                           f"só põe contratos não ativos em B e C. Mostrar ao advogado.")
        if qtde and ini < comp("04/2021"):
            alertas.append(f"Contrato {r['contrato']}: há descontos anteriores a 30/03/2021. Usar o bloco [[SE HÁ DESCONTO ANTES DE "
                           f"30/03/2021]] do tópico da dobra: o EAREsp 676.608/RS foi modulado para pagamentos posteriores a essa data, e "
                           f"para os anteriores a dobra se apoia só no art. 42, parágrafo único, do CDC (decisão R7, 01/11/2026).")
        if liberado_zero(r):
            alertas.append(f"Contrato {r['contrato']}: valor liberado ausente ou R$ 0,00 no extrato (possível portabilidade "
                           f"pura). Examinar FSC4.")

    ativos = [l["contrato"] for l in linhas if l["ativo"]]
    tot_desc = round(sum(l["total"] for l in linhas), 2)
    tot_dobro = round(sum(l["dobro"] for l in linhas), 2)
    valor_causa = round(tot_dobro + DANO_MORAL, 2)
    com_desc = [l for l in linhas if l.get("qtde")]
    inicios = [l["ini_n"] for l in com_desc]
    limite5 = (hoje.year - 5) * 12 + hoje.month - 1
    limite10 = (hoje.year - 10) * 12 + hoje.month - 1
    prescricao = bool(inicios) and min(inicios) < limite5
    if inicios and min(inicios) < limite10:
        alertas.append("Há descontos com MAIS DE 10 ANOS: o tópico de prescrição não pode afirmar que todos estão no "
                       "prazo decenal. Decisão do advogado sobre o pedido dessas parcelas.")

    # segunda via do total geral
    if abs(sum(l["total"] for l in linhas) - tot_desc) > 0.005:
        alertas.append("Total geral não bate com a soma das linhas.")

    res_esc = esc.checagem(sel, todos_ext, "nao-contratado", hoje=hoje, rito=a.rito, extrato_bancario=a.extrato_bancario,
                           dossie_pre_acao=a.dossie_pre_acao)
    alertas.extend(x for x in res_esc["roteamento"] if x not in alertas)
    out = {
        "data_peca": hoje.isoformat(), "processo": a.processo, "nb": proc.get("nb"), "reu": proc["reu"],
        "reu_cadastrado": bool(reu), "caixa": eh_caixa, "competencia": proc.get("competencia"),
        "contratos": linhas, "ativos": ativos, "tutela": bool(ativos), "prescricao_5_anos": prescricao,
        "total_descontado": tot_desc, "total_dobro": tot_dobro, "dano_moral": DANO_MORAL,
        "valor_causa": valor_causa, "valor_causa_extenso": brl_ext(valor_causa),
        "dano_moral_extenso": brl_ext(DANO_MORAL), "alertas": alertas, "conferir": conferir, "checagem_fsc": res_esc["fsc"], "checagem_vf": res_esc["vf"],
        "mesma_data": res_esc["mesma_data"],
        "marca": "CÁLCULO A CONFERIR",
    }
    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)
    (saida / "calculo.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")

    md = [f"# Cálculo do processo {a.processo} (NB {proc.get('nb')}) — **CÁLCULO A CONFERIR**", "",
          f"Data da peça: {hoje.strftime('%d/%m/%Y')} · última competência de contrato ativo: {comp_str(mes_ref)}", "",
          "| Contrato | Status | Início | Fim usado | Qtde | Parcela | Total | Dobro |", "|---|---|---|---|---|---|---|---|"]
    for l in linhas:
        md.append(f"| {l['contrato']} | {l['status']} | {l.get('inicio', '')} | {l.get('ate_comp') or ''} | {l['qtde']} | "
                  f"{brl(l.get('parcela') or 0)} | {brl(l['total'])} | {brl(l['dobro'])} |")
    md += ["", f"- Total descontado: **{brl(tot_desc)}**",
           f"- Restituição em dobro: **{brl(tot_dobro)}**",
           f"- Dano moral (fixo): **{brl(DANO_MORAL)}**",
           f"- Valor da causa: **{brl_ext(valor_causa)}**" + (" (Vara Federal: valor real, sem renúncia a teto)" if eh_caixa else ""),
           f"- Tutela de urgência: {'SIM, só sobre ' + ', '.join(ativos) if ativos else 'não (sem contrato ativo)'}",
           f"- Tópico de prescrição (algum desconto com mais de 5 anos): {'SIM' if prescricao else 'não'}", ""]
    if conferir:
        md += ["## Conferir antes de protocolar", ""] + [f"- {x}" for x in conferir] + [""]
    if alertas:
        md += ["## Alertas", ""] + [f"- {x}" for x in alertas] + [""]
    md += ["", esc.para_markdown(res_esc)]
    (saida / "calculo.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    crono = esc.cronologia(esc.eventos_dos_contratos([l for l in linhas if l.get("inicio")], hoje, data_emissao(a.extrato)))
    esc.gravar(saida, res_esc, "nao-contratado", a.processo, hoje, out, a.extrato_bancario, a.dossie_pre_acao, crono)
    print(f"ok: {saida / 'calculo.json'} e calculo.md · valor da causa {brl(valor_causa)}")


def data_emissao(caminho):
    """Data de emissão do extrato do INSS (ciência dos descontos, padrão do escritório); None se não ler."""
    try:
        return ext.data_extrato(caminho)
    except Exception:
        return None


def liberado_zero(r):
    return r.get("liberado") in (None, 0, 0.0) and r.get("inclusao") is not None


if __name__ == "__main__":
    main()
