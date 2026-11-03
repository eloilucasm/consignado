#!/usr/bin/env python3
"""Qualificação do banco réu (CNPJ e endereço) a partir de fonte pública, sem pedir conferência ao advogado.

Caminho: código do banco no extrato do INSS -> BrasilAPI /banks (ISPB, que nos bancos é a raiz do CNPJ) -> CNPJ da matriz
(raiz + 0001 + dígitos verificadores) -> BrasilAPI /cnpj (dados da Receita Federal: razão social, situação, endereço).
Só devolve a qualificação se (1) o CNPJ tem dígitos verificadores válidos, (2) a situação cadastral é ATIVA e (3) a razão
social da Receita bate com o nome do banco no BCB. Falha em qualquer ponto = devolve None e o motivo; nunca inventa.

Uso:
  python buscar_reu.py --codigo 707                  mostra a qualificação obtida
  python buscar_reu.py --cnpj 62232889000190         idem, por CNPJ
  python buscar_reu.py --verificar [reus.json]       confere cada réu do cadastro contra a Receita (só relata)
  python buscar_reu.py --acrescentar 033 218 [...]   imprime as entradas novas no formato de reus.json

Como módulo: resolver(codigo) -> (entrada | None, mensagem).
"""
import json, re, sys, time, unicodedata, urllib.request, urllib.error
import datetime as dt

BASE = "https://brasilapi.com.br/api"


def _get(url, tentativas=3):
    ultimo = None
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "skills-consignado/1.0"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            ultimo = e
        except Exception as e:  # rede fora, timeout
            ultimo = e
        time.sleep(1.5 * (i + 1))
    raise ConnectionError(f"{url}: {ultimo}")


def dv_cnpj(base12):
    n = [int(c) for c in base12]
    p1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    d1 = sum(a * b for a, b in zip(n, p1)) % 11
    d1 = 0 if d1 < 2 else 11 - d1
    p2 = [6] + p1
    d2 = sum(a * b for a, b in zip(n + [d1], p2)) % 11
    d2 = 0 if d2 < 2 else 11 - d2
    return f"{d1}{d2}"


def cnpj_valido(c):
    c = re.sub(r"\D", "", c)
    return len(c) == 14 and c[12:] == dv_cnpj(c[:12])


def fmt_cnpj(c):
    c = re.sub(r"\D", "", c)
    return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"


def _norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().upper()
    s = re.sub(r"\b(S\.?A\.?|S/A|LTDA|BCO|BANCO|CAIXA|ECONOMICA|FEDERAL|FINANCEIRA|CREDITO|FINANCIAMENTO|E|INVESTIMENTO|DE|DO|DA)\b", " ", s)
    return re.sub(r"[^A-Z0-9]+", " ", s).strip()


_ACENTOS = {"Sao": "São", "Conceicao": "Conceição", "America": "América", "Nacoes": "Nações", "Uniao": "União", "Brasilia": "Brasília",
            "Jose": "José", "Joao": "João", "Paulista": "Paulista", "Centro Historico": "Centro Histórico", "Sitio": "Sítio", "Avenida Pres": "Avenida Presidente",
            "Pres": "Presidente", "Gov": "Governador", "Cond": "Condomínio", "Praca": "Praça", "Canada": "Canadá"}


def _acentuar(t):
    for a, b in _ACENTOS.items():
        t = re.sub(r"(?<![A-Za-zÀ-ÿ])" + re.escape(a) + r"(?![A-Za-zÀ-ÿ])", b, t)
    return t


def _titulo(s):
    peq = {"de", "da", "do", "das", "dos", "e"}
    return _acentuar(" ".join(w.lower() if w.lower() in peq else w.capitalize() for w in (s or "").split()))


def qualificar(cnpj, nome_esperado=None):
    """Consulta a Receita (via BrasilAPI). Devolve (entrada, mensagem)."""
    c = re.sub(r"\D", "", cnpj)
    if not cnpj_valido(c):
        return None, f"CNPJ {cnpj} com dígito verificador inválido"
    d = _get(f"{BASE}/cnpj/v1/{c}")
    if not d:
        return None, f"CNPJ {fmt_cnpj(c)} não encontrado na base da Receita"
    sit = (d.get("descricao_situacao_cadastral") or "").upper()
    if sit != "ATIVA":
        return None, f"CNPJ {fmt_cnpj(c)} com situação cadastral {sit or 'desconhecida'}"
    razao = d.get("razao_social") or ""
    if nome_esperado and _norm(nome_esperado)[:8] not in _norm(razao) and _norm(razao)[:8] not in _norm(nome_esperado):
        return None, f"razão social da Receita ({razao}) não bate com o nome do BCB ({nome_esperado})"
    tipo = _acentuar((d.get("descricao_tipo_de_logradouro") or "").title())
    logr = _titulo(d.get("logradouro"))
    num = (d.get("numero") or "").strip()
    cep = re.sub(r"\D", "", d.get("cep") or "")
    end = f"{(tipo + ' ' if tipo and not logr.lower().startswith(tipo.lower()) else '')}{logr}"
    end += f", nº {num}" if num and num.upper() != "S/N" else ", s/nº"
    comp = (d.get("complemento") or "").strip()
    if comp:
        end += f", {_titulo(comp)}"
    end += f", {_titulo(d.get('bairro'))}, {_titulo(d.get('municipio'))}/{d.get('uf')}, CEP {cep[:5]}-{cep[5:]}"
    primeira = razao.split()[0].upper() if razao else ""
    artigo = "do" if primeira in ("BANCO", "BCO", "ITAÚ", "ITAU") else "da"
    entrada = {
        "nome": razao,
        "artigo": artigo,
        "descricao": f"pessoa jurídica de direito privado, inscrito no CNPJ sob o n° {fmt_cnpj(c)}, com endereço na {end}",
        "fonte": f"Receita Federal (CNPJ, situação ATIVA), via BrasilAPI, consulta de {dt.date.today().isoformat()}",
        "cnpj": fmt_cnpj(c),
    }
    return entrada, "ok"


def resolver(codigo):
    """Código do banco (extrato do INSS) -> (entrada | None, mensagem)."""
    cod = str(codigo).strip().lstrip("0") or "0"
    try:
        b = _get(f"{BASE}/banks/v1/{cod}")
    except ConnectionError as e:
        return None, f"sem acesso à rede: {e}"
    if not b or not b.get("ispb"):
        return None, f"código {codigo} não consta da lista de bancos do BCB"
    ispb = re.sub(r"\D", "", str(b["ispb"])).zfill(8)
    base12 = ispb + "0001"
    cnpj = base12 + dv_cnpj(base12)
    try:
        ent, msg = qualificar(cnpj, b.get("fullName") or b.get("name"))
    except ConnectionError as e:
        return None, f"sem acesso à rede: {e}"
    if ent:
        ent["fonte"] += f"; código {str(codigo).zfill(3)} e ISPB {ispb} do BCB"
    return ent, msg


def _cnpj_do_texto(s):
    m = re.search(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", s or "")
    return m.group(0) if m else None


def verificar(caminho):
    reus = json.load(open(caminho, encoding="utf-8"))["reus"]
    problemas = 0
    for cod, r in reus.items():
        c = _cnpj_do_texto(r.get("descricao"))
        if not c:
            print(f"{cod} {r['nome']}: SEM CNPJ na descrição"); problemas += 1; continue
        try:
            ent, msg = qualificar(c, r["nome"])
        except ConnectionError as e:
            print(f"{cod}: sem rede ({e})"); return 2
        if not ent:
            print(f"{cod} {r['nome']} ({c}): {msg}"); problemas += 1; continue
        # compara endereço: CEP e número
        cep_a = re.search(r"CEP ([\d.\- ]{8,11})", r["descricao"]); cep_b = re.search(r"CEP ([\d.\- ]{8,11})", ent["descricao"])
        igual_cep = cep_a and cep_b and re.sub(r"\D", "", cep_a.group(1)) == re.sub(r"\D", "", cep_b.group(1))
        print(f"{cod} {r['nome']} ({c}): CNPJ válido e ATIVO; razão social Receita = {ent['nome']}; CEP {'igual' if igual_cep else 'DIFERENTE'}")
        if not igual_cep:
            print(f"     cadastro : {r['descricao']}\n     Receita  : {ent['descricao']}")
            problemas += 1
        time.sleep(0.4)
    print(f"{problemas} divergência(s) em {len(reus)} réus.")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(0)
    if a[0] == "--verificar":
        sys.exit(verificar(a[1] if len(a) > 1 else "../dados/reus.json"))
    if a[0] == "--cnpj":
        e, m = qualificar(a[1]); print(json.dumps(e, ensure_ascii=False, indent=1) if e else f"NÃO RESOLVIDO: {m}"); sys.exit(0 if e else 1)
    if a[0] in ("--codigo", "--acrescentar"):
        saida, ok = {}, True
        for cod in a[1:]:
            e, m = resolver(cod)
            if e:
                saida[str(cod).zfill(3)] = e
            else:
                ok = False; print(f"# {cod}: NÃO RESOLVIDO: {m}", file=sys.stderr)
            time.sleep(0.4)
        print(json.dumps(saida, ensure_ascii=False, indent=1)); sys.exit(0 if ok else 1)
