# Fontes e limites do acervo de consignado

Data da consulta: 2026-10-28; registro conferido em 2026-11-01. **Próxima revisão geral: 23/11/2026** (fim do prazo da MP 1.393/2026).
Níveis de confiança (usados também no painel): VERIFICADO, FEITO, PRESUMIDO, ABERTO.

## 1. Normas

| Arquivo | Fonte oficial | Recorte | Integridade | Nível |
|---|---|---|---|---|
| `normas/cpc.md` | Planalto, Lei 13.105/2015 | integral | página → Markdown: 3.945 parágrafos, 0 ausentes | VERIFICADO |
| `normas/cdc.md` | Planalto, Lei 8.078/1990 (compilado) | integral | 906 parágrafos, 0 ausentes | VERIFICADO |
| `normas/cc.md` | Planalto, Lei 10.406/2002 (compilada) | integral | 6.884 parágrafos, 0 ausentes | VERIFICADO |
| `normas/lei-9099.md` | Planalto, Lei 9.099/1995 | integral | 416 parágrafos, 0 ausentes | VERIFICADO |
| `normas/lei-14905.md` | Planalto, Lei 14.905/2024 | integral | 59 parágrafos, 0 ausentes | VERIFICADO |
| `normas/lei-10741.md` | Planalto, Lei 10.741/2003 | integral | 987 parágrafos, 0 ausentes na passada com letras (105 falsos ausentes na passada estrita, por linha quebrada no HTML) | VERIFICADO |
| `normas/lei-14690.md` | Planalto, Lei 14.690/2023 | integral | 551 parágrafos, 0 ausentes | VERIFICADO |
| `normas/lgpd.md` | Planalto, Lei 13.709/2018 | integral | 890 parágrafos, 0 ausentes | VERIFICADO |
| `normas/res-cmn-4549-consolidada.md` | Banco Central, PDF consolidado (arts. 2º-A a 2º-D incluídos pela Res. CMN 5.112/2023) | integral | extraído do PDF e lido por inteiro; sem segundo texto | FEITO |
| `normas/res-cmn-4753-consolidada.md` | Banco Central, PDF consolidado (`v3`) | integral | extraído do PDF; sem segundo texto | FEITO |
| `normas/in-inss-138-2022-consolidada.md` | gov.br/inss, PDF "com as alterações" | integral; **incorpora até a IN 213, de 17/8/2026** (o PDF oficial no site do INSS se chama "alterada 19-5-2026"; vale o conteúdo, não o nome) | extraído do PDF; arts. 4º, 5º, 18, 34 a 40 conferidos por amostragem; notas das INs 204, 207 e 213 localizadas | FEITO |
| `normas/res-cmn-4935.md` | Banco Central, portal de normativos (id 51464, v2) | integral; **vigente**, só o art. 8º revogado (Res. Conjunta BCB/CMN 17/2025) | texto do campo do portal; sem segundo texto | FEITO |
| `normas/res-cmn-3954-original.md` | Banco Central, PDF original (`v1_O`) | integral, redação original; aplica-se a fatos anteriores a 1º/2/2022; documento consta como revogado pela Res. BCB 277/2022 | extraído do PDF | FEITO |
| `normas/in-inss-143-2023.md` | gov.br/inss (cópia do DOU) | integral | texto lido por inteiro | FEITO |
| `normas/res-bcb-96-2021.md` | Banco Central, portal de normativos (id 51384), página indicada pelo escritório | integral; **vigente** (portal: "Revogado: falso"); conta de pagamento, sem norma de guarda de trilha de contratação de consignado | texto do campo do portal; sem segundo texto | FEITO |
| `normas/in-inss-28-2008-consolidada-2020.md` | gov.br/inss, acervo "legado" (consolidação de 22/7/2020) | integral; **revogada** pela IN 138 (a partir de 13/12/2022) | extraído do PDF; **não incorpora** alterações posteriores a 22/7/2020 | FEITO |
| `normas/in-inss-alteradoras-da-in28-2022.md` | gov.br/inss, INs 131 (25/3/2022), 136 (11/8/2022) e 137 (14/9/2022) | integral | páginas lidas; a IN 134/2022 não consta da listagem oficial lida | FEITO |

Teste de integridade: página oficial → Markdown com `comparar-fonte.js` (passada estrita e passada só com letras; só conta como ausente o que falha nas duas). Para PDF não há comparador automático: o nível é FEITO até haver segunda leitura.

## 2. Jurisprudência

| Arquivo | Fonte | Situação em 2026-10-28 | Nível |
|---|---|---|---|
| `jurisprudencia/tema-929-stj.md` | página oficial do STJ | mérito julgado, **tese não publicada na página**, sem menção a modulação | FEITO (a tese em 4 itens das referências do recurso segue **sem fonte oficial**: `[VERIFICAR]`) |
| `jurisprudencia/tema-1061-stj.md` | página oficial do STJ | trânsito em julgado em 25/05/2022 | FEITO |
| `jurisprudencia/tema-1198-stj.md` | página oficial do STJ | trânsito em julgado; DJe 11/06/2026 | FEITO |
| `jurisprudencia/earesp-738991-stj.md` | Informativo 651/STJ (portal oficial); inteiro teor não lido | Corte Especial, por maioria, j. 20/02/2019, DJe 11/06/2019; prazo decenal da repetição de indébito (caso de telefonia) | FEITO; citar por analogia |
| `jurisprudencia/tema-1414-stj.md` | página do STJ (Precedentes Qualificados), lida diretamente em 28/10/2026 | afetado, **sem tese**; suspensão nacional dos processos de RMC; decisões do TJMG afastam a suspensão em ação de inexistência por fraude (ementa de artigo de doutrina) | VERIFICADO (tema); FEITO (ementa do TJMG) |
| `jurisprudencia/sumula-326-stj.md` | página oficial de súmulas do STJ | vigente (Corte Especial, 22/05/2006) | FEITO |

| `jurisprudencia/sumulas-stj.md` | texto conferido pelo escritório e pelo STJ (43, 54, 297, 362, 479); Súmula 203 com data do DJ conferida no PDF de verbetes do Cortex | FEITO |
| `jurisprudencia/sumulas-tjba-turma-uniformizacao.md` | texto fornecido pelo escritório, súmulas 1 a 55, até 10/11/2025; revogadas: 3 e 22; Súmula 45 alterada em 03/09/2025 | FEITO (conferir no site do TJBA se há súmula posterior) |

## 3. O que NÃO está no acervo (limites do pacote)

| Item | Motivo | Tratamento |
|---|---|---|
| MP 1.393/2026 | **em vigor, não convertida.** Publicada em 25/9/2026 (DOU, Ed. Extra A); prazo de deliberação de 25/9 a 23/11/2026 segundo o Congresso; comissão mista designada em 30/9; 38 emendas; página atualizada em 21/10/2026. Incluiu o art. 28-A na Lei 14.690 e alterou o art. 57 do CDC (multa administrativa; irrelevante para as teses). O art. 28, § 1º da Lei 14.690 não aparece alterado | citar a Lei 14.690 como "texto consolidado pelo Planalto em 28/10/2026, com a MP 1.393/2026 pendente de conversão"; rever a partir de 23/11/2026 |
| Texto da tese do Tema 929 | mérito julgado, acórdão não publicado | **não citar** (protocolo, "Regras de citação e de pedido vigentes") |
| Acórdãos das Súmulas do TJBA e inteiro teor dos Temas | não baixados | citar só enunciado e data de aprovação |
| Res. BCB 277/2022 | norma de câmbio (Lei 14.286). Seu art. 86, IX, **revoga a Res. CMN 3.954/2011**; vigência na data da publicação (31/12/2022), e as exceções de 1º/7/2023 não incluem o art. 86. **Não** lista a Res. CMN 4.935 | para fatos até 31/1/2022 vale o art. 2º da 3.954 original; a partir de 1º/2/2022, o art. 3º da 4.935 |
| IN INSS/PRES 28/2008 | texto obtido, mas a consolidação oficial é de 22/7/2020 e as INs 131, 136 e 137 de 2022 estão em arquivo à parte; a IN 134/2022 (citada por fonte secundária) não consta da listagem oficial lida | para contrato de 2021 a 12/12/2022, conferir as alterações de 2022 antes de citar artigo da IN 28 |
| Inteiro teor do EAREsp 738.991/RS | dados conferidos no Informativo 651/STJ; o acórdão não foi lido; caso de telefonia fixa | citar por analogia, com os dados do Informativo |
