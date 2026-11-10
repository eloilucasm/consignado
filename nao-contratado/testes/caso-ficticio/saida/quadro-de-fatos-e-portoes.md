# Quadro de fatos e portões — piloto (CASO FICTÍCIO)

**Caso:** MGES-2026 · **Processo:** NB 999.999.999-9 + BANCO DAYCOVAL S.A. + não contratado · **Data do resumo:** 28/10/2026 (conferido contra o modelo atual em 10/11/2026)

## Perguntas feitas ao advogado antes de gerar (premissas do teste)

| Pergunta | Resposta assumida |
|---|---|
| Rito: JEC ou Justiça Comum? (valor da causa R$ 46.810,20; sugestão: JEC, se couber nos 40 salários mínimos: R$ 64.840,00 em 2026, Decreto 12.797/2025) | **JEC** |
| Confirma tutela sobre o contrato 00555111222, que a análise listou em B mas o extrato mostra ativo (ANOMALIA)? | **Sim**, só sobre o ativo |

Juízo e cidade do fecho não se perguntam: vêm do `foro` do `calculo.json`, pelo endereço do autor (Vara do Sistema dos Juizados Especiais da Comarca de Ilhéus; fecho Ilhéus - BA).

## A. Autor e benefício

| # | Fato | Estado | Valor | Proveniência |
|---|---|---|---|---|
| 1 | Nome, gênero, nascimento | confirmado | Maria das Graças Exemplo Santos, F, 12/04/1958 (68 anos) | qualificacao.json (documentos pessoais fictícios, ID 3) |
| 2 | Residência | confirmado | Ilhéus/BA | comprovante fictício, ID 4 |
| 3 | Benefício | confirmado | NB 999.999.999-9, espécie 41 (aposentadoria por idade) | extrato, ID 5 |
| 4 | Gratuidade e prioridade (≥ 60 anos) | confirmado / inferido | gratuidade na procuração; 68 anos | ID 6, ID 3 |
| 5 | Analfabeta ou assinatura a rogo? | desconhecido | não informado | perguntar ao cliente |

## B. Banco e tese

| # | Fato | Estado | Valor | Proveniência |
|---|---|---|---|---|
| 6 | Banco réu | confirmado | 707 – Banco Daycoval S.A. | extrato; `reus.json` |
| 7 | Tese e bloco | confirmado | não contratado (B, C, B) | análise |
| 8 | Contratos na análise **e** no termo | confirmado | os três | análise × termo |
| 9 | Rito | confirmado (pelo advogado) | JEC | resposta do advogado |
| 10 | Outro processo contra o mesmo banco | desconhecido | nenhum informado | confirmar |

## C. Contratos

Ver `calculo.md`. Os três têm valor liberado no extrato (R$ 4.800,00; R$ 3.100,00; R$ 4.200,00). Sem extrato bancário (padrão do escritório), a peça afirma que cabe ao banco comprovar o crédito em conta (art. 373, II, do CPC), sem negar o recebimento. Sem sinais de cadeia de refinanciamentos (nenhuma averbação em par, parcela repetida ou valor liberado zero): o bloco `[[SE HÁ CADEIA]]` não entra. Há desconto anterior a 30/03/2021 (contrato 00123456789): entra o ramo da dobra pelo art. 42, parágrafo único, para esses descontos.

## D. Prova e autoria

| # | Fato | Estado | Valor | Proveniência |
|---|---|---|---|---|
| 12 | Nega ter contratado | relatado | nega os três contratos | análise; termo |
| 13 | Valor liberado × crédito em conta | não pedido | extrato bancário não é pedido ao cliente (padrão do escritório) | protocolo, "Não recebimento" |
| 14 | Ciência dos descontos | confirmado | 28/10/2026, data de emissão do extrato (protocolo); o relato de 10/08/2026 pelo Meu INSS não tem documento | extrato; análise (relato) |
| 15 | Reclamação prévia ao banco | registrado | 02/09/2026, consumidor.gov.br, sem resposta; não usada na peça (premissa do teste: sem tentativa administrativa) | ID 7 |
| 16 | Contratos no mesmo dia ou próximos | confirmado | não | extrato |
| 17 | Correspondente identificado | desconhecido | | |
| 18 | Assinatura manuscrita ou eletrônica | desconhecido | a peça impugna, por antecipação, a assinatura de qualquer instrumento que o banco juntar | |
| 19 | Juízo e cidade do fecho | confirmado | Vara do Sistema dos Juizados Especiais de Ilhéus; Ilhéus - BA | `foro` do `calculo.json` (endereço do autor) |

## Pendências

1. Confirmar a litispendência (fato 10).
2. Se a cliente tem assinatura manuscrita em algum documento do banco (fato 18).
3. Número da vara: sai em branco (`__ª`) do endereçamento da tabela do TJBA, até a distribuição.

## Portões

1. **Fatos e enquadramento: PASSOU com pendência.** Rito confirmado; juízo e fecho pelo `foro` do `calculo.json`; contratos conferidos contra termo e análise; status tirado do extrato; competência pela tabela do TJBA (Ilhéus, com Vara do Sistema); idade 68 anos; litispendência `desconhecido` (confirmar). Anomalia de bloco B ativo mostrada e tutela confirmada.
2. **Prova e cálculo: PASSOU com pendência.** Cálculo pelas duas vias (33, 22 e 25 parcelas; total do dobro R$ 19.730,20; valor da causa R$ 46.810,20), marcado `[CÁLCULO A CONFERIR]`. O crédito em conta fica a cargo do banco (art. 373, II, do CPC).
3. **Contraditório (checagem pré-recurso): PENDENTE.** FSC3 (art. 14, § 3º; art. 429, II; Tema 1061) feito. FSC7/1/2/4 (negativa por contrato; valor liberado) feito. FSC6 ATIVADO (desconto desde 03/2019): tópico de prescrição com o prazo decenal (EAREsp 676.608/RS, segunda tese, e EAREsp 738.991/RS); ciência pela data de emissão do extrato. FSC8 (Súmula 40, natureza alimentar, valor e duração, pessoa idosa) feito. FSC9 (JEC: sem exibição, perícia ou ofício) feito. FSC10 e FSC12 pendentes com o advogado (correspondente e trilha; documentos legíveis, um processo por NB + banco + tese, nada sobre outras ações).
4. **Revisão final: PENDENTE.** Restam três `[CÁLCULO A CONFERIR]` (tabela dos fatos, total do dobro, valor da causa) e um `[CONFERIR]` (prazo da IN 143/2023 em relação ao contrato de 05/09/2024). O Tema 929/STJ não é fundamento (a dobra se apoia no art. 42, parágrafo único, do CDC e no EAREsp 676.608/RS); a Lei 14.905/2024 entra só como ressalva nos pedidos de juros ("observada a Lei 14.905/2024 a partir de 30/08/2024"), sem marca. O trecho do TRF-4 está no acervo (VERIFICADO) e sai sem marca. Signatários e intimações são os padrão do escritório.

**Resultado:** minuta **não pronta para protocolo** (há marcas pendentes), mas sem FALHA estrutural.

## Resumo de continuidade

Caso MGES-2026: inicial de não contratado contra o Daycoval, três contratos, JEC, Ilhéus. Falta: confirmação de litispendência, conferência do cálculo e do prazo da IN 143/2023, FSC10 e FSC12 com o advogado.
