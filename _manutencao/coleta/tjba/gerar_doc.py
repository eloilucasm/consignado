"""Monta territorial-tjba.md: município -> comarca -> unidade que recebe o procedimento dos Juizados (Lei 9.099/95)."""
import json, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path

S, PAC, SAIDA = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
cz = json.loads((S / "cruzamento.json").read_text(encoding="utf-8"))
mc = json.loads((PAC / "_acervo/dados/tjba_comarcas.json").read_text(encoding="utf-8"))["municipio_comarca"]
vsj_det = json.loads((S / "unidades.json").read_text(encoding="utf-8"))
sem_acento = lambda s: unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().upper()

MIN = {"às", "e", "de", "da", "do", "dos", "das", "a", "o"}
def nome_vara(u):
    u = re.split(r"\s+PODER JUDICI", u)[0]
    u = re.sub(r"\bVAC[ÂA]NCIA TITULAR\b", "", u).strip(" .;")
    if re.fullmatch(r"(PLENA\s*)+", u, re.I) or re.fullmatch(r"PLENA", u.split()[0], re.I) and len(u.split()) <= 2:
        return "Vara de Jurisdição Plena"
    u = re.sub(r"^(\d+ª)\s+DOS", r"\1 VARA DOS", u, flags=re.I)
    u = re.sub(r"^DOS FEITOS", "VARA DOS FEITOS", u, flags=re.I)
    if not re.search(r"VARA", u, re.I):
        return None
    ws = u.lower().split()
    out = [w if (i and w in MIN) else (w[:1].upper() + w[1:]) for i, w in enumerate(ws)]
    s = " ".join(out).replace("Cíveis", "Cíveis").replace(" ,", ",")
    s = re.sub(r"Registro Público(?!s)", "Registros Públicos", s)
    return s

ADJUNTOS = {  # Juizados Especiais Adjuntos Cível e Criminal instituídos por decreto (fonte na seção 6)
    "Anagé": "Decreto Judiciário 812/2022", "Chorrochó": "Decreto Judiciário 813/2022", "Cocos": "Decreto Judiciário 814/2022",
    "Correntina": "Decreto Judiciário 815/2022", "Igaporã": "Decreto Judiciário 816/2022", "Macarani": "Decreto Judiciário 817/2022",
    "Maracás": "Decreto Judiciário 818/2022", "Planalto": "Decreto Judiciário 819/2022", "Serra Dourada": "Decreto Judiciário 820/2022",
    "Tanque Novo": "Decreto Judiciário 821/2022",
    "Antas": "decretos de 08/09/2022", "Barra da Estiva": "decretos de 08/09/2022", "Barra do Choça": "decretos de 08/09/2022",
    "Jitaúna": "decretos de 08/09/2022", "Laje": "decretos de 08/09/2022", "Terra Nova": "decretos de 08/09/2022",
}
GRAFIA = {"Camacã": "Camacan", "Santa Teresinha": "Santa Terezinha"}  # grafia das relações de 2026

linhas_vsj = defaultdict(list)
for u in vsj_det:
    if "Criminal" in u["unidade"]:
        continue
    linhas_vsj[u["comarca"]].append(u)

def comarca_info(c):
    base = c.split("/")[0].strip()
    x = cz["comarcas"][c]
    if base == "Salvador":
        return "FINAL", "vsj_ssa", []
    if x["vsj"]:
        return x["entrancia"], "vsj", [v["unidade"] for v in x["vsj"]]
    varas = []
    for u in x["civeis"]:
        n = nome_vara(re.sub(r"^PLENA\s+(?=VARA)", "", u, flags=re.I))
        if n and not re.search(r"Sistema d(e|os) Juizados", n) and n not in varas:
            varas.append(n)
    # tira o nome cortado (quebra de linha no PDF) quando há o nome inteiro, e a mesma vara com e sem número
    chave = lambda s: re.sub(r"^\d+ª ", "", s).rstrip(",")
    varas = [v for v in varas if not any(w != v and w.startswith(v) for w in varas)]  # mesmo número: nome cortado
    vistos, uniq = set(), []
    for v in sorted(varas, key=lambda s: (not re.match(r"^\d", s), s)):
        if (re.match(r"^\d+ª", v).group(0) if re.match(r"^\d+ª", v) else chave(v)) in vistos:
            continue
        vistos.add(re.match(r"^\d+ª", v).group(0) if re.match(r"^\d+ª", v) else chave(v)); uniq.append(v)
    varas = uniq
    if not varas and x["entrancia"] in ("INICIAL", "INTERMEDIÁRIA"):
        varas = ["Vara de Jurisdição Plena"]
    if "Vara de Jurisdição Plena" in varas and len(varas) > 1:
        varas = [v for v in varas if v != "Vara de Jurisdição Plena"]
    return x["entrancia"], "comum", varas

def ender(c, tipo, varas):
    base = c.split("/")[0].strip()
    nome = GRAFIA.get(base, base).upper()
    if tipo == "vsj_ssa":
        return "AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DO CONSUMIDOR DA COMARCA DE SALVADOR - BA"
    if tipo == "vsj":
        if len(varas) == 1:
            return f"AO JUÍZO DA {varas[0].upper()} DA COMARCA DE {nome} - BA"
        return f"AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE {nome} - BA"
    if varas == ["Vara de Jurisdição Plena"]:
        return f"AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE {nome} - BA"
    if len(varas) == 1:  # vara cível única: nome oficial inteiro
        return f"AO JUÍZO DA {varas[0].upper()} DA COMARCA DE {nome} - BA"
    if varas:  # mais de uma vara cível: o número e a competência saem na distribuição
        return f"AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE {nome} - BA"
    return "[CONFERIR: unidade cível da comarca]"

comarcas = sorted(cz["comarcas"], key=sem_acento)
info = {c: comarca_info(c) for c in comarcas}

def comum(c):
    """Justiça Comum: a(s) vara(s) cível(is) da comarca (sem as do Sistema dos Juizados)."""
    base = c.split("/")[0].strip()
    nome = GRAFIA.get(base, base).upper()
    if base == "Salvador":
        return ["1ª a 20ª Vara de Relações de Consumo"], "AO JUÍZO DA [N]ª VARA DE RELAÇÕES DE CONSUMO DA COMARCA DE SALVADOR - BA"
    e, t, v = info[c]
    if t == "vsj":
        x = cz["comarcas"][c]
        v = []
        for u in x["civeis"]:
            n = nome_vara(re.sub(r"^PLENA\s+(?=VARA)", "", u, flags=re.I))
            if n and not re.search(r"Sistema d(e|os) Juizados", n) and n not in v:
                v.append(n)
        chave = lambda s: re.sub(r"^\d+ª ", "", s).rstrip(",")
        v = [a for a in v if not any(w != a and w.startswith(a) for w in v)]
    if len(v) == 1:
        return v, f"AO JUÍZO DA {v[0].upper()} DA COMARCA DE {nome} - BA"
    if v:
        return v, f"AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE {nome} - BA"
    return [], "[CONFERIR: unidade cível da comarca]"

tabela = {}
for c in comarcas:
    e, t, v = info[c]
    base = c.split("/")[0].strip()
    cu, ce = comum(c)
    tabela[c] = {
        "grafia_2026": GRAFIA.get(base, base), "entrancia": (e or "").title() or None,
        "jec": {"tipo": "vara_do_sistema" if t in ("vsj", "vsj_ssa") else "vara_civel_com_procedimento_da_lei_9099",
                "unidades": (["1ª a 20ª Vara do Sistema dos Juizados Especiais do Consumidor"] if t == "vsj_ssa" else v),
                "enderecamento": ender(c, t, v)},
        "comum": {"unidades": cu, "enderecamento": ce},
        "juizado_adjunto": ADJUNTOS.get(base),
        "conferir": ("comarca de desativação automática (Resolução 13/2019); se desativada, usar a agrupadora" if "/" in c else None),
    }
(SAIDA.parent / "tjba_unidades.json").write_text(json.dumps({
    "fonte": "TJBA: quadro das Varas do Sistema dos Juizados (17/04/2026), Portal dos Juizados, relações de magistrados por entrância (22/09/2026 e 02/10/2026); comarcas de tjba_comarcas.json (15/03/2023). Ver territorial-tjba.md.",
    "consulta": "2026-11-03", "aprovado_pelo_escritorio": "2026-11-03", "comarcas": tabela}, ensure_ascii=False, indent=1),
    encoding="utf-8", newline="\n")
L = []
A = L.append
A("# Base territorial do TJBA para o Juizado Especial Cível (comarcas e unidades)")
A("")
A("> Fontes oficiais do TJBA consultadas em 03/11/2026 (lista na seção 6). Município → comarca: \"Relação Municípios x Comarca\" do TJBA, de 15/03/2023 (`_acervo/dados/tjba_comarcas.json`). Unidades: quadro das Varas do Sistema dos Juizados de 17/04/2026, páginas de endereços do Portal dos Juizados (capital e interior) e relações de magistrados por entrância de 22/09/2026 (final do interior e intermediária) e 02/10/2026 (inicial), que listam também as unidades vagas.")
A("> Só dados de unidade. Os documentos de origem trazem nomes de magistrados e servidores, que não foram copiados.")
A("")
A("## 1. Regra de endereçamento no Juizado Especial Cível (consignado contra banco)")
A("")
A("1. **Ache a comarca** do município de residência do autor no índice da seção 5 (`grep -n \"Nome do município\"`). A comarca nem sempre é o próprio município.")
A("2. **Comarca com Vara do Sistema dos Juizados Especiais** (seção 2; 40 comarcas): a petição vai à Vara do Sistema. Com mais de uma vara, o número sai na distribuição: deixe `[N]ª`. Em Salvador, a ação de consumo contra banco vai às **Varas do Sistema dos Juizados Especiais do Consumidor** (1ª a 20ª).")
A("3. **Comarca sem Vara do Sistema** (seção 3; as demais): não há unidade própria de Juizado. A Lei de Organização Judiciária da Bahia (Lei 10.845/2007, arts. 107 e 156) e a Lei estadual 7.033/1997 (art. 22) mandam que a causa da Lei 9.099/95 seja processada e decidida pelo juiz da comarca, **com a classe do Procedimento do Juizado Especial**. A petição vai à unidade cível da comarca: a **Vara de Jurisdição Plena** (entrância inicial e parte da intermediária) ou a **Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais** (havendo varas especializadas). Onde o TJBA instituiu Juizado Especial Adjunto por decreto, ele funciona anexado a essa mesma vara (seção 3, coluna \"Adjunto\").")
A("4. No corpo da petição, diga que a ação segue o **procedimento da Lei 9.099/95**: é isso que dá a classe do Juizado na comarca sem Vara do Sistema.")
A("5. Réu Caixa: Justiça Federal (`territorial-ba.md`), não esta tabela.")
A("")
A("**Decisão do escritório (03/11/2026).** Aprovada a forma desta tabela: nas 40 comarcas da seção 2, a Vara do Sistema dos Juizados Especiais; nas demais, a unidade cível da comarca (Vara de Jurisdição Plena ou Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais), com o procedimento da Lei 9.099/95 indicado no corpo da petição.")
A("")
A("**Para os scripts:** `references/dados/tjba_unidades.json` traz, por comarca, a entrância e o endereçamento pronto do JEC e da Justiça Comum (`jec.enderecamento`, `comum.enderecamento`). A comarca do município continua em `tjba_comarcas.json`.")
A("")

# ---- seção 2
n_vsj = [c for c in comarcas if info[c][1] in ("vsj", "vsj_ssa")]
A(f"## 2. Comarcas com Vara do Sistema dos Juizados Especiais ({len(n_vsj)})")
A("")
A("Nome oficial das unidades (competência cível e criminal no interior). Fonte: quadro de 17/04/2026 e Portal dos Juizados.")
A("")
A("| Comarca | Entrância | Unidade(s) do Juizado | Endereçamento no JEC | Endereçamento na Justiça Comum |")
A("|---|---|---|---|---|")
for c in n_vsj:
    e, t, v = info[c]
    if t == "vsj_ssa":
        unid = "1ª a 20ª Vara do Sistema dos Juizados Especiais do Consumidor; 1ª a 8ª de Causas Comuns; 1ª de Trânsito; 1ª e 2ª da Fazenda Pública"
    else:
        unid = "; ".join(v)
    A(f"| {GRAFIA.get(c, c)} | {(e or '').title()} | {unid} | {ender(c, t, v)} | {comum(c)[1]} |")
A("")
A("**Salvador (capital).** Varas do Sistema dos Juizados Especiais do **Consumidor**: 1ª a 20ª. As 1ª a 18ª substituíram os antigos Juizados de Defesa do Consumidor (Brotas, extensões NAJ e UNIJORGE, Juizado Modelo Federação, Universo). Há também as de **Causas Comuns** (1ª a 8ª), **Trânsito** (1ª) e **Fazenda Pública** (1ª e 2ª), e seis criminais. A ação de consumo contra banco vai às do Consumidor, por distribuição.")
A("")

# ---- seção 3
outros = [c for c in comarcas if info[c][1] == "comum"]
A(f"## 3. Comarcas sem Vara do Sistema dos Juizados ({len(outros)})")
A("")
A("A causa do Juizado tramita na unidade cível da comarca, com a classe do Procedimento do Juizado Especial (seção 1, item 3).")
A("")
A("Nestas comarcas, a mesma unidade cível recebe a ação no JEC e na Justiça Comum; o que muda é o procedimento indicado no corpo da petição.")
A("")
A("| Comarca | Entrância | Unidade cível | Adjunto | Endereçamento |")
A("|---|---|---|---|---|")
for c in outros:
    e, t, v = info[c]
    base = c.split("/")[0].strip()
    nota = " [CONFERIR: seção 4]" if "/" in c or base in GRAFIA else ""
    A(f"| {GRAFIA.get(base, base)}{' (' + c + ' na tabela de 2023)' if '/' in c else ''} | {(e or '[CONFERIR]').title()} | {'; '.join(v) or '[CONFERIR]'} | {ADJUNTOS.get(base, '—')} | {ender(c, t, v)}{nota} |")
A("")
A("\"Adjunto\" traz só os Juizados Especiais Adjuntos achados em decreto. Comarca sem decreto achado também julga a causa da Lei 9.099/95 pela regra dos arts. 107 e 156 da Lei 10.845/2007; a falta do decreto não muda o endereçamento.")
A("")

# ---- seção 4
A("## 4. Divergências e pontos a conferir")
A("")
A("- **Tabela município → comarca de 15/03/2023.** As relações de 2026 não mostraram comarca desativada depois dela, mas a tabela é anterior a três anos de atos. Refaça o cruzamento quando o TJBA publicar relação nova.")
A("- **São Félix e Tremedal.** A tabela de 2023 traz \"São Félix/Cachoeira\" e \"Tremedal/Belo Campo\", porque a Resolução TJBA 13/2019 desativa as duas automaticamente quando o juiz titular for removido ou promovido. Nas relações de 2026 ambas ainda aparecem como comarcas de Jurisdição Plena, São Félix com o titular vago e juiz designado. `[CONFERIR: se a desativação já ocorreu, use a comarca agrupadora (Cachoeira; Belo Campo)]`.")
A("- **Grafias.** \"Camacã\" (tabela de 2023) aparece como **Camacan** nas relações de 2026, e \"Santa Teresinha\" como **Santa Terezinha**. O endereçamento usa a grafia de 2026.")
A("- **Presidente Dutra.** Comarca desativada (Resolução 06/2017), agrupada a **Irecê**.")
A("- **Grafia de município diferente da base da Justiça Federal (`territorial-ba.md`).** A tabela do TJBA escreve \"Brotas de Macaúbas\", \"Muquém de São Francisco\", \"Oliveira de Brejinhos\", \"Camacã\" e \"Santa Teresinha\"; a base federal, \"Brotas da Macaúbas\", \"Muquém do São Francisco\", \"Oliveira dos Brejinhos\", \"Camacan\" e \"Santa Terezinha\". Barro Preto aparece duas vezes na tabela do TJBA (\"Barro Preto (Governador Lomanto Júnior)\" e \"Governador Lomanto Júnior (Barro Preto)\"), por isso o índice tem 418 linhas para 417 municípios. Busque pelo começo do nome.")
A("- **Varas criminais** não entram na tabela: só a unidade cível recebe a ação de consignado.")
A("")
if cz["desativadas"]:
    A(f"Comarcas desativadas lidas na relação da entrância inicial (02/10/2026), com a agrupadora: {len(cz['desativadas'])}. Elas já estão absorvidas pela tabela município → comarca e não recebem petição.")
    A("")

# ---- seção 5
A("## 5. Índice por município")
A("")
A("Município — comarca — unidade que recebe a causa do Juizado.")
A("")
for m in sorted(mc, key=sem_acento):
    c = mc[m]
    e, t, v = info[c]
    base = c.split("/")[0].strip()
    if t == "vsj_ssa":
        u = "Varas do Sistema dos Juizados Especiais do Consumidor (1ª a 20ª)"
    elif t == "vsj":
        u = "Vara do Sistema dos Juizados Especiais" if len(v) == 1 else f"Varas do Sistema dos Juizados Especiais (1ª a {len(v)}ª)"
    else:
        u = "; ".join(v) if v else "[CONFERIR]"
    A(f"- {m} — {GRAFIA.get(base, base)}{' (ver seção 4)' if '/' in c else ''} — {u}")
A("")

# ---- seção 6
A("## 6. Fontes (consulta em 03/11/2026)")
A("")
A("- Quadro das Varas do Sistema dos Juizados Especiais, 17/04/2026: <https://www.tjba.jus.br/juizadosespeciais/wp-content/uploads/2026/04/quadro-17-04-2026.pdf>")
A("- Portal dos Juizados Especiais, endereços do interior e da Região Metropolitana: <https://www.tjba.jus.br/juizadosespeciais/enderecos-e-telefones-interior/>; da capital: <https://www.tjba.jus.br/juizadosespeciais/enderecos-e-telefones-capital/>")
A("- Relações de magistrados (entrância final do interior e intermediária, 22/09/2026; inicial, 02/10/2026) e de unidades vagas com designação (22/09/2026): <https://www.tjba.jus.br/portal/relacao-de-magistrados/>")
A("- Relação Municípios x Comarca, 15/03/2023: <https://www.tjba.jus.br/portal/wp-content/uploads/2023/03/Relacao-Municipios-Comarca.pdf> (mesmo arquivo de `triagem-consignado/references/tjba_relacao_municipios_comarca.pdf`)")
A("- Decretos Judiciários 812 a 821, de 18/11/2022 (DJe 3220, de 21/11/2022), que instituem Juizados Especiais Adjuntos e citam os arts. 107 e 156 da Lei 10.845/2007 e o art. 22 da Lei 7.033/1997: <https://www.tjba.jus.br/portal/wp-content/uploads/2022/12/Juizados-adjuntos.pdf>")
A("- Notícia do TJBA de 08/09/2022 sobre os Juizados Adjuntos de Antas, Barra da Estiva, Barra do Choça, Jitaúna, Laje e Terra Nova: <https://www.tjba.jus.br/portal/pjba-institui-juizados-especiais-adjuntos-civel-e-criminal-em-seis-comarcas-do-interior/>")
A("- Corregedoria, comarcas agregadas e desativadas: <https://www.tjba.jus.br/corregedoria/comarcas/>")
A("")
SAIDA.write_text("\n".join(L), encoding="utf-8", newline="\n")
print("ok", len(mc), "municípios;", len(n_vsj), "comarcas com VSJ;", len(outros), "sem;",
      sum(1 for c in outros if not info[c][2]), "sem unidade")
