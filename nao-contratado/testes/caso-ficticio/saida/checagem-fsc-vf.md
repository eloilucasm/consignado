# Checagem FSC e VF: processo 1 (nao-contratado) em 28/10/2026

Registro de trabalho: não entra na peça. Formato e regras em `assets/escrutinio-fsc-vf.md`.

| FSC | Status | Achado | Onde a peça trata |
|---|---|---|---|
| FSC1 | OK | negativa específica por contrato no modelo; conferir que cada número aparece na negativa | subtópico da negativa de contratação |
| FSC2 | OK | a parte não usou plataforma digital nem forneceu biometria; autenticação controvertida por antecipação | subtópico da negativa de contratação |
| FSC3 | OK | art. 14, § 3º, do CDC + art. 429, II, do CPC + Tema 1061/STJ antes do art. 6º, VIII | tópico da inversão do ônus da prova |
| FSC4 | ATIVADO | 00123456789: liberado R$ 4.800,00; 00987654321: liberado R$ 3.100,00; 00555111222: liberado R$ 4.200,00. extrato bancário do mês da averbação ainda não informado. Risco da Súmula 42/TJBA se o crédito chegou à conta e a peça nega tudo [DECISÃO DO ADVOGADO: devolução, depósito ou compensação] | fatos; tabela de documentos; pedido |
| FSC5 | NAO_SE_APLICA | sem origem de migração, portabilidade ou refinanciamento no extrato | — |
| FSC6 | ATIVADO | contrato(s) 00123456789 com desconto iniciado há mais de 5 anos: tratar prescrição (decisão do advogado) e a data da ciência | fatos (ciência); tópico de prescrição |
| FSC7 | OK | negativa específica por contrato e pedido de juntada de cada documento com a contestação; o risco maior é da réplica | negativa específica; inversão do ônus |
| FSC8 | OK | natureza alimentar, período e valor vêm do cálculo; sem tentativa administrativa prévia (padrão do escritório) | subtópico do dano extrapatrimonial |
| FSC9 | OK | JEC: sem exibição nem perícia; inversão do ônus e encargo de juntar documentos com a contestação | inversão do ônus |
| FSC10 | PENDENTE_ADVOGADO | pedir que o banco identifique o correspondente e junte a trilha completa; registrar a residência do cliente com ID e página para a réplica | tabela de documentos |
| FSC11 | NAO_SE_APLICA | nenhuma inclusão no mesmo dia nem em até 7 dias de outro contrato do extrato | — |
| FSC12 | PENDENTE_ADVOGADO | documentos de identidade e residência atuais e legíveis; procuração atualizada; um processo por benefício + banco + tese; nada sobre outras ações | lista de documentos |

| VF | Status | Achado |
|---|---|---|
| VF1 | PENDENTE_ADVOGADO | índice dos documentos do cliente (ID provisório de cada um) |
| VF2 | NAO_SE_APLICA | sem documento do banco antes da ação; ficha do contrato fica para a réplica |
| VF3 | NAO_SE_APLICA | extrato sem origem de migração |
| VF4 | NAO_SE_APLICA | sem documento do banco antes da ação; autenticação eletrônica fica para a réplica |
| VF5 | NAO_SE_APLICA | sem documento do banco antes da ação; correspondente bancário fica para a réplica |
| VF6 | PENDENTE_ADVOGADO | pedir ao cliente o extrato bancário do mês da averbação de cada contrato (Súmula 42/TJBA) |
| VF7 | EXECUTADA | sem repetição de datas entre contratos do mesmo banco |
| VF8 | EXECUTADA | 0 par(es) até 7 dias |
| VF9 | PENDENTE_ADVOGADO | registrar a residência com ID e página (e coordenada, se houver) para a geolocalização da réplica |

**Portão 3:** PENDENTE (4 FSC ativado(s) ou pendente(s): FSC4, FSC6, FSC10, FSC12)

**Para a réplica:** FSC7 (impugnar um a um os documentos que o banco juntar), FSC1/FSC2 (autenticidade), FSC4 e VF6 (confrontar o TED com o valor liberado), FSC10 e VF9 (correspondente, IP e geolocalização com a residência registrada).

## Linha do tempo

| Data | Evento | Fonte | Efeito |
|---|---|---|---|
| 20/02/2019 | Averbação do contrato 00123456789 | extrato do INSS, contrato 00123456789 | norma do INSS aplicável: IN 28/2008 |
| 03/2019 | Primeiro desconto do contrato 00123456789 | extrato do INSS, contrato 00123456789 | início da repetição do indébito |
| 01/10/2021 | Limite de 5 anos antes da peça | cálculo | descontos anteriores: tópico de prescrição (FSC6) |
| 11/2021 | Último desconto contado do contrato 00123456789 | extrato do INSS, contrato 00123456789 | fim da contagem do cálculo |
| 15/12/2021 | Exclusão do contrato 00123456789 (Exclusão Banco) | extrato do INSS, contrato 00123456789 |  |
| 12/04/2022 | Averbação do contrato 00987654321 | extrato do INSS, contrato 00987654321 | norma do INSS aplicável: IN 28/2008 |
| 05/2022 | Primeiro desconto do contrato 00987654321 | extrato do INSS, contrato 00987654321 | início da repetição do indébito |
| 02/2024 | Último desconto contado do contrato 00987654321 | extrato do INSS, contrato 00987654321 | fim da contagem do cálculo |
| 03/03/2024 | Exclusão do contrato 00987654321 (Exclusão INSS) | extrato do INSS, contrato 00987654321 |  |
| 09/2024 | Primeiro desconto do contrato 00555111222 | extrato do INSS, contrato 00555111222 | início da repetição do indébito |
| 05/09/2024 | Averbação do contrato 00555111222 | extrato do INSS, contrato 00555111222 | norma do INSS aplicável: IN 138/2022 |
| 09/2026 | Último desconto contado do contrato 00555111222 | extrato do INSS, contrato 00555111222 | fim da contagem do cálculo |
| 28/10/2026 | Data da peça | argumento --data do cálculo | contrato ativo conta até a competência anterior |
| 28/10/2026 | Emissão do extrato do INSS | extrato do INSS, primeira página | ciência dos descontos (padrão do escritório); FSC6 |
