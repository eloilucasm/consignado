# Redação proposta para R4 a R7: textos para o escritório aprovar

Data: 01/11/2026. Continua a `NOTA-revisao-encadeamento-2026-10-29.md`. **Nenhum modelo foi alterado.** Para cada ponto: o trecho atual, o texto proposto (pronto para colar) e o que mais muda se for aprovado. As linhas citadas são as de 01/11/2026.

| # | Skill | O que muda | Pronto para aplicar? |
|---|---|---|---|
| R4 | migrado | "nulidade da migração" passa a "ineficácia da cessão perante a parte autora" | sim, depois do aceite |
| R5 | rmc | refinanciamento anterior a 01/2024 ganha pedido próprio (limitação e dobro do excesso) | depende de decisão sobre o art. 2º-D (ver o risco) |
| R6 | rmc | tópico do Tema 1414 transcreve as três questões e distingue pelo teto legal | sim, depois do aceite |
| R7 | todas | dobra com o EAREsp 676.608/RS para descontos posteriores a 30/03/2021 | **aprovado e aplicado em 01/11/2026** |

---

## R4. Migrado: ineficácia da cessão no lugar de "nulidade da migração"

O art. 290 do CC diz que a cessão "não tem eficácia em relação ao devedor, senão quando a este notificada". O pedido passa a seguir a consequência que a própria tese escolhe.

**1. Ementa** (`migrado/assets/modelo-inicial-migrado.md:22`)
- Atual: "… Inexistência de autorização para a migração. Nulidade da migração. …"
- Proposto: "… Inexistência de autorização para a migração. Ineficácia da cessão perante o devedor. …"

**2. Nome da ação** (mesmo arquivo, `:26`)
- Atual: "Ação Declaratória de Inexistência de Relação Jurídica e Nulidade de Migração de Contrato, Cumulada com …"
- Proposto: "Ação Declaratória de Inexistência de Relação Jurídica e de Ineficácia de Cessão de Crédito, Cumulada com Repetição do Indébito em Dobro, Obrigação de Fazer e Indenização por Danos Extrapatrimoniais[[SE TUTELA]], com Pedido de Tutela Provisória de Urgência[[FIM]]"

**3. Efeitos** (mesmo arquivo, `:181`)
- Atual: "Declarada a inexistência e a nulidade, as partes voltam ao estado anterior (art. 182 do CC)."
- Proposto: "Declaradas a inexistência da relação jurídica com o réu e a ineficácia da cessão perante a parte autora, nada lhe pode ser cobrado com base nela, e o que foi descontado deve ser restituído."
- Motivo: o art. 182 do CC trata de negócio **anulado**. Com a ineficácia, a restituição decorre da cobrança sem causa perante a autora. Fica dispensado o apoio no art. 182.

**4. Pedido 1** (mesmo arquivo, `:322`)
- Atual: "1. seja declarada a inexistência da relação jurídica entre as partes quanto ao(s) contrato(s) nº [CONTRATOS] e a nulidade da sua migração e averbação, com a inexigibilidade de todo e qualquer débito decorrente;"
- Proposto: "1. seja declarada a inexistência de relação jurídica entre a parte autora e o réu quanto ao(s) contrato(s) nº [CONTRATOS] e a ineficácia, perante a parte autora, da cessão que fundamentou a sua migração (art. 290 do CC), com a consequente invalidade da averbação no benefício e a inexigibilidade de todo e qualquer débito decorrente;"

**5. Arquivos de apoio**
- `_acervo/pecas/padrao-pecas.md:31`: trocar o exemplo do nome da ação pelo nome proposto acima.
- `_acervo/pecas/padrao-pecas.md:56`:
  - atual: "(migrado: nulidade da migração e da averbação)";
  - proposto: "(migrado: inexistência da relação com o réu e ineficácia da cessão perante a parte autora, art. 290 do CC)".
- `migrado/SKILL.md:8`:
  - atual: "inexistência de relação jurídica e nulidade da migração";
  - proposto: "inexistência de relação jurídica e ineficácia da cessão perante a parte autora".
- `migrado/references/01-tese-e-roteiro.md:5`:
  - atual: "inexistência da relação jurídica (subsidiariamente, nulidade) e **nulidade da migração**";
  - proposto: "inexistência da relação jurídica com o réu e **ineficácia da cessão** perante a parte autora (art. 290 do CC)".

**O que mais muda:** sincronizar o `padrao-pecas.md` e refazer a peça de exemplo `migrado/testes/caso-ficticio/saida/inicial-migrado.md`, que tem o nome da ação e o pedido 1. O verificador não tem regra sobre esse trecho e não precisa mudar.

---

## R5. RMC com refinanciamento anterior a 01/2024: pedido próprio

**Risco que a nota de 29/10 não mostrava.** O art. 2º-D da Res. CMN 4.549, no acervo (`res-cmn-4549-consolidada.md:62`), diz que os arts. 2º-A a 2º-C "se aplica[m] somente às operações realizadas após o prazo de 90 (noventa) dias de que trata o § 1º do art. 28 da Lei nº 14.690, de 2023, independentemente da data de assinatura do contrato de cartão". Para o refinanciamento anterior a 01/2024, então, a resolução **não** dá o teto, nem para os encargos posteriores.
- O pedido de limitação só se sustenta no art. 28, § 1º, da própria Lei 14.690/2023, lido com o trato sucessivo. É exatamente o argumento que hoje está marcado `[VERIFICAR]`.
- A opção (a) da nota de 29/10 continua melhor do que pedir a nulidade, porque a nulidade de um ato anterior ao teto é ainda mais frágil. Mas não elimina o risco.
- **Decisão pedida:** confirmar a opção (a) sabendo desse limite, ou não ajuizar o RMC com refinanciamento anterior a 01/2024 até haver precedente.

**1. Tópico novo, só para o refinanciamento anterior** (inserir em `rmc/assets/modelo-inicial-rmc.md` antes de `:159`. O tópico atual "O refinanciamento é nulo por fraude à lei imperativa" passa a ficar dentro de `[[SE REFINANCIAMENTO ≥ 01/2024]] … [[FIM]]`.)

> [[SE REFINANCIAMENTO < 01/2024]]
> ## Os juros e encargos cobrados depois de 01/01/2024 estão limitados ao teto legal
>
> O refinanciamento de [COMPETÊNCIA DO REFINANCIAMENTO] é anterior ao fim do prazo de 90 dias do art. 28, § 1º, da Lei 14.690/2023. A parte autora não pede, por isso, que ele seja declarado nulo desde a origem. O contrato de cartão é de trato sucessivo: a cada mês o banco lança novos juros e encargos sobre o saldo. Os lançamentos feitos a partir de 01/2024 são atos posteriores à lei e devem respeitar o limite do art. 28, § 1º. Como os pagamentos da parte autora já somavam [PCT ATÉ O REFINANCIAMENTO] do capital em [COMPETÊNCIA DO MARCO], todo encargo cobrado desde 01/2024 excede o teto e deve ser restituído em dobro. [VERIFICAR ANTES DE PROTOCOLAR: o art. 2º-D da Res. CMN 4.549 restringe a resolução às operações posteriores ao prazo; o argumento se apoia só na lei, sem precedente no acervo.]
> [[FIM]]

**2. Pedidos para esse caso** (em `:316` e no pedido de restituição)
- Pedido 1:
  - [[SE REFINANCIAMENTO < 01/2024]] "1. sejam limitados ao teto do art. 28, § 1º, da Lei 14.690/2023 os juros e encargos cobrados sobre o cartão nº [NÚMERO DO CARTÃO] a partir de 01/2024, com a declaração de inexigibilidade do que o exceder; subsidiariamente, seja declarada a nulidade do refinanciamento de [COMPETÊNCIA DO REFINANCIAMENTO] (art. 166, VI, do CC);"
  - [[SE REFINANCIAMENTO ≥ 01/2024]] mantém o texto atual.
- Restituição:
  - [[SE REFINANCIAMENTO < 01/2024]] "o réu seja condenado a restituir em dobro os valores descontados desde 01/2024, no total atual de [DOBRO PÓS-TETO POR EXTENSO], …"
  - Correção e juros como hoje (Súmula 33/TJBA).

**3. Script** (`rmc/scripts/cartao.py:140-162`, `calcular()`)
- Hoje ele separa só antes e depois do refinanciamento (`total_ate_refin`, `total_pos_refin`).
- Para este ramo, precisa somar também os descontos a partir de `max(refinanciamento, 01/2024)`: `total_pos_teto`, `dobro_pos_teto` e o valor da causa correspondente, com segunda via, como os demais totais.
- `calcular_rmc.py` grava os campos novos, e o verificador passa a exigi-los na peça desse ramo.
- O teste do caso fictício já tem a variante "antigo" (refinanciamento em 11/2022), que serve de regressão.

---

## R6. RMC: distinção do Tema 1414 com as três questões transcritas

**Atual** (`rmc/assets/modelo-inicial-rmc.md:250-252`): descreve o tema como suspensão "dos processos que discutem a nulidade de contratos de cartão consignado por vício de informação". A página do STJ é mais ampla. O banco transcreve a questão II.b e a distinção perde força.

**Proposto** (substitui `:250` e `:252`; transcrição conferida com `tema-1414-stj.md:28-32`, lido no STJ em 28/10/2026):

> O Tema 1.414/STJ (Segunda Seção, Rel. Min. Raul Araújo) está afetado e sem tese, conforme a página do STJ lida em [DATA DA CONSULTA no arquivo tema-1414-stj.md]; a skill relê a situação na data da minuta. As questões submetidas a julgamento são:
>
> > I - Definir se os alegados vícios que atingem os contratos de cartão de crédito com reserva de margem consignável (RMC) sujeitam a pretensão do autor: a) ao prazo decadencial do art. 178 do Código Civil, com fixação do termo inicial de contagem desse prazo; ou b) não se sujeitam a prazos extintivos em razão de nulidade, conforme o art. 169 do CC.
> >
> > II - Definir parâmetros objetivos para a aferição da validade e eventual caráter abusivo dos contratos de cartão de crédito consignado, considerando: a) o dever de prestar informações suficientes, claras e adequadas ao consumidor, em especial quando este alega que pretendia contratar simples empréstimo consignado; e b) o prolongamento indeterminado da dívida, ante a aparente insuficiência dos descontos mensais para amortizá-la, frente aos juros rotativos aplicados no refinanciamento do saldo.
> >
> > III - Em caso de vício no contrato, aferir se a consequência a ser adotada deverá ser: a) a restituição das partes ao estado anterior; b) a conversão do contrato em empréstimo consignado; ou c) a revisão de cláusulas contratuais; e d) se haverá configuração de dano moral in re ipsa.
>
> O tema vai fixar **parâmetros** para julgar a validade e a abusividade do contrato, a partir do dever de informação e do prolongamento da dívida. Esta ação não depende desses parâmetros. Não alega vício no contrato do cartão contratado em [DATA DE INCLUSÃO DO CARTÃO], que não é impugnado. Pede a aplicação de um **limite legal objetivo**, o teto do art. 28, § 1º, da Lei 14.690/2023: uma conta entre o capital e o que já foi pago, que não passa por exame de informação, de abusividade nem de vício de consentimento. A lei é posterior aos contratos que o tema examina e não está entre as questões afetadas. Demonstrada a distinção, a parte autora requer o prosseguimento do processo (art. 1.037, § 9º, do CPC). [VERIFICAR ANTES DE PROTOCOLAR: proximidade com a questão II.b; não há, no acervo, decisão que tenha aceitado essa distinção.]

**O que mais muda:**
- `replica-consignado/references/02-defesas-do-banco.md`, linha P9: trocar "(decisão D25 do escritório; redação em revisão, D37)" por remissão a este tópico.
- O verificador passa a conferir a transcrição contra o arquivo do Tema 1414, pela regra nova de transcrição literal.

---

## R7. Dobra com o EAREsp 676.608/RS

**Situação: APROVADO pelo escritório e APLICADO em 01/11/2026.** O texto proposto abaixo entrou no tópico da repetição em dobro dos quatro modelos de inicial (não contratado, migrado, Tese 1000 e RMC), com o acórdão na lista de precedentes. Também foram atualizados:
- o protocolo ("Regras de citação e de pedido vigentes") e o padrão de peças;
- os roteiros das três skills de contrato;
- a resposta M8 do catálogo de defesas da réplica;
- as referências do recurso;
- os alertas dos três scripts de cálculo, que agora mandam usar o bloco `[[SE HÁ DESCONTO ANTES DE 30/03/2021]]`;
- a ficha do acervo, que passou de "NÃO CITAR" a "citar";
- uma regra nova no teste do verificador, que reprova a tese adulterada.

A segunda tese (prescrição decenal) **não** foi aplicada: o tópico de prescrição segue só com o EAREsp 738.991/RS até nova decisão.

**Acórdão conferido em 01/11/2026.** O escritório trouxe o inteiro teor certificado (documento 1498374, DJe 30/03/2021). Ficha no acervo: `_acervo/jurisprudencia/earesp-676608-stj.md`, com a tese e a modulação transcritas.

| Dado | No acórdão |
|---|---|
| Órgão e relator | Corte Especial, **Rel. Min. Og Fernandes** (a divergência de 29/10 está resolvida: a nota do NUGEPNAC sobre "relator para acórdão Herman Benjamin" é do grupo de cinco processos; aqui o acórdão adotou os moldes do voto de Herman Benjamin, mas a relatoria é de Og Fernandes) |
| Julgamento e publicação | 21/10/2020; DJe 30/03/2021 |
| Resultado | por maioria; vencidas as Ministras Nancy Andrighi e Maria Thereza de Assis Moura (outro fundamento, sem modulação); vencido em parte o Ministro Raul Araújo (prescrição) |
| Primeira tese | a dobra "independe da natureza do elemento volitivo do fornecedor" e cabe quando a cobrança "consubstanciar conduta contrária à boa-fé objetiva" |
| Modulação | só a primeira tese; só cobranças em contratos de consumo que não envolvam serviço público, "quando pagas após a data da publicação do acórdão" |
| Segunda tese | prazo **decenal** (art. 205 do CC) para a repetição de cobrança de serviço **não contratado** (telefonia) |

**Texto proposto, pronto para colar** (tópico da repetição em dobro, depois do art. 42):

> A restituição em dobro não depende de prova de má-fé. A Corte Especial do Superior Tribunal de Justiça fixou que ela "independe da natureza do elemento volitivo do fornecedor que realizou a cobrança indevida, revelando-se cabível quando a referida cobrança consubstanciar conduta contrária à boa-fé objetiva" (EAREsp 676.608/RS, Rel. Min. Og Fernandes, j. 21/10/2020, DJe 30/03/2021). Promover descontos em benefício previdenciário sem autorização do titular é conduta contrária à boa-fé objetiva.[[SE HÁ DESCONTO ANTES DE 30/03/2021]] Quanto aos descontos anteriores a 30/03/2021, a dobra decorre do próprio art. 42, parágrafo único, do CDC, que só a afasta no engano justificável, não demonstrado pelo réu.[[FIM]]

**Decisão que continua com o escritório:** citar o acórdão traz a modulação para dentro da peça. O banco a invocará de qualquer forma, então a peça responde antes. O acórdão diz expressamente que os pagamentos anteriores a 30/03/2021 **não** são alcançados pelo novo entendimento. Para eles, a tese do escritório fica só no texto do art. 42, sem precedente favorável. A regra atual (dobra de todos os descontos, sem citar o marco) continua possível; a diferença é que, com o acórdão, os descontos posteriores ganham fundamento forte.

**Achado extra (segunda tese):** reforça o prazo decenal para repetição de cobrança de serviço não contratado, hoje sustentado só pelo EAREsp 738.991/RS (réplica, defesa P4; FSC6). Pode entrar no tópico de prescrição das iniciais, por analogia, se o escritório aprovar.

**Se aprovado, muda também:** a linha "Repetição em dobro" das regras vigentes do protocolo; os roteiros das quatro skills; o alerta dos scripts (`calcular.py:146`, `calcular_migrado.py:190`, `calcular_1000.py:212`) passa a separar os descontos antes e depois de 30/03/2021; e a ficha do acervo deixa de ter "NÃO CITAR".

### Registro anterior (antes do PDF)

**O que se tentou em 01/11/2026:**
- **Portal de pesquisa do STJ (scon):** abre um desafio anti-robô. A ferramenta não resolve esse tipo de desafio, e o acórdão não foi lido.
- **Link oficial do inteiro teor** devolvido pela busca: "página não encontrada". O endereço é <https://www.stj.jus.br/websecstj/cgi/revista/REJ.cgi/ATC?seq=119444796&tipo=2&nreg=201500497769&dt=20210330&formato=PDF&salvar=false>.
- **O advogado pode abrir no navegador, passando pelo desafio:**
  - <https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?num_registro=201500497769&dt_publicacao=30%2F03%2F2021> (EAREsp 676.608/RS);
  - <https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?num_registro=201303558269&dt_publicacao=30%2F03%2F2021> (EREsp 1.413.542/RS, julgado na mesma sessão).

**O que as fontes dizem, sem confirmação no acórdão:**

| Dado | Fonte | Situação |
|---|---|---|
| Rel. Min. Og Fernandes, Corte Especial, j. 21/10/2020, DJe 30/03/2021 | resumo de busca na web, que cita acórdão posterior do STJ | não confirmado |
| "Relator para acórdão Ministro Herman Benjamin, publicado no DJe de 30/03/2021" | `_acervo/jurisprudencia/stj/temas/tema-929.md:45` | provavelmente se refere a outro processo do mesmo grupo (o EAREsp 600.663/RS); conferir |
| Tese: "A repetição em dobro, prevista no parágrafo único do art. 42 do CDC, é cabível quando a cobrança indevida consubstanciar conduta contrária à boa-fé objetiva, ou seja, deve ocorrer independentemente da natureza do elemento volitivo"; modulação para cobranças posteriores a 30/03/2021 | ementa do TRF-4, item 5 (`ac-5003696-trf4.md`, lida no portal do TRF-4), que atribui a tese ao **EAREsp 600.663/RS** | confirmado que o TRF-4 escreveu isso; não confirmado no acórdão do STJ |

A divergência de relator registrada em 29/10 continua aberta. Há uma explicação provável: a Corte Especial julgou vários embargos juntos em 21/10/2020, cada um com seu relator.

**Texto proposto, só se o escritório conferir o acórdão** (para descontos posteriores a 30/03/2021; para os anteriores, só o art. 42):

> A restituição em dobro independe da prova de má-fé: basta que a cobrança indevida contrarie a boa-fé objetiva (EAREsp [NÚMERO CONFERIDO]/RS, Corte Especial, Rel. [RELATOR CONFERIDO], j. 21/10/2020, DJe 30/03/2021). Promover descontos em benefício previdenciário sem autorização do titular é conduta contrária à boa-fé objetiva.

**O que mais muda, se aprovado:**
- novo arquivo no acervo com a ementa lida;
- tirar a proibição do marco de 30/03/2021 em `_acervo/protocolo/protocolo.md` ("Regras de citação e de pedido vigentes", linha "Repetição em dobro") e nos roteiros das quatro skills;
- trocar o alerta dos scripts (`calcular.py:146`, `calcular_migrado.py:190`, `calcular_1000.py:212`), que hoje manda não usar o marco.

**Ponto de atenção para qualquer decisão:** o item 5 da ementa do TRF-4 que os modelos já transcrevem (itens 1, 3 e 4) aplica a modulação de 30/03/2021. O banco pode usar o mesmo acórdão para limitar a dobra. Os modelos não transcrevem o item 5, e isso deve continuar assim.
