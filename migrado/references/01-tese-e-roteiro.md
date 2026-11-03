# A tese do migrado e o roteiro de redação

## Quando esta skill se aplica

Contrato de empréstimo consignado cujo extrato do INSS registra, no campo "Origem da Averbação", **"Migrado do contrato [número] CBC: [código do banco]"**, e que o beneficiário **nega ter firmado**. É o bloco A da análise. A tese é de **inexistência** da relação jurídica (subsidiariamente, nulidade) e **nulidade da migração**, com repetição do indébito em dobro, obrigação de fazer e dano extrapatrimonial.

Não é desta skill: contrato não contratado sem migração (`nao-contratado`), derivado com sufixo sobre raiz excluída (`tese-1000`), refinanciamento de cartão RMC/RCC (`rmc`) e recurso.

## Onde a tese realmente se apoia

O modelo do escritório (Francisco x Agibank) dizia que a migração é "figura que nenhuma das normas de regência autoriza sem novo consentimento expresso do titular". **O texto das normas diz o contrário do que essa frase afirma:**

- IN 138/2022, art. 4º, XVI: troca de titularidade é a "migração da carteira (ou parte dela) de operações de crédito de instituição credora original para instituição proponente".
- IN 138/2022, art. 11: "A cessão de créditos entre instituições financeiras poderá ser realizada, desde que atenda às normas editadas pelo BCB e pelo CMN."
- IN 28/2008, art. 56 (até 12/12/2022): regra equivalente, com remissão à Res. CMN 2.836/2001 (`normas/res-cmn-2836-consolidada.md`, no acervo desde 30/10/2026).

A migração, portanto, é **permitida**, desde que atenda às normas do BCB e do CMN. Se a petição disser o contrário, o banco cita o art. 11 e a peça perde credibilidade. A tese correta tem três passos, todos no modelo (decisão do escritório de 29/10/2026: **não** sustentar a inexistência do crédito cedido, porque o argumento é perigoso; trabalhar só a hipótese de a cessão não ter sido notificada ao devedor):

1. **A cessão não vale contra o devedor sem notificação** (CC, art. 290). O extrato não mostra notificação nem ciência. `[VERIFICAR]` a aplicação do art. 290 à troca de titularidade da carteira de consignado.
2. **Se o banco alegar nova contratação**, ela exigiria instrumento e autorização assinados (IN 28, art. 5º; IN 138, art. 5º, II e III). A origem "Migrado" mostra que o banco não se apresenta como autor de nova contratação.
3. **Inexistência por falta de consentimento** (CC, art. 104), com o ônus da prova no banco (CDC, art. 14, § 3º; CPC, art. 429, II; Tema 1061/STJ).

**Pendente:** o escritório informou que há uma petição de migrado mais robusta, que deve orientar esta skill. Ela ainda não foi incorporada (arquivo não localizado na pasta do projeto em 29/10/2026).

## A norma depende da data da averbação

| Averbação | Norma | Dispositivos que a peça usa |
|---|---|---|
| até 12/12/2022 | IN 28/2008 | art. 5º (assinatura antes do envio do arquivo), art. 6º (responsabilidade), art. 56 (cessão) |
| a partir de 13/12/2022 | IN 138/2022 | art. 4º, XVI e XXVII; art. 5º, II e III; art. 11 |

**Vigência da IN 138 (D30, decidida em 29/10/2026).** O escritório conferiu no DOU: publicação em **13/12/2022** (DOU nº 233, republicação; a edição original, DOU nº 214 de 11/11/2022, saiu com incorreções). Pelo art. 40 ("entra em vigor no ato da publicação"), a IN 138 vige desde **13/12/2022**; a IN 28 vale até 12/12/2022.

## O que a peça NÃO pode afirmar

1. **"Nenhuma norma autoriza a migração sem novo consentimento"**: ver acima.
2. **Contexto de "ilícito de massa" com a Operação Sem Desconto**: a operação (CGU e PF, 23/04/2025) apurou descontos de mensalidades de entidades associativas nos benefícios do INSS, e não empréstimos consignados. Usá-la como "fato notório" do esquema de consignados é impreciso, e o número de R$ 6,3 bilhões e os "97%" não dizem respeito a consignado. A afirmação de que a DATAPREV suspendeu a averbação de novos consignados em 2025 e o Acórdão TCU 1.094/2026 também não foram confirmados em fonte.
3. **Res. CMN 4.753/2019** como base da "fidedignidade dos registros": a norma trata de conta de depósitos (D2).
4. **Doutrina sem fonte** (nomes de autores de teoria do negócio jurídico, da carga dinâmica da prova e do desestímulo): não está no acervo. Os conceitos podem ser usados sem a atribuição.
5. **Dano *in re ipsa***: questão em aberto no Tema 1414/STJ; a peça usa a Súmula 40/TJBA.
6. **R$ 40.000,00 de dano moral e multa diária de R$ 1.621,00**: o escritório adota R$ 20.000,00 e R$ 500,00.
7. **EAREsp 676.608/RS**: citado para a dobra dos descontos posteriores a 30/03/2021 (decisão R7, 01/11/2026); os anteriores, pelo art. 42, parágrafo único, do CDC. O Tema 929/STJ não é usado.
8. **Tutela da evidência pelo art. 311, II, com o Tema 1061**: o Tema 1061 trata do ônus da autenticidade da assinatura de contrato juntado pelo banco, e aqui não há contrato juntado. A skill usa só o art. 311, IV.

## Gatilhos dos tópicos condicionais

| Tópico | Gatilho | Fonte do dado |
|---|---|---|
| Tutela de urgência | algum contrato **ativo** (só sobre os ativos) | `calculo.json`, campo `ativos` |
| Bloco da IN 28 ou da IN 138 | data da averbação | `calculo.json`, `regime_norma` |
| Troca de titularidade (mesmo número em outro banco) | `troca_de_titularidade` | `calculo.json` |
| Prescrição | algum desconto com mais de 5 anos | `calculo.json`, `prescricao_5_anos` |
| Litispendência | `litispendencia` preenchido na ficha | ficha |
| Tramitação prioritária | autor com 60 anos ou mais | qualificação (nascimento) |
| Exibição e perícia com quesitos | rito = Justiça Comum | pergunta ao advogado |
| Honorários sobre condenação mais proveito | rito = Justiça Comum | pergunta ao advogado |
| Proveito econômico declaratório no valor da causa | Justiça Comum e contrato ativo | `calculo.json`, `proveito_declaratorio`; decisão do advogado |
| LGPD | decisão do advogado | pergunta ao advogado |
| Interesse na conciliação | resposta do advogado (Justiça Comum) | pergunta ao advogado |
| Endereçamento federal | réu = Caixa (código 104) | `reus.json` |

## Anomalias que exigem pausa

- Contrato **sem origem de migração** no extrato: o script alerta; pode ser não contratado comum (`nao-contratado`).
- O número da origem difere do número do contrato: descreva os dois.
- **Mesmo número em outro banco**: o script não soma os descontos do banco anterior e alerta; o advogado decide a legitimidade do réu e a soma (`--incluir-outros-bancos`). A primeira averbação, em qualquer banco, define a norma aplicável.
- Contratos de regimes diferentes (IN 28 e IN 138) no mesmo processo: o modelo traz os dois blocos; revise.
- Descontos anteriores a 30/03/2021: pedir o dobro de todos, com o bloco `[[SE HÁ DESCONTO ANTES DE 30/03/2021]]` (dobra pelo art. 42). Sem Tema 929.
- Valor liberado ausente ou R$ 0,00: examinar FSC4; não afirme que não houve crédito sem prova.
- Réu fora de `reus.json`: não preencha CNPJ nem endereço de memória.

## Campos do quadro de fatos específicos desta tese

Além dos campos comuns (`protocolo/quadro-de-fatos.md`), registre, para cada contrato e com ID e página do extrato: número do contrato; **origem da averbação** (texto literal do campo) e o **código do banco de origem**; data da averbação; parcela, prazo, início e fim dos descontos; valor liberado; exclusão e motivo, se houver; o mesmo número no banco anterior, com datas, situação e motivo da baixa; data e meio da ciência; reclamação prévia; e se o cliente alguma vez teve relação com o banco de origem. Estado de cada campo: confirmado (extrato), relatado (cliente), inferido ou desconhecido.

## Perguntas típicas (máximo três por rodada)

1. Rito: JEC ou Justiça Comum? (sempre)
2. Cidade e UF do fecho? (sempre)
3. Interesse ou desinteresse na audiência de conciliação? (Justiça Comum)
4. O cliente já teve algum contrato com o banco de origem? (muda a tese: se teve, a inexistência pode não valer)
5. O cliente recebeu algum crédito em conta nas datas dos contratos? Há extrato bancário?

## Mapa da checagem pré-recurso (FSC) para o modelo

| Fundamento de sentença | Onde a inicial se previne |
|---|---|
| FSC3, ônus da prova | tópico da inversão do ônus e a tabela de documentos |
| FSC5, FSC11, cessão e mesma data | tópico "A norma do INSS admite a migração de carteira, mas a cessão não vale contra o devedor que não foi notificado" (arts. 286 e 290 do CC) |
| FSC7, FSC1, FSC2, autoria | subtópico "nega a contratação de origem e a migração" |
| FSC4, proveito econômico | mesmo subtópico (valor liberado do extrato) e tabela de documentos |
| FSC6, impugnação tardia | fatos (data da ciência) e tópico de prescrição |
| FSC8, mero dissabor | subtópico do dano extrapatrimonial (Súmula 40 do TJBA) |
| FSC9, FSC10, prova técnica | inversão (JEC) ou exibição e perícia com quesitos (Justiça Comum) |
| FSC12, litigância predatória | documentos legíveis e atuais; um processo por benefício + banco + tese; nada sobre outras ações |
