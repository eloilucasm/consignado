#!/usr/bin/env python3
"""fichas.py - fichas dos contratos e quadro de indícios da réplica de consignado (VF1 a VF9 sobre a contestação).

Cruza o extrato do INSS (scripts/extrato.py) com os dados que o advogado extraiu dos documentos do banco
(contestacao.json, formato em references/01-roteiro-e-vf.md) e grava:
  fichas.md    ficha de cada contrato impugnado, quadro de indícios com gravidade e o que fica para a geolocalização
  fichas.json  o mesmo, para a peça e para o dossiê do caso

Não lê PDF do banco nem imagem: só o que o advogado registrou, cada dado com a sua fonte (ID e página).
Não conclui sobre geolocalização nem IP: isso é do geo_check.py e do ip_check.py (VF4 e VF9).

Uso:  python3 fichas.py --extrato extrato.pdf --contestacao contestacao.json --saida pasta/
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extrato as ext  # noqa: E402
import escrutinio as esc  # noqa: E402

GRAV = ("CRÍTICO", "RELEVANTE", "REFORÇO", "PROCESSUAL", "ALERTA_CONTRA")
CAMPOS_CADASTRO = (("nb", "NB"), ("email", "e-mail"), ("telefone", "telefone"), ("endereco", "endereço"),
                   ("cep", "CEP"), ("estado_civil", "estado civil"))


def _brl(v):
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _norm(s):
    return "".join(ch for ch in str(s or "").lower() if ch.isalnum())


def indicio(lista, contrato, vf, achado, fonte, gravidade, fsc):
    assert gravidade in GRAV, gravidade
    lista.append({"contrato": contrato, "vf": vf, "achado": achado, "fonte": fonte or "[CONFERIR: ID e página]",
                  "gravidade": gravidade, "fsc": fsc})


def analisar(todos_ext, cont):
    """todos_ext: extrato.contratos(); cont: dict do contestacao.json. Devolve dict com fichas e indícios."""
    autor = cont.get("autor", {})
    impugnados = [str(c) for c in cont.get("impugnados", [])]
    defendidos = {str(d["contrato"]): d for d in cont.get("contratos_defendidos", [])}
    ind, fichas, alertas = [], [], []

    # escopo (VF1/VF2): impugnado sem defesa; defendido fora do escopo (substituição de objeto)
    for c in impugnados:
        if c not in defendidos:
            indicio(ind, c, "VF2", "contrato impugnado na inicial sem defesa específica na contestação: presumem-se verdadeiras as "
                    "alegações de fato não impugnadas (art. 341 do CPC)", "contestação", "PROCESSUAL", "FSC7")
    for c, d in defendidos.items():
        if c not in impugnados:
            alertas.append(f"O banco defende o contrato {c}, que não foi impugnado na inicial: possível substituição de objeto. "
                           f"Não aceitar a troca; o contrato impugnado continua sem defesa.")

    sel = []
    for c in impugnados:
        occ = ext.buscar(todos_ext, c)
        r = next((x for x in occ if x["secao"] == "ATIVO"), occ[-1]) if occ else None
        if r:
            sel.append(r)
        d = defendidos.get(c, {})
        f = {"contrato": c, "no_extrato": bool(r), "defendido": c in defendidos,
             "banco_extrato": r["banco"] if r else None, "origem_averbacao": r["origem_averbacao"] if r else None,
             "origem_tipo": esc.classificar_origem(r["origem_averbacao"]) if r else "SEM_DADO",
             "inclusao": r["inclusao"] if r else None, "exclusao": r["exclusao"] if r else None,
             "liberado": r["liberado"] if r else None, "parcela": r["parcela"] if r else None,
             "inicio": r["inicio"] if r else None, "fim": r["fim"] if r else None,
             "fonte_defesa": d.get("id_pagina")}
        if not r:
            alertas.append(f"Contrato {c} não localizado no extrato do INSS: conferir o número.")
        if not d:
            fichas.append(f)
            continue
        fonte = d.get("id_pagina")

        # VF2: instrumento, assinatura, datas
        if d.get("ccb_juntada") is False:
            indicio(ind, c, "VF2", "o banco não juntou o instrumento do contrato (CCB): não há documento cuja autenticidade se possa "
                    "examinar, e o ônus era dele (art. 14, § 3º, do CDC; art. 373, II, do CPC)", fonte, "CRÍTICO", "FSC1, FSC3")
        ass = d.get("assinatura")
        f["assinatura"] = ass
        if ass == "manuscrita":
            indicio(ind, c, "VF2", "assinatura manuscrita: autenticidade impugnada; só perícia grafotécnica a dirime (Justiça Comum: "
                    "requerer; JEC: valorar a dúvida contra o banco, art. 429, II, do CPC)", fonte, "RELEVANTE", "FSC1, FSC9")
        elif ass == "nenhuma":
            indicio(ind, c, "VF2", "instrumento sem assinatura da parte autora", fonte, "CRÍTICO", "FSC1")
        dt_ = d.get("datas", {})
        da, dtr = esc.data_de(dt_.get("assinatura_ccb")), esc.data_de(dt_.get("trilha"))
        if da and dtr and da < dtr:
            indicio(ind, c, "VF2", f"datas incoerentes: a CCB traz assinatura em {dt_['assinatura_ccb']}, antes da trilha de "
                    f"contratação ({dt_['trilha']})", fonte, "RELEVANTE", "FSC2, FSC7")

        # VF2: quadro comparativo de dados cadastrais
        cad = d.get("cadastro", {})
        comp = []
        for k, nome in CAMPOS_CADASTRO:
            a_, b_ = autor.get(k), cad.get(k)
            if a_ is None and b_ is None:
                continue
            div = (a_ is not None and b_ is not None and _norm(a_) != _norm(b_))
            comp.append({"campo": nome, "contrato": b_, "autor": a_, "diverge": div})
            if div:
                extra = (" (se comprovadamente de terceiro, o indício é CRÍTICO: [DECISÃO DO ADVOGADO])"
                         if k in ("email", "telefone") else "")
                extra = extra or (" (contrato com NB de outro benefício não poderia ter sido averbado neste)" if k == "nb" else "")
                indicio(ind, c, "VF2", f"{nome} da CCB ({b_}) diverge do da parte autora ({a_}){extra}", cad.get("fonte") or fonte,
                        "RELEVANTE", "FSC2, FSC7")
        f["cadastro_comparado"] = comp

        # VF6: TED x LIBERADO
        ted = d.get("ted")
        if ted and ted.get("valor") is not None:
            lib = r["liberado"] if r else None
            f["ted"] = ted
            if not r:
                pass
            elif lib in (None, 0, 0.0):
                indicio(ind, c, "VF6", f"TED de {_brl(ted['valor'])}, mas o extrato do INSS não registra valor liberado (portabilidade "
                        f"pura ou sem troco): o TED não prova crédito deste contrato", ted.get("fonte"), "CRÍTICO", "FSC4")
            elif abs(ted["valor"] - lib) > 0.01:
                indicio(ind, c, "VF6", f"TED de {_brl(ted['valor'])} diverge do valor liberado no extrato do INSS ({_brl(lib)}): o "
                        f"TED pode não corresponder ao contrato impugnado", ted.get("fonte"), "CRÍTICO", "FSC4")
            else:
                indicio(ind, c, "VF6", f"TED de {_brl(ted['valor'])} coincide com o valor liberado: depósito em conta não prova quem "
                        f"contratou nem que a parte usou o valor. Risco da Súmula 42/TJBA se a peça negar o recebimento "
                        f"[DECISÃO DO ADVOGADO: devolução, depósito ou compensação]", ted.get("fonte"), "ALERTA_CONTRA", "FSC4, FSC12")
            if ted.get("conta_mesma_do_beneficio") is False:
                indicio(ind, c, "VF6", "conta receptora do TED diferente da conta do benefício: o banco deve provar a titularidade e a "
                        "abertura da conta", ted.get("fonte"), "RELEVANTE", "FSC4")

        # VF3: cessão (migrado ou cessão alegada)
        ces = d.get("cessao")
        if f["origem_tipo"] == "MIGRADO" or ces:
            ces = ces or {}
            f["cessao"] = ces
            if not ces.get("instrumento"):
                indicio(ind, c, "VF3", "eixo existência: o banco não juntou instrumento de cessão que identifique este contrato "
                        "(CC, arts. 286 a 288)", ces.get("fonte") or fonte, "CRÍTICO", "FSC5")
            elif not ces.get("identifica_contrato") or not ces.get("assinaturas"):
                indicio(ind, c, "VF3", "eixo existência: o instrumento de cessão não identifica este contrato por número, data e valor, "
                        "ou não traz as assinaturas de cedente e cessionário", ces.get("fonte") or fonte, "RELEVANTE", "FSC5")
            if not ces.get("notificacao"):
                indicio(ind, c, "VF3", "eixo eficácia: não há notificação da cessão à parte autora (CC, art. 290); averbação e "
                        "descontos no extrato não substituem a notificação", ces.get("fonte") or fonte, "CRÍTICO", "FSC5")

        # VF5: correspondente
        cor = d.get("correspondente")
        if cor:
            f["correspondente"] = cor
            if cor.get("contrato_correspondencia") is False:
                indicio(ind, c, "VF5", f"correspondente {cor.get('nome') or ''} sem contrato de correspondência comprovado nos autos "
                        f"(Res. CMN 4.935/2021, art. 3º, ou Res. CMN 3.954/2011, art. 2º, conforme a data)", cor.get("fonte"), "CRÍTICO", "FSC10")
            if cor.get("uf") and autor.get("uf") and cor["uf"].upper() != autor["uf"].upper():
                indicio(ind, c, "VF5", f"correspondente sediado em {cor['uf']}, fora da UF da residência da parte autora ({autor['uf']})",
                        cor.get("fonte"), "RELEVANTE", "FSC10")

        # VF4: o que vai para o ip_check/geo_check
        log = d.get("log", {})
        f["log"] = log
        if log and not log.get("cidade_uf") and log.get("plataforma"):
            indicio(ind, c, "VF4", "campo de localização (Cidade-UF) vazio no log de assinatura", log.get("fonte"), "CRÍTICO", "FSC2, FSC10")
        fichas.append(f)

    # VF7: análise cruzada entre contratos
    for chave, nome, grav in (("hash", "hash do documento", "CRÍTICO"), ("selfie_id", "selfie", "RELEVANTE"), ("ip", "IP", "REFORÇO")):
        vistos = {}
        for c, d in defendidos.items():
            v = (d.get("log") or {}).get(chave)
            if v:
                vistos.setdefault(v, []).append(c)
        for v, cs in vistos.items():
            if len(cs) > 1:
                prop = "" if chave == "hash" else " (critério proposto, a validar)"
                indicio(ind, ", ".join(cs), "VF7", f"mesmo {nome} ({v}) em contratos distintos{prop}", "logs dos contratos", grav,
                        "FSC5" if chave == "hash" else "FSC2, FSC10")

    # VF8: mesma data (todos os bancos do extrato)
    md = esc.mesma_data(sel, todos_ext)
    for p in md:
        cs = " e ".join(f"{c} [{b}] em {i}" for c, b, i in p["contratos"])
        indicio(ind, p["contratos"][0][0], "VF8", f"{'mesmo dia' if p['tipo'] == 'MESMO_DIA' else str(p['dias']) + ' dias'}: {cs}",
                "extrato do INSS", "REFORÇO", "FSC11")

    ordem = {g: i for i, g in enumerate(("CRÍTICO", "RELEVANTE", "PROCESSUAL", "REFORÇO", "ALERTA_CONTRA"))}
    ind.sort(key=lambda x: (ordem[x["gravidade"]], x["contrato"]))
    geo = [{"contrato": c, "ip": (d.get("log") or {}).get("ip"), "cidade_uf": (d.get("log") or {}).get("cidade_uf"),
            "coordenadas": (d.get("log") or {}).get("coordenadas")} for c, d in defendidos.items() if d.get("log")]
    return {"fichas": fichas, "indicios": ind, "alertas": alertas, "mesma_data": md, "para_geo_ip": geo,
            "rito": cont.get("rito")}


def markdown(res):
    L = ["# Fichas dos contratos e quadro de indícios (réplica)", "",
         "Registro de trabalho, não entra na peça. Cada achado traz a fonte; o que estiver sem ID e página não pode ser usado.", ""]
    if res["alertas"]:
        L += ["## Alertas", ""] + [f"- {a}" for a in res["alertas"]] + [""]
    for f in res["fichas"]:
        L += [f"## Contrato {f['contrato']}", "",
              "| Campo | Valor |", "|---|---|",
              f"| Defendido na contestação | {'sim (' + (f.get('fonte_defesa') or '[CONFERIR]') + ')' if f['defendido'] else '**não** (art. 341 do CPC)'} |",
              f"| Banco no extrato | {f.get('banco_extrato') or '[CONFERIR]'} |",
              f"| Origem da averbação | {f.get('origem_averbacao') or '[CONFERIR]'} ({f['origem_tipo']}) |",
              f"| Inclusão / exclusão | {f.get('inclusao') or '—'} / {f.get('exclusao') or '—'} |",
              f"| Valor liberado (extrato) | {_brl(f['liberado']) if f.get('liberado') else 'não registrado'} |",
              f"| Assinatura | {f.get('assinatura') or '—'} |"]
        if f.get("ted"):
            L.append(f"| TED juntado pelo banco | {_brl(f['ted']['valor'])} em {f['ted'].get('data') or '—'} ({f['ted'].get('fonte') or '[CONFERIR]'}) |")
        L.append("")
        if f.get("cadastro_comparado"):
            L += ["| Dado | Na CCB | Da parte autora | Diverge? |", "|---|---|---|---|"]
            L += [f"| {x['campo']} | {x['contrato'] or 'não consta'} | {x['autor'] or 'não consta'} | {'**sim**' if x['diverge'] else 'não'} |"
                  for x in f["cadastro_comparado"]]
            L.append("")
    L += ["## Quadro de indícios", "", "| # | Contrato | VF | Achado | Fonte | Gravidade | FSC |", "|---|---|---|---|---|---|---|"]
    L += [f"| {i} | {x['contrato']} | {x['vf']} | {x['achado']} | {x['fonte']} | {x['gravidade']} | {x['fsc']} |"
          for i, x in enumerate(res["indicios"], 1)]
    L += ["", "Gravidade: CRÍTICO (objetivo e autônomo), RELEVANTE (pesa com contexto), REFORÇO (não decide sozinho), PROCESSUAL "
          "(efeito de processo, como o art. 341 do CPC), ALERTA_CONTRA (pesa contra a parte autora e pede decisão).", ""]
    if res["para_geo_ip"]:
        L += ["## Para o ip_check.py e o geo_check.py (VF4 e VF9)", ""]
        L += [f"- {g['contrato']}: IP {g['ip'] or '—'}; Cidade-UF {g['cidade_uf'] or 'vazio'}; coordenadas {g['coordenadas'] or 'não constam'}"
              for g in res["para_geo_ip"]]
        L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extrato", required=True)
    ap.add_argument("--contestacao", required=True)
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()
    cont = json.loads(Path(a.contestacao).read_text(encoding="utf-8"))
    res = analisar(ext.contratos(a.extrato), cont)
    s = Path(a.saida)
    s.mkdir(parents=True, exist_ok=True)
    (s / "fichas.json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    (s / "fichas.md").write_text(markdown(res), encoding="utf-8", newline="\n")
    crit = sum(1 for x in res["indicios"] if x["gravidade"] == "CRÍTICO")
    print(f"ok: {s / 'fichas.md'} · {len(res['fichas'])} contrato(s) · {len(res['indicios'])} indício(s), {crit} crítico(s)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
