#!/usr/bin/env python3
"""teste.py - regressão do caso fictício da skill migrado.

Gera o extrato fictício em PDF e calcula dois processos com scripts/calcular_migrado.py, conferindo os números esperados (conta feita à mão):
  1. três contratos migrados do banco 934 (dois excluídos, sob a IN 28; um ativo, sob a IN 138, que também aparece no banco anterior):
     sem a flag, os descontos do banco anterior NÃO são somados; com a flag, são;
  2. contrato cuja origem não é migração: o script alerta que a tese pode ser a do não contratado.
Também testa a origem da migração e a escolha da norma na fronteira de 13/12/2022. Sai com código 0 se tudo bate.

Uso:  python3 teste.py          (requer: pip install pypdf)
"""
import datetime as dt
import importlib.util
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


def calcula(tmp, pdf, processo, *extra):
    saida = Path(tmp) / f"p{processo}{'x' if extra else ''}"
    roda(RAIZ / "scripts/calcular_migrado.py", "--ficha", AQUI / "ficha.json", "--processo", processo, "--extrato", pdf,
         "--data", "2026-10-28", "--saida", saida, *extra)
    crono = json.loads((saida / "dossie-do-caso.json").read_text(encoding="utf-8"))["cronologia"]
    ev = {e["evento"] for e in crono}
    if [e["data"] for e in crono] != sorted(e["data"] for e in crono) or "Data da peça" not in ev \
            or "Início da vigência da IN PRES/INSS 138/2022" not in ev or not any(x.startswith("Averbação do contrato") for x in ev):
        CRONO_ERROS.append(f"processo {processo}{' ' + ' '.join(extra) if extra else ''}: linha do tempo incompleta ou fora de ordem")
    return json.loads((saida / "calculo.json").read_text(encoding="utf-8"))


CRONO_ERROS = []


def confere(erros, nome, obtido, esperado):
    for k, v in esperado.items():
        ok = abs(obtido[k] - v) < 0.005 if isinstance(v, float) else obtido[k] == v
        if not ok:
            erros.append(f"{nome}: {k} obtido {obtido[k]!r}, esperado {v!r}")


def main():
    erros = []
    spec = importlib.util.spec_from_file_location("calcmig", RAIZ / "scripts" / "calcular_migrado.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    for d, esp in ((dt.date(2022, 12, 12), "IN28"), (dt.date(2022, 12, 13), "IN138"), (dt.date(2021, 6, 16), "IN28")):
        if m.regime_da_data(d) != esp:
            erros.append(f"regime_da_data({d}) = {m.regime_da_data(d)}, esperado {esp}")
    for o, esp in (("Migrado do contrato 7001001 CBC: 934", ("7001001", "934")), ("Migrado do contrato 1519826531 CBC: 934", ("1519826531", "934")),
                   ("Averbação Banco", (None, None)), (None, (None, None))):
        if m.origem_da_migracao(o) != esp:
            erros.append(f"origem_da_migracao({o!r}) = {m.origem_da_migracao(o)}, esperado {esp}")

    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "extrato.pdf"
        roda(AQUI / "gerar_extrato_ficticio.py", pdf)
        c1, c1x, c2 = calcula(tmp, pdf, 1), calcula(tmp, pdf, 1, "--incluir-outros-bancos"), calcula(tmp, pdf, 2)
    a, b, c = c1["contratos"]
    confere(erros, "A (7001001)", a, {"qtde": 6, "total": 409.50, "dobro": 819.00, "migrado": True, "contrato_origem": "7001001", "banco_origem_cbc": "934",
                                      "regime_norma": "IN28", "status": "EXCLUÍDO", "troca_de_titularidade": False})
    confere(erros, "B (7001002)", b, {"qtde": 8, "total": 3861.12, "dobro": 7722.24, "migrado": True, "regime_norma": "IN28", "status": "EXCLUÍDO"})
    confere(erros, "C (7001003)", c, {"qtde": 20, "total": 1556.00, "dobro": 3112.00, "migrado": True, "regime_norma": "IN138", "status": "ATIVO",
                                      "troca_de_titularidade": True, "primeira_averbacao": "10/01/2024", "vincendas_qtde": 64,
                                      "vincendas_valor": 4979.20, "outros_bancos_somados": False})
    confere(erros, "p1", c1, {"total_descontado": 5826.62, "total_dobro": 11653.24, "valor_causa": 31653.24, "proveito_declaratorio": 4979.20,
                              "valor_causa_com_proveito": 36632.44, "tutela": True, "prescricao_5_anos": True, "todos_migrados": True,
                              "troca_de_titularidade": True})
    if len(c["outras_ocorrencias"]) != 1 or c["outras_ocorrencias"][0]["qtde"] != 11 or abs(c["outras_ocorrencias"][0]["total"] - 855.80) > 0.005:
        erros.append(f"C: ocorrência no banco anterior {c['outras_ocorrencias']}")
    if not any("TROCA DE TITULARIDADE" in x for x in c1["alertas"]) or any("TROCA DE TITULARIDADE" in x for x in c1x["alertas"]):
        erros.append("o alerta de troca de titularidade deve aparecer sem a flag e sumir com ela")
    cx = c1x["contratos"][2]
    confere(erros, "C com flag", cx, {"qtde": 31, "total": 2411.80, "dobro": 4823.60, "outros_bancos_somados": True})
    confere(erros, "p1 com flag", c1x, {"total_descontado": 6682.42, "total_dobro": 13364.84, "valor_causa": 33364.84})
    if "20.000,00 (vinte mil reais)" not in c1["dano_moral_extenso"]:
        erros.append("dano moral por extenso incorreto")

    d = c2["contratos"][0]
    confere(erros, "D (7002001)", d, {"migrado": False, "qtde": 19, "total": 1900.00, "regime_norma": "IN138"})
    if c2["todos_migrados"] or not any("e não migração" in x for x in c2["alertas"]):
        erros.append("p2: contrato sem origem de migração deve gerar alerta de rever a tese")
    f1 = {f["fsc"]: f["status"] for f in c1["checagem_fsc"]}
    v1 = {v["vf"]: v["status"] for v in c1["checagem_vf"]}
    f2 = {f["fsc"]: f["status"] for f in c2["checagem_fsc"]}
    if len(c1["checagem_fsc"]) != 12 or len(c1["checagem_vf"]) != 9:
        erros.append("checagem FSC/VF incompleta no calculo.json")
    if f1.get(5) != "OK" or v1.get(3) != "EXECUTADA" or f2.get(5) != "NAO_SE_APLICA":
        erros.append(f"FSC5/VF3 inesperados: {f1.get(5)}, {v1.get(3)}, {f2.get(5)}")
    erros += CRONO_ERROS
    if erros:
        sys.exit("TESTE FALHOU:\n- " + "\n- ".join(erros))
    print("TESTE OK: 3 contratos migrados (IN 28 e IN 138), troca de titularidade com e sem a flag, proveito declaratório R$ 4.979,20 e "
          "contrato sem origem de migração com alerta.")


if __name__ == "__main__":
    main()
