# O que mudou em relação ao modelo AMN de RMC

Fontes comparadas: a skill de RMC do pacote AMN v1.4 (`SKILL.md` e `scripts/gerar.py`) e as 6 petições de RMC geradas pelo AMN em 28/10/2026 (BMG para Francisco, Manoel, Maria, Sueli e Antonia; Daycoval para Raiane). Cada linha diz o que o AMN fazia, o que esta skill faz e por quê.

| # | AMN | Esta skill | Motivo |
|---|---|---|---|
| 1 | Cita o "art. 2º-C da Res. CMN 5.112/2023" como dispositivo autônomo | "art. 2º-C da Res. CMN 4.549/2017, incluído pela Res. CMN 5.112/2023" | o art. 2º-C é artigo da Res. 4.549; a 5.112 só o incluiu (`normas/res-cmn-4549-consolidada.md`) |
| 2 | Não menciona o art. 4º da Res. CMN 4.549, que exclui o cartão com pagamento por consignação | Enfrenta o art. 4º no corpo da peça: no RMC só o mínimo da fatura é consignado, o resto é pago por boleto; logo, a resolução vale (decisão D1 do escritório, 29/10/2026), e o teto também se funda na Lei | o banco invocará o art. 4º; a peça que o ignora perde o argumento no primeiro round |
| 3 | Cita o § 1º do art. 28 da Lei 14.690 truncado ("o total cobrado a título de juros e encargos financeiros não poderá exceder o valor original da dívida") | Transcreve o § 1º literal, com a condição ("se os limites ... não forem aprovados no prazo máximo de 90 dias") e o § 2º | o AMN omitia a condição, que é justamente o ponto de ataque do banco |
| 4 | Não considera o prazo de 90 dias nem o art. 2º-D | Compara a data do refinanciamento com o fim do prazo; refinanciamento anterior a 01/2024 sai com o alerta B2, sem bloqueio, e o modelo traz o argumento do trato sucessivo (decisão D19 do escritório, 29/10/2026) | a petição AMN de referência tem refinanciamento em 10/2023 e marco de 200% em 03/2023, antes de a lei existir |
| 5 | Trata o limite do cartão como "capital originalmente emprestado" sem dizer que é premissa | A peça declara a premissa, marca `[CONFERIR]` e pede as faturas na inversão do ônus | o art. 2º-A, IV, define "valor original da dívida" como o saldo da operação de crédito, não o limite do cartão |
| 6 | "Fraude" e "refinanciamento sigiloso" afirmados como fato | "Sem contato, proposta, nova assinatura ou repasse de numerário", sem marca, e "o banco não comprovou o repasse" no tópico do marco de 200% | o extrato mostra o lançamento, não prova que o cliente nada recebeu: a peça descreve o que o extrato registra e põe no banco a prova do crédito (protocolo, "Não recebimento"; o escritório ajuíza sem o extrato bancário do cliente) |
| 7 | Descrição do IOF como "tributo que somente incide sobre operação de crédito nova" | "tributo que incide sobre operação de crédito" com `[CONFERIR]` | a legislação do IOF não está no acervo |
| 8 | Dano moral de R$ 10.000,00 | **R$ 20.000,00** | decisão do escritório (28/10/2026) |
| 9 | Multa diária de R$ 1.000,00 (tutela) e R$ 2.000,00 (obrigação de fazer) | **R$ 500,00** nas duas | decisão do escritório (28/10/2026) |
| 10 | Dobra com base no "EAREsp 600.663/RS, modulado a partir de 30/03/2021" | Art. 42, parágrafo único, do CDC e a primeira tese do EAREsp 676.608/RS (Corte Especial, DJe 30/03/2021), sem Tema 929; com a frase de modulação conforme a data dos descontos: todos posteriores a 30/03/2021, a modulação alcança toda a repetição; havendo anteriores, a dobra destes se apoia só no art. 42 | decisão do escritório de 29/10/2026 (a página oficial do Tema 929 não traz tese publicada); o EAREsp 676.608/RS está no acervo (`jurisprudencia/earesp-676608-stj.md`) |
| 11 | Correção monetária da restituição pela Súmula 362 (petição) ou 43 (gerador): inconsistente | Súmula 43 para a restituição e Súmula 362 só para o dano extrapatrimonial | a 362 trata da correção do dano moral (acervo) |
| 12 | Valor da causa "art. 292, IV, do CPC" (petição) | art. 292, II (nulidade do ato), VI (soma) e V (dano moral) | o inciso IV trata de ação de divisão, demarcação e reivindicação (`normas/cpc.md`) |
| 13 | Tutela de evidência por "art. 311, II e IV" | art. 311, IV | o inciso II exige tese firmada em julgamento de casos repetitivos ou súmula vinculante; o acervo não traz nenhuma sobre o tema |
| 14 | Cita o "Enunciado Cível nº 26 do FONAJE" para admitir tutela no Juizado | Retirado | fora do acervo |
| 15 | Fundamenta a competência do JEC em salário mínimo de R$ 1.621,00 (Decreto 12.797/2025) | Mantém o cálculo e cita o Decreto 12.797/2025 sem marca; outro ano, decreto daquele ano | decreto no acervo desde 30/10/2026 (`normas/dec-12797.md`); antes, saía com `[CONFERIR]` |
| 16 | "Excelentíssimo(a) Senhor(a) Doutor(a) Juiz(a) de Direito" | Endereçamento impessoal: "AO JUÍZO DA ... VARA ..." | decisão do escritório (28/10/2026) |
| 17 | Sempre Vara Cível ou JEC pela peça; gerador só gera Vara Cível | Pergunta o rito; exibição de documentos só na Justiça Comum; perícia não se pede na inicial em nenhum rito (na Justiça Comum, a necessidade é examinada na réplica; no JEC, a parte se reserva o parecer técnico do art. 35 da Lei 9.099/95) | decisão do escritório |
| 18 | Súmula 479 aplicada "com mais razão quando o ato é de sua própria autoria" sem explicar | Mantida, com o raciocínio explícito: se a fraude de terceiro é fortuito interno, o ato do próprio banco também responde | texto da Súmula 479 no acervo |
| 19 | Planilha com competências ausentes interpoladas na tabela da petição | Ausente registrada como "ausente no extrato", sem valor; total é piso | regra do roteiro AMN, mantida e testada |
| 20 | Gerador monta .docx por XML | Markdown preenchido a partir de `calculo.json`; Word via `tipografia-azul` com realce amarelo nas pendências | decisão do escritório |
| 21 | Honorários "em caso de recurso" e fecho "Termos em que pede e espera deferimento" | Fecho "Termos em que, pede deferimento."; no JEC, sem pedido de custas e honorários (Lei 9.099, art. 55) | padrão do pacote |
| 22 | Subsidiário de lesão (art. 157 do CC) e de revisão contratual | Mantidos sempre, sem marca (decisão do escritório de 10/11/2026) | pedidos subsidiários do modelo AMN; o advogado retira na revisão se não couberem |
| 23 | Não cita a IN 138 do INSS | Subtópico sobre o art. 14 (refinanciamento só se atender às normas do BCB, do CMN e do INSS) e o art. 15, I, II e VIII (biometria, Termo de Consentimento Esclarecido e fatura mensal), com a IN 28/2008, art. 17, para cartão até 12/12/2022; linhas novas na tabela de documentos | a IN 138 trata expressamente de refinanciamento e de RMC/RCC; o AMN só citava a lei e a resolução do CMN |

## O que o script confere e o AMN não conferia

- Refinanciamento anterior ao prazo de 90 dias do art. 28, § 1º (alerta B2).
- Marco de 200% anterior à vigência do teto (alerta).
- Descontinuidade do saldo na troca de registro do cartão (alerta, como no AMN).
- Segunda via do total descontado desde o refinanciamento.
- Teste de regressão com extrato fictício (`testes/caso-ficticio/teste.py`) e verificador do pacote.

## Revisão de 08/11/2026 (comparativo com a peça do advogado de referência)

- Acabamento: "em face" com artigo; tramitação prioritária e pedido "b" condicionais; "confirmada a tutela" só com tutela; linha de tabela condicional por linha inteira; instruções de acabamento no topo do modelo.
- Lei 14.905/2024: só a ressalva "observada a Lei 14.905/2024 a partir de 30/08/2024" nos pedidos de restituição e de dano moral.
- Audiência: tópico de desinteresse só na Justiça Comum, com convite à composição extrajudicial; JEC não trata do assunto.
- Modulação do EAREsp: frase própria quando todos os descontos são posteriores a 30/03/2021.
- Tutela da evidência: o art. 311, IV, passa a ser pedido depois da contestação (não se concede liminarmente).
- Ciência: se há extrato anterior que já registra o refinanciamento, a data da ciência é decisão do advogado.
- Narrativa dos fatos em PRIMEIRO a QUINTO, no estilo da Peça A, só com dados do extrato; tom do "Do direito" mais firme, com citações e marcas intactas.
- Decidido em 08/11/2026 (comparativo E x F, itens 5 e 4.1): (a) **pedido de quitação no marco de 200% (g.2) mantido** depois de retirado por poucas horas: o acervo já tem a sentença de primeiro grau da 12ª VSJE do Consumidor de Salvador (Processo 0209760-63.2026.8.05.0001) que declarou a quitação na competência do marco e deu o dobro só desde o refinanciamento, estrutura idêntica à do modelo. O tópico do marco ganhou um parágrafo que declara a delimitação (repetição só desde o refinanciamento, sem afetar a quitação) e cita a sentença como exemplo de primeiro grau, não como precedente; (b) **subtópico novo** "O refinanciamento sem proposta, sem assinatura e sem repasse é serviço não solicitado" (art. 39, III, do CDC, literal do acervo), com remissão à IN 28, art. 2º, XII, ou à IN 138, art. 14, caput e parágrafo único (refinanciamento "entre o beneficiário e a instituição financeira contratada"; repactuação de "livre negociação entre as partes"), conforme a data, e o pedido g.1 passa a ter o fundamento autônomo (art. 104 do CC; art. 39, III); o parágrafo do Tema 1.414/STJ foi ajustado; (c) **tópico e pedido do "Motivo da Exclusão"** (`[[SE MOTIVO]]`: cartão ativo ou excluído), com a providência na baixa quando o cartão está ativo; `lgpd.md` e o Acórdão 1.094/2026-TCU foram incluídos na skill pelo sincronizador para esse tópico; (d) **início da repetição mantido** na competência do refinanciamento (o `calcular_rmc.py` já conta assim).
- Fica para o advogado, caso a caso: incluir ou não na repetição o desconto da própria competência do refinanciamento (o script e o modelo contam a partir dela), se preferir o critério mais conservador da Peça E (a partir da competência seguinte).

## Revisão de 12/11/2026 (pedido do escritório)

- **Subtópico do teto retirado:** saiu inteiro o subtópico "O teto de juros e encargos do art. 28, § 1º, da Lei 14.690/2023 alcança o cartão consignado" (art. 28, §§ 1º e 2º, resposta ao art. 4º da Res. CMN 4.549, prazo de 90 dias, art. 2º-A e as marcas `[VERIFICAR ANTES DE PROTOCOLAR]` e `[CONFERIR: faturas]` que ele trazia). As linhas 2 e 4 da tabela acima ficam superadas na inicial.
- **Art. 28 no subtópico da nulidade:** o item a) do subtópico "O refinanciamento é nulo por fraude à lei imperativa" transcreve o caput e o § 1º do art. 28 (texto do acervo), no lugar de "acima transcrito"; o item b) deixou de remeter ao art. 4º.

## Revisão de 13/11/2026 (restituição a partir do marco)

- **Restituição em dobro desde o mês seguinte ao marco de 200%** (decisão do escritório, mesma da sessão de 12/11/2026 em outro computador): o pedido de restituição, o tópico da dobra ("Os valores descontados depois de atingido o teto devem ser restituídos em dobro"), o efeito da nulidade e o subtópico do marco deixaram de contar "desde o refinanciamento". `cartao.py` calcula `total_pos_marco`; `calcular_rmc.py` grava `inicio_restituicao` e `total_pos_marco` e usa esse total no dobro e no valor da causa. O resumo financeiro ganhou a linha "Descontado desde [INÍCIO DA RESTITUIÇÃO]". Caso fictício: restituição desde 09/2025, dobro R$ 1.410,00, valor da causa R$ 23.210,00.
- **Bloco `[[SE PRESCRIÇÃO]]`**: prazo decenal do art. 205 do CC com o EAREsp 738.991/RS (incluído no acervo do rmc), art. 169 do CC e, subsidiariamente, art. 27 do CDC com `[DECISÃO DO ADVOGADO]`, copiado da sessão de 12/11/2026 a pedido do escritório. O script alerta acima de 5 anos (inclui o bloco) e acima de 10 anos (prescrição parcial mesmo pelo prazo decenal). **Diverge do protocolo** (prescrição sempre decenal, sem pedido subsidiário pelo art. 27): ver PAINEL.

## O que continua em aberto

- Premissa de fato da D1: conferir nas faturas que só o mínimo é consignado.
- **D18**: o leitor do extrato (`cartao.py`) foi testado só com PDF fictício; conferir a primeira leitura real contra o PDF do INSS.
- Jurisprudência sobre o marco de 200% em cartão consignado: o acervo tem só a sentença de primeiro grau da 12ª VSJE do Consumidor de Salvador (Processo 0209760-63.2026.8.05.0001, `jurisprudencia/sentenca-0209760-2026-tjba-rmc.md`), que o modelo cita como exemplo, não como precedente; nenhum acórdão de Turma Recursal, de tribunal ou do STJ sobre o teto em cartão consignado, e por isso o tópico do teto mantém `[VERIFICAR ANTES DE PROTOCOLAR]`. Conferir o trânsito em julgado da sentença antes de citá-la.
