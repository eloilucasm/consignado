# Roteiro da réplica e verificações forenses VF1 a VF9 sobre a contestação

Consulta: 29/10/2026. Origem: verificações forenses e catálogo de fundamentos de sentença da skill de recurso inominado de consignado, aplicados ao momento da **réplica**, que é a última oportunidade de impugnar os documentos do banco antes da sentença. É aqui que se evita o fundamento de sentença mais perigoso, o FSC7 ("não impugnado especificamente"): documento particular não impugnado se considera autêntico (CPC, art. 411, III), e a impugnação de autenticidade precisa de argumentação específica (art. 436, parágrafo único).

## 1. Quando a réplica é a peça certa

- Há contestação do banco nos autos, com ou sem documentos.
- O processo é de consignado do INSS (não contratado, migrado, Tese 1000 ou RMC).
- Prazo: na Justiça Comum, 15 dias (CPC, arts. 350 e 351; a falsidade de documento, no mesmo prazo, art. 430). No JEC, a forma e o prazo são os fixados pelo juízo, muitas vezes em audiência `[CONFERIR no despacho]`.

## 2. Etapas

1. **Escopo (Etapa 0).** Leia a **inicial** primeiro: contratos impugnados, rito, pedidos. Se houver `dossie-do-caso.json` da inicial, carregue-o (checagem FSC, residência, extrato bancário). Leia o extrato do INSS: origem da averbação de cada contrato ("Migrado do contrato…" ativa a VF3).
2. **Índice dos autos (VF1).** Monte o índice real: ID, data, tipo, quem juntou, páginas. Abra a primeira página de cada documento do banco antes de afirmar o que ele é: o nome do arquivo não prova o conteúdo.
3. **Pontos da contestação.** Liste **cada** alegação de fato e **cada** preliminar, com ID e página, e associe a resposta em `02-defesas-do-banco.md`. Nada fica sem resposta, e nada se responde que o banco não alegou.
4. **Fichas e quadro de indícios (VF2 a VF8).** Registre os dados dos documentos do banco em `contestacao.json` (formato abaixo) e rode `scripts/fichas.py`. Confira cada linha do quadro contra a página citada.
5. **Autenticação e geolocalização (VF4 e VF9).** Se o log traz IP, rode `scripts/ip_check.py`; se traz coordenadas, IP ou Cidade-UF, rode `scripts/geo_check.py` com a residência da parte autora. Item de REVISÃO HUMANA OBRIGATÓRIA fica fora da peça até o advogado decidir.
6. **Cartão de pausa.** Antes de redigir, mostre ao advogado: escopo, contratos sem defesa, quadro de indícios por gravidade, achados de VF4/VF9, pontos da contestação × resposta, riscos (FSC) e as decisões pendentes. **Só redija depois da confirmação.**
7. **Redação** pelo modelo `assets/modelo-replica-consignado.md` e portões do protocolo.

## 3. Formato do `contestacao.json`

Um arquivo por processo. Todo dado vem dos autos, com a fonte (ID e página); campo desconhecido fica fora ou `null`.

```json
{
  "processo": "0000000-00.2026.8.05.0000",
  "rito": "jec",
  "autor": {"nb": "1234567890", "email": "maria@exemplo.com", "telefone": "73999990000",
            "endereco": "Rua A, 10, Ilhéus", "cep": "45650000", "estado_civil": "viúva", "uf": "BA"},
  "impugnados": ["00123456789", "00987654321"],
  "pontos": [
    {"defesa": "P2", "id_pagina": "ID 200 p. 2", "resumo": "incompetência do JEC: a causa exigiria perícia"},
    {"defesa": "M3", "id_pagina": "ID 200 p. 8", "resumo": "o valor foi creditado na conta da autora", "contratos": ["00123456789"]},
    {"defesa": "NOVO", "id_pagina": "ID 200 p. 12", "resumo": "alegação fora do catálogo"}
  ],
  "contratos_defendidos": [
    {"contrato": "00123456789", "id_pagina": "ID 201 p. 3",
     "ccb_juntada": true, "assinatura": "eletronica",
     "datas": {"emissao_ccb": "10/03/2024", "assinatura_ccb": "10/03/2024", "trilha": "11/03/2024"},
     "cadastro": {"nb": "1234567890", "email": "outro@exemplo.com", "telefone": "11988887777", "fonte": "ID 202 p. 1"},
     "ted": {"valor": 4800.00, "data": "12/03/2024", "conta_mesma_do_beneficio": true, "fonte": "ID 203 p. 1"},
     "log": {"plataforma": "BemSign", "hash": "ab12…", "ip": "10.0.0.5", "selfie_id": "ID 204 p. 2",
             "cidade_uf": null, "coordenadas": null, "fonte": "ID 204 p. 1"},
     "correspondente": {"nome": "Promotora X", "cnpj": "00.000.000/0001-00", "uf": "SP",
                        "contrato_correspondencia": false, "fonte": "ID 205 p. 1"},
     "cessao": null}
  ]
}
```

`pontos`: uma entrada por preliminar ou alegação da contestação, com o código da linha de `references/02-defesas-do-banco.md` (`P1` a `P9`, `M1` a `M12`) ou `NOVO`, o ID e a página e, se a alegação for de um contrato só, `contratos`. Alimenta o mapa de argumentos (`mapa-argumentos.md`); ponto `NOVO` sai com `[DECISÃO DO ADVOGADO]`.

Para contrato migrado, `cessao` traz `instrumento`, `identifica_contrato`, `assinaturas` e `notificacao` (verdadeiro ou falso) e `fonte`. Para a VF9, use o formato de entrada do `geo_check.py` (exemplo em `testes/caso-ficticio/geo-entrada.json`).

## 4. As verificações na réplica

| VF | O que fazer | Quem faz | Alimenta |
|---|---|---|---|
| VF1 | índice real dos autos, com a primeira página de cada documento do banco visualizada | advogado/Claude | todas |
| VF2 | ficha de cada contrato impugnado: instrumento juntado?, tipo de assinatura, coerência de datas (CCB antes da trilha?), NB e quadro comparativo de dados cadastrais (CCB × documentos da parte autora) | `fichas.py` | FSC1, FSC7 |
| VF3 | cessão (só com origem "Migrado" ou cessão alegada): eixo existência (instrumento que identifique o contrato, assinaturas) e eixo eficácia (notificação ao devedor, art. 290 do CC) | `fichas.py` | FSC5 |
| VF4 | autenticação: listar **todos** os campos do log (IP, Cidade-UF, biometria, hash, plataforma); IP privado é lacuna do documento (indício RELEVANTE, nunca "impossível para cliente residencial"); biometria sem relatório técnico é selfie | `ip_check.py` + leitura | FSC2, FSC10 |
| VF5 | correspondente: sede, CNPJ, contrato de correspondência; o banco responde por ele | `fichas.py` | FSC10 |
| VF6 | TED ou PIX × valor liberado do extrato do INSS: liberado zero, valor divergente ou coincidente; conta receptora | `fichas.py` | FSC4, FSC12 |
| VF7 | análise cruzada: mesmo hash (crítico), mesma selfie e mesmo IP (critérios propostos) em contratos diferentes | `fichas.py` | FSC2, FSC5, FSC10 |
| VF8 | contratos incluídos no mesmo dia ou em até 7 dias, em qualquer banco do extrato (reforço) | `fichas.py` (via `escrutinio.py`) | FSC11 |
| VF9 | geolocalização: posição registrada no log × **residência** da parte autora (ID e página); classificação COMPATIVEL, DIVERGENTE, informativo ou REVISÃO HUMANA OBRIGATÓRIA | `geo_check.py` | FSC2, FSC10 |

## 5. Gravidade dos indícios

| Nível | Quando | Exemplos |
|---|---|---|
| CRÍTICO | objetivo e autônomo | CCB não juntada; TED divergente do liberado ou com liberado zero; ausência de instrumento de cessão ou de notificação; correspondente sem contrato comprovado; campo de localização vazio; mesmo hash em contratos diferentes; GPS divergente da residência (VF9) |
| RELEVANTE | pesa com contexto | assinatura manuscrita impugnada; datas incoerentes; dado cadastral divergente (e-mail ou telefone de terceiro comprovado sobe a CRÍTICO, por decisão do advogado); IP privado no log; conta receptora diferente da do benefício; correspondente em outra UF |
| REFORÇO | não decide sozinho | contratos na mesma data; IP repetido em contratos diferentes |
| PROCESSUAL | efeito de processo | contrato impugnado sem defesa (art. 341 do CPC) |
| ALERTA_CONTRA | pesa contra a parte autora | TED coincidente com o liberado, na conta do benefício (Súmula 42 do TJBA): decisão do advogado antes de redigir |

A escala vem da skill de recurso e é **proposta a validar** pelo escritório. Indício fraco isolado não prova nada; a peça trabalha a convergência.

## 6. Regras da réplica

1. **Ponto a ponto.** Cada alegação e cada documento do banco recebe resposta própria, com ID e página. Nunca agrupar argumentos do banco em bloco genérico.
2. **Impugnação específica** (CPC, art. 436, parágrafo único): a autenticidade se impugna com os elementos objetivos de cada documento, nunca com fórmula genérica.
3. **Contratos não se misturam.** Cada número é um contrato; o banco que defende outro contrato não defendeu o impugnado.
4. **Nada sobre imagem não vista.** Selfie, assinatura e tela só se descrevem depois de visualizadas.
5. **Geolocalização:** "o log juntado pelo réu registra", sem afirmar a fonte que o log não diz nem a posição da parte autora; a referência é sempre a **residência** (ID e página), e assim se chama na peça; dado sem ID e página não entra; REVISÃO HUMANA OBRIGATÓRIA não entra sem decisão.
6. **Rito:** no JEC, nada de pedido de exibição, perícia ou ofício (a lacuna do banco vira argumento); na Justiça Comum, reiterar exibição e perícia com quesitos (sem isso, não há cerceamento a alegar no recurso, FSC9).
7. **Sem fato sobre outras ações** e sem nada sobre a colheita da procuração (FSC12).
8. **Valores da inicial** não mudam: a réplica reitera os pedidos.
9. **Súmula 42 do TJBA:** se o crédito chegou à conta, a réplica não nega o recebimento; trata o valor conforme a decisão do advogado.

## 7. Projeção dos fundamentos de sentença (o que a réplica previne)

| FSC | Pergunta antes de entregar |
|---|---|
| FSC1, FSC7 | Cada documento do banco foi impugnado especificamente? Cada contrato impugnado tem resposta própria? |
| FSC2, FSC10 | Os achados de VF4, VF5 e VF9 estão na peça, com ID e página? |
| FSC3 | A réplica reafirma o ônus legal (art. 14, § 3º, do CDC; art. 429, II, do CPC; Tema 1061/STJ)? |
| FSC4 | O TED foi confrontado com o liberado? O caso de valores coincidentes teve decisão do advogado? |
| FSC5 | Na migração, os dois eixos da cessão foram examinados? |
| FSC6 | A alegação de silêncio ou anuência foi respondida (CC, art. 111; autorização expressa)? |
| FSC8 | As particularidades do dano estão reafirmadas? |
| FSC9 | Justiça Comum: perícia e exibição reiteradas, com quesitos? |
| FSC11 | Contratos da mesma data descritos só pelo extrato? |
| FSC12 | Nada sobre outras ações; documentos atualizados juntados, se o banco os contestou? |
