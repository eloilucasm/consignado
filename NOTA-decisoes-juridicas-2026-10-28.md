# Nota: decisões jurídicas dos modelos de inicial (28/10/2026): três aplicadas e uma pendente (D25)

**Para:** advogados do escritório que revisam e assinam as iniciais de consignado.
**Sobre:** o que mudou nos modelos `nao-contratado` e `rmc`, por que mudou, o que a mudança não resolve e o que ainda depende de você.
**Base:** o texto integral das 55 súmulas da Turma de Uniformização das Turmas Recursais do TJBA (arquivo fornecido pelo escritório, até 10/11/2025) e dos enunciados cíveis do FONAJE (Portal do CNJ, consulta de 28/10/2026, enunciados 1 a 178). Estão em `references/jurisprudencia/` de cada skill.

Nenhuma das três decisões vem de pesquisa em acórdãos. Todas decorrem do texto de súmulas e enunciados que já estão no acervo. Isso muda o grau de segurança de cada uma, e a nota diz qual é.

---

## 1. Súmula 41 do TJBA: o banco vai invocá-la no RMC

### O que a súmula diz
> É lícita a contratação de cartão de crédito consignável, desde que observado o direito à informação do consumidor e afastado qualquer vício do seu consentimento na realização do negócio jurídico.

### O problema
As petições de RMC do AMN não mencionavam essa súmula. O banco, na contestação, vai dizer que o cartão consignado é lícito e que a parte autora o contratou. Uma inicial que não antecipa esse argumento deixa o juiz com a impressão de que a tese impugna o próprio cartão.

### O que foi aplicado
O modelo `rmc` ganhou o subtópico **"A licitude do cartão consignável não alcança o refinanciamento"**, logo depois da responsabilidade objetiva do banco. O texto faz três coisas:
1. reconhece a súmula;
2. diz que a ação **não** pede a invalidade do cartão, e sim a nulidade do refinanciamento, ato posterior e distinto;
3. usa a própria condição da súmula (direito à informação, art. 6º, III, do CDC) para pôr no banco o ônus de demonstrar que informou a parte autora do refinanciamento e de seus custos.

A súmula entrou também na lista de precedentes evocados.

### O que a mudança não resolve
- O subtópico afirma que o banco registrou o refinanciamento **sem proposta, sem nova assinatura e sem repasse de numerário**. O extrato do INSS mostra o lançamento, mas não prova a ausência de repasse. Por isso o trecho está marcado `[CONFIRMAR COM O CLIENTE]`. Se o cliente recebeu o dinheiro, o subtópico e a tese precisam mudar.
- Não há acórdão no acervo aplicando a Súmula 41 a refinanciamento. O argumento é lógico, a partir do texto da súmula.

### Em que o `nao-contratado` difere
A Súmula 41 não entra no `nao-contratado`: lá a tese é a inexistência do contrato, e a súmula trata de contrato lícito. Para o não contratado o risco análogo é a **Súmula 42 do TJBA** (negar a contratação é indício de litigância de má-fé se o banco provar o negócio e a disponibilização do numerário). Ela está no índice, marcada como risco.

---

## 2. Súmulas 32 e 33 do TJBA: termo inicial dos juros de mora

### O que dizem as súmulas
- **Súmula 32:** na responsabilidade **extracontratual**, os juros de mora contam do **evento danoso** (Súmula 54/STJ).
- **Súmula 33:** na responsabilidade **contratual**, os juros de mora contam da **citação**, ressalvada a anterior constituição em mora, nos termos do art. 397, parágrafo único, do Código Civil.

### O problema
O modelo `rmc` pedia juros "desde o evento danoso (Súmula 54 do STJ)" para a restituição em dobro e para o dano extrapatrimonial. Mas o cartão consignado é contrato: o refinanciamento é ato praticado dentro de uma relação contratual existente. Pela Súmula 33, a Turma Recursal contaria os juros da citação, e o pedido do modelo ficaria acima do que a turma concede.

### O que foi aplicado
No `rmc`, os pedidos g.4 (restituição em dobro) e g.5 (dano extrapatrimonial) passaram a dizer: "juros de mora desde a citação, ressalvada a constituição anterior em mora (Súmula 33 da Turma de Uniformização do TJBA; art. 397, parágrafo único, do CC)". A Súmula 54/STJ saiu do `rmc`.

### Por que o `nao-contratado` não mudou
No não contratado **não há contrato**: a cobrança decorre de averbação que a parte autora nega ter autorizado. A responsabilidade é extracontratual, e o evento danoso é a primeira cobrança. Por isso o modelo continua com a Súmula 54/STJ, e o índice registra a Súmula 32/TJBA como apoio disponível.

### O que a mudança não resolve
- Quem entende que o refinanciamento é ato ilícito autônomo (e não inadimplemento) pode sustentar o evento danoso. A escolha por **citação** é a conservadora. Se você preferir o outro termo inicial, é só voltar ao texto anterior; o índice continua com as duas súmulas.
- O modelo não traz precedente do STJ sobre o ponto. A Súmula 33 cita, no próprio texto, julgados do STJ (AgInt nos EDcl no REsp 2046807/SP; AgInt no AREsp 1313917/DF) que não foram baixados; confira-os antes de citar o fundamento além do texto da súmula.

---

## 3. Enunciado 162 do FONAJE: o art. 489 do CPC no Juizado

### O que o enunciado diz
> Não se aplica ao Sistema dos Juizados Especiais a regra do art. 489 do CPC/2015 diante da expressa previsão contida no art. 38, caput, da Lei 9.099/95.

O art. 38 da Lei 9.099/95 diz que a sentença "mencionará os elementos de convicção do Juiz, com breve resumo dos fatos relevantes ocorridos em audiência, dispensado o relatório". O Enunciado 161 acrescenta que o CPC/2015 só se aplica ao Juizado quando há remissão expressa ou compatibilidade com os critérios do art. 2º da Lei 9.099/95.

### O problema
O padrão de peças do escritório manda incluir, em toda petição judicial que cite precedente, o tópico **"Dos Precedentes Judiciais Evocados"**, com o pedido de apreciação expressa de cada precedente "nos termos do art. 489, § 1º, VI, do CPC". No JEC, o juiz pode responder que o art. 489 não se aplica ao rito.

### O que foi aplicado (decisão do escritório)
Numa primeira versão, o JEC recebeu um texto curto, sem o art. 489. O escritório decidiu manter o **texto completo também nos Juizados**, e foi isso que ficou:
- O tópico (modelos `nao-contratado` e `rmc`, e `padrao-pecas.md`) traz o texto completo da skill de benefícios por incapacidade do kit Cortex: o art. 489, § 1º, VI, o *distinguishing*, o *overruling* e o pedido de apreciação de cada precedente, com duas notas de rodapé de doutrina.
- No JEC, um parágrafo de **ponte** entra logo depois do primeiro: a sentença segue o art. 38 da Lei 9.099/95; o art. 489, § 1º, VI, é compatível com os critérios do art. 2º da mesma lei e é invocado como parâmetro para o enfrentamento dos precedentes. A ponte usa o próprio critério do Enunciado 161 (compatibilidade com o art. 2º) sem citá-lo.
- O pedido **f** é igual nos dois ritos: "apreciação expressa de cada precedente evocado, nos termos do art. 489, § 1º, VI, do CPC".
- **Não cite os Enunciados 161 e 162 na peça.** Eles servem à redação, não à tese.

### Riscos que permanecem
- O juiz do JEC pode aplicar o Enunciado 162 e dizer que o art. 489 não incide. A ponte reduz o risco, não o elimina. O pedido de apreciação continua sendo um pedido, sem a sanção de nulidade do art. 489 como eventual fundamento de recurso.
- **As duas obras da nota de rodapé não foram conferidas.** Vêm do kit Cortex (Donizetti, 2018; Fensterseifer, Revista de Processo v. 252, 2017) e estão com `[CONFERIR: fonte do kit Cortex, não conferida]`. Confirme autor, título e fonte antes de protocolar, ou retire as notas.

## 4. Tema 1414/STJ: a ação de RMC tende a ser suspensa (decisão D25, **pendente**)

Esta decisão ainda não foi tomada. Os itens 1 a 3 acima estão aplicados nos modelos; este não.

### O que o STJ decidiu
Na página de Precedentes Qualificados do STJ (lida em 28/10/2026), o Tema Repetitivo 1414 está **afetado, sem tese firmada** (Segunda Seção, relator Min. Raul Araújo; afetado em 06/03/2026 e ampliado em 02/10/2026). A questão submetida a julgamento tem três partes:
- **I.** se os vícios dos contratos de cartão com reserva de margem consignável (RMC) sujeitam a pretensão ao prazo decadencial do art. 178 do Código Civil ou não se sujeitam a prazo extintivo, por nulidade (art. 169 do CC);
- **II.** parâmetros de validade e abusividade, considerando (a) o dever de informar, em especial quando o consumidor alega que queria um empréstimo consignado simples, e (b) "o prolongamento indeterminado da dívida, ante a aparente insuficiência dos descontos mensais para amortizá-la, frente aos juros rotativos aplicados no refinanciamento do saldo";
- **III.** a consequência do vício (restituição ao estado anterior, conversão em empréstimo consignado ou revisão de cláusulas) e se há dano moral *in re ipsa*.

Em 08/04/2026, a Segunda Seção, por unanimidade, referendou a **suspensão do processamento de todos os processos pendentes, individuais ou coletivos, que versem sobre a mesma questão, em todo o país** (CPC, art. 1.037, II), **exceto os cumprimentos de sentença**. A página não proíbe o ajuizamento de ação nova.

### O problema para a skill `rmc`
A tese da skill é a **nulidade do refinanciamento** de RMC, e o refinanciamento do saldo com juros rotativos é a questão II.b do tema. A ação ajuizada hoje tende a ser suspensa até o STJ julgar. O tema também pode mudar pontos que a skill trata como assentados: decadência ou nulidade, consequência da invalidade e dano moral.

### Opções
| Opção | O que acontece | Risco |
|---|---|---|
| **1. Ajuizar e pedir o prosseguimento por distinção** (CPC, art. 1.037, § 9º) | O modelo tem um tópico condicional: a ação não discute a validade do cartão, e sim a nulidade do refinanciamento pelo teto do art. 28, § 1º, da Lei 14.690 | A distinção é **frágil**: o refinanciamento do saldo está dentro da questão II.b |
| **2. Ajuizar e aceitar a suspensão** | A ação fica parada até o julgamento | Os descontos mensais continuam; os prazos prescricional e decadencial seguem correndo |
| **3. Aguardar a tese** | Não ajuíza agora | Cliente segue pagando sem a ação; a tese pode vir contrária |

**Sugestão:** a opção 1 para os clientes com desconto em curso, para a ação nascer já com o pedido de prosseguimento. Se o juiz suspender, o resultado é o da opção 2. Quem pode esperar sem prejuízo pode aguardar (opção 3).

### Como fica no `nao-contratado`
A skill `nao-contratado` alega **inexistência** de contratação (fraude), questão anterior à validade que o tema discute. Decisões do TJMG afastaram a suspensão por distinção nesse caso (ementa de artigo de doutrina; julgado de outro estado, sem efeito vinculante na Bahia; ver `jurisprudencia/tema-1414-stj.md`). O risco é de o juiz suspender por engano um processo de inexistência que envolva cartão consignado.

### O que fazer agora
1. **Decida a opção.** A skill `rmc` pergunta isso antes de gerar a peça (pergunta 4-A do roteiro).
2. **Reconfira a página do Tema 1414 no dia do protocolo.** O tema pode ser julgado a qualquer momento, e a suspensão pode ser levantada ou alterada.
3. **Decida junto com o D1.** Este é o segundo ponto que condiciona a skill `rmc`: o art. 4º da Res. CMN 4.549 exclui o cartão consignado, e o modelo sustenta o teto no art. 28, § 1º, da Lei 14.690 (`rmc/references/01-tese-e-roteiro.md`, seções B1 a B3). Os dois pontos, somados, decidem se vale ajuizar agora.

### Onde está
- `rmc/references/jurisprudencia/tema-1414-stj.md` e a cópia em `nao-contratado/` (texto da questão, recursos, datas e suspensão).
- `rmc/assets/modelo-inicial-rmc.md`: tópico condicional "Do prosseguimento do feito: distinção em relação ao Tema 1.414/STJ" (`[[SE D25 = DISTINGUIR O TEMA 1414]]`).
- `rmc/references/01-tese-e-roteiro.md`, seção B4; `_manutencao/PAINEL.md`, linha D25.

## O que mudou nos arquivos

| Arquivo | Mudança |
|---|---|
| `rmc/assets/modelo-inicial-rmc.md` | subtópico da Súmula 41; juros pela citação nos pedidos g.4 e g.5; tópico de precedentes completo, com ponte para o JEC |
| `nao-contratado/assets/modelo-inicial-nao-contratado.md` | tópico de precedentes completo (distinguishing, overruling, notas de rodapé), com ponte para o JEC |
| `_acervo/pecas/padrao-pecas.md` (distribuído às duas skills) | seção 8 com o texto completo, a ponte para o JEC e a regra de não citar os Enunciados 161 e 162 |
| `*/testes/caso-ficticio/saida/inicial-*.md` | peças de teste refeitas com as mudanças (as duas são de JEC) |
| `*/references/jurisprudencia/INDEX.md` | índice por assunto, gerado por `_manutencao/gerar-indice-jurisprudencia.py` |

## Outros achados do índice que não geraram mudança, mas merecem atenção
- **Enunciados 26, 22, 120 e 144 do FONAJE** (tutela no JEC e multa) estão disponíveis e ainda não foram inseridos nos modelos. O Enunciado 26 é o que as petições do AMN citavam sem fonte.
- **Enunciado 170 do FONAJE:** no JEC, o valor do dano moral soma-se ao do dano material para a alçada. É o que o modelo já faz no valor da causa; pode ser citado.
- **Súmulas 13 e 38 do TJBA** (consignado de pessoa analfabeta): o banco pode invocá-las se o cliente não souber ler. Vale perguntar na triagem.
- **Súmulas 46 a 54 do TJBA** (litigância predatória): já alimentam a checagem pré-recurso (FSC12) do padrão de peças.

## Para você decidir
1. Manter o juros pela **citação** no RMC (aplicado) ou voltar ao evento danoso.
2. Manter o subtópico da Súmula 41 como está ou reduzi-lo a uma frase.
3. Manter o texto completo do tópico de precedentes também no JEC, com a ponte (aplicado), ou voltar à versão curta sem o art. 489.
4. Conferir as duas obras de doutrina das notas de rodapé (ou retirar as notas).
4-A. **D25 (seção 4): ajuizar o RMC e pedir o prosseguimento por distinção, ajuizar e aceitar a suspensão, ou aguardar o Tema 1414/STJ.** Pendente.
5. Inserir os Enunciados 26, 22 e 120 do FONAJE nos modelos (tutela e multa no JEC).

Registro no painel: D22 (Súmula 41), D23 (juros) e D24 (Enunciado 162), em `_manutencao/PAINEL.md`.
