#!/usr/bin/env python3
"""ip_check.py - classificação de endereços IP de logs (VF4 e VF9, Regra 16).

O script NÃO localiza ninguém por IP e NÃO conclui por distância. Ele responde
a perguntas que o advogado precisa fazer ao ler o log:
  1. O IP é público ou de rede interna, CGNAT, loopback, reservado?  (offline)
  2. Quem é o titular do bloco? Provedor residencial, móvel, hospedagem/VPN?  (RDAP, opcional)

O RDAP (RFC 7480) é a consulta pública e gratuita aos registros regionais
(LACNIC para o Brasil). Vem ligado por padrão; --sem-rdap desliga, porque a
consulta envia o IP ao registro público do bloco. Se a rede bloquear, o script
segue com a classificação offline e avisa.
O titular do bloco não é o titular da linha: o provedor identifica o assinante
só mediante ordem judicial. Também vale lembrar que o mesmo IP muda de assinante
ao longo do tempo; sempre cite a data e a hora do log.

Uso:
    python3 ip_check.py 177.10.20.30 10.0.0.5
    python3 ip_check.py --entrada caso.json --saida-md ip.md
    python3 ip_check.py --entrada caso.json --sem-rdap

Entrada JSON: o mesmo arquivo do geo_check.py (lê eventos[].ip e eventos[].datahora).
Sem dependências além da biblioteca padrão.
"""
import argparse
import ipaddress
import json
import sys
import urllib.error
import urllib.request

RDAP_PADRAO = "https://rdap.org/ip/{ip}"   # redireciona ao registro regional correto
ROTULO_REVISAO = "REVISÃO HUMANA OBRIGATÓRIA"

# Palavras no nome do titular que sugerem hospedagem, nuvem ou VPN. Lista aberta, editar à vontade.
PALAVRAS_HOSPEDAGEM = [
    "amazon", "aws", "google cloud", "google llc", "microsoft", "azure", "digitalocean", "ovh",
    "hetzner", "linode", "vultr", "cloudflare", "oracle", "hosting", "hospedagem", "datacenter",
    "data center", "vpn", "proxy", "tor exit", "colocation", "servidor", "cloud",
]


_DOC_NETS = [ipaddress.ip_network(n) for n in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24", "2001:db8::/32")]


def classifica_offline(txt):
    """Retorna (classe, explicação). Classes: PUBLICO, REDE_INTERNA, CGNAT, LOOPBACK, RESERVADO, INVALIDO."""
    try:
        a = ipaddress.ip_address(str(txt).strip())
    except ValueError:
        return "INVALIDO", "Não é um endereço IP válido. Conferir a transcrição do log."
    if any(a in n for n in _DOC_NETS if n.version == a.version):
        return "RESERVADO", "Faixa de documentação (RFC 5737/3849): não é IP real. Conferir a transcrição do log."
    if a.is_loopback:
        return "LOOPBACK", "Endereço de loopback: registro de teste ou de proxy local do réu."
    if a.version == 4 and a in ipaddress.ip_network("100.64.0.0/10"):
        return "CGNAT", ("Faixa 100.64.0.0/10 (CGNAT): compartilhada por muitos clientes da operadora. "
                         "Não indica local e dificulta identificar o assinante.")
    if a.is_private:
        return "REDE_INTERNA", "Faixa privada: endereço interno do réu ou de intermediário. Pedir o IP público da sessão."
    if a.is_link_local or a.is_reserved or a.is_multicast or a.is_unspecified:
        return "RESERVADO", "Faixa reservada ou especial: não roteável na internet pública."
    return "PUBLICO", "Endereço público. A localização por IP é aproximada (Regra 16)."


def consulta_rdap(ip, modelo_url, timeout):
    url = modelo_url.format(ip=ip)
    req = urllib.request.Request(url, headers={"Accept": "application/rdap+json, application/json",
                                               "User-Agent": "ip_check/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        dados = json.loads(r.read().decode("utf-8", "replace"))
    nomes = []
    for ent in dados.get("entities", []) or []:
        vcard = ent.get("vcardArray")
        if vcard and len(vcard) > 1:
            for campo in vcard[1]:
                if campo and campo[0] == "fn":
                    nomes.append(campo[3])
    inicio, fim = dados.get("startAddress"), dados.get("endAddress")
    cidr = None
    if dados.get("cidr0_cidrs"):
        c = dados["cidr0_cidrs"][0]
        cidr = f"{c.get('v4prefix') or c.get('v6prefix')}/{c.get('length')}"
    return {
        "nome_bloco": dados.get("name"),
        "pais": dados.get("country"),
        "faixa": cidr or (f"{inicio} - {fim}" if inicio else None),
        "tipo": dados.get("type"),
        "entidades": nomes,
        "handle": dados.get("handle"),
    }


def sugere_hospedagem(info):
    texto = " ".join(str(x).lower() for x in [info.get("nome_bloco")] + list(info.get("entidades") or []) if x)
    return [p for p in PALAVRAS_HOSPEDAGEM if p in texto]


def processa(itens, usar_rdap, modelo, timeout):
    saida = []
    cache = {}
    for it in itens:
        ip = it["ip"]
        classe, expl = classifica_offline(ip)
        r = {"evento": it.get("evento"), "ip": ip, "datahora": it.get("datahora"),
             "classe": classe, "explicacao": expl, "rdap": None, "erro_rdap": None,
             "revisao": classe == "INVALIDO"}
        if usar_rdap and classe == "PUBLICO":
            if ip not in cache:
                try:
                    cache[ip] = (consulta_rdap(ip, modelo, timeout), None)
                except (urllib.error.URLError, OSError, ValueError, json.JSONDecodeError) as e:
                    cache[ip] = (None, str(e))
            r["rdap"], r["erro_rdap"] = cache[ip]
            if r["rdap"]:
                pal = sugere_hospedagem(r["rdap"])
                r["sugere_hospedagem_ou_vpn"] = pal
                pais = (r["rdap"].get("pais") or "").upper()
                if pais and pais != "BR":
                    r["revisao"] = True
                    r["explicacao"] += f" Titular do bloco registrado fora do Brasil ({pais})."
                if pal:
                    r["revisao"] = True
                    r["explicacao"] += " Nome do titular sugere hospedagem, nuvem ou VPN: conferir."
            else:
                r["explicacao"] += " Consulta RDAP indisponível (rede bloqueada ou falha); titular do bloco não verificado."
        saida.append(r)
    return saida


def para_markdown(res, usou_rdap):
    L = ["# Classificação de IPs (VF4/VF9)\n"]
    n = sum(1 for r in res if r["revisao"])
    if n:
        L.append(f'<span style="color:red">**ATENÇÃO: {n} ITEM(NS) COM {ROTULO_REVISAO}.**</span>\n')
    L.append("IP não prova local nem autoria (Regra 16). O titular do bloco não é o titular da linha. "
             "Cite sempre a data e a hora do log.\n")
    if not usou_rdap:
        L.append("Consulta RDAP não executada (--sem-rdap). Só a classificação offline consta abaixo.\n")
    L.append("| Evento | IP | Data/hora | Classe | Titular do bloco (RDAP) | Observação |")
    L.append("|---|---|---|---|---|---|")
    for r in res:
        rd = r["rdap"]
        tit = ""
        if rd:
            tit = f"{rd.get('nome_bloco') or ''} ({rd.get('pais') or '?'}); {rd.get('faixa') or ''}; {', '.join(rd.get('entidades') or [])}"
        elif r["erro_rdap"]:
            tit = f"falha na consulta: {r['erro_rdap']}"
        obs = r["explicacao"]
        if r["revisao"]:
            obs = f'<span style="color:red">**{ROTULO_REVISAO}**</span> {obs}'
        L.append(f"| {r['evento'] or ''} | {r['ip']} | {r['datahora'] or ''} | {r['classe']} | {tit} | {obs} |")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Classificação de IPs com RDAP opcional.")
    ap.add_argument("ips", nargs="*", help="endereços IP")
    ap.add_argument("--entrada", help="JSON do geo_check.py (lê eventos[].ip)")
    ap.add_argument("--rdap", action="store_true", help=argparse.SUPPRESS)  # compatibilidade: já é o padrão
    ap.add_argument("--sem-rdap", action="store_true", help="não consulta o RDAP (nada sai da máquina)")
    ap.add_argument("--rdap-url", default=RDAP_PADRAO, help="modelo de URL com {ip}")
    ap.add_argument("--timeout", type=float, default=10.0)
    ap.add_argument("--saida-json")
    ap.add_argument("--saida-md")
    a = ap.parse_args()

    itens = [{"ip": x} for x in a.ips]
    if a.entrada:
        try:
            with open(a.entrada, encoding="utf-8") as f:
                d = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Erro ao ler a entrada: {e}", file=sys.stderr)
            return 2
        for i, ev in enumerate(d.get("eventos", []), 1):
            if ev.get("ip"):
                itens.append({"evento": i, "ip": ev["ip"], "datahora": ev.get("datahora")})
    if not itens:
        print("Nenhum IP informado.", file=sys.stderr)
        return 2

    usar_rdap = not a.sem_rdap
    res = processa(itens, usar_rdap, a.rdap_url, a.timeout)
    n = sum(1 for r in res if r["revisao"])
    if n:
        msg = f"ATENÇÃO: {n} ITEM(NS) COM {ROTULO_REVISAO}."
        print(f"\033[1;31m{msg}\033[0m" if sys.stderr.isatty() else msg, file=sys.stderr)
    if a.saida_json:
        with open(a.saida_json, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
    md = para_markdown(res, usar_rdap)
    if a.saida_md:
        with open(a.saida_md, "w", encoding="utf-8") as f:
            f.write(md)
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
