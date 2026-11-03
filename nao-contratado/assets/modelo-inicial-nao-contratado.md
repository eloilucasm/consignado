<!--
MODELO — INICIAL DE EMPRÉSTIMO CONSIGNADO NÃO CONTRATADO (blocos B, C e Caixa)

Como usar (instruções para quem redige; apague este comentário na peça):
- Preencha os campos [PREENCHER: ...] com o quadro de fatos e os documentos. Campo sem fonte vira [CONFERIR: ...].
- Blocos entre [[SE ...]] e [[FIM]] entram só quando a condição vale. Apague os marcadores.
- Números e valores vêm de calculo.json (scripts/calcular.py). Nunca refaça a conta de cabeça.
- Não digite número de tópico: a tipografia-azul numera. Remissão interna: "tópico 5" calculado depois de fechada a estrutura.
- Títulos de tópico (#) no formato "Da/Do/Dos…"; subtópicos (##) em frase completa.
- Citação de lei: texto literal do acervo. Marcas [VERIFICAR ANTES DE PROTOCOLAR] ficam no ponto exato.
- Perguntar ao advogado ANTES de gerar: rito (JEC ou Justiça Comum) e cidade/UF do fecho.
- Forma, endereçamento, qualificação e pedidos de rotina: assets/padrao-pecas.md (prevalece em caso de conflito).
-->

[[SE JEC]] [PREENCHER: `jec.enderecamento` da comarca em references/dados/tjba_unidades.json; comarca do município em tjba_comarcas.json] [[SE JUSTIÇA COMUM]] [PREENCHER: `comum.enderecamento` da comarca em references/dados/tjba_unidades.json] [[FIM]]

[[SE CAIXA]] Substituir o endereçamento por: AO JUÍZO DA [N]ª VARA FEDERAL DA SUBSEÇÃO JUDICIÁRIA DE [subseção da tabela TRF1] - BAHIA [[FIM]]

**EMENTA:** Empréstimo consignado não contratado. [Beneficiário/Beneficiária] do INSS. Ausência de manifestação volitiva. Ato juridicamente inexistente. Desconto indevido sobre verba de natureza alimentar. Responsabilidade objetiva da instituição financeira. Repetição do indébito. Dano extrapatrimonial.[[SE TUTELA]] Tutela de urgência para suspensão imediata dos descontos.[[FIM]]

**[NOME DO AUTOR]**, [nacionalidade], [estado civil], [profissão], [inscrito/inscrita] no CPF sob nº [CPF], RG sob nº [RG], [residente e domiciliado/domiciliada] na [ENDEREÇO], CEP [CEP], cidade de [CIDADE]/[UF], por seu advogado que esta subscreve (procuração anexa), vem, respeitosamente, perante este Juízo, propor a presente

## Ação Declaratória de Inexistência de Relação Obrigacional, Cumulada com Repetição do Indébito, Obrigação de Fazer e Indenização por Danos Extrapatrimoniais[[SE TUTELA]], com Pedido de Tutela Provisória de Urgência[[FIM]]

em face **[RÉU]**, [descrição do réu de references/dados/reus.json: pessoa jurídica, CNPJ e endereço], [[SE JEC]] pelo procedimento da Lei nº 9.099/95, [[FIM]] pelos seguintes fatos, fundamentos e razões de direito.

# Da gratuidade da justiça

A parte autora não tem condições de arcar com as despesas do processo, uma vez que são insuficientes seus recursos financeiros para pagar todas as despesas processuais, inclusive o recolhimento das custas iniciais.

Requer sejam deferidos os benefícios da gratuidade da justiça, o que faz por declaração de seus advogados, nos termos do art. 99, § 4º, c/c o art. 105, in fine, ambos do CPC, prerrogativa que consta do instrumento procuratório anexo. Presume-se verdadeira a alegação de insuficiência deduzida por pessoa natural (art. 99, § 3º, do CPC).[[SE JEC]] No Juizado Especial, o acesso em primeiro grau independe do pagamento de custas, taxas ou despesas (art. 54 da Lei 9.099/95).[[FIM]]

# Da tramitação prioritária

[[SE IDADE ≥ 60]] Conforme documento pessoal anexo, a parte autora é pessoa idosa e faz jus à prioridade na tramitação (art. 1.048, I, do CPC; art. 71 da Lei 10.741/2003 — Estatuto da Pessoa Idosa). [[FIM]]

# Dos fatos

A parte autora é beneficiária do INSS, e o benefício previdenciário é a sua única fonte de renda.

Em [DATA DE EMISSÃO], ao analisar o Histórico de Empréstimo Consignado emitido pelo INSS (ID [__], p. [__]), tomou conhecimento da existência de descontos mensais referentes a contrato(s) de empréstimo consignado que jamais contratou, relacionados a seguir.

| Contrato | Averbação | Início | Fim | Parcela | Qtde. | Total descontado | Restituição (dobro) | Status |
|---|---|---|---|---|---|---|---|---|
| [uma linha por contrato, de calculo.json] | | | | | | | | |
| **Total** | | | | | | [total] | [total em dobro] | |

*Fonte: Histórico de Empréstimo Consignado do INSS, emitido em [DATA DE EMISSÃO] (ID [__], p. [__]). CÁLCULO A CONFERIR.*

## A parte autora nega, contrato a contrato, a existência de manifestação de vontade

Para cada contrato da tabela, escrever um parágrafo com os campos do quadro de fatos. Não afirmar o que só o contrato ou o log do banco podem mostrar.

> **Contrato nº [CONTRATO].** A parte autora nega ter firmado esse contrato, nega ter assinado qualquer instrumento a ele relativo e nega ter autorizado a averbação. [[SE ASSINATURA IMPUGNÁVEL]] Se o banco juntar instrumento com assinatura, desde já fica impugnada a sua autenticidade, o que desloca ao banco o ônus de prová-la. [[FIM]] O extrato do INSS registra valor liberado de [VALOR LIBERADO DO EXTRATO] [[SE LIBERADO AUSENTE/ZERO]] ou não registra valor liberado algum, hipótese compatível com portabilidade ou refinanciamento sem crédito novo ao beneficiário [[FIM]]. Cabe ao banco comprovar o crédito, em conta de titularidade da parte autora, de valor idêntico ao liberado (art. 373, II, do CPC).

A parte autora não utiliza plataformas digitais de autenticação, não domina mecanismos de verificação biométrica, tokens ou senhas dinâmicas e jamais forneceu sua imagem facial, dados biométricos ou credenciais de acesso.

Casos de fraude envolvendo aposentados e pensionistas, com descontos de contratos que o beneficiário não reconhece, são de conhecimento público. A parte autora não reconhece o(s) empréstimo(s) a ela atribuído(s) e não recebeu qualquer atendimento do banco que lhe permitisse resolver a situação.

[[SE CONTRATO ATIVO]] Por cautela, a parte autora informa que, da data desta petição até o trânsito em julgado, o banco poderá continuar descontando valores do benefício, caso não haja provimento que o impeça. Eventuais novas cobranças serão incluídas na liquidação, o que se requer. [[FIM]]

[[SE CRÉDITO EM CONTA]]
<!-- Entra só quando o extrato bancário da parte autora (pedido antes de ajuizar: VF6, Súmula 42/TJBA) mostra crédito ligado ao contrato. A peça não nega o recebimento: reconhece o lançamento e nega a contratação. O tratamento do valor é decisão do advogado. -->

## O crédito que aparece na conta da parte autora não prova a contratação

O extrato bancário da parte autora (ID [__], p. [__]) registra, em [DATA DO CRÉDITO], crédito de [VALOR CREDITADO] [DESCREVER: histórico do lançamento, como consta do extrato bancário]. A parte autora não omite esse lançamento. Ele não prova, porém, quem contratou: o depósito é feito pela própria instituição financeira, por iniciativa dela, e não contém manifestação de vontade do titular da conta. A existência do negócio continua a depender do instrumento e da trilha de contratação, que só o banco detém (art. 373, II, do CPC).

[DECISÃO DO ADVOGADO: devolução, depósito em juízo ou compensação] A parte autora põe o valor recebido à disposição do juízo, para [devolução ao réu depois de declarada a inexistência | depósito em juízo, à disposição do réu | compensação com a restituição material]. Em nenhuma hipótese o valor se compensa com a indenização extrapatrimonial, que tem causa e função distintas.
[[FIM]]

# Do direito

## O Código de Defesa do Consumidor se aplica às instituições financeiras

Conforme a Súmula 297 do STJ, o Código de Defesa do Consumidor é aplicável às instituições financeiras.

## A responsabilidade do banco é objetiva, e a prova de excludente é dele

Dispõe o art. 14, caput e § 3º, do Código de Defesa do Consumidor:

> Art. 14. O fornecedor de serviços responde, independentemente da existência de culpa, pela reparação dos danos causados aos consumidores por defeitos relativos à prestação dos serviços, bem como por informações insuficientes ou inadequadas sobre sua fruição e riscos.
>
> § 3° O fornecedor de serviços só não será responsabilizado quando provar: I - que, tendo prestado o serviço, o defeito inexiste; II - a culpa exclusiva do consumidor ou de terceiro.

Trata-se de inversão que decorre da lei: o ônus de provar a inexistência do defeito ou a culpa exclusiva do consumidor ou de terceiro é do banco. A fraude de terceiro em operação bancária é fortuito interno e não afasta a responsabilidade (Súmula 479 do STJ).

A parte autora jamais celebrou os contratos impugnados e não deu causa aos descontos, de modo que nenhuma das excludentes se verifica. Configura-se o ato ilícito do art. 186 do Código Civil:

> Art. 186. Aquele que, por ação ou omissão voluntária, negligência ou imprudência, violar direito e causar dano a outrem, ainda que exclusivamente moral, comete ato ilícito.

Estão presentes a conduta (averbação e cobrança sem consentimento), o dano (desconto sobre verba alimentar) e o nexo causal.

## A regularidade da contratação era exigência da norma do INSS, e o descumprimento é do banco

[[SE CONTRATO ATÉ 12/12/2022]] Até 12/12/2022 vigorou a IN INSS/PRES 28/2008. Seu art. 5º determina que a instituição financeira somente encaminhará o arquivo para averbação **após a devida assinatura do contrato** pelo beneficiário, ainda que por meio eletrônico, e seu art. 6º atribui à instituição total responsabilidade pela inobservância, tornando a operação irregular e não autorizada. [[FIM]]

[[SE CONTRATO A PARTIR DE 13/12/2022]] Desde 13/12/2022 vigora a IN PRES/INSS 138/2022. Seu art. 5º, II e III, exige contrato firmado e assinado, com uso de reconhecimento biométrico, e autorização de consignação expressa, também assinada com uso de reconhecimento biométrico. O § 11 do mesmo artigo admite, alternativamente, o "acesso autenticado", se a contratação é formalizada pelo beneficiário diretamente na instituição financeira ou por seus canais eletrônicos. O prazo de implementação da biometria foi prorrogado pelo art. 2º da IN 143/2023 [CONFERIR: data de cada contrato em relação ao prazo prorrogado]. Cabe ao banco demonstrar qual das formas foi usada e que ela corresponde à parte autora. [[FIM]]

A instituição contratante responde pelos atos do correspondente que atua em seu nome: [[SE CONTRATO ATÉ 31/01/2022]] art. 2º da Resolução CMN 3.954/2011 (redação original) [[FIM]] [[SE CONTRATO A PARTIR DE 01/02/2022]] art. 3º e parágrafo único da Resolução CMN 4.935/2021 [[FIM]], que lhe atribuem inteira responsabilidade pelo atendimento prestado por meio do contratado e o dever de garantir a integridade, a confiabilidade, a segurança e o sigilo das transações realizadas.

## Os valores descontados devem ser restituídos em dobro

O art. 42, parágrafo único, do Código de Defesa do Consumidor dispõe:

> Parágrafo único. O consumidor cobrado em quantia indevida tem direito à repetição do indébito, por valor igual ao dobro do que pagou em excesso, acrescido de correção monetária e juros legais, salvo hipótese de engano justificável.

O dispositivo ressalva apenas o engano justificável. Descontos mensais de empréstimo que a parte autora não contratou, lançados diretamente sobre verba de natureza alimentar, não decorrem de engano justificável. A parte autora pede, por isso, a restituição em dobro de **todos** os descontos.

A restituição em dobro não depende de prova de má-fé. A Corte Especial do Superior Tribunal de Justiça fixou que ela "independe da natureza do elemento volitivo do fornecedor que realizou a cobrança indevida, revelando-se cabível quando a referida cobrança consubstanciar conduta contrária à boa-fé objetiva" (EAREsp 676.608/RS, Corte Especial, Rel. Min. Og Fernandes, j. 21/10/2020, DJe 30/03/2021). Promover descontos em benefício previdenciário sem autorização do titular é conduta contrária à boa-fé objetiva.[[SE HÁ DESCONTO ANTES DE 30/03/2021]] Quanto aos descontos anteriores a 30/03/2021, a dobra decorre do próprio art. 42, parágrafo único, do CDC, que só a afasta no engano justificável, não demonstrado pelo réu.[[FIM]]

Para cada contrato com desconto, escrever:

> **Contrato nº [CONTRATO].** Até a presente data, a parte autora suportou [QTDE] [parcela/parcelas], cuja soma resulta em [TOTAL DESCONTADO POR EXTENSO]. Assim, o banco deve restituir os valores descontados em dobro, que correspondem a [DOBRO POR EXTENSO].

Totalizando, [TOTAL DO DOBRO POR EXTENSO]. *CÁLCULO A CONFERIR.*

## O dano extrapatrimonial é devido e decorre da natureza alimentar da verba

A situação vivida pela parte autora ultrapassa o mero aborrecimento cotidiano. Os descontos incidem mensalmente sobre benefício previdenciário, de natureza alimentar, durante [PERÍODO: de MM/AAAA a MM/AAAA], sem que a parte autora pudesse impedi-los na origem. [[SE CONFIRMADO]] Os valores subtraídos destinavam-se a despesas básicas, como medicamentos e contas essenciais. [[FIM]]

A Súmula 40 da Turma de Uniformização das Turmas Recursais do TJBA admite o dano moral por desconto indevido quando, observadas as particularidades do caso, demonstrada violação significativa a direito da personalidade. As particularidades aqui são: a natureza alimentar do benefício, o valor e a duração dos descontos[[SE IDADE ≥ 60]], a condição de pessoa idosa[[FIM]].

Além da função compensatória, a indenização cumpre função pedagógica: o valor deve ser suficiente para desestimular a repetição da conduta por instituição de grande porte. Considerados o porte econômico do banco, a gravidade da falha e o caráter alimentar da verba, o valor de **R$ 20.000,00 (vinte mil reais)** é justo e razoável e não gera enriquecimento sem causa. O valor é estimativo: conforme a Súmula 326 do STJ, a condenação em montante inferior ao postulado na inicial não implica sucumbência recíproca.

A orientação de que o desconto indevido em benefício de pessoa idosa extrapola o mero aborrecimento consta de julgado do TRF-4 (AC 5003696-87.2023.4.04.7118/RS, Rel. Roger Raupp Rios, 3ª Turma, j. 13/05/2025), cuja ementa, em trecho, é a seguinte:

> (...) 1. Responde objetivamente o banco pelos danos causados por simples falta do serviço em razão do risco inerente à atividade que exerce (artigo 14 do Código de Defesa do Consumidor) (...). 3. Importante consignar ainda se tratar de pessoa idosa, sabidamente com maior dificuldade de acesso à informação tecnológica (...). 4. Especificamente quanto aos casos de descontos realizados indevidamente sobre proventos, decorrentes de empréstimo fraudulento, a jurisprudência predominante aponta que tal situação extrapola o mero aborrecimento, configurando, pois, dano moral indenizável. Em julgamentos recentíssimos desta Corte sobre o mesmo tema, a indenização tem sido fixada entre R$ 10.000,00 (dez mil reais) e R$ 20.000,00 (vinte mil reais).¹

¹ BRASIL. Tribunal Regional Federal da 4ª Região. Terceira Turma. **Apelação Cível n. 5003696-87.2023.4.04.7118/RS**. Relator: Roger Raupp Rios. Julgado em: 13 maio 2025.

[[SE PRESCRIÇÃO]]
## A pretensão não está prescrita

Por cautela, afasta-se desde logo a alegação de prescrição. A pretensão não decorre de defeito de serviço contratado, mas da cobrança de valores sem lastro contratual, por averbações que a parte autora jamais autorizou. A Corte Especial do STJ decidiu, em caso de cobrança de serviços não contratados de telefonia fixa, que a repetição de indébito prescreve em dez anos, pelo art. 205 do Código Civil, e não em três (EAREsp 738.991/RS, Rel. Min. Og Fernandes, j. 20/02/2019, DJe 11/06/2019; julgado de telefonia fixa, aplicado ao consignado por analogia).² Além disso, a declaração de inexistência da relação jurídica não está sujeita a prazo prescricional: o negócio nulo não convalesce pelo decurso do tempo (art. 169 do CC).

Subsidiariamente, ainda que se aplicasse o prazo quinquenal do art. 27 do CDC, ele só começa a correr do conhecimento do dano e de sua autoria. [[SE CIÊNCIA INFORMADA]] A parte autora só soube da origem dos descontos em [DATA DA CIÊNCIA], pelo Histórico de Empréstimo Consignado emitido em [DATA DE EMISSÃO]. [[FIM]] O prazo e o termo inicial aplicáveis são decisão do advogado responsável [DECISÃO DO ADVOGADO: art. 27 do CDC ou art. 205 do CC].

² BRASIL. Superior Tribunal de Justiça. Corte Especial. Embargos de Divergência em Agravo em Recurso Especial n. 738.991/RS. Relator: Ministro Og Fernandes. Julgado em: 20 fev. 2019. Publicado no DJe em: 11 jun. 2019.
[[FIM]]

[[SE LITISPENDÊNCIA]]
# Da ausência de litispendência

Gerar conforme o quadro de fatos (item 10): objeto exclusivo do NB deste processo; se há ação contra o mesmo banco em outro benefício, indicar a espécie e o NB de cada um e que são benefícios e contratos distintos; se a outra ação tem tese diferente (por exemplo, migrado ou Tese 1000), dizer que os contratos, a causa de pedir e os pedidos não se confundem. Fundamento: art. 337, §§ 1º a 3º, do CPC. Não informar quantas ações a parte autora ou o escritório têm.
[[FIM]]

# Da inversão do ônus da prova

O ônus de provar a regularidade da contratação é do banco por força de lei, independentemente de decisão judicial: art. 14, § 3º, do CDC; art. 429, II, do CPC, quando se impugna a autenticidade da assinatura de documento juntado por quem o produziu; e o Tema Repetitivo 1061 do STJ, que atribui à instituição financeira o ônus de provar a autenticidade da assinatura impugnada em contrato bancário (CPC, arts. 6º, 369 e 429, II).³ A inversão judicial do art. 6º, VIII, do CDC reforça esse resultado:

> Art. 6º São direitos básicos do consumidor: (...) VIII - a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, no processo civil, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiências;

³ BRASIL. Superior Tribunal de Justiça. Segunda Seção. Tema Repetitivo 1061. Recurso Especial n. 1.846.649/MA. Relator: Ministro Marco Aurélio Bellizze. Julgado em: 24 nov. 2021. Publicado no DJe em: 9 dez. 2021.

A verossimilhança está na própria negativa de fato e na hipossuficiência técnica da parte autora: contrato, registro de autenticação, comprovante de crédito e trilha de auditoria estão sob domínio exclusivo do banco. Requer-se a inversão e que o banco junte, **com a contestação**, os documentos abaixo:

| Documento | Fundamento | Se não for apresentado |
|---|---|---|
| Instrumento contratual original, assinado | Art. 429, II, do CPC; Tema 1061/STJ; IN 28/2008, art. 5º (até 12/12/2022); IN 138/2022, art. 5º, II (desde 13/12/2022) | [[SE JEC]] o fato impeditivo não está provado, e isso se valora contra o banco (art. 373, II, do CPC) [[SE JUSTIÇA COMUM]] admitem-se como verdadeiros os fatos que o documento provaria (art. 400 do CPC) [[FIM]] |
| Registro de autenticação da contratação (biometria com prova de vida e índice de similaridade, ou acesso autenticado, conforme a data) | IN 138/2022, art. 4º, VIII, e art. 5º, II, III e § 11 | Mesma consequência |
| Autorização expressa da consignação | IN 28/2008, art. 5º (até 12/12/2022); IN 138/2022, art. 5º, III | Mesma consequência |
| Comprovante do crédito efetivo em conta de titularidade da parte autora, de valor idêntico ao liberado no extrato | Art. 14, § 3º, do CDC; art. 373, II, do CPC; IN 138/2022, art. 5º, VII | Mesma consequência |
| Trilha de auditoria da contratação (IP, dispositivo, localização, etapas) | Dever da instituição contratante de garantir a integridade, a confiabilidade, a segurança e o sigilo das transações realizadas pelo correspondente (Res. CMN 4.935/2021, art. 3º, parágrafo único; Res. CMN 3.954/2011, art. 2º, para fatos até 31/01/2022) | Mesma consequência |

[[SE JUSTIÇA COMUM]]
## A exibição dos documentos e a perícia são necessárias

Requer-se, também, a exibição dos documentos acima (arts. 396 a 404 do CPC) no prazo do art. 398, com as consequências do art. 400.

Havendo [[SE ASSINATURA MANUSCRITA]] assinatura manuscrita impugnada, requer-se perícia grafotécnica [[SE TRILHA ELETRÔNICA]] trilha eletrônica de contratação, requer-se perícia em informática forense [[FIM]], com os seguintes quesitos [QUESITOS A VALIDAR PELO ADVOGADO; propostos abaixo]:

1. A assinatura aposta no instrumento (ID [__]) procede do punho da parte autora, confrontada com os padrões indicados (documento de identidade, procuração)?
2. Há elementos de imitação, decalque ou montagem na assinatura questionada?
3. [Trilha eletrônica] Os registros de IP, dispositivo e localização do aceite (ID [__]) são compatíveis com o local de residência da parte autora?
4. [Trilha eletrônica] O registro de autenticação (biometria ou acesso autenticado) identifica a parte autora com a pontuação e os parâmetros técnicos informados?
[[FIM]]

[[SE JEC]] Nos Juizados Especiais não se pede perícia nem exibição autônoma: a juntada dos documentos acima decorre do ônus do banco, e a omissão é valorada contra ele. [[FIM]]

# Dos precedentes judiciais evocados ao caso concreto

Precedentes evocados nesta peça: [LISTA COM O TÓPICO DE CADA UM: Súmula 297/STJ; Súmula 479/STJ; Súmula 40 da Turma de Uniformização do TJBA; Tema 1061/STJ; AC 5003696-87.2023.4.04.7118/RS (TRF-4); EAREsp 738.991/RS, se houver prescrição; EAREsp 676.608/RS (repetição em dobro)].

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

O *distinguishing* pressupõe ausência de coincidência entre os fatos da demanda e a tese jurídica que sustentou o precedente, ou peculiaridade do caso concreto que afaste a aplicação de sua *ratio decidendi*. Mesmo diante de precedente vinculante, essa distinção deve ser feita de forma expressa e fundamentada, e não presumida.⁴

O *overruling*, por sua vez, pressupõe que o precedente já não se sustenta, apurando-se sua consistência sistêmica e congruência social por meio do denominado *basic overruling principle*. Falhando em qualquer desses aspectos, a superação também deve ser expressamente justificada.⁵

Requer-se a apreciação de cada um dos precedentes evocados de forma expressa, promovendo a distinção ou a superação que entender cabível, mas sempre de modo fundamentado, nos termos do art. 489, § 1º, VI, do CPC, sob pena de a decisão incorrer em vício apto a ensejar embargos de declaração.

⁴ DONIZETTI, Elpídio. **A Força dos Precedentes do Novo Código de Processo Civil**. 2018. Disponível em: https://elpidiodonizetti.jusbrasil.com.br/artigos/155178268/a-forca-dos-precedentes-do-novo-codigo-de-processo-civil.

⁵ FENSTERSEIFER, Wagner Arnold. Distinguishing e overruling na aplicação do art. 489, § 1.º, VI, do CPC/2015. **Revista de Processo**, São Paulo, v. 252. Editora Revista dos Tribunais, 2017.

# Do preenchimento do campo "Motivo da Exclusão" no sistema eConsignado/DATAPREV

O extrato do Histórico de Empréstimo Consignado é gerado a partir do sistema eConsignado, mantido pelo INSS em conjunto com a Dataprev, e constitui o repositório do histórico consignatário do beneficiário. Esse repositório é consultado pelas instituições financeiras habilitadas antes de nova averbação, de modo que o que nele consta, e o que deixa de constar, produz efeitos continuados sobre a vida financeira do titular.

O sistema estrutura a baixa de contratos em três campos:

| Campo | Quem preenche | Situação no caso |
|---|---|---|
| Data da Exclusão | Sistema, automaticamente | [[SE HÁ ATIVO]] A ser preenchida quando da baixa [[SENÃO]] Preenchida [[FIM]] |
| Origem da Exclusão | A própria instituição financeira, de forma unilateral (por exemplo, "Exclusão Banco", "Exclusão por portabilidade") | [[SE HÁ ATIVO]] A ser preenchida pela ré; não se pede a sua alteração [[SENÃO]] Preenchida; não se pede a sua alteração [[FIM]] |
| Motivo da Exclusão | Campo destinado ao registro da causa jurídica da baixa | Em branco: é este o campo que se pede preencher |

A parte autora não pretende alterar o campo "Origem da Exclusão". Pretende apenas o preenchimento do campo "Motivo da Exclusão", hoje vazio, com a expressão "Por força de decisão judicial". A providência tem custo operacional irrisório e traz vantagens verificáveis ao consumidor:

| # | Vantagem | Fundamento |
|---|---|---|
| 1 | Impede a reaverbação do mesmo contrato sob numeração distinta (linha derivada de contratos) | CPC, art. 497 |
| 2 | Documenta a irregularidade no histórico oficial, tornando-a oponível a futuras instituições consulentes | CDC, art. 43 |
| 3 | Libera a margem consignável de forma documentada | CDC, art. 6º, VI |
| 4 | Impede que a baixa seja revertida por lançamento posterior | CPC, art. 497; CC, art. 422 |
| 5 | Corrige dado pessoal incompleto de base oficial | LGPD, art. 18, III |
| 6 | Alinha-se à transparência exigida dos operadores do sistema consignado | IN 138/2022 [CONFERIR: o modelo anterior citava também o Acórdão TCU 1.094/2026, fora do acervo] |

[[SE HÁ ATIVO E EXCLUÍDO]] Quanto aos contratos já excluídos, a exclusão já ocorreu e o campo permanece vazio, de modo que o provimento consiste na simples complementação do registro histórico. Quanto ao(s) contrato(s) ainda ativo(s), a providência será cumprida no momento da baixa determinada por este Juízo. [[FIM]] [[SE SÓ ATIVO]] Tratando-se de contrato ainda ativo, o preenchimento dar-se-á no momento da baixa determinada por este Juízo. [[FIM]] [[SE SÓ EXCLUÍDO]] Tratando-se de contratos já excluídos, a exclusão já ocorreu e o campo permanece vazio, de modo que o provimento consiste na simples complementação do registro histórico. [[FIM]]

[[SE TUTELA]]
# Da tutela provisória de urgência

A tutela provisória pode fundamentar-se em urgência ou evidência (art. 294 do CPC). Aqui se pede a de urgência, que será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo (art. 300 do CPC).

A probabilidade do direito resulta da negativa específica de contratação, da titularidade do benefício e dos documentos anexos, e do ônus que a lei impõe ao banco (tópico da inversão do ônus). O perigo de dano está no desconto mensal sobre verba alimentar, única renda da parte autora, que se renova a cada competência.

Não há perigo de irreversibilidade (art. 300, § 3º, do CPC): a suspensão dos descontos pode ser revertida se o banco comprovar a contratação.

Requer-se a antecipação dos efeitos da tutela para que o banco se abstenha de realizar novos descontos no benefício referentes ao(s) contrato(s) nº [CONTRATOS ATIVOS], sob pena de multa diária a ser fixada por este Juízo.
[[FIM]]

# Das provas

Protesta provar o alegado por todos os meios admitidos em direito (art. 369 do CPC), especialmente a prova documental anexa e o depoimento pessoal do representante do réu, bem como os documentos que o banco deva juntar.

# Dos pedidos

Diante do exposto, requer:

a) o deferimento da gratuidade da justiça (arts. 98 e 99, caput e § 3º, do CPC[[SE JEC]]; art. 54 da Lei 9.099/95[[FIM]]);

b) a prioridade de tramitação [[SE IDADE ≥ 60]] (art. 1.048, I, do CPC; art. 71 da Lei 10.741/2003) [[FIM]];

c) a citação do réu para que apresente contestação no prazo legal, sob pena de revelia, manifestando a parte autora interesse na audiência de conciliação;

[[SE TUTELA]] d) a antecipação dos efeitos da tutela, nos termos do tópico próprio, para que o réu se abstenha de novos descontos referentes ao(s) contrato(s) nº [CONTRATOS ATIVOS]; [[FIM]]

e) a inversão do ônus da prova, com o encargo de o réu juntar, com a contestação, os documentos do tópico [REMISSÃO: tópico da inversão do ônus]; [[SE JUSTIÇA COMUM]] a exibição desses documentos e a perícia [grafotécnica / em informática forense] com os quesitos do tópico [REMISSÃO]; [[FIM]]

f) a apreciação expressa de cada precedente evocado, nos termos do art. 489, § 1º, VI, do CPC;

g) a procedência dos pedidos, confirmada a tutela ou concedida em sentença, para que:

1. seja declarada a inexistência da relação jurídica entre as partes quanto ao(s) contrato(s) nº [CONTRATOS] e, subsidiariamente, a sua nulidade, com a inexigibilidade de todo e qualquer débito decorrente;
2. o réu seja condenado à obrigação de fazer de cessar definitivamente os descontos, baixar a averbação no INSS e liberar integralmente a margem consignável correspondente;
3. o réu seja condenado à obrigação de não fazer: não averbar de novo, não descontar, não cobrar, não inscrever a parte autora em cadastros restritivos e não ceder a terceiros o crédito impugnado;
4. o réu seja condenado à obrigação de fazer de preencher, no sistema eConsignado/DATAPREV, o campo "Motivo da Exclusão", hoje em branco, com a expressão "Por força de decisão judicial", mantido inalterado o campo "Origem da Exclusão", em 10 (dez) dias úteis, sob pena de multa diária de R$ 500,00, nos termos dos arts. 497 e 537 do CPC [[SE HÁ ATIVO]], providência que, quanto a contrato ativo, será cumprida no momento da baixa [[FIM]];
5. o réu seja condenado a restituir em dobro os valores descontados, no total atual de [TOTAL DO DOBRO POR EXTENSO], assim discriminados: [uma linha por contrato com o dobro por extenso]. Correção monetária desde cada desconto (Súmula 43 do STJ) e juros de mora desde o evento danoso (Súmula 54 do STJ). Requer-se que os descontos posteriores a esta petição, até o trânsito em julgado, sejam apurados na liquidação;
6. o réu seja condenado ao pagamento de indenização por danos extrapatrimoniais de **R$ 20.000,00 (vinte mil reais)**, com correção monetária desde o arbitramento (Súmula 362 do STJ) e juros de mora desde o evento danoso (Súmula 54 do STJ);
7. seja vedada a compensação entre eventual valor comprovadamente creditado à parte autora e a indenização por dano extrapatrimonial, que tem causa e função distintas, restringindo-se eventual acerto à restituição (art. 182 do CC);[[SE CRÉDITO EM CONTA]] quanto ao valor de [VALOR CREDITADO] creditado em [DATA DO CRÉDITO] (ID [__], p. [__]), requer-se [DECISÃO DO ADVOGADO: devolução, depósito em juízo ou compensação] [a sua devolução ao réu depois de declarada a inexistência | a autorização para depositá-lo em juízo | a sua compensação com a restituição material];[[FIM]]

[[SE JUSTIÇA COMUM]] h) a condenação do réu ao pagamento das custas e dos honorários advocatícios de sucumbência (art. 85 do CPC); [[FIM]]
[[SE JEC]] (Sem pedido de custas e honorários: a sentença de primeiro grau não condena o vencido, salvo litigância de má-fé — art. 55 da Lei 9.099/95.) [[FIM]]

Requer, ainda, que todas as intimações e publicações sejam feitas exclusivamente em nome de Diego Ramos Arléo Barbosa, OAB/BA nº 38.179, e Michael Santos Neves, OAB/BA nº 50.954.

# Do valor da causa

Dá-se à causa o valor de [VALOR DA CAUSA POR EXTENSO], correspondente à restituição em dobro ([TOTAL DO DOBRO]) e ao dano extrapatrimonial (R$ 20.000,00) (art. 292 do CPC). *CÁLCULO A CONFERIR.* [[SE CAIXA]] Valor real, sem renúncia a teto. [[FIM]]

Termos em que, pede deferimento.

[CIDADE DO FECHO, perguntada ao advogado] - [UF], [dd] de [mês por extenso] de [aaaa].


DIEGO RAMOS ARLÉO BARBOSA
OAB/BA nº 38.179

MICHAEL SANTOS NEVES
OAB/BA nº 50.954
