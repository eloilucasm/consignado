<!--
MODELO — INICIAL DE NULIDADE DE REFINANCIAMENTO DE CARTÃO CONSIGNADO (RMC/RCC), com a tese do teto da Lei 14.690/2023

Como usar (instruções para quem redige; apague este comentário na peça):
- Preencha os campos [PREENCHER: ...] com o quadro de fatos e o calculo.json (scripts/calcular_rmc.py). Campo sem fonte vira [CONFERIR: ...].
- Blocos entre [[SE ...]] e [[FIM]] entram só quando a condição vale. Apague os marcadores.
- Números, datas de competência e valores vêm de calculo.json. Nunca refaça a conta de cabeça. A planilha mensal vem pronta em calculo.md.
- Se calculo.json trouxer alerta B2 (refinanciamento anterior a 01/2024), leve-o ao advogado. A minuta **não** é bloqueada: o escritório decidiu em 29/10/2026 manter a tese do teto (references/01-tese-e-roteiro.md, B1 a B4).
- Não digite número de tópico: a tipografia-azul numera. Remissão interna: "tópico ..." calculado depois de fechada a estrutura.
- Títulos de tópico (#) no formato "Da/Do/Dos…"; subtópicos (##) em frase completa.
- Citação de lei: texto literal do acervo. Marcas [VERIFICAR ANTES DE PROTOCOLAR] ficam no ponto exato.
- Perguntar ao advogado ANTES de gerar: rito (JEC ou Justiça Comum), cidade/UF do fecho e ação anterior sobre o cartão.
- Forma, endereçamento, qualificação e pedidos de rotina: assets/padrao-pecas.md (prevalece em caso de conflito).
-->

[[SE JEC]] [PREENCHER: `jec.enderecamento` da comarca em references/dados/tjba_unidades.json; comarca do município em tjba_comarcas.json] [[SE JUSTIÇA COMUM]] [PREENCHER: `comum.enderecamento` da comarca em references/dados/tjba_unidades.json] [[FIM]]

[[SE CAIXA]] Substituir o endereçamento por: AO JUÍZO DA [N]ª VARA FEDERAL DA SUBSEÇÃO JUDICIÁRIA DE [subseção da tabela TRF1] - BAHIA [[FIM]]

**EMENTA:** Cartão de crédito consignado (RMC/RCC). [Beneficiário/Beneficiária] do INSS. Refinanciamento do saldo pelo banco sem manifestação de vontade e sem repasse de numerário. Total pago superior a 200% do capital antes do refinanciamento. Teto de juros e encargos do art. 28, § 1º, da Lei 14.690/2023. Nulidade (art. 166, VI, do CC). Repetição do indébito em dobro. Dano extrapatrimonial.[[SE COISA JULGADA]] Fato novo e objeto distinto de ação anterior.[[FIM]][[SE TUTELA]] Tutela de urgência para suspensão imediata dos descontos.[[FIM]]

**[NOME DO AUTOR]**, [nacionalidade], [estado civil], [profissão], [inscrito/inscrita] no CPF sob nº [CPF], RG sob nº [RG], [beneficiário/beneficiária] do INSS (NB [NB], [ESPÉCIE DO BENEFÍCIO]), [residente e domiciliado/domiciliada] na [ENDEREÇO], CEP [CEP], cidade de [CIDADE]/[UF], por seu advogado que esta subscreve (procuração anexa), vem, respeitosamente, perante este Juízo, propor a presente

## Ação Declaratória de Nulidade de Refinanciamento de Cartão Consignado, Cumulada com Repetição do Indébito em Dobro, Obrigação de Fazer e Indenização por Danos Extrapatrimoniais[[SE TUTELA]], com Pedido de Tutela Provisória de Urgência[[FIM]]

em face **[RÉU]**, [descrição do réu de references/dados/reus.json: pessoa jurídica, CNPJ e endereço], [[SE JEC]] pelo procedimento da Lei nº 9.099/95, [[FIM]] pelos seguintes fatos, fundamentos e razões de direito.

# Da gratuidade da justiça

A parte autora não tem condições de arcar com as despesas do processo, uma vez que são insuficientes seus recursos financeiros para pagar todas as despesas processuais, inclusive o recolhimento das custas iniciais.

Requer sejam deferidos os benefícios da gratuidade da justiça, o que faz por declaração de seus advogados, nos termos do art. 99, § 4º, c/c o art. 105, in fine, ambos do CPC, prerrogativa que consta do instrumento procuratório anexo. Presume-se verdadeira a alegação de insuficiência deduzida por pessoa natural (art. 99, § 3º, do CPC). Seu benefício tem base de cálculo de [BASE DE CÁLCULO DO BENEFÍCIO, do extrato], [[SE CONSIGNAÇÕES RELEVANTES]] dos quais [VALOR] mensais estão comprometidos em consignações [FONTE: extrato] [[FIM]].[[SE JEC]] No Juizado Especial, o acesso em primeiro grau independe do pagamento de custas, taxas ou despesas (art. 54 da Lei 9.099/95).[[FIM]]

# Da tramitação prioritária

[[SE IDADE ≥ 60]] Conforme documento pessoal anexo, a parte autora é pessoa idosa e faz jus à prioridade na tramitação (art. 1.048, I, do CPC; art. 71 da Lei 10.741/2003 — Estatuto da Pessoa Idosa). [[FIM]]

[[SE JEC]]
# Da competência do Juizado Especial

A causa é de competência do Juizado Especial Cível (art. 3º, I, da Lei 9.099/95): o valor da causa, [VALOR DA CAUSA], é inferior a 40 (quarenta) salários mínimos, que, à razão de [SALÁRIO MÍNIMO VIGENTE NO AJUIZAMENTO: Decreto 12.797/2025, R$ 1.621,00, para 2026; outro ano, decreto daquele ano], correspondem a [40 × SALÁRIO MÍNIMO: R$ 64.840,00 em 2026]. A prova é documental (o extrato oficial do INSS) e a tese se apura pela soma dos descontos mensais ali registrados. [CONFERIR: se o advogado entender necessária perícia contábil, a causa é complexa e o rito deve ser a Justiça Comum.]
[[FIM]]

[[SE COISA JULGADA]]
# Da inaplicabilidade da coisa julgada

[CONFERIR: números, datas e resultado das ações anteriores (processos nº [PROCESSOS ANTERIORES]); o texto abaixo pressupõe que elas discutiram a contratação original do cartão.]

Foram propostas ações anteriores sobre este cartão, nas quais se discutiu a validade da contratação originária. Não há coisa julgada, por faltar a identidade de causa de pedir e de pedido exigida pelo art. 337, §§ 1º a 4º, do CPC. Pedem-se a apreciação e, se for o caso, a distinção do caso concreto (art. 489, § 1º, VI, do CPC), por seis razões:

1. **Fato posterior e autônomo.** As ações anteriores trataram da validade do contrato de [DATA DE INCLUSÃO DO CARTÃO]. Esta ação trata do refinanciamento de [COMPETÊNCIA DO REFINANCIAMENTO], ato unilateral do banco, praticado depois, sem manifestação de vontade da parte autora. A coisa julgada não impede novo pedido fundado em fato superveniente (art. 505, I, do CPC).
2. **Objeto diverso.** Antes se pediu a nulidade ou a revisão do contrato original. Aqui se pede a declaração de nulidade do refinanciamento e de seus consectários.
3. **Marco normativo posterior.** A tese se funda na Lei 14.690/2023 (DOU de 03/10/2023) e nos arts. 2º-A a 2º-D da Res. CMN 4.549, incluídos pela Res. CMN 5.112/2023 [CONFERIR: a data de ajuizamento das ações anteriores; só vale se foram propostas antes dessas normas].
4. **A sentença anterior não autorizou alteração futura.** Se o contrato original foi reconhecido válido nas condições em que foi pactuado, o banco não podia modificá-lo unilateralmente depois.
5. **O refinanciamento não foi objeto da ação anterior.** Ainda que a sentença seja posterior a ele, o ato não constou da causa de pedir. A coisa julgada cobre o que foi decidido, e as alegações que poderiam ter sido deduzidas em outra causa de pedir não a atingem (art. 508 do CPC) [CONFERIR: leitura do art. 508 contra a sentença anterior].
6. **As ações são compatíveis.** Esta ação aceita a sentença anterior e dela decorre: se o contrato era válido como foi pactuado, o refinanciamento unilateral é ilícito.
[[FIM]]

[[SE LITISPENDÊNCIA]]
# Da ausência de litispendência

Gerar conforme o quadro de fatos (item 10): objeto exclusivo do NB deste processo; se há ação contra o mesmo banco em outro benefício, indicar a espécie e o NB de cada um e que são benefícios e contratos distintos; se a outra ação tem tese diferente, dizer que os contratos, a causa de pedir e os pedidos não se confundem. Fundamento: art. 337, §§ 1º a 3º, do CPC. Não informar quantas ações a parte autora ou o escritório têm.
[[FIM]]

# Dos fatos

## O cartão consignado e os descontos mensais

A parte autora é [beneficiária/beneficiário] de [ESPÉCIE DO BENEFÍCIO] (NB [NB]), com base de cálculo de [BASE DE CÁLCULO]. Em [DATA DE INCLUSÃO, do extrato] foi averbado no benefício o contrato de [Cartão de Crédito com Reserva de Margem Consignável (RMC) / Cartão Consignado de Benefício (RCC)] nº [NÚMERO DO CARTÃO], do [RÉU], com limite de **[LIMITE]**.

**Premissa do cálculo.** O extrato do INSS não informa o valor efetivamente utilizado pela parte autora. Adota-se, como capital originalmente disponibilizado, o limite do cartão registrado no INSS, [LIMITE] [CONFERIR: premissa; substituir pelo valor efetivamente sacado, se as faturas ou o relato do cliente o mostrarem]. O banco detém as faturas e, no tópico da inversão do ônus, é instado a juntá-las.

Desde então, descontos mensais foram feitos no benefício a título de "desconto de cartão ([RMC/RCC])". [[SE RELATO DE BOA-FÉ]] A parte autora relata que acreditava que os descontos amortizavam a dívida. [[FIM]]

Em [DATA DE EMISSÃO], ao analisar o Histórico de Empréstimo Consignado, a parte autora tomou conhecimento do refinanciamento descrito abaixo.

## O extrato oficial do INSS prova o refinanciamento

Em [COMPETÊNCIA DO REFINANCIAMENTO], sem contato, proposta, nova assinatura ou repasse de numerário à parte autora, o banco registrou no sistema do INSS/DATAPREV nova operação sobre o cartão nº [NÚMERO DO CARTÃO]. O Histórico de Empréstimo Consignado, emitido em [DATA DE EMISSÃO] (ID [__], p. [__]), registra, para o contrato de id [ID DA LINHA DO EXTRATO], os seguintes sinais:

a) **Salto do "utilizado no mês".** [[SE HÁ VALORES ANTERIORES]] Nas competências anteriores, o campo registra apenas [UTILIZADO NOS MESES ANTERIORES]. [[FIM]] Em [COMPETÊNCIA DO REFINANCIAMENTO] passa a [UTILIZADO NO MÊS], [idêntico/praticamente idêntico] ao saldo devedor então registrado ([SALDO DEVEDOR]), como se tivesse sido novo saque, sem solicitação ou assinatura da parte autora.

b) **IOF lançado na mesma competência**, no valor de [IOF], tributo que incide sobre operação de crédito. [CONFERIR: a incidência de IOF sobre a operação, nos termos da legislação tributária; não consta do acervo.]

[[SE JUROS CAEM]]
c) **Queda da taxa de juros.** A taxa mensal, de [MENOR TAXA DOS VIZINHOS]% ou mais nas competências próximas, cai para [TAXA DO REFINANCIAMENTO]% na competência do refinanciamento.
[[FIM]]

O documento é oficial e sua autenticidade pode ser conferida pelo código do rodapé. A prova é a soma dos lançamentos que ele traz.

## O custo real da dívida

A tabela abaixo reúne os descontos mensais do cartão nº [NÚMERO DO CARTÃO], extraídos do Histórico de Empréstimo Consignado emitido em [DATA DE EMISSÃO][[SE HISTÓRICO COMPLEMENTADO]] e complementados por [FONTE: HISCRE / faturas], anexo [ID] [[FIM]], de [PRIMEIRA COMPETÊNCIA] a [ÚLTIMA COMPETÊNCIA].[[SE HÁ COMPETÊNCIAS AUSENTES]] As competências [COMPETÊNCIAS AUSENTES] não constam do documento e foram registradas como ausentes, sem interpolação; o total é, portanto, o piso do efetivamente pago.[[FIM]]

[COLAR AQUI a tabela "Planilha" de calculo.md: mês/ano, desconto, acumulado, % do capital, com o refinanciamento e o marco de 200% marcados]

*Fonte: Histórico de Empréstimo Consignado do INSS, emitido em [DATA DE EMISSÃO] (ID [__], p. [__]). CÁLCULO A CONFERIR.*

Em [COMPETÊNCIA DO MARCO DE 200%], o acumulado pago, [ACUMULADO NO MARCO], chegou a [PERCENTUAL NO MARCO] do capital adotado, [MESES ENTRE O MARCO E O REFINANCIAMENTO] [mês/meses] antes do refinanciamento.

## Resumo financeiro

| Descrição | Valor |
|---|---|
| Capital adotado (limite do cartão, [DATA DE INCLUSÃO]) | [LIMITE] |
| Dobro do capital (200%) | [DOBRO DO CAPITAL] |
| Total pago até o mês anterior ao refinanciamento ([COMPETÊNCIA ANTERIOR]) | [TOTAL ATÉ O REFINANCIAMENTO] ([PERCENTUAL]) |
| Valor registrado como "utilizado no mês" no refinanciamento ([COMPETÊNCIA]), com IOF | [UTILIZADO NO MÊS] |
| Total pago até [ÚLTIMA COMPETÊNCIA] | [TOTAL PAGO] ([PERCENTUAL]) |
| Descontado desde o refinanciamento | [TOTAL APÓS O REFINANCIAMENTO] |
| Saldo devedor no INSS em [ÚLTIMA COMPETÊNCIA] | [SALDO ATUAL] |
| Custo total mínimo (pago + saldo devedor) | [CUSTO TOTAL] |
| Onerosidade sobre o capital adotado | [ONEROSIDADE] |

[[SE CONTRATO ATIVO]] Por cautela, a parte autora informa que, da data desta petição até o trânsito em julgado, o banco poderá continuar descontando valores do benefício, caso não haja provimento que o impeça. Eventuais novas cobranças serão incluídas na liquidação, o que se requer. [[FIM]]

# Do direito

## O Código de Defesa do Consumidor se aplica às instituições financeiras

Conforme a Súmula 297 do STJ, o Código de Defesa do Consumidor é aplicável às instituições financeiras.

## A responsabilidade do banco é objetiva

Dispõe o art. 14, caput e § 3º, do Código de Defesa do Consumidor:

> Art. 14. O fornecedor de serviços responde, independentemente da existência de culpa, pela reparação dos danos causados aos consumidores por defeitos relativos à prestação dos serviços, bem como por informações insuficientes ou inadequadas sobre sua fruição e riscos.
>
> § 3° O fornecedor de serviços só não será responsabilizado quando provar: I - que, tendo prestado o serviço, o defeito inexiste; II - a culpa exclusiva do consumidor ou de terceiro.

O refinanciamento foi ato do próprio banco, e não de terceiro. Se a fraude de terceiro já é fortuito interno (Súmula 479 do STJ), com mais razão responde o banco pelo ato que ele mesmo praticou.

## A licitude do cartão consignável não alcança o refinanciamento

A Súmula 41 da Turma de Uniformização das Turmas Recursais do TJBA reconhece como lícita a contratação de cartão de crédito consignável, desde que observado o direito à informação do consumidor e afastado qualquer vício de consentimento. Esta ação não pede a invalidade do cartão contratado em [DATA DE INCLUSÃO DO CARTÃO]. Pede a nulidade do refinanciamento de [COMPETÊNCIA DO REFINANCIAMENTO], ato posterior e distinto, que o banco registrou sem proposta, sem nova assinatura e sem repasse de numerário. A própria súmula condiciona a licitude ao direito à informação (art. 6º, III, do CDC): cabe ao banco demonstrar que informou a parte autora do refinanciamento e de seus custos, o que se requer no tópico da inversão do ônus da prova.

## O teto de juros e encargos do art. 28, § 1º, da Lei 14.690/2023 alcança o cartão consignado

[VERIFICAR ANTES DE PROTOCOLAR: tese do escritório, sem precedente no acervo sobre o teto em cartão consignado.]

O art. 28 da Lei 14.690/2023 dispõe, em seu caput, sobre limites de juros e encargos no crédito rotativo e no parcelamento do saldo devedor das faturas de cartões de crédito e de outros instrumentos de pagamento pós-pagos, e prevê, em seus §§ 1º e 2º:

> § 1º Se os limites referidos no caput deste artigo não forem aprovados no prazo máximo de 90 (noventa) dias, contado da data da publicação desta Lei, o total cobrado em cada caso a título de juros e encargos financeiros não poderá exceder o valor original da dívida.
>
> § 2º O limite previsto no § 1º deste artigo também será aplicável aos emissores de cartão de crédito e de outros instrumentos de pagamento pós-pagos que deixarem de aderir à autorregulação de que trata o caput deste artigo.

O banco poderá invocar o art. 4º da Resolução CMN 4.549/2017, segundo o qual "o disposto nesta Resolução não se aplica aos cartões de crédito e aos demais instrumentos de pagamento pós-pagos cujos contratos prevejam pagamento das faturas mediante consignação em folha de pagamento". O dispositivo não alcança o contrato da parte autora:

1. **No cartão com reserva de margem consignável, a fatura não é paga por consignação.** Apenas o valor mínimo da fatura é descontado do benefício; o restante deve ser pago pelo consumidor, por boleto [CONFERIR: faturas]. O art. 4º afasta a resolução dos contratos que preveem o pagamento **das faturas** por consignação, e não daqueles em que só o mínimo é consignado. A Resolução CMN 4.549, com os arts. 2º-A a 2º-D, aplica-se, portanto, ao cartão desta ação.
2. **A lei não excepciona o cartão com desconto do mínimo em folha.** O art. 28, § 1º, é norma legal e não depende da regulamentação do CMN. Ato infralegal não pode afastar de um grupo de consumidores a proteção que a lei concede a todos [VERIFICAR ANTES DE PROTOCOLAR: precedentes sobre a hierarquia entre o art. 28 da Lei 14.690 e o art. 4º da Res. CMN 4.549; não há julgado no acervo].
3. **O teto é o mesmo nas duas leituras.** Se os limites foram aprovados pelo CMN (art. 2º-C da Res. CMN 4.549, incluído pela Res. CMN 5.112/2023), vale esse limite, que é o do valor original da dívida. Se não foram aprovados para o cartão consignado, incide o § 1º, de igual conteúdo.

[[SE REFINANCIAMENTO ≥ 01/2024]] O refinanciamento ocorreu em [COMPETÊNCIA DO REFINANCIAMENTO], depois de decorrido o prazo de 90 dias contado da publicação da lei (DOU de 03/10/2023, edição extra) (90 dias a partir de 03/10/2023, pela regra de contagem do escritório: 01/01/2024; o art. 2º-D da Res. CMN 4.549 limita os arts. 2º-A a 2º-C às operações posteriores a esse prazo). [[FIM]]

[[SE REFINANCIAMENTO < 01/2024]] O refinanciamento ocorreu em [COMPETÊNCIA DO REFINANCIAMENTO], antes do término do prazo de 90 dias contado da publicação da lei (DOU de 03/10/2023, edição extra). O banco invocará o art. 2º-D da Res. CMN 4.549, que limita os arts. 2º-A a 2º-C às operações realizadas depois desse prazo. O contrato de cartão, porém, é de trato sucessivo, com cobranças mensais, e os juros e encargos lançados depois do prazo se submetem ao teto, que se mede sobre o total cobrado [VERIFICAR ANTES DE PROTOCOLAR: tese do escritório, sem precedente no acervo; o texto do art. 2º-D indica que o teto vale para operações posteriores ao prazo]. [[FIM]]

Para a apuração, o art. 2º-A da Res. CMN 4.549 (incluído pela Res. CMN 5.112/2023) define "valor original da dívida" como o saldo das operações de crédito rotativo ou de parcelamento de fatura concedidas para o financiamento do saldo devedor, apurado toda vez que for concedida nova operação. Como o extrato do INSS não traz essa operação, a parte autora adota o limite do cartão como capital (tópico dos fatos) e pede ao banco as faturas.

## O refinanciamento é nulo por fraude à lei imperativa

O art. 166, VI, do Código Civil dispõe:

> Art. 166. É nulo o negócio jurídico quando: (...) VI - tiver por objetivo fraudar lei imperativa;

A nulidade é declarável de ofício (art. 168, caput, do CC) e não se convalida (art. 169 do CC). Duas normas foram contornadas:

a) o art. 28, § 1º, da Lei 14.690/2023, acima transcrito. O refinanciamento levou o custo total do cartão a [ONEROSIDADE] do capital adotado;

b) o art. 2º-C da Res. CMN 4.549, incluído pela Res. CMN 5.112/2023, aplicável ao cartão desta ação, pelo que se disse sobre o art. 4º:

> Art. 2º-C É assegurada, a qualquer momento, a renegociação das operações de crédito de que trata o art. 2º-A, desde que o valor total cobrado a título de juros e encargos financeiros aplicáveis a cada renegociação não exceda o valor original da dívida da operação inicial que foi renegociada, descontando-se os juros e encargos que já foram pagos.

O banco registrou o novo saldo de [UTILIZADO NO MÊS] sem deduzir o que a parte autora já havia pago ([TOTAL ATÉ O REFINANCIAMENTO]), conforme o extrato (tópico dos fatos). Declarada a nulidade, as partes voltam ao estado anterior (art. 182 do CC): desconstituição do refinanciamento, liberação da margem e devolução do que foi descontado desde [COMPETÊNCIA DO REFINANCIAMENTO].

## Quando o total pago supera 200% do capital, o teto estava esgotado antes do refinanciamento

O raciocínio é encadeado, com a premissa de capital já explicitada nos fatos:

1. O art. 28, § 1º, da Lei 14.690 impede que o total de juros e encargos exceda o valor original da dívida.
2. Em [COMPETÊNCIA DO MARCO DE 200%], a parte autora já havia pago [ACUMULADO NO MARCO], [PERCENTUAL NO MARCO] do capital adotado, acima dos 200% ([DOBRO DO CAPITAL]).
3. Quando o total pago supera 200% do capital, cobriram-se o capital (100%) e juros e encargos em valor igual ao do capital (mais 100%), que é o teto legal.
4. Ao renegociar, o art. 2º-C exige descontar os juros e encargos já pagos. Com o teto já atingido em [COMPETÊNCIA DO MARCO DE 200%], o saldo disponível para novos juros em [COMPETÊNCIA DO REFINANCIAMENTO] era nulo.
5. Logo, o saldo de [UTILIZADO NO MÊS] registrado no refinanciamento não tem lastro, e o banco não comprovou o repasse na ocasião.

O banco detém o desdobramento de cada parcela entre capital e juros e deve demonstrar que o teto não havia sido atingido (art. 6º, VIII, do CDC). Na dúvida, interpreta-se a favor do consumidor (art. 47 do CDC).

## O refinanciamento do cartão consignado deve respeitar as normas do CMN e do INSS

O art. 14 da IN PRES/INSS 138/2022 admite o refinanciamento "desde que atenda às normas editadas pelo BCB e pelo CMN, bem como às normas editadas pelo INSS". Seu parágrafo único exige que a repactuação observe "os limites contidos nesta Instrução Normativa e no Código de Defesa do Consumidor, especialmente quanto à manutenção do mínimo existencial, evitando-se o superendividamento". O refinanciamento impugnado não atendeu à norma do CMN (tópico do teto de juros e encargos) e manteve o desconto sobre verba alimentar.

A norma do INSS impõe ainda ao banco o envio mensal de fatura "com informações essenciais mínimas em destaque, descrição detalhada das operações realizadas" (IN 138, art. 15, VIII). [[SE CARTÃO INCLUÍDO ATÉ 12/12/2022]] Para o cartão constituído até 12/12/2022, vigorava o art. 17 da IN INSS/PRES 28/2008, que já exigia o envio mensal de extrato com descrição detalhada das operações realizadas. [[FIM]] [[SE CARTÃO INCLUÍDO A PARTIR DE 13/12/2022]] A constituição da RMC/RCC está condicionada à solicitação formal por reconhecimento biométrico (art. 15, I) e ao Termo de Consentimento Esclarecido, em página única e instrumento apartado (art. 15, II): o banco deve exibi-los. [[FIM]] Cabe ao banco demonstrar o cumprimento dessas exigências e a regularidade do refinanciamento, o que se requer no tópico da inversão do ônus da prova.

## O refinanciamento unilateral viola a boa-fé objetiva

O art. 422 do Código Civil impõe aos contratantes a probidade e a boa-fé. O banco aceitou anos de pagamentos como amortização e depois renovou o saldo como se nada tivesse sido pago, sem aviso à parte autora: comportamento contraditório (venire contra factum proprium). O art. 39, V, do CDC veda exigir do consumidor vantagem manifestamente excessiva.

## Os valores descontados desde o refinanciamento devem ser restituídos em dobro

O art. 42, parágrafo único, do Código de Defesa do Consumidor dispõe:

> Parágrafo único. O consumidor cobrado em quantia indevida tem direito à repetição do indébito, por valor igual ao dobro do que pagou em excesso, acrescido de correção monetária e juros legais, salvo hipótese de engano justificável.

O dispositivo ressalva apenas o engano justificável. A cobrança sobre saldo sem lastro, mantida mês a mês e sem aviso, não decorre de engano justificável.

A restituição em dobro não depende de prova de má-fé. A Corte Especial do Superior Tribunal de Justiça fixou que ela "independe da natureza do elemento volitivo do fornecedor que realizou a cobrança indevida, revelando-se cabível quando a referida cobrança consubstanciar conduta contrária à boa-fé objetiva" (EAREsp 676.608/RS, Corte Especial, Rel. Min. Og Fernandes, j. 21/10/2020, DJe 30/03/2021). Promover descontos em benefício previdenciário sem autorização do titular é conduta contrária à boa-fé objetiva.[[SE HÁ DESCONTO ANTES DE 30/03/2021]] Quanto aos descontos anteriores a 30/03/2021, a dobra decorre do próprio art. 42, parágrafo único, do CDC, que só a afasta no engano justificável, não demonstrado pelo réu.[[FIM]]

Todos os descontos a partir de [COMPETÊNCIA DO REFINANCIAMENTO] incidem sobre saldo sem lastro, e a cobrança é unilateral e sem aviso. Somam [TOTAL APÓS O REFINANCIAMENTO] em valor simples e **[DOBRO POR EXTENSO]** em dobro. *CÁLCULO A CONFERIR.*

## O dano extrapatrimonial é devido e decorre da natureza alimentar da verba

A situação vivida pela parte autora ultrapassa o mero aborrecimento cotidiano. Os descontos incidem mensalmente sobre benefício previdenciário, de natureza alimentar, e a parte autora já pagou [PERCENTUAL PAGO] do capital adotado e ainda é cobrada por saldo de [SALDO ATUAL], após o banco renovar a dívida sem lhe dar ciência.

A Súmula 40 da Turma de Uniformização das Turmas Recursais do TJBA admite o dano moral por desconto indevido quando, observadas as particularidades do caso, demonstrada violação significativa a direito da personalidade. As particularidades aqui são: a natureza alimentar do benefício, o valor e a duração dos descontos[[SE IDADE ≥ 60]], a condição de pessoa idosa[[FIM]].

Além da função compensatória, a indenização cumpre função pedagógica: o valor deve ser suficiente para desestimular a repetição da conduta por instituição de grande porte. Considerados o porte econômico do banco, a gravidade da falha e o caráter alimentar da verba, o valor de **R$ 20.000,00 (vinte mil reais)** é justo e razoável e não gera enriquecimento sem causa. O valor é estimativo: conforme a Súmula 326 do STJ, a condenação em montante inferior ao postulado na inicial não implica sucumbência recíproca.

# Da inversão do ônus da prova

O ônus de provar que o refinanciamento era regular é do banco por força de lei (art. 14, § 3º, do CDC). A inversão judicial do art. 6º, VIII, do CDC reforça esse resultado:

> Art. 6º São direitos básicos do consumidor: (...) VIII - a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, no processo civil, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiências;

A verossimilhança está no extrato oficial do INSS e na hipossuficiência técnica da parte autora: faturas, desdobramento de capital e juros e documentos do refinanciamento estão sob domínio exclusivo do banco. Requer-se a inversão e que o banco junte, **com a contestação**, os documentos abaixo:

| Documento | Fundamento | Se não for apresentado |
|---|---|---|
| Todas as faturas do cartão, da inclusão ([DATA DE INCLUSÃO]) ao presente | Art. 14, § 3º, do CDC; art. 373, II, do CPC; IN 138/2022, art. 15, VIII (e IN 28/2008, art. 17, até 12/12/2022); art. 2º-B da Res. CMN 4.549 (detalhamento do valor original e dos juros e encargos nas faturas), se aplicável | [[SE JEC]] o fato impeditivo não está provado, e isso se valora contra o banco (art. 373, II, do CPC) [[SE JUSTIÇA COMUM]] admitem-se como verdadeiros os fatos que o documento provaria (art. 400 do CPC) [[FIM]] |
| Desdobramento de cada parcela entre capital, juros e encargos | Art. 6º, VIII, do CDC; art. 373, II, do CPC | Mesma consequência |
| Documentação do refinanciamento de [COMPETÊNCIA DO REFINANCIAMENTO], inclusive proposta, contrato e prova de repasse de numerário à parte autora | Art. 14, § 3º, do CDC; art. 373, II, do CPC | Mesma consequência |
| [[SE CARTÃO INCLUÍDO A PARTIR DE 13/12/2022]] Solicitação formal por reconhecimento biométrico e Termo de Consentimento Esclarecido da constituição da RMC/RCC [[FIM]] | IN 138/2022, art. 15, I e II | Mesma consequência |
| Comprovantes de comunicação à parte autora sobre o refinanciamento | Art. 6º, III, do CDC | Mesma consequência |
| Histórico completo de transações do cartão no DATAPREV | Art. 373, II, do CPC | Mesma consequência |

[[SE JUSTIÇA COMUM]]
## A exibição dos documentos e a perícia contábil são necessárias

Requer-se, também, a exibição dos documentos acima (arts. 396 a 404 do CPC) no prazo do art. 398, com as consequências do art. 400.

Requer-se perícia contábil, com os seguintes quesitos [QUESITOS A VALIDAR PELO ADVOGADO; propostos abaixo]:

1. Qual o total pago de [DATA DE INCLUSÃO] a [COMPETÊNCIA DO REFINANCIAMENTO]?
2. Qual o saldo devedor na data do refinanciamento, considerados os pagamentos?
3. Os juros e encargos pagos já haviam atingido o valor original da dívida ([LIMITE]) nessa data?
4. O saldo refinanciado ([UTILIZADO NO MÊS]) considerou a amortização do capital?
5. Qual seria o saldo correto aplicando o art. 28, § 1º, da Lei 14.690/2023, descontados os juros e encargos já pagos?
[[FIM]]

[[SE JEC]] Nos Juizados Especiais não se pede perícia nem exibição autônoma: a juntada dos documentos acima decorre do ônus do banco, e a omissão é valorada contra ele. A parte reserva-se a faculdade de apresentar parecer técnico contábil (art. 35 da Lei 9.099/95). [[FIM]]

# Do prosseguimento do feito: distinção em relação ao Tema 1.414/STJ

O Tema 1.414/STJ (Segunda Seção, Rel. Min. Raul Araújo) determinou a suspensão nacional dos processos que discutem a nulidade de contratos de cartão consignado por vício de informação, exceto cumprimentos de sentença (situação "Afetado", sem tese, conforme a página do STJ lida em [DATA DA CONSULTA no arquivo tema-1414-stj.md]; a skill relê a situação do tema na data da minuta e relata se mudou).

Esta ação não discute a validade do contrato do cartão contratado em [DATA DE INCLUSÃO DO CARTÃO], que não é impugnado. Discute a nulidade do refinanciamento de [COMPETÊNCIA DO REFINANCIAMENTO], ato posterior, por violação ao teto legal do art. 28, § 1º, da Lei 14.690/2023, cuja análise depende do total já pago pela parte autora, e não de vício de informação nem da abusividade contratual que o Tema 1.414/STJ examinará. Demonstrada a distinção, a parte autora requer o prosseguimento do processo (art. 1.037, § 9º, do CPC).

# Dos precedentes judiciais evocados ao caso concreto

Precedentes evocados nesta peça: [LISTA COM O TÓPICO DE CADA UM: Súmula 297/STJ; Súmula 479/STJ; Súmula 326/STJ (sucumbência recíproca no dano moral); Súmula 41 e Súmula 33 da Turma de Uniformização do TJBA (cartão consignável; juros); Tema 1414/STJ (suspensão e distinção); Súmula 40 da Turma de Uniformização do TJBA; EAREsp 676.608/RS (repetição em dobro)]. [CONFERIR: o acervo não tem acórdão sobre o teto de 200% em cartão consignado; incluir aqui os que o advogado trouxer e conferir.]

O Código de Processo Civil estabelece sistema de precedentes destinado a assegurar coerência e integridade aos julgamentos, de modo que decisões sobre o mesmo tema e as mesmas circunstâncias não destoem entre si.

[[SE JEC]] Nos Juizados Especiais, a sentença segue o art. 38 da Lei 9.099/95, que dispensa o relatório, mas exige que mencione os elementos de convicção do Juiz. O art. 489, § 1º, VI, do CPC é compatível com os critérios do art. 2º da mesma lei e é invocado aqui como parâmetro para o enfrentamento dos precedentes. [[FIM]]

Nesse sentido, dispõe o art. 489, § 1º, VI:

> Art. 489. (...).
>
> § 1º Não se considera fundamentada qualquer decisão judicial, seja ela interlocutória, sentença ou acórdão, que:
>
> (...)
>
> VI - deixar de seguir enunciado de súmula, jurisprudência ou precedente invocado pela parte, sem demonstrar a existência de distinção no caso em julgamento ou a superação do entendimento.

A norma impõe que, uma vez invocado precedente pela parte, o julgador que pretenda decidir em sentido diverso deve, de forma expressa e fundamentada, distingui-lo do caso concreto (*distinguishing*) ou justificar sua superação (*overruling*), sob pena de a decisão ser tida por não fundamentada.

O *distinguishing* pressupõe ausência de coincidência entre os fatos da demanda e a tese jurídica que sustentou o precedente, ou peculiaridade do caso concreto que afaste a aplicação de sua *ratio decidendi*. Mesmo diante de precedente vinculante, essa distinção deve ser feita de forma expressa e fundamentada, e não presumida.¹

O *overruling*, por sua vez, pressupõe que o precedente já não se sustenta, apurando-se sua consistência sistêmica e congruência social por meio do denominado *basic overruling principle*. Falhando em qualquer desses aspectos, a superação também deve ser expressamente justificada.²

Requer-se a apreciação de cada um dos precedentes evocados de forma expressa, promovendo a distinção ou a superação que entender cabível, mas sempre de modo fundamentado, nos termos do art. 489, § 1º, VI, do CPC, sob pena de a decisão incorrer em vício apto a ensejar embargos de declaração.

¹ DONIZETTI, Elpídio. **A Força dos Precedentes do Novo Código de Processo Civil**. 2018. Disponível em: https://elpidiodonizetti.jusbrasil.com.br/artigos/155178268/a-forca-dos-precedentes-do-novo-codigo-de-processo-civil.

² FENSTERSEIFER, Wagner Arnold. Distinguishing e overruling na aplicação do art. 489, § 1.º, VI, do CPC/2015. **Revista de Processo**, São Paulo, v. 252. Editora Revista dos Tribunais, 2017.

[[SE TUTELA]]
# Da tutela provisória de urgência

A tutela provisória pode fundamentar-se em urgência ou evidência (art. 294 do CPC). Aqui se pede a de urgência, que será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo (art. 300 do CPC).

A probabilidade do direito resulta do extrato oficial do INSS, que registra o refinanciamento em [COMPETÊNCIA DO REFINANCIAMENTO] e uma onerosidade de [ONEROSIDADE] sobre o capital adotado. O perigo de dano está no desconto mensal sobre verba alimentar, que se renova a cada competência. Não há perigo de irreversibilidade (art. 300, § 3º, do CPC): a suspensão dos descontos pode ser revertida se o banco comprovar a regularidade do refinanciamento.

Requer-se a antecipação dos efeitos da tutela para que o banco suspenda os descontos do cartão nº [NÚMERO DO CARTÃO] no benefício NB [NB] e não repasse a margem a terceiros, sob pena de multa diária de R$ 500,00. Alternativamente, tutela da evidência (art. 311, IV, do CPC), por estar a inicial instruída com prova documental suficiente.
[[FIM]]

# Das provas

Protesta provar o alegado por todos os meios admitidos em direito (art. 369 do CPC), especialmente a prova documental anexa e o depoimento pessoal do representante do réu, bem como os documentos que o banco deva juntar.

# Dos pedidos

Diante do exposto, requer:

a) o deferimento da gratuidade da justiça (arts. 98 e 99, caput e § 3º, do CPC[[SE JEC]]; art. 54 da Lei 9.099/95[[FIM]]);

b) a prioridade de tramitação [[SE IDADE ≥ 60]] (art. 1.048, I, do CPC; art. 71 da Lei 10.741/2003) [[FIM]];

c) a citação do réu para que apresente contestação no prazo legal, sob pena de revelia, manifestando a parte autora interesse na audiência de conciliação;

[[SE TUTELA]] d) a antecipação dos efeitos da tutela, nos termos do tópico próprio, para suspender os descontos do cartão nº [NÚMERO DO CARTÃO], sob pena de multa diária de R$ 500,00; [[FIM]]

e) a inversão do ônus da prova, com o encargo de o réu juntar, com a contestação, os documentos do tópico [REMISSÃO: tópico da inversão do ônus]; [[SE JUSTIÇA COMUM]] a exibição desses documentos e a perícia contábil com os quesitos do tópico [REMISSÃO]; [[FIM]]

f) a apreciação expressa de cada precedente evocado, nos termos do art. 489, § 1º, VI, do CPC;

g) a procedência dos pedidos, confirmada a tutela ou concedida em sentença, para que:

1. seja declarada a nulidade do refinanciamento de [COMPETÊNCIA DO REFINANCIAMENTO] sobre o cartão nº [NÚMERO DO CARTÃO] (saldo registrado de [UTILIZADO NO MÊS], com IOF de [IOF]), por fraude à lei imperativa (art. 166, VI, do CC, c/c o art. 28, § 1º, da Lei 14.690/2023), com desconstituição de seus efeitos desde a data da prática;
2. seja declarada a quitação do contrato do cartão nº [NÚMERO DO CARTÃO] em [COMPETÊNCIA DO REFINANCIAMENTO], quando os pagamentos somavam [TOTAL ATÉ O REFINANCIAMENTO], [PERCENTUAL] do capital adotado, acima do teto do art. 28, § 1º, da Lei 14.690/2023;
3. o réu seja condenado à obrigação de fazer de, em 5 (cinco) dias úteis do trânsito em julgado, baixar o bloqueio da margem consignável junto ao INSS/DATAPREV e cessar os descontos, sob pena de multa diária de R$ 500,00, nos termos dos arts. 497 e 537 do CPC;
4. o réu seja condenado a restituir em dobro os valores descontados desde [COMPETÊNCIA DO REFINANCIAMENTO], no total atual de [DOBRO POR EXTENSO]. Correção monetária desde cada desconto (Súmula 43 do STJ) e juros de mora desde a citação, ressalvada a constituição anterior em mora (Súmula 33 da Turma de Uniformização do TJBA; art. 397, parágrafo único, do CC). Requer-se que os descontos posteriores a esta petição, até o trânsito em julgado, sejam apurados na liquidação;
5. o réu seja condenado ao pagamento de indenização por danos extrapatrimoniais de **R$ 20.000,00 (vinte mil reais)**, com correção monetária desde o arbitramento (Súmula 362 do STJ) e juros de mora desde a citação, ressalvada a constituição anterior em mora (Súmula 33 da Turma de Uniformização do TJBA; art. 397, parágrafo único, do CC);

h) **subsidiariamente** ao pedido g.1: [DECISÃO DO ADVOGADO: manter ou retirar os dois pedidos subsidiários abaixo, que vêm do modelo AMN e não têm fonte no acervo sobre lesão]
   1. a anulação do refinanciamento por lesão (art. 157 do CC), com recálculo do saldo devedor deduzidos os valores pagos e aplicado o teto da Lei 14.690/2023;
   2. a revisão judicial do contrato, com abatimento dos valores pagos e vedação de novo refinanciamento sem anuência expressa e escrita da parte autora (art. 6º, V, do CDC);

[[SE JUSTIÇA COMUM]] i) a condenação do réu ao pagamento das custas e dos honorários advocatícios de sucumbência (art. 85 do CPC); [[FIM]]
[[SE JEC]] (Sem pedido de custas e honorários: a sentença de primeiro grau não condena o vencido, salvo litigância de má-fé — art. 55 da Lei 9.099/95.) [[FIM]]

Requer, ainda, que todas as intimações e publicações sejam feitas exclusivamente em nome de Diego Ramos Arléo Barbosa, OAB/BA nº 38.179, e Michael Santos Neves, OAB/BA nº 50.954.

# Do valor da causa

Dá-se à causa o valor de [VALOR DA CAUSA POR EXTENSO], correspondente ao saldo do refinanciamento declarado nulo ([UTILIZADO NO MÊS]; art. 292, II, do CPC), à restituição em dobro ([DOBRO]; art. 292, VI, do CPC) e ao dano extrapatrimonial (R$ 20.000,00) (art. 292, V, do CPC). *CÁLCULO A CONFERIR.* [[SE CAIXA]] Valor real, sem renúncia a teto. [[FIM]]

Termos em que, pede deferimento.

[CIDADE DO FECHO, perguntada ao advogado] - [UF], [dd] de [mês por extenso] de [aaaa].


DIEGO RAMOS ARLÉO BARBOSA
OAB/BA nº 38.179

MICHAEL SANTOS NEVES
OAB/BA nº 50.954
