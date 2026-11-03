# O que mudou em relação ao modelo AMN de RMC

Fontes comparadas: a skill de RMC do pacote AMN v1.4 (`SKILL.md` e `scripts/gerar.py`) e as 6 petições de RMC geradas pelo AMN em 28/10/2026 (BMG para Francisco, Manoel, Maria, Sueli e Antonia; Daycoval para Raiane). Cada linha diz o que o AMN fazia, o que esta skill faz e por quê.

| # | AMN | Esta skill | Motivo |
|---|---|---|---|
| 1 | Cita o "art. 2º-C da Res. CMN 5.112/2023" como dispositivo autônomo | "art. 2º-C da Res. CMN 4.549/2017, incluído pela Res. CMN 5.112/2023" | o art. 2º-C é artigo da Res. 4.549; a 5.112 só o incluiu (`normas/res-cmn-4549-consolidada.md`) |
| 2 | Não menciona o art. 4º da Res. CMN 4.549, que exclui o cartão com pagamento por consignação | Enfrenta o art. 4º no corpo da peça: no RMC só o mínimo da fatura é consignado, o resto é pago por boleto; logo, a resolução vale (decisão D1 do escritório, 29/10/2026), e o teto também se funda na Lei | o banco invocará o art. 4º; a peça que o ignora perde o argumento no primeiro round |
| 3 | Cita o § 1º do art. 28 da Lei 14.690 truncado ("o total cobrado a título de juros e encargos financeiros não poderá exceder o valor original da dívida") | Transcreve o § 1º literal, com a condição ("se os limites ... não forem aprovados no prazo máximo de 90 dias") e o § 2º | o AMN omitia a condição, que é justamente o ponto de ataque do banco |
| 4 | Não considera o prazo de 90 dias nem o art. 2º-D | Compara a data do refinanciamento com o fim do prazo; refinanciamento anterior a 01/2024 sai com o alerta B2, sem bloqueio, e o modelo traz o argumento do trato sucessivo (decisão D19 do escritório, 29/10/2026) | a petição AMN de referência tem refinanciamento em 10/2023 e marco de 200% em 03/2023, antes de a lei existir |
| 5 | Trata o limite do cartão como "capital originalmente emprestado" sem dizer que é premissa | A peça declara a premissa, marca `[CONFERIR]` e pede as faturas na inversão do ônus | o art. 2º-A, IV, define "valor original da dívida" como o saldo da operação de crédito, não o limite do cartão |
| 6 | "Fraude" e "refinanciamento sigiloso" afirmados como fato | "Sem contato, proposta, nova assinatura ou repasse" com `[CONFIRMAR COM O CLIENTE]` na ausência de crédito | o extrato mostra o lançamento, não prova que o cliente nada recebeu |
| 7 | Descrição do IOF como "tributo que somente incide sobre operação de crédito nova" | "tributo que incide sobre operação de crédito" com `[CONFERIR]` | a legislação do IOF não está no acervo |
| 8 | Dano moral de R$ 10.000,00 | **R$ 20.000,00** | decisão do escritório (28/10/2026) |
| 9 | Multa diária de R$ 1.000,00 (tutela) e R$ 2.000,00 (obrigação de fazer) | **R$ 500,00** nas duas | decisão do escritório (28/10/2026) |
| 10 | Dobra com base no "EAREsp 600.663/RS, modulado a partir de 30/03/2021" | Art. 42, parágrafo único, do CDC, sem Tema 929 e sem modulação | decisão do escritório de 29/10/2026 (a página oficial do Tema 929 não traz tese publicada) |
| 11 | Correção monetária da restituição pela Súmula 362 (petição) ou 43 (gerador): inconsistente | Súmula 43 para a restituição e Súmula 362 só para o dano extrapatrimonial | a 362 trata da correção do dano moral (acervo) |
| 12 | Valor da causa "art. 292, IV, do CPC" (petição) | art. 292, II (nulidade do ato), VI (soma) e V (dano moral) | o inciso IV trata de ação de divisão, demarcação e reivindicação (`normas/cpc.md`) |
| 13 | Tutela de evidência por "art. 311, II e IV" | art. 311, IV | o inciso II exige tese firmada em julgamento de casos repetitivos ou súmula vinculante; o acervo não traz nenhuma sobre o tema |
| 14 | Cita o "Enunciado Cível nº 26 do FONAJE" para admitir tutela no Juizado | Retirado | fora do acervo |
| 15 | Fundamenta a competência do JEC em salário mínimo de R$ 1.621,00 (Decreto 12.797/2025) | Mantém o cálculo e cita o Decreto 12.797/2025 sem marca; outro ano, decreto daquele ano | decreto no acervo desde 30/10/2026 (`normas/dec-12797.md`); antes, saía com `[CONFERIR]` |
| 16 | "Excelentíssimo(a) Senhor(a) Doutor(a) Juiz(a) de Direito" | Endereçamento impessoal: "AO JUÍZO DA ... VARA ..." | decisão do escritório (28/10/2026) |
| 17 | Sempre Vara Cível ou JEC pela peça; gerador só gera Vara Cível | Pergunta o rito; exibição e perícia contábil com quesitos só em Justiça Comum | decisão do escritório |
| 18 | Súmula 479 aplicada "com mais razão quando o ato é de sua própria autoria" sem explicar | Mantida, com o raciocínio explícito: se a fraude de terceiro é fortuito interno, o ato do próprio banco também responde | texto da Súmula 479 no acervo |
| 19 | Planilha com competências ausentes interpoladas na tabela da petição | Ausente registrada como "ausente no extrato", sem valor; total é piso | regra do roteiro AMN, mantida e testada |
| 20 | Gerador monta .docx por XML | Markdown preenchido a partir de `calculo.json`; Word via `tipografia-azul` com realce amarelo nas pendências | decisão do escritório |
| 21 | Honorários "em caso de recurso" e fecho "Termos em que pede e espera deferimento" | Fecho "Termos em que, pede deferimento."; no JEC, sem pedido de custas e honorários (Lei 9.099, art. 55) | padrão do pacote |
| 22 | Subsidiário de lesão (art. 157 do CC) e de revisão contratual | Mantidos, marcados `[DECISÃO DO ADVOGADO]` | não há fonte no acervo sobre lesão no caso; o advogado decide |
| 23 | Não cita a IN 138 do INSS | Subtópico sobre o art. 14 (refinanciamento só se atender às normas do BCB, do CMN e do INSS) e o art. 15, I, II e VIII (biometria, Termo de Consentimento Esclarecido e fatura mensal), com a IN 28/2008, art. 17, para cartão até 12/12/2022; linhas novas na tabela de documentos | a IN 138 trata expressamente de refinanciamento e de RMC/RCC; o AMN só citava a lei e a resolução do CMN |

## O que o script confere e o AMN não conferia

- Refinanciamento anterior ao prazo de 90 dias do art. 28, § 1º (alerta B2).
- Marco de 200% anterior à vigência do teto (alerta).
- Descontinuidade do saldo na troca de registro do cartão (alerta, como no AMN).
- Segunda via do total descontado desde o refinanciamento.
- Teste de regressão com extrato fictício (`testes/caso-ficticio/teste.py`) e verificador do pacote.

## O que continua em aberto

- Premissa de fato da D1: conferir nas faturas que só o mínimo é consignado.
- **D18**: o leitor do extrato (`cartao.py`) foi testado só com PDF fictício; conferir a primeira leitura real contra o PDF do INSS.
- Jurisprudência sobre o marco de 200% em cartão consignado: nenhuma no acervo.
