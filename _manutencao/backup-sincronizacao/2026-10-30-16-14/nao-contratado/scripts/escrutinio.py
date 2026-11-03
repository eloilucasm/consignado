#!/usr/bin/env python3
"""Escrutínio FSC e VF da inicial de consignado (ver assets/escrutinio-fsc-vf.md).

Recebe os contratos lidos do extrato do INSS (extrato.contratos()) e devolve, para cada FSC de 1 a 12 e cada VF de 1 a 9,
um status e o achado. O que o extrato permite apurar sozinho é calculado (FSC4, FSC5, FSC6, FSC11, VF3, VF6, VF7, VF8);
o que depende de documento ou de decisão fica PENDENTE_ADVOGADO. Nada aqui entra na peça: é registro de trabalho.

Status das FSC: ATIVADO (o risco existe neste caso e a peça precisa tratá-lo), OK (tratado no modelo da skill),
NAO_SE_APLICA, PENDENTE_ADVOGADO. Status das VF: EXECUTADA, NAO_SE_APLICA, PENDENTE_ADVOGADO.

Uso como módulo:
    import escrutinio as esc
    res = esc.checagem(do_processo, todos, skill="nao-contratado", hoje=hoje, rito="jec",
                       extrato_bancario=None, dossie_pre_acao=False)
    res["fsc"], res["vf"], res["roteamento"], res["mesma_data"]
    esc.para_markdown(res)

Autoteste: python3 escrutinio.py --teste
"""
import datetime as dt
import re
import sys

STATUS_FSC = ("ATIVADO", "OK", "NAO_SE_APLICA", "PENDENTE_ADVOGADO")
STATUS_VF = ("EXECUTADA", "NAO_SE_APLICA", "PENDENTE_ADVOGADO")
INTERVALO_CURTO_DIAS = 7  # decisão do escritório de 29/10/2026 (VF8): mesmo dia = alerta; até 7 dias = reforço
RE_DERIVADO = re.compile(r"^(.+?)(_\d{1,4})$")


# ------------------------------------------------------------------ utilidades

def data_de(s):
    """dd/mm/aa ou dd/mm/aaaa -> date (None se não for data)."""
    m = re.fullmatch(r"(\d{2})/(\d{2})/(\d{2}|\d{4})", s or "")
    if not m:
        return None
    d, mes, a = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return dt.date(a + 2000 if a < 100 else a, mes, d)


def comp_n(s):
    """MM/AAAA -> número de meses (None se vazio)."""
    if not s:
        return None
    m, a = s.split("/")
    return int(a) * 12 + int(m) - 1


def classificar_origem(origem):
    """Classifica o campo 'Origem da Averbação' do extrato do INSS.

    'Migrado do contrato …' é o valor conferido nos extratos do escritório. Os demais rótulos (portabilidade,
    refinanciamento, compra de dívida) seguem o layout do INSS e devem ser conferidos na primeira leitura de extrato real.
    """
    o = (origem or "").lower()
    if "migrad" in o:
        return "MIGRADO"
    if "portabil" in o:
        return "PORTABILIDADE"
    if "refinanc" in o:
        return "REFINANCIAMENTO"
    if "compra" in o and "d" in o:
        return "COMPRA_DIVIDA"
    return "NOVO" if o else "SEM_DADO"


def _brl(v):
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def fsc4_contrato(r):
    """LIBERADO_ZERO (portabilidade pura ou sem crédito), LIBERADO_POSITIVO ou SEM_DADO."""
    if not r.get("inclusao"):
        return "SEM_DADO"
    lib = r.get("liberado")
    if lib in (None, 0, 0.0):
        return "LIBERADO_ZERO"
    return "LIBERADO_POSITIVO"


def mais_de_5_anos(r, hoje):
    ini = comp_n(r.get("inicio"))
    if ini is None:
        return False
    limite5 = (hoje.year - 5) * 12 + hoje.month - 1
    return ini < limite5


def derivado(contrato):
    m = RE_DERIVADO.match(contrato or "")
    return (m.group(1), m.group(2)) if m else (None, None)


# ------------------------------------------------------------------ mesma data (FSC11, VF8)

def mesma_data(do_processo, todos, dias=INTERVALO_CURTO_DIAS):
    """Inclusões no mesmo dia (alerta) ou até `dias` dias (reforço), em qualquer banco do extrato.

    Só entram pares em que ao menos um contrato é do processo. Devolve lista de
    {tipo: 'MESMO_DIA'|'INTERVALO_CURTO', dias, contratos: [(contrato, banco, inclusao)]}.
    """
    nums = {id(r) for r in do_processo}
    chaves = {(r["contrato"], r.get("banco")) for r in do_processo}
    pares = []
    vistos = set()
    for a in do_processo:
        da = data_de(a.get("inclusao"))
        if not da:
            continue
        for b in todos:
            if (b["contrato"], b.get("banco")) == (a["contrato"], a.get("banco")):
                continue
            db = data_de(b.get("inclusao"))
            if not db:
                continue
            delta = abs((da - db).days)
            if delta > dias:
                continue
            chave = frozenset({(a["contrato"], a.get("banco")), (b["contrato"], b.get("banco"))})
            if chave in vistos:
                continue
            vistos.add(chave)
            pares.append({"tipo": "MESMO_DIA" if delta == 0 else "INTERVALO_CURTO", "dias": delta,
                          "contratos": [(a["contrato"], a.get("banco"), a.get("inclusao")),
                                        (b["contrato"], b.get("banco"), b.get("inclusao"))]})
    pares.sort(key=lambda p: (p["dias"], p["contratos"][0][0]))
    return pares


# ------------------------------------------------------------------ roteamento (outra skill seria a certa?)

def roteamento(do_processo, skill):
    """Alertas de que o extrato sugere outra tese. Não bloqueia: o advogado decide."""
    avisos = []
    for r in do_processo:
        c = r["contrato"]
        orig = classificar_origem(r.get("origem_averbacao"))
        raiz, suf = derivado(c)
        if skill != "migrado" and orig == "MIGRADO":
            avisos.append(f"ROTEAMENTO: o contrato {c} tem origem de migração no extrato ('{r.get('origem_averbacao')}'): "
                          f"o caso é da skill `migrado`.")
        if skill != "tese-1000" and suf:
            avisos.append(f"ROTEAMENTO: o contrato {c} tem sufixo {suf} sobre o número-raiz {raiz}: pode ser derivado de "
                          f"contrato excluído, caso da skill `tese-1000`.")
        if skill == "migrado" and orig != "MIGRADO":
            avisos.append(f"ROTEAMENTO: o contrato {c} não tem origem de migração no extrato "
                          f"('{r.get('origem_averbacao')}'): pode ser caso de `nao-contratado`.")
    return avisos


# ------------------------------------------------------------------ checagem

def _fsc(n, status, achado, onde):
    assert status in STATUS_FSC, status
    return {"fsc": n, "status": status, "achado": achado, "onde_na_peca": onde}


def _vf(n, status, achado):
    assert status in STATUS_VF, status
    return {"vf": n, "status": status, "achado": achado}


def checagem(do_processo, todos, skill, hoje=None, rito=None, extrato_bancario=None, dossie_pre_acao=False,
             dias_curto=INTERVALO_CURTO_DIAS):
    """Monta o registro FSC1 a FSC12 e VF1 a VF9 de um processo.

    do_processo: ocorrências do extrato que entram no processo (dicts de extrato.contratos()); pode ser [] (RMC).
    todos: todas as ocorrências do extrato (todos os bancos), para FSC11/VF8.
    rito: 'jec', 'comum' ou None (ainda não informado).
    extrato_bancario: 'sim' (cliente trouxe o extrato do mês da averbação), 'nao' ou None (não informado).
    """
    hoje = hoje or dt.date.today()
    f4 = [(r["contrato"], fsc4_contrato(r), r.get("liberado")) for r in do_processo]
    origens = [(r["contrato"], classificar_origem(r.get("origem_averbacao")), r.get("origem_averbacao")) for r in do_processo]
    md = mesma_data(do_processo, todos, dias_curto)
    rot = roteamento(do_processo, skill)
    fsc = []

    fsc.append(_fsc(1, "OK", "negativa específica por contrato no modelo; conferir que cada número aparece na negativa",
                    "subtópico da negativa de contratação"))
    fsc.append(_fsc(2, "OK", "a parte não usou plataforma digital nem forneceu biometria; autenticação controvertida por antecipação",
                    "subtópico da negativa de contratação"))
    fsc.append(_fsc(3, "OK", "art. 14, § 3º, do CDC + art. 429, II, do CPC + Tema 1061/STJ antes do art. 6º, VIII",
                    "tópico da inversão do ônus da prova"))

    # FSC4
    if not f4:
        fsc.append(_fsc(4, "PENDENTE_ADVOGADO", "sem contrato do extrato neste cálculo: tratar o valor liberado pelas faturas ou pelo extrato bancário",
                        "fatos e tabela de documentos"))
    elif any(s == "LIBERADO_POSITIVO" for _, s, _ in f4):
        det = "; ".join(f"{c}: liberado {_brl(v)}" for c, s, v in f4 if s == "LIBERADO_POSITIVO")
        eb = {"sim": "extrato bancário do cliente trazido: comparar o crédito com o valor liberado",
              "nao": "cliente não tem o extrato bancário: decisão do advogado",
              None: "extrato bancário do mês da averbação ainda não informado"}[extrato_bancario]
        fsc.append(_fsc(4, "ATIVADO", f"{det}. {eb}. Risco da Súmula 42/TJBA se o crédito chegou à conta e a peça nega tudo "
                        f"[DECISÃO DO ADVOGADO: devolução, depósito ou compensação]", "fatos; tabela de documentos; pedido"))
    elif any(s == "LIBERADO_ZERO" for _, s, _ in f4):
        fsc.append(_fsc(4, "ATIVADO", "valor liberado ausente ou R$ 0,00 (possível portabilidade pura): registrar e não afirmar que não houve "
                        "crédito sem prova", "fatos; tabela de documentos"))
    else:
        fsc.append(_fsc(4, "PENDENTE_ADVOGADO", "sem dado do valor liberado no extrato", "fatos e tabela de documentos"))

    # FSC5
    cess = [(c, o, t) for c, o, t in origens if o in ("MIGRADO", "PORTABILIDADE", "REFINANCIAMENTO", "COMPRA_DIVIDA")]
    if cess and skill == "migrado":
        fsc.append(_fsc(5, "OK", "; ".join(f"{c}: {t}" for c, o, t in cess) + ". Tese da skill: cessão não notificada ao devedor (CC, art. 290)",
                        "tópico da migração e da cessão"))
    elif cess:
        fsc.append(_fsc(5, "ATIVADO", "; ".join(f"{c}: origem {o.lower()} ('{t}')" for c, o, t in cess) +
                        ". Questionar a cadeia (existência e eficácia, CC, arts. 286 a 290) ou rotear para a skill certa",
                        "ver roteamento"))
    else:
        fsc.append(_fsc(5, "NAO_SE_APLICA", "sem origem de migração, portabilidade ou refinanciamento no extrato", "—"))

    # FSC6
    antigos = [r["contrato"] for r in do_processo if mais_de_5_anos(r, hoje)]
    if antigos:
        fsc.append(_fsc(6, "ATIVADO", f"contrato(s) {', '.join(antigos)} com desconto iniciado há mais de 5 anos: tratar prescrição "
                        f"(decisão do advogado) e a data da ciência", "fatos (ciência); tópico de prescrição"))
    else:
        fsc.append(_fsc(6, "PENDENTE_ADVOGADO", "registrar quando e como a parte soube dos descontos; separar inexistência (não prescreve) de repetição e dano",
                        "fatos (ciência)"))

    fsc.append(_fsc(7, "OK", "negativa específica por contrato e pedido de juntada de cada documento com a contestação; o risco maior é da réplica",
                    "negativa específica; inversão do ônus"))
    fsc.append(_fsc(8, "PENDENTE_ADVOGADO", "natureza alimentar, período e valor vêm do cálculo; reclamação prévia ao banco precisa constar do quadro de fatos",
                    "subtópico do dano extrapatrimonial"))
    if rito == "jec":
        fsc.append(_fsc(9, "OK", "JEC: sem exibição nem perícia; inversão do ônus e encargo de juntar documentos com a contestação",
                        "inversão do ônus"))
    elif rito == "comum":
        fsc.append(_fsc(9, "OK", "Justiça Comum: exibição (arts. 396 a 404 do CPC) e perícia com quesitos pedidas já na inicial",
                        "exibição e perícia"))
    else:
        fsc.append(_fsc(9, "PENDENTE_ADVOGADO", "rito ainda não informado (JEC ou Justiça Comum)", "—"))
    fsc.append(_fsc(10, "PENDENTE_ADVOGADO", "pedir que o banco identifique o correspondente e junte a trilha completa; registrar a residência do cliente com ID e página para a réplica",
                    "tabela de documentos"))

    # FSC11
    if md:
        forte = [p for p in md if p["tipo"] == "MESMO_DIA"]
        tx = "; ".join(f"{p['tipo'].lower().replace('_', ' ')} ({p['dias']} d): " +
                       " e ".join(f"{c} [{b}] em {i}" for c, b, i in p["contratos"]) for p in md[:6])
        tese_mesma_data = skill == "tese-1000"
        fsc.append(_fsc(11, "OK" if tese_mesma_data else "ATIVADO",
                        tx + (". Na Tese 1000 o intervalo é a própria tese" if tese_mesma_data else
                              (". Mesmo dia: alerta; até 7 dias: reforço. Descrever só pelo extrato" if forte else ". Reforço: descrever só pelo extrato")),
                        "fatos"))
    elif skill == "tese-1000":
        fsc.append(_fsc(11, "OK", "o intervalo entre a exclusão da raiz e a reaverbação do derivado é a própria tese (categoria_intervalo no calculo.json)", "fatos"))
    else:
        fsc.append(_fsc(11, "NAO_SE_APLICA", f"nenhuma inclusão no mesmo dia nem em até {dias_curto} dias de outro contrato do extrato", "—"))

    fsc.append(_fsc(12, "PENDENTE_ADVOGADO", "documentos de identidade e residência atuais e legíveis; procuração atualizada; um processo por benefício + banco + tese; nada sobre outras ações",
                    "lista de documentos"))

    # VF
    vf = []
    vf.append(_vf(1, "PENDENTE_ADVOGADO", "índice dos documentos do cliente (ID provisório de cada um)"))
    for n, nome in ((2, "ficha do contrato"), (4, "autenticação eletrônica"), (5, "correspondente bancário")):
        if dossie_pre_acao:
            vf.append(_vf(n, "PENDENTE_ADVOGADO", f"há dossiê do banco entregue antes da ação: impugnar já na inicial ({nome})"))
        else:
            vf.append(_vf(n, "NAO_SE_APLICA", f"sem documento do banco antes da ação; {nome} fica para a réplica"))
    mig = [(c, t) for c, o, t in origens if o == "MIGRADO"]
    vf.insert(2, _vf(3, "EXECUTADA", "; ".join(f"{c}: {t}" for c, t in mig)) if mig else
              _vf(3, "NAO_SE_APLICA", "extrato sem origem de migração"))
    if f4 and extrato_bancario == "sim":
        vf.append(_vf(6, "PENDENTE_ADVOGADO", "extrato bancário trazido: confrontar o crédito do mês da averbação com o valor liberado do extrato do INSS"))
    elif f4:
        vf.append(_vf(6, "PENDENTE_ADVOGADO", "pedir ao cliente o extrato bancário do mês da averbação de cada contrato (Súmula 42/TJBA)"))
    else:
        vf.append(_vf(6, "NAO_SE_APLICA", "sem contrato do extrato neste cálculo"))
    mesmo_banco = [p for p in md if len({b for _, b, _ in p["contratos"]}) == 1]
    vf.append(_vf(7, "EXECUTADA" if do_processo else "NAO_SE_APLICA",
                  (f"{len(mesmo_banco)} par(es) do mesmo banco em datas próximas" if mesmo_banco else "sem repetição de datas entre contratos do mesmo banco")
                  if do_processo else "sem contrato do extrato neste cálculo"))
    vf.append(_vf(8, "EXECUTADA" if do_processo else "NAO_SE_APLICA", f"{len(md)} par(es) até {dias_curto} dias" if do_processo else "sem contrato do extrato neste cálculo"))
    vf.append(_vf(9, "PENDENTE_ADVOGADO", "registrar a residência com ID e página (e coordenada, se houver) para a geolocalização da réplica"))
    vf.sort(key=lambda x: x["vf"])

    return {"fsc": fsc, "vf": vf, "roteamento": rot, "mesma_data": md}


# ------------------------------------------------------------------ saída

def para_markdown(res, titulo="Checagem FSC e VF"):
    L = [f"## {titulo}", "", "| FSC | Status | Achado | Onde a peça trata |", "|---|---|---|---|"]
    for f in res["fsc"]:
        L.append(f"| FSC{f['fsc']} | {f['status']} | {f['achado']} | {f['onde_na_peca']} |")
    L += ["", "| VF | Status | Achado |", "|---|---|---|"]
    for v in res["vf"]:
        L.append(f"| VF{v['vf']} | {v['status']} | {v['achado']} |")
    if res["roteamento"]:
        L += ["", "**Roteamento:**"] + [f"- {x}" for x in res["roteamento"]]
    return "\n".join(L) + "\n"


def pendencias(res):
    """FSC ATIVADO ou PENDENTE_ADVOGADO: o que ainda impede marcar o portão 3 como passou."""
    return [f for f in res["fsc"] if f["status"] in ("ATIVADO", "PENDENTE_ADVOGADO")]


def gravar(saida, res, skill, processo, hoje, calculo=None, extrato_bancario=None, dossie_pre_acao=False):
    """Grava, ao lado da peça, o registro de trabalho `checagem-fsc-vf.md` e o `dossie-do-caso.json`.

    O dossiê é arquivo do CASO (não da skill): o advogado o leva para a réplica ou o recurso. Qualquer skill funciona sem ele.
    """
    import json
    from pathlib import Path
    saida = Path(saida)
    saida.mkdir(parents=True, exist_ok=True)
    pend = pendencias(res)
    L = [f"# Checagem FSC e VF: processo {processo} ({skill}) em {hoje.strftime('%d/%m/%Y')}", "",
         "Registro de trabalho: não entra na peça. Formato e regras em `assets/escrutinio-fsc-vf.md`.", "",
         "| FSC | Status | Achado | Onde a peça trata |", "|---|---|---|---|"]
    L += [f"| FSC{f['fsc']} | {f['status']} | {f['achado']} | {f['onde_na_peca']} |" for f in res["fsc"]]
    L += ["", "| VF | Status | Achado |", "|---|---|---|"]
    L += [f"| VF{v['vf']} | {v['status']} | {v['achado']} |" for v in res["vf"]]
    if res["roteamento"]:
        L += ["", "**Roteamento:**"] + [f"- {x}" for x in res["roteamento"]]
    L += ["", f"**Portão 3:** {'PENDENTE' if pend else 'PASSOU'}"
          + (f" ({len(pend)} FSC ativado(s) ou pendente(s): " + ", ".join(f"FSC{f['fsc']}" for f in pend) + ")" if pend else ""), "",
          "**Para a réplica:** FSC7 (impugnar um a um os documentos que o banco juntar), FSC1/FSC2 (autenticidade), FSC4 e VF6 (confrontar o TED com o "
          "valor liberado), FSC10 e VF9 (correspondente, IP e geolocalização com a residência registrada)."]
    (saida / "checagem-fsc-vf.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    dossie = {
        "versao": 1, "skill": skill, "processo": processo, "data": hoje.isoformat(),
        "calculo": calculo, "checagem": {"fsc": res["fsc"], "vf": res["vf"], "roteamento": res["roteamento"], "mesma_data": res["mesma_data"]},
        "quadro_de_fatos": {"data_ciencia": None, "reclamacao_previa": None, "extrato_bancario": extrato_bancario,
                            "dossie_pre_acao": bool(dossie_pre_acao),
                            "residencia": {"id": None, "pagina": None, "coordenada": None}},
    }
    (saida / "dossie-do-caso.json").write_text(json.dumps(dossie, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")


# ------------------------------------------------------------------ autoteste

def _r(contrato, banco, inclusao, liberado, origem="Averbação normal", inicio="01/2024", fim="12/2024"):
    return {"contrato": contrato, "banco": banco, "inclusao": inclusao, "liberado": liberado, "origem_averbacao": origem,
            "inicio": inicio, "fim": fim, "secao": "EXCLUIDO"}


def _teste():
    hoje = dt.date(2026, 10, 29)
    a = _r("111", "934 - BANCO A", "10/01/24", 2000.0)
    b = _r("222", "934 - BANCO A", "10/01/24", 0.0, origem="Portabilidade de empréstimo")
    c = _r("333", "623 - BANCO B", "15/01/24", 1500.0, origem="Migrado do contrato 999 CBC: 341")
    d = _r("444_0001", "934 - BANCO A", "02/02/24", None, inicio="01/2019", fim="12/2019")
    todos = [a, b, c, d]

    assert classificar_origem("Migrado do contrato 999 CBC: 341") == "MIGRADO"
    assert classificar_origem("Portabilidade de empréstimo") == "PORTABILIDADE"
    assert classificar_origem("Averbação normal") == "NOVO"
    assert classificar_origem(None) == "SEM_DADO"
    assert fsc4_contrato(a) == "LIBERADO_POSITIVO" and fsc4_contrato(b) == "LIBERADO_ZERO"
    assert fsc4_contrato({"inclusao": None}) == "SEM_DADO"
    assert derivado("444_0001") == ("444", "_0001") and derivado("444") == (None, None)

    md = mesma_data([a], todos)
    tipos = {p["tipo"]: p for p in md}
    assert "MESMO_DIA" in tipos and tipos["MESMO_DIA"]["dias"] == 0          # a e b
    assert "INTERVALO_CURTO" in tipos and tipos["INTERVALO_CURTO"]["dias"] == 5  # a e c (5 dias)
    assert all(p["dias"] <= 7 for p in md)
    assert mesma_data([d], todos) == []                                       # 02/02/24 está a 23 dias dos outros
    assert len(mesma_data([a], todos, dias=3)) == 1                           # só o mesmo dia

    rot = roteamento([c, d], "nao-contratado")
    assert any("`migrado`" in x for x in rot) and any("`tese-1000`" in x for x in rot)
    assert not any("ROTEAMENTO" in x for x in roteamento([c], "migrado"))
    assert any("`nao-contratado`" in x for x in roteamento([a], "migrado"))

    res = checagem([a, b], todos, "nao-contratado", hoje=hoje, rito="jec")
    s = {f["fsc"]: f["status"] for f in res["fsc"]}
    assert len(res["fsc"]) == 12 and len(res["vf"]) == 9
    assert s[4] == "ATIVADO" and "Súmula 42" in res["fsc"][3]["achado"] and "R$ 2.000,00" in res["fsc"][3]["achado"]
    assert s[9] == "OK" and s[11] == "ATIVADO" and s[1] == "OK" and s[8] == "PENDENTE_ADVOGADO"
    assert checagem([a], todos, "nao-contratado", hoje=hoje, rito=None)["fsc"][8]["status"] == "PENDENTE_ADVOGADO"
    assert checagem([a], todos, "nao-contratado", hoje=hoje, rito="comum")["fsc"][8]["status"] == "OK"

    res_d = checagem([d], todos, "nao-contratado", hoje=hoje, rito="jec")
    assert {f["fsc"]: f["status"] for f in res_d["fsc"]}[6] == "ATIVADO"      # início em 2019: mais de 5 anos
    assert {f["fsc"]: f["status"] for f in res_d["fsc"]}[11] == "NAO_SE_APLICA"
    assert any("tese-1000" in x for x in res_d["roteamento"])

    res_c = checagem([c], todos, "migrado", hoje=hoje, rito="jec")
    assert {f["fsc"]: f["status"] for f in res_c["fsc"]}[5] == "OK"
    assert {v["vf"]: v["status"] for v in res_c["vf"]}[3] == "EXECUTADA"
    assert {f["fsc"]: f["status"] for f in checagem([c], todos, "nao-contratado", hoje=hoje, rito="jec")["fsc"]}[5] == "ATIVADO"

    vf = {v["vf"]: v["status"] for v in checagem([a], todos, "nao-contratado", hoje=hoje, dossie_pre_acao=True)["vf"]}
    assert vf[2] == vf[4] == vf[5] == "PENDENTE_ADVOGADO"
    vf = {v["vf"]: v["status"] for v in checagem([a], todos, "nao-contratado", hoje=hoje)["vf"]}
    assert vf[2] == vf[4] == vf[5] == "NAO_SE_APLICA" and vf[6] == "PENDENTE_ADVOGADO"

    vazio = checagem([], [], "rmc", hoje=hoje, rito="jec")                     # RMC: sem contratos do extrato
    assert len(vazio["fsc"]) == 12 and {f["fsc"]: f["status"] for f in vazio["fsc"]}[4] == "PENDENTE_ADVOGADO"
    assert "FSC4" in para_markdown(res) and len(pendencias(res)) >= 3
    import tempfile
    from pathlib import Path
    with tempfile.TemporaryDirectory() as tmp:
        gravar(tmp, res, "nao-contratado", 1, hoje, {"x": 1})
        md = (Path(tmp) / "checagem-fsc-vf.md").read_text(encoding="utf-8")
        assert "FSC4" in md and "VF9" in md and "Portão 3:** PENDENTE" in md
        import json
        dj = json.loads((Path(tmp) / "dossie-do-caso.json").read_text(encoding="utf-8"))
        assert dj["versao"] == 1 and len(dj["checagem"]["fsc"]) == 12 and dj["quadro_de_fatos"]["residencia"]["id"] is None
    print("escrutinio.py: autoteste OK")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--teste":
        sys.stdout.reconfigure(encoding="utf-8")
        _teste()
    else:
        sys.exit(__doc__)
