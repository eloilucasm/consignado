# Quadro de fatos de consignado — modelo

O script de cálculo grava, ao lado da peça, o registro `checagem-fsc-vf.md` e o `dossie-do-caso.json` (quadro + cálculo + checagem), que o advogado leva para a réplica ou o recurso. Copie este quadro para a conversa, preencha o que já souber e reapresente-o atualizado a cada rodada. Não precisa de arquivo. Estados: `confirmado` (há documento), `relatado` (relato do cliente), `inferido`, `desconhecido`.

**Caso (identificador pseudônimo):** ______  **Processo (benefício + banco + tese):** ______  **Data do resumo:** ______

## A. Autor e benefício

| # | Fato | Estado | Valor | Proveniência (documento e página, ou "relato") |
|---|---|---|---|---|
| 1 | Nome, gênero (pelo documento, nunca pelo nome), data de nascimento e idade | | | |
| 2 | Município e endereço da **residência** (comprovante atual e legível) | | | |
| 3 | Benefício (espécie e NB) | | | |
| 4 | Gratuidade (declaração e procuração) e prioridade de tramitação (60 anos ou mais) | | | |
| 5 | Analfabeto ou assinatura a rogo? | | | |

## B. Banco e tese

| # | Fato | Estado | Valor | Proveniência |
|---|---|---|---|---|
| 6 | Banco réu (razão social e CNPJ de `reus.json`) | | | |
| 7 | Tese (não contratado, migrado, Tese 1000, RMC) e bloco da análise | | | |
| 8 | Contrato está **na análise e no termo**? | | | |
| 9 | Rito: JEC ou Justiça Comum (**perguntado ao advogado**; a skill sugere pelo valor e pela prova) e órgão competente | | | |
| 10 | Outro processo contra o mesmo banco (benefício diferente ou tese diferente)? Para o tópico de litispendência | | | |

## C. Contratos (uma linha por contrato)

| # | Contrato | Tipo | Inclusão | Início/Fim dos descontos | Parcela | Valor liberado (extrato) | Status (ativo/excluído) | Motivo da exclusão (extrato) | Estado | Proveniência |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | | | | | | | | | | |

Para migrado: contrato de origem, banco de origem e banco de destino. Para Tese 1000: contrato-raiz, contrato derivado (sufixo), datas de exclusão e de reaverbação e intervalo. Para RMC: capital (limite), data de inclusão, histórico mês a mês, competência do refinanciamento e IOF.

## C2. Linha do tempo

O script de cálculo monta a linha do tempo a partir do extrato e a grava na seção "Linha do tempo" do `checagem-fsc-vf.md` e na chave `cronologia` do `dossie-do-caso.json`: averbação de cada contrato (com a norma do INSS da data), primeiro e último desconto, exclusão e motivo, emissão do extrato (ciência), limite de 5 anos da prescrição e data da peça; no migrado, a primeira averbação no banco de origem; na Tese 1000, averbação e exclusão da raiz e a reaverbação com o intervalo; no RMC, inclusão do cartão, fim do prazo de 90 dias da Lei 14.690/2023, marco de 200% e refinanciamento. Copie a tabela para cá e acrescente o que só os documentos mostram (crédito em conta, contato do banco, ajuizamento de outra ação). Data que decide norma, prazo ou tese e não tem documento fica `desconhecido` no quadro.

| Data | Evento | Documento (ID e página) | Efeito jurídico |
|---|---|---|---|
| | | | |

## D. Prova e autoria (o que o banco poderá alegar)

| # | Fato | Estado | Valor | Proveniência |
|---|---|---|---|---|
| 12 | Cliente nega ter contratado? Em que termos (para impugnação específica) | | | |
| 13 | Valor liberado do extrato × crédito em conta alegado pelo banco (portabilidade pura?) | | | |
| 14 | Data em que o cliente soube dos descontos (ciência): padrão = data de emissão do extrato | | | |
| 15 | — (não se aplica: o escritório não faz tentativa administrativa prévia) | | | |
| 16 | Contratos incluídos no mesmo dia ou em intervalo curto | | | |
| 17 | Correspondente bancário identificado? | | | |
| 18 | Assinatura manuscrita ou eletrônica? Há perícia ou prova técnica a pedir (Justiça Comum)? | | | |
| 19 | Cidade e UF do fecho (**perguntado ao advogado**) | | | |
| 20 | **Extrato bancário** do cliente do mês da averbação de cada contrato: houve crédito? de quanto? (VF6; Súmula 42/TJBA). **Recomendado** antes de ajuizar: sem ele, fica a pendência e o advogado decide se ajuíza. Se houver crédito, o tratamento (devolução, depósito em juízo ou compensação) é decisão do advogado | | | |
| 21 | O banco entregou contrato, trilha de assinatura ou dossiê **antes da ação** (só se os autos trouxerem; o escritório não faz tentativa administrativa prévia)? (VF2, VF4, VF5) | | | |
| 22 | Residência com ID e página do comprovante e, se o advogado der, coordenada copiada de um mapa (VF9, para a réplica) | | | |
| 23 | Índice dos documentos do cliente, com a identificação provisória de cada um (VF1) | | | |

## E. Pendências, fontes e portões

**Pendências** (o que falta e quem pode fornecer):
1.
2.
3.

**Fontes usadas** (norma, artigo, data da consulta do arquivo):
-

**Portões:** 1 Fatos ☐  2 Prova e cálculo ☐  3 Contraditório (checagem pré-recurso) ☐  4 Revisão final ☐

**Resumo de continuidade** (cole numa nova conversa para retomar): ______
