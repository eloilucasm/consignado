#!/usr/bin/env python3
"""testar-verificador.py - prova que cada regra do verificador dispara.

Copia o pacote para uma pasta temporária, aplica UM defeito de cada vez e confere que o verificador reprova
com a mensagem esperada. Antes, confirma que a cópia limpa passa. Não altera o pacote original.

Uso:  python3 testar-verificador.py --tmp <pasta temporária>
Requer: node 18+.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SK = "nao-contratado"
MODELO = f"{SK}/assets/modelo-inicial-nao-contratado.md"
PECA = f"{SK}/testes/caso-ficticio/saida/inicial-nao-contratado.md"
REG = f"{SK}/testes/caso-ficticio/saida/checagem-fsc-vf.md"


def troca(rel, de, para):
    def f(raiz):
        p = raiz / rel
        t = p.read_text(encoding="utf-8")
        assert de in t, f"{rel}: trecho de teste não encontrado: {de[:40]}"
        p.write_text(t.replace(de, para, 1), encoding="utf-8", newline="\n")
    return f


def troca_todas(rel, de, para):
    def f(raiz):
        p = raiz / rel
        t = p.read_text(encoding="utf-8")
        assert de in t, f"{rel}: trecho de teste não encontrado: {de[:40]}"
        p.write_text(t.replace(de, para), encoding="utf-8", newline="\n")
    return f


def remove(rel):
    def f(raiz):
        (raiz / rel).unlink()
    return f


def acrescenta(rel, texto):
    def f(raiz):
        p = raiz / rel
        antes = p.read_text(encoding="utf-8") if p.exists() else ""  # arquivo novo: a mutação o cria
        p.write_text(antes + "\n" + texto + "\n", encoding="utf-8", newline="\n")
    return f


CASOS = [  # (descrição, mutação, trecho esperado na mensagem de erro)
    ("tratamento antigo no modelo", acrescenta(MODELO, "Excelentíssimo Senhor Juiz"), "tratamento antigo"),
    ("Súmula 326 usada como base", acrescenta(MODELO, "conforme Súmula 326 do STJ, o caráter é punitivo"), "Súmula 326"),
    ("'inexistência confirmada'", acrescenta(MODELO, "Efeito: Inexistência confirmada"), "inexistência confirmada"),
    ("Res. CMN 4.753 como base", acrescenta(MODELO, "na forma da Resolução CMN nº 4.753/2019"), "4.753"),
    ("dano moral diferente na fundamentação do modelo", troca(MODELO, "o valor de **R$ 20.000,00", "o valor de **R$ 15.000,00"), "fundamentação sem o dano moral"),
    ("dano moral diferente no pedido do modelo", troca(MODELO, "danos extrapatrimoniais de **R$ 20.000,00", "danos extrapatrimoniais de **R$ 15.000,00"), "pedido sem o dano moral"),
    ("dano moral diferente no valor da causa da peça", troca(PECA, "dano extrapatrimonial (R$ 20.000,00)", "dano extrapatrimonial (R$ 25.000,00)"), "valor da causa sem o dano moral"),
    ("art. 2º-C atribuído à Res. 5.112", acrescenta(MODELO, "nos termos do art. 2º-C da Resolução CMN 5.112/2023"), "art. 2º-C da Res. CMN 5.112"),
    ("art. 292, IV, do CPC", acrescenta(MODELO, "valor da causa pelo art. 292, IV, do CPC"), "art. 292, IV"),
    ("enunciado do FONAJE inexistente", acrescenta(PECA, "Conforme o Enunciado 999 do FONAJE."), "Enunciado 999 do FONAJE"),
    ("enunciado do FONAJE revogado", acrescenta(PECA, "Conforme o Enunciado 103 do FONAJE."), "Enunciado 103 do FONAJE"),
    ("índice de jurisprudência cita enunciado revogado", acrescenta(f"{SK}/references/jurisprudencia/INDEX.md", "| Enunciado 103 do FONAJE | revogado | `fonaje-enunciados-civeis.md` | teste |"), "Enunciado 103 do FONAJE"),
    ("MAPA.md desatualizado", acrescenta(f"{SK}/references/normas/lei-9099.md", "linha nova de teste"), "MAPA.md desatualizado"),
    ("enunciado do FONAJEF inexistente", acrescenta(PECA, "Conforme o Enunciado 999 do FONAJEF."), "Enunciado 999 do FONAJEF"),
    ("\"prática sistêmica\" sem fonte", acrescenta(MODELO, "O banco adota prática sistêmica de fraude."), "sem fonte no acervo"),
    ("migração \"que nenhuma norma autoriza\"", acrescenta(MODELO, "figura que nenhuma das normas de regência autoriza"), "cessão"),
    ("modelo sem o tópico de precedentes", troca(MODELO, "Dos precedentes judiciais evocados ao caso concreto", "Das ideias"), "precedentes"),
    ("marcador [[SE]] sobrando na peça", acrescenta(PECA, "[[SE JEC]] texto"), "marcador de condicional"),
    ("campo de modelo não preenchido na peça", acrescenta(PECA, "contrato [CONTRATO]"), "campo de modelo"),
    ("valor da causa diferente do calculo.json", troca(PECA, "R$ 39.730,20", "R$ 39.730,21"), "valor da causa"),
    ("artigo inexistente no CPC", acrescenta(PECA, "Nos termos do art. 9999 do CPC."), "não existe em cpc.md"),
    ("súmula do STJ não transcrita", acrescenta(PECA, "Conforme a Súmula 999 do STJ."), "Súmula 999/STJ"),
    ("tema não transcrito", acrescenta(PECA, "Conforme o Tema 777/STJ."), "Tema 777/STJ"),
    ("acórdão fora do acervo", acrescenta(PECA, "Conforme o EAREsp 111.111/RS."), "não consta de references/jurisprudencia"),
    ("cópia do protocolo difere do acervo", acrescenta(f"{SK}/protocolo/protocolo.md", "linha estranha"), "difere do acervo"),
    ("ESTRUTURA.md desatualizado", acrescenta(f"{SK}/references/normas/lei-9099.md", "linha nova"), "ESTRUTURA.md desatualizado"),
    ("name diferente da pasta", troca(f"{SK}/SKILL.md", "name: nao-contratado", "name: outro-nome"), "difere da pasta"),
    ("link para arquivo inexistente", acrescenta(f"{SK}/SKILL.md", "Veja `assets/nao-existe.md`."), "não existe"),
    ("peça sem o registro FSC/VF", remove(REG), "sem checagem-fsc-vf.md"),
    ("registro sem a linha FSC7", troca(REG, "| FSC7 |", "| FSX7 |"), "falta a linha FSC7"),
    ("registro sem a linha VF9", troca(REG, "| VF9 |", "| VX9 |"), "falta a linha VF9"),
    ("status de FSC inválido", troca(REG, "| FSC1 | OK |", "| FSC1 | TALVEZ |"), "status inválido"),
    ("FSC3: peça sem o art. 429, II, do CPC", troca_todas(PECA, "art. 429, II", "art. 429"), "FSC3"),
    ("JEC em comarca sem Vara do Sistema sem o preâmbulo da Lei 9.099", troca(PECA, "AO JUÍZO DA [PREENCHER: N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE ILHÉUS - BAHIA", "AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE URUÇUCA - BAHIA"), "FSC9: peça de Justiça Comum sem o pedido de exibição"),
    ("FSC9: JEC com pedido de exibição", acrescenta(PECA, "Requer-se, também, a exibição dos documentos acima (arts. 396 a 404 do CPC)."), "FSC9"),
    ("arquivo do mapa alterado", acrescenta("recurso-inominado-consignado-geolocalizacao/scripts/geo_compor.py", "# alteração de teste"), "arquivo do mapa alterado"),
    ("arquivo do mapa ausente", remove("recurso-inominado-consignado-geolocalizacao/assets/mapa/lib/pmtiles.js"), "arquivo do mapa ausente"),
    ("Tema 929 volta às referências do recurso", acrescenta("recurso-inominado-consignado-geolocalizacao/references/referencias_juridicas.md", 'Citar SEM pedido de verificação, com esta nota de rodapé, exatamente:\n  "BRASIL. Superior Tribunal de Justiça. Corte Especial. Tema Repetitivo 929."'), "Tema 929/STJ como fundamento"),
    ("IN 138 com vigência antiga no recurso", acrescenta("recurso-inominado-consignado-geolocalizacao/references/referencias_juridicas.md", "Contrato a partir de 11/11/2022: IN 138/2022."), "IN 138 com vigência em 11/11/2022"),
    ("FSC1/FSC7: contrato sem negativa específica", troca(PECA, "**Contrato nº 00123456789.** A parte autora nega", "**Contrato nº 00123456789.** A parte autora afirma"), "negativa específica do contrato 00123456789"),
    ("transcrição de artigo adulterada no modelo", troca(MODELO, "responde, independentemente da existência de culpa", "responde, apenas quando houver culpa"), "trecho transcrito não confere com cdc.md"),
    ("transcrição de ementa adulterada no modelo", troca(MODELO, "sabidamente com maior dificuldade", "sem nenhuma dificuldade"), "trecho transcrito não confere com ac-5003696-trf4.md"),
    ("tese do EAREsp 676.608 adulterada no modelo", troca(MODELO, "referida cobrança consubstanciar conduta contrária", "referida cobrança consubstanciar conduta conforme"), "trecho transcrito não confere com earesp-676608-stj.md"),
    ("aspas atribuídas a artigo que não diz aquilo", acrescenta(PECA, 'O art. 290 do Código Civil dispõe que "a cessão de crédito é sempre eficaz perante o devedor, ainda que não notificado".'), "trecho transcrito não confere com cc.md"),
    ("RMC com juros desde o evento danoso no modelo", acrescenta("rmc/assets/modelo-inicial-rmc.md", "juros de mora desde o evento danoso (Súmula 54 do STJ)"), "no RMC os juros contam da citação"),
    ("RMC com juros desde o evento danoso na peça", acrescenta("rmc/testes/caso-ficticio/saida/inicial-rmc.md", "juros de mora desde o evento danoso (Súmula 54 do STJ)"), "no RMC os juros contam da citação"),
    ("ponto do mapa de argumentos sem pedido", troca("replica-consignado/testes/caso-ficticio/saida/mapa-argumentos.json", '"pedidos": [\n      "preliminares"\n    ]', '"pedidos": []'), "sem pedido"),
    ("pedido do mapa ausente da réplica", acrescenta("replica-consignado/testes/caso-ficticio/saida/replica-teste.md", "# Dos pedidos\n\na) a procedência dos pedidos, nos termos da inicial."), "que não está nos pedidos da peça"),
    ("ementa de precedente fora do acervo", acrescenta(PECA, "Conforme a ementa do TRF-4 (AC 5009999-11.2024.4.04.7100/RS):\n\n> 1. O banco responde por qualquer desconto feito em benefício previdenciário sem prova da contratação."), "que não está em references/jurisprudencia"),
]


def verifica(raiz):
    r = subprocess.run(["node", str(raiz / "_manutencao" / "verificar-pacote.js"), "--raiz", str(raiz),
                        "--config", str(raiz / "_manutencao" / "verificador.config.js"), "--detalhe"],
                       capture_output=True, text=True, encoding="utf-8")
    return r.returncode, r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tmp", required=True)
    a = ap.parse_args()
    base = Path(a.tmp)
    base.mkdir(parents=True, exist_ok=True)
    falhas = []
    copia = base / "pacote-teste"
    for numero, (desc, mut, esperado) in enumerate([("cópia limpa", None, None)] + CASOS):
        if copia.exists():
            shutil.rmtree(copia)
        shutil.copytree(RAIZ, copia, ignore=shutil.ignore_patterns("_backup", "backup-sincronizacao", "__pycache__", "node_modules"))
        if mut:
            mut(copia)
        codigo, saida = verifica(copia)
        if mut is None:
            ok = codigo == 0
            print(("OK   " if ok else "FALHA"), desc, "(deve passar)")
            if not ok:
                falhas.append(desc + "\n" + saida)
                break
            continue
        ok = codigo == 1 and esperado in saida
        print(("OK   " if ok else "FALHA"), desc, f"(esperado: reprovar com '{esperado}')")
        if not ok:
            falhas.append(f"{desc}: código {codigo}\n{saida[:900]}")
    if copia.exists():
        shutil.rmtree(copia)
    if falhas:
        sys.exit("\n\nREGRAS QUE NÃO DISPARARAM:\n" + "\n---\n".join(falhas))
    print(f"\nTodas as {len(CASOS)} regras dispararam e a cópia limpa passa.")


if __name__ == "__main__":
    main()
