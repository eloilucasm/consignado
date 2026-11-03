#!/usr/bin/env python3
"""
geo_figuras.py - VF9: figuras ilustrativas de geolocalização para a peça.

Gera, a partir do MESMO JSON de entrada do geo_check.py, o conjunto de TRÊS imagens obrigatórias, nesta ordem:
  A  visão geral dos dois pontos (1 = local registrado no log, 2 = residência do autor), com a linha, a distância,
     a escala e os limites municipais da Bahia (malha do IBGE), 100% offline;
  B  captura de mapa de ruas do local registrado no log;
  C  captura de mapa de ruas da residência do autor, com os círculos de 100 m e 150 m.
As capturas B e C vêm do arquivo regiao.pmtiles (geo_mapa_pmtiles.py), sem rede. A visão geral (A) vem sempre da
malha do IBGE (geo_malha.py + assets/ba_municipios.json).

Arquivos gerados por evento (em --saida-dir):
  fig_evento<N>_A_visao_geral.png, _B_log.png, _C_residencia.png   as três imagens, em ordem (uso na peça);
                                   figuras.json traz, em `paineis`, a ordem e a legenda de cada uma
  fig_evento<N>_comparativo.png   painel esquemático único (só para conferência; vai à peça apenas no modo esquema,
                                   autorizado pelo usuário)
  fig_evento<N>_visao_geral.png   a visão geral em malha do IBGE (base da imagem A)
  figuras.json                    legendas, fontes, avisos e `completa` de cada figura
  links_coordenadas.md            nota de rodapé com os links das coordenadas

Modos (--fundo):
  auto (padrão)  EXIGE o regiao.pmtiles. Sem ele, PARA (código 5), não gera figura e manda perguntar ao usuário.
                 Com ele, entrega as três imagens para cada evento cujos dois pontos caem na área do arquivo; o
                 evento fora da área sai só com a visão geral e o aviso "FIGURA INCOMPLETA".
  esquema        só a visão geral esquemática, por autorização expressa do usuário.

Por padrão gera figura para os eventos com resultado DIVERGENTE na distância ao domicílio, de qualquer fonte (GPS,
REDE, IP ou não identificada); a fonte vai na legenda e nos avisos (Regras 16 e 19). Use --eventos para escolher outros.

Uso:
    python3 geo_figuras.py entrada.json --saida-dir figuras/
    python3 geo_figuras.py entrada.json --saida-dir figuras/ --eventos 2,3
    python3 geo_figuras.py entrada.json --saida-dir figuras/ --fundo esquema     (só com autorização do usuário)

Dependência: Pillow.
"""

import argparse
import json
import math
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # pragma: no cover
    print("Erro: este script precisa do Pillow (pip install pillow --break-system-packages).",
          file=sys.stderr)
    sys.exit(2)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geo_check as gc  # noqa: E402
import geo_malha as gm  # noqa: E402
import geo_dados_figura as gh  # noqa: E402

TILE = 256

VERMELHO = (200, 30, 30)
AZUL = (25, 80, 170)
VERDE = (20, 130, 60)
CINZA = (90, 90, 90)
BRANCO = (255, 255, 255)
NAVY = (35, 39, 95)


# ------------------------------------------------------------- projeção

def mundo_px(lat, lon, z):
    """Coordenada em pixels do mapa mundial (Web Mercator, tiles de 256 px)."""
    n = TILE * (2 ** z)
    x = (lon + 180.0) / 360.0 * n
    lat = max(min(lat, 85.0511), -85.0511)
    s = math.sin(math.radians(lat))
    y = (0.5 - math.log((1 + s) / (1 - s)) / (4 * math.pi)) * n
    return x, y


def lonlat_de_px(x, y, z):
    n = TILE * (2 ** z)
    lon = x / n * 360.0 - 180.0
    lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n))))
    return lon, lat


def metros_por_pixel(lat, z):
    return 156543.03392 * math.cos(math.radians(lat)) / (2 ** z)


# ------------------------------------------------------------- fontes

ESCALA_FONTE = 1.3  # a imagem é reduzida a 17 cm na peça; letras maiores mantêm a leitura


def fonte(tam, negrito=False):
    tam = int(round(tam * ESCALA_FONTE))
    try:
        import matplotlib
        nome = "DejaVuSans-Bold.ttf" if negrito else "DejaVuSans.ttf"
        caminho = os.path.join(matplotlib.get_data_path(), "fonts", "ttf", nome)
        return ImageFont.truetype(caminho, tam)
    except Exception:
        pass
    for nome in ("DejaVuSans-Bold.ttf" if negrito else "DejaVuSans.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if negrito
                 else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(nome, tam)
        except Exception:
            continue
    try:
        return ImageFont.load_default(size=tam)
    except TypeError:  # Pillow antigo
        return ImageFont.load_default()


# ------------------------------------------------------------- desenho

def passo_bonito(alvo_m):
    for v in (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000,
              50000, 100000, 200000, 500000, 1000000):
        if v >= alvo_m:
            return v
    return 1000000


def rotulo_dist(m):
    return f"{m:.0f} m" if m < 1000 else f"{m/1000:.1f} km".replace(".", ",")


def circulo(draw, c, raio_px, cor, largura=3, tracejado=False):
    x, y = c
    caixa = [x - raio_px, y - raio_px, x + raio_px, y + raio_px]
    if not tracejado:
        draw.ellipse(caixa, outline=cor, width=largura)
        return
    ang = 0
    while ang < 360:
        draw.arc(caixa, ang, ang + 8, fill=cor, width=largura)
        ang += 16


def ajusta(draw, txt, f, largura):
    """Corta o texto com reticências para caber na largura."""
    if draw.textlength(txt, font=f) <= largura:
        return txt
    while len(txt) > 1 and draw.textlength(txt + "…", font=f) > largura:
        txt = txt[:-1]
    return txt.rstrip() + "…"


def limpa(s):
    """Tira parênteses da fonte para a legenda não ficar com parênteses aninhados."""
    return s.replace(" (", ", ").replace("(", "").replace(")", "")


def texto_caixa(draw, xy, txt, f, cor=(20, 20, 20), fundo=(255, 255, 255, 215), pad=4):
    x0, y0, x1, y1 = draw.textbbox(xy, txt, font=f)
    draw.rectangle([x0 - pad, y0 - pad, x1 + pad, y1 + pad], fill=fundo)
    draw.text(xy, txt, font=f, fill=cor)
    return x1 + pad, y1 + pad


def marcador(draw, c, cor, numero):
    x, y = c
    draw.ellipse([x - 19, y - 19, x + 19, y + 19], fill=BRANCO)
    draw.ellipse([x - 16, y - 16, x + 16, y + 16], fill=cor)
    f = fonte(14, True)
    w = draw.textlength(str(numero), font=f)
    draw.text((x - w / 2, y - 12), str(numero), font=f, fill=BRANCO)


def painel(centro, z, w, h, titulo, subtitulo, marcas, circulos, rodape=None, malha=None):
    """Desenha um painel de mapa.
    marcas: lista de (lat, lon, cor, numero). circulos: lista de dicts
    {lat, lon, raio_m, cor, tracejado, preencher}. Painel esquemático: grade métrica, sem mapa de fundo
    (o mapa de ruas vem do regiao.pmtiles, em geo_mapa_pmtiles.py). Retorna (imagem, pontos)."""
    cx, cy = mundo_px(centro[0], centro[1], z)
    left, top = cx - w / 2, cy - h / 2
    img = Image.new("RGB", (w, h), (236, 236, 232))
    mpp = metros_por_pixel(centro[0], z)

    if True:  # grade métrica
        d0 = ImageDraw.Draw(img)
        passo = passo_bonito(60 * mpp)
        passo_px = passo / mpp
        k = 0
        while k * passo_px < max(w, h) * 2:
            for sinal in (1, -1):
                off = sinal * k * passo_px
                d0.line([(w / 2 + off, 0), (w / 2 + off, h)], fill=(208, 208, 204), width=1)
                d0.line([(0, h / 2 + off), (w, h / 2 + off)], fill=(208, 208, 204), width=1)
            k += 1
        d0.text((8, 118), f"grade: {rotulo_dist(passo)}", font=fonte(12), fill=CINZA)

    def pt(lat, lon):
        x, y = mundo_px(lat, lon, z)
        return x - left, y - top

    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    if malha and gm.disponivel():
        lon0, lat1 = lonlat_de_px(left, top, z)
        lon1, lat0 = lonlat_de_px(left + w, top + h, z)
        gm.desenha_malha(d, pt, (lon0, lat0, lon1, lat1), destaque=malha.get("destaque", ()))
        fm = fonte(12, True)
        for lat, lon, nome in malha.get("rotulos", []):
            px = pt(lat, lon)
            texto_caixa(d, (px[0] + 16, px[1] + 16), nome, fm, cor=NAVY, fundo=(255, 255, 255, 230))
        fx = fonte(11)
        fonte_txt = "Limites municipais: " + gm.carrega()["fonte"]
        tw0 = d.textlength(fonte_txt, font=fx)
        d.rectangle([w - tw0 - 14, h - 54, w - 2, h - 30], fill=(255, 255, 255, 215))
        d.text((w - tw0 - 8, h - 51), fonte_txt, font=fx, fill=(40, 40, 40, 255))
    for c in circulos:
        px = pt(c["lat"], c["lon"])
        r = c["raio_m"] / mpp
        if c.get("preencher"):
            d.ellipse([px[0] - r, px[1] - r, px[0] + r, px[1] + r],
                      fill=c["cor"] + (45,))
        circulo(d, px, r, c["cor"] + (255,), largura=3, tracejado=c.get("tracejado", False))
    pontos = []
    for lat, lon, cor, num in marcas:
        px = pt(lat, lon)
        pontos.append(px)
        marcador(d, px, cor, num)

    # barra de escala
    bonitos = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000,
               50000, 100000, 200000, 500000, 1000000]
    L = bonitos[0]
    for v in bonitos:
        if v / mpp <= 190:
            L = v
    barra = L / mpp
    bx, by = 14, h - 34
    d.rectangle([bx - 6, by - 28, bx + barra + 6, by + 12], fill=(255, 255, 255, 215))
    d.line([(bx, by), (bx + barra, by)], fill=(20, 20, 20, 255), width=3)
    d.line([(bx, by - 6), (bx, by + 4)], fill=(20, 20, 20, 255), width=3)
    d.line([(bx + barra, by - 6), (bx + barra, by + 4)], fill=(20, 20, 20, 255), width=3)
    d.text((bx, by - 26), rotulo_dist(L), font=fonte(13, True), fill=(20, 20, 20, 255))

    # nota de rodapé da imagem esquemática
    fa = fonte(11)
    nota = "Figura esquemática, sem mapa de fundo"
    tw = d.textlength(nota, font=fa)
    d.rectangle([w - tw - 14, h - 28, w - 2, h - 2], fill=(255, 255, 255, 215))
    d.text((w - tw - 8, h - 26), nota, font=fa, fill=(40, 40, 40, 255))

    # faixa de título
    d.rectangle([0, 0, w, 36 + (30 if subtitulo else 0)], fill=NAVY + (235,))
    d.text((8, 6), ajusta(d, titulo, fonte(15, True), w - 16), font=fonte(15, True), fill=(255, 255, 255, 255))
    if subtitulo:
        d.text((8, 38), ajusta(d, subtitulo, fonte(12), w - 16), font=fonte(12), fill=(225, 228, 245, 255))
    if rodape:
        fr = fonte(12)
        tw = d.textlength(rodape, font=fr)
        d.rectangle([w - tw - 16, h - 64, w - 2, h - 32], fill=(255, 255, 255, 215))
        d.text((w - tw - 10, h - 61), rodape, font=fr, fill=(20, 20, 20, 255))

    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    return img, pontos


def escolhe_zoom_raio(lat, raio_m, w, h, zmax=19, zmin=3):
    alvo = 0.80 * min(w, h) / 2.0
    for z in range(zmax, zmin - 1, -1):
        if raio_m / metros_por_pixel(lat, z) <= alvo:
            return z
    return zmin


def escolhe_zoom_dois(p1, p2, w, h, zmax=17, zmin=3):
    for z in range(zmax, zmin - 1, -1):
        x1, y1 = mundo_px(p1[0], p1[1], z)
        x2, y2 = mundo_px(p2[0], p2[1], z)
        if abs(x1 - x2) <= 0.62 * w and abs(y1 - y2) <= 0.52 * (h - 60):
            return z
    return zmin


# ------------------------------------------------------------- figuras

def gera_figuras_evento(n, ev, autor, saida, w, h, zoom_fixo, raio_m, limite_m, k_fig):
    lat_e, lon_e = float(ev["lat"]), float(ev["lon"])
    lat_a, lon_a = float(autor["lat"]), float(autor["lon"])
    dist_m = gc.haversine_km(lat_e, lon_e, lat_a, lon_a) * 1000.0
    prec = float(ev.get("precisao_m") or 0)
    fonte_ev = ev.get("fonte") or "fonte não informada"
    fonte_au = autor.get("fonte") or "fonte não informada"
    quando = ev.get("datahora") or ""
    origem = gc.fonte_norm(ev) or "origem não identificada"
    if origem == "REDE":
        origem = "REDE (Wi-Fi ou torre)"

    rotulo_ref = "residência do autor"
    ref = max(limite_m * 1.6, prec * 1.5)
    z = zoom_fixo or min(escolhe_zoom_raio(lat_e, ref, w, h), escolhe_zoom_raio(lat_a, ref, w, h))

    circ_log = []
    if prec > 0:
        circ_log.append({"lat": lat_e, "lon": lon_e, "raio_m": prec, "cor": VERMELHO,
                         "preencher": True, "tracejado": False})
    img1, _ = painel(
        (lat_e, lon_e), z, w, h,
        "LOCAL REGISTRADO NO LOG (PONTO 1)",
        f"{fonte_ev} | origem: {origem}" + (f" | {quando}" if quando else ""),
        [(lat_e, lon_e, VERMELHO, 1)], circ_log,
        rodape=(f"precisão informada: {prec:.0f} m" if prec > 0 else None))

    circ_dom = [
        {"lat": lat_a, "lon": lon_a, "raio_m": raio_m, "cor": VERDE, "preencher": True, "tracejado": False},
        {"lat": lat_a, "lon": lon_a, "raio_m": limite_m, "cor": VERMELHO, "preencher": False, "tracejado": True},
    ]
    img2, _ = painel(
        (lat_a, lon_a), z, w, h,
        f"{gc.ref_nome(autor).upper()} DO AUTOR (PONTO 2)" if gc.ref_de(autor) == "da residência" else f"{gc.ref_nome(autor).upper()} (PONTO 2)",
        f"{fonte_au}",
        [(lat_a, lon_a, AZUL, 2)], circ_dom,
        rodape=f"círculos: {raio_m:.0f} m (compatível) e {limite_m:.0f} m (limite)")

    gap = 16
    mun_e = gm.municipio_de(lat_e, lon_e)
    mun_a = gm.municipio_de(lat_a, lon_a)
    malha = None
    if gm.disponivel():
        malha = {"destaque": {m["codigo"] for m in (mun_e, mun_a) if m},
                 "rotulos": [(la, lo, m["nome"]) for la, lo, m in ((lat_e, lon_e, mun_e), (lat_a, lon_a, mun_a)) if m]}
    w3 = w * 2 + gap  # a visão geral é um painel largo
    z3 = zoom_fixo or escolhe_zoom_dois((lat_e, lon_e), (lat_a, lon_a), w3, h)
    centro = ((lat_e + lat_a) / 2.0, (lon_e + lon_a) / 2.0)
    img3, pts = painel(
        centro, z3, w3, h,
        "VISÃO GERAL - OS DOIS PONTOS",
        f"1 = local registrado no log ({limpa(fonte_ev)}) | 2 = {rotulo_ref} ({limpa(fonte_au)}) | distância em linha reta: {rotulo_dist(dist_m)}",
        [(lat_e, lon_e, VERMELHO, 1), (lat_a, lon_a, AZUL, 2)],
        [{"lat": lat_a, "lon": lon_a, "raio_m": limite_m, "cor": VERMELHO, "preencher": False, "tracejado": True}],
        malha=malha)
    d3 = ImageDraw.Draw(img3)
    (x1, y1), (x2, y2) = pts
    seg = 0
    comp = math.hypot(x2 - x1, y2 - y1)
    if comp > 30:
        ux, uy = (x2 - x1) / comp, (y2 - y1) / comp
        t = 16
        while t < comp - 16:
            d3.line([(x1 + ux * t, y1 + uy * t), (x1 + ux * min(t + 10, comp - 16), y1 + uy * min(t + 10, comp - 16))],
                    fill=(20, 20, 20), width=3)
            t += 20
            seg += 1
    texto_caixa(d3, ((x1 + x2) / 2 + 12, (y1 + y2) / 2 - 24), rotulo_dist(dist_m), fonte(15, True))

    # painel esquemático único, com cabeçalho e rodapé (conferência; é a imagem da peça só se o usuário autorizar a esquemática)
    cab, rod = 52, 96
    comp_img = Image.new("RGB", (w * 2 + gap, h + cab + rod), BRANCO)
    comp_img.paste(img3, (0, cab))
    dc = ImageDraw.Draw(comp_img)
    dc.text((8, 10), f"FIGURA ILUSTRATIVA {k_fig}", font=fonte(18, True), fill=NAVY)
    y0 = cab + h + 8
    dc.text((8, y0), f"Distância entre o local registrado no log e a residência do autor: {rotulo_dist(dist_m)} em linha reta.",
            font=fonte(14, True), fill=(20, 20, 20))
    dc.text((8, y0 + 32), "Elaborada a partir dos dados constantes dos autos. Figura ilustrativa; não introduz fato nem documento novo.",
            font=fonte(12), fill=CINZA)

    base = os.path.join(saida, f"fig_evento{n}")
    arquivos = {
        "comparativo": base + "_comparativo.png",
        "visao_geral": base + "_visao_geral.png",
    }
    comp_img.save(arquivos["comparativo"], dpi=(150, 150))
    img3.save(arquivos["visao_geral"], dpi=(150, 150))
    def osm(la, lo):
        return f"https://www.openstreetmap.org/?mlat={la}&mlon={lo}#map=17/{la}/{lo}"

    def goo(la, lo):
        return f"https://www.google.com/maps?q={la},{lo}"
    nota_rodape = (f"Coordenadas plotadas na Figura Ilustrativa {k_fig}. Local registrado no log ({lat_e}, {lon_e}): "
                   f"{osm(lat_e, lon_e)} ou {goo(lat_e, lon_e)}. {rotulo_ref[0].upper() + rotulo_ref[1:]} ({lat_a}, {lon_a}): "
                   f"{osm(lat_a, lon_a)} ou {goo(lat_a, lon_a)}.")
    legenda = (
        f"Figura Ilustrativa esquemática {k_fig}. O ponto 1 representa o local registrado na trilha de auditoria "
        f"juntada pelo réu ({limpa(fonte_ev)}); o ponto 2, a residência do autor ({limpa(fonte_au)}). "
        f"Os pontos distam cerca de {rotulo_dist(dist_m)} em linha reta"
        + (f"; a localização do log é estimada por rede (Wi-Fi ou torre), com precisão registrada de {prec:.0f} m"
           if gc.fonte_norm(ev) == "REDE" else "")
        + ". Elaborada pelo patrono a partir dos dados constantes dos autos, por plotagem das coordenadas, sem "
        "mapa de fundo"
        + (", com os limites municipais da " + gm.carrega()["fonte"] if malha else "")
        + "; "
        + ("a coordenada da residência foi indicada pelo patrono a partir do endereço da residência constante dos autos (fonte citada)"
           if gc.ref_de(autor) == "da residência"
           else "a coordenada de referência consta dos autos, na fonte citada")
        + ". Os links para conferir as coordenadas em mapa constam da nota de rodapé. Figura meramente "
        "ilustrativa, que não introduz fato nem documento novo.")

    return {
        "evento": n,
        "tipo": ev.get("tipo"),
        "figura": k_fig,
        "distancia_m": round(dist_m, 1),
        "zoom_paineis": z,
        "zoom_visao_geral": z3,
        "esquematica": True,
        "municipio_log": (mun_e or {}).get("nome"),
        "municipio_referencia": (mun_a or {}).get("nome"),
        "perto_da_divisa": bool((mun_e or {}).get("perto_da_divisa") or (mun_a or {}).get("perto_da_divisa")),
        "fonte_evento": fonte_ev,
        "fonte_domicilio": fonte_au,
        "arquivos": arquivos,
        "paineis": [{"arquivo": arquivos["comparativo"], "legenda": legenda}],
        "nota_rodape": nota_rodape,
    }


def main():
    ap = argparse.ArgumentParser(description="VF9: figuras ilustrativas de geolocalização.")
    ap.add_argument("entrada", help="JSON de entrada (o mesmo do geo_check.py)")
    ap.add_argument("--saida-dir", required=True, help="pasta de saída das imagens")
    ap.add_argument("--eventos", help="números dos eventos, separados por vírgula (padrão: DIVERGENTE na distância ao domicílio, qualquer fonte)")
    ap.add_argument("--fundo", choices=["auto", "esquema"], default="auto",
                    help="auto (padrão): EXIGE o regiao.pmtiles (sem ele, PARA com código 5 e manda perguntar ao usuário); "
                         "entrega as três imagens (visão geral do IBGE, captura do log, captura da residência) nas figuras "
                         "cujos pontos estão dentro do arquivo; esquema: só a visão geral esquemática, por autorização "
                         "expressa do usuário")
    ap.add_argument("--pmtiles", help="caminho do arquivo PMTiles (nome exato regiao.pmtiles; padrão: raiz da pasta de trabalho)")
    ap.add_argument("--zoom", type=int, help="força o zoom dos painéis (3 a 19)")
    ap.add_argument("--largura", type=int, default=640)
    ap.add_argument("--altura", type=int, default=480)
    ap.add_argument("--raio-residencia-m", type=float, default=gc.RAIO_RESIDENCIA_M)
    ap.add_argument("--limite-local-m", type=float, default=gc.LIMITE_LOCAL_M)
    args = ap.parse_args()

    try:
        with open(args.entrada, encoding="utf-8") as f:
            dados = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Erro ao ler a entrada: {e}", file=sys.stderr)
        return 2

    autor = dados.get("autor", {})
    ok, motivo = gc.valida_coordenada(autor.get("lat"), autor.get("lon"))
    if not ok:
        print(f"Erro: o domicílio do autor precisa de coordenada válida para gerar figuras ({motivo}).",
              file=sys.stderr)
        return 2

    gc.RAIO_RESIDENCIA_M = args.raio_residencia_m
    gc.LIMITE_LOCAL_M = args.limite_local_m
    eventos = dados.get("eventos", [])

    if args.eventos:
        try:
            escolhidos = [int(x) for x in args.eventos.split(",") if x.strip()]
        except ValueError:
            print("Erro: --eventos deve ser uma lista de números.", file=sys.stderr)
            return 2
    else:
        res = gc.processa(dados, None, gc.VEL_MAX_KMH_PADRAO)
        escolhidos = []
        for e in res["eventos"]:
            ev = eventos[e["n"] - 1]
            if any(a["teste"] == "distância ao domicílio" and a["classe"] == "DIVERGENTE" for a in e["achados"]):
                # um ponto repetido em várias etapas gera uma só figura
                repetido = any(
                    gc.haversine_km(float(ev["lat"]), float(ev["lon"]),
                                    float(eventos[m - 1]["lat"]), float(eventos[m - 1]["lon"])) * 1000.0
                    <= gc.RAIO_RESIDENCIA_M for m in escolhidos)
                if not repetido:
                    escolhidos.append(e["n"])

    if not escolhidos:
        print("Nenhum evento com resultado DIVERGENTE na distância ao domicílio: nenhuma figura gerada. "
              "Use --eventos para escolher outros.", file=sys.stderr)
        return 0

    if args.fundo == "auto":
        import geo_mapa_pmtiles as gmp0
        if not gmp0.acha_pmtiles(args.pmtiles):
            print("PARADO: o arquivo regiao.pmtiles não foi encontrado (convenção: raiz da pasta conectada, com este nome "
                  "exato). Nenhuma figura foi gerada. Procurado em: " + "; ".join(gmp0.BUSCADOS) + ". "
                  "SOLICITAR AO USUÁRIO: (a) colocar o regiao.pmtiles na pasta conectada ou informar o caminho "
                  "(--pmtiles); ou (b) autorizar, expressamente, só a visão geral esquemática desta vez (--fundo esquema). "
                  "Não escolher por conta própria.", file=sys.stderr)
            return 5

    os.makedirs(args.saida_dir, exist_ok=True)

    manifesto = {"processo": dados.get("processo"), "contrato": dados.get("contrato"), "figuras": [], "avisos": []}
    k = 0
    for n in escolhidos:
        if n < 1 or n > len(eventos):
            print(f"Aviso: evento {n} não existe.", file=sys.stderr)
            continue
        ev = eventos[n - 1]
        oke, mote = gc.valida_coordenada(ev.get("lat"), ev.get("lon"))
        if not oke:
            print(f"Aviso: evento {n} sem coordenada válida ({mote}); figura não gerada.", file=sys.stderr)
            continue
        if gc.fonte_norm(ev) == "REDE":
            manifesto["avisos"].append(
                f"Evento {n}: localização por rede (Wi-Fi ou torre), menos precisa que o GPS. A legenda informa a "
                "precisão registrada no log; confira se o log traz esse valor.")
        elif gc.fonte_norm(ev) != "GPS":
            manifesto["avisos"].append(
                f"Evento {n}: fonte {ev.get('fonte_geo') or 'não identificada'}. Localização que não é GPS é "
                "aproximada (Regra 16); a figura não prova a localização exata.")
        k += 1
        info = gera_figuras_evento(n, ev, autor, args.saida_dir, args.largura, args.altura,
                                   args.zoom, args.raio_residencia_m, args.limite_local_m, k)
        manifesto["figuras"].append(info)
        if gm.disponivel():
            if not info["municipio_log"] or not info["municipio_referencia"]:
                manifesto["avisos"].append(
                    f"Evento {n}: um dos pontos cai fora da malha municipal da Bahia; a figura mostra o contorno "
                    "da Bahia e o ponto fora dele, sem nome de município para esse ponto.")
            if info["perto_da_divisa"]:
                manifesto["avisos"].append(
                    f"Evento {n}: ponto a menos de ~100 m de divisa municipal; a malha é simplificada, então não "
                    "afirmar o município na peça sem conferir.")

    if args.fundo == "auto" and manifesto["figuras"]:
        import subprocess
        import geo_mapa_pmtiles as gmp
        pm = gmp.acha_pmtiles(args.pmtiles)  # já conferido acima; aqui só recupera o caminho
        manifesto["mapa_de_ruas"] = {"arquivo": pm, "buscado_em": list(gmp.BUSCADOS)}
        r = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "geo_mapa_pmtiles.py"),
                            args.entrada, "--saida-dir", args.saida_dir, "--pmtiles", pm,
                            "--eventos", ",".join(str(f_["evento"]) for f_ in manifesto["figuras"]),
                            "--raio-residencia-m", str(args.raio_residencia_m), "--limite-local-m", str(args.limite_local_m)],
                           capture_output=True, text=True, timeout=900)
        pj = os.path.join(args.saida_dir, "figuras_pmtiles.json")
        feitos = {}
        if os.path.exists(pj):
            with open(pj, encoding="utf-8") as fh:
                dj = json.load(fh)
            feitos = {m["evento"]: m for m in dj.get("figuras", [])}
            manifesto["avisos"] += dj.get("avisos", [])
        for f_ in manifesto["figuras"]:
            m = feitos.get(f_["evento"])
            if m and m.get("paineis"):
                f_["tipo_fundo"] = "visão geral do IBGE + capturas de mapa de ruas (PMTiles)"
                f_["paineis"] = m["paineis"]
            else:
                f_["tipo_fundo"] = "só a visão geral do IBGE"
            f_["completa"] = len(f_["paineis"]) >= 3
            if not f_["completa"]:
                manifesto["avisos"].append(
                    f"FIGURA INCOMPLETA (evento {f_['evento']}): só a visão geral (malha do IBGE); faltam as capturas de mapa "
                    "do local do log e da residência (ponto fora da área do regiao.pmtiles ou falha na renderização). "
                    "O conjunto obrigatório são três imagens. SOLICITAR AO USUÁRIO: um regiao.pmtiles que cubra a área ou "
                    "autorização expressa para seguir só com a visão geral. Não decidir por conta própria.")
        if r.returncode not in (0, 4):
            manifesto["avisos"].append("Capturas de mapa de ruas não geradas (" + (r.stderr.strip().splitlines() or ["erro sem mensagem"])[-1] + ").")
    else:  # --fundo esquema, por autorização expressa do usuário
        for f_ in manifesto["figuras"]:
            f_["tipo_fundo"] = "só a visão geral do IBGE (autorizada pelo usuário)"
            f_["completa"] = False
        manifesto["avisos"].append("Figura só com a visão geral esquemática, por autorização expressa do usuário: o conjunto "
                                   "obrigatório (visão geral, captura do log, captura da residência) não foi gerado.")
    if manifesto["figuras"]:
        with open(os.path.join(args.saida_dir, "links_coordenadas.md"), "w", encoding="utf-8") as lf:
            lf.write("# Nota de rodapé: links das coordenadas\n\nUma nota por figura. Colar no rodapé do ponto "
                     "em que a figura entra na peça.\n\n")
            for f_ in manifesto["figuras"]:
                lf.write(f"- {f_['nota_rodape']}\n")
        manifesto["avisos"].append("Inserir a nota de rodapé de cada figura, com os links das coordenadas "
                                   "(figuras.json, campo nota_rodape; também em links_coordenadas.md).")
    manifesto["avisos"].append(
        "Figura Ilustrativa: cada elemento remete a ID e página dos autos; a coordenada da residência foi indicada "
        "pelo advogado. Conferir o ponto do log contra a imagem da página citada antes de usar.")

    with open(os.path.join(args.saida_dir, "figuras.json"), "w", encoding="utf-8") as f:
        json.dump(manifesto, f, ensure_ascii=False, indent=2)

    for f_ in manifesto["figuras"]:
        print(f"Evento {f_['evento']}: {len(f_['paineis'])} imagem(ns), {'completa' if f_['completa'] else 'INCOMPLETA'} "
              f"({rotulo_dist(f_['distancia_m'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
