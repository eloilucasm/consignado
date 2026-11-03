"""Recolhe da fonte oficial as normas do acervo que hoje estão no nível FEITO e confere contra o acervo.

Fase 1 (regressão): baixa cada fonte, converte para o formato do acervo, grava em `--saida` e compara,
palavra a palavra, com o arquivo atual de `_acervo/normas`. Veredito por norma:

    APROVADA   texto igual ao acervo (TEXTO=0, ESTRUT=0, SUB=0, SOBRE=0)
    REPROVADA  há diferença; o relatório `<norma>.diferencas.txt` lista todas e deve ser lido
    ERRO       a fonte não pôde ser obtida/lida (rede, 403, PDF escaneado)
    PENDENTE   a fonte ainda não tem implementação (ex.: API do Banco Central)

Código de saída: 1 se houver REPROVADA ou ERRO; 0 caso contrário (`--estrito` conta PENDENTE como falha).
Nunca escreve em `_acervo`. Cada execução grava `manifesto.json` (URL, HTTP, Last-Modified, sha256).

Este comparador mede igualdade com o acervo, NÃO a correção do acervo: a norma só sobe de FEITO para
VERIFICADO com segunda fonte independente (`--secundaria`, ainda não implementada para as fontes pendentes).
O coletor também não certifica vigência: registra texto e data da fonte.

    python -I coletar_pdf.py --saida ../../../_coleta-pdf                     # todas
    python -I coletar_pdf.py --saida ../../../_coleta-pdf res-cmn-4549-consolidada
    python -I coletar_pdf.py --saida ... --local in-inss-138-2022-consolidada=C:/dl/in138.pdf
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import auditar_conversao  # noqa: E402
sys.stdout.reconfigure(encoding="utf-8")  # console do Windows grava cp1252 por padrão
from fontes import (BcbApi, DouHtml, FonteErro, FontePendente, PdfHttp, PdfLocal, Rede)  # noqa: E402

ACERVO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_acervo", "normas"))
BCB = "https://normativos.bcb.gov.br/Lists/Normativos/Attachments/"
INSS = "https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/"

# arquivo -> (fonte primária, segunda fonte ou None). A segunda fonte alimenta o nível VERIFICADO.
ALVOS = {
    "res-cmn-4549-consolidada": (PdfHttp(BCB + "50330/Res_4549_v2_L.pdf"), BcbApi("Resolução CMN", 4549)),
    "res-cmn-4753-consolidada": (PdfHttp(BCB + "50847/Res_4753_v3_L.pdf"), BcbApi("Resolução CMN", 4753)),
    "res-cmn-3954-original": (PdfHttp(BCB + "49450/Res_3954_v1_O.pdf"), BcbApi("Resolução CMN", 3954)),
    "in-inss-138-2022-consolidada": (
        PdfHttp(INSS + "instrucao-normativa/2022/in138pres-inss-alterada19-5-2026.pdf"), DouHtml("(DOU 11/11 e 13/12/2022)")),
    "in-inss-28-2008-consolidada-2020": (
        PdfHttp(INSS + "legado/in28PRESINSSatualizada22.07.2020.pdf"), DouHtml("(DOU 19/5/2008)")),
    "res-cmn-4935": (BcbApi("Resolução CMN", 4935, id_portal=51464), None),
    "res-bcb-96-2021": (BcbApi("Resolução BCB", 96, id_portal=51384), None),
    "in-inss-143-2023": (DouHtml("https://www.in.gov.br/web/dou/-/instrucao-normativa-pres/inss-n-143-de-10-de-fevereiro-de-2023-463867770"), None),
}


def titulo_do_acervo(arquivo):
    caminho = os.path.join(ACERVO, arquivo + ".md")
    if os.path.isfile(caminho):
        with open(caminho, encoding="utf-8") as f:
            primeira = f.readline().strip()
        if primeira.startswith("# "):
            return primeira
    return "# " + arquivo


def cabecalho(arquivo, doc):
    return (f"{titulo_do_acervo(arquivo)}\n\n> Fonte: <{doc.url}>\n"
            f"> Coletado em {doc.obtido_em} · HTTP {doc.http} · Last-Modified: {doc.last_modified or '—'} · sha256: {doc.sha256}\n"
            f"> Gerado por coletar_pdf.py; este arquivo é preparo e não substitui o do acervo.\n\n")


def palavras_arquivo(texto):
    return auditar_conversao.palavras_md(texto, acervo=True)


def conferir(texto_novo, arquivo):
    """Compara com o acervo. Devolve (achados, palavras_ref, palavras_novas, iguais) ou None se o acervo não tem o arquivo."""
    caminho = os.path.join(ACERVO, arquivo + ".md")
    if not os.path.isfile(caminho):
        return None
    with open(caminho, encoding="utf-8") as f:  # UTF-8 estrito
        ref = palavras_arquivo(f.read())
    novo = palavras_arquivo(texto_novo)
    achados, iguais = auditar_conversao.comparar(ref, novo)
    return achados, len(ref), len(novo), iguais


def relatorio(achados):
    linhas = []
    for cat, itens in achados.items():
        for desc, ctx in itens:
            linhas.append(f"{cat:6} {desc}\n       ...{ctx}")
    return "\n".join(linhas) + ("\n" if linhas else "")


def processar(arquivo, primaria, rede, saida, local):
    reg = {"arquivo": arquivo, "fonte": primaria.tipo}
    try:
        if arquivo in local:
            primaria = PdfLocal(local[arquivo], primaria.url)
            reg["fonte"] = "pdf-local"
        doc = primaria.obter(rede)
        reg["documento"] = doc.meta()
        corpo = primaria.extrair(doc)
    except FontePendente as e:
        reg.update(veredito="PENDENTE", motivo=str(e))
        return reg
    except (FonteErro, OSError, UnicodeDecodeError) as e:
        reg.update(veredito="ERRO", motivo=str(e))
        return reg
    os.makedirs(os.path.join(saida, "_fonte"), exist_ok=True)
    with open(os.path.join(saida, "_fonte", arquivo + ".pdf"), "wb") as f:
        f.write(doc.bruto)
    texto = cabecalho(arquivo, doc) + corpo + "\n"
    with open(os.path.join(saida, arquivo + ".md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    res = conferir(texto, arquivo)
    if res is None:
        reg.update(veredito="ERRO", motivo="arquivo não existe em _acervo/normas")
        return reg
    achados, n_ref, n_novo, iguais = res
    reg["palavras"] = {"acervo": n_ref, "coletado": n_novo, "iguais": iguais}
    reg["achados"] = {k: len(v) for k, v in achados.items()}
    ruim = any(achados.values())
    reg["veredito"] = "REPROVADA" if ruim else "APROVADA"
    if ruim:
        with open(os.path.join(saida, arquivo + ".diferencas.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write(relatorio(achados))
    return reg


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivos", nargs="*", help="nomes de ALVOS (padrão: todos)")
    ap.add_argument("--saida", required=True, help="pasta de preparo; nunca use _acervo")
    ap.add_argument("--local", action="append", default=[], metavar="NORMA=ARQUIVO.pdf",
                    help="usa um PDF já baixado (fonte que bloqueia cliente automatizado)")
    ap.add_argument("--rps", type=float, default=0.5)
    ap.add_argument("--estrito", action="store_true", help="PENDENTE também falha")
    a = ap.parse_args()
    if os.path.abspath(a.saida).startswith(ACERVO):
        ap.error("--saida não pode ficar dentro de _acervo/normas")
    local = dict(x.split("=", 1) for x in a.local)
    desconhecidos = [n for n in [*a.arquivos, *local] if n not in ALVOS]
    if desconhecidos:
        ap.error(f"norma fora de ALVOS: {desconhecidos}")
    os.makedirs(a.saida, exist_ok=True)
    rede = Rede(a.rps)
    regs = []
    for arq, (prim, _sec) in ALVOS.items():
        if a.arquivos and arq not in a.arquivos:
            continue
        r = processar(arq, prim, rede, a.saida, local)
        regs.append(r)
        det = r.get("motivo") or (f"palavras acervo={r['palavras']['acervo']} coletado={r['palavras']['coletado']} "
                                  + " ".join(f"{k}={v}" for k, v in r["achados"].items()))
        print(f"{r['veredito']:9} {arq}: {det[:200]}", flush=True)
    with open(os.path.join(a.saida, "manifesto.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(regs, f, ensure_ascii=False, indent=2)
    cont = {v: sum(1 for r in regs if r["veredito"] == v) for v in ("APROVADA", "REPROVADA", "ERRO", "PENDENTE")}
    print("\nResumo: " + " ".join(f"{k}={v}" for k, v in cont.items()))
    print("RESULTADO: " + ("REPROVADO" if cont["REPROVADA"] or cont["ERRO"] or (a.estrito and cont["PENDENTE"]) else "APROVADO"))
    return 1 if cont["REPROVADA"] or cont["ERRO"] or (a.estrito and cont["PENDENTE"]) else 0


if __name__ == "__main__":
    sys.exit(main())
