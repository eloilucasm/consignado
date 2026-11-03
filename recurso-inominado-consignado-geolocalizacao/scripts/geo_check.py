#!/usr/bin/env python3
"""
geo_check.py - Verificação VF9 (geolocalização em contratos).

Python puro (biblioteca padrão). Não acessa a internet e não envia nenhum
dado para fora. Só calcula sobre o que recebe no JSON de entrada. As imagens
(Figuras Ilustrativas) saem de outro script, o geo_figuras.py, que usa a rede.

Uso:
    python3 geo_check.py entrada.json
    python3 geo_check.py entrada.json                            (usa a malha da Bahia da skill)
    python3 geo_check.py entrada.json --municipios malha.geojson (outra malha, GeoJSON)
    python3 geo_check.py entrada.json --saida-json resultado.json --saida-md quadro.md

Entrada: ver exemplo_entrada.json.
Saída: quadro em Markdown (stdout ou arquivo) e, opcionalmente, JSON.

Referência única: a residência do autor. Não há ponto de venda do réu como
segundo referencial (os autos normalmente não trazem esse endereço).

PRESSUPOSTO DA SKILL: localização distante da casa do autor, no log do réu, indica
fraude, e cabe ao banco provar o contrário (ônus de quem juntou o documento).
O script aponta a inconsistência; não pondera a "força" da fonte.

Só há duas conclusões possíveis: COMPATIVEL e DIVERGENTE.
  COMPATIVEL  GPS dentro do raio da residência (RAIO_RESIDENCIA_M), já
              descontada a precisão.
  DIVERGENTE  GPS fora do limite local (LIMITE_LOCAL_M), MESMO DENTRO DA MESMA
              CIDADE; município diferente; GPS fisicamente incompatível entre
              si; ou ponto de GPS fixo, recorrente e fora da residência.
  IP ou fonte não identificada: DIVERGENTE acima de LIMITE_IP_KM (5 km) ou em
  outro município; abaixo disso, INFORMATIVO (aproximação normal do IP, que
  quase nunca cai na casa nem na mesma cidade). Nunca COMPATIVEL.
Fontes de coordenada aceitas em fonte_geo: GPS, REDE (Wi-Fi, torre de celular
ou "localização de rede"), IP e DECLARADO. REDE conclui como o GPS, mas só se o
log informar precisao_m, e a margem de precisão é dobrada (FATOR_PRECISAO_REDE).
Tudo o que não se enquadra nessas faixas NÃO É CONCLUÍDO pelo script: sai
marcado como REVISÃO HUMANA OBRIGATÓRIA (caixa alta, vermelho no quadro e no
aviso final). Isso vale para dado ausente ou inválido, fonte IP ou não
identificada, faixa entre o raio e o limite local e incompatibilidades só
possíveis por avião. Um achado marcado assim nunca pode ir para a peça sem
decisão do advogado.
INFORMATIVO é só contexto (mesma cidade; ponto recorrente na própria
residência): não conclui nada. Coincidência de cidade não afasta divergência
local, porque a fraude pode ter sido operada em loja do próprio município.
Geolocalização por IP nunca gera COMPATIVEL nem DIVERGENTE por distância; só
a Cidade-UF do log diferente do domicílio gera DIVERGENTE de município, com a
ressalva da fonte.
A precisão do GPS (campo opcional precisao_m, no evento e no autor) é
descontada nos limites.

INDICADORES SEM COORDENADA. Muitos logs não trazem GPS e cada banco registra
campos diferentes, que mudam com o tempo. Por isso o script faz um inventário:
  - checagens automáticas: IP de rede interna (RFC 1918), CGNAT, fuso do
    aparelho, DDD do telefone x UF do domicílio, horário atípico, intervalo
    curto entre etapas e dispositivo repetido;
  - campos livres (lista "indicadores" no evento ou no topo do JSON), cruzados
    com scripts/catalogo_indicadores.json, que traz a pergunta de verificação
    de cada tipo de campo e pode ser editado sem mexer no código;
  - campo que não está no catálogo vira REVISÃO HUMANA OBRIGATÓRIA e deve ser
    proposto para inclusão no catálogo.
Cada item pode receber "avaliacao" (INDICIO_FORTE, INDICIO_MEDIO, REFORCO ou
SEM_RELEVANCIA) depois de lido nos autos; sem avaliação, fica em revisão.
Indício isolado e fraco não prova nada: vale a convergência de vários.
"""

import argparse
import ipaddress
import json
import math
import os
import re
import sys
from datetime import datetime

RAIO_TERRA_KM = 6371.0088

# Limites de plausibilidade (ajustáveis por --vel-max-kmh).
VEL_MAX_KMH_PADRAO = 900.0       # avião comercial (acima disso: impossível)
VEL_TERRESTRE_KMH = 120.0        # deslocamento terrestre plausível
RAIO_RESIDENCIA_M = 100.0        # GPS até 100 m da residência: compatível (definido pelo advogado)
LIMITE_LOCAL_M = 150.0           # GPS a mais de 150 m da residência: divergente, mesmo na cidade (definido pelo advogado)
ROTULO_REVISAO = "REVISÃO HUMANA OBRIGATÓRIA"
LIMITE_IP_KM = 5.0               # IP ou fonte não identificada: acima disso é DIVERGENTE (definido pelo advogado)
NOTA_REDACAO = ("Redigir como 'o log juntado pelo réu registra', sem afirmar a fonte nem a posição da parte autora; "
                "o ônus de explicar o ponto é do banco.")
MARGEM_PONTO_NA_BORDA_KM = 1.0   # tolerância de borda de município
FATOR_PRECISAO_REDE = 2.0        # localização por Wi-Fi/torre: margem de precisão dobrada
INTERVALO_CURTO_S = 30.0         # etapas seguidas em menos de 30 s (PROPOSTA, validar)
HORA_ATIPICA = (0, 5)            # contratação entre 00h e 05h (PROPOSTA, validar)

DDD_UF = {}
for _uf, _ddds in {
    "SP": "11 12 13 14 15 16 17 18 19", "RJ": "21 22 24", "ES": "27 28",
    "MG": "31 32 33 34 35 37 38", "PR": "41 42 43 44 45 46", "SC": "47 48 49",
    "RS": "51 53 54 55", "DF": "61", "GO": "62 64", "TO": "63", "MT": "65 66",
    "MS": "67", "AC": "68", "RO": "69", "BA": "71 73 74 75 77", "SE": "79",
    "PE": "81 87", "AL": "82", "PB": "83", "RN": "84", "CE": "85 88",
    "PI": "86 89", "PA": "91 93 94", "AM": "92 97", "RR": "95", "AP": "96",
    "MA": "98 99",
}.items():
    for _d in _ddds.split():
        DDD_UF[_d] = _uf

_SINONIMOS_FONTE = {
    "GPS": {"gps", "gnss"},
    "REDE": {"rede", "wifi", "wi-fi", "wi fi", "torre", "celular", "cell", "network",
             "tower", "erb", "rede movel", "localizacao de rede", "localizacao por rede",
             "wifi/torre", "wi-fi/torre"},
    "IP": {"ip", "geoip", "geo ip", "por ip", "endereco ip"},
    "DECLARADO": {"declarado", "informado", "manual", "endereco informado"},
}


# ---------------------------------------------------------------- utilidades

def valida_coordenada(lat, lon):
    """Retorna (ok, motivo)."""
    if lat is None or lon is None:
        return False, "coordenada ausente"
    try:
        lat = float(lat)
        lon = float(lon)
    except (TypeError, ValueError):
        return False, "coordenada não numérica"
    if not (-90 <= lat <= 90):
        return False, "latitude fora de -90..90"
    if not (-180 <= lon <= 180):
        return False, "longitude fora de -180..180"
    if lat == 0 and lon == 0:
        return False, "coordenada 0,0 (valor padrão de erro)"
    # Brasil: lat ~ +5,3 a -33,8 ; lon ~ -74 a -28,8
    if not (-34.0 <= lat <= 6.0 and -74.5 <= lon <= -28.0):
        return True, "fora do território brasileiro (conferir o dado)"
    return True, ""


def haversine_km(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = p2 - p1
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * RAIO_TERRA_KM * math.asin(math.sqrt(a))


def parse_dt(txt):
    """Aceita ISO 8601 com fuso. Sem fuso => retorna naive (sinalizado)."""
    if not txt:
        return None
    try:
        return datetime.fromisoformat(txt)
    except ValueError:
        return None


def ponto_em_anel(lat, lon, anel):
    """Ray casting. anel = lista de [lon, lat]."""
    dentro = False
    n = len(anel)
    j = n - 1
    for i in range(n):
        xi, yi = anel[i][0], anel[i][1]
        xj, yj = anel[j][0], anel[j][1]
        if (yi > lat) != (yj > lat):
            x_cruza = (xj - xi) * (lat - yi) / (yj - yi) + xi
            if lon < x_cruza:
                dentro = not dentro
        j = i
    return dentro


def ponto_em_poligono(lat, lon, poligono):
    """poligono = [anel_externo, buraco1, ...] (formato GeoJSON)."""
    if not poligono:
        return False
    if not ponto_em_anel(lat, lon, poligono[0]):
        return False
    for buraco in poligono[1:]:
        if ponto_em_anel(lat, lon, buraco):
            return False
    return True


def distancia_ponto_anel_km(lat, lon, anel):
    """Distância aproximada do ponto ao vértice mais próximo do anel (km).
    Serve só para tolerância de borda; não é distância exata ao segmento."""
    return min(haversine_km(lat, lon, p[1], p[0]) for p in anel)


def carrega_malha(caminho):
    """GeoJSON FeatureCollection. Cada feature deve ter properties com
    'nome' (ou 'NM_MUN') e 'uf' (ou 'SIGLA_UF'), geometria Polygon/MultiPolygon.
    Retorna lista de dicts {nome, uf, poligonos}."""
    with open(caminho, encoding="utf-8") as f:
        gj = json.load(f)
    municipios = []
    for ft in gj.get("features", []):
        props = ft.get("properties", {})
        nome = props.get("nome") or props.get("NM_MUN") or props.get("name")
        uf = props.get("uf") or props.get("SIGLA_UF") or props.get("UF")
        geom = ft.get("geometry") or {}
        if geom.get("type") == "Polygon":
            polys = [geom["coordinates"]]
        elif geom.get("type") == "MultiPolygon":
            polys = geom["coordinates"]
        else:
            continue
        municipios.append({"nome": nome, "uf": uf, "poligonos": polys})
    return municipios


def malha_da_skill():
    """Malha da Bahia que vem na skill (assets/ba_municipios.json, IBGE), no formato de carrega_malha.
    Cada anel vira um polígono próprio (a malha simplificada quase não tem furos). [] se faltar o arquivo."""
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import geo_malha as gm
        return [{"nome": m["n"], "uf": m.get("uf") or "BA", "poligonos": [[a] for a in m["r"]], "skill": True}
                for m in gm.carrega()["municipios"]]
    except Exception:
        return []


def norm(txt):
    if not txt:
        return ""
    import unicodedata
    t = unicodedata.normalize("NFKD", str(txt))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return t.strip().lower()


def ref_de(autor):
    """Rótulo da referência do autor, com preposição: sempre 'da residência'. Decisão do advogado: o ponto de
    assinatura da procuração (feita com o apoio do escritório) é tomado como o local da residência, e na peça
    o ponto se chama sempre 'residência'. O campo antigo autor.referencia_de é ignorado."""
    return "da residência"


def ref_nome(autor):
    r = ref_de(autor)
    for pre in ("do ", "da ", "de "):
        if r.lower().startswith(pre):
            return r[len(pre):]
    return r


def fonte_norm(ev):
    """Normaliza a origem da coordenada: GPS | REDE | IP | DECLARADO | '' (não identificada)."""
    bruto = norm(ev.get("fonte_geo") if isinstance(ev, dict) else ev)
    for chave, sinonimos in _SINONIMOS_FONTE.items():
        if bruto in sinonimos:
            return chave
    return ""


def municipio_do_ponto(lat, lon, malha):
    for m in malha:
        for poly in m["poligonos"]:
            if ponto_em_poligono(lat, lon, poly):
                return m
    return None


def encontra_municipio_por_nome(malha, nome, uf):
    for m in malha:
        if norm(m["nome"]) == norm(nome) and (not uf or norm(m["uf"]) == norm(uf)):
            return m
    return None


def separa_cidade_uf(txt):
    """'Salvador-BA' / 'Salvador - BA' / 'Salvador/BA' -> ('Salvador','BA')."""
    if not txt:
        return None, None
    for sep in ("-", "/", ","):
        if sep in txt:
            cidade, uf = txt.rsplit(sep, 1)
            if len(uf.strip()) == 2:
                return cidade.strip(), uf.strip().upper()
    return txt.strip(), None


# ------------------------------------------------------------------- análise

def analisa_evento_vs_domicilio(ev, autor, malha, vel_unused=None):
    """Compara um evento com o domicílio do autor."""
    achados = []
    fonte = fonte_norm(ev)  # GPS | REDE | IP | DECLARADO | ""
    tem_coord = ev.get("lat") is not None and ev.get("lon") is not None

    # 1. Cidade-UF do log x cidade-UF do domicílio (texto, sem coordenada)
    cid_ev, uf_ev = separa_cidade_uf(ev.get("cidade_uf"))
    cid_au, uf_au = separa_cidade_uf(autor.get("cidade_uf") or autor.get("domicilio_cidade_uf"))
    if cid_ev and cid_au:
        mesma_cidade = norm(cid_ev) == norm(cid_au)
        mesma_uf = (not uf_ev or not uf_au) or norm(uf_ev) == norm(uf_au)
        if mesma_cidade and mesma_uf:
            achados.append(("município (texto do log)", "INFORMATIVO",
                            f"log indica {ev.get('cidade_uf')}; domicílio em {autor.get('cidade_uf')}; "
                            "coincidência de cidade não esclarece o local"))
        else:
            achados.append(("município (texto do log)", "DIVERGENTE",
                            f"log indica {ev.get('cidade_uf')}; domicílio em {autor.get('cidade_uf')}"
                            + ("" if fonte in ("GPS", "REDE") else "; fonte não é GPS")))

    # 2. Coordenada
    if not tem_coord:
        if not any(c == "DIVERGENTE" for _, c, _ in achados):
            achados.append(("coordenada", "REVISAO",
                            "evento sem coordenada: o teste de distância local não pôde ser executado"))
        return achados

    ok, motivo = valida_coordenada(ev.get("lat"), ev.get("lon"))
    if not ok:
        achados.append(("coordenada", "REVISAO", f"coordenada inválida: {motivo}"))
        return achados
    if motivo:
        achados.append(("coordenada", "REVISAO", motivo))

    lat, lon = float(ev["lat"]), float(ev["lon"])

    # 2a. Município por polígono (offline)
    if malha:
        mun_ponto = municipio_do_ponto(lat, lon, malha)
        mun_decl = encontra_municipio_por_nome(malha, cid_au, uf_au) if cid_au else None
        so_ba = bool(malha[0].get("skill"))
        if so_ba and (mun_ponto is None or (cid_au and mun_decl is None)):
            achados.append(("município (polígono)", "INFORMATIVO",
                            "um dos pontos fica fora da Bahia (a malha da skill cobre só a BA); o teste de distância "
                            "e o texto do log decidem"))
        elif mun_ponto is None:
            achados.append(("município (polígono)", "REVISAO",
                            "ponto não cai em nenhum município da malha fornecida (malha incompleta ou ponto fora/na borda)"))
        elif mun_decl is None:
            achados.append(("município (polígono)", "REVISAO",
                            f"ponto cai em {mun_ponto['nome']}-{mun_ponto['uf']}; município do domicílio não localizado na malha"))
        elif mun_ponto is mun_decl:
            achados.append(("município (polígono)", "INFORMATIVO",
                            f"ponto cai dentro de {mun_ponto['nome']}-{mun_ponto['uf']}; "
                            "coincidência de cidade não esclarece o local"))
        else:
            # tolerância de borda
            dist_borda = min(
                distancia_ponto_anel_km(lat, lon, poly[0]) for poly in mun_decl["poligonos"]
            )
            if dist_borda <= MARGEM_PONTO_NA_BORDA_KM:
                achados.append(("município (polígono)", "REVISAO",
                                f"ponto cai em {mun_ponto['nome']}-{mun_ponto['uf']}, a cerca de {dist_borda:.1f} km do limite de {mun_decl['nome']}; precisão do dado não permite concluir"))
            else:
                achados.append(("município (polígono)", "DIVERGENTE",
                                f"ponto cai em {mun_ponto['nome']}-{mun_ponto['uf']}, não em {mun_decl['nome']}-{mun_decl['uf']}"
                                + ("" if fonte in ("GPS", "REDE") else "; fonte não é GPS")))

    # 2b. Distância ao domicílio
    if autor.get("lat") is not None and autor.get("lon") is not None:
        oka, mota = valida_coordenada(autor["lat"], autor["lon"])
        if not oka:
            achados.append(("distância ao domicílio", "REVISAO",
                            f"coordenada do domicílio inválida: {mota}"))
        else:
            d = haversine_km(lat, lon, float(autor["lat"]), float(autor["lon"]))
            if fonte == "GPS":
                d_m = d * 1000.0
                prec_ev = ev.get("precisao_m")
                prec_au = autor.get("precisao_m")
                p = float(prec_ev or 0) + float(prec_au or 0)
                aviso_prec = ("" if prec_ev is not None
                              else "; precisão do GPS não informada no log (considerada 0 m)")
                dist_txt = f"{d_m:.0f} m" if d_m < 10000 else f"{d_m/1000:.1f} km"
                base = (f"{dist_txt} {ref_de(autor)} (fonte GPS; raio de residência {RAIO_RESIDENCIA_M:.0f} m, "
                        f"limite local {LIMITE_LOCAL_M:.0f} m, margem de precisão {p:.0f} m){aviso_prec}")
                if d_m - p > LIMITE_LOCAL_M:
                    achados.append(("distância ao domicílio", "DIVERGENTE", base))
                elif d_m + p <= RAIO_RESIDENCIA_M:
                    achados.append(("distância ao domicílio", "COMPATIVEL", base))
                else:
                    achados.append(("distância ao domicílio", "REVISAO",
                                    base + "; faixa entre o raio e o limite local: o script não conclui"))
            elif fonte == "REDE":
                d_m = d * 1000.0
                prec_ev = ev.get("precisao_m")
                if prec_ev is None:
                    achados.append(("distância ao domicílio", "REVISAO",
                                    f"{d_m:.0f} m (fonte REDE: Wi-Fi ou torre); o log não informa a precisão, "
                                    "então o script não conclui"))
                else:
                    p = FATOR_PRECISAO_REDE * float(prec_ev) + float(autor.get("precisao_m") or 0)
                    dist_txt = f"{d_m:.0f} m" if d_m < 10000 else f"{d_m/1000:.1f} km"
                    base = (f"{dist_txt} {ref_de(autor)} (fonte REDE: Wi-Fi ou torre; raio de residência "
                            f"{RAIO_RESIDENCIA_M:.0f} m, limite local {LIMITE_LOCAL_M:.0f} m, margem de precisão "
                            f"{p:.0f} m, com a precisão da rede multiplicada por {FATOR_PRECISAO_REDE:.0f})")
                    if d_m - p > LIMITE_LOCAL_M:
                        achados.append(("distância ao domicílio", "DIVERGENTE", base))
                    elif d_m + p <= RAIO_RESIDENCIA_M:
                        achados.append(("distância ao domicílio", "COMPATIVEL", base))
                    else:
                        achados.append(("distância ao domicílio", "REVISAO",
                                        base + "; faixa entre o raio e o limite local: o script não conclui"))
            else:
                rot = "fonte IP" if fonte == "IP" else (
                    "fonte declarada" if fonte == "DECLARADO" else "fonte não identificada no log")
                if d > LIMITE_IP_KM:
                    achados.append(("distância ao domicílio", "DIVERGENTE",
                                    f"{d:.1f} km {ref_de(autor)} ({rot}; limite {LIMITE_IP_KM:.0f} km para fonte sem precisão)"))
                else:
                    achados.append(("distância ao domicílio", "INFORMATIVO",
                                    f"{d:.1f} km {ref_de(autor)} ({rot}); até {LIMITE_IP_KM:.0f} km é a aproximação "
                                    "normal de IP, que não conta como divergência nem como compatibilidade"))
    else:
        achados.append(("distância ao domicílio", "REVISAO",
                        "domicílio sem coordenada informada; só foi possível comparar por município"))
    return achados


def analisa_espaco_tempo(eventos, vel_max):
    """Compara todos os pares de eventos com coordenada e horário."""
    res = []
    base = []
    for ev in eventos:
        if ev.get("lat") is None or ev.get("lon") is None:
            continue
        ok, _ = valida_coordenada(ev["lat"], ev["lon"])
        dt = parse_dt(ev.get("datahora"))
        if ok and dt is not None:
            base.append((dt, ev))
    # Não compara naive com aware
    aware = [b for b in base if b[0].tzinfo is not None]
    naive = [b for b in base if b[0].tzinfo is None]
    for grupo, rotulo in ((aware, ""), (naive, " (sem fuso horário no log)")):
        grupo.sort(key=lambda x: x[0])
        # Todos os pares (não só consecutivos): um evento de IP no meio não
        # pode esconder uma incompatibilidade entre dois pontos de GPS.
        pares = [(grupo[i], grupo[j]) for i in range(len(grupo)) for j in range(i + 1, len(grupo))]
        for (t1, e1), (t2, e2) in pares:
            d = haversine_km(float(e1["lat"]), float(e1["lon"]), float(e2["lat"]), float(e2["lon"]))
            horas = (t2 - t1).total_seconds() / 3600.0
            fontes = {fonte_norm(e1), fonte_norm(e2)}
            par = f"{e1.get('tipo')} -> {e2.get('tipo')}"
            if horas <= 0:
                res.append((par, "REVISAO",
                            f"{d:.1f} km; horários iguais ou invertidos (conferir fuso e ordem){rotulo}"))
                continue
            v = d / horas
            base_txt = f"{d:.1f} km em {horas*60:.0f} min ({v:.0f} km/h)"
            impreciso = "IP" in fontes or "" in fontes or "DECLARADO" in fontes
            if v <= VEL_TERRESTRE_KMH:
                if horas > 24:
                    continue  # pares compatíveis separados por mais de um dia só poluem o quadro
                res.append((par, "COMPATIVEL", f"{base_txt}; possível por via terrestre{rotulo}"))
            elif v <= vel_max:
                res.append((par, "REVISAO",
                            f"{base_txt}; só seria possível por via aérea. Verificar se o deslocamento aéreo é plausível no caso concreto{rotulo}"))
            elif impreciso:
                res.append((par, "DIVERGENTE",
                            f"{base_txt}: incompatível com qualquer deslocamento no mesmo fluxo; ao menos um ponto vem de IP ou de fonte não identificada. "
                            f"O log do réu é internamente inconsistente e o ônus de explicar é do banco{rotulo}"))
            else:
                res.append((par, "DIVERGENTE",
                            f"{base_txt}: acima do limite de {vel_max:.0f} km/h; ambos os pontos vêm de GPS ou de rede{rotulo}"))
    if len(aware) and len(naive):
        res.append(("fusos", "REVISAO",
                    "há eventos com e sem fuso horário; não foram comparados entre si"))
    return res


def analisa_recorrencia(eventos, autor):
    """Cruzamento entre eventos: pontos (e IPs) que se repetem em datas ou
    contratos diferentes. Um ponto fixo que se repete e não é a residência
    sugere local de operação, não a rotina do consumidor. Para comparar
    contratos diferentes, informar 'contrato' em cada evento."""
    res = []
    grupos = []  # cada grupo: {"lat","lon","itens":[(i, ev)]}
    for i, ev in enumerate(eventos, 1):
        if ev.get("lat") is None or ev.get("lon") is None:
            continue
        ok, _ = valida_coordenada(ev["lat"], ev["lon"])
        if not ok:
            continue
        lat, lon = float(ev["lat"]), float(ev["lon"])
        for g in grupos:
            if haversine_km(lat, lon, g["lat"], g["lon"]) * 1000.0 <= RAIO_RESIDENCIA_M:
                g["itens"].append((i, ev))
                break
        else:
            grupos.append({"lat": lat, "lon": lon, "itens": [(i, ev)]})

    def dia(ev):
        dt = parse_dt(ev.get("datahora"))
        return dt.date().isoformat() if dt else None

    for g in grupos:
        itens = g["itens"]
        if len(itens) < 2:
            continue
        dias = {dia(e) for _, e in itens if dia(e)}
        contratos = {e.get("contrato") for _, e in itens if e.get("contrato")}
        if len(dias) < 2 and len(contratos) < 2:
            continue
        fontes = {fonte_norm(e) for _, e in itens}
        nums = ", ".join(str(i) for i, _ in itens)
        onde = ""
        fora = None
        if autor.get("lat") is not None and autor.get("lon") is not None:
            oka, _ = valida_coordenada(autor["lat"], autor["lon"])
            if oka:
                dm = haversine_km(g["lat"], g["lon"], float(autor["lat"]), float(autor["lon"])) * 1000.0
                lim_m = LIMITE_LOCAL_M if fontes <= {"GPS", "REDE"} else LIMITE_IP_KM * 1000.0
                fora = dm > lim_m
                onde = f"; a {dm:.0f} m {ref_de(autor)}"
        so_gps = fontes <= {"GPS", "REDE"}
        sessoes = {(dia(e), e.get("contrato") or "") for _, e in itens}
        quando = (f"{len(dias)} dias distintos" if len(dias) > 1 else f"{len(contratos)} contratos distintos")
        det = (f"{len(itens)} eventos ({nums}) em {len(sessoes)} sessão(ões) no mesmo ponto ({quando}){onde}. "
               "As etapas de uma mesma assinatura não são observações independentes: citar as sessões, não os eventos")
        if fora:
            res.append(("ponto recorrente", "DIVERGENTE",
                        det + f"; ponto fixo fora {ref_de(autor)}, repetido em ocasiões diferentes"
                        + ("" if so_gps else ". Fonte não é GPS: pode ser o ponto atribuído ao IP pela plataforma ou local fixo")))
        elif fora is False:
            res.append(("ponto recorrente", "INFORMATIVO", det + f"; dentro da margem {ref_de(autor)}"))
        else:
            res.append(("ponto recorrente", "REVISAO", det + "; sem coordenada do domicílio para comparar"))

    por_ip = {}
    for i, ev in enumerate(eventos, 1):
        if ev.get("ip"):
            por_ip.setdefault(ev["ip"], []).append((i, ev))
    for ip, itens in por_ip.items():
        if len(itens) < 2:
            continue
        dias = {dia(e) for _, e in itens if dia(e)}
        contratos = {e.get("contrato") for _, e in itens if e.get("contrato")}
        if len(dias) < 2 and len(contratos) < 2:
            continue
        nums = ", ".join(str(i) for i, _ in itens)
        res.append(("IP recorrente", "INFORMATIVO",
                    f"IP {ip} nos eventos {nums} em ocasiões diferentes: liga os contratos a uma mesma origem de rede "
                    "(pode ser CGNAT, operadora ou rede do correspondente). Rodar ip_check.py para identificar o titular do bloco; reforço, não prova"))
    return res


# ------------------------------------------------------- indicadores sem coordenada

NIVEIS = ("FORTE", "MEDIO", "REFORCO")
_AVALIACOES = {"INDICIO_FORTE": "FORTE", "INDICIO_MEDIO": "MEDIO", "REFORCO": "REFORCO"}


_DOC_NETS = [ipaddress.ip_network(n) for n in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24", "2001:db8::/32")]


def carrega_catalogo(caminho=None):
    caminho = caminho or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "catalogo_indicadores.json")
    try:
        with open(caminho, encoding="utf-8") as f:
            return json.load(f).get("tipos", [])
    except (OSError, json.JSONDecodeError):
        return []


def casa_catalogo(campo, catalogo):
    c = norm(campo)
    for tipo in catalogo:
        for kw in tipo.get("palavras_chave", []):
            if norm(kw) in c:
                return tipo
    return None


def _offset_horas(txt):
    m = re.search(r"([+-])\s*(\d{1,2})(?::?(\d{2}))?", str(txt or ""))
    if not m:
        return None
    h = int(m.group(2)) + (int(m.group(3) or 0) / 60.0)
    return -h if m.group(1) == "-" else h


def _fuso_esperado(uf):
    if uf == "AC":
        return -5.0
    if uf in ("AM", "RO", "RR", "MT", "MS"):
        return -4.0
    return -3.0


def _item(n, ind, valor, origem, nivel, classe, detalhe):
    return {"evento": n, "indicador": ind, "valor": valor, "origem": origem,
            "nivel": nivel, "classe": classe, "detalhe": detalhe}


def analisa_indicadores(dados, catalogo):
    """Inventário de dados sem coordenada. Classes: INDICIO (com nível), INFORMATIVO, REVISAO."""
    autor = dados.get("autor", {})
    eventos = dados.get("eventos", [])
    _, uf_autor = separa_cidade_uf(autor.get("domicilio"))
    itens = []
    dispositivos = {}
    anterior = None
    for i, ev in enumerate(eventos, 1):
        ip = ev.get("ip")
        if ip:
            try:
                a = ipaddress.ip_address(str(ip).strip())
                if any(a in n for n in _DOC_NETS if n.version == a.version):
                    itens.append(_item(i, "IP de faixa de documentação", ip, "automático", None, "INFORMATIVO",
                                       "Faixa reservada para exemplos (RFC 5737): não é IP real. Conferir a transcrição do log."))
                elif a.is_loopback or a.is_link_local or a.is_private:
                    itens.append(_item(i, "IP de rede interna", ip, "automático", None, "INFORMATIVO",
                                       "Faixa privada (RFC 1918): é endereço interno do réu ou de proxy, não indica local. "
                                       "Pedir o IP público da sessão."))
                elif a.version == 4 and a in ipaddress.ip_network("100.64.0.0/10"):
                    itens.append(_item(i, "IP em faixa CGNAT", ip, "automático", None, "INFORMATIVO",
                                       "Faixa 100.64.0.0/10: compartilhada por vários clientes da operadora; "
                                       "a localização por IP é ainda menos confiável."))
            except ValueError:
                itens.append(_item(i, "IP inválido", ip, "automático", None, "REVISAO",
                                   "O valor não é um endereço IP válido; conferir a transcrição do log."))
        if ev.get("fuso") and uf_autor:
            off = _offset_horas(ev["fuso"])
            if off is not None and abs(off - _fuso_esperado(uf_autor)) >= 0.99:
                itens.append(_item(i, "Fuso do aparelho", ev["fuso"], "automático", "REFORCO", "INDICIO",
                                   f"Fuso difere do esperado para {uf_autor} (UTC{_fuso_esperado(uf_autor):+.0f}). "
                                   "Pode decorrer de configuração do aparelho; serve só como reforço."))
        tel = ev.get("telefone") or ev.get("ddd")
        if tel and uf_autor:
            dig = re.sub(r"\D", "", str(tel))
            if dig.startswith("55") and len(dig) > 11:
                dig = dig[2:]
            ddd = dig[:2] if len(dig) >= 10 else (dig if len(dig) == 2 else "")
            uf_ddd = DDD_UF.get(ddd)
            if uf_ddd and uf_ddd != uf_autor:
                itens.append(_item(i, "DDD do telefone", f"({ddd}) → {uf_ddd}", "automático", "REFORCO", "INDICIO",
                                   f"DDD de {uf_ddd}, e o domicílio do autor é {uf_autor}. "
                                   "Pessoas mudam de estado e mantêm o número; só reforça."))
        dt = parse_dt(ev.get("datahora"))
        if dt and HORA_ATIPICA[0] <= dt.hour < HORA_ATIPICA[1]:
            itens.append(_item(i, "Horário atípico", ev.get("datahora"), "automático", "REFORCO", "INDICIO",
                               f"Evento entre {HORA_ATIPICA[0]:02d}h e {HORA_ATIPICA[1]:02d}h (faixa proposta, a validar)."))
        if dt and anterior and anterior[1]:
            delta = abs((dt - anterior[1]).total_seconds())
            if 0 <= delta < INTERVALO_CURTO_S and anterior[2] != ev.get("tipo"):
                itens.append(_item(i, "Intervalo curto entre etapas", f"{delta:.0f} s", "automático", "REFORCO", "INDICIO",
                                   f"Etapas '{anterior[2]}' e '{ev.get('tipo')}' separadas por menos de "
                                   f"{INTERVALO_CURTO_S:.0f} s (limite proposto, a validar)."))
        anterior = (i, dt, ev.get("tipo"))
        disp = ev.get("dispositivo")
        if disp:
            dispositivos.setdefault(str(disp), set()).add(str(ev.get("contrato") or dados.get("contrato") or ""))
        for ind in ev.get("indicadores", []) or []:
            itens.append(_item_manual(i, ind, catalogo))
    for disp, contratos in dispositivos.items():
        contratos.discard("")
        if len(contratos) > 1:
            itens.append(_item(None, "Dispositivo repetido", disp, "automático", "MEDIO", "INDICIO",
                               f"Mesmo aparelho em {len(contratos)} contratos diferentes: {', '.join(sorted(contratos))}."))
    for ind in dados.get("indicadores", []) or []:
        itens.append(_item_manual(None, ind, catalogo))
    return itens


def _item_manual(n, ind, catalogo):
    campo = ind.get("campo", "")
    valor = ind.get("valor", "")
    tipo = casa_catalogo(campo, catalogo)
    aval = (ind.get("avaliacao") or "").upper()
    if not tipo:
        return _item(n, campo or "(sem nome)", valor, "manual", None, "REVISAO",
                     "Campo fora do catálogo. Ler nos autos, avaliar e propor a inclusão em catalogo_indicadores.json. "
                     + (f"Fonte: {ind['fonte']}." if ind.get("fonte") else ""))
    fonte = f" Fonte: {ind['fonte']}." if ind.get("fonte") else ""
    if aval == "SEM_RELEVANCIA":
        return _item(n, campo, valor, "manual", None, "INFORMATIVO",
                     "Avaliado como sem relevância pelo advogado." + fonte)
    if aval in _AVALIACOES:
        return _item(n, campo, valor, "manual", _AVALIACOES[aval], "INDICIO",
                     tipo["pergunta"] + fonte)
    return _item(n, campo, valor, "manual", None, "REVISAO",
                 "Sem avaliação. Verificar: " + tipo["pergunta"] + fonte)


def processa(dados, malha, vel_max, catalogo=None):
    autor = dados.get("autor", {})
    eventos = dados.get("eventos", [])
    saida = {
        "processo": dados.get("processo"),
        "contrato": dados.get("contrato"),
        "autor": autor,
        "eventos": [],
        "espaco_tempo": [],
        "recorrencia": [],
        "indicadores": [],
        "alertas": [],
    }
    for i, ev in enumerate(eventos, 1):
        achados = analisa_evento_vs_domicilio(ev, autor, malha)
        saida["eventos"].append({
            "n": i,
            "tipo": ev.get("tipo"),
            "fonte_dado": ev.get("fonte"),
            "fonte_geo": ev.get("fonte_geo"),
            "datahora": ev.get("datahora"),
            "cidade_uf": ev.get("cidade_uf"),
            "ip": ev.get("ip"),
            "achados": [{"teste": t, "classe": c, "detalhe": d} for t, c, d in achados],
        })
    for par, cls, det in analisa_espaco_tempo(eventos, vel_max):
        saida["espaco_tempo"].append({"par": par, "classe": cls, "detalhe": det})
    for tipo, cls, det in analisa_recorrencia(eventos, autor):
        saida["recorrencia"].append({"tipo": tipo, "classe": cls, "detalhe": det})

    saida["indicadores"] = analisa_indicadores(dados, catalogo if catalogo is not None else carrega_catalogo())
    cont = {n: sum(1 for x in saida["indicadores"] if x["classe"] == "INDICIO" and x["nivel"] == n) for n in NIVEIS}
    saida["resumo_indicadores"] = cont
    if any(a["classe"] == "INFORMATIVO" for e in saida["eventos"] for a in e["achados"]):
        saida["alertas"].append(
            "Coincidência de município (INFORMATIVO) não afasta divergência: a contratação pode ter sido operada em loja da mesma cidade. "
            "Em escala local, vale a distância do GPS à residência.")
    saida["revisao_humana"] = (
        sum(1 for e in saida["eventos"] for a in e["achados"] if a["classe"] == "REVISAO")
        + sum(1 for r in saida["espaco_tempo"] if r["classe"] == "REVISAO")
        + sum(1 for r in saida["recorrencia"] if r["classe"] == "REVISAO")
        + sum(1 for r in saida["indicadores"] if r["classe"] == "REVISAO"))
    if any(a["classe"] == "DIVERGENTE" and ev_fonte not in ("GPS", "REDE")
           for ev_fonte, e in ((fonte_norm(eventos[x["n"] - 1]), x) for x in saida["eventos"]) for a in e["achados"]):
        saida["alertas"].append(NOTA_REDACAO + " (vale para os itens divergentes de fonte IP, declarada ou não identificada.)")
    if not malha:
        saida["alertas"].append(
            "Sem malha municipal: o teste de ponto em polígono não foi executado (malha da skill ausente; use --municipios).")
    saida["alertas"].append(
        "Resultado é indício de inconsistência, não prova de fraude. Conferir cada dado contra os autos antes de usar na peça.")
    return saida


def fmt_classe(c):
    """REVISAO sai em caixa alta e vermelho (HTML inline, aceito por visualizadores Markdown)."""
    if c == "REVISAO":
        return f'<span style="color:red">**{ROTULO_REVISAO}**</span>'
    if c == "INFORMATIVO":
        return "informativo"
    if c == "INDICIO":
        return "indício"
    return c


def para_markdown(s):
    L = []
    L.append("# Quadro de verificação de geolocalização (VF9)\n")
    n = s.get("revisao_humana", 0)
    if n:
        L.append(f'<span style="color:red">**ATENÇÃO: {n} ACHADO(S) FORA DAS FAIXAS. '
                 f'{ROTULO_REVISAO} ANTES DE QUALQUER USO NA PEÇA.**</span>\n')
    if s.get("processo"):
        L.append(f"Processo: {s['processo']}  ")
    if s.get("contrato"):
        L.append(f"Contrato: {s['contrato']}  ")
    a = s["autor"]
    L.append(f"Domicílio do autor: {a.get('domicilio', 'não informado')} "
             f"(fonte: {a.get('fonte', 'não informada')})\n")
    L.append("## Eventos x domicílio\n")
    L.append("| # | Evento | Fonte do dado (ID/pág.) | Fonte geo | Teste | Classe | Detalhe |")
    L.append("|---|---|---|---|---|---|---|")
    for e in s["eventos"]:
        for ach in e["achados"]:
            L.append(f"| {e['n']} | {e['tipo']} | {e['fonte_dado'] or ''} | {e['fonte_geo'] or ''} | "
                     f"{ach['teste']} | {fmt_classe(ach['classe'])} | {ach['detalhe']} |")
    L.append("\n## Compatibilidade espaço-tempo entre eventos\n")
    if s["espaco_tempo"]:
        L.append("| Par | Classe | Detalhe |")
        L.append("|---|---|---|")
        for r in s["espaco_tempo"]:
            L.append(f"| {r['par']} | {fmt_classe(r['classe'])} | {r['detalhe']} |")
    else:
        L.append("Sem pares de eventos com coordenada e horário válidos.")
    L.append("\n## Cruzamento: pontos e IPs recorrentes\n")
    if s.get("recorrencia"):
        L.append("| Tipo | Classe | Detalhe |")
        L.append("|---|---|---|")
        for r in s["recorrencia"]:
            L.append(f"| {r['tipo']} | {fmt_classe(r['classe'])} | {r['detalhe']} |")
    else:
        L.append("Nenhum ponto ou IP repetido em datas ou contratos diferentes.")
    L.append("\n## Indicadores sem coordenada\n")
    if s.get("indicadores"):
        rs = s.get("resumo_indicadores", {})
        L.append(f"Indícios por nível: FORTE {rs.get('FORTE', 0)}, MÉDIO {rs.get('MEDIO', 0)}, "
                 f"REFORÇO {rs.get('REFORCO', 0)}. Um indício isolado e fraco não prova nada; vale a convergência.\n")
        L.append("| Evento | Indicador | Valor | Origem | Nível | Classe | Detalhe |")
        L.append("|---|---|---|---|---|---|---|")
        for r in s["indicadores"]:
            L.append(f"| {r['evento'] or ''} | {r['indicador']} | {r['valor']} | {r['origem']} | "
                     f"{r['nivel'] or ''} | {fmt_classe(r['classe'])} | {r['detalhe']} |")
    else:
        L.append("Nenhum indicador sem coordenada informado ou detectado.")
    L.append("\n## Alertas\n")
    for al in s["alertas"]:
        L.append(f"- {al}")
    return "\n".join(L) + "\n"


def main():
    global RAIO_RESIDENCIA_M, LIMITE_LOCAL_M
    ap = argparse.ArgumentParser(description="VF9: verificação de geolocalização.")
    ap.add_argument("entrada", help="JSON de entrada")
    ap.add_argument("--municipios", help="GeoJSON da malha municipal (opcional, offline)")
    ap.add_argument("--vel-max-kmh", type=float, default=VEL_MAX_KMH_PADRAO)
    ap.add_argument("--raio-residencia-m", type=float, default=RAIO_RESIDENCIA_M,
                    help="GPS até este raio da residência é COMPATIVEL (padrão 100 m)")
    ap.add_argument("--limite-local-m", type=float, default=LIMITE_LOCAL_M,
                    help="GPS além deste limite é DIVERGENTE, mesmo na cidade (padrão 150 m)")
    ap.add_argument("--catalogo-indicadores", help="JSON do catálogo (padrão: catalogo_indicadores.json ao lado do script)")
    ap.add_argument("--saida-json")
    ap.add_argument("--saida-md")
    args = ap.parse_args()

    if args.raio_residencia_m >= args.limite_local_m:
        print("Erro: --raio-residencia-m deve ser menor que --limite-local-m.", file=sys.stderr)
        sys.exit(2)
    RAIO_RESIDENCIA_M = args.raio_residencia_m
    LIMITE_LOCAL_M = args.limite_local_m

    try:
        with open(args.entrada, encoding="utf-8") as f:
            dados = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Erro ao ler a entrada: {e}", file=sys.stderr)
        sys.exit(2)

    malha = None
    if args.municipios:
        try:
            malha = carrega_malha(args.municipios)
        except (OSError, json.JSONDecodeError, KeyError) as e:
            print(f"Erro ao ler a malha municipal: {e}", file=sys.stderr)
            sys.exit(2)
    else:
        malha = malha_da_skill() or None  # padrão: malha da Bahia que vem na skill

    res = processa(dados, malha, args.vel_max_kmh, carrega_catalogo(args.catalogo_indicadores))

    if args.saida_json:
        with open(args.saida_json, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
    n_rev = res.get("revisao_humana", 0)
    if n_rev:
        msg = f"ATENÇÃO: {n_rev} ACHADO(S) FORA DAS FAIXAS. {ROTULO_REVISAO}."
        if sys.stderr.isatty():
            msg = f"\033[1;31m{msg}\033[0m"
        print(msg, file=sys.stderr)
    md = para_markdown(res)
    if args.saida_md:
        with open(args.saida_md, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        print(md)


if __name__ == "__main__":
    main()
