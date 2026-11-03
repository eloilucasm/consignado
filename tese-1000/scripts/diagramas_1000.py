#!/usr/bin/env python3
"""diagramas_1000.py - figuras da Tese 1000 a partir do calculo.json (decisão D28, item 14: diagramas como imagem).

Para cada contrato derivado, grava duas imagens PNG:
  fig_anatomia_<n>.png      "Anatomia da reaverbação": contrato-raiz (averbação e exclusão) e contrato derivado
                            (mesmo número-raiz + sufixo), com o intervalo entre a exclusão e a reaverbação
  fig_linha_tempo_<n>.png   "Linha do tempo": averbação da raiz, exclusão, averbação do derivado e período dos descontos
e figuras.json com a legenda de cada imagem, para a peça.

Formato: padrão de figuras do pacote (assets/padrao-figuras.md; desenho em scripts/figuras.py): 17 cm a 300 dpi, fonte mínima
de 9 pt no papel. O rodapé cita o extrato como anexo, sem ID: a figura é da inicial, e o processo ainda não existe.

Os dados vêm só do calculo.json (que vem do extrato do INSS). A figura não introduz fato novo: reproduz o extrato.

Uso:  python3 diagramas_1000.py --calculo calculo.json --saida pasta/figuras
Requer: Pillow (pip install pillow).
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import figuras as fg  # noqa: E402

FONTE = "Fonte: Histórico de Empréstimo Consignado do INSS, anexo. Figura elaborada a partir do extrato; não introduz fato novo."


def data(s):
    if not s:
        return None
    for fmt in ("%d/%m/%Y", "%d/%m/%y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def comp(s):  # MM/AAAA -> primeiro dia do mês
    try:
        m, a = s.split("/")
        return dt.date(int(a), int(m), 1)
    except Exception:
        return None


def intervalo_txt(d):
    n, cat = d.get("intervalo_dias"), d.get("categoria_intervalo")
    if cat == "MESMO_DIA":
        return "reaverbado no mesmo dia da exclusão da raiz"
    if cat == "ANTES_DA_EXCLUSAO":
        return f"averbado {fg.dias(abs(n))} ANTES da exclusão da raiz"
    if n is None:
        return "intervalo não apurado"
    return f"reaverbado {fg.dias(n)} depois da exclusão da raiz"


def anatomia(d, destino):
    im, dr = fg.tela()
    rd = d.get("raiz_dados") or {}
    y = fg.cabecalho(dr, "Anatomia da reaverbação", f"Contrato derivado nº {d['contrato']} sobre o número-raiz {d.get('raiz') or '[raiz não localizada]'}") + fg.P(12)
    y = fg.caixas(dr, y, [
        ("Contrato-raiz", (d.get("raiz") or "não localizado", ""), [
            f"Averbação: {rd.get('averbacao') or '—'}",
            f"Exclusão: {rd.get('exclusao') or '—'}",
            f"Motivo da exclusão: {rd.get('motivo_exclusao') or '—'}",
            f"Banco: {rd.get('banco') or '—'}",
        ]),
        ("Contrato derivado", (d.get("raiz") or d["contrato"], d.get("sufixo") or ""), [
            "Sem nova contratação",
            f"Averbação: {d.get('primeira_averbacao') or d.get('inclusao') or '—'}",
            f"Descontos: {d.get('inicio') or '—'} a {d.get('ate_comp') or d.get('fim') or '—'}",
            f"{fg.parcelas(d.get('qtde', 0))} de {fg.brl(d.get('parcela') or 0)}",
            f"Total descontado: {fg.brl(d.get('total') or 0)}",
        ]),
    ]) + fg.P(10)
    suf = d.get("sufixo") or ""
    nota = f"Mesmo número-raiz, acrescido do sufixo {suf}: {intervalo_txt(d)}." if suf else intervalo_txt(d)[:1].upper() + intervalo_txt(d)[1:] + "."
    y = fg.faixa(dr, y, nota) + fg.P(12)
    return fg.fechar(im, fg.rodape(dr, y, FONTE), destino)


def linha_tempo(d, destino):
    im, dr = fg.tela()
    rd = d.get("raiz_dados") or {}
    y = fg.cabecalho(dr, "Linha do tempo", f"Sequência registrada no extrato do INSS para o contrato derivado nº {d['contrato']}") + fg.P(14)
    ate = d.get("ate_comp") or d.get("fim")
    marcos = [  # (data, é competência (MM/AAAA), rótulo, data como no extrato, cor)
        (data(rd.get("averbacao")), False, "Averbação da raiz", rd.get("averbacao"), fg.AZUL),
        (data(rd.get("exclusao")), False, "Exclusão da raiz", rd.get("exclusao"), fg.AZUL),
        (data(d.get("primeira_averbacao") or d.get("inclusao")), False, "Averbação do derivado", d.get("primeira_averbacao") or d.get("inclusao"), fg.VERMELHO),
        (comp(d.get("inicio")), True, "Primeiro desconto", f"competência {d.get('inicio')}", fg.VERMELHO),
        (comp(ate) if ate != d.get("inicio") else None, True, "Último desconto apurado", f"competência {ate}", fg.VERMELHO),
    ]
    marcos = sorted((m for m in marcos if m[0]), key=lambda m: m[0])  # sort estável: no empate fica a ordem acima
    if len(marcos) < 2:
        y = fg.frase(dr, y, "Datas insuficientes no extrato para a linha do tempo.", fg.VERMELHO) + fg.P(12)
        return fg.fechar(im, fg.rodape(dr, y, FONTE), destino)
    trechos = []
    for a, b in zip(marcos, marcos[1:]):
        t = [fg.entre_datas(a[0], b[0], competencia=a[1] or b[1])]
        descontos = a[2] == "Primeiro desconto" and b[2] == "Último desconto apurado"
        if descontos:
            t.append(f"{fg.parcelas(d.get('qtde', 0))} de {fg.brl(d.get('parcela') or 0)}")
        trechos.append((t, descontos))
    y = fg.linha_tempo(dr, y, [(m[2], m[3], m[4]) for m in marcos], trechos)
    y = fg.frase(dr, y + fg.P(10), intervalo_txt(d) + ".") + fg.P(12)
    return fg.fechar(im, fg.rodape(dr, y, FONTE), destino)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--calculo", required=True)
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    c = json.loads(Path(a.calculo).read_text(encoding="utf-8"))
    s = Path(a.saida)
    s.mkdir(parents=True, exist_ok=True)
    figs = []
    for n, d in enumerate(c.get("derivados", []), 1):
        fa, fl = s / f"fig_anatomia_{n}.png", s / f"fig_linha_tempo_{n}.png"
        anatomia(d, fa)
        linha_tempo(d, fl)
        figs.append({"derivado": d["contrato"], "anatomia": fa.name, "linha_tempo": fl.name,
                     "legenda_anatomia": f"Anatomia da reaverbação do contrato nº {d['contrato']} (número-raiz {d.get('raiz')}).",
                     "legenda_linha_tempo": f"Linha do tempo do contrato nº {d['contrato']}, conforme o extrato do INSS."})
    (s / "figuras.json").write_text(json.dumps({**fg.metadados(), "figuras": figs}, ensure_ascii=False, indent=2),
                                    encoding="utf-8", newline="\n")
    if not fg.FR:
        print("AVISO: nenhuma fonte TrueType encontrada; usada a fonte padrão do Pillow (defina FONTES_DIAGRAMA).")
    print(f"ok: {len(figs) * 2} figura(s) em {s} ({fg.LARGURA_CM} cm a {fg.DPI} dpi; inserir na peça com {fg.LARGURA_CM} cm de largura)")


if __name__ == "__main__":
    main()
