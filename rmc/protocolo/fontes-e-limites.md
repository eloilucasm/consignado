# Fontes e limites da skill rmc

Data da consulta: 2026-10-28. Níveis de confiança: VERIFICADO, FEITO, PRESUMIDO, ABERTO.

## 1. Normas

| Arquivo | Fonte oficial | Recorte | Integridade | Nível |
|---|---|---|---|---|
| `normas/cpc.md` | Planalto, Lei 13.105/2015 | integral | 3.945 parágrafos, 0 ausentes | VERIFICADO |
| `normas/cdc.md` | Planalto, Lei 8.078/1990 (compilado) | integral | 906 parágrafos, 0 ausentes | VERIFICADO |
| `normas/cc.md` | Planalto, Lei 10.406/2002 (compilada) | integral | 6.884 parágrafos, 0 ausentes | VERIFICADO |
| `normas/lei-9099.md` | Planalto, Lei 9.099/1995 | integral | 416 parágrafos, 0 ausentes | VERIFICADO |
| `normas/lei-10741.md` | Planalto, Lei 10.741/2003 | integral | 987 parágrafos, 0 ausentes na passada com letras | VERIFICADO |
| `normas/lei-14905.md` | Planalto, Lei 14.905/2024 | integral | 59 parágrafos, 0 ausentes | VERIFICADO |
| `normas/lei-14690.md` | Planalto, Lei 14.690/2023 | integral; DOU de 3.10.2023, edição extra | 551 parágrafos, 0 ausentes | VERIFICADO |
| `normas/res-cmn-4549-consolidada.md` | Banco Central, PDF consolidado (arts. 2º-A a 2º-D incluídos pela Res. CMN 5.112/2023) | integral | extraído do PDF e lido por inteiro; sem segundo texto | FEITO |
| `normas/in-inss-138-2022-consolidada.md` | gov.br/inss, PDF "com as alterações" | integral; incorpora até a IN 213, de 17/8/2026; **o art. 15 traz redações sucessivas (taxa de juros, limites)** | extraído do PDF; arts. 14 a 16 lidos por inteiro | FEITO |
| `normas/in-inss-143-2023.md` | gov.br/inss (cópia do DOU) | integral | texto lido por inteiro | FEITO |
| `normas/in-inss-28-2008-consolidada-2020.md` | gov.br/inss, acervo "legado" (consolidação de 22/7/2020) | integral; **revogada** pela IN 138 (a partir de 13/12/2022); só para cartão constituído até essa data | extraído do PDF; **não incorpora** alterações posteriores a 22/7/2020 | FEITO |
| `normas/in-inss-alteradoras-da-in28-2022.md` | gov.br/inss, INs 131, 136 e 137 de 2022 | integral | páginas lidas | FEITO |

## 2. Jurisprudência

| Arquivo | Fonte | Situação em 2026-10-28 | Nível |
|---|---|---|---|
| `jurisprudencia/tema-929-stj.md` | página oficial do STJ | mérito julgado, **tese não publicada na página**, sem menção a modulação | FEITO (`[VERIFICAR]` em toda citação) |
| `jurisprudencia/tema-1414-stj.md` | página do STJ (Precedentes Qualificados), lida diretamente em 28/10/2026 | afetado, **sem tese**; suspensão nacional dos processos pendentes, exceto cumprimentos de sentença (Segunda Seção, 08/04/2026) | VERIFICADO |
| `jurisprudencia/sumula-326-stj.md` | página oficial de súmulas do STJ | vigente; trata de sucumbência | FEITO |
| `jurisprudencia/sumulas-stj.md` | texto conferido pelo escritório e pelo STJ (43, 54, 297, 362, 479) | vigentes | FEITO |
| `jurisprudencia/sumulas-tjba-turma-uniformizacao.md` | texto fornecido pelo escritório, súmulas 1 a 55, até 10/11/2025 | revogadas: 3 e 22; Súmula 45 alterada em 03/09/2025 | FEITO (conferir no site do TJBA se há súmula posterior) |

## 3. O que NÃO está no acervo (limites da skill)

| Item | Motivo | Tratamento |
|---|---|---|
| **Res. CMN 5.112/2023 como ato próprio** | só o texto consolidado da Res. 4.549, que incorpora os arts. 2º-A a 2º-D. **Não existe "art. 2º-C da Res. 5.112" como dispositivo autônomo** | citar "art. 2º-C da Res. CMN 4.549/2017, incluído pela Res. CMN 5.112/2023" |
| **Art. 4º da Res. CMN 4.549** | afasta a resolução dos cartões cujo contrato preveja pagamento da fatura **por consignação em folha** (texto literal no acervo) | decisão D1 do escritório (29/10/2026): no RMC só o mínimo é consignado, logo o art. 4º não afasta a resolução; ver `references/01-tese-e-roteiro.md`, B1 |
| **Art. 2º-D da Res. CMN 4.549** | os arts. 2º-A a 2º-C valem **só para operações realizadas após o prazo de 90 dias do art. 28, § 1º, da Lei 14.690** | o script alerta quando o refinanciamento é anterior; contagem do prazo `[VERIFICAR]` |
| **Condição do art. 28, § 1º, da Lei 14.690** | o teto só vale "se os limites do caput não forem aprovados" em 90 dias; a Res. CMN 5.112 (21/12/2023) pode ter aprovado limites dentro do prazo | a peça responde em alternativa (art. 2º-C ou § 1º, mesmo teto); ver B3 |
| Lei 10.820/2003 (consignado) e normas do INSS sobre cartão consignado | a Lei 10.820 está **disponível** em `references/normas/lei-10820.md` desde 01/11/2026 (VERIFICADO); o modelo não a cita. As normas do INSS sobre cartão não foram baixadas | Lei 10.820: citar pelo arquivo, se o advogado quiser. Normas do INSS sobre cartão: `[CONFERIR]` |
| Jurisprudência de RMC (STJ, TJBA, Turmas Recursais) | **nenhum acórdão sobre o marco de 200% está no acervo**; os modelos AMN não citam julgado sobre ele | tópico de precedentes só com o que o advogado trouxer e conferir |
| MP 1.393/2026 | **em vigor, não convertida**; incluiu o art. 28-A na Lei 14.690. O art. 28, § 1º aparece sem alteração | citar a Lei 14.690 como "texto consolidado pelo Planalto em 28/10/2026, com a MP 1.393/2026 pendente de conversão"; rever a partir de 23/11/2026 |
| Texto da tese do Tema 929 | mérito julgado, acórdão não publicado | **não citar** (protocolo, "Regras de citação e de pedido vigentes") |
| Extrato real do INSS com cartão | só o extrato fictício do teste | conferir a primeira leitura real contra o PDF (D18) |
