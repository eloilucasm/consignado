# Cálculo do processo 1 (NB 999.999.999-9) — **CÁLCULO A CONFERIR**

Data da peça: 28/10/2026 · última competência de contrato ativo: 09/2026

| Contrato | Status | Início | Fim usado | Qtde | Parcela | Total | Dobro | Vincendas |
|---|---|---|---|---|---|---|---|---|
| 00123456789 | EXCLUÍDO | 03/2019 | 11/2021 | 33 | R$ 142,50 | R$ 4.702,50 | R$ 9.405,00 | 0 (R$ 0,00) |
| 00987654321 | EXCLUÍDO | 05/2022 | 02/2024 | 22 | R$ 98,30 | R$ 2.162,60 | R$ 4.325,20 | 0 (R$ 0,00) |
| 00555111222 | ATIVO | 09/2024 | 09/2026 | 25 | R$ 120,00 | R$ 3.000,00 | R$ 6.000,00 | 59 (R$ 7.080,00) |

- Total descontado: **R$ 9.865,10**
- Restituição em dobro: **R$ 19.730,20**
- Dano moral (fixo): **R$ 20.000,00**
- Proveito econômico declaratório (parcelas vincendas dos ativos): **R$ 7.080,00**
- Valor da causa (dobro + dano moral + proveito declaratório): **R$ 46.810,20 (quarenta e seis mil, oitocentos e dez reais e vinte centavos)**
- Tutela de urgência: SIM, só sobre 00555111222
- Tópico de prescrição (algum desconto com mais de 5 anos): SIM

## Alertas

- Contrato 00123456789: há descontos anteriores a 30/03/2021. Usar o bloco [[SE HÁ DESCONTO ANTES DE 30/03/2021]] do tópico da dobra: o EAREsp 676.608/RS foi modulado para pagamentos posteriores a essa data, e para os anteriores a dobra se apoia só no art. 42, parágrafo único, do CDC (decisão R7, 01/11/2026).
- ANOMALIA: contrato 00555111222 (bloco B) está ATIVO no extrato; a análise só põe contratos não ativos em B e C. Mostrar ao advogado.


## Checagem FSC e VF

| FSC | Status | Achado | Onde a peça trata |
|---|---|---|---|
| FSC1 | OK | negativa específica por contrato no modelo; conferir que cada número aparece na negativa | subtópico da negativa de contratação |
| FSC2 | OK | a parte não usou plataforma digital nem forneceu biometria; autenticação controvertida por antecipação | subtópico da negativa de contratação |
| FSC3 | OK | art. 14, § 3º, do CDC + art. 429, II, do CPC + Tema 1061/STJ antes do art. 6º, VIII | tópico da inversão do ônus da prova |
| FSC4 | OK | 00123456789: liberado R$ 4.800,00; 00987654321: liberado R$ 3.100,00; 00555111222: liberado R$ 4.200,00. Sem extrato bancário (padrão do escritório): a peça afirma que o banco não comprovou o crédito em conta (art. 373, II, do CPC), sem negar o recebimento em nome do cliente; o TED do banco é confrontado na réplica (VF6) | negativa por contrato; inversão do ônus |
| FSC5 | NAO_SE_APLICA | sem origem de migração, portabilidade ou refinanciamento no extrato | — |
| FSC6 | ATIVADO | contrato(s) 00123456789 com desconto iniciado há mais de 5 anos: o tópico de prescrição sustenta o prazo decenal (art. 205 do CC), sem perguntar ao advogado (padrão do escritório, 05/11/2026); registrar a data da ciência | fatos (ciência); tópico de prescrição |
| FSC7 | OK | negativa específica por contrato e pedido de juntada de cada documento com a contestação; o risco maior é da réplica | negativa específica; inversão do ônus |
| FSC8 | OK | natureza alimentar, período e valor vêm do cálculo; sem tentativa administrativa prévia (padrão do escritório) | subtópico do dano extrapatrimonial |
| FSC9 | OK | JEC: sem exibição nem perícia; inversão do ônus e encargo de juntar documentos com a contestação | inversão do ônus |
| FSC10 | PENDENTE_ADVOGADO | pedir que o banco identifique o correspondente e junte a trilha completa; registrar o comprovante de residência do cliente para a réplica | tabela de documentos |
| FSC11 | NAO_SE_APLICA | nenhuma inclusão no mesmo dia nem em até 7 dias de outro contrato do extrato | — |
| FSC12 | PENDENTE_ADVOGADO | documentos de identidade e residência atuais e legíveis; procuração atualizada; um processo por benefício + banco + tese; nada sobre outras ações | lista de documentos |

| VF | Status | Achado |
|---|---|---|
| VF1 | PENDENTE_ADVOGADO | lista dos documentos do cliente anexados à inicial (sem ID: o processo ainda não existe) |
| VF2 | NAO_SE_APLICA | sem documento do banco antes da ação; ficha do contrato fica para a réplica |
| VF3 | NAO_SE_APLICA | extrato sem origem de migração |
| VF4 | NAO_SE_APLICA | sem documento do banco antes da ação; autenticação eletrônica fica para a réplica |
| VF5 | NAO_SE_APLICA | sem documento do banco antes da ação; correspondente bancário fica para a réplica |
| VF6 | NAO_SE_APLICA | extrato bancário não é pedido ao cliente (padrão do escritório); o TED que o banco juntar é confrontado com o valor liberado na réplica |
| VF7 | EXECUTADA | sem repetição de datas entre contratos do mesmo banco |
| VF8 | EXECUTADA | 0 par(es) até 7 dias |
| VF9 | PENDENTE_ADVOGADO | registrar o comprovante de residência (e coordenada, se houver) para a geolocalização da réplica |
