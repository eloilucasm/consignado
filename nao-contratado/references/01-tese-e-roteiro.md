# A tese do não contratado e o roteiro de redação

## Quando esta skill se aplica

Contrato de empréstimo consignado que o beneficiário **nega ter firmado**, averbado em benefício do INSS, nos blocos B, C ou Caixa da análise. A tese é de **inexistência** da relação jurídica (subsidiariamente, nulidade), com repetição do indébito em dobro, obrigação de fazer e dano moral.

Não é desta skill: contrato **migrado** de outro banco sem anuência (bloco A), **Tese 1000** (contrato derivado com sufixo sobre contrato-raiz excluído, bloco E), **refinanciamento de cartão RMC/RCC** (bloco D) e recurso contra sentença.

## Gatilhos dos tópicos condicionais

| Tópico | Gatilho | Fonte do dado |
|---|---|---|
| Tutela de urgência | algum contrato **ativo** no extrato (só sobre os ativos) | `calculo.json`, campo `ativos` |
| Prescrição | algum desconto com mais de 5 anos | `calculo.json`, campo `prescricao_5_anos` |
| Litispendência | `litispendencia` preenchido na ficha | ficha |
| Tramitação prioritária | autor com 60 anos ou mais | qualificação (nascimento) |
| Campo "Motivo da Exclusão" | sempre que há contrato excluído com o campo em branco, ou ativo | extrato |
| Exibição e perícia com quesitos | rito = Justiça Comum | pergunta ao advogado |
| Endereçamento federal | réu = Caixa (código 104) | `reus.json` |

## Anomalias que exigem pausa

- Contrato de bloco B ou C **ativo** no extrato: a análise só põe contratos não ativos nesses blocos. Mostre ao advogado e confirme a tutela.
- Valor liberado **ausente ou R$ 0,00**: possível portabilidade pura. Trate o proveito econômico (FSC4) e não afirme que não houve crédito sem prova.
- Descontos **anteriores a 30/03/2021**: pedir o dobro de todos. O EAREsp 676.608/RS (decisão R7, 01/11/2026) sustenta a dobra dos posteriores; para os anteriores, use o bloco `[[SE HÁ DESCONTO ANTES DE 30/03/2021]]` (dobra pelo art. 42). Sem Tema 929.
- Descontos com **mais de 10 anos**: o tópico de prescrição não pode afirmar que todos estão no prazo decenal.
- Réu fora de `reus.json`: não preencha CNPJ nem endereço de memória.
- Contrato negado que seja **cartão consignado (RMC/RCC)**: o juiz pode suspender a ação com base no **Tema 1414/STJ** (afetado, sem tese). Esta skill alega **inexistência** (fraude), questão anterior à validade que o tema discute. Decisões do TJMG afastaram a suspensão por distinção (ver `jurisprudencia/tema-1414-stj.md`; julgado de outro estado, ementa de fonte secundária). Se a suspensão vier, peça o prosseguimento por distinção (CPC, art. 1.037, § 9º).

## Perguntas típicas (máximo três por rodada)

1. Rito: JEC ou Justiça Comum? (peça sempre)
2. Cidade e UF do fecho? (peça sempre)
3. O cliente recebeu algum crédito em conta nas datas dos contratos? Há extrato bancário?
4. O cliente tem assinatura manuscrita em algum documento do banco, ou a contratação foi eletrônica? (define a perícia na Justiça Comum)

## Mapa da checagem pré-recurso (FSC) para o modelo

| Fundamento de sentença | Onde a inicial se previne |
|---|---|
| FSC3, ônus da prova | tópico "Do direito", subtópico da responsabilidade (art. 14, § 3º, CDC) e tópico da inversão do ônus (art. 429, II, CPC; Tema 1061) |
| FSC7, FSC1, FSC2, autoria | subtópico "nega, contrato a contrato" nos fatos |
| FSC4, proveito econômico | mesmo subtópico: valor liberado do extrato; tabela de documentos (comprovante do crédito) |
| FSC5, FSC11, cessão e mesma data | não se aplica a esta tese, salvo contratos do mesmo dia (descrever nos fatos) |
| FSC6, impugnação tardia | fatos (data da ciência) e tópico de prescrição |
| FSC8, mero dissabor | subtópico do dano extrapatrimonial (Súmula 40 do TJBA, particularidades) |
| FSC9, FSC10, prova técnica | tópico da inversão (JEC) ou exibição e perícia com quesitos (Justiça Comum) |
| FSC12, litigância predatória | documentos legíveis e atuais; um processo por benefício + banco + tese; nada sobre outras ações |
