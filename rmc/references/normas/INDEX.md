# Normas e jurisprudência desta skill: o que serve para quê

Consulta de 28/10/2026. Veja `MAPA.md` para achar o artigo pelo conteúdo (uma linha por dispositivo, com a linha do arquivo) e `ESTRUTURA.md` para localizar por Livro, Título e Capítulo, `../jurisprudencia/INDEX.md` para achar precedente por assunto e `../../protocolo/fontes-e-limites.md` para o que **não** está aqui.

## Normas (`references/normas/`)

| Arquivo | Serve para | Dispositivos que o modelo usa |
|---|---|---|
| `lei-14690.md` | o teto de juros e encargos do cartão (art. 28, §§ 1º e 2º); **o § 1º só vale depois de 90 dias da publicação** | art. 28 |
| `res-cmn-4549-consolidada.md` | definições (art. 2º-A), renegociação (art. 2º-C), vigência no tempo (art. 2º-D) e **exclusão do cartão consignado (art. 4º)** | arts. 2º-A, 2º-B, 2º-C, 2º-D e 4º |
| `cdc.md` | relação de consumo, responsabilidade, dobra, inversão, informação | arts. 6º, III, V e VIII; 14 e § 3º; 39, V; 42, parágrafo único; 47 |
| `cpc.md` | gratuidade, prioridade, ônus, exibição, tutela, coisa julgada, precedentes, valor | arts. 85, 98, 99, 105, 292, 294, 300, 311, 337, 369, 373, 396 a 404, 489, 497, 505, 508, 537, 1.048 |
| `cc.md` | nulidade por fraude à lei, restituição, boa-fé, lesão | arts. 157, 166, 168, 169, 182, 186, 422 |
| `in-inss-138-2022-consolidada.md` | contratos e refinanciamentos a partir de 11/11/2022; **art. 14 (refinanciamento só se atender às normas do BCB, do CMN e do INSS)**; art. 15 (RMC/RCC: biometria, Termo de Consentimento Esclarecido, fatura mensal) | arts. 14 e 15 (I, II e VIII) |
| `in-inss-28-2008-consolidada-2020.md` | cartão constituído até 10/11/2022 (**revogada**; consolidação de 22/7/2020, sem as alterações de 2022) | arts. 15 a 17 |
| `in-inss-alteradoras-da-in28-2022.md` | INs 131, 136 e 137 de 2022 | conferir antes de citar artigo da IN 28 |
| `in-inss-143-2023.md` | prorrogou o prazo da biometria da IN 138 | art. 2º |
| `lei-9099.md` | JEC: competência, gratuidade, honorários, perícia informal | arts. 3º, 35, 54, 55 |
| `lei-10741.md` | prioridade de tramitação da pessoa idosa | art. 71 |
| `lei-14905.md` | juros e correção (Código Civil) | arts. 2º e 5º (data dos efeitos: `[CONFERIR]`) |

## Jurisprudência (`references/jurisprudencia/`)

Por assunto da peça: `references/jurisprudencia/INDEX.md`. Por arquivo:

| Arquivo | Serve para | Situação |
|---|---|---|
| `tema-929-stj.md` | repetição em dobro | tese **não publicada**; citar com `[VERIFICAR ANTES DE PROTOCOLAR]` |
| `tema-1061-stj.md` | ônus da autenticidade da assinatura | trânsito em julgado; pouco usado no RMC |
| `sumulas-stj.md` | Súmulas 43, 54, 203, 297, 362 e 479 | conferidas |
| `sumula-326-stj.md` | sucumbência no dano moral | **não** usar para caráter punitivo |
| `sumulas-tjba-turma-uniformizacao.md` | Súmulas 30 e 40 (dano), 41 (cartão consignável), 33 (juros), 46 a 54 (litigância) | até 10/11/2025; 3 e 22 revogadas |
| `fonaje-enunciados-civeis.md` | tutela, competência e valor da causa no JEC | enunciados 1 a 178, vigentes e revogados separados; **não** são súmulas |

## Dados (`references/dados/`)

`reus.json` (CNPJ e endereço de 5 réus; réu ausente vira `[CONFERIR]`), `tjba_comarcas.json` (município → comarca) e `trf1_jurisdicao.json` (município → subseção, para a Caixa).
