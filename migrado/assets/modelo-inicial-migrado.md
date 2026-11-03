<!--
MODELO — INICIAL DE CONSIGNADO MIGRADO (contrato averbado com origem "Migrado do contrato … CBC: …", cuja migração o beneficiário nega ter autorizado)

Como usar (instruções para quem redige; apague este comentário na peça):
- Preencha os campos [PREENCHER: ...] com o quadro de fatos e o calculo.json (scripts/calcular_migrado.py). Campo sem fonte vira [CONFERIR: ...].
- Blocos entre [[SE ...]] e [[FIM]] entram só quando a condição vale. Apague os marcadores.
- Números, datas e valores vêm de calculo.json. Nunca refaça a conta de cabeça.
- **A migração, por si, é permitida pela norma do INSS** (IN 138, art. 11; IN 28, art. 56). A tese não é "a norma não autoriza migração": é que **a cessão não foi notificada ao devedor** (CC, art. 290). **Não sustente a inexistência do crédito cedido** (decisão do escritório de 29/10/2026: argumento perigoso). O modelo anterior do escritório dizia que nenhuma norma autoriza a migração sem novo consentimento: não repita.
- **A norma depende da data da averbação**: até 12/12/2022, IN INSS/PRES 28/2008; desde 13/12/2022, IN 138/2022.
- Não afirme fraude em escala nem prática reiterada do banco, e não cite a operação policial de 2025 como contexto: ela apurou descontos de mensalidades de entidades associativas, e não empréstimos consignados; o acervo não tem fonte para o contexto que a petição anterior usava (ver references/02-mudancas-no-modelo.md).
- Não digite número de tópico: a tipografia-azul numera. Remissão interna: "tópico ..." calculado depois de fechada a estrutura.
- Títulos de tópico (#) no formato "Da/Do/Dos…"; subtópicos (##) em frase completa.
- Citação de lei: texto literal do acervo. Marcas [VERIFICAR ANTES DE PROTOCOLAR] ficam no ponto exato.
- Perguntar ao advogado ANTES de gerar: rito (JEC ou Justiça Comum), cidade/UF do fecho e interesse ou desinteresse na audiência de conciliação.
- Forma, endereçamento, qualificação e pedidos de rotina: assets/padrao-pecas.md (prevalece em caso de conflito).
-->

[[SE JEC]] [PREENCHER: `jec.enderecamento` da comarca em references/dados/tjba_unidades.json; comarca do município em tjba_comarcas.json] [[SE JUSTIÇA COMUM]] [PREENCHER: `comum.enderecamento` da comarca em references/dados/tjba_unidades.json] [[FIM]]

[[SE CAIXA]] Substituir o endereçamento por: AO JUÍZO DA [N]ª VARA FEDERAL DA SUBSEÇÃO JUDICIÁRIA DE [subseção da tabela TRF1] - BAHIA [[FIM]]

**EMENTA:** Empréstimo consignado. Averbação por migração de contrato de outra instituição financeira (troca de titularidade), sem nova manifestação de vontade do beneficiário. [Beneficiário/Beneficiária] do INSS. Cessão de crédito não notificada ao devedor (CC, art. 290). Inexistência de autorização para a migração. Nulidade da migração. Desconto indevido sobre verba de natureza alimentar. Responsabilidade objetiva da instituição financeira. Repetição do indébito em dobro. Dano extrapatrimonial.[[SE TUTELA]] Tutela de urgência para suspensão imediata dos descontos.[[FIM]]

**[NOME DO AUTOR]**, [nacionalidade], [estado civil], [profissão], [inscrito/inscrita] no CPF sob nº [CPF], RG sob nº [RG], [beneficiário/beneficiária] do INSS (NB [NB], [ESPÉCIE DO BENEFÍCIO]), [residente e domiciliado/domiciliada] na [ENDEREÇO], CEP [CEP], cidade de [CIDADE]/[UF], por seu advogado que esta subscreve (procuração anexa), vem, respeitosamente, perante este Juízo, propor a presente

## Ação Declaratória de Inexistência de Relação Jurídica e Nulidade de Migração de Contrato, Cumulada com Repetição do Indébito em Dobro, Obrigação de Fazer e Indenização por Danos Extrapatrimoniais[[SE TUTELA]], com Pedido de Tutela Provisória de Urgência[[FIM]]

em face **[RÉU]**, [descrição do réu de references/dados/reus.json: pessoa jurídica, CNPJ e endereço], [[SE JEC]] pelo procedimento da Lei nº 9.099/95, [[FIM]] pelos seguintes fatos, fundamentos e razões de direito.

# Da gratuidade da justiça

A parte autora não tem condições de arcar com as despesas do processo, uma vez que são insuficientes seus recursos financeiros para pagar todas as despesas processuais, inclusive o recolhimento das custas iniciais.

Requer sejam deferidos os benefícios da gratuidade da justiça, o que faz por declaração de seus advogados, nos termos do art. 99, § 4º, c/c o art. 105, in fine, ambos do CPC, prerrogativa que consta do instrumento procuratório anexo. Presume-se verdadeira a alegação de insuficiência deduzida por pessoa natural (art. 99, § 3º, do CPC).[[SE JEC]] No Juizado Especial, o acesso em primeiro grau independe do pagamento de custas, taxas ou despesas (art. 54 da Lei 9.099/95).[[FIM]]

# Da tramitação prioritária

[[SE IDADE ≥ 60]] Conforme documento pessoal anexo, a parte autora é pessoa idosa e faz jus à prioridade na tramitação (art. 1.048, I, do CPC; art. 71 da Lei 10.741/2003 — Estatuto da Pessoa Idosa). [[FIM]]

[[SE JEC]]
# Da competência do Juizado Especial

A causa é de competência do Juizado Especial Cível (art. 3º, I, da Lei 9.099/95): o valor da causa, [VALOR DA CAUSA], é inferior a 40 (quarenta) salários mínimos, que, à razão de [SALÁRIO MÍNIMO VIGENTE NO AJUIZAMENTO: Decreto 12.797/2025, R$ 1.621,00, para 2026; outro ano, decreto daquele ano], correspondem a [40 × SALÁRIO MÍNIMO: R$ 64.840,00 em 2026]. A prova é documental (o extrato oficial do INSS).
[[FIM]]

# Dos fatos

A parte autora é beneficiária do INSS, e o benefício previdenciário é a sua única fonte de renda.

Em [DATA DE EMISSÃO], ao analisar o Histórico de Empréstimo Consignado emitido pelo INSS (ID [__], p. [__]), a parte autora tomou conhecimento de descontos de contratos de empréstimo consignado migrados para o réu sem sua autorização, relacionados a seguir.

O extrato registra, no campo "Origem da Averbação", que os contratos impugnados foram averbados pelo réu como migração de contrato anteriormente mantido com outra instituição financeira:

[UMA LINHA POR CONTRATO, de calculo.json: "— Contrato [CONTRATO], averbado em [AVERBAÇÃO], com a anotação do extrato: '[ORIGEM DA AVERBAÇÃO]'."]

| Contrato | Origem da averbação | Banco de origem (código) | Averbação | Início | Fim | Parcela | Qtde. | Total descontado | Restituição (dobro) | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| [uma linha por contrato, de calculo.json] | | | | | | | | | | |
| **Total** | | | | | | | | [total] | [total em dobro] | |

*Fonte: Histórico de Empréstimo Consignado do INSS, emitido em [DATA DE EMISSÃO] (ID [__], p. [__]). CÁLCULO A CONFERIR.*

[[SE TROCA DE TITULARIDADE]] O extrato registra ainda o mesmo número de contrato sob o código [CÓDIGO E NOME DO BANCO ANTERIOR], com [DESCREVER SÓ O QUE ESTÁ NO EXTRATO: situação, datas, parcelas, motivo da baixa; calculo.json, campo outras_ocorrencias]. [[SE COMPETÊNCIAS COINCIDEM]] A contagem de descontos deste quadro não soma as competências registradas no banco anterior, porque coincidem com as do registro do réu (mesma inclusão, mesma parcela, mesmo valor liberado e mesmo início dos descontos). [[SENÃO]] A contagem de descontos deste quadro [inclui / não inclui] os registrados no banco anterior [DECISÃO DO ADVOGADO; script: --incluir-outros-bancos]. [[FIM]] [[FIM]]

A parte autora jamais foi consultada, contatada ou informada sobre essas migrações. Não assinou novo instrumento, não forneceu nova autorização biométrica e não manifestou, por qualquer meio admitido em direito, a vontade de transferir dívida ou de contratar com o réu.

## A parte autora nega a migração

Para cada contrato da tabela, escrever um parágrafo com os campos do quadro de fatos; contratos com os mesmos fatos podem ser reunidos em uma linha "Contratos nº X e Y. Valem as mesmas afirmações", sempre com o valor liberado de cada um. Não afirmar o que só o contrato ou o log do banco podem mostrar.

> **Contrato nº [CONTRATO].** A parte autora nega a migração: não foi consultada, não assinou novo instrumento com o réu e não autorizou a averbação nem a transferência do contrato; não contesta a contratação de origem, firmada com o banco de origem. [[SE ASSINATURA IMPUGNÁVEL]] Se o banco juntar instrumento com assinatura, desde já fica impugnada a sua autenticidade, o que desloca ao banco o ônus de prová-la. [[FIM]] O extrato do INSS registra valor liberado de [VALOR LIBERADO DO EXTRATO] [[SE LIBERADO AUSENTE/ZERO]] ou não registra valor liberado algum [[FIM]]. Essa anotação é lançamento da própria instituição financeira no sistema de averbação e não prova crédito em conta de titularidade da parte autora. Cabe ao banco comprovar o crédito (art. 373, II, do CPC).

A parte autora não utiliza plataformas digitais de autenticação, não domina mecanismos de verificação biométrica, tokens ou senhas dinâmicas e jamais forneceu sua imagem facial, dados biométricos ou credenciais de acesso.

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

O Tema Repetitivo 466 do STJ firmou que as instituições financeiras respondem objetivamente pelos danos gerados por fortuito interno relativo a fraudes e delitos praticados por terceiros no âmbito de operações bancárias, entre elas o recebimento de empréstimo mediante fraude ou com documentos falsos.

## A norma do INSS admite a migração de carteira, mas a cessão não vale contra o devedor que não foi notificado

A parte autora não impugna a possibilidade de a carteira de crédito consignado migrar entre instituições financeiras. O que impugna é que as migrações ocorreram sem que ela, devedora, fosse notificada.

A IN PRES/INSS 138/2022 define a troca de titularidade como a "migração da carteira (ou parte dela) de operações de crédito de instituição credora original para instituição proponente" (art. 4º, XVI), e dispõe que a cessão de créditos entre instituições financeiras "poderá ser realizada, desde que atenda às normas editadas pelo BCB e pelo CMN" (art. 11). [[SE REAVERBAÇÃO ATÉ 12/12/2022]] Até 12/12/2022, a IN INSS/PRES 28/2008 trazia regra equivalente (art. 56), com remissão à Resolução CMN 2.836/2001, que autoriza as instituições financeiras a ceder, entre si, créditos oriundos de operações de empréstimo (art. 1º). [[FIM]]

A migração é, portanto, uma cessão de crédito. O Código Civil permite ao credor "ceder o seu crédito" (art. 286), mas a eficácia da cessão perante o devedor tem condição. O art. 290 do Código Civil dispõe que "a cessão do crédito não tem eficácia em relação ao devedor, senão quando a este notificada; mas por notificado se tem o devedor que, em escrito público ou particular, se declarou ciente da cessão feita". O extrato não registra notificação nem ciência da parte autora. Cabe ao banco demonstrar que a migração atendeu às normas do BCB e do CMN e que a parte autora foi notificada.

## Se o banco alegar nova contratação, ela exigiria instrumento e autorização assinados

[[SE REAVERBAÇÃO ATÉ 12/12/2022]]
A averbação em [AVERBAÇÃO] está sob a IN INSS/PRES 28/2008, vigente até 12/12/2022. Seu art. 5º determina que a instituição financeira somente encaminhará o arquivo para averbação **após a devida assinatura do contrato** pelo beneficiário, ainda que por meio eletrônico, e seu art. 6º atribui à instituição total responsabilidade pela inobservância, tornando a operação irregular e não autorizada.
[[FIM]]

[[SE REAVERBAÇÃO A PARTIR DE 13/12/2022]]
A averbação em [AVERBAÇÃO] está sob a IN PRES/INSS 138/2022. Seu art. 5º, II, exige desconto formalizado por contrato firmado e assinado, com uso de reconhecimento biométrico, documento oficial com foto e CPF, e o inciso III exige autorização da consignação dada de forma expressa e assinada com reconhecimento biométrico. As consignações eletivas dependem de "expressa vontade do titular do benefício" (art. 4º, XXVII).
[[FIM]]

O registro "Migrado do contrato" mostra que o banco **não** se apresenta como autor de uma nova contratação. Se alegar o contrário, precisa exibir o instrumento e a autorização, assinados e, quando a norma exigir, com biometria, datados da averbação.

## A inexistência do negócio decorre da ausência de consentimento da parte autora

O art. 104 do Código Civil exige, para a validade do negócio jurídico, agente capaz, objeto lícito e forma prescrita ou não defesa em lei. No consignado em benefício do INSS soma-se a manifestação expressa do beneficiário (tópico anterior). Quanto aos contratos impugnados, não há registro de instrumento, de autorização ou de ato da parte autora, nem com o banco de origem nem com o réu. A prova de que existiram incumbe ao banco, por força do art. 14, § 3º, do CDC e da inversão pedida abaixo; [[SE ASSINATURA IMPUGNÁVEL]] se juntar instrumento assinado, o ônus de provar a autenticidade da assinatura impugnada é seu (Tema Repetitivo 1061 do STJ). [[FIM]] Sem consentimento, o que existe é ato do banco, sem força obrigatória, que usa o sistema do INSS para descontar valores do benefício sem causa jurídica.

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

## A restituição ao estado anterior opera em favor da parte autora

Declarada a inexistência e a nulidade, as partes voltam ao estado anterior (art. 182 do CC). Aqui a restituição opera em uma só direção: [[SE CRÉDITO EM CONTA]] o crédito que o extrato bancário da parte autora registra não prova a migração e tem o tratamento do tópico dos fatos e do pedido 7. [[SENÃO]] o banco não comprovou crédito algum em conta de titularidade da parte autora, e a anotação de valor liberado no extrato é lançamento da própria instituição. [[FIM]] A restituição ao estado anterior é a devolução à parte autora, em dobro, do que lhe foi descontado. Eventual crédito que o banco demonstre por documento idôneo só poderá ser considerado no acerto da restituição material, e nunca por compensação com a indenização extrapatrimonial, que tem causa e função distintas.

A vedação ao enriquecimento sem causa (art. 884 do CC) não socorre o banco, que desconta sem comprovar desembolso. A boa-fé objetiva (art. 422 do CC) veda ainda o comportamento contraditório: o banco, que não verificou a contratação, não pode invocá-la para reaver o que não prova ter entregue.

[[SE LGPD]]
# Da Lei Geral de Proteção de Dados

[DECISÃO DO ADVOGADO: manter ou retirar este tópico. Os dispositivos estão em normas/lgpd.md; o modelo anterior do escritório os usava, e o AMN v1.4 usava o art. 37 da LGPD como norma de guarda da trilha, o que se retirou.]

A averbação de contrato que a parte autora não firmou pressupõe o tratamento de seus dados pessoais (nome, documentos, número de benefício). Sem base legal e sem consentimento, esse tratamento viola a Lei 13.709/2018. O dado biométrico é dado pessoal sensível (art. 5º, II) e só pode ser tratado com consentimento específico e destacado do titular (art. 11, I). O controlador deve observar os princípios da segurança, da prevenção e da responsabilização (art. 6º, VII, VIII e X) e adotar medidas de segurança aptas a proteger os dados (art. 46). A falha que permitiu a averbação reforça a responsabilidade do banco.
[[FIM]]

# Da inversão do ônus da prova

O ônus de provar a regularidade da contratação e da migração é do banco por força de lei, independentemente de decisão judicial: art. 14, § 3º, do CDC e, quando se impugna a autenticidade da assinatura, art. 429, II, do CPC, com o Tema Repetitivo 1061 do STJ.³ A inversão judicial do art. 6º, VIII, do CDC reforça esse resultado:

> Art. 6º São direitos básicos do consumidor: (...) VIII - a facilitação da defesa de seus direitos, inclusive com a inversão do ônus da prova, a seu favor, no processo civil, quando, a critério do juiz, for verossímil a alegação ou quando for ele hipossuficiente, segundo as regras ordinárias de experiências;

A verossimilhança está no próprio extrato, que registra a origem "Migrado do contrato". A hipossuficiência é técnica: contrato, autenticação, instrumento da migração e crédito estão sob domínio exclusivo do banco. Requer-se a inversão e que o banco junte, **com a contestação**, os documentos abaixo, para cada contrato:

| Documento | Fundamento | Se não for apresentado |
|---|---|---|
| Contrato de origem, com o instrumento assinado e a autenticação da contratação com o banco anterior | Art. 429, II, do CPC; Tema 1061/STJ; IN 28/2008, art. 5º (até 12/12/2022); IN 138/2022, art. 5º, II e III (desde 13/12/2022) | [[SE JEC]] o fato impeditivo não está provado, e isso se valora contra o banco (art. 373, II, do CPC) [[SE JUSTIÇA COMUM]] admitem-se como verdadeiros os fatos que o documento provaria (art. 400 do CPC) [[FIM]] |
| Instrumento da cessão ou da troca de titularidade entre os bancos, com a demonstração de que atendeu às normas do BCB e do CMN | IN 138/2022, arts. 4º, XVI, e 11; IN 28/2008, art. 56 (até 12/12/2022) | Mesma consequência |
| Prova de que a parte autora foi notificada ou se declarou ciente da cessão | Art. 290 do CC | Mesma consequência |
| Comprovante do crédito efetivo em conta de titularidade da parte autora, de valor idêntico ao liberado no extrato | Art. 14, § 3º, do CDC; art. 373, II, do CPC | Mesma consequência |
| [[SE REAVERBAÇÃO A PARTIR DE 13/12/2022]] Registro biométrico da contratação [[FIM]] | IN 138/2022, art. 5º, II | Mesma consequência |

³ BRASIL. Superior Tribunal de Justiça. Segunda Seção. Tema Repetitivo 1061. Recurso Especial n. 1.846.649/MA. Relator: Ministro Marco Aurélio Bellizze. Julgado em: 24 nov. 2021. Publicado no DJe em: 9 dez. 2021.

[[SE JUSTIÇA COMUM]]
## A exibição dos documentos e a perícia são necessárias

Requer-se, também, a exibição dos documentos acima (arts. 396 a 404 do CPC) no prazo do art. 398, com as consequências do art. 400.

Havendo [[SE ASSINATURA MANUSCRITA]] assinatura manuscrita impugnada, requer-se perícia grafotécnica [[SE TRILHA ELETRÔNICA]] trilha eletrônica de contratação, requer-se perícia em informática forense [[FIM]], com os seguintes quesitos [QUESITOS A VALIDAR PELO ADVOGADO; propostos abaixo]:

1. A assinatura aposta no instrumento de origem (ID [__]) procede do punho da parte autora, confrontada com os padrões indicados (documento de identidade, procuração)?
2. Há elementos de imitação, decalque ou montagem na assinatura questionada?
3. [Trilha eletrônica] Os registros de IP, dispositivo e localização do aceite (ID [__]) são compatíveis com o local de residência da parte autora?
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

[[SE JUSTIÇA COMUM]]
# Dos honorários sobre a soma da condenação e do proveito econômico

O art. 85, § 2º, do CPC fixa os honorários entre 10% e 20% "sobre o valor da condenação, do proveito econômico obtido ou, não sendo possível mensurá-lo, sobre o valor atualizado da causa". Esta ação tem dois resultados econômicos distintos: o capítulo condenatório (repetição em dobro e reparação extrapatrimonial) e o capítulo declaratório, que libera a parte autora das parcelas vincendas dos contratos ativos, no valor de [VINCENDAS, de calculo.json], descontadas mensalmente do benefício [DECISÃO DO ADVOGADO: adotar o proveito declaratório como base; só vale com contrato ativo].

O Tema Repetitivo 1076 do STJ firmou que a fixação de honorários por apreciação equitativa não é permitida quando os valores da condenação, da causa ou o proveito econômico forem elevados, e que o arbitramento por equidade só se admite quando o proveito econômico for inestimável ou irrisório, ou o valor da causa for muito baixo. Aqui o proveito é líquido e calculado contrato a contrato. Em ação declaratória de inexistência de contrato bancário cumulada com danos morais, a Terceira Turma do STJ admitiu a soma do valor da condenação com o proveito econômico (REsp 2.168.312/PR, Rel. Min. Humberto Martins, j. 03/11/2025, DJEN 06/11/2025; Informativo 875/STJ), segundo o qual o art. 85, § 2º, do CPC "não impede a cumulação das bases de cálculo dos honorários advocatícios sucumbenciais, sendo possível considerar tanto o valor da condenação quanto o proveito econômico obtido".
[[FIM]]

# Dos pedidos

Diante do exposto, requer:

a) o deferimento da gratuidade da justiça (arts. 98 e 99, caput e § 3º, do CPC[[SE JEC]]; art. 54 da Lei 9.099/95[[FIM]]);

b) a prioridade de tramitação [[SE IDADE ≥ 60]] (art. 1.048, I, do CPC; art. 71 da Lei 10.741/2003) [[FIM]];

c) a citação do réu para que apresente contestação no prazo legal, sob pena de revelia, [[SE COM INTERESSE NA CONCILIAÇÃO]] manifestando a parte autora interesse na audiência de conciliação [[SE SEM INTERESSE NA CONCILIAÇÃO]] declarando a parte autora, desde já, desinteresse na audiência de conciliação (arts. 319, VII, e 334, § 5º, do CPC) [[FIM]];

[[SE TUTELA]] d) a antecipação dos efeitos da tutela, nos termos do tópico próprio, para que o réu se abstenha de novos descontos referentes ao(s) contrato(s) nº [CONTRATOS ATIVOS]; [[FIM]]

e) a inversão do ônus da prova, com o encargo de o réu juntar, com a contestação, os documentos do tópico [REMISSÃO: tópico da inversão do ônus]; [[SE JUSTIÇA COMUM]] a exibição desses documentos e a perícia [grafotécnica / em informática forense] com os quesitos do tópico [REMISSÃO]; [[FIM]]

f) a apreciação expressa de cada precedente evocado, nos termos do art. 489, § 1º, VI, do CPC;

g) a procedência dos pedidos, confirmada a tutela ou concedida em sentença, para que:

1. seja declarada a inexistência da relação jurídica entre as partes quanto ao(s) contrato(s) nº [CONTRATOS] e a nulidade da sua migração e averbação, com a inexigibilidade de todo e qualquer débito decorrente;
2. [[SE HÁ ATIVO]] o réu seja condenado à obrigação de fazer de cessar definitivamente os descontos, baixar a averbação no INSS e liberar integralmente a margem consignável correspondente; [[FIM]] [[SE SÓ EXCLUÍDO]] o réu seja condenado à obrigação de fazer de manter a baixa do(s) contrato(s) e de não restabelecer a margem comprometida; [[FIM]]
3. o réu seja condenado à obrigação de não fazer: não averbar de novo nem migrar o(s) contrato(s) impugnado(s), não descontar, não cobrar, não inscrever a parte autora em cadastros restritivos e não ceder a terceiros o crédito impugnado;
4. o réu seja condenado à obrigação de fazer de preencher, no sistema eConsignado/DATAPREV, o campo "Motivo da Exclusão", hoje em branco, com a expressão "Por força de decisão judicial", mantido inalterado o campo "Origem da Exclusão", em 10 (dez) dias úteis, sob pena de multa diária de R$ 500,00, nos termos dos arts. 497 e 537 do CPC [[SE HÁ ATIVO]], providência que, quanto a contrato ativo, será cumprida no momento da baixa [[FIM]];
5. o réu seja condenado a restituir em dobro os valores descontados, no total atual de [TOTAL DO DOBRO POR EXTENSO], assim discriminados: [uma linha por contrato com o dobro por extenso]. Correção monetária desde a data de cada desconto (Súmula 43 do STJ) e juros moratórios a contar do evento danoso (Súmula 54 do STJ). Requer-se que os descontos posteriores a esta petição, até o trânsito em julgado, sejam apurados na liquidação;
6. o réu seja condenado ao pagamento de indenização por danos extrapatrimoniais de **R$ 20.000,00 (vinte mil reais)**, com correção monetária desde o arbitramento (Súmula 362 do STJ) e juros de mora desde o evento danoso (Súmula 54 do STJ);
7. seja vedada a compensação entre eventual valor comprovadamente creditado à parte autora e a indenização por dano extrapatrimonial, que tem causa e função distintas, restringindo-se eventual acerto à restituição (art. 182 do CC);[[SE CRÉDITO EM CONTA]] quanto ao valor de [VALOR CREDITADO] creditado em [DATA DO CRÉDITO] (ID [__], p. [__]), requer-se [DECISÃO DO ADVOGADO: devolução, depósito em juízo ou compensação] [a sua devolução ao réu depois de declarada a inexistência | a autorização para depositá-lo em juízo | a sua compensação com a restituição material];[[FIM]]

[[SE JUSTIÇA COMUM]] h) a condenação do réu ao pagamento das custas e dos honorários advocatícios de sucumbência (art. 85 do CPC), [PERCENTUAL: de 10% a 20%, art. 85, § 2º; o modelo anterior pedia 20%] sobre a soma do valor da condenação e do proveito econômico, este de [VINCENDAS], com a fixação expressa dessa base na sentença; subsidiariamente, sobre o proveito econômico total ou o valor atualizado da causa, vedada a equidade (Tema 1076/STJ); [[FIM]]
[[SE JEC]] (Sem pedido de custas e honorários: a sentença de primeiro grau não condena o vencido, salvo litigância de má-fé — art. 55 da Lei 9.099/95.) [[FIM]]

Requer, ainda, que todas as intimações e publicações sejam feitas exclusivamente em nome de Diego Ramos Arléo Barbosa, OAB/BA nº 38.179, e Michael Santos Neves, OAB/BA nº 50.954.

# Do valor da causa

Dá-se à causa o valor de [VALOR DA CAUSA POR EXTENSO], correspondente à restituição em dobro ([TOTAL DO DOBRO]) e ao dano extrapatrimonial (R$ 20.000,00) (art. 292 do CPC). [[SE JUSTIÇA COMUM E HÁ ATIVO]] [DECISÃO DO ADVOGADO: somar o proveito econômico declaratório de [VINCENDAS] (valor da causa com proveito: [VALOR_CAUSA_COM_PROVEITO POR EXTENSO]; art. 292, II e VI, do CPC)] [[FIM]] *CÁLCULO A CONFERIR.* [[SE CAIXA]] Valor real, sem renúncia a teto. [[FIM]]

Termos em que, pede deferimento.

[CIDADE DO FECHO, perguntada ao advogado] - [UF], [dd] de [mês por extenso] de [aaaa].


DIEGO RAMOS ARLÉO BARBOSA
OAB/BA nº 38.179

MICHAEL SANTOS NEVES
OAB/BA nº 50.954
