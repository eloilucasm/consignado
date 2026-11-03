#!/usr/bin/env python3
"""teste.py - regressão do caso fictício da skill tese-1000.

Gera o extrato fictício em PDF e calcula cinco processos com scripts/calcular_1000.py, conferindo os números esperados (conta feita
à mão):
  1. derivado excluído, reaverbado no mesmo dia, sob a IN 28;
  2. derivado ativo, reaverbado no mesmo dia, sob a IN 138, com tutela;
  3. dois derivados da mesma raiz, ativos (2 dias e 79 dias depois da exclusão), sob a IN 138;
  4. troca de titularidade: o mesmo derivado em outro banco; sem a flag, descontos do outro banco NÃO somados; com a flag, somados;
  5. derivado averbado ANTES da exclusão da raiz.
Também testa a escolha da norma na fronteira de 13/12/2022 e as categorias de intervalo. Sai com código 0 se tudo bate.

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
    roda(RAIZ / "scripts/calcular_1000.py", "--ficha", AQUI / "ficha.json", "--processo", processo, "--extrato", pdf,
         "--data", "2026-10-28", "--saida", saida, *extra)
    crono = json.loads((saida / "dossie-do-caso.json").read_text(encoding="utf-8"))["cronologia"]
    ev = [e["evento"] for e in crono]
    if [e["data"] for e in crono] != sorted(e["data"] for e in crono) or "Data da peça" not in ev \
            or not any(x.startswith("Exclusão do contrato-raiz") for x in ev):
        CRONO_ERROS.append(f"processo {processo}{' ' + ' '.join(extra) if extra else ''}: linha do tempo incompleta ou fora de ordem")
    reav = [e for e in crono if e["evento"].startswith("Reaverbação do derivado")]
    excl = [e for e in crono if e["evento"].startswith("Exclusão do contrato-raiz")]
    if reav and excl and "ANTES_DA_EXCLUSAO" not in reav[0]["efeito"] and reav[0]["data"] < excl[0]["data"]:
        CRONO_ERROS.append(f"processo {processo}: reaverbação antes da exclusão da raiz sem a categoria ANTES_DA_EXCLUSAO")
    return json.loads((saida / "calculo.json").read_text(encoding="utf-8"))


CRONO_ERROS = []


def confere(erros, nome, obtido, esperado):
    for k, v in esperado.items():
        ok = abs(obtido[k] - v) < 0.005 if isinstance(v, float) else obtido[k] == v
        if not ok:
            erros.append(f"{nome}: {k} obtido {obtido[k]!r}, esperado {v!r}")


def main():
    erros = []
    spec = importlib.util.spec_from_file_location("calc1000", RAIZ / "scripts" / "calcular_1000.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    # fronteira da IN 138 (13/12/2022) e categorias de intervalo
    for d, esp in ((dt.date(2022, 12, 12), "IN28"), (dt.date(2022, 12, 13), "IN138"), (dt.date(2018, 8, 11), "IN28"), (dt.date(2024, 1, 2), "IN138")):
        if m.regime_da_data(d) != esp:
            erros.append(f"regime_da_data({d}) = {m.regime_da_data(d)}, esperado {esp}")
    for n, esp in ((None, None), (-1, "ANTES_DA_EXCLUSAO"), (0, "MESMO_DIA"), (1, "ATE_30_DIAS"), (30, "ATE_30_DIAS"), (31, "MAIS_DE_30_DIAS")):
        if m.categoria_intervalo(n) != esp:
            erros.append(f"categoria_intervalo({n}) = {m.categoria_intervalo(n)}, esperado {esp}")
    if m.raiz_de("51-195502/15310_0001") != ("51-195502/15310", "_0001") or m.raiz_de("51-195502/15310") != (None, None):
        erros.append("raiz_de não separa o sufixo")

    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "extrato.pdf"
        roda(AQUI / "gerar_extrato_ficticio.py", pdf)
        c1, c2, c3, c4, c4x, c5 = (calcula(tmp, pdf, 1), calcula(tmp, pdf, 2), calcula(tmp, pdf, 3), calcula(tmp, pdf, 4),
                                   calcula(tmp, pdf, 4, "--incluir-outros-bancos"), calcula(tmp, pdf, 5))
    d1, d2 = c1["derivados"][0], c2["derivados"][0]
    confere(erros, "p1", d1, {"qtde": 11, "total": 371.25, "dobro": 742.50, "regime_norma": "IN28", "categoria_intervalo": "MESMO_DIA",
                              "intervalo_dias": 0, "raiz": "51-000111/00001", "sufixo": "_0001", "status": "EXCLUÍDO", "troca_de_titularidade": False})
    confere(erros, "p2", d2, {"qtde": 30, "total": 1500.00, "dobro": 3000.00, "regime_norma": "IN138", "categoria_intervalo": "MESMO_DIA",
                              "intervalo_dias": 0, "raiz": "51-000222/00002", "sufixo": "_0001", "status": "ATIVO"})
    for nome, c, vc, tutela, presc in (("p1", c1, 20742.50, False, True), ("p2", c2, 23000.00, True, False)):
        confere(erros, nome, c, {"valor_causa": vc, "tutela": tutela, "prescricao_5_anos": presc})
        if "20.000,00 (vinte mil reais)" not in c["dano_moral_extenso"]:
            erros.append(f"{nome}: dano moral por extenso incorreto")
    if d1["raiz_dados"]["exclusao"] != "11/08/2018" or d1["inclusao"] != "11/08/2018":
        erros.append(f"p1: datas da raiz e do derivado {d1['raiz_dados']} / {d1['inclusao']}")
    if "setecentos e quarenta e dois reais e cinquenta centavos" not in c1["total_dobro_extenso"]:
        erros.append(f"p1: dobro por extenso {c1['total_dobro_extenso']}")

    # p3: dois derivados da mesma raiz
    a, b = c3["derivados"]
    confere(erros, "p3 _0001", a, {"qtde": 41, "total": 1640.00, "categoria_intervalo": "ATE_30_DIAS", "intervalo_dias": 2, "regime_norma": "IN138"})
    confere(erros, "p3 _0002", b, {"qtde": 38, "total": 1140.00, "categoria_intervalo": "MAIS_DE_30_DIAS", "intervalo_dias": 79, "regime_norma": "IN138"})
    confere(erros, "p3", c3, {"total_descontado": 2780.00, "total_dobro": 5560.00, "valor_causa": 25560.00, "tutela": True})
    if len(c3["ativos"]) != 2 or any("mais de um contrato-raiz" in x.lower() for x in c3["alertas"]):
        erros.append("p3: dois derivados da MESMA raiz não deveriam gerar alerta de mais de uma raiz")

    # p4: troca de titularidade
    d4, d4x = c4["derivados"][0], c4x["derivados"][0]
    confere(erros, "p4", d4, {"qtde": 1, "total": 33.75, "dobro": 67.50, "troca_de_titularidade": True, "categoria_intervalo": "MESMO_DIA",
                              "regime_norma": "IN28", "primeira_averbacao": "11/08/2018", "outros_bancos_somados": False})
    confere(erros, "p4 com flag", d4x, {"qtde": 12, "total": 405.00, "dobro": 810.00, "outros_bancos_somados": True})
    confere(erros, "p4", c4, {"valor_causa": 20067.50, "troca_de_titularidade": True})
    confere(erros, "p4 com flag", c4x, {"valor_causa": 20810.00})
    if not any("TROCA DE TITULARIDADE" in x for x in c4["alertas"]) or any("TROCA DE TITULARIDADE" in x for x in c4x["alertas"]):
        erros.append("p4: o alerta de troca de titularidade deve aparecer sem a flag e sumir com ela")
    if len(d4["outras_ocorrencias"]) != 1 or d4["outras_ocorrencias"][0]["qtde"] != 11 or abs(d4["outras_ocorrencias"][0]["total"] - 371.25) > 0.005:
        erros.append(f"p4: ocorrência no outro banco {d4['outras_ocorrencias']}")
    if d4["raiz_dados"]["banco"].split(" - ")[0] != "739":
        erros.append(f"p4: a raiz deveria estar no banco 739, veio {d4['raiz_dados']}")

    # p5: derivado antes da exclusão da raiz
    d5 = c5["derivados"][0]
    confere(erros, "p5", d5, {"categoria_intervalo": "ANTES_DA_EXCLUSAO", "intervalo_dias": -5, "qtde": 2, "total": 40.00})
    if not any("ANTES da exclusão" in x for x in c5["alertas"]):
        erros.append("p5: faltou o alerta de derivado averbado antes da exclusão da raiz")

    fs1 = {f["fsc"]: f["status"] for f in c1["checagem_fsc"]}
    if len(c1["checagem_fsc"]) != 12 or len(c1["checagem_vf"]) != 9 or fs1.get(11) != "OK":
        erros.append(f"checagem FSC/VF inesperada no calculo.json: {fs1}")
    if any("ROTEAMENTO" in x and "tese-1000" in x for x in c1["alertas"]):
        erros.append("derivado com sufixo não deve rotear para a própria skill")
    # figuras (D28, item 14)
    try:
        from PIL import Image
        with tempfile.TemporaryDirectory() as tmp2:
            cj = Path(tmp2) / "calculo.json"
            cj.write_text(json.dumps(c1, ensure_ascii=False), encoding="utf-8")
            roda(RAIZ / "scripts/diagramas_1000.py", "--calculo", cj, "--saida", Path(tmp2) / "fig", "--fonte", "ID 12, p. 3")
            for nome, tam in (("fig_anatomia_1.png", (1400, 470)), ("fig_linha_tempo_1.png", (1400, 500))):
                f = Path(tmp2) / "fig" / nome
                if not f.exists() or Image.open(f).size != tam:
                    erros.append(f"figura {nome} ausente ou com tamanho errado")
    except ImportError:
        print("AVISO: Pillow ausente; figuras não testadas")
    erros += CRONO_ERROS
    if erros:
        sys.exit("TESTE FALHOU:\n- " + "\n- ".join(erros))
    print("TESTE OK: 5 processos (IN 28 e IN 138; mesmo dia, 2 e 79 dias, antes da exclusão; dois derivados da mesma raiz; troca de "
          "titularidade com e sem a flag) e a fronteira de 13/12/2022.")


if __name__ == "__main__":
    main()
