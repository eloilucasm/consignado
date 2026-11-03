"""Extrai do quadro dos Juizados do TJBA (17/04/2026) só os dados da unidade (sem nomes de pessoas)."""
import json, re, sys
from pathlib import Path

linhas = [l.strip() for l in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines()]
unidades = []
for k, nome in enumerate(linhas):
    # a linha do nome é "COMARCA - Unidade"; a anterior é o rótulo ("Vara", "1ª Vara", "Única"...)
    if not re.match(r"^[^a-z]{3,}? - .*(Vara|Juizado|Turma)", nome) or k == 0:
        continue
    i = k - 1
    comarca, unidade = nome.split(" - ", 1)
    # campos antes de "Vara" (até o início da ficha, marcado por "Imóvel:")
    ini = max(j for j in range(i, -1, -1) if linhas[j] == "Imóvel:" or j == 0)
    antes = linhas[ini:i]
    depois = linhas[i + 2:i + 12]
    def depois_de(rot, bloco):
        return bloco[bloco.index(rot) + 1] if rot in bloco and bloco.index(rot) + 1 < len(bloco) else None
    end = depois_de("Endereço:", antes)
    cep = next((x.replace("CEP:", "").strip() for x in antes if x.startswith("CEP:")), None)
    email = next((x for x in depois if "@" in x), None)
    comp = None
    if "Competência:" in depois:
        k = depois.index("Competência:")
        comp = depois[k - 1] if k > 0 and depois[k - 1] not in ("E-mail's Juizado:",) and "@" not in depois[k - 1] else depois[k + 1]
    entr = depois_de("Entrância:", depois)
    unidades.append({"comarca": comarca.strip(), "unidade": unidade.strip(), "competencia": comp, "entrancia": entr,
                     "endereco": end, "cep": cep, "email": email, "funcionamento": depois_de("Funcionamento:", antes)})
json.dump(unidades, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(unidades), "unidades;", len({u["comarca"] for u in unidades}), "comarcas")
