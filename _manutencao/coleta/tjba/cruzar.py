"""Cruza município -> comarca (tjba_comarcas.json, relação TJBA de 15/03/2023) com as unidades judiciárias por comarca
(relações de magistrados e de unidades vagas de 09-10/2026) e com as Varas do Sistema dos Juizados (quadro de 17/04/2026
e portal dos Juizados). Só dados de unidade; nomes de pessoas são descartados."""
import json, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path

S = Path(sys.argv[1]); PAC = Path(sys.argv[2])
norm = lambda s: re.sub(r"[^A-Z ]", "", unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().upper()).strip()
norm = (lambda f: (lambda s: re.sub(r"\s+", " ", f(s))))(norm)

mc = json.loads((PAC / "_acervo/dados/tjba_comarcas.json").read_text(encoding="utf-8"))["municipio_comarca"]
comarcas_json = sorted(set(mc.values()))
nome_comarca = {}
for c in comarcas_json:
    for parte in c.split("/"):
        nome_comarca[norm(parte)] = parte.strip()
# grafias das relações de 2026 diferentes da tabela de 2023
nome_comarca["CAMACAN"] = "Camacã"; nome_comarca["SANTA TEREZINHA"] = "Santa Teresinha"; nome_comarca["SAO FELIX"] = "São Félix"

# ---------- unidades por comarca a partir das relações ----------
RUIDO = re.compile(r"^(ELEVA|RESOLU|CONVERS|DJE|ATIVA|DESATIVA|AGREGA|LEI |INSTAL|CRIADA|OPEREZ|P[ÁA]GINA|\d+\.?$|MAGISTRADO|COMARCA$|VARA$|UNIDADE$|JUIZ)", re.I)
unidades = defaultdict(set); entr = {}; desativ = {}
def ler_relacao(arq, entrancia):
    ls = [l.strip() for l in (S / arq).read_text(encoding="utf-8").splitlines()]
    atual, buf = None, []
    def fecha():
        if atual and buf:
            u = re.sub(r"\s+", " ", " ".join(buf)).strip(" .")
            if u and not re.search(r"[a-z]{3,} [a-z]{3,} [a-z]{3,}$", u) or u.isupper():
                unidades[atual].add(u.upper())
    for l in ls:
        n = norm(l.replace("Comarca de ", ""))
        if n in nome_comarca:
            fecha(); atual, buf = nome_comarca[n], []; entr.setdefault(atual, entrancia); continue
        m = re.search(r"(?:Agrupadora|AGRUPADA A|AGRUPADORA)\s+([A-ZÀ-Úa-zà-ú' ]+)", l)
        if m and atual is None:
            pass
        if not l or RUIDO.match(l) or atual is None:
            if re.match(r"^\d+\.$", l): fecha(); buf = []
            continue
        if re.match(r"^[A-ZÀ-Ú0-9ªº,.;\-–() ]+$", l) or re.match(r"^(Plena|Vara|\d+ª Vara)", l):
            buf.append(l)
    fecha()

def ler_registros(arq, entrancia):
    """Cada unidade ativa é um registro numerado ("12."): magistrado (ou VACÂNCIA TITULAR), comarca, vara.
    Comarca desativada não tem número e fica de fora."""
    ls = [l.strip() for l in (S / arq).read_text(encoding="utf-8").splitlines()]
    regs, atual = [], None
    for l in ls:
        m = re.match(r"^(\d+)\.\s*(.*)$", l)
        if m and not re.match(r"^\d+\.\d", l):
            if atual is not None: regs.append(atual)
            atual = [m.group(2)] if m.group(2) else []
        elif atual is not None:
            atual.append(l)
    if atual is not None: regs.append(atual)
    for r in regs:
        idx = next((i for i, l in enumerate(r) if norm(l.rstrip(".")) in nome_comarca), None)
        if idx is None:  # comarca colada ao fim da linha do magistrado ("… VACÂNCIA TITULAR IRARÁ")
            for i, l in enumerate(r[:3]):
                fim = [k for k in nome_comarca if norm(l).endswith(" " + k)]
                if fim:
                    idx, r = i, r[:i] + [max(fim, key=len)] + r[i + 1:]
                    break
        if idx is None: continue
        c = nome_comarca[norm(r[idx].rstrip("."))]
        partes = []
        for l in r[idx + 1:]:
            if re.match(r"^(PODER JUDICI|TRIBUNAL DE JUSTI|ASSESSORIA|RELA[ÇC][ÃA]O DE MAGISTRADOS|MAGISTRADO|COMARCA$|VARA$|OPerez|\d+$)", l): continue
            m2 = re.match(r"^(?:Eleva|Convers).*?\b(PLENA|CRIMINAL.*)$", l)
            if m2: partes.append(m2.group(1)); continue
            if re.match(r"^(Eleva|Convers|RESOLU|DJE|ATIVA|DESATIVA|AGREGA|Instala|Cria|Lei )", l, re.I) or not l: continue
            if re.match(r"^[A-ZÀ-Ú0-9ªº,.;\-–() ]+$", l): partes.append(l)
        u = re.sub(r"\s+", " ", " ".join(partes)).strip(" .")
        if u:
            unidades[c].add(u.upper()); entr.setdefault(c, entrancia)

ler_registros("rel-final-int.txt", "FINAL"); ler_registros("rel-intermediaria.txt", "INTERMEDIÁRIA"); ler_registros("rel-inicial.txt", "INICIAL")

# desativações (entrância inicial): "DESATIVAÇÃO ... – Agrupadora X" seguido do nome da comarca desativada
t = (S / "rel-inicial.txt").read_text(encoding="utf-8")
for m in re.finditer(r"(DESATIVA[ÇC][ÃA]O RESOLU[ÇC][ÃA]O N[ºo°]\s*(\d+/\d{4})\s*\n?\s*DJE\s*([\d/]+)\s*[–-]\s*(?:Agrupadora|AGRUPADORA|AGRUPADA A|Agrupada a)\s+([^\n]+?)\s*\n(?:[^\n]*\n){0,3}?\s*([A-ZÀ-Ú][A-ZÀ-Ú' ()]+?)\s*\n\s*\(?[A-ZÀ-Ú ]*\)?\s*PLENA)", t):
    desativ[m.group(5).strip()] = {"ato": f"Resolução nº {m.group(2)}", "dje": m.group(3), "agrupadora": m.group(4).strip().title()}

# ---------- Varas do Sistema dos Juizados ----------
vsj = defaultdict(list)
for u in json.loads((S / "unidades.json").read_text(encoding="utf-8")):
    if "Criminal" in u["unidade"]: continue
    vsj[nome_comarca.get(norm(u["comarca"]), u["comarca"].title())].append(u)

def civeis(c):
    us = sorted(unidades.get(c, []))
    return [u for u in us if re.search(r"PLENA|CONSUMO|C[ÍI]VE|SISTEMA DOS JUIZADOS", u)]

out = {"comarcas": {}, "desativadas": desativ, "sem_unidade_lida": []}
for c in comarcas_json:
    base = c.split("/")[0].strip()
    cv = civeis(base)
    out["comarcas"][c] = {"entrancia": entr.get(base), "vsj": [{k: u[k] for k in ("unidade", "entrancia", "email")} for u in vsj.get(base, [])],
                          "civeis": cv, "todas": sorted(unidades.get(base, []))}
    if not cv and base not in vsj: out["sem_unidade_lida"].append(c)
json.dump(out, open(S / "cruzamento.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("comarcas", len(comarcas_json), "| com VSJ", sum(1 for c in out["comarcas"].values() if c["vsj"]),
      "| sem unidade lida", len(out["sem_unidade_lida"]), out["sem_unidade_lida"][:40], "| desativadas lidas", len(desativ))
print("VSJ fora da tabela de comarcas:", [c for c in vsj if c not in [x.split('/')[0].strip() for x in comarcas_json]])
