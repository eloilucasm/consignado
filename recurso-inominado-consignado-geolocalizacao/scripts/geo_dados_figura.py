#!/usr/bin/env python3
"""geo_dados_figura.py - dados e legendas da Figura Ilustrativa (VF9), usados pelo geo_figuras.py e pelo
geo_mapa_pmtiles.py. Não gera imagem nem acessa a rede.

Funções: rotulo_dist, seleciona (eventos que viram figura), legendas_paineis (legenda de cada uma das três imagens:
A visão geral do IBGE, B captura do local do log, C captura da residência) e monta_figs (dados de cada figura).
Regras: 6, 16, 17, 18 e 19 (ver SKILL.md). Figura Ilustrativa não introduz fato novo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import geo_check as gc  # noqa: E402


def rotulo_dist(m):
    return f"{m:.0f} m" if m < 1000 else f"{m / 1000:.1f} km".replace(".", ",")


def seleciona(dados, escolhidos):
    eventos = dados.get("eventos", [])
    if escolhidos:
        return escolhidos
    res = gc.processa(dados, None, gc.VEL_MAX_KMH_PADRAO)
    sel = []
    for e in res["eventos"]:
        ev = eventos[e["n"] - 1]
        ok, _ = gc.valida_coordenada(ev.get("lat"), ev.get("lon"))
        if not ok:
            continue
        if any(a["teste"] == "distância ao domicílio" and a["classe"] == "DIVERGENTE" for a in e["achados"]):
            rep = any(gc.haversine_km(float(ev["lat"]), float(ev["lon"]),
                                      float(eventos[m - 1]["lat"]), float(eventos[m - 1]["lon"])) * 1000.0
                      <= gc.RAIO_RESIDENCIA_M for m in sel)
            if not rep:
                sel.append(e["n"])
    return sel


def legendas_paineis(k, ev, autor, dist_m, atribuicao="Mapa de fundo © OpenStreetMap contributors."):
    """Legenda própria de cada imagem, na ordem da peça: A visão geral dos dois pontos (malha do IBGE),
    B local registrado no log (captura de mapa), C residência do autor (captura de mapa)."""
    fonte_ev = ev.get("fonte") or "fonte não informada"
    fonte_au = autor.get("fonte") or "fonte não informada"
    extra = ""
    if gc.fonte_norm(ev) == "REDE":
        extra = (f"; a localização do log é estimada por rede (Wi-Fi ou torre), com precisão registrada de "
                 f"{float(ev.get('precisao_m') or 0):.0f} m")
    try:
        import geo_malha as gm
        malha = gm.carrega()["fonte"] if gm.disponivel() else None
    except Exception:
        malha = None
    fim = " Figura meramente ilustrativa, que não introduz fato nem documento novo."
    return [
        f"Figura Ilustrativa {k}A. Visão geral dos dois pontos (1, local registrado na trilha de auditoria juntada pelo "
        f"réu; 2, residência do autor), que distam cerca de {rotulo_dist(dist_m)} em linha reta"
        + (f", sobre os limites municipais da {malha}" if malha else "")
        + f". Elaborada pelo patrono a partir dos dados constantes dos autos ({fonte_ev}; {fonte_au}).{fim}",
        f"Figura Ilustrativa {k}B. Local registrado na trilha de auditoria juntada pelo réu ({fonte_ev}){extra}. "
        f"Elaborada pelo patrono a partir dos dados constantes dos autos. {atribuicao}{fim}",
        f"Figura Ilustrativa {k}C. Residência do autor ({fonte_au}); a coordenada da residência foi indicada pelo "
        f"patrono a partir do endereço da residência constante dos autos (fonte citada). Os círculos marcam as "
        f"distâncias de referência indicadas na própria imagem. {atribuicao}{fim}",
    ]


def monta_figs(dados, sel):
    """Dados de cada figura (coordenadas, rótulos, legendas das três imagens). Usada pelo geo_mapa_pmtiles.py."""
    autor = dados.get("autor", {})
    figs = []
    for k, n in enumerate(sel, 1):
        ev = dados["eventos"][n - 1]
        ok, _ = gc.valida_coordenada(ev.get("lat"), ev.get("lon"))
        if not ok:
            print(f"Aviso: evento {n} sem coordenada válida; ignorado.", file=sys.stderr)
            continue
        lat, lon = float(ev["lat"]), float(ev["lon"])
        rlat, rlon = float(autor["lat"]), float(autor["lon"])
        dist_m = gc.haversine_km(lat, lon, rlat, rlon) * 1000.0
        figs.append({"k": k, "n": n, "lat": lat, "lon": lon, "prec": float(ev.get("precisao_m") or 0),
                     "rlat": rlat, "rlon": rlon, "rprec": float(autor.get("precisao_m") or 0),
                     "ref": "residência do autor",
                     "dist": rotulo_dist(dist_m),
                     "paineis": legendas_paineis(k, ev, autor, dist_m)})
    return figs
