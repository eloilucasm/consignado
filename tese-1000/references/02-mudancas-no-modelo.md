# O que mudou em relação ao modelo do escritório e ao AMN

Fontes comparadas: a inicial "Tese 1000 - Maria x BNP" (PDF do escritório, 15/10/2026) e o gerador da skill de Tese 1000 do pacote AMN v1.4 (`SKILL.md` e `scripts/gerar.py`). Cada linha diz o que o modelo anterior fazia, o que esta skill faz e por quê.

| # | Modelo anterior | Esta skill | Motivo |
|---|---|---|---|
| 1 | Aplica a IN 138/2022 a reaverbação de 2018 ("publicada em 13 de dezembro de 2022, período em que tais reaverbações irregulares vêm sendo praticadas") | Escolhe a norma pela data: IN 28/2008 até 12/12/2022; IN 138 desde 13/12/2022. O script grava `regime_norma` | a IN 138 vige desde 13/12/2022 (publicação conferida no DOU pelo escritório; art. 40, decisão D30); antes, vigorava a IN 28 (`normas/`) |
| 2 | "O sistema do INSS, por desenho próprio, não permite reaverbação sob o mesmo número. Trata-se de barreira técnica" | **Mantido** (decisão do escritório, D28, 29/10/2026), ao lado da IN 28, art. 30, IV e § 2º, com `[CONFERIR]` da fonte | o escritório decidiu manter; nenhuma norma do acervo afirma a barreira técnica, então a peça pede a fonte (manual da Dataprev ou ofício do INSS) |
| 3 | "Prática sistêmica de instituições financeiras, identificada e mapeada por doutrina e jurisprudência especializadas"; "dispensa demonstração de dolo" | Retirado. O extrato prova este caso | sem fonte no acervo; FSC12 (litigância predatória): não afirmar volume de ações ou padrão do banco |
| 4 | Tabela da IN 138 cita o art. 5º, § 1º ("autorização vale enquanto subscrita pelo titular, não persistindo por sucessão") como violado pelo reuso de autorização | Retirado | o § 1º trata de sucessão aos pensionistas e dependentes (texto no acervo) |
| 5 | Pedido final de "retificação do histórico ... para que conste que o contrato derivado foi excluído por inexistência de relação jurídica" | Preenchimento do campo "Motivo da Exclusão" com "Por força de decisão judicial", mantida a "Origem da Exclusão" (mesma providência dos demais modelos), mais a obrigação de não averbar de novo o contrato-raiz sob qualquer sufixo | a providência do campo é objetiva e verificável; a vedação ataca a repetição da prática |
| 6 | Dobra: "ainda que os descontos tenham ocorrido antes de 30/03/2021, termo inicial da modulação do EAREsp 676.608/RS, a má-fé está caracterizada pelo modus operandi" | Art. 42, parágrafo único, do CDC, sem Tema 929 e sem modulação | decisão do escritório de 29/10/2026 (a página do Tema 929 traz mérito julgado e tese não publicada) |
| 7 | Prescrição: "prazo decenal ... EAREsp 676.608/RS (Og Fernandes, 21/10/2020) e EAREsp 738.991/RS" | **Prazo decenal mantido** (art. 205 do CC; decisão do escritório, D28), com o EAREsp 738.991/RS por analogia e `[VERIFICAR]`; o EAREsp 676.608/RS não é citado para a prescrição; termo inicial é decisão do advogado | o EAREsp 676.608 é o precedente da dobra, não da prescrição; o 738.991 é de telefonia |
| 8 | Dano moral de R$ 10.000,00, "in re ipsa" | **R$ 20.000,00**; Súmula 40/TJBA com as particularidades; Súmula 326/STJ só para o valor estimativo | decisão do escritório; dano *in re ipsa* é questão aberta no Tema 1414/STJ (III.d) |
| 9 | Afirma que a jurisprudência do STJ e dos Tribunais estaduais reconhece a presunção do dano moral, sem citar julgado | **Mantido** (decisão do escritório, D28) com `[VERIFICAR ANTES DE PROTOCOLAR]`: indicar os julgados | nenhum julgado no acervo; a Súmula 40 do TJBA diz o contrário (desconto indevido, por si só, não é dano moral); o banco a invocará |
| 10 | Valor da causa: dobro + R$ 10.000,00 | dobro + R$ 20.000,00 (art. 292 do CPC), calculado pelo script | decisão do escritório |
| 11 | Gratuidade pelo "art. 5º, LXXIV, da Constituição Federal" | arts. 98 e 99 do CPC **e** art. 5º, LXXIV, da CF (decisão do escritório, D28) | na montagem a CF não estava no acervo; desde 01/11/2026 está em `references/normas/cf88.md` |
| 12 | "Citação ... para comparecer à audiência de conciliação" e "dispensando-se a prova pericial" | Pergunta o rito: JEC (sem perícia; documentos como ônus do banco) ou Justiça Comum (exibição e perícia com quesitos) | decisão do escritório |
| 13 | Sem tutela; pedido final só de retificação do histórico | Tutela de urgência condicional ao derivado **ativo**, só sobre os ativos; campo "Motivo da Exclusão" ("Por força de decisão judicial") com multa de R$ 500,00; obrigação de não fazer contra nova averbação do contrato-raiz sob qualquer sufixo | regra do escritório (tutela só sobre ativos) e utilidade da providência |
| 14 | Diagramas ("Anatomia da reaverbação" e "Linha do tempo") em imagem | **Imagens**, geradas por `scripts/diagramas_1000.py` a partir do `calculo.json` (decisão do escritório, D28); a tabela fica como reserva se o Pillow não estiver disponível | os dados vêm só do extrato, e a legenda diz que a figura não introduz fato novo |
| 15 | Altera a narrativa para "contrato ressuscitado" sem medir o intervalo | O script mede o intervalo (mesmo dia, até 30 dias, mais de 30 dias, antes da exclusão); "antes da exclusão" bloqueia a narrativa | fato do extrato |
| 16 | "Excelentíssimo"/"Vossa Excelência" e "mui respeitosamente" | Tratamento impessoal | decisão do escritório |
| 17 | Fecho: "Termos em que, pede deferimento" com data fixa | Pergunta a cidade e a UF; data do dia da produção | padrão do pacote |
| 18 | Tópico de precedentes ausente | Tópico completo (art. 489, § 1º, VI; *distinguishing*; *overruling*), com ponte para o JEC | padrão de peças do escritório (decisão de 28/10/2026) |
| 19 | Pede ao banco atual (BNP) a restituição de descontos feitos pelo banco anterior (Cetelem, código 739), sem tratar da troca de titularidade | Retirado: o escritório informou em 29/10/2026 que, na Tese 1000, o contrato não é reaverbado por outro banco; o caso com dois bancos fica fora do escopo e o script alerta | decisão D29 do escritório; sem precedente no acervo sobre a responsabilidade do banco que recebeu a carteira |

## O que o script confere e o AMN não conferia

- Regime da norma pela data da averbação do derivado.
- Segunda via do total descontado.
- Derivado averbado antes da exclusão da raiz (alerta).
- Intervalo e norma medidos pela **primeira** averbação do derivado, em qualquer banco (na troca de titularidade, o registro do banco atual é posterior).
- Mesmo número em outro banco: fora do escopo; descontos do outro banco **não** somados (alerta).
- Mesmo número em outros bancos (alerta).
- Teste de regressão com extrato fictício (`testes/caso-ficticio/teste.py`) e verificador do pacote.

## O que continua em aberto

- Jurisprudência sobre contrato derivado com sufixo: nenhuma no acervo.
- D18: o leitor do extrato foi testado só com PDF fictício; conferir a primeira leitura real contra o PDF do INSS.
- O modelo trata um contrato-raiz por processo. Se o cliente tiver derivados de duas raízes, separe os processos.
