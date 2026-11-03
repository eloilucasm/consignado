#!/usr/bin/env python3
"""teste.py - regressão do caso fictício da skill rmc.

Gera o extrato fictício em PDF, calcula com scripts/calcular_rmc.py e confere os números esperados (conta feita à mão).
Também confere que a variante "antigo" (refinanciamento em 11/2022) sai com o alerta B2, sem bloqueio.
Sai com código 0 se tudo bate.

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


def roda(*args):
    r = subprocess.run([PY, *map(str, args)], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        sys.exit(f"FALHOU: {' '.join(map(str, args))}\n{r.stdout}\n{r.stderr}")
    return r.stdout


def calcula(tmp, variante):
    pdf = Path(tmp) / f"extrato-{variante}.pdf"
    saida = Path(tmp) / variante
    roda(AQUI / "gerar_extrato_ficticio.py", pdf, variante)
    roda(RAIZ / "scripts/calcular_rmc.py", "--ficha", AQUI / "ficha.json", "--processo", 1, "--extrato", pdf,
         "--data", "2026-10-28", "--saida", saida)
    c = json.loads((saida / "calculo.json").read_text(encoding="utf-8"))
    c["_dossie"] = json.loads((saida / "dossie-do-caso.json").read_text(encoding="utf-8"))
    return c


def main():
    erros = []
    with tempfile.TemporaryDirectory() as tmp:
        c = calcula(tmp, "atual")
        antigo = calcula(tmp, "antigo")
    esperado = {  # conta feita à mão: 42 descontos de R$ 50,00 até 10/2025 (falta 06/2024) e 11 de R$ 55,00 desde 11/2025
        "capital": 1000.00, "dobro_capital": 2000.00, "total_ate_refin": 2100.00, "total_pos_refin": 605.00,
        "dobro": 1210.00, "total_pago": 2705.00, "saldo_atual": 1700.00, "custo_total": 4405.00,
        "valor_causa": 23010.00, "onerosidade_pct": 440.5, "pct_ate_refin": 210.0, "meses_teto": 3,
    }
    for campo, esp in esperado.items():
        if abs(c[campo] - esp) > 0.005:
            erros.append(f"{campo}: obtido {c[campo]}, esperado {esp}")
    if c["marco"]["competencia"] != "08/2025" or abs(c["marco"]["acumulado"] - 2000.00) > 0.005:
        erros.append(f"marco de 200%: obtido {c['marco']}, esperado 08/2025 com R$ 2.000,00")
    if c["refinanciamento"]["competencia"] != "11/2025" or c["refinanciamento"]["utilizado"] != 1800.00:
        erros.append(f"refinanciamento: obtido {c['refinanciamento']}")
    if c["cartao"]["tipo"] != "RMC" or not c["ativo"] or not c["tutela"]:
        erros.append("cartão ativo deveria gerar tutela")
    if c["competencias_ausentes"] != ["06/2024"]:
        erros.append(f"competência ausente: obtido {c['competencias_ausentes']}, esperado ['06/2024']")
    if c["juros_cai"]:
        erros.append("a taxa de juros não cai no caso fictício; o argumento (c) não pode entrar")
    if c["bloqueios_juridicos"] or not c["pode_gerar"]:
        erros.append(f"refinanciamento de 11/2025 não deveria ter bloqueio: {c['bloqueios_juridicos']}")
    if "dez reais" not in c["dobro_extenso"] or "um mil, duzentos" not in c["dobro_extenso"]:
        erros.append(f"dobro por extenso incorreto: {c['dobro_extenso']}")
    if "20.000,00 (vinte mil reais)" not in c["dano_moral_extenso"]:
        erros.append("dano moral por extenso incorreto")
    if not any("boleto" in a for a in c["alertas"]):
        erros.append("faltou o alerta da premissa do boleto (D1)")
    if antigo["refinanciamento"]["competencia"] != "11/2022":
        erros.append(f"variante antigo: refinanciamento {antigo['refinanciamento']['competencia']}, esperado 11/2022")
    if not antigo["pode_gerar"] or antigo["bloqueios_juridicos"] or not any(a.startswith("B2") for a in antigo["alertas"]):
        erros.append("variante antigo deveria sair com o alerta B2, sem bloqueio (refinanciamento antes do prazo de 90 dias)")
    fr = {f["fsc"]: f["status"] for f in c["checagem_fsc"]}
    if len(c["checagem_fsc"]) != 12 or len(c["checagem_vf"]) != 9 or fr.get(4) != "PENDENTE_ADVOGADO":
        erros.append(f"checagem FSC/VF inesperada no calculo.json: {fr}")
    cr = {e["evento"].split(" (")[0]: e["data"] for e in c["_dossie"]["cronologia"]}
    if not (cr.get("Marco de 200% do capital atingido") == "2025-08-01" < cr.get("Refinanciamento do saldo do cartão", "") == "2025-11-01"):
        erros.append(f"linha do tempo: marco 08/2025 antes do refinanciamento 11/2025; obtido {cr}")
    if cr.get("Fim do prazo de 90 dias da Lei 14.690/2023") != "2024-01-01" or cr.get("Data da peça") != "2026-10-28":
        erros.append(f"linha do tempo sem o fim do prazo do teto (01/2024) ou sem a data da peça: {cr}")
    datas = [e["data"] for e in c["_dossie"]["cronologia"]]
    if datas != sorted(datas):
        erros.append("linha do tempo fora de ordem")
    if erros:
        sys.exit("TESTE FALHOU:\n- " + "\n- ".join(erros))
    print("TESTE OK: marco de 200% em 08/2025; refinanciamento em 11/2025; dobro R$ 1.210,00; valor da causa "
          "R$ 23.010,00; competência ausente sinalizada; alerta B2 na variante antiga (sem bloqueio).")


if __name__ == "__main__":
    main()
