#!/usr/bin/env python3
"""teste_mapa.py - regressão da geolocalização e das figuras (VF9). Não altera a skill.

Confere, com scripts/exemplo_entrada.json, numa pasta temporária:
  1. os SHA-256 dos arquivos congelados do mapa (testes/mapa/congelados.json);
  2. geo_check.py: as classificações de cada evento, a contagem de REVISÃO HUMANA OBRIGATÓRIA e o resumo dos indicadores;
  3. geo_figuras.py --fundo esquema: as imagens de cada evento DIVERGENTE (visão geral 1296 x 480) e o figuras.json
     com paineis, nota_rodape e links das coordenadas;
  4. geo_figuras.py no modo auto, SEM regiao.pmtiles: sai com código 5 (a trava que manda perguntar ao usuário);
  5. se houver regiao.pmtiles (--pmtiles ou na pasta atual) e Playwright: modo auto completo, com as imagens A, B e C
     e completa = true. Sem eles, avisa que B e C não foram testadas (testar no Cowork).

Uso:  python3 testes/mapa/teste_mapa.py [--pmtiles caminho/regiao.pmtiles]
      python3 testes/mapa/teste_mapa.py --atualizar-hashes   (só depois de alterar o mapa DE PROPÓSITO e conferir as figuras)
Requer: Pillow. Para o item 5: Playwright com Chromium.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SKILL = AQUI.parent.parent
CONG = AQUI / "congelados.json"
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def roda(args, cwd):
    r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, encoding="utf-8", env=ENV, cwd=cwd)
    return r.returncode, r.stdout, r.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pmtiles")
    ap.add_argument("--atualizar-hashes", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    cong = json.loads(CONG.read_text(encoding="utf-8"))
    if a.atualizar_hashes:
        cong["hashes"] = {k: sha(SKILL / k) for k in cong["hashes"]}
        CONG.write_text(json.dumps(cong, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
        print("hashes atualizados; rode o teste de novo e confira as figuras a olho")
        return
    erros, avisos = [], []

    # 1. hashes
    for rel, h in cong["hashes"].items():
        p = SKILL / rel
        if not p.exists():
            erros.append(f"arquivo do mapa ausente: {rel}")
        elif sha(p) != h:
            erros.append(f"arquivo do mapa alterado: {rel}")

    ent = SKILL / "scripts" / "exemplo_entrada.json"
    esp = cong["esperado"]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        # 2. geo_check
        c, o, e = roda([SKILL / "scripts/geo_check.py", ent, "--saida-md", tmp / "q.md", "--saida-json", tmp / "q.json"], tmp)
        if c != 0 or not (tmp / "q.json").exists():
            erros.append(f"geo_check.py falhou (código {c}): {e[-300:]}")
        else:
            q = json.loads((tmp / "q.json").read_text(encoding="utf-8"))
            classes = {str(x["n"]): [[y["teste"], y["classe"]] for y in x["achados"]] for x in q["eventos"]}
            if classes != esp["classes"]:
                erros.append(f"classificações do geo_check mudaram: {classes} (esperado {esp['classes']})")
            if q["revisao_humana"] != esp["revisao_humana"]:
                erros.append(f"REVISÃO HUMANA OBRIGATÓRIA: {q['revisao_humana']} (esperado {esp['revisao_humana']})")
            if q["resumo_indicadores"] != esp["resumo_indicadores"]:
                erros.append(f"resumo dos indicadores: {q['resumo_indicadores']} (esperado {esp['resumo_indicadores']})")

        # 3. figuras em esquema
        c, o, e = roda([SKILL / "scripts/geo_figuras.py", ent, "--saida-dir", tmp / "esq", "--fundo", "esquema"], tmp)
        if c != 0:
            erros.append(f"geo_figuras.py --fundo esquema falhou (código {c}): {e[-300:]}")
        else:
            pngs = sorted(p.name for p in (tmp / "esq").glob("*.png"))
            if pngs != esp["png_esquema"]:
                erros.append(f"figuras em esquema: {pngs} (esperado {esp['png_esquema']})")
            try:
                from PIL import Image
                for p in (tmp / "esq").glob("*visao_geral.png"):
                    if Image.open(p).size != (1296, 480):
                        erros.append(f"{p.name}: tamanho {Image.open(p).size}, esperado (1296, 480)")
            except ImportError:
                avisos.append("Pillow ausente: tamanho das imagens não conferido")
            fj = json.loads((tmp / "esq" / "figuras.json").read_text(encoding="utf-8"))
            for f in fj["figuras"]:
                for k in ("paineis", "nota_rodape", "arquivos", "completa"):
                    if k not in f:
                        erros.append(f"figuras.json, evento {f.get('evento')}: falta '{k}'")
                if "openstreetmap" not in json.dumps(f.get("nota_rodape", "")).lower():
                    erros.append(f"figuras.json, evento {f.get('evento')}: nota de rodapé sem o link do OpenStreetMap")
            if not (tmp / "esq" / "links_coordenadas.md").exists():
                erros.append("links_coordenadas.md não gerado")

        # 4. trava sem pmtiles
        c, o, e = roda([SKILL / "scripts/geo_figuras.py", ent, "--saida-dir", tmp / "auto"], tmp)
        if c != 5:
            erros.append(f"modo auto sem regiao.pmtiles deveria parar com código 5 e saiu com {c}")

        # 5. completo, se houver pmtiles e Playwright
        pm = Path(a.pmtiles) if a.pmtiles else Path.cwd() / "regiao.pmtiles"
        try:
            import playwright  # noqa: F401
            tem_pw = True
        except ImportError:
            tem_pw = False
        if pm.exists() and tem_pw:
            c, o, e = roda([SKILL / "scripts/geo_figuras.py", ent, "--saida-dir", tmp / "completo", "--pmtiles", pm], tmp)
            if c != 0:
                erros.append(f"modo auto com regiao.pmtiles falhou (código {c}): {e[-300:]}")
            else:
                fj = json.loads((tmp / "completo" / "figuras.json").read_text(encoding="utf-8"))
                for f in fj["figuras"]:
                    if not f.get("completa"):
                        avisos.append(f"evento {f.get('evento')}: FIGURA INCOMPLETA (fora da área do regiao.pmtiles?)")
                nomes = {p.name for p in (tmp / "completo").glob("*.png")}
                for suf in ("_A_visao_geral.png", "_B_log.png", "_C_residencia.png"):
                    if not any(n.endswith(suf) for n in nomes):
                        erros.append(f"modo completo sem imagem *{suf}")
                print("Figuras completas geradas; confira A, B e C a olho antes de usar.")
        else:
            motivo = [] if pm.exists() else ["regiao.pmtiles"]
            motivo += [] if tem_pw else ["Playwright"]
            avisos.append(f"B e C não testadas aqui (falta: {', '.join(motivo)}): testar no Cowork com o arquivo real")

    for x in avisos:
        print("AVISO:", x)
    if erros:
        sys.exit("TESTE DO MAPA FALHOU:\n- " + "\n- ".join(erros))
    print(f"TESTE DO MAPA OK: {len(cong['hashes'])} arquivos congelados; geo_check igual à linha de base; "
          f"{len(esp['png_esquema'])} figuras em esquema; trava do código 5 de pé.")


if __name__ == "__main__":
    main()
