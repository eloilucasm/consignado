# A tese do RMC/RCC e o roteiro de redação

## Quando esta skill se aplica

Cartão de crédito consignado (RMC: reserva de margem consignável; RCC: cartão consignado de benefício) averbado no benefício do INSS, cujo **saldo foi refinanciado pelo banco** depois de o beneficiário já ter pago, em descontos mensais, **mais de 200% do capital**. A tese é de **nulidade do refinanciamento**, com declaração de quitação, repetição em dobro do que foi descontado desde o refinanciamento, obrigação de liberar a margem e dano extrapatrimonial.

Não é desta skill: empréstimo consignado não contratado, contrato migrado, Tese 1000 (cada um tem a sua) e recurso.

## Como a tese é montada (tudo do extrato)

1. **Capital** = limite do cartão registrado no INSS. É uma **premissa**, não um fato: o limite não é o valor efetivamente sacado. A peça diz isso e pede as faturas.
2. **Refinanciamento** = competência em que o campo "utilizado no mês" salta para quase todo o saldo devedor (pelo menos 90% do saldo e 5 vezes o desconto mensal), com IOF lançado.
3. **Planilha** = descontos mensais acumulados e percentual do capital. Competência ausente no extrato fica ausente, **nunca é interpolada**; o total é piso.
4. **Marco de 200%** = primeira competência em que o acumulado chega a 200% do capital.
5. **Valor da causa** = saldo refinanciado (CPC, art. 292, II) + dobro do que foi descontado desde o refinanciamento + R$ 20.000,00.

O argumento da queda de taxa de juros só entra quando a taxa do mês do refinanciamento é menor que a de **todos** os meses vizinhos.

## Pontos jurídicos da tese (decididos pelo escritório em 29/10/2026)

A tese do AMN cita o art. 28, § 1º, da Lei 14.690/2023 e o art. 2º-C da Res. CMN 4.549 (incluído pela Res. 5.112). A leitura dos textos do acervo mostra quatro pontos que o banco levantará. Nenhum bloqueia a minuta: o escritório decidiu e a peça responde a todos.

### B1. O art. 4º da Res. CMN 4.549 e o cartão consignado (D1, decidida)

> Art. 4º O disposto nesta Resolução não se aplica aos cartões de crédito e aos demais instrumentos de pagamento pós-pagos cujos contratos prevejam pagamento das faturas mediante consignação em folha de pagamento.

**Decisão do escritório:** o art. 4º **não** afasta a resolução do RMC, porque no RMC apenas o **valor mínimo** da fatura é consignado em folha; o restante é pago pelo consumidor, por boleto. O dispositivo trata de contratos que preveem o pagamento **das faturas** por consignação. Logo, a Res. CMN 4.549, com os arts. 2º-A a 2º-D, aplica-se ao cartão, e a tese se funda **na Lei (art. 28, § 1º) e na resolução**. A premissa de fato (só o mínimo é consignado) deve ser conferida nas faturas: o script alerta. Sem precedente no acervo: o texto do modelo leva `[VERIFICAR ANTES DE PROTOCOLAR]`.

### B2. O prazo de 90 dias (art. 28, § 1º; art. 2º-D da Res. CMN 4.549) (D19, decidida)

O § 1º do art. 28 diz que o teto aplica-se "se os limites referidos no caput ... não forem aprovados no prazo máximo de 90 (noventa) dias, contado da data da publicação desta Lei". A lei foi publicada no DOU de 3.10.2023 (edição extra). O art. 2º-D da Res. 4.549 diz que os arts. 2º-A a 2º-C se aplicam **somente às operações realizadas após esse prazo**. Pela contagem simples, o prazo terminou em 1º/01/2024 `[VERIFICAR a contagem]`.

**Decisão do escritório:** manter a tese do teto também para refinanciamento anterior a janeiro de 2024; **não** se segue pela linha de nulidade por vício de informação. O modelo traz, para esse caso, o argumento do trato sucessivo (os encargos lançados depois do prazo se submetem ao teto), com `[VERIFICAR]`: é tese do escritório e o texto do art. 2º-D a contraria. O script apenas **avisa** (alerta B2). Na petição AMN de referência o refinanciamento é de outubro de 2023 e o marco de 200% de março de 2023, antes de a lei existir.

### B3. Os limites aprovados pelo CMN e a condição do § 1º

O banco pode dizer que o CMN aprovou limites dentro do prazo (a Res. 5.112 é de 21/12/2023) e que, por isso, o § 1º não se aplica. Com a decisão D1 (a resolução vale para o RMC), o modelo responde em alternativa: se os limites foram aprovados, vale o art. 2º-C, que adota o valor original da dívida; se não foram, incide o § 1º, de igual conteúdo. O teto é o mesmo nas duas leituras. `[VERIFICAR ANTES DE PROTOCOLAR]`.

### B4. Tema 1414/STJ e a suspensão nacional (D25, decidida)

O STJ afetou, em 06/03/2026, o Tema Repetitivo 1414 (Segunda Seção, relator Min. Raul Araújo; ampliado em 02/10/2026): validade e abusividade dos contratos de cartão de crédito consignado, incluindo o "prolongamento indeterminado da dívida, ante a aparente insuficiência dos descontos mensais para amortizá-la, frente aos juros rotativos aplicados no refinanciamento do saldo". Em 08/04/2026 a Segunda Seção referendou a suspensão de todos os processos pendentes sobre a mesma questão, em todo o país, exceto cumprimentos de sentença (`jurisprudencia/tema-1414-stj.md`).

**Decisão do escritório:** a tese do refinanciamento (teto legal) não se enquadra na suspensão, que alcança as ações de nulidade por vício de informação. **O pedido de prosseguimento por distinção entra sempre**, em tópico próprio (art. 1.037, § 9º, do CPC). Risco registrado: a questão II.b do tema (prolongamento da dívida frente aos juros do refinanciamento) tem proximidade com a tese; o juiz pode suspender. Não há julgado do TJBA nem do STJ no acervo sobre o prosseguimento de ação de refinanciamento de RMC. Reconferir o portal do STJ antes de protocolar, porque o tema pode ser julgado a qualquer momento.

## Gatilhos dos tópicos condicionais

| Tópico | Gatilho | Fonte do dado |
|---|---|---|
| Tutela de urgência | cartão **ativo** no extrato | `calculo.json`, campo `ativo` |
| Coisa julgada (distinguishing) | houve ação anterior sobre o cartão | pergunta ao advogado |
| Litispendência | `litispendencia` preenchido na ficha | ficha |
| Tramitação prioritária | autor com 60 anos ou mais | qualificação (nascimento) |
| Exibição e perícia contábil com quesitos | rito = Justiça Comum | pergunta ao advogado |
| Endereçamento federal | réu = Caixa (código 104) | `reus.json` |
| Queda da taxa de juros | taxa do mês do refinanciamento menor que a de todos os vizinhos | `calculo.json`, campo `juros_cai` |
| Histórico complementado | `--historico-extra` usado | `calculo.json`, campo `fontes_extra` |

Não há tópico de prescrição: a repetição pedida é só a posterior ao refinanciamento. Se o advogado pedir o dobro de descontos mais antigos, traga o tópico do modelo `nao-contratado`.

## Travas do script (ele não calcula além delas)

- **Histórico incompleto**: o extrato começa mais de 2 meses depois da inclusão do cartão. Peça o HISCRE ou as faturas, transcreva as competências em CSV (`MM/AAAA;valor;fonte`) e passe em `--historico-extra`. Nunca estime nem repita valores para completar meses. O documento vai anexado.
- **Sem refinanciamento detectado**: a tese não se aplica.
- **200% não atingido antes do refinanciamento**: o núcleo da tese não se sustenta; devolva ao advogado com os números.
- **Mais de um cartão** no processo: separe em processos distintos.

## Anomalias que exigem pausa

- Mais de um refinanciamento detectado: a peça trata o primeiro; avalie os demais.
- Saldo devedor descontínuo na troca de registro (código do benefício para número do cartão): confira se as linhas antigas são do mesmo cartão.
- Cartão excluído no mesmo dia da averbação de outro do mesmo banco: pode ser relevante, **não vai para a peça**; mostre ao advogado.
- Competências ausentes: a planilha é piso; diga isso na peça.
- Réu fora de `reus.json`: não preencha CNPJ nem endereço de memória.

## Perguntas típicas (máximo três por rodada)

1. Rito: JEC ou Justiça Comum? (sempre)
2. Cidade e UF do fecho? (sempre)
3. Houve ação anterior sobre esse cartão? Número e resultado? (sempre; define a coisa julgada)
4. No cartão, só o mínimo da fatura é descontado em folha e o restante é pago por boleto? (sempre; é a premissa de D1)
5. O cliente tem as faturas ou o HISCRE? (se o histórico estiver incompleto)
6. O cliente recebeu algum valor em conta na data do refinanciamento? (confirma a ausência de repasse)
7. O cliente reclamou ao banco? Há prova? (reforça a dobra)

## Mapa da checagem pré-recurso (FSC) para o modelo

| Fundamento de sentença | Onde a inicial se previne |
|---|---|
| FSC3, ônus da prova | tópico da inversão do ônus (art. 6º, VIII, do CDC) e tabela de documentos |
| FSC4, proveito econômico | fatos (ausência de repasse no refinanciamento) e tabela de documentos (comprovante do crédito) |
| FSC6, impugnação tardia | fatos (data da ciência) |
| FSC8, mero dissabor | subtópico do dano extrapatrimonial |
| FSC9, FSC10, prova técnica | inversão (JEC) ou exibição e perícia contábil com quesitos (Justiça Comum) |
| FSC12, litigância predatória | documentos legíveis e atuais; um processo por benefício + banco + tese; nada sobre outras ações |
| Coisa julgada | tópico condicional de distinguishing |
