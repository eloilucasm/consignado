#!/usr/bin/env python3
"""
geo_malha.py - malha municipal da Bahia (IBGE, 2025) para as figuras e para a checagem de município.

Dois usos:
  1) Construir o arquivo compacto a partir do shapefile do IBGE (uma vez, ou quando sair malha nova):
         python3 geo_malha.py --construir BA_Municipios_2025.shp --saida ../assets/ba_municipios.json [--tol-m 40]
     Só biblioteca padrão. Lê .shp (polígonos) e .dbf (CD_MUN, NM_MUN), simplifica os limites pelo método de
     Douglas-Peucker (tolerância em metros) e grava JSON compacto. Sistema de coordenadas: SIRGAS 2000, que
     para este fim equivale a WGS 84 (diferença de centímetros).
  2) Importar como módulo: carrega(), municipio_de(lat, lon), desenha_malha(...) (usado pelo geo_figuras.py).

Limites de uso (ler antes de citar na peça):
  - A malha é simplificada para o desenho. Ponto a menos de ~100 m de uma divisa pode cair no município
    vizinho; municipio_de() devolve também a distância aproximada à divisa mais próxima ("perto_da_divisa")
    para o script avisar. Não usar para decidir caso de divisa sem conferir.
  - Fonte: IBGE, Malha Municipal Digital, 2025. Citar a fonte na legenda. Antes de usar, leia a Nota
    Metodológica do IBGE indicada no LEIA-ME que acompanha a malha.
  - Cobre só a Bahia. Ponto fora da Bahia devolve None.
"""
import argparse
import json
import math
import os
import struct
import sys

CAMINHO_PADRAO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "ba_municipios.json")
FONTE = "Malha Municipal Digital, IBGE, 2025"
_cache = None


# ----------------------------------------------------------- construção

def _le_dbf(caminho):
    d = open(caminho, "rb").read()
    n, hl, rl = struct.unpack("<xxxxIHH", d[:12])
    campos, o = [], 32
    while d[o] != 0x0D:
        campos.append((d[o:o + 11].split(b"\0")[0].decode(), d[o + 16]))
        o += 32
    regs = []
    for i in range(n):
        r = d[hl + i * rl: hl + (i + 1) * rl]
        p, linha = 1, {}
        for nome, ln in campos:
            linha[nome] = r[p:p + ln].decode("utf-8", "replace").strip()
            p += ln
        regs.append(linha)
    return regs


def _le_shp(caminho):
    s = open(caminho, "rb").read()
    if struct.unpack("<i", s[32:36])[0] != 5:
        raise ValueError("o shapefile precisa ser de polígonos (tipo 5)")
    o, formas = 100, []
    while o + 8 <= len(s):
        _, clen = struct.unpack(">ii", s[o:o + 8])
        c = s[o + 8: o + 8 + clen * 2]
        o += 8 + clen * 2
        tipo = struct.unpack("<i", c[:4])[0]
        if tipo == 0:
            formas.append([])
            continue
        npart, npts = struct.unpack("<ii", c[36:44])
        partes = list(struct.unpack(f"<{npart}i", c[44:44 + 4 * npart])) + [npts]
        base = 44 + 4 * npart
        pts = struct.unpack(f"<{2 * npts}d", c[base: base + 16 * npts])
        aneis = []
        for i in range(npart):
            a = [(pts[2 * k], pts[2 * k + 1]) for k in range(partes[i], partes[i + 1])]
            aneis.append(a)
        formas.append(aneis)
    return formas


def _area_assinada(a):
    return sum(a[i][0] * a[i + 1][1] - a[i + 1][0] * a[i][1] for i in range(len(a) - 1)) / 2.0


def _dp(pts, tol):
    """Douglas-Peucker iterativo."""
    if len(pts) < 3:
        return pts
    manter = [False] * len(pts)
    manter[0] = manter[-1] = True
    pilha = [(0, len(pts) - 1)]
    while pilha:
        i, j = pilha.pop()
        ax, ay = pts[i]
        bx, by = pts[j]
        dx, dy = bx - ax, by - ay
        den = math.hypot(dx, dy)
        dmax, k = -1.0, -1
        for m in range(i + 1, j):
            px, py = pts[m]
            d = (math.hypot(px - ax, py - ay) if den == 0
                 else abs(dy * (px - ax) - dx * (py - ay)) / den)
            if d > dmax:
                dmax, k = d, m
        if dmax > tol and k > 0:
            manter[k] = True
            pilha += [(i, k), (k, j)]
    return [p for p, m in zip(pts, manter) if m]


def constroi(shp, saida, tol_m=40.0):
    dbf = os.path.splitext(shp)[0] + ".dbf"
    regs, formas = _le_dbf(dbf), _le_shp(shp)
    if len(regs) != len(formas):
        raise ValueError("DBF e SHP com número de registros diferente")
    tol = tol_m / 111320.0
    out, antes, depois = [], 0, 0
    for r, aneis in zip(regs, formas):
        rr = []
        for a in aneis:
            antes += len(a)
            s = _dp(a, tol)
            if len(s) >= 4:
                depois += len(s)
                rr.append([[round(x, 5), round(y, 5)] for x, y in s])
        xs = [p[0] for a in rr for p in a]
        ys = [p[1] for a in rr for p in a]
        out.append({"c": r.get("CD_MUN"), "n": r.get("NM_MUN"), "uf": r.get("SIGLA_UF"),
                    "ri": r.get("NM_RGI"), "rt": r.get("NM_RGINT"),
                    "b": [min(xs), min(ys), max(xs), max(ys)], "r": rr})
    os.makedirs(os.path.dirname(os.path.abspath(saida)), exist_ok=True)
    with open(saida, "w", encoding="utf-8") as f:
        json.dump({"fonte": FONTE, "tol_m": tol_m, "municipios": out}, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(out)} municípios; vértices {antes} -> {depois}; {os.path.getsize(saida) / 1e6:.2f} MB em {saida}")


# ----------------------------------------------------------- uso

def carrega(caminho=None):
    global _cache
    if _cache is None:
        try:
            with open(caminho or CAMINHO_PADRAO, encoding="utf-8") as f:
                _cache = json.load(f)
        except (OSError, json.JSONDecodeError):
            _cache = {"fonte": FONTE, "municipios": []}
    return _cache


def disponivel():
    return bool(carrega()["municipios"])


def _dentro(x, y, anel):
    dentro = False
    j = len(anel) - 1
    for i in range(len(anel)):
        xi, yi = anel[i]
        xj, yj = anel[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            dentro = not dentro
        j = i
    return dentro


def _dist_segmento_m(x, y, a, b):
    k = 111320.0
    cx = math.cos(math.radians(y))
    px, py = x * cx * k, y * k
    ax, ay, bx, by = a[0] * cx * k, a[1] * k, b[0] * cx * k, b[1] * k
    dx, dy = bx - ax, by - ay
    t = 0 if dx == dy == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def municipio_de(lat, lon, folga_divisa_m=100.0):
    """Devolve {'codigo','nome','uf','perto_da_divisa'} ou None (fora da malha). Sem malha: None."""
    for m in carrega()["municipios"]:
        b = m["b"]
        if not (b[0] <= lon <= b[2] and b[1] <= lat <= b[3]):
            continue
        # furo (anel interno) é raro nesta malha; regra par-ímpar sobre todos os anéis cobre os dois casos
        n = sum(1 for a in m["r"] if _dentro(lon, lat, a))
        if n % 2 == 1:
            dmin = min(_dist_segmento_m(lon, lat, a[i], a[i + 1]) for a in m["r"] for i in range(len(a) - 1))
            return {"codigo": m["c"], "nome": m["n"], "uf": m.get("uf") or "BA",
                    "perto_da_divisa": dmin <= folga_divisa_m}
    return None


def desenha_malha(draw, pt, caixa_lonlat, destaque=(), cor_linha=(150, 150, 146), cor_destaque=(35, 39, 95),
                  rotulo=None, fonte=None, largura_img=0, altura_img=0):
    """Desenha os limites municipais que cruzam a caixa (lon_min, lat_min, lon_max, lat_max).
    pt(lat, lon) -> (x, y) em pixels. destaque: códigos de município a realçar, com o nome impresso."""
    x0, y0, x1, y1 = caixa_lonlat
    for m in carrega()["municipios"]:
        b = m["b"]
        if b[2] < x0 or b[0] > x1 or b[3] < y0 or b[1] > y1:
            continue
        realce = m["c"] in destaque
        for a in m["r"]:
            xy = [pt(p[1], p[0]) for p in a]
            draw.line(xy, fill=(cor_destaque if realce else cor_linha) + (255,), width=3 if realce else 1)
        if realce and rotulo and fonte:
            cx, cy = pt((b[1] + b[3]) / 2, (b[0] + b[2]) / 2)
            if 0 <= cx <= largura_img and 0 <= cy <= altura_img:
                rotulo((int(cx) - 40, int(cy) + 40), m["n"], fonte)


def _norm(s):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", (s or "").lower()) if unicodedata.category(c) != "Mn").strip()


def regiao(rgint=None, rgi=None, municipios=None):
    """Municípios de uma região geográfica intermediária, imediata ou lista de nomes (sem acento/caixa)."""
    mm = carrega()["municipios"]
    if rgint:
        return [m for m in mm if _norm(m.get("rt")) == _norm(rgint)]
    if rgi:
        return [m for m in mm if _norm(m.get("ri")) == _norm(rgi)]
    nomes = {_norm(x) for x in (municipios or [])}
    return [m for m in mm if _norm(m["n"]) in nomes]


def grava_regiao(muns, saida_geojson):
    """GeoJSON (MultiPolygon) da região para o `pmtiles extract --region`. Devolve a caixa (lon_min, lat_min, lon_max, lat_max)."""
    def ccw(a):  # GeoJSON (RFC 7946): anel externo anti-horário; o shapefile do IBGE vem no sentido horário
        return a if _area_assinada(a) > 0 else a[::-1]
    polys = [[ccw(a)] for m in muns for a in m["r"]]
    try:  # com shapely: um contorno só (união, folga de ~1 km, simplificado), bem mais leve para o pmtiles extract
        from shapely.geometry import MultiPolygon, Polygon, mapping
        from shapely.ops import unary_union
        u = unary_union([Polygon(a).buffer(0) for m in muns for a in m["r"]]).buffer(0.01).simplify(0.004)
        from shapely.geometry.polygon import orient
        u = (MultiPolygon([orient(g, 1.0) for g in u.geoms]) if u.geom_type == "MultiPolygon" else orient(u, 1.0))
        geom = mapping(u)
    except ImportError:
        geom = {"type": "MultiPolygon", "coordinates": polys}
    x0 = min(m["b"][0] for m in muns); y0 = min(m["b"][1] for m in muns)
    x1 = max(m["b"][2] for m in muns); y1 = max(m["b"][3] for m in muns)
    with open(saida_geojson, "w", encoding="utf-8") as f:
        json.dump({"type": "Feature", "properties": {"municipios": len(muns)}, "geometry": geom},
                  f, separators=(",", ":"))
    return x0, y0, x1, y1


def main():
    ap = argparse.ArgumentParser(description="Malha municipal da Bahia (IBGE) para as figuras da VF9.")
    ap.add_argument("--construir", metavar="SHP", help="shapefile do IBGE a converter")
    ap.add_argument("--saida", default=CAMINHO_PADRAO)
    ap.add_argument("--tol-m", type=float, default=40.0, help="tolerância de simplificação, em metros")
    ap.add_argument("--listar-regioes", action="store_true", help="lista as regiões geográficas intermediárias da Bahia")
    ap.add_argument("--regiao-rgint", metavar="NOME", help='região intermediária, ex.: "Ilhéus - Itabuna"')
    ap.add_argument("--regiao-rgi", metavar="NOME", help='região imediata, ex.: "Ilhéus - Itabuna"')
    ap.add_argument("--regiao-municipios", metavar="A,B,C", help="lista de municípios separados por vírgula")
    ap.add_argument("--regiao-bahia", action="store_true", help="a Bahia inteira (417 municípios)")
    ap.add_argument("--regiao-saida", default="regiao.geojson", help="GeoJSON de saída para o pmtiles extract")
    ap.add_argument("--onde", nargs=2, type=float, metavar=("LAT", "LON"), help="diz em que município cai o ponto")
    a = ap.parse_args()
    if a.construir:
        constroi(a.construir, a.saida, a.tol_m)
    if a.onde:
        print(municipio_de(*a.onde) or "fora da malha da Bahia")
    if a.listar_regioes:
        cont = {}
        for m in carrega()["municipios"]:
            cont.setdefault(m.get("rt"), set()).add(m.get("ri"))
        for k, v in sorted(cont.items(), key=lambda kv: str(kv[0])):
            print(f"{k}: {', '.join(sorted(x for x in v if x))}")
    if a.regiao_bahia or a.regiao_rgint or a.regiao_rgi or a.regiao_municipios:
        muns = (carrega()["municipios"] if a.regiao_bahia else
                regiao(a.regiao_rgint, a.regiao_rgi, a.regiao_municipios.split(",") if a.regiao_municipios else None))
        if not muns:
            print("Nenhum município encontrado para essa região (use --listar-regioes).", file=sys.stderr)
            return 2
        x0, y0, x1, y1 = grava_regiao(muns, a.regiao_saida)
        print(f"{len(muns)} municípios; caixa {x0:.4f},{y0:.4f},{x1:.4f},{y1:.4f}; GeoJSON em {a.regiao_saida}")
        print(f"pmtiles extract <URL-da-build> regiao.pmtiles --region={os.path.basename(a.regiao_saida)} --maxzoom=14")
    if not (a.construir or a.onde or a.listar_regioes or a.regiao_bahia or a.regiao_rgint or a.regiao_rgi or a.regiao_municipios):
        ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
