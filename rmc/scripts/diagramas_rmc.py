#!/usr/bin/env python3
"""diagramas_rmc.py - figuras da inicial de RMC/RCC a partir do calculo.json e do extrato do INSS.

Grava até quatro imagens PNG e o figuras.json com a legenda de cada uma, para a peça:
  fig_extrato_cartao.png          recorte do extrato: linha do cartão na seção CARTÃO DE CRÉDITO (limite e averbação)
  fig_extrato_refinanciamento.png recorte do extrato: competências em volta do refinanciamento, na seção DESCONTOS DE
                                  CARTÃO, com contorno discreto na linha do refinanciamento
  fig_acumulado.png               evolução do acumulado pago x 200% do capital adotado, com o mês do marco e o do
                                  refinanciamento
  fig_linha_tempo.png             averbação do cartão, marco de 200%, refinanciamento e último desconto apurado

Recorte: a página do extrato é rasterizada (PyMuPDF) e o trecho é localizado pelas coordenadas do texto no PDF (número do
cartão, competência). Ele só reproduz o documento: nada é escrito por cima, só o contorno da linha que prova a tese. Extrato
sem camada de texto (digitalizado) ou layout não reconhecido: o recorte não sai e o figuras.json diz por quê (recorte manual).

Formato: padrão de figuras do pacote (assets/padrao-figuras.md; desenho em scripts/figuras.py): 17 cm a 300 dpi, fonte
mínima de 9 pt no que a figura escreve. O rodapé cita o extrato como anexo, sem ID: a figura é da inicial.

Uso:  python3 diagramas_rmc.py --calculo calculo.json --extrato extrato.pdf --saida pasta/figuras
Requer: Pillow; para os recortes, PyMuPDF (pip install pillow pymupdf).
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import figuras as fg  # noqa: E402

try:
    import pymupdf as fitz
except ImportError:
    try:
        import fitz
    except ImportError:
        fitz = None

FONTE = "Fonte: Histórico de Empréstimo Consignado do INSS, anexo."
FONTE_FIG = FONTE + " Figura elaborada a partir do extrato; não introduz fato novo. Capital adotado: limite do cartão."


def comp_n(c):
    m, a = c.split("/")
    return int(a) * 12 + int(m) - 1


def comp_s(n):
    return f"{n % 12 + 1:02d}/{n // 12}"


def data(s):
    for fmt in ("%d/%m/%Y", "%d/%m/%y"):
        try:
            return dt.datetime.strptime(s or "", fmt).date()
        except ValueError:
            pass
    return None


def comp_data(c):
    return dt.date(int(c[3:]), int(c[:2]), 1)


# ---------- leitura do PDF pelas coordenadas do texto ----------

def _linhas(pg):
    """Linhas de texto da página, de cima para baixo: {y0, y1, x0, x1, txt, palavras}."""
    grupos = {}
    for x0, y0, x1, y1, w, b, ln, _ in pg.get_text("words"):
        grupos.setdefault((b, ln), []).append((x0, y0, x1, y1, w))
    out = []
    for ws in grupos.values():
        out.append({"y0": min(w[1] for w in ws), "y1": max(w[3] for w in ws), "x0": min(w[0] for w in ws),
                    "x1": max(w[2] for w in ws), "txt": " ".join(w[4] for w in ws), "palavras": [w[4] for w in ws]})
    return sorted(out, key=lambda l: (l["y0"], l["x0"]))


def _regras(pg):
    """y das linhas horizontais da grade da tabela (se o PDF tiver)."""
    ys = set()
    for d in pg.get_drawings():
        for it in d.get("items", []):
            if it[0] == "l" and abs(it[1].y - it[2].y) < 0.5 and abs(it[2].x - it[1].x) > 50:
                ys.add(round(it[1].y, 1))
            elif it[0] == "re" and it[1].height < 1.5 and it[1].width > 50:
                ys.add(round(it[1].y0, 1))
    return sorted(ys)


def _faixa(linhas, regras, i):
    """Faixa vertical (y0, y1) do registro que contém a linha i: entre as linhas da grade, se houver; senão, a linha e
    as continuações logo abaixo ("(RMC)", "Cartão de crédito (RMC)")."""
    l = linhas[i]
    h = l["y1"] - l["y0"]
    yc = (l["y0"] + l["y1"]) / 2
    acima = [r for r in regras if r < yc]
    abaixo = [r for r in regras if r > yc]
    if acima and abaixo and abaixo[0] - acima[-1] < 6 * h:
        return acima[-1], abaixo[0]
    y0, y1 = l["y0"], l["y1"]
    for m in linhas[i + 1:]:
        if m["y0"] - y1 > 0.8 * h:
            break
        if m["txt"].startswith("(") or "(RMC)" in m["txt"] or "(RCC)" in m["txt"]:
            y1 = max(y1, m["y1"])
    return y0, y1


def _registro(linhas, regras, achar):
    """Primeira linha que satisfaz achar(linha, vizinhas) e a faixa do registro dela."""
    for i, l in enumerate(linhas):
        h = l["y1"] - l["y0"]
        viz = [m for m in linhas if m["y1"] >= l["y0"] - 1.5 * h and m["y0"] <= l["y1"] + 1.5 * h]
        if achar(l, viz):
            return i, _faixa(linhas, regras, i)
    return None


def _cabecalho_acima(linhas, y, chave, limite):
    """Topo do cabeçalho da tabela (linha com a chave) logo acima de y, se estiver a menos de 'limite' pt."""
    cands = [l for l in linhas if l["y1"] <= y and chave in l["txt"].upper()]
    if not cands:
        return None
    hdr = max(cands, key=lambda l: l["y0"])
    if y - hdr["y0"] > limite:
        return None
    topo = hdr["y0"]
    h = hdr["y1"] - hdr["y0"]
    for l in sorted(linhas, key=lambda l: -l["y0"]):  # título ou supercabeçalho colado acima (sem números)
        if l["y1"] <= topo and topo - l["y1"] < 0.8 * h and not any(ch.isdigit() for ch in l["txt"]):
            topo = l["y0"]
    return topo


def _meio(linhas, y, para_cima):
    """Ponto entre y e a linha de texto vizinha (para o contorno e a margem do recorte não cortarem texto)."""
    if para_cima:
        viz = [l["y1"] for l in linhas if l["y1"] <= y + 0.1]
        return (y + max(viz)) / 2 if viz and y - max(viz) < 8 else y - 3
    viz = [l["y0"] for l in linhas if l["y0"] >= y - 0.1]
    return (y + min(viz)) / 2 if viz and min(viz) - y < 8 else y + 3


def _rasterizar(pg, linhas, y0, y1, destaque):
    """Recorte da página entre y0 e y1, na largura da tabela, rasterizado para a largura útil da figura."""
    from PIL import Image, ImageDraw
    pad = 4  # pt de margem branca acima e abaixo do texto recortado
    top, bot = y0 - pad, y1 + pad
    xs = [(l["x0"], l["x1"]) for l in linhas if l["y1"] > y0 and l["y0"] < y1]
    x0 = max(pg.rect.x0, min(a for a, _ in xs) - 6)
    x1 = min(pg.rect.x1, max(b for _, b in xs) + 6)
    clip = fitz.Rect(x0, top, x1, bot)
    z = (fg.LARG - 2 * fg.M) / clip.width
    pix = pg.get_pixmap(matrix=fitz.Matrix(z, z), clip=clip, alpha=False)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    d = ImageDraw.Draw(img)  # o recorte termina no texto: pedaço de linha vizinha que invada a margem sai em branco
    d.rectangle([0, 0, img.width, round((y0 - 0.5 - top) * z)], fill="#FFFFFF")
    d.rectangle([0, round((y1 + 0.5 - top) * z), img.width, img.height], fill="#FFFFFF")
    dentro = [l for l in linhas if l["y0"] >= y0 - 0.1 and l["y1"] <= y1 + 0.1]
    for l in linhas:  # linha vizinha cuja caixa invade o recorte (ex.: vírgula que desce): apaga o que sobra dela
        if l in dentro or l["y1"] <= top or l["y0"] >= bot:
            continue
        sel = [s for s in dentro if s["y0"] < l["y1"] and s["y1"] > l["y0"]]
        xa = max([s["x1"] for s in sel if s["x0"] < l["x1"]] or [l["x0"] - 1]) + 1  # só à direita do texto que fica
        d.rectangle([round((max(xa, l["x0"] - 1) - x0) * z), round((max(l["y0"], top) - top) * z),
                     round((l["x1"] + 1 - x0) * z), round((min(l["y1"], bot) - top) * z)], fill="#FFFFFF")
    d0 = max(_meio(linhas, destaque[0], True), top + 1)
    d1 = min(_meio(linhas, destaque[1], False), bot - 1)
    caixa = (4, round((d0 - top) * z), img.width - 5, round((d1 - top) * z))
    return img, [caixa]


def recortes(extrato, c):
    """Acha no PDF a linha do cartão e o histórico em volta do refinanciamento. Devolve ({nome: (img, destaques, pág)}, aviso)."""
    if fitz is None:
        return {}, "PyMuPDF ausente (pip install pymupdf): recortes do extrato não gerados"
    doc = fitz.open(str(extrato))
    num = c["cartao"]["numero"]
    incl = c["cartao"]["inclusao"]  # dd/mm/aaaa; o extrato pode trazer dd/mm/aa
    incls = {incl, incl[:6] + incl[8:]}
    R, marco = c["refinanciamento"]["competencia"], c["marco"]["competencia"]
    rn, mn = comp_n(R), comp_n(marco)
    ini = mn - 1 if rn - mn <= 6 else rn - 3
    janela = [comp_s(n) for n in range(ini, rn + 3)]
    out, faltou = {}, []
    if not any(pg.get_text("words") for pg in doc):
        return {}, "extrato sem camada de texto (digitalizado): faça o recorte à mão"
    for k, pg in enumerate(doc):
        linhas, regras = _linhas(pg), _regras(pg)
        if "cartao" not in out:
            achou = _registro(linhas, regras, lambda l, viz: num in l["palavras"] and any(w in incls for v in viz for w in v["palavras"]))
            if achou:
                i, (y0, y1) = achou
                topo = _cabecalho_acima(linhas, y0, "CONTRATO", 6 * (y1 - y0)) or y0
                out["cartao"] = (*_rasterizar(pg, linhas, topo, y1, (y0, y1)), k + 1)
        if "refin" not in out:
            def da_janela(comp):
                return lambda l, viz: comp in l["palavras"] and any(w.startswith(num) for v in viz for w in v["palavras"])
            achou = _registro(linhas, regras, da_janela(R))
            if achou:
                _, faixa_r = achou
                faixas = [faixa_r] + [a[1] for a in (_registro(linhas, regras, da_janela(cp)) for cp in janela if cp != R) if a]
                y0, y1 = min(f[0] for f in faixas), max(f[1] for f in faixas)
                # cabeçalho só se estiver a até 3 registros da janela: não se emendam pedaços do documento
                topo = _cabecalho_acima(linhas, y0, "COMPET", 3.5 * (faixa_r[1] - faixa_r[0])) or y0
                out["refin"] = (*_rasterizar(pg, linhas, topo, y1, faixa_r), k + 1)
                out["janela"] = (comp_s(ini), comp_s(rn + 2))
    if "cartao" not in out:
        faltou.append(f"linha do cartão {num} na seção CARTÃO DE CRÉDITO")
    if "refin" not in out:
        faltou.append(f"competência {R} do cartão {num} na seção DESCONTOS DE CARTÃO")
    return out, ("não localizado no PDF: " + "; ".join(faltou) + " (recorte à mão)") if faltou else None


# ---------- figuras ----------

def fig_recorte(destino, titulo, sub, rec, frase):
    img, dest, pag = rec
    im, dr = fg.tela(img.height + 2000)
    y = fg.cabecalho(dr, titulo, sub) + fg.P(10)
    y = fg.documento(im, dr, y, img, dest) + fg.P(8)
    y = fg.frase(dr, y, frase) + fg.P(10)
    nota = f"{FONTE[:-1]}, página {pag}. Recorte do documento, sem alteração; só o contorno vermelho foi acrescentado."
    return fg.fechar(im, fg.rodape(dr, y, nota), destino)


def fig_acumulado(c, destino):
    im, dr = fg.tela()
    cap, R, marco = c["capital"], c["refinanciamento"]["competencia"], c["marco"]
    num, tipo = c["cartao"]["numero"], c["cartao"]["tipo"]
    plan = c["planilha"]
    y = fg.cabecalho(dr, "Acumulado pago e marco de 200%",
                     f"Cartão {tipo} nº {num}: soma dos descontos mensais de {c['primeira']} a {c['ultima']}, frente ao "
                     f"capital adotado de {fg.brl(cap)}") + fg.P(12)
    pontos = [(comp_n(p["competencia"]), p["acumulado"]) for p in plan]
    y = fg.grafico(dr, y, pontos, comp_s,
                   horizontais=[(2 * cap, "200%", fg.VERMELHO), (cap, "100%", fg.CINZA)],
                   verticais=[(comp_n(marco["competencia"]), fg.VERMELHO), (comp_n(R), fg.VERMELHO)],
                   destaque_desde=comp_n(R)) + fg.P(10)
    pos = [p for p in plan if comp_n(p["competencia"]) >= comp_n(R)]
    itens = [("linha", fg.AZUL, "Acumulado pago: soma dos descontos de cartão registrados no extrato"),
             ("tracejado", fg.VERMELHO, f"200% do capital adotado: {fg.brl(2 * cap)}"),
             (1, fg.VERMELHO, f"Marco de 200%: competência {marco['competencia']}, acumulado de {fg.brl(marco['acumulado'])}"),
             (2, fg.VERMELHO, f"Refinanciamento: competência {R}, utilizado no mês de "
                              f"{fg.brl(c['refinanciamento']['utilizado'])}, com IOF"),
             ("area", fg.VERMELHO, f"Descontado desde o refinanciamento: {fg.plural(len(pos), 'desconto', 'descontos')}, "
                                   f"{fg.brl(c['total_pos_refin'])}")]
    if c.get("competencias_ausentes"):
        aus = c["competencias_ausentes"]
        itens.append((None, fg.CINZA, f"{'Competência ausente' if len(aus) == 1 else 'Competências ausentes'} no extrato "
                                      f"({', '.join(aus)}): a linha é interrompida, sem interpolação"))
    y = fg.legenda(dr, y, itens) + fg.P(10)
    y = fg.frase(dr, y, f"Os descontos somaram 200% do capital em {marco['competencia']}, "
                        f"{fg.meses(c['meses_teto'])} antes do refinanciamento de {R}.") + fg.P(12)
    return fg.fechar(im, fg.rodape(dr, y, FONTE_FIG), destino)


def fig_linha_tempo(c, destino):
    im, dr = fg.tela()
    R, marco, num = c["refinanciamento"]["competencia"], c["marco"]["competencia"], c["cartao"]["numero"]
    plan = c["planilha"]
    entre = lambda a, b: [p for p in plan if a < comp_n(p["competencia"]) < b]  # noqa: E731
    desc = lambda n: fg.plural(n, "desconto", "descontos")  # noqa: E731
    y = fg.cabecalho(dr, "Linha do tempo do cartão", f"Sequência registrada no extrato do INSS para o cartão "
                                                     f"{c['cartao']['tipo']} nº {num}") + fg.P(14)
    incl = data(c["cartao"]["inclusao"])
    n12 = len([p for p in plan if comp_n(p["competencia"]) <= comp_n(marco)])
    n23 = len(entre(comp_n(marco), comp_n(R)))
    n34 = len([p for p in plan if comp_n(p["competencia"]) >= comp_n(R)])
    marcos = [("Averbação do cartão", c["cartao"]["inclusao"], fg.AZUL),
              ("Marco de 200%", f"competência {marco}", fg.VERMELHO),
              ("Refinanciamento", f"competência {R}", fg.VERMELHO),
              ("Último desconto apurado", f"competência {c['ultima']}", fg.AZUL)]
    trechos = [([fg.entre_datas(incl, comp_data(marco), competencia=True), f"{desc(n12)}, {fg.brl(c['marco']['acumulado'])}"], False),
               ([fg.meses(c["meses_teto"]), f"mais {desc(n23)}" if n23 else "sem desconto entre os dois"], False),
               ([fg.entre_datas(comp_data(R), comp_data(c["ultima"]), competencia=True), f"{desc(n34)}, {fg.brl(c['total_pos_refin'])}"], True)]
    if c["ultima"] == R:  # sem desconto depois do refinanciamento: o último marco coincide
        marcos, trechos = marcos[:3], trechos[:2]
    y = fg.linha_tempo(dr, y, marcos, trechos)
    y = fg.frase(dr, y + fg.P(10), f"Refinanciado {fg.meses(c['meses_teto'])} depois de os descontos atingirem 200% do capital.") + fg.P(12)
    return fg.fechar(im, fg.rodape(dr, y, FONTE_FIG), destino)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--calculo", required=True)
    ap.add_argument("--extrato", help="PDF do Histórico de Empréstimo Consignado (para os recortes)")
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    c = json.loads(Path(a.calculo).read_text(encoding="utf-8"))
    if not c.get("planilha"):
        sys.exit("calculo.json sem a planilha mês a mês: gere de novo com scripts/calcular_rmc.py")
    s = Path(a.saida)
    s.mkdir(parents=True, exist_ok=True)
    num, tipo, R = c["cartao"]["numero"], c["cartao"]["tipo"], c["refinanciamento"]["competencia"]
    rf = c["refinanciamento"]
    figs, avisos = [], []
    rec, aviso = recortes(a.extrato, c) if a.extrato else ({}, "extrato não informado (--extrato): recortes não gerados")
    if aviso:
        avisos.append(aviso)
    if "cartao" in rec:
        f = s / "fig_extrato_cartao.png"
        fig_recorte(f, "Extrato do INSS: o cartão", f"Seção Cartão de Crédito: cartão {tipo} nº {num}", rec["cartao"],
                    f"Cartão {tipo} nº {num}, com limite de {fg.brl(c['capital'])}, averbado em {c['cartao']['inclusao']}.")
        figs.append({"arquivo": f.name, "tipo": "recorte", "onde": "dos fatos: o extrato prova o refinanciamento",
                     "legenda": f"Recorte do Histórico de Empréstimo Consignado do INSS: linha do cartão {tipo} nº {num}."})
    if "refin" in rec:
        de, ate = rec["janela"]
        f = s / "fig_extrato_refinanciamento.png"
        igual = "igual" if rf.get("identico_ao_saldo") else "praticamente igual"
        fig_recorte(f, "Extrato do INSS: o refinanciamento",
                    f"Seção Descontos de Cartão: competências de {de} a {ate}, com a de {R} contornada", rec["refin"],
                    f"Em {R}, o utilizado no mês ({fg.brl(rf['utilizado'])}) é {igual} ao saldo devedor "
                    f"({fg.brl(rf['saldo'])}), com IOF de {fg.brl(rf['iof'] or 0)}.")
        figs.append({"arquivo": f.name, "tipo": "recorte", "onde": "dos fatos: o extrato prova o refinanciamento",
                     "legenda": f"Recorte do Histórico de Empréstimo Consignado do INSS: descontos do cartão nº {num} de "
                                f"{de} a {ate}, com a competência do refinanciamento ({R}) contornada."})
    f = s / "fig_acumulado.png"
    fig_acumulado(c, f)
    figs.append({"arquivo": f.name, "tipo": "grafico", "onde": "dos fatos: o custo real da dívida",
                 "legenda": f"Acumulado pago no cartão nº {num} e marco de 200% do capital adotado ({c['marco']['competencia']}), "
                            f"antes do refinanciamento ({R})."})
    f = s / "fig_linha_tempo.png"
    fig_linha_tempo(c, f)
    figs.append({"arquivo": f.name, "tipo": "linha_tempo", "onde": "dos fatos: o custo real da dívida",
                 "legenda": f"Linha do tempo do cartão nº {num}, conforme o extrato do INSS."})
    for n, x in enumerate(figs, 1):
        x["numero"] = n
        x["legenda"] = f"Figura {n}: {x['legenda']}"
    (s / "figuras.json").write_text(json.dumps({**fg.metadados(), "avisos": avisos, "figuras": figs}, ensure_ascii=False, indent=2),
                                    encoding="utf-8", newline="\n")
    if not fg.FR:
        print("AVISO: nenhuma fonte TrueType encontrada; usada a fonte padrão do Pillow (defina FONTES_DIAGRAMA).")
    for x in avisos:
        print("AVISO:", x)
    print(f"ok: {len(figs)} figura(s) em {s} ({fg.LARGURA_CM} cm a {fg.DPI} dpi; inserir na peça com {fg.LARGURA_CM} cm de largura)")


if __name__ == "__main__":
    main()
