#!/usr/bin/env python3
"""
geo_mapa_pmtiles.py - Figura Ilustrativa com MAPA DE RUAS OFFLINE, a partir de um arquivo PMTiles da região.

Não usa a internet. Funciona na própria máquina do Cowork (ou em qualquer máquina com Python, Pillow,
Playwright e Chromium): sobe um servidor local com suporte a Range, abre um Chromium sem janela com o
MapLibre GL, desenha o mapa-base do Protomaps (dados do OpenStreetMap) lendo o PMTiles local, marca os pontos
e captura três painéis por figura:
    figura<k>_evento<n>_captura1_log.png          ponto do log (círculo de precisão, se houver)
    figura<k>_evento<n>_captura2_referencia.png   ponto de referência do autor, com os círculos de 100 m e 150 m
Depois chama o geo_compor.py, que grava as imagens B e C (e a A, da malha do IBGE) e fig_evento<n>_paineis.json
(ordem e legenda de cada imagem). Grava também figuras_pmtiles.json (paineis, arquivos, avisos) para o
geo_figuras.py, que é quem normalmente chama este script.

O arquivo PMTiles não vem na skill (passa do limite de 30 MB): o advogado o gera uma vez (ver
references/mapa_offline_pmtiles.md) e o coloca, com o nome exato regiao.pmtiles, na raiz da pasta conectada, ou o
informa em --pmtiles. Figura cujos pontos caem fora da área do arquivo não ganha as capturas B e C (aviso); o
geo_figuras.py marca a figura como INCOMPLETA e manda perguntar ao usuário.

Uso:
    python3 geo_mapa_pmtiles.py entrada.json --saida-dir figuras/
    python3 geo_mapa_pmtiles.py entrada.json --saida-dir figuras/ --eventos 2,3 --pmtiles /caminho/regiao.pmtiles

Dependências: Pillow, playwright (Python) e um Chromium. Bibliotecas JS, fontes e ícones já estão em assets/mapa/.
"""
import argparse
import json
import math
import os
import re
import struct
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import geo_check as gc  # noqa: E402
import geo_dados_figura as gh  # noqa: E402

RAIZ_ASSETS = os.path.join(AQUI, "..", "assets", "mapa")
PMTILES_PADRAO = os.path.join(RAIZ_ASSETS, "regiao.pmtiles")
ATRIBUICAO = "© OpenStreetMap contributors | Protomaps"
ATRIBUICAO_LEGENDA = "Mapa de fundo © OpenStreetMap contributors, Protomaps."
ARGS_CHROMIUM = ["--no-sandbox", "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader",
                 "--ignore-gpu-blocklist", "--disable-dev-shm-usage"]
W, H = 1100, 700


BUSCADOS = []  # lugares onde a última busca olhou (vai para figuras.json e para o aviso)


def _pmtiles_valido(c):
    try:
        with open(c, "rb") as f:
            b = f.read(8)
        return b[:7] == b"PMTiles" and b[7] == 3
    except OSError:
        return False


def acha_pmtiles(explicito=None):
    """Procura SÓ o arquivo `regiao.pmtiles` (convenção): --pmtiles, variável GEO_PMTILES, assets/mapa/, raiz da
    pasta de trabalho, /mnt/<pasta>/, /sessions/<sessão>/mnt/<pasta>/ (pasta conectada do Cowork) e uma subpasta
    abaixo da pasta de trabalho. Só aceita arquivo com cabeçalho
    PMTiles v3. Outro nome NÃO é aceito. Devolve o caminho ou None; os lugares olhados ficam em BUSCADOS.
    O arquivo é grande demais para ir dentro da skill (limite de 30 MB)."""
    import glob
    BUSCADOS.clear()
    cwd = os.getcwd()
    for c in (explicito, os.environ.get("GEO_PMTILES"), PMTILES_PADRAO, os.path.join(cwd, "regiao.pmtiles")):
        if c:
            BUSCADOS.append(c)
            if os.path.isfile(c) and _pmtiles_valido(c):
                return c
    for padrao in ("/mnt/*/regiao.pmtiles", "/mnt/*/*/regiao.pmtiles",
                   "/sessions/*/mnt/*/regiao.pmtiles", "/sessions/*/mnt/*/*/regiao.pmtiles",
                   os.path.join(cwd, "mnt", "*", "regiao.pmtiles"), os.path.join(cwd, "*", "regiao.pmtiles")):
        BUSCADOS.append(padrao)
        for f in sorted(glob.glob(padrao)):
            if os.path.isfile(f) and _pmtiles_valido(f):
                return f
    return None


# ------------------------------------------------------------- cabeçalho do PMTiles

def le_cabecalho(caminho):
    """Lê o cabeçalho PMTiles v3 (127 bytes): zoom mínimo e máximo e a caixa em graus."""
    with open(caminho, "rb") as f:
        b = f.read(127)
    if len(b) < 127 or b[:7] != b"PMTiles" or b[7] != 3:
        raise ValueError("não é um arquivo PMTiles versão 3")
    tipo = b[99]
    minz, maxz = b[100], b[101]
    minlon, minlat, maxlon, maxlat = struct.unpack("<4i", b[102:118])
    return {"tipo": tipo, "minzoom": minz, "maxzoom": maxz,
            "bbox": (minlon / 1e7, minlat / 1e7, maxlon / 1e7, maxlat / 1e7)}


def dentro(bbox, lat, lon):
    return bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]


# ------------------------------------------------------------- servidor local com Range

class Servidor:
    def __init__(self, pmtiles, pagina_html):
        self.rotas = {"/lib/": os.path.join(RAIZ_ASSETS, "lib"), "/fonts/": os.path.join(RAIZ_ASSETS, "fonts"),
                      "/sprites/": os.path.join(RAIZ_ASSETS, "sprites")}
        self.pmtiles = pmtiles
        self.pagina = pagina_html.encode("utf-8")
        srv = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def _arquivo(self):
                caminho = self.path.split("?")[0]
                from urllib.parse import unquote
                caminho = unquote(caminho)
                # os nomes no disco não têm espaço nem "@" (o zip da skill os recusa): "Noto Sans Regular" -> "Noto_Sans_Regular",
                # "light@2x" -> "light_2x"
                if caminho.startswith(("/fonts/", "/sprites/")):
                    caminho = caminho.replace(" ", "_").replace("@", "_")
                if caminho in ("/", "/pagina.html"):
                    return None, srv.pagina, "text/html; charset=utf-8"
                if caminho == "/regiao.pmtiles":
                    return srv.pmtiles, None, "application/octet-stream"
                for pref, pasta in srv.rotas.items():
                    if caminho.startswith(pref):
                        rel = os.path.normpath(caminho[len(pref):])
                        if rel.startswith("..") or os.path.isabs(rel):
                            return "", None, ""
                        return os.path.join(pasta, rel), None, ""
                return "", None, ""

            def _tipo(self, p):
                return {".js": "text/javascript", ".css": "text/css", ".json": "application/json",
                        ".png": "image/png", ".pbf": "application/x-protobuf"}.get(os.path.splitext(p)[1], "application/octet-stream")

            def _serve(self, enviar_corpo):
                caminho, corpo, tipo = self._arquivo()
                if corpo is not None:
                    self.send_response(200)
                    self.send_header("Content-Type", tipo)
                    self.send_header("Content-Length", str(len(corpo)))
                    self.end_headers()
                    if enviar_corpo:
                        self.wfile.write(corpo)
                    return
                if not caminho or not os.path.isfile(caminho):
                    self.send_response(404)
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                tam = os.path.getsize(caminho)
                ini, fim, status = 0, tam - 1, 200
                m = re.match(r"bytes=(\d*)-(\d*)", self.headers.get("Range") or "")
                if m:
                    if m.group(1):
                        ini = int(m.group(1))
                        fim = int(m.group(2)) if m.group(2) else tam - 1
                    elif m.group(2):
                        ini, fim = max(0, tam - int(m.group(2))), tam - 1
                    fim = min(fim, tam - 1)
                    status = 206
                self.send_response(status)
                self.send_header("Content-Type", tipo or self._tipo(caminho))
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Content-Length", str(fim - ini + 1))
                if status == 206:
                    self.send_header("Content-Range", f"bytes {ini}-{fim}/{tam}")
                self.end_headers()
                if enviar_corpo:
                    with open(caminho, "rb") as f:
                        f.seek(ini)
                        restante = fim - ini + 1
                        while restante > 0:
                            bloco = f.read(min(65536, restante))
                            if not bloco:
                                break
                            self.wfile.write(bloco)
                            restante -= len(bloco)

            def do_GET(self):
                try:
                    self._serve(True)
                except (BrokenPipeError, ConnectionResetError):
                    pass

            def do_HEAD(self):
                self._serve(False)

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.porta = self.httpd.server_address[1]
        self.t = threading.Thread(target=self.httpd.serve_forever, daemon=True)

    def __enter__(self):
        self.t.start()
        return self

    def __exit__(self, *a):
        self.httpd.shutdown()


# ------------------------------------------------------------- página

PAGINA = r'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="/lib/maplibre-gl.css">
<style>
 html,body{margin:0;background:#fff}
 #map{width:1100px;height:700px;position:relative;font-family:Arial,sans-serif}
 .tit{position:absolute;left:0;top:0;right:0;padding:7px 12px;background:rgba(35,39,95,.92);color:#fff;font:700 15px Arial;z-index:5}
 .sub{font:400 12px Arial;opacity:.9;display:block;margin-top:2px}
 .nota{position:absolute;left:10px;bottom:30px;padding:4px 8px;background:rgba(255,255,255,.88);font:12px Arial;color:#222;z-index:5}
 .pino{width:30px;height:30px;border-radius:50%;border:3px solid #fff;color:#fff;font:700 14px/24px Arial;text-align:center;box-shadow:0 0 3px #000}
 .rot{background:rgba(255,255,255,.92);padding:2px 6px;font:700 13px Arial;border:1px solid #bbb;white-space:nowrap}
 .maplibregl-ctrl-attrib{font-size:12px!important}
</style></head><body><div id="map"></div>
<script src="/lib/maplibre-gl.js"></script><script src="/lib/pmtiles.js"></script><script src="/lib/basemaps.js"></script>
<script>
const O = location.origin;
maplibregl.addProtocol('pmtiles', new pmtiles.Protocol().tile);
const style = { version: 8, glyphs: O + '/fonts/{fontstack}/{range}.pbf', sprite: O + '/sprites/light',
  sources: { protomaps: { type: 'vector', url: 'pmtiles://' + O + '/regiao.pmtiles', attribution: '__ATRIBUICAO__' } },
  layers: basemaps.layers('protomaps', basemaps.namedFlavor('light'), { lang: 'pt' }) };
const map = new maplibregl.Map({ container: 'map', style: style, center: [-39, -14.8], zoom: 8, interactive: false,
  fadeDuration: 0, attributionControl: { compact: false } });
let marcadores = [], camadas = [];
window.pronto = false;
map.on('load', () => { window.pronto = true; });
const sleep = ms => new Promise(r => setTimeout(r, ms));

function anel(lat, lon, raio) {
  const pts = [], dlat = raio / 111320, dlon = raio / (111320 * Math.cos(lat * Math.PI / 180));
  for (let i = 0; i <= 120; i++) { const a = i / 120 * 2 * Math.PI; pts.push([lon + dlon * Math.cos(a), lat + dlat * Math.sin(a)]); }
  return pts;
}
function limpa() {
  marcadores.forEach(m => m.remove()); marcadores = [];
  camadas.forEach(id => { if (map.getLayer(id)) map.removeLayer(id); }); camadas = [];
  if (map.getSource('ov')) map.removeSource('ov');
  document.querySelectorAll('.tit,.nota').forEach(e => e.remove());
}
async function mostra(s) {
  limpa();
  const feats = [];
  (s.circulos || []).forEach(c => feats.push({ type: 'Feature', properties: { cor: c.cor, dash: !!c.tracejado, fill: !!c.preencher },
    geometry: { type: 'Polygon', coordinates: [anel(c.lat, c.lon, c.raio)] } }));
  if (s.linha) feats.push({ type: 'Feature', properties: { cor: '#c62828', dash: true, fill: false, linha: true },
    geometry: { type: 'LineString', coordinates: s.linha } });
  map.addSource('ov', { type: 'geojson', data: { type: 'FeatureCollection', features: feats } });
  const add = (id, def) => { map.addLayer(Object.assign({ id: id, source: 'ov' }, def)); camadas.push(id); };
  add('ov-fill', { type: 'fill', filter: ['all', ['==', ['geometry-type'], 'Polygon'], ['get', 'fill']], paint: { 'fill-color': ['get', 'cor'], 'fill-opacity': 0.16 } });
  add('ov-solido', { type: 'line', filter: ['!', ['get', 'dash']], paint: { 'line-color': ['get', 'cor'], 'line-width': 3 } });
  add('ov-tracejado', { type: 'line', filter: ['get', 'dash'], paint: { 'line-color': ['get', 'cor'], 'line-width': 3, 'line-dasharray': [2, 2] } });
  (s.marcas || []).forEach(m => {
    const el = document.createElement('div'); el.className = 'pino'; el.style.background = m.cor; el.textContent = m.n;
    marcadores.push(new maplibregl.Marker({ element: el }).setLngLat([m.lon, m.lat]).addTo(map));
  });
  (s.rotulos || []).forEach(r => {
    const el = document.createElement('div'); el.className = 'rot'; el.style.color = r.cor || '#222'; el.textContent = r.texto;
    marcadores.push(new maplibregl.Marker({ element: el, anchor: 'top-left', offset: [r.dx || 18, r.dy || 4] }).setLngLat([r.lon, r.lat]).addTo(map));
  });
  const tit = document.createElement('div'); tit.className = 'tit'; tit.innerHTML = s.titulo + (s.sub ? '<span class="sub">' + s.sub + '</span>' : '');
  document.getElementById('map').appendChild(tit);
  if (s.nota) { const n = document.createElement('div'); n.className = 'nota'; n.textContent = s.nota; document.getElementById('map').appendChild(n); }
  if (s.bbox) map.fitBounds([[s.bbox[0], s.bbox[1]], [s.bbox[2], s.bbox[3]]], { padding: s.padding || 20, duration: 0, maxZoom: s.maxZoom || 18 });
  else map.jumpTo({ center: s.centro, zoom: s.zoom });
  map.triggerRepaint(); await sleep(300);
  const t0 = Date.now();
  while (Date.now() - t0 < 40000) { if (map.loaded() && map.areTilesLoaded()) break; await sleep(100); }
  await sleep(500);
  let n = 0; ['earth', 'water', 'landuse', 'roads', 'buildings', 'places'].forEach(l => { n += map.querySourceFeatures('protomaps', { sourceLayer: l }).length; });
  return { zoom: map.getZoom(), feicoes: n, ok: map.loaded() && map.areTilesLoaded() };
}
</script></body></html>'''


# ------------------------------------------------------------- painéis

def caixa_raio(lat, lon, raio_m):
    dlat = raio_m / 111320.0
    dlon = raio_m / (111320.0 * math.cos(math.radians(lat)))
    return [lon - dlon, lat - dlat, lon + dlon, lat + dlat]


def specs_figura(f, raio, limite):
    rv = max(limite * 1.6, f["prec"] * 1.5)
    rv2 = max(limite * 1.6, f["rprec"] * 1.5)
    circ_log = ([{"lat": f["lat"], "lon": f["lon"], "raio": f["prec"], "cor": "#1565c0", "preencher": True}]
                if f["prec"] > 0 else [])
    a = {"titulo": "LOCAL REGISTRADO NO LOG (PONTO 1)", "bbox": caixa_raio(f["lat"], f["lon"], rv), "padding": 0,
         "marcas": [{"lat": f["lat"], "lon": f["lon"], "cor": "#c62828", "n": 1}], "circulos": circ_log,
         "nota": (f"precisão informada: {f['prec']:.0f} m" if f["prec"] > 0 else None)}
    b = {"titulo": f["ref"].upper() + " (PONTO 2)", "bbox": caixa_raio(f["rlat"], f["rlon"], rv2), "padding": 0,
         "marcas": [{"lat": f["rlat"], "lon": f["rlon"], "cor": "#1F3A5F", "n": 2}],
         "circulos": [{"lat": f["rlat"], "lon": f["rlon"], "raio": raio, "cor": "#2e7d32", "preencher": True},
                      {"lat": f["rlat"], "lon": f["rlon"], "raio": limite, "cor": "#c62828", "tracejado": True}],
         "nota": f"círculos: {raio:.0f} m (compatível) e {limite:.0f} m (limite)"}
    c = {"titulo": "VISÃO GERAL - OS DOIS PONTOS", "sub": "distância em linha reta: " + f["dist"],
         "bbox": [min(f["lon"], f["rlon"]), min(f["lat"], f["rlat"]), max(f["lon"], f["rlon"]), max(f["lat"], f["rlat"])],
         "padding": 130, "maxZoom": 17,
         "marcas": [{"lat": f["lat"], "lon": f["lon"], "cor": "#c62828", "n": 1},
                    {"lat": f["rlat"], "lon": f["rlon"], "cor": "#1F3A5F", "n": 2}],
         "linha": [[f["lon"], f["lat"]], [f["rlon"], f["rlat"]]],
         "rotulos": [{"lat": (f["lat"] + f["rlat"]) / 2, "lon": (f["lon"] + f["rlon"]) / 2, "texto": f["dist"], "dx": 14, "dy": -28}]}
    return [("captura1_log", a), ("captura2_referencia", b)]  # a visão geral é a da malha do IBGE (geo_figuras)


def main():
    ap = argparse.ArgumentParser(description="Figura Ilustrativa com mapa de ruas offline (PMTiles).")
    ap.add_argument("entrada")
    ap.add_argument("--saida-dir", default="figuras")
    ap.add_argument("--eventos", help="números dos eventos, separados por vírgula (padrão: divergentes, um por ponto)")
    ap.add_argument("--pmtiles", help="caminho do arquivo (padrão: procura em assets/mapa/, pasta de trabalho e /mnt)")
    ap.add_argument("--raio-residencia-m", type=float, default=gc.RAIO_RESIDENCIA_M)
    ap.add_argument("--limite-local-m", type=float, default=gc.LIMITE_LOCAL_M)
    a = ap.parse_args()

    a.pmtiles = acha_pmtiles(a.pmtiles)
    if not a.pmtiles:
        print("Sem arquivo PMTiles (assets/mapa/regiao.pmtiles, pasta de trabalho, /mnt ou GEO_PMTILES). "
              "Veja references/mapa_offline_pmtiles.md.", file=sys.stderr)
        return 3
    try:
        cab = le_cabecalho(a.pmtiles)
    except (OSError, ValueError) as e:
        print(f"PMTiles inválido: {e}", file=sys.stderr)
        return 3
    if cab["tipo"] != 1:
        print("O PMTiles precisa conter tiles vetoriais (MVT) do mapa-base do Protomaps.", file=sys.stderr)
        return 3
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Falta o pacote Python 'playwright' (pip install playwright --break-system-packages) e um Chromium.",
              file=sys.stderr)
        return 3

    with open(a.entrada, encoding="utf-8") as f:
        dados = json.load(f)
    autor = dados.get("autor", {})
    oka, mota = gc.valida_coordenada(autor.get("lat"), autor.get("lon"))
    if not oka:
        print(f"Erro: a referência do autor precisa de coordenada válida ({mota}).", file=sys.stderr)
        return 2
    gc.RAIO_RESIDENCIA_M, gc.LIMITE_LOCAL_M = a.raio_residencia_m, a.limite_local_m
    esc = [int(x) for x in a.eventos.split(",") if x.strip()] if a.eventos else []
    sel = gh.seleciona(dados, esc)
    figs = gh.monta_figs(dados, sel)
    saida = a.saida_dir
    os.makedirs(saida, exist_ok=True)

    manifesto = {"pmtiles": os.path.basename(a.pmtiles), "bbox_pmtiles": cab["bbox"], "figuras": [], "avisos": []}
    elegiveis = []
    for f in figs:
        if dentro(cab["bbox"], f["lat"], f["lon"]) and dentro(cab["bbox"], f["rlat"], f["rlon"]):
            elegiveis.append(f)
        else:
            manifesto["avisos"].append(
                f"Evento {f['n']}: ponto fora da área do arquivo PMTiles ({cab['bbox']}); figura de mapa de ruas "
                "não gerada (usar a figura esquemática ou ampliar a região do PMTiles).")
    if not elegiveis:
        with open(os.path.join(saida, "figuras_pmtiles.json"), "w", encoding="utf-8") as fh:
            json.dump(manifesto, fh, ensure_ascii=False, indent=2)
        print("Nenhuma figura dentro da área do PMTiles.", file=sys.stderr)
        return 4

    pagina = PAGINA.replace("__ATRIBUICAO__", ATRIBUICAO)
    erros_console = []
    with Servidor(a.pmtiles, pagina) as srv, sync_playwright() as p:
        nav = p.chromium.launch(args=ARGS_CHROMIUM)
        pg = nav.new_page(viewport={"width": W, "height": H})
        pg.on("console", lambda m: erros_console.append(m.text) if m.type == "error" else None)
        pg.goto(f"http://127.0.0.1:{srv.porta}/")
        pg.wait_for_function("window.pronto === true", timeout=60000)
        legendas, falhas = [], []
        for f in elegiveis:
            arquivos, ok_fig = [], True
            for nome, spec in specs_figura(f, a.raio_residencia_m, a.limite_local_m):
                r = pg.evaluate("s => mostra(s)", spec)
                destino = os.path.join(saida, f"figura{f['k']}_evento{f['n']}_{nome}.png")
                if not r["ok"] or r["feicoes"] == 0:
                    ok_fig = False
                    falhas.append(f"Evento {f['n']}, painel {nome}: mapa sem dados ({r})")
                    continue
                pg.locator("#map").screenshot(path=destino)
                arquivos.append(destino)
            if ok_fig:
                legendas.append({"k": f["k"], "n": f["n"], "distancia": f["dist"],
                                 "paineis": [x.replace("Mapa de fundo © OpenStreetMap contributors.", ATRIBUICAO_LEGENDA)
                                             for x in f["paineis"]]})
                manifesto["figuras"].append({"evento": f["n"], "figura": f["k"], "distancia": f["dist"]})
        nav.close()
    manifesto["avisos"] += falhas
    if erros_console:
        manifesto["avisos"].append("Mensagens de erro do navegador (podem ser faixas de fonte ausentes): "
                                   + "; ".join(sorted(set(erros_console))[:4]))
    with open(os.path.join(saida, "legendas_plano_b.json"), "w", encoding="utf-8") as fh:
        json.dump(legendas, fh, ensure_ascii=False, indent=2)
    subprocess.run([sys.executable, os.path.join(AQUI, "geo_compor.py"), "--pasta", saida,
                    "--atribuicao", ATRIBUICAO_LEGENDA], check=False)
    for m in manifesto["figuras"]:
        pj_ = os.path.join(saida, f"fig_evento{m['evento']}_paineis.json")
        if os.path.exists(pj_):
            with open(pj_, encoding="utf-8") as fh_:
                m["paineis"] = json.load(fh_)
    with open(os.path.join(saida, "figuras_pmtiles.json"), "w", encoding="utf-8") as fh:
        json.dump(manifesto, fh, ensure_ascii=False, indent=2)
    for av in manifesto["avisos"]:
        print("Aviso:", av, file=sys.stderr)
    print(f"{len(manifesto['figuras'])} figura(s) com mapa de ruas offline em {saida}.")
    return 0 if manifesto["figuras"] else 4


if __name__ == "__main__":
    sys.exit(main())
