#!/usr/bin/env python3
"""teste.py - regressão do caso fictício da skill replica-consignado.

Gera o extrato fictício, roda scripts/fichas.py com a contestação fictícia (contestacao.json) e confere o quadro de
indícios; roda também o geo_check.py e o ip_check.py (sem rede) para conferir que as cópias funcionam. Sai com código 0 se tudo bate.

Uso:  python3 teste.py          (requer: pip install pypdf)
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
PY = sys.executable


def roda(*args, ok=(0,)):
    r = subprocess.run([PY, *map(str, args)], capture_output=True, text=True, encoding="utf-8",
                       env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    if r.returncode not in ok:
        sys.exit(f"FALHOU: {' '.join(map(str, args))}\n{r.stdout}\n{r.stderr}")
    return r


def tem(ind, contrato, vf, gravidade, trecho):
    return any(x["contrato"] == contrato and x["vf"] == vf and x["gravidade"] == gravidade and trecho in x["achado"] for x in ind)


def main():
    erros = []
    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "extrato.pdf"
        roda(AQUI / "gerar_extrato_ficticio.py", pdf)
        roda(RAIZ / "scripts/fichas.py", "--extrato", pdf, "--contestacao", AQUI / "contestacao.json", "--saida", tmp)
        res = json.loads((Path(tmp) / "fichas.json").read_text(encoding="utf-8"))
        mapa = json.loads((Path(tmp) / "mapa-argumentos.json").read_text(encoding="utf-8"))
        md = (Path(tmp) / "fichas.md").read_text(encoding="utf-8")
        g = roda(RAIZ / "scripts/geo_check.py", AQUI / "geo-entrada.json", "--saida-md", Path(tmp) / "geo.md",
                 "--saida-json", Path(tmp) / "geo.json", ok=(0, 1, 2, 3))
        geo_ok = (Path(tmp) / "geo.json").exists()
        ip = subprocess.run([PY, str(RAIZ / "scripts/ip_check.py"), "10.0.0.5", "--sem-rdap"],
                            capture_output=True, text=True, encoding="utf-8", env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    ind = res["indicios"]
    checks = [
        ("00555111222", "VF2", "PROCESSUAL", "art. 341"),
        ("00123456789", "VF6", "ALERTA_CONTRA", "Súmula 42"),
        ("00123456789", "VF2", "RELEVANTE", "e-mail"),
        ("00123456789", "VF4", "CRÍTICO", "Cidade-UF"),
        ("00123456789", "VF5", "CRÍTICO", "sem contrato de correspondência"),
        ("00123456789", "VF5", "RELEVANTE", "SP"),
        ("00987654321", "VF6", "CRÍTICO", "diverge do valor liberado"),
        ("00987654321", "VF6", "RELEVANTE", "conta receptora"),
        ("00987654321", "VF2", "RELEVANTE", "manuscrita"),
        ("00123456789, 00987654321", "VF7", "CRÍTICO", "hash"),
        ("00123456789, 00987654321", "VF7", "REFORÇO", "IP"),
    ]
    for c in checks:
        if not tem(ind, *c):
            erros.append(f"faltou o indício {c}")
    if tem(ind, "00123456789", "VF2", "RELEVANTE", "telefone"):
        erros.append("telefone igual não pode gerar divergência")
    if not any("00999999999" in a and "substituição de objeto" in a for a in res["alertas"]):
        erros.append("faltou o alerta de substituição de objeto (contrato 00999999999)")
    if res["mesma_data"]:
        erros.append(f"o caso fictício não tem inclusões próximas: {res['mesma_data']}")
    if "Quadro de indícios" not in md or "## Contrato 00555111222" not in md:
        erros.append("fichas.md incompleto")
    ordem = [x["gravidade"] for x in ind]
    if ordem != sorted(ordem, key=["CRÍTICO", "RELEVANTE", "PROCESSUAL", "REFORÇO", "ALERTA_CONTRA"].index):
        erros.append("quadro de indícios fora da ordem de gravidade")
    por = {x["defesa"]: x for x in mapa}
    for d in ("P2", "M2", "M3", "M10", "M11", "M12", "NOVO"):
        if d not in por:
            erros.append(f"mapa de argumentos sem o ponto {d}")
    if any(not x["pedidos"] or not x["tese"] for x in mapa):
        erros.append("ponto do mapa sem pedido ou sem resposta")
    if por.get("P2", {}).get("pedidos") != ["preliminares"] or por.get("M10", {}).get("pedidos") != ["ma_fe"]:
        erros.append("pedido errado no mapa (P2 -> preliminares; M10 -> má-fé)")
    if "prova" not in por.get("M2", {}).get("pedidos", []) or not any("Cidade-UF" in p["achado"] for p in por.get("M2", {}).get("provas", [])):
        erros.append("M2 sem o pedido de valoração das lacunas (JEC) ou sem a prova do log (Cidade-UF vazio)")
    if not por.get("M3", {}).get("decisao_pendente") or not por.get("NOVO", {}).get("decisao_pendente"):
        erros.append("M3 (TED igual ao liberado) e defesa fora do catálogo deveriam pedir decisão do advogado")
    if por.get("M11", {}).get("contratos") != ["00555111222"] or por.get("M12", {}).get("contratos") != ["00999999999"]:
        erros.append("M11/M12 automáticos com contrato errado")
    if not geo_ok:
        erros.append(f"geo_check.py não gerou o quadro (código {g.returncode}): {g.stderr[-300:]}")
    if ip.returncode or "10.0.0.5" not in ip.stdout:
        erros.append(f"ip_check.py falhou (código {ip.returncode}): {ip.stdout[-200:]} {ip.stderr[-200:]}")
    if erros:
        sys.exit("TESTE FALHOU:\n- " + "\n- ".join(erros))
    print(f"TESTE OK: {len(ind)} indícios (art. 341, Súmula 42, TED divergente, hash repetido, correspondente, Cidade-UF vazio), "
          "substituição de objeto, geo_check e ip_check funcionando.")


if __name__ == "__main__":
    main()
