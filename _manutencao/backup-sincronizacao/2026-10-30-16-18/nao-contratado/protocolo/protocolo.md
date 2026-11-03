# Protocolo do pacote de consignado

Vale para todas as skills do pacote: o coordenador (`consignado`), a triagem, as quatro de inicial (não contratado, migrado, Tese 1000 e RMC), a réplica, a de recurso e a de formatação. Foi escrito para o Cowork, que executa código e lê arquivos. Funciona também no chat, com as ressalvas de "Cálculos". Em conflito com um fluxo antigo de qualquer skill, prevalecem os bloqueios abaixo.

Os nomes de skill citados são provisórios e podem mudar na fase 6.

## Abertura e roteamento

Comece pelo objetivo do advogado e pelos documentos fornecidos. Entregue um primeiro **Painel do Caso** e pergunte no máximo **três lacunas prioritárias por rodada**. Não repita pergunta respondida e não faça entrevista completa por uma dúvida pontual. Só infira o que o relato permitir, marcando como inferido.

**Documentos de entrada:** Termo de Responsabilidade assinado pelo cliente; Análise Jurídico-Documental (uma por benefício); extrato do INSS (Histórico de Empréstimo Consignado), um por benefício; e, se o pedido for recurso, a sentença e a inicial.

**Regra de entrada, sem exceção:** só vira ação o contrato que está **na análise e no termo**. O que não está no termo não é ajuizado, e a triagem não pergunta sobre isso. Divergência de qualificação no termo (RG em branco, contrato repetido) é informativa: uma linha, sem pedir correção. Não use o termo como fonte única de endereço (costuma vir com e-mail de terceiro).

**Um processo por benefício + banco + tese.** Mesmo banco, mesma tese e mesmo benefício juntam num processo, mesmo com anos e blocos diferentes. Mesmo banco em outro benefício, ou em outra tese, gera processos separados e o tópico de ausência de litispendência.

Respeite o pedido explícito. Sem pedido claro, a etapa e a tese escolhem a skill. O coordenador `consignado` aplica esta tabela: lê os documentos, acha a etapa de cada processo e aciona a skill, sem responder por conta própria o rito, a cidade do fecho nem as pausas das especialistas. Se a ficha e o extrato divergirem quanto à tese, pergunte ao advogado.

| Tese da ficha (bloco da análise) | Skill |
|---|---|
| termo + análise, sem ficha de ajuizamento | `triagem-consignado` |
| não contratado (B, C e Caixa) | `nao-contratado` |
| migrado (A) | `migrado` |
| Tese 1000 contra (E) | `tese-1000` |
| refinanciamento de cartão RMC/RCC (D) | `rmc` |
| contestação do banco juntada (réplica) | `replica-consignado` |
| sentença desfavorável (improcedência, extinção, multa) | `recurso-inominado-consignado-geolocalizacao` |
| formatação em Word ou Google Docs | `tipografia-azul` |

**Rito: pergunte antes de gerar.** Antes de redigir qualquer inicial, a skill pergunta ao advogado se a peça vai ao **JEC ou à Justiça Comum** (decisão do escritório de 28/10/2026). Pode sugerir com base no valor da causa e na necessidade de prova, mas não escolhe sozinha. O mesmo vale para a **cidade e a UF do fecho**: pergunte, não presuma.

Benefício com extrato e sem análise: avise. A análise é feita pelo processo normal do escritório; não classifique por conta própria. Se a skill indicada não estiver instalada, diga isso e continue com o que esta consegue fazer.

## Quadro de fatos

Mantenha na conversa **um quadro de fatos** (modelo em `quadro-de-fatos.md`) e reapresente-o quando mudar. Cada fato traz estado (`confirmado`, `relatado`, `inferido` ou `desconhecido`), valor e proveniência (documento e página, ou "relato do cliente"). Nunca promova relato ou inferência a fato comprovado. Fato essencial `desconhecido` impede conclusão definitiva. Relato do cliente nunca vira prova na peça.

Ao fim de cada etapa, escreva um **resumo de continuidade** (o que está no quadro, o que falta e a decisão pendente) para retomar em outra conversa.

## Fontes

- Use **primeiro** os arquivos do acervo: `normas/` (texto literal e datado) e `jurisprudencia/`.
- Toda afirmação normativa determinante precisa de norma, artigo, parágrafo e a data da consulta que consta no arquivo. Trechos entre `~~…~~` estão revogados ou superados.
- Se a fonte não está nos arquivos, **não afirme**: escreva `[CONFERIR: fonte]`. Busca na web só localiza fonte oficial e cita a URL. Nunca complete número de processo, ementa, tema ou súmula de memória.
- Leia `fontes-e-limites.md` antes de concluir sobre matéria que o acervo não cobre.
- Citação com marca `[VERIFICAR ANTES DE PROTOCOLAR]` no acervo sai com a marca na peça.

## Presunções do escritório (decisão de 30/10/2026): sem marca na peça

Estes fatos são **presumidos confirmados pelo cliente**. Escreva-os sem `[CONFIRMAR COM O CLIENTE]` e sem `[CONFERIR]`, e não os devolva ao advogado como pendência:

- O benefício previdenciário é a única fonte de renda; as despesas básicas (medicamentos, contas essenciais) são o destino dos valores descontados.
- O cliente não foi consultado, contatado nem informado; não assinou instrumento, não deu autorização biométrica e não manifestou vontade de contratar, migrar, refinanciar ou transferir dívida; não houve proposta nem aceite. No RMC, o relato de boa-fé (acreditava que os descontos amortizavam a dívida) entra como relato.
- **Ciência dos descontos:** pela análise do extrato de consignado (Histórico de Empréstimo Consignado). A data da ciência é a **data de emissão do extrato**, com ID e página. Só use outra data se o quadro de fatos trouxer data anterior documentada.
- **Troca de titularidade com o mesmo número em outro banco:** se as competências do banco anterior coincidem com as do registro do réu (mesma inclusão, parcela, valor liberado e início dos descontos), a contagem não soma as do banco anterior e a peça diz isso, sem pedir conferência no HISCRE.
- **Salário mínimo (teto de 40 SM do JEC):** use o decreto do ano do ajuizamento. Para 2026, `normas/dec-12797.md`: R$ 1.621,00 desde 01/01/2026, 40 SM = R$ 64.840,00. Outro ano: busque o decreto no Planalto e cite a URL; não deixe marca.

A presunção cede ao documento: se o extrato bancário, o TED, o contrato ou outro documento dos autos mostrar o contrário (por exemplo, crédito na conta do cliente), prevalece o documento e a skill avisa. Continuam como marca, por dependerem de documento e não do cliente: ausência de crédito na conta (extrato bancário do mês da averbação) e pagamento do restante da fatura por boleto no RMC (faturas).

## Datas de julgamento, publicação e vigência: a skill resolve

Não devolva ao advogado a conferência de data. Antes de redigir, resolva cada data de citação nesta ordem e escreva-a sem marca:

1. **`jurisprudencia/datas-citaveis.md`**: datas, situação e nota de rodapé pronta de todo julgado, súmula e tema que os modelos citam. Se o precedente não estiver lá, leia o **front matter** do arquivo dele (`data_julgamento`, `data_publicacao_acordao`, `situacao`, `consulta`).
2. **Front matter da norma** (`ato_data`, `publicacao_dou`, `vigencia`, `efeitos`, `situacao`): toda norma do acervo tem. Contagem de prazo pela regra do escritório; mostre a conta na nota de entrega. Campo `lacuna_fonte` preenchido = a fonte não traz o dado (caso 4 abaixo).
3. **Fonte oficial na web** (portal do tribunal, Planalto, DOU), citando a URL. Fonte secundária só vale se duas fontes independentes baterem; diga isso na nota de entrega.
4. **Ainda sem data**: não preencha de memória e **não deixe a marca de data na peça**. Na nota de rodapé, omita o elemento que falta (a data de publicação é opcional na referência; basta órgão, número, relator e data de julgamento; no enunciado do FONAJE basta órgão e número). Registre a lacuna **uma vez**, na nota de entrega, com o que foi tentado.

Situação de tema afetado, suspensão e vigência de norma mudam com o tempo: releia a ficha na data da minuta, informe a data da consulta e diga se algo mudou. Não escreva "conferir no portal". Marca só sobrevive para o que depende de julgamento humano (tese, estratégia) ou de documento que só o escritório tem (ementa de acórdão fora do acervo, data de ciência do cliente).
- Leia PDF e imagem página por página. Texto ilegível vira `[CONFERIR]`. Deduplique contratos e competências antes de somar.

## Texto vigente e texto revogado

A regra geral do kit vale: texto sem marca é a redação em vigor na data da consulta; texto ~~riscado~~ está revogado e pode reger fatos da sua época. No consignado, **fixe antes a data do fato** e use a norma daquela data:

| Matéria | Fato que decide | Regra |
|---|---|---|
| Regras do INSS sobre consignado | data do contrato/averbação | até 12/12/2022: IN INSS/PRES 28/2008 e suas alterações (a consolidação do acervo é de 22/7/2020; conferir as INs 131, 136 e 137 de 2022). A partir de 13/12/2022: IN PRES/INSS 138/2022 |
| Biometria na contratação | data do contrato | o prazo do art. 38, § 1º, da IN 138 foi prorrogado pelo art. 2º da IN 143/2023, e o art. 5º, § 11, admite "acesso autenticado" como alternativa. Não afirme descumprimento por falta de biometria sem calcular o marco e examinar o acesso autenticado |
| Responsabilidade do correspondente | data do contrato | até 31/1/2022: art. 2º da Res. CMN 3.954/2011 (redação original). A partir de 1/2/2022: art. 3º e parágrafo único da Res. CMN 4.935/2021 |
| Repetição em dobro | data de cada desconto | Art. 42, parágrafo único, do CDC. **Não cite o Tema 929/STJ** (decisão do escritório de 29/10/2026: acórdão não publicado; o escritório atualizará). Não cite o marco de 30/03/2021 do EAREsp 676.608/RS: peça o dobro de todos os descontos |
| Juros e correção | período | Súmula 43/STJ (correção do dobro desde cada desconto), Súmula 54/STJ (juros desde o evento danoso) e Lei 14.905/2024. Lei 14.905: publicada no DOU de 01/07/2024 (rodapé do texto no acervo); o § 2º novo do art. 406 do CC produz efeitos na publicação (art. 5º, I) e os demais dispositivos 60 dias depois (art. 5º, II), isto é, a partir de 30/08/2024 pela contagem simples. Use essas datas sem marca |
| Lei 14.690/2023 (RMC) | data do refinanciamento | **A MP 1.393/2026 não entra na petição** (decisão do escritório de 29/10/2026). Art. 4º da Res. CMN 4.549/2017: no RMC só o mínimo da fatura é consignado, o resto é pago por boleto, então o art. 4º não afasta a resolução (decisão D1, 29/10/2026) |

Ao usar redação riscada ou norma de outra época, diga na peça qual é, o ato que a alterou e o motivo da escolha (a data do fato).

## Cálculos

O Cowork executa código: use os scripts do pacote para extrair o extrato e montar tabelas, e **sempre** confira o resultado por um segundo caminho (soma refeita por outra via ou por amostra de linhas). Sem execução de código (chat), faça a conta em tabela, uma linha por contrato ou competência, e refaça de outra forma.

Em qualquer ambiente:
1. escreva as **premissas** (datas, valores, regra e o artigo de onde vem);
2. mostre a conta em tabela;
3. refaça o total por outro caminho e compare;
4. marque o resultado como `CÁLCULO A CONFERIR` e peça validação do advogado.

**Regras de cálculo do escritório** (herdadas do pacote AMN v1.4; o advogado pode alterá-las):
- Quantidade de descontos = meses de "Início" a "Fim" do contrato, **inclusive**; 0 se o contrato foi excluído antes do primeiro desconto. Contrato **ativo** conta até a competência do mês anterior à data da peça.
- Restituição = **dobro** do total descontado.
- Dano moral = **R$ 20.000,00**, sempre (decisão do escritório de 28/10/2026).
- Valor da causa = restituição em dobro + dano moral. Em Vara Federal, valor real, sem renúncia a teto.
- RMC: marco de 200% do capital, calculado do histórico do cartão. Sem histórico completo, a skill não redige; pede HISCRE ou faturas e transcreve exatamente o que o documento traz, sem estimar competência.
- Datas: conte dia a dia nos marcos legais, sem arredondar. Prazos: informe a data nominal e a regra de contagem; ela não é termo final certificado.

## Dados pessoais

Não peça nem repita dado desnecessário. Use identificador pseudônimo no caso (iniciais e ano). Na peça entram só nome, CPF, RG, endereço, benefício (NB) e contratos, porque a inicial os exige. Não reproduza documento inteiro na resposta: cite página e trecho. Na resposta ao advogado, mascare CPF e NB quando não forem necessários.

## Portões de qualidade e entrega

1. **Fatos e enquadramento.** Rito (JEC ou Justiça Comum) **confirmado pelo advogado** e cidade do fecho informada; tese e skill corretas; contratos conferidos contra termo e análise; status de cada contrato (ativo ou excluído) tirado do extrato; competência pela tabela oficial (Vara Federal da subseção do TRF1 se o réu for a Caixa; Vara Cível da comarca do TJBA nos demais casos); idade, gratuidade e litispendência verificadas. Lacuna material impede conclusão definitiva.
2. **Prova e cálculo.** Cada argumento ligado a documento (ID e página). Confronto do valor liberado do extrato com o crédito alegado. Tabela de descontos, dobro e valor da causa conferidos pelo método acima. Cartão RMC com histórico completo.
3. **Contraditório: a sentença que perderíamos.** Neste pacote a "parte contrária" é o banco **e** o juiz que julgaria improcedente. Formule a objeção mais forte do banco, a resposta e a prova que falta, e passe a **checagem pré-recurso** (FSC1 a FSC12) e as **verificações pré-ajuizamento** (VF1 a VF9), descritas em `assets/escrutinio-fsc-vf.md`. O script de cálculo grava a checagem em `calculo.json` e em `checagem-fsc-vf.md`; complete com o quadro de fatos o que o script não vê. **FSC ATIVADO que a peça não trata, ou PENDENTE_ADVOGADO sem resposta, deixa o portão 3 pendente.** Perguntas-chave:
   - **FSC3 (ônus):** a inicial abre pelo art. 14, § 3º, do CDC, pelo art. 429, II, do CPC e pelo Tema 1061/STJ, e não depende só do art. 6º, VIII?
   - **FSC7 (não impugnação específica) e FSC1/FSC2 (assinatura e autenticação):** a autoria é negada de forma específica, contrato a contrato? A inicial controverte a autenticidade da assinatura ou da trilha, sem afirmar o que só o contrato do banco pode mostrar?
   - **FSC4 e FSC5/FSC11 (proveito econômico e cessão):** o valor liberado do extrato foi tratado? Portabilidade pura e contratos do mesmo dia foram identificados? Há cadeia de cessão a questionar (arts. 286 a 290 do CC)?
   - **FSC4 e Súmula 42/TJBA (VF6):** o extrato bancário do mês da averbação foi pedido ao cliente? Se o crédito chegou à conta, a peça não nega o recebimento: a decisão do advogado é devolução, depósito ou compensação. Sem o extrato, registre a pendência.
   - **FSC6 (impugnação tardia):** a data da ciência dos descontos está no quadro? A declaração de inexistência (não prescreve) e a repetição e o dano (prescrevem) estão separadas? Prazo e termo inicial são decisão do advogado.
   - **FSC8 (dano moral como "mero dissabor"):** natureza alimentar do benefício, valor e tempo dos descontos, e tentativa administrativa prévia ao banco (fato, sem apoio no Tema 929)?
   - **FSC9/FSC10 (prova técnica e correspondente):** Justiça Comum: exibição e perícia com quesitos pedidos já na inicial. JEC: apenas inversão do ônus e encargo de juntar documentos com a contestação, sem exibição, perícia ou ofício. Na inicial, peça que o banco identifique o correspondente e junte a trilha completa com a contestação, e registre a residência do cliente (ID e página) para a geolocalização da réplica.
   - **FSC12 (litigância predatória):** comprovante de residência atual e legível, documento de identidade, procuração atualizada, uma ação por benefício + banco + tese, sem fracionamento. Nada na peça sobre quantas ações o autor ou o escritório têm, nem sobre a colheita da procuração.
4. **Revisão final.** Confira citações, valores, pedidos, competência, prazos e dados pessoais, com o checklist de `padrao-pecas.md`, seção 9. Se um portão falhar duas vezes, entregue apenas **diagnóstico ou minuta parcial** marcada `BLOQUEADO PARA USO FINAL`, com as pendências. Apenas o advogado responsável aprova e assina.

Registre no fim da resposta os quatro portões (passou, pendente ou bloqueado, com o motivo em uma linha).

## Proporcionalidade

A triagem entrega a ficha e as pendências, sem peça. As especialistas exigem prova específica e a checagem pré-recurso. O recurso exige diagnóstico dos fundamentos da sentença, viabilidade e exposição, e **pausa** antes de redigir. Não crie burocracia onde a dúvida é pontual.

## Formato de entrega

A peça sai em **Markdown**; a formatação em Word ou Google Docs fica com a skill `tipografia-azul`. Ofereça gerar o documento ao fim da peça. A `tipografia-azul` não prevê página amarela nem cabeçalho de rascunho: peça bloqueada ou com pendências leva no topo uma **Observação interna** (Título 6) com "BLOQUEADO PARA USO FINAL" e a lista do que falta, a remover antes de protocolar. Sem execução de código, entregue o Markdown e diga que a formatação ficou pendente.

**Marcas de pendência** (`[CONFERIR…]`, `[PREENCHER…]`, `[VERIFICAR ANTES DE PROTOCOLAR]`, `CÁLCULO A CONFERIR`) precisam saltar aos olhos. No chat, em negrito. No Word, saem com **realce amarelo** (decisão do escritório de 28/10/2026), aplicado ao texto da marca como realce de caractere, nunca como página amarela. A `tipografia-azul` ainda não descreve esse realce: ao formatar, a instrução deve vir junto. Nunca omita, resuma ou mova uma marca: ela fica no ponto exato da pendência. Peça com marca não está pronta para protocolo.

Na resposta ao advogado: Painel do Caso, conclusão no alcance possível, fundamento com norma e artigo, cálculo quando aplicável, riscos e até três próximas diligências. Não exponha nomes internos de etapas ou arquivos, salvo para indicar uma ação.

Toda peça é **minuta de trabalho**: o advogado revisa e assina.
