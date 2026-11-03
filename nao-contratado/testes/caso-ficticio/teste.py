#!/usr/bin/env python3
"""teste.py - regressão do caso fictício da skill nao-contratado.

Gera o extrato fictício em PDF, lê com scripts/extrato.py, calcula com scripts/calcular.py e confere os
números esperados (conta feita à mão). Sai com código 0 se tudo bate.

Uso:  python3 teste.py          (requer: pip install pypdf)
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
PY = sys.executable

ESPERADO = {  # contrato: (qtde, total, dobro, status)
    "00123456789": (33, 4702.50, 9405.00, "EXCLUÍDO"),
    "00987654321": (22, 2162.60, 4325.20, "EXCLUÍDO"),
    "00555111222": (25, 3000.00, 6000.00, "ATIVO"),
}


def roda(*args):
    r = subprocess.run([PY, *map(str, args)], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        sys.exit(f"FALHOU: {' '.join(map(str, args))}\n{r.stdout}\n{r.stderr}")
    return r.stdout


def main():
    erros = []
    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "extrato.pdf"
        roda(AQUI / "gerar_extrato_ficticio.py", pdf)
        linhas = [json.loads(l) for l in roda(RAIZ / "scripts/extrato.py", pdf).splitlines() if l.strip()]
        if len(linhas) != 3:
            erros.append(f"extrato.py leu {len(linhas)} contratos, esperado 3")
        roda(RAIZ / "scripts/calcular.py", "--ficha", AQUI / "ficha.json", "--processo", 1, "--extrato", pdf,
             "--data", "2026-10-28", "--saida", tmp)
        calc = json.loads((Path(tmp) / "calculo.json").read_text(encoding="utf-8"))
        crono = json.loads((Path(tmp) / "dossie-do-caso.json").read_text(encoding="utf-8"))["cronologia"]
    ev = {e["evento"]: e for e in crono}
    if [e["data"] for e in crono] != sorted(e["data"] for e in crono):
        erros.append("linha do tempo fora de ordem")
    lim = ev.get("Limite de 5 anos antes da peça")
    if not lim or lim["data"] != "2021-10-01" or ev.get("Data da peça", {}).get("data") != "2026-10-28":
        erros.append("linha do tempo sem o limite de 5 anos (10/2021) ou sem a data da peça")
    if sum(x.startswith("Averbação do contrato") for x in ev) != 3:
        erros.append("linha do tempo deveria ter a averbação dos 3 contratos")
    for l in calc["contratos"]:
        esp = ESPERADO.get(l["contrato"])
        if not esp:
            erros.append(f"contrato inesperado {l['contrato']}")
            continue
        got = (l["qtde"], l["total"], l["dobro"], l["status"])
        if got != esp:
            erros.append(f"{l['contrato']}: obtido {got}, esperado {esp}")
    for campo, esp in (("total_descontado", 9865.10), ("total_dobro", 19730.20), ("valor_causa", 39730.20)):
        if abs(calc[campo] - esp) > 0.005:
            erros.append(f"{campo}: obtido {calc[campo]}, esperado {esp}")
    if calc["ativos"] != ["00555111222"] or not calc["tutela"]:
        erros.append("tutela deveria recair só sobre o contrato ativo 00555111222")
    if not calc["prescricao_5_anos"]:
        erros.append("tópico de prescrição deveria estar ativo (desconto desde 03/2019)")
    if not any("ANOMALIA" in a for a in calc["alertas"]):
        erros.append("faltou o alerta de ANOMALIA (bloco B ativo)")
    if "20.000,00 (vinte mil reais)" not in calc["dano_moral_extenso"]:
        erros.append("dano moral por extenso incorreto")
    fsc = {f["fsc"]: f["status"] for f in calc["checagem_fsc"]}
    if len(calc["checagem_fsc"]) != 12 or len(calc["checagem_vf"]) != 9:
        erros.append("checagem FSC/VF incompleta no calculo.json")
    if fsc.get(4) != "ATIVADO" or fsc.get(6) != "ATIVADO" or fsc.get(5) != "NAO_SE_APLICA":
        erros.append(f"FSC4/FSC6/FSC5 inesperados: {fsc}")
    if any("ROTEAMENTO" in a for a in calc["alertas"]):
        erros.append("o caso fictício não deveria ter alerta de roteamento")
    if erros:
        sys.exit("TESTE FALHOU:\n- " + "\n- ".join(erros))
    print("TESTE OK: 3 contratos lidos; 33, 22 e 25 parcelas; dobro R$ 19.730,20; valor da causa R$ 39.730,20; "
          "tutela só sobre o ativo; prescrição e anomalia sinalizadas.")


if __name__ == "__main__":
    main()
