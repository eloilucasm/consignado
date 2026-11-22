"""Base territorial de MG, PR e SC para o endereçamento (comarca do autor -> juízo e fecho).

Lê as fontes fornecidas pelo escritório em 22/11/2026 (pastas tjmg/, tjpr/, tjsc/ ao lado deste script)
e a lista de municípios do IBGE (API de localidades: MG.json, PR.json, SC.json numa pasta), e grava em
<pacote>/_acervo/dados/:
  tj{uf}_comarcas.json   município -> comarca (mesmo formato de tjba_comarcas.json, mais "conferir")
  tj{uf}_unidades.json   comarca -> entrância, unidades e endereçamento do JEC e da Justiça Comum
                         (mesmo formato de tjba_unidades.json, mais "uf", "sede" e "nome_no_enderecamento")
  territorial-tj{uf}.md  regra, fontes, limites e índice por município

Uso: python -I territorial_ufs.py <pasta do IBGE> <pacote>   (sem <pacote>: só o relatório de cobertura)
O IBGE só confere a cobertura (todo município do estado tem comarca) e dá a grafia com acento.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CONSULTA = "2026-11-22"
NOME_UF = {"MG": "Minas Gerais", "PR": "Paraná", "SC": "Santa Catarina"}


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def chave(s):
    return re.sub(r"[^a-z]", "", sem_acento(s or "").lower())


def ibge(pasta, uf):
    return [m["nome"] for m in json.loads((Path(pasta) / f"{uf}.json").read_text(encoding="utf-8"))]


def lista_nomes(txt):
    """'A, B, C e D' -> [A, B, C, D]."""
    txt = re.sub(r"\s+", " ", txt).strip().rstrip(".")
    return [p.strip() for p in re.split(r"\s*,\s*|\s+e\s+(?:de\s+)?", txt) if p.strip()]


def _celulas(ln):
    return [c.strip() for c in ln.strip().strip("|").split("|")]


def municipio_comarca(comarcas, nomes_ibge, apelidos=None, resolvidos=None):
    """Cruza as listas de cada comarca com o IBGE. Município que é sede de comarca fica na própria comarca;
    nome em duas listas sem ser sede vira conflito. Devolve (mapa com a grafia do IBGE, faltantes, conflitos)."""
    apelidos, resolvidos = apelidos or {}, resolvidos or {}
    grafia = {chave(n): n for n in nomes_ibge}
    sede = {chave(c): c for c in comarcas}
    achados = {}
    for c, d in comarcas.items():
        for m in d["municipios"]:
            k = chave(apelidos.get(m, m))
            if k in grafia:
                achados.setdefault(k, set()).add(c)
    mapa, conflitos = {}, {}
    for k, cs in achados.items():
        if grafia[k] in resolvidos:
            mapa[grafia[k]] = resolvidos[grafia[k]]
        elif k in sede and sede[k] in cs:
            mapa[grafia[k]] = sede[k]
        elif len(cs) == 1:
            mapa[grafia[k]] = next(iter(cs))
        else:
            conflitos[grafia[k]] = sorted(cs)
    faltantes = sorted(n for n in nomes_ibge if n not in mapa and n not in conflitos)
    return mapa, faltantes, conflitos


# ------------------------------------------------------------------ PR

PR_FONTE = "tjpr/fonte-tjpr-foruns-juizados.md"
# entrância que a conversão do PDF separou do título (lida na fonte)
PR_ENTRANCIA = {"Nova Esperança": "Intermediária", "Congonhinhas": "Inicial", "São Mateus do Sul": "Intermediária",
                "União da Vitória": "Final", "Goioerê": "Intermediária", "Icaraíma": "Inicial"}
# grafia da fonte -> grafia do IBGE
PR_APELIDOS = {"Conselheiro Mayrinck": "Conselheiro Mairinck", "Diamante do Oeste": "Diamante D'Oeste",
               "Itaguagé": "Itaguajé", "Lunardeli": "Lunardelli", "Mirasselva": "Miraselva",
               "Moreira Salles": "Moreira Sales", "Munhoz de Mello": "Munhoz de Melo", "Pérola do Oeste": "Pérola d'Oeste",
               "4.º Centenário": "Quarto Centenário", "Rancho Alegre do Oeste": "Rancho Alegre D'Oeste",
               "Santa Cruz do Monte Castelo": "Santa Cruz de Monte Castelo", "Santa Teresa do Oeste": "Santa Tereza do Oeste",
               "Santa Terezinha do Itaipu": "Santa Terezinha de Itaipu", "São Jorge do Oeste": "São Jorge d'Oeste",
               "Mal. Cândido Rondon": "Marechal Cândido Rondon"}
# "Guairacá" (distrito de Guarapuava) e "Guairaçá" (município da comarca de Terra Rica) só diferem no acento
PR_RESOLVIDOS = {"Guairaçá": "Terra Rica"}
# o bloco de Guarapuava perdeu o título na conversão; os Juizados numerados (telefone 42) ficaram no bloco seguinte
PR_JUIZADOS_DE = {("Guaraniaçu", "1.º Juizado Especial Cível/Criminal e Fazenda Pública"): "Guarapuava",
                  ("Guaraniaçu", "2.º Juizado Especial Cível/Criminal e Fazenda Pública"): "Guarapuava"}


def _pr_fluxo(texto):
    """Achata as tabelas (as duas colunas repetem a mesma célula) num fluxo de linhas."""
    out = []
    for ln in texto.split("\n"):
        s = ln.strip()
        if not s or re.fullmatch(r"\|[-| ]+\|?", s):
            continue
        if s.startswith("|"):
            vistos = []
            for c in _celulas(s):
                if c and c not in vistos:
                    vistos.append(c)
            out.append("@@CURITIBA@@" if vistos == ["Curitiba"] else " | ".join(vistos))
        else:
            out.append(s.lstrip("# ").strip())
    return " \n ".join(out)


def pr():
    flux = _pr_fluxo((AQUI / PR_FONTE).read_text(encoding="utf-8"))
    # cada "Jurisdição:" abre uma comarca; o nome é o "Comarca de X"/"Foro Regional de X" logo antes,
    # ou, quando a conversão perdeu o título (Guarapuava), o primeiro município da lista
    tokens = re.finditer(r"(Comarca de|Foro Regional d[aeo]|Foro de)\s+([^|\n]+?)(?=\s+Jurisdi|\s*\||\s*\n)"
                         r"|Jurisdi[çc][ãa]o:\s*([^|\n]+)|(@@CURITIBA@@)|(\d{3,4}) - ([^|\n]*Juizado[^|\n]*)", flux)
    comarcas = {}
    titulo, atual = None, None
    for t in tokens:
        if t.group(1):
            titulo = (("Foro Regional" if t.group(1).startswith("Foro R") else "Comarca"), t.group(2).strip())
        elif t.group(3) is not None:
            lst = t.group(3)
            ent = re.search(r"Entr[âa]ncia\s+(Inicial|Intermedi[áa]ria|Final)", lst, re.I)
            lst = re.split(r"\s*Entr[âa]ncia", lst)[0]
            tipo, nome = titulo if titulo else ("Comarca", lista_nomes(lst)[0])
            nome = re.sub(r"\s+Entr[âa]ncia.*$", "", nome).strip()
            muns = [nome] + ([] if re.match(r"Compreend", lst) else lista_nomes(lst))
            atual = comarcas.setdefault(nome, {"tipo": tipo, "municipios": [], "entrancia": None, "juizados": []})
            atual["municipios"] += [m for m in muns if m not in atual["municipios"]]
            if ent:
                atual["entrancia"] = ent.group(1).capitalize().replace("Intermediaria", "Intermediária")
            titulo = None
        elif t.group(4):
            atual = comarcas.setdefault("Curitiba", {"tipo": "Foro Central", "municipios": ["Curitiba"],
                                                     "entrancia": "Final", "juizados": []})
        elif t.group(5) and atual is not None:
            j = re.sub(r"\s+", " ", t.group(6))
            j = re.sub(r"\s*-\s*(Endere[çc]o|Avenida|Rua|Pra[çc]a|\(\d\d\)).*$", "", j).strip(" -")
            if j.startswith("Bl "):
                continue
            dono = PR_JUIZADOS_DE.get((next(k for k, v in comarcas.items() if v is atual), j))
            (comarcas[dono] if dono else atual)["juizados"].append(j)
    ne = comarcas["Nova Esperança"]  # lista quebrada na conversão ("... Uniflor e" / "Presidente Castelo Branco")
    ne["municipios"] = [m for m in ne["municipios"] if m != "Uniflor e"] + ["Uniflor", "Presidente Castelo Branco"]
    for nome, ent in PR_ENTRANCIA.items():
        if nome in comarcas and not comarcas[nome]["entrancia"]:
            comarcas[nome]["entrancia"] = ent
    return comarcas


def pr_unidades(comarcas):
    out = {}
    for nome, d in comarcas.items():
        numerados = [j for j in d["juizados"] if re.match(r"\d", j)]
        conferir = []
        if d["tipo"] == "Foro Central":
            onde = "DO FORO CENTRAL DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA"
            conferir.append("Curitiba: a fonte lista o 1º Juizado Especial Cível (Matéria Bancária) e Juizados regionais "
                            "por bairro (Sítio Cercado, Santa Felicidade, CIC, Pinheirinho); confira a unidade pela matéria e pelo bairro do autor")
        elif d["tipo"] == "Foro Regional":
            onde = f"DO FORO REGIONAL DE {nome.upper()} DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA"
            conferir.append("foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba")
        else:
            onde = f"DA COMARCA DE {nome.upper()}"
        if numerados:
            jec_e = f"AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL {onde} - PR"
        else:
            jec_e = f"AO JUÍZO DO JUIZADO ESPECIAL CÍVEL {onde} - PR"
        if not d["juizados"]:
            conferir.append("a fonte não traz a unidade do Juizado desta comarca")
        vara = "AO JUÍZO DA VARA CÍVEL" if d["entrancia"] == "Inicial" else "AO JUÍZO DA [N]ª VARA CÍVEL"
        conferir.append("Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível")
        adj = next((j for j in d["juizados"] if "Adjunt" in j), None)
        out[nome] = {
            "grafia_2026": nome, "uf": "PR", "sede": nome, "entrancia": d["entrancia"],
            "jec": {"tipo": "juizado_especial", "unidades": d["juizados"], "enderecamento": jec_e},
            "comum": {"unidades": [], "enderecamento": f"{vara} {onde} - PR"},
            "juizado_adjunto": adj, "conferir": "; ".join(conferir) or None,
        }
    return out


# ------------------------------------------------------------------ SC

SC_FONTE = "tjsc/fonte-tjsc-composicao-comarcas.md"


def sc(nomes_ibge):
    """Tabela "Composição das Comarcas" do TJSC: Circ | Entr | Comarca | Municípios (nomes sem acento, separados
    por espaço ou por \\v). Os municípios se separam pela lista do IBGE (programação dinâmica sobre as letras)."""
    texto = (AQUI / SC_FONTE).read_text(encoding="utf-8")
    por_chave = {}
    for n in nomes_ibge:
        por_chave.setdefault(chave(n), n)
    comarcas, nao_lidos, foros, circ_atual = {}, [], {}, None
    for ln in texto.split("\n"):  # splitlines() quebraria no \v que a fonte usa entre municípios
        cel = [c.strip().replace("\\-", "-") for c in ln.strip().strip("|").split("|")]
        if len(cel) != 4 or cel[1] not in ("ESPECIAL", "FINAL", "INICIAL"):
            continue
        circ, ent, com, muns = cel
        circ_atual = circ or circ_atual
        sede_circ = "(SEDE)" in com
        com = re.sub(r"\s*\(SEDE\)", "", com).strip()
        if " - " in com:  # CAPITAL - FORO ..., JOINVILLE - FORO FAZENDARIO, BLUMENAU - FORO UNIVERSITARIO
            foros.setdefault(com.split(" - ")[0], []).append(com.split(" - ", 1)[1])
            if not com.startswith("CAPITAL"):
                continue
            com = "CAPITAL"
        letras = chave(re.sub(r"\(.*?\)", "", muns).replace("CHAPADAO DO LAJEADO", "CHAPADAO DO LAGEADO"))
        best = [None] * (len(letras) + 1)
        best[0] = []
        for i in range(len(letras)):
            if best[i] is None:
                continue
            for j in range(i + 1, len(letras) + 1):
                k = letras[i:j]
                if k in por_chave and (best[j] is None or len(best[j]) > len(best[i]) + 1):
                    best[j] = best[i] + [por_chave[k]]
        if best[-1] is None:
            nao_lidos.append((com, muns))
            continue
        nome = "Florianópolis" if com == "CAPITAL" else por_chave.get(chave(com), com.title())
        d = comarcas.setdefault(nome, {"tipo": "Comarca", "circunscricao": circ_atual, "sede_circunscricao": False,
                                       "entrancia": ent.capitalize(), "municipios": [], "juizados": []})
        d["municipios"] += [m for m in best[-1] if m not in d["municipios"]]
        d["sede_circunscricao"] |= sede_circ
    return comarcas, nao_lidos, foros


def sc_unidades(comarcas, foros):
    out = {}
    for nome, d in comarcas.items():
        capital = nome == "Florianópolis"
        onde = "DA COMARCA DA CAPITAL" if capital else f"DA COMARCA DE {nome.upper()}"
        conferir = ["a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado "
                    "(Juizado próprio ou adjunto à vara) e o nome e o número da vara cível"]
        if capital:
            conferir.insert(0, "Capital: foros " + ", ".join(f.title() for f in foros.get("CAPITAL", []))
                            + "; confira o foro pelo bairro do autor")
        for cidade, fs in foros.items():
            if chave(cidade) == chave(nome) and not capital:
                conferir.insert(0, f"a comarca tem também {', '.join(f.title() for f in fs)}")
        if d["entrancia"] == "Inicial":
            comum = f"AO JUÍZO DA VARA ÚNICA {onde} - SC"
        else:
            comum = f"AO JUÍZO DA [N]ª VARA CÍVEL {onde} - SC"
        out[nome] = {
            "grafia_2026": "Capital" if capital else nome, "uf": "SC", "sede": nome, "entrancia": d["entrancia"],
            "circunscricao": d["circunscricao"],
            "jec": {"tipo": "juizado_especial", "unidades": [], "enderecamento": f"AO JUÍZO DO JUIZADO ESPECIAL CÍVEL {onde} - SC"},
            "comum": {"unidades": [], "enderecamento": comum},
            "juizado_adjunto": None, "conferir": "; ".join(conferir),
        }
    return out


# ------------------------------------------------------------------ MG

MG_FONTE = "tjmg/fonte-tjmg-comarcas.md"
# grafia da fonte -> grafia do IBGE
MG_APELIDOS = {"Dona Eusébia": "Dona Euzébia", "Santa Rita do Ibitipoca": "Santa Rita de Ibitipoca",
               "Matias Lobato": "Mathias Lobato"}
# lista "Comendador Gomes, Fronteira, Frutal, Planura" na seção de Frutal (o nome se repete em outra seção)
MG_RESOLVIDOS = {"Fronteira": "Frutal"}


def mg(nomes_ibge):
    """Percorre a fonte em ordem. A seção de cada comarca abre com "## Nome NNNN" (NNNN = código TJMG da sede)
    ou, quando a conversão perdeu o título, com o cabeçalho do fórum ("... Cidade - MG CEP") ou com a linha
    da sede na tabela "Municípios e Distritos Integrantes" (código, nome e só a distância da capital).
    As demais linhas de município da tabela (código, nome, distância da comarca e da capital) entram na comarca."""
    linhas = (AQUI / MG_FONTE).read_text(encoding="utf-8").split("\n")
    ibge_k = {chave(n): n for n in nomes_ibge}
    ibge_k.update({chave(a): b for a, b in MG_APELIDOS.items()})
    comarcas = {}
    atual = None

    def abrir(nome, codigo, n):
        nonlocal atual
        nome = ibge_k.get(chave(nome), nome)  # "Grão Mogol" -> "Grão-Mogol", "São João del Rei" -> "São João del-Rei"
        atual = comarcas.setdefault(nome, {"tipo": "Comarca", "codigo": codigo, "linha": n, "municipios": [nome],
                                           "entrancia": None, "secao": [], "pela_secao": []})

    for n, ln in enumerate(linhas, 1):
        m = re.fullmatch(r"## (.+?) (\d{4})", ln.strip())
        if m:
            abrir(m.group(1).strip(), m.group(2), n)
            continue
        if " - MG" in ln:  # cabeçalho do fórum da comarca
            for antes in re.findall(r"([^|]*?) - MG", ln):
                pal = antes.split()
                for k in range(min(6, len(pal)), 0, -1):
                    nome = ibge_k.get(chave(" ".join(pal[-k:])))
                    if nome:
                        if nome not in comarcas:
                            abrir(nome, None, n)
                        break
        if atual is None:
            continue
        atual["secao"].append(ln)
        if not ln.startswith("|"):
            continue
        cel = _celulas(ln)
        for i in range(len(cel) - 1):
            a, b, resto = cel[i], cel[i + 1], cel[i + 2:]
            if re.fullmatch(r"\d{4}", a) and chave(b) in ibge_k:
                tok = re.findall(r"\b\d+\b", " ".join(resto))
                dist = [x for x in tok if len(x) < 4]
                distrito = any(len(x) == 4 for x in tok)
                nome = ibge_k[chave(b)]
                if len(dist) == 1 and not distrito and nome not in comarcas:
                    abrir(nome, a, n)  # sede sem título
                elif nome not in atual["municipios"]:
                    atual["municipios"].append(nome)
                break
    # segunda passada, só para o município que as tabelas não trouxeram: "Nome 0123" (lista fora de tabela),
    # linha só com o nome ou "Registro Civil/Notarial ... de Nome" na seção de uma única comarca
    achados = {m for c in comarcas.values() for m in c["municipios"]}
    for nome in nomes_ibge:
        if nome in achados:
            continue
        if nome in MG_RESOLVIDOS:
            comarcas[MG_RESOLVIDOS[nome]]["municipios"].append(nome)
            comarcas[MG_RESOLVIDOS[nome]]["pela_secao"].append(nome)
            continue
        e = "|".join(re.escape(a) for a in [nome] + [a for a, b in MG_APELIDOS.items() if b == nome])
        e = f"(?:{e})"
        pad = re.compile(rf"(?<![\w-]){e}\s+\d{{4}}\b|^\|?\s*{e}\s*(\|\s*)*$|(Registro Civil|Notarial)[^|\n]* de {e}\b", re.M)
        onde = [k for k, c in comarcas.items() if pad.search("\n".join(c["secao"]))]
        if len(onde) == 1:
            comarcas[onde[0]]["municipios"].append(nome)
            comarcas[onde[0]]["pela_secao"].append(nome)
    for c in comarcas.values():
        c["texto"] = "\n".join(c.pop("secao"))
        e = re.search(r"(Primeira|Segunda|Especial)\s+Entr[âa]ncia|Entr[âa]ncia:\s*(?:\|\s*)?\n*\s*(Primeira|Segunda|Especial)", c["texto"])
        c["entrancia"] = (e.group(1) or e.group(2)) if e else None
    return comarcas


def _mg_titulos(texto):
    return [t.strip() for t in re.findall(r"^## (.+)$", texto, re.M)]


def mg_unidades(comarcas):
    out = {}
    for nome, d in comarcas.items():
        txt = d["texto"]
        conferir = []
        onde = f"DA COMARCA DE {nome.upper()}"
        fim = r"(?=\s*(?:\||$|Gabinete|Secretaria|Sala|Tel))"
        varas = re.findall(r"Vara [ÚU]nica|\d+ª Vara C[íi]vel(?:,? [^|\n]*?)?" + fim
                           + r"|(?<![\dª] )Vara C[íi]vel(?:,? [^|\n]*?)?" + fim, txt, re.M)
        varas = list(dict.fromkeys(re.sub(r"\s+", " ", v).strip(" ,") for v in varas if "Administra" not in v))
        puras = [v for v in varas if re.fullmatch(r"\d+ª Vara C[íi]vel", v)]
        mistas = [v for v in varas if re.match(r"\d+ª Vara C[íi]vel[, ]", v)]
        if any(re.fullmatch(r"Vara [ÚU]nica", v) for v in varas):
            comum = f"AO JUÍZO DA VARA ÚNICA {onde} - MG"
        elif puras:
            comum = f"AO JUÍZO DA [N]ª VARA CÍVEL {onde} - MG"
        elif mistas:
            base = re.sub(r"^\d+ª\s+", "", mistas[0])
            comum = f"AO JUÍZO DA [N]ª {base.upper()} {onde} - MG"
            if len({re.sub(r"^\d+ª\s+", "", v) for v in mistas}) > 1:
                conferir.append("varas cíveis com competências diferentes: " + "; ".join(mistas))
        elif varas:
            comum = f"AO JUÍZO DA {varas[0].upper()} {onde} - MG"
        else:
            comum = f"AO JUÍZO DA VARA CÍVEL {onde} - MG"
            conferir.append("a fonte não traz vara cível desta comarca")
        numeradas = sorted(set(re.findall(r"(\d+)ª (?:Unidade Jurisdicional|Un\.\s?Jur\.)", txt)), key=int)
        if numeradas and len(numeradas) >= 2:
            jec = f"AO JUÍZO DA [N]ª UNIDADE JURISDICIONAL CÍVEL DO JUIZADO ESPECIAL {onde} - MG"
            tipo, unid = "juizado_especial", [f"{n}ª Unidade Jurisdicional" for n in numeradas]
            if nome == "Belo Horizonte":
                conferir.append("Belo Horizonte: confira a unidade jurisdicional cível (há unidades regionais, como a do Barreiro)")
        elif re.search(r"Unidade Jurisdicional [ÚU]nica|Un\.\s?Jur\.\s?[ÚU]nica", txt):
            jec = f"AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL {onde} - MG"
            tipo, unid = "juizado_especial", ["Unidade Jurisdicional Única do Juizado Especial"]
        elif re.search(r"Juizado Especial", txt):
            jec = f"AO JUÍZO DO JUIZADO ESPECIAL CÍVEL {onde} - MG"
            tipo, unid = "juizado_especial", ["Juizado Especial"]
            conferir.append("a fonte cita o Juizado Especial sem a unidade jurisdicional")
        else:
            jec = f"AO JUÍZO DO JUIZADO ESPECIAL CÍVEL {onde} - MG"
            tipo, unid = "juizado_nao_listado", []
            conferir.append("a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade")
        if d["pela_secao"]:
            conferir.append("municípios achados fora da tabela da comarca, conferir: " + ", ".join(d["pela_secao"]))
        out[nome] = {
            "grafia_2026": nome, "uf": "MG", "sede": nome, "entrancia": d["entrancia"], "codigo_tjmg": d["codigo"],
            "jec": {"tipo": tipo, "unidades": unid, "enderecamento": jec},
            "comum": {"unidades": varas, "enderecamento": comum},
            "juizado_adjunto": None, "conferir": "; ".join(conferir) or None,
        }
    return out


# ------------------------------------------------------------------ saída

FONTES = {
    "MG": ("TJMG: guia das comarcas (fórum, órgãos, \"Municípios e Distritos Integrantes\"), arquivo fornecido pelo escritório "
           "(_manutencao/coleta/tjmg/fonte-tjmg-comarcas.md)"),
    "PR": ("TJPR: \"Fóruns e Juizados Especiais (endereços e telefones)\", arquivo fornecido pelo escritório "
           "(_manutencao/coleta/tjpr/fonte-tjpr-foruns-juizados.md)"),
    "SC": ("TJSC: \"Composição das Comarcas\" (circunscrição, entrância, comarca, municípios), arquivo fornecido pelo escritório "
           "(_manutencao/coleta/tjsc/fonte-tjsc-composicao-comarcas.md)"),
}

LIMITES = {
    "MG": ["A fonte é um PDF convertido, com tabelas quebradas: a comarca de cada município saiu da tabela "
           "\"Municípios e Distritos Integrantes\" da seção da comarca; o que ficou fora da tabela está na coluna \"conferir\".",
           "Juizado: \"Unidade Jurisdicional Única\" ou unidades numeradas, como aparecem na seção da comarca. "
           "Onde a fonte não lista Juizado, a linha diz \"conferir\".",
           "Justiça Comum: a Vara Única ou as varas cíveis da seção da comarca."],
    "PR": ["A fonte traz só os Juizados (unidade, endereço e jurisdição). A vara cível da Justiça Comum não consta: "
           "o endereçamento da Justiça Comum é genérico e marcado \"conferir\".",
           "Região Metropolitana de Curitiba: Curitiba (Foro Central) e os foros regionais aparecem como unidades próprias, "
           "com o fecho na cidade do foro."],
    "SC": ["A fonte traz só a composição das comarcas (município → comarca e entrância). Nenhuma unidade (Juizado ou vara) "
           "consta: os endereçamentos seguem um padrão pela entrância e estão todos marcados \"conferir\".",
           "Florianópolis é a Comarca da Capital (foros Central, Continente, Norte da Ilha, Des. Eduardo Luz e outros); "
           "Joinville e Blumenau têm foros especiais listados na fonte."],
}


def gravar(uf, comarcas, unidades, mapa, faltantes, conflitos, pacote):
    dados = Path(pacote) / "_acervo" / "dados"
    sig = uf.lower()
    conferir_mun = {m: "consta das jurisdições de " + " e ".join(cs) + ": confira a comarca" for m, cs in conflitos.items()}
    for m, cs in conflitos.items():
        mapa[m] = cs[0]
    for m in faltantes:
        conferir_mun[m] = "município sem comarca na fonte: confira a comarca"
    mapa = dict(sorted(mapa.items(), key=lambda x: chave(x[0])))
    (dados / f"tj{sig}_comarcas.json").write_text(json.dumps({
        "fonte": FONTES[uf], "uf": uf, "consulta": CONSULTA,
        "municipio_comarca": mapa, "conferir": dict(sorted(conferir_mun.items())),
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (dados / f"tj{sig}_unidades.json").write_text(json.dumps({
        "fonte": FONTES[uf] + "; municípios conferidos com a lista do IBGE (API de localidades). Ver territorial-tj" + sig + ".md.",
        "consulta": CONSULTA, "aprovado_pelo_escritorio": "2026-11-22",
        "comarcas": dict(sorted(unidades.items(), key=lambda x: chave(x[0]))),
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    # documento
    L = [f"# Base territorial do TJ{uf} ({NOME_UF[uf]}) para o endereçamento (comarcas e unidades)", "",
         f"> Fonte: {FONTES[uf]}, recebido em 22/11/2026. Municípios conferidos com a lista do IBGE (API de localidades, "
         f"consulta em 22/11/2026). Gerado por `_manutencao/coleta/territorial_ufs.py`.",
         "> Só dados de unidade. Telefones e endereços dos fóruns ficam na fonte.", "",
         "## 1. Regra de endereçamento", "",
         f"1. **Ache a comarca** do município de residência do autor no índice da seção 4 (`grep -n \"Nome do município\"`). "
         "A comarca nem sempre é o próprio município.",
         f"2. O endereçamento pronto do JEC e da Justiça Comum está em `references/dados/tj{sig}_unidades.json` "
         "(`jec.enderecamento`, `comum.enderecamento`); `[N]` é o número da unidade, que sai na distribuição (`__`).",
         "3. A cidade do fecho é a sede da comarca (ou do foro), com a UF: `sede - " + uf + "`.",
         "4. Linha com \"conferir\" vira pendência da triagem: o advogado confirma a unidade antes de protocolar.",
         f"5. Réu Caixa: Justiça Federal ({'TRF6' if uf == 'MG' else 'TRF4'}), que **não tem tabela** neste pacote: "
         "a subseção é pendência a conferir.", "",
         "**Decisão do escritório (22/11/2026).** Aprovada a forma do endereçamento desta tabela; "
         "as linhas com \"conferir\" continuam pendência do caso concreto.", "",
         "## 2. Limites da fonte", ""]
    L += [f"- {x}" for x in LIMITES[uf]]
    if faltantes or conflitos:
        L += ["", "Municípios a conferir:", ""]
        L += [f"- {m}: {v}" for m, v in sorted(conferir_mun.items())]
    L += ["", f"## 3. Comarcas ({len(unidades)})", "",
          "| Comarca | Entrância | JEC | Justiça Comum | Conferir |", "|---|---|---|---|---|"]
    for nome, u in sorted(unidades.items(), key=lambda x: chave(x[0])):
        L.append(f"| {u['grafia_2026']} | {u['entrancia'] or '?'} | {u['jec']['enderecamento']} | "
                 f"{u['comum']['enderecamento']} | {u['conferir'] or ''} |")
    L += ["", f"## 4. Índice por município ({len(mapa)})", ""]
    L += [f"- {m} → {unidades[c]['grafia_2026']}" + (" (conferir)" if m in conferir_mun else "") for m, c in mapa.items()]
    (dados / f"territorial-tj{sig}.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    pasta = sys.argv[1]
    pacote = sys.argv[2] if len(sys.argv) > 2 else None
    res = {}
    c = pr()
    res["PR"] = (c, pr_unidades(c), *municipio_comarca(c, ibge(pasta, "PR"), PR_APELIDOS, PR_RESOLVIDOS))
    n = ibge(pasta, "SC")
    c, nao_lidos, foros = sc(n)
    assert not nao_lidos, nao_lidos
    res["SC"] = (c, sc_unidades(c, foros), *municipio_comarca(c, n))
    n = ibge(pasta, "MG")
    c = mg(n)
    res["MG"] = (c, mg_unidades(c), *municipio_comarca(c, n, MG_APELIDOS, MG_RESOLVIDOS))
    for uf, (c, u, mapa, falt, conf) in res.items():
        print(f"{uf}: {len(c)} comarcas, {len(mapa)} municípios; sem comarca {len(falt)} {falt}; em duas {conf}")
        if pacote:
            gravar(uf, c, u, mapa, falt, conf, pacote)


if __name__ == "__main__":
    main()
