#!/usr/bin/env python3
"""teste_extenso.py - confere scripts/calcular.py contra valores por extenso reais do escritório.

Os pares de extenso-do-escritorio.json saíram de petições já geradas pelo AMN (sem dado pessoal).
Sai com código 0 se todos os extensos coincidem.

Uso:  python3 teste_extenso.py
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
AQUI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("calcular", AQUI.parent.parent / "scripts" / "calcular.py")
calcular = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calcular)

pares = json.loads((AQUI / "extenso-do-escritorio.json").read_text(encoding="utf-8"))["pares"]
erros = []
for p in pares:
    valor = float(p["valor"].replace(".", "").replace(",", "."))
    obtido = re.search(r"\((.*)\)", calcular.brl_ext(valor)).group(1)
    if obtido.lower() != p["extenso"].lower():
        erros.append(f'R$ {p["valor"]}: obtido "{obtido}", esperado "{p["extenso"]}"')
if erros:
    sys.exit("TESTE FALHOU:\n- " + "\n- ".join(erros))
print(f"TESTE OK: {len(pares)} valores por extenso conferem com as petições do escritório.")
