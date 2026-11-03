#!/usr/bin/env python3
"""gerar-indice-jurisprudencia.py - gera references/jurisprudencia/INDEX.md em cada skill, por ASSUNTO da peça.

A curadoria (qual precedente serve a qual assunto, o que diz e como a skill o usa) está em DADOS, abaixo. O script só monta
o arquivo e deixa de fora a linha cujo arquivo de precedente não existe na skill. Edite DADOS, rode o script e depois o
verificador: ele confere que cada precedente citado no INDEX existe (e, no FONAJE, está vigente).

Uso (a partir de consignado-pacote/):  python3 _manutencao/gerar-indice-jurisprudencia.py [--skill nome]
"""
import argparse
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent

STJ, TJBA, FON = "sumulas-stj.md", "sumulas-tjba-turma-uniformizacao.md", "fonaje-enunciados-civeis.md"
S326, T929, T1061, T1198, E738 = "sumula-326-stj.md", "tema-929-stj.md", "tema-1061-stj.md", "tema-1198-stj.md", "earesp-738991-stj.md"
T1414 = "tema-1414-stj.md"
T466, T1076, R2168312 = "tema-466-stj.md", "tema-1076-stj.md", "resp-2168312-pr-stj.md"

# (assunto, citar como, o que diz, arquivo, uso em nao-contratado, uso em rmc). Uso None = a linha não entra na skill.
DADOS = [
    ("Relação de consumo e responsabilidade do banco", "Súmula 297/STJ", "o CDC se aplica às instituições financeiras", STJ,
     "no modelo (tópico do CDC)", "no modelo (tópico do CDC)"),
    ("Relação de consumo e responsabilidade do banco", "Súmula 479/STJ", "o banco responde objetivamente por fortuito interno, inclusive fraude de terceiro", STJ,
     "no modelo (responsabilidade objetiva)", "no modelo; no RMC o ato é do próprio banco ('com mais razão')"),
    ("Relação de consumo e responsabilidade do banco", "Súmula 10/TJBA", "a relação de consumo se prova por qualquer meio, sem exigir o instrumento contratual", TJBA,
     "**o banco pode invocá-la** para provar o contrato por outros meios; a resposta é o ônus da prova e o Tema 1061", "**o banco pode invocá-la**; no RMC o contrato do cartão não é impugnado"),
    ("Relação de consumo e responsabilidade do banco", "Súmula 41/TJBA", "é lícita a contratação de cartão de crédito consignável, observado o direito à informação e sem vício de consentimento", TJBA,
     None, "**o banco a invocará**; o modelo tem subtópico próprio: não se discute o cartão, discute-se o refinanciamento e a informação"),
    ("Prova, ônus e inversão", "Tema 1061/STJ", "na impugnação da assinatura do contrato bancário, o ônus de provar a autenticidade é de quem produziu o documento (o banco)", T1061,
     "no modelo (inversão do ônus)", None),
    ("Prova, ônus e inversão", "Enunciado 53 do FONAJE", "a citação deve advertir, em termos claros, da possibilidade de inversão do ônus da prova", FON,
     "disponível; reforça o pedido de inversão no JEC (ainda não está no modelo)", "disponível; reforça o pedido de inversão no JEC (ainda não está no modelo)"),
    ("Prova, ônus e inversão", "Enunciado 12 do FONAJE", "a perícia informal é admissível (art. 35 da Lei 9.099/95)", FON,
     "disponível, para o JEC quando houver prova técnica", "disponível; o modelo já reserva o parecer técnico contábil no JEC"),
    ("Dano extrapatrimonial", "Súmula 40/TJBA", "desconto indevido não é dano moral por si só; caracteriza-se havendo violação significativa a direito da personalidade, nas particularidades do caso", TJBA,
     "no modelo (dano extrapatrimonial)", "no modelo (dano extrapatrimonial)"),
    ("Dano extrapatrimonial", "Súmula 326/STJ", "condenação em montante inferior ao pedido de dano moral não gera sucumbência recíproca; **não trata de caráter punitivo**", S326,
     "no modelo (valor estimativo)", "no modelo (valor estimativo)"),
    ("Correção monetária e juros", "Súmula 43/STJ", "a correção monetária do dano material conta do efetivo prejuízo", STJ,
     "no modelo (restituição)", "no modelo (restituição)"),
    ("Correção monetária e juros", "Súmula 362/STJ", "a correção monetária do dano moral conta do arbitramento", STJ,
     "no modelo (dano extrapatrimonial)", "no modelo (dano extrapatrimonial)"),
    ("Correção monetária e juros", "Súmula 54/STJ", "os juros de mora contam do evento danoso na responsabilidade extracontratual", STJ,
     "no modelo (contrato inexistente: responsabilidade extracontratual)", None),
    ("Correção monetária e juros", "Súmula 33/TJBA", "na responsabilidade contratual, os juros de mora contam da citação, salvo constituição anterior em mora", TJBA,
     None, "no modelo (juros de mora da citação, porque o cartão é contrato)"),
    ("Correção monetária e juros", "Súmula 32/TJBA", "na responsabilidade extracontratual, os juros de mora contam do evento danoso", TJBA,
     "disponível, para sustentar o termo inicial dos juros", None),
    ("Relação de consumo e responsabilidade do banco", "Tema 466/STJ", "as instituições financeiras respondem objetivamente por fortuito interno relativo a fraudes e delitos de terceiros em operações bancárias (origem da Súmula 479)", T466,
     "disponível; reforça a Súmula 479 (no migrado, já está no modelo)", "disponível; reforça a Súmula 479"),
    ("Honorários (Justiça Comum)", "Tema 1076/STJ", "honorários por equidade só se o proveito econômico for inestimável ou irrisório, ou o valor da causa muito baixo; nos demais casos, percentuais do art. 85, §§ 2º ou 3º", T1076,
     "disponível para o pedido de honorários em Justiça Comum (no migrado, já está no modelo)", "disponível para o pedido de honorários em Justiça Comum"),
    ("Honorários (Justiça Comum)", "REsp 2.168.312/PR", "o art. 85, § 2º, do CPC não impede somar o valor da condenação e o proveito econômico como base dos honorários (ação dúplice: declaratória e indenizatória); **Informativo 875/STJ (portal do STJ); acórdão não lido**", R2168312,
     "no modelo (migrado), com [VERIFICAR]", "no modelo (migrado), com [VERIFICAR]"),
    ("Cartão consignado (RMC) e suspensão nacional", "Tema 1414/STJ", "validade e abusividade dos contratos de RMC (informação; prolongamento da dívida frente aos juros rotativos no refinanciamento; decadência ou nulidade; consequência; dano moral in re ipsa); **afetado, sem tese; suspensão nacional dos processos pendentes, exceto cumprimentos de sentença**", T1414,
     "**alerta**: se a ação envolver cartão consignado, o juiz pode suspendê-la; para inexistência por fraude há decisões do TJMG afastando a suspensão (outro estado; ementa de fonte secundária)", "**alerta**: a questão II.b do tema (prolongamento da dívida frente aos juros do refinanciamento) tem proximidade com a tese; o escritório decidiu em 29/10/2026 pedir o prosseguimento por distinção"),
    ("Dano extrapatrimonial", "Julgados do STJ citados na Súmula 40/TJBA", "AgInt no AREsp 2149415/MG (3ª T., j. 29/05/2023); AgInt no AREsp 2157547/SC (4ª T., j. 12/12/2022); AgInt no AREsp n. 1.622.003/SP (4ª T., j. 19/10/2020); REsp 1.550.509-RJ (j. 03/03/2016) e outros", TJBA,
     "disponíveis só pela lista do texto da súmula (inteiros teores não baixados); conferir antes de citar; poderiam substituir o acórdão do TRF-4 do modelo", "idem"),
    ("Repetição em dobro e prescrição", "Tema 929/STJ", "hipóteses de repetição em dobro do art. 42, parágrafo único, do CDC; **NÃO CITAR na peça (decisão de 29/10/2026): tese não publicada**", T929,
     "no modelo, sempre com [VERIFICAR ANTES DE PROTOCOLAR]", "no modelo, sempre com [VERIFICAR ANTES DE PROTOCOLAR]"),
    ("Repetição em dobro e prescrição", "EAREsp 738.991/RS", "prazo decenal da repetição de indébito (caso de telefonia); fonte secundária", E738,
     "no modelo (prescrição), por analogia e com [VERIFICAR]", None),
    ("Litigância e riscos da inicial", "Súmula 42/TJBA", "a negativa de contratação é indício de litigância de má-fé se provados o negócio e a disponibilização do numerário", TJBA,
     "**risco**: o banco a invocará se juntar contrato e comprovante de crédito; conferir o crédito antes de afirmar que não houve", "risco menor (a tese não nega o cartão)"),
    ("Litigância e riscos da inicial", "Súmula 46/TJBA", "ajuizamento de múltiplas ações semelhantes ou idênticas para obter vantagem indevida é litigância predatória", TJBA,
     "checagem FSC12 do padrão de peças", "checagem FSC12 do padrão de peças"),
    ("Litigância e riscos da inicial", "Súmula 51/TJBA", "documentos desatualizados ou ilegíveis autorizam o juiz a exigir documentação idônea e atualizada", TJBA,
     "checagem FSC12: comprovante de residência atual e legível", "checagem FSC12: comprovante de residência atual e legível"),
    ("Litigância e riscos da inicial", "Súmula 53/TJBA", "em caso suspeito de fraude, o juiz deve exigir a confirmação pessoal da parte autora", TJBA,
     "checagem FSC12", "checagem FSC12"),
    ("Litigância e riscos da inicial", "Tema 1198/STJ", "litigância abusiva e emenda da inicial", T1198,
     "usado na checagem FSC12", None),
    ("Litigância e riscos da inicial", "Enunciado 136 do FONAJE", "o reconhecimento da litigância de má-fé pode implicar custas, honorários, multa e indenização (art. 55 da Lei 9.099/95)", FON,
     "disponível", "disponível"),
    ("Consignado e pessoa analfabeta", "Súmula 13/TJBA", "o analfabetismo, por si só, não invalida o negócio; exige-se vício de consentimento", TJBA,
     "**o banco pode invocá-la** se o cliente for analfabeto", None),
    ("Consignado e pessoa analfabeta", "Súmula 38/TJBA", "é válido o consignado de analfabeto com assinatura a rogo e duas testemunhas (art. 595 do CC)", TJBA,
     "**o banco pode invocá-la** se o cliente for analfabeto", None),
    ("Tutela provisória no JEC", "Enunciado 26 do FONAJE", "são cabíveis a tutela acautelatória e a antecipatória nos Juizados Especiais Cíveis", FON,
     "disponível; ainda não está no modelo", "disponível; ainda não está no modelo (as petições AMN o citavam como nº 26)"),
    ("Tutela provisória no JEC", "Enunciado 163 do FONAJE", "a tutela de urgência requerida em caráter antecedente (CPC, arts. 303 a 310) é incompatível com o JEC", FON,
     "o modelo pede tutela incidental, o que é compatível", "o modelo pede tutela incidental, o que é compatível"),
    ("Tutela provisória no JEC", "Enunciado 22 do FONAJE", "a multa cominatória é cabível desde o descumprimento da tutela antecipada", FON,
     "disponível, para o pedido de multa diária", "disponível, para o pedido de multa diária"),
    ("Tutela provisória no JEC", "Enunciado 120 do FONAJE", "a multa por descumprimento de tutela é executável antes do trânsito em julgado", FON,
     "disponível", "disponível"),
    ("Tutela provisória no JEC", "Enunciado 144 do FONAJE", "a multa cominatória não fica limitada a 40 salários mínimos, mas deve ser razoável", FON,
     "disponível", "disponível"),
    ("Competência, complexidade e valor da causa no JEC", "Enunciado 54 do FONAJE", "a menor complexidade se afere pelo objeto da prova e não pelo direito material", FON,
     "disponível", "disponível; sustenta a competência do JEC"),
    ("Competência, complexidade e valor da causa no JEC", "Enunciado 70 do FONAJE", "ação sobre ilegalidade de juros não é complexa, exceto se exigir perícia contábil", FON,
     "disponível", "disponível; conversa com a regra do modelo (perícia contábil leva à Justiça Comum)"),
    ("Competência, complexidade e valor da causa no JEC", "Enunciado 94 do FONAJE", "cabe revisão de contrato no JEC, observada a alçada, exceto se exigir perícia contábil", FON,
     "disponível", "disponível; idem"),
    ("Competência, complexidade e valor da causa no JEC", "Enunciado 69 do FONAJE", "ação de dano moral não é, por si só, matéria complexa", FON,
     "disponível", "disponível"),
    ("Competência, complexidade e valor da causa no JEC", "Enunciado 170 do FONAJE", "no JEC não se aplica o art. 292, V, do CPC ao dano moral; o valor específico atribuído soma-se ao do dano material para a alçada", FON,
     "disponível, para o tópico do valor da causa (o modelo já soma)", "disponível, para o tópico do valor da causa (o modelo já soma)"),
    ("Competência, complexidade e valor da causa no JEC", "Enunciado 39 do FONAJE", "o valor da causa corresponde à pretensão econômica do pedido", FON,
     "disponível", "disponível"),
    ("Competência, complexidade e valor da causa no JEC", "Enunciado 175 do FONAJE", "em obrigação de trato sucessivo, 12 parcelas vincendas mais as vencidas não podem exceder a alçada", FON,
     "**conferir** quando houver contrato ativo e pedido de parcelas futuras", "**conferir** quando o cartão estiver ativo"),
    ("Aplicação do CPC no JEC", "Enunciado 161 do FONAJE", "o CPC/2015 só se aplica ao JEC com remissão expressa ou compatibilidade com o art. 2º da Lei 9.099/95", FON,
     "alerta geral", "alerta geral"),
    ("Aplicação do CPC no JEC", "Enunciado 162 do FONAJE", "não se aplica ao JEC a regra do art. 489 do CPC/2015, diante do art. 38 da Lei 9.099/95", FON,
     "no modelo: o tópico de precedentes vale no JEC com uma ponte pelo art. 2º da Lei 9.099/95 (decisão do escritório); não cite os Enunciados 161 e 162 na peça", "no modelo: o tópico de precedentes vale no JEC com uma ponte pelo art. 2º da Lei 9.099/95 (decisão do escritório); não cite os Enunciados 161 e 162 na peça"),
    ("Gratuidade, custas e honorários", "Enunciado 116 do FONAJE", "o juiz pode exigir comprovação da insuficiência de recursos; a presunção é relativa", FON,
     "disponível: prepare a prova da hipossuficiência (base de cálculo do benefício)", "disponível: o modelo já informa a base de cálculo"),
    ("Gratuidade, custas e honorários", "Enunciado 114 do FONAJE", "a gratuidade não abrange a condenação por litigância de má-fé", FON,
     "disponível", "disponível"),
    ("Gratuidade, custas e honorários", "Súmula 5/TJBA", "havendo sucumbência recíproca, é vedada a compensação de honorários", TJBA,
     "disponível (recurso)", "disponível (recurso)"),
    ("Citação, audiência e revelia", "Enunciado 10 do FONAJE", "a contestação pode ser apresentada até a audiência de instrução e julgamento", FON,
     "disponível: no JEC o banco responde até a AIJ; por isso a inversão pede a juntada 'com a contestação'", "disponível: idem"),
    ("Citação, audiência e revelia", "Enunciado 20 do FONAJE", "o comparecimento pessoal da parte à audiência é obrigatório; a pessoa jurídica pode ter preposto", FON,
     "disponível", "disponível"),
    ("Recurso inominado (para a skill de recurso)", "Enunciado 80 do FONAJE", "o recurso inominado é julgado deserto sem o preparo integral e sua comprovação em 48 horas", FON,
     "disponível", "disponível"),
    ("Recurso inominado (para a skill de recurso)", "Enunciado 168 do FONAJE", "não se aplica aos recursos dos Juizados o art. 1.007 do CPC/2015", FON,
     "disponível", "disponível"),
]

USO_TESE_1000 = {
    "Tema 1414/STJ": "relevância baixa: é tese de cartão RMC; só importa se o derivado for cartão",
    "Súmula 54/STJ": "no modelo (contrato inexistente: responsabilidade extracontratual)",
}

CAB = """# Índice da jurisprudência por assunto: {skill}

Gerado por `python3 _manutencao/gerar-indice-jurisprudencia.py` (não edite à mão: a curadoria está no script). Consulta de 28/10/2026.

**Como usar.** Ache o assunto da peça aqui e abra só o precedente: `grep -n "^## Enunciado 26$" references/jurisprudencia/{fon}` (FONAJE), `grep -n "Súmula nº 40" references/jurisprudencia/{tjba}` (TJBA), `grep -n "SÚMULA 297" references/jurisprudencia/{stj}` (STJ). Não leia o arquivo inteiro. O que **não** está no acervo está em `protocolo/fontes-e-limites.md`.

**Regras.** Cite precedente que está neste índice e no arquivo. Enunciado do FONAJE não é súmula nem tem força de lei: cite como "Enunciado N do FONAJE". Na coluna "Uso", **negrito** é alerta: o banco pode invocar o precedente, ou há decisão do advogado pendente.
"""


def montar(skill, dir_jur):
    existentes = {p.name for p in dir_jur.glob("*.md")}
    col = 4 if skill in ("nao-contratado", "tese-1000", "migrado", "replica-consignado", "recurso-inominado-consignado-geolocalizacao") else 5
    ajustes = USO_TESE_1000 if skill in ("tese-1000", "migrado") else {}
    linhas, grupo = [CAB.format(skill=skill, fon=FON, tjba=TJBA, stj=STJ)], None
    for d in DADOS:
        if d[col] is None or d[3] not in existentes:
            continue
        if d[0] != grupo:
            grupo = d[0]
            linhas.append(f"\n## {grupo}\n\n| Citar como | O que diz | Arquivo | Uso nesta skill |\n|---|---|---|---|")
        linhas.append(f"| {d[1]} | {d[2]} | `{d[3]}` | {ajustes.get(d[1], d[col])} |")
    linhas.append("\n## Arquivos desta pasta\n\n| Arquivo | Conteúdo | Situação |\n|---|---|---|")
    info = {
        STJ: ("Súmulas do STJ conferidas para o consignado (43, 54, 203, 297, 362, 479) e súmulas 1 a 10", "conferidas"),
        S326: ("Súmula 326/STJ", "vigente; trata de sucumbência"),
        TJBA: ("Súmulas 1 a 55 da Turma de Uniformização das Turmas Recursais do TJBA", "todas com data de aprovação (55 de 55; a da Súmula 55, 10/11/2025, foi informada pelo advogado); 3 e 22 revogadas; 45 alterada em 03/09/2025"),
        FON: ("Enunciados cíveis 1 a 178 do FONAJE (139 vigentes)", "até o 57º Encontro (27 a 29/05/2026); os revogados estão no fim do arquivo"),
        T929: ("Tema Repetitivo 929/STJ", "mérito julgado, tese não publicada"),
        T1061: ("Tema Repetitivo 1061/STJ", "trânsito em julgado em 25/05/2022"),
        T1198: ("Tema Repetitivo 1198/STJ", "trânsito em julgado em 13/10/2026; DJe 11/06/2026"),
        E738: ("EAREsp 738.991/RS", "fonte secundária; caso de telefonia"),
        "fonaje-encontros.md": ("Encontros do FONAJE e do FONAJEF: cidade e data, para a nota de rodapé do enunciado", "FONAJEF completo (Ajufe, mês e ano); FONAJE parcial, com `[CONFERIR]` onde não há fonte de data"),
        T466: ("Tema Repetitivo 466/STJ", "trânsito em julgado em 18/10/2011; origem da Súmula 479"),
        T1076: ("Tema Repetitivo 1076/STJ", "acórdão publicado em 31/05/2022; só Justiça Comum"),
        R2168312: ("REsp 2.168.312/PR", "Informativo 875/STJ (portal do STJ); acórdão não lido"),
        T1414: ("Tema Repetitivo 1414/STJ", "**afetado, sem tese**; suspensão nacional; página do STJ lida em 28/10/2026"),
        "fonajef-enunciados.md": ("Enunciados 1 a 226 do FONAJEF (Juizados Federais)", "até o XVIII FONAJEF; sem as Recomendações; só para processo da Caixa em Juizado Especial Federal"),
    }
    for nome in sorted(existentes):
        if nome in info:
            linhas.append(f"| `{nome}` | {info[nome][0]} | {info[nome][1]} |")
    return "\n".join(linhas) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill")
    a = ap.parse_args()
    for d in sorted(RAIZ.iterdir()):
        jur = d / "references" / "jurisprudencia"
        if not (d / "SKILL.md").exists() or not jur.exists() or (a.skill and d.name != a.skill):
            continue
        (jur / "INDEX.md").write_text(montar(d.name, jur), encoding="utf-8", newline="\n")
        print("ok:", jur / "INDEX.md")


if __name__ == "__main__":
    main()
