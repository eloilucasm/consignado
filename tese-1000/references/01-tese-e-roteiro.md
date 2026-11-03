# A Tese 1000 Contra e o roteiro de redação

## Quando esta skill se aplica

Contrato de empréstimo consignado cujo número é o de **um contrato anterior do mesmo banco, já excluído, mais um sufixo** (`_0001`, `_0002`…), averbado como "Averbação nova" no benefício do INSS, sem nova contratação. É o bloco E da análise. A tese é de **inexistência** da relação jurídica quanto ao derivado (subsidiariamente, nulidade), com repetição em dobro, obrigação de fazer e dano extrapatrimonial. A ação tem por objeto **só o derivado**; não discute o contrato-raiz.

Não é desta skill: contrato não contratado comum (sem raiz excluída), contrato **migrado** de outro banco, refinanciamento de cartão RMC/RCC e recurso.

## O núcleo da prova

A prova é o **extrato do INSS**: o número-raiz, a data de exclusão da raiz ("Exclusão Banco" ou outro motivo), a data e a origem da averbação do derivado ("Averbação nova") e o **intervalo** entre as duas. O script (`calcular_1000.py`) mede o intervalo e classifica: **mesmo dia**, **até 30 dias**, **mais de 30 dias** ou **antes da exclusão** (neste último caso a narrativa de "reinclusão depois da exclusão" não vale; rever a tese).

## A norma depende da data da reaverbação

O modelo anterior do escritório (Maria x BNP) aplicava a **IN 138/2022** a uma reaverbação de **2018**. A IN 138 vale desde 13/12/2022; antes, vigorava a **IN INSS/PRES 28/2008**. O script grava `regime_norma` em cada derivado, e o modelo traz os dois blocos:

| Reaverbação | Norma | Dispositivos que a peça usa |
|---|---|---|
| até 12/12/2022 | IN 28/2008 | art. 30, IV (número "único e específico para cada contratação ou refinanciamento") e § 2º ("o contrato celebrado não poderá ser alterado, podendo somente ocorrer a sua exclusão do sistema e averbação de um novo"); art. 5º (assinatura antes do envio do arquivo); art. 6º (responsabilidade) |
| a partir de 13/12/2022 | IN 138/2022 | art. 4º, XIV (exclusão), XV (portabilidade), XVII (repactuação/refinanciamento), XXVII (consignações eletivas); art. 5º, II, III e § 9º; art. 14, parágrafo único |

A redação desses artigos mudou ao longo do tempo (o arquivo consolidado traz redações sucessivas): `[CONFERIR]` na peça.

## O que a peça NÃO pode afirmar

1. **"Barreira técnica da Dataprev"**: que o sistema não permite reaverbar sob o mesmo número. Nenhuma norma do acervo diz isso. A peça usa o texto da IN 28, art. 30, IV e § 2º.
2. **Prática "sistêmica", "reiterada" ou "de massa" do banco**, ou "mapeada por doutrina e jurisprudência": sem fonte no acervo. O extrato prova este caso, e só ele.
3. **"Ilícito de massa" e "Operação Sem Desconto"**: a petição Francisco x Agibank do escritório usa esse contexto, em tese de migração. Ele não faz parte desta skill e tem de ser conferido na fonte antes de qualquer uso.
4. **IN 138, art. 5º, § 1º** como fundamento de que "a autorização não persiste": o parágrafo trata de sucessão aos pensionistas e dependentes, não de reuso para outro contrato.
5. **Dano moral *in re ipsa***: questão em aberto no Tema 1414/STJ. A peça usa a Súmula 40/TJBA.
6. **Prazo decenal atribuído ao EAREsp 676.608/RS**: esse é o precedente da dobra. O da prescrição é o EAREsp 738.991/RS (telefonia), por analogia, com `[VERIFICAR]`.

## Gatilhos dos tópicos condicionais

| Tópico | Gatilho | Fonte do dado |
|---|---|---|
| Tutela de urgência | algum derivado **ativo** (só sobre os ativos) | `calculo.json`, campo `ativos` |
| Bloco da IN 28 ou da IN 138 | data de averbação do derivado | `calculo.json`, `regime_norma` |
| Narrativa do intervalo | mesmo dia, até 30 dias ou mais de 30 dias | `calculo.json`, `categoria_intervalo` |
| Outras ocorrências do número | mesmo número em outro banco (migração, troca de titularidade) | `calculo.json`, `outras_ocorrencias` (fora do escopo: ver abaixo) |
| Prescrição | algum desconto com mais de 5 anos | `calculo.json`, `prescricao_5_anos` |
| Litispendência | `litispendencia` preenchido na ficha | ficha |
| Tramitação prioritária | autor com 60 anos ou mais | qualificação (nascimento) |
| Exibição e perícia com quesitos | rito = Justiça Comum | pergunta ao advogado |
| Endereçamento federal | réu = Caixa (código 104) | `reus.json` |

## Campos do quadro de fatos específicos desta tese

Além dos campos comuns (`protocolo/quadro-de-fatos.md`), registre, para cada derivado e com ID e página do extrato: número do derivado e da raiz; averbação e exclusão da raiz, com o motivo; data e origem da averbação do derivado ("Averbação nova" ou "Migrado do contrato…"); parcela, prazo, início e fim dos descontos; valor liberado; exclusão do derivado e motivo, se houver; o mesmo número em outro banco, com banco, datas e motivo; e se o cliente reconhece o contrato-raiz. Estado de cada campo: confirmado (extrato), relatado (cliente), inferido ou desconhecido.

## Anomalias que exigem pausa

- Derivado averbado **antes** da exclusão da raiz.
- Mais de uma raiz no processo: o modelo trata uma; separe os processos ou adapte a tabela.
- Derivados de regimes diferentes (IN 28 e IN 138): o modelo traz os dois blocos; revise.
- Mesmo número em **outro banco**: **fora do escopo** desta skill (decisão do escritório de 29/10/2026: na Tese 1000 o contrato não é reaverbado por outro banco). O script alerta e não soma os descontos do outro banco; confira se o caso é de outra tese (por exemplo, migrado).
- Derivado **depois refinanciado** ou migrado: parágrafo factual do advogado, só com o que o extrato mostra.
- Descontos anteriores a 30/03/2021: pedir o dobro de todos, com o bloco `[[SE HÁ DESCONTO ANTES DE 30/03/2021]]` (dobra pelo art. 42). O EAREsp 676.608/RS sustenta a dobra dos posteriores. Sem Tema 929.
- Valor liberado ausente ou R$ 0,00: examinar FSC4; não afirme que não houve crédito sem prova.
- Réu fora de `reus.json`: não preencha CNPJ nem endereço de memória.

## Perguntas típicas (máximo três por rodada)

1. Rito: JEC ou Justiça Comum? (sempre)
2. Cidade e UF do fecho? (sempre)
3. O cliente recebeu algum crédito em conta na data do derivado? Há extrato bancário?
4. O cliente reconhece o contrato-raiz? (a peça não discute a raiz; a resposta evita contradição com outra ação)

## Mapa da checagem pré-recurso (FSC) para o modelo

| Fundamento de sentença | Onde a inicial se previne |
|---|---|
| FSC3, ônus da prova | tópico da inversão do ônus (art. 14, § 3º, do CDC; art. 429, II, do CPC; Tema 1061) e a tabela de documentos |
| FSC7, FSC1, FSC2, autoria | subtópico "nega a manifestação de vontade quanto ao derivado" |
| FSC4, proveito econômico | mesmo subtópico (valor liberado do extrato) e tabela de documentos (comprovante do crédito) |
| FSC6, impugnação tardia | fatos (data da ciência) e tópico de prescrição |
| FSC8, mero dissabor | subtópico do dano extrapatrimonial (Súmula 40 do TJBA, particularidades) |
| FSC9, FSC10, prova técnica | inversão (JEC) ou exibição e perícia com quesitos (Justiça Comum) |
| FSC12, litigância predatória | documentos legíveis e atuais; um processo por benefício + banco + tese; nada sobre outras ações |
| FSC5, FSC11, cessão e mesma data | a tese **é** o caso de mesma data (exclusão e reinclusão); descrever só pelo extrato |
