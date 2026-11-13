#!/usr/bin/env python3
"""teste.py - regressão do caso fictício da skill rmc.

Gera o extrato fictício em PDF, calcula com scripts/calcular_rmc.py e confere os números esperados (conta feita à mão).
Também confere que a variante "antigo" (refinanciamento em 11/2022) sai com o alerta B2, sem bloqueio, e gera as figuras
(scripts/diagramas_rmc.py): recortes do extrato, gráfico do acumulado e linha do tempo, com 17 cm a 300 dpi.
Sai com código 0 se tudo bate.

Uso:  python3 teste.py          (requer: pip install pypdf; para as figuras, pillow e pymupdf)
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


FIGURAS = {  # nome: (tipo, faixa de altura em px); largura sempre 2008 px (17 cm a 300 dpi)
    "fig_extrato_cartao.png": ("recorte", (500, 1200)),
    "fig_extrato_refinanciamento.png": ("recorte", (900, 2200)),
    "fig_acumulado.png": ("grafico", (1200, 2200)),
    "fig_linha_tempo.png": ("linha_tempo", (600, 1300)),
}


def figuras(tmp):
    """Gera as figuras do caso fictício (recortes do extrato, gráfico e linha do tempo) e confere tamanho e legendas."""
    try:
        from PIL import Image
    except ImportError:
        print("AVISO: Pillow ausente; figuras não testadas")
        return []
    erros = []
    fig = Path(tmp) / "fig"
    saida = roda(RAIZ / "scripts/diagramas_rmc.py", "--calculo", Path(tmp) / "atual" / "calculo.json",
                 "--extrato", Path(tmp) / "extrato-atual.pdf", "--saida", fig)
    if "PyMuPDF ausente" in saida:
        print("AVISO: PyMuPDF ausente; recortes do extrato não testados")
    j = json.loads((fig / "figuras.json").read_text(encoding="utf-8"))
    por_nome = {f["arquivo"]: f for f in j["figuras"]}
    for nome, (tipo, (hmin, hmax)) in FIGURAS.items():
        if tipo == "recorte" and "PyMuPDF ausente" in saida:
            continue
        f = fig / nome
        tam, dpi = (0, 0), 0
        if f.exists():
            with Image.open(f) as im:  # com 'with': no Windows o arquivo aberto trava a limpeza da pasta temporária
                tam, dpi = im.size, round(im.info.get("dpi", (0,))[0])
        if tam[0] != 2008 or dpi != 300 or not hmin < tam[1] < hmax:
            erros.append(f"figura {nome}: {tam[0]} x {tam[1]} px a {dpi} dpi (esperado 2008 px de largura, 300 dpi, "
                         f"altura entre {hmin} e {hmax})")
        x = por_nome.get(nome)
        if not x or x["tipo"] != tipo or not x["legenda"].startswith(f"Figura {x['numero']}: "):
            erros.append(f"figuras.json sem a figura {nome} ou com legenda fora do padrão")
    if j["avisos"] and "PyMuPDF ausente" not in saida:
        erros.append(f"figuras com aviso no caso fictício: {j['avisos']}")
    if [f["numero"] for f in j["figuras"]] != list(range(1, len(j["figuras"]) + 1)):
        erros.append("figuras.json com numeração fora de ordem")
    leg = " ".join(f["legenda"] for f in j["figuras"])
    if "11/2025" not in leg or "08/2025" not in leg:
        erros.append("legendas sem a competência do refinanciamento (11/2025) ou do marco (08/2025)")
    return erros


def main():
    erros = []
    with tempfile.TemporaryDirectory() as tmp:
        c = calcula(tmp, "atual")
        antigo = calcula(tmp, "antigo")
        erros += figuras(tmp)
    esperado = {  # conta feita à mão: 42 descontos de R$ 50,00 até 10/2025 (falta 06/2024) e 11 de R$ 55,00 desde 11/2025;
        # restituição desde 09/2025, mês seguinte ao marco (12/11/2026): 2 x R$ 50,00 + 11 x R$ 55,00 = R$ 705,00
        "capital": 1000.00, "dobro_capital": 2000.00, "total_ate_refin": 2100.00, "total_pos_refin": 605.00,
        "total_pos_marco": 705.00, "dobro": 1410.00, "total_pago": 2705.00, "saldo_atual": 1700.00, "custo_total": 4405.00,
        "valor_causa": 23210.00, "onerosidade_pct": 440.5, "pct_ate_refin": 210.0, "meses_teto": 3,
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
    if c.get("inicio_restituicao") != "09/2025":
        erros.append(f"início da restituição: obtido {c.get('inicio_restituicao')}, esperado 09/2025 (mês seguinte ao marco)")
    if "dez reais" not in c["dobro_extenso"] or "um mil, quatrocentos" not in c["dobro_extenso"]:
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
    print("TESTE OK: marco de 200% em 08/2025; refinanciamento em 11/2025; restituição desde 09/2025; dobro R$ 1.410,00; valor da causa "
          "R$ 23.210,00; competência ausente sinalizada; alerta B2 na variante antiga (sem bloqueio); 4 figuras com 17 cm a 300 dpi.")


if __name__ == "__main__":
    main()
