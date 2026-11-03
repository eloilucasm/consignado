# Manual de uso: pacote de consignado do INSS

Para: advogados do escritório que vão usar as skills de consignado no Claude (Cowork ou chat).
Versão: rascunho de 01/11/2026, a revisar depois do piloto com casos reais.

Este manual ensina a **usar** o pacote: o que levar, o que pedir, o que responder e como ler a resposta. Não traz regra jurídica, que está nas skills e muda com o tempo.

---

## 1. O que o pacote faz e o que não faz

**Faz**, em ações de empréstimo consignado do INSS contra banco:
- a triagem do cliente (o que ajuizar, contra quem, em qual tese);
- a petição inicial nas quatro teses: não contratado, migrado, Tese 1000 e refinanciamento de cartão RMC/RCC;
- a réplica à contestação do banco;
- o recurso inominado (JEC) ou a apelação (Justiça Comum) contra sentença desfavorável;
- o Word no padrão do escritório, pela `tipografia-azul`.

**Não faz:**
- conta bancária ou de pagamento fraudulenta e seguro não contratado (há skills próprias para isso, fora deste pacote);
- protocolo, envio ou assinatura de peça;
- peça pronta: **tudo o que sai é minuta**. O advogado revisa, decide o que ficou marcado e assina.

---

## 2. Primeiro uso

O jeito mais simples: **mande a pasta do cliente**, ou digite `/consignado`. O coordenador lê os documentos, descobre em que etapa está cada processo e chama a skill certa. Você não precisa saber o nome de nenhuma skill.

Se já sabe o que quer, chame a skill direto pelo nome, com a barra (seção 3). Exemplos:
- `/nao-contratado` com a ficha do cliente;
- `/replica-consignado` com o processo que tem a contestação.

**Ambiente.** No **Cowork**, as skills rodam os scripts de cálculo, de checagem e de Word. **No chat, sem execução de código**, elas fazem as contas em tabela, mas o resultado sai com a pendência do cálculo aberta: rode o caso no Cowork antes de protocolar.

---

## 3. Mapa das skills

| Skill | Quando usar | Exemplo de pedido |
|---|---|---|
| `consignado` (coordenador) | não sabe por onde começar, ou o cliente tem processos em etapas diferentes | "Segue a pasta da Dona Maria. O que faço agora?" |
| `triagem-consignado` | cliente novo: tem o termo e a análise, ainda não tem a ficha | "Cruza o termo com a análise e me diz o que ajuizar." |
| `nao-contratado` | inicial de contrato que o cliente nega (blocos B, C e Caixa) | "Faz a inicial do processo 1 da ficha." |
| `migrado` | inicial de contrato que veio de outro banco ("Migrado do contrato … CBC") | "Inicial do migrado contra o Agibank, processo 2." |
| `tese-1000` | inicial de contrato derivado com sufixo (`_0001`) sobre contrato já excluído | "Inicial da Tese 1000 contra o BNP." |
| `rmc` | inicial de refinanciamento de cartão consignado (marco de 200%) | "Inicial do RMC do BMG, com o histórico do cartão." |
| `replica-consignado` | o banco contestou | "Réplica neste processo; a contestação está no ID 200." |
| `recurso-inominado-consignado-geolocalizacao` | sentença de improcedência, extinção ou multa | "Recurso contra esta sentença." |
| `tipografia-azul` | gerar o Word no padrão do escritório | "Gera o Word desta peça." |

**A inicial é melhor feita pela skill da tese**, não pelo coordenador. O coordenador só encaminha.

---

## 4. O que levar em cada etapa

| Etapa | Documentos | Observação |
|---|---|---|
| Entrada (triagem) | Termo de Responsabilidade assinado; Análise Jurídico-Documental (uma por benefício); extrato do INSS (Histórico de Empréstimo Consignado), um por benefício | **Só vira ação o contrato que está na análise e no termo.** O que não está no termo não é ajuizado, sem pergunta. |
| Inicial | a ficha aprovada; extrato do INSS; documentos pessoais e comprovante de residência atuais e legíveis | Recomendado: **extrato bancário do cliente no mês de cada averbação** (seção 5). No RMC, o histórico mensal completo do cartão (HISCRE ou faturas). |
| Réplica | a inicial, a contestação e os documentos do banco; se tiver, o `dossie-do-caso.json` que a inicial gerou | A skill abre a primeira página de cada documento do banco antes de dizer o que ele é. |
| Recurso | a sentença, a inicial e a réplica; se tiver, o `dossie-do-caso.json` e o `fichas.json` | O prazo é controlado pelo escritório; a skill não pergunta a data da intimação. |

Documento ilegível vira `[CONFERIR]`. Documento que falta e muda o próximo passo vira pergunta; os demais viram pendência.

---

## 5. As perguntas que você vai responder (e por quê)

A skill pergunta **uma vez**, no máximo três coisas por rodada, e não escolhe por você:

| Pergunta | Por quê |
|---|---|
| **Rito: JEC ou Justiça Comum?** | Muda o juízo, os pedidos de prova (exibição e perícia só na Justiça Comum) e o recurso. A skill pode sugerir; quem decide é você. |
| **Cidade e UF do fecho** | Não se presume pelo endereço do cliente nem pela comarca. |
| **O cliente trouxe o extrato bancário do mês da averbação?** | Se o dinheiro do empréstimo caiu na conta e a peça negar tudo, o juiz pode ver má-fé (Súmula 42 do TJBA). É **recomendado**, não obrigatório: sem ele, fica registrado como pendência e você decide se ajuíza. |
| **Se caiu dinheiro na conta: devolução, depósito em juízo ou compensação?** | A peça reconhece o lançamento e nega a contratação; o tratamento do valor é decisão sua, e fica marcado até você decidir. |
| **O banco entregou contrato ou trilha antes da ação?** | Muda as verificações sobre os documentos do banco. |
| Só no migrado: **interesse na audiência de conciliação** (Justiça Comum) | Requisito da inicial. |
| Só no RMC: **ação anterior sobre o mesmo cartão?** e **só o mínimo da fatura é descontado em folha?** | Coisa julgada e a premissa da tese. |

---

## 6. Como ler a resposta

Toda resposta traz, nesta ordem:

1. **Painel do Caso:** quem é o cliente (com identificador abreviado), cada processo (benefício, banco, tese, etapa) e o que foi feito.
2. **Quadro de fatos:** cada fato com um estado. `confirmado` tem documento, ID e página. `relatado` vem do cliente e **nunca vira prova na peça**. `inferido` foi deduzido. `desconhecido` é o que falta. A linha do tempo do caso (averbação, descontos, exclusão, ciência, prescrição) vem do script.
3. **A minuta**, em Markdown.
4. **Os quatro portões**, cada um como passou, pendente ou bloqueado:
   - fatos e enquadramento;
   - prova e cálculo;
   - contraditório, isto é, "a sentença que perderíamos";
   - revisão final.
5. **Pendências e próximas diligências**, no máximo três.

**Marcas na minuta** (em negrito no chat, com realce amarelo no Word):

| Marca | O que significa | O que fazer |
|---|---|---|
| `[CONFERIR: …]` | falta dado ou fonte | conferir no documento indicado |
| `[PREENCHER: …]` | campo sem informação | preencher |
| `[VERIFICAR ANTES DE PROTOCOLAR: …]` | tese ou citação que depende do seu juízo | ler e decidir se mantém |
| `[DECISÃO DO ADVOGADO: …]` | escolha que é sua (por exemplo, o valor que caiu na conta) | escolher e apagar a alternativa |
| `CÁLCULO A CONFERIR` | conta feita pelo pacote | conferir a tabela do cálculo |

**Peça com marca não está pronta para protocolo.** Peça com a **Observação interna "BLOQUEADO PARA USO FINAL"** no topo é só diagnóstico ou minuta parcial: algo essencial falta. A observação lista o quê.

---

## 7. Três fluxos típicos

**A. Cliente novo, contrato que ele não reconhece.**
1. Mande termo, análise e extrato do INSS (ou a pasta inteira, com `/consignado`).
2. Confira a **ficha de ajuizamento**: processos, réus, contratos, skill de cada um. Aprove ou corrija.
3. Responda rito, cidade e se há extrato bancário.
4. Receba a minuta e a tabela do cálculo. Confira as marcas e os portões.
5. Peça o Word.

**B. O banco contestou e juntou TED do valor do empréstimo na conta do cliente.**
1. Chame `/replica-consignado` com a inicial e a contestação.
2. A skill monta o índice dos autos, as fichas dos contratos e o **mapa de argumentos**: cada alegação do banco, a resposta, a prova e o pedido correspondente.
3. No **cartão de pausa**, ela mostra o TED igual ao valor liberado como **alerta contra o cliente**. Decida o tratamento do valor antes de ela redigir.
4. Alegações fora do catálogo de defesas aparecem como `NOVO` e pedem sua decisão.

**C. Sentença de improcedência.**
1. Chame a skill de recurso com a sentença, a inicial e a réplica.
2. Ela fixa o escopo (rito, nome da peça, desfecho, multa) e diagnostica o fundamento da sentença.
3. Ela monta o **mapa de ataque**: fundamento, erro, norma, prova, pedido e viabilidade. No JEC, avalia também a exposição a honorários se o recurso perder.
4. **Pausa obrigatória:** nada é redigido sem a sua confirmação. Itens de geolocalização marcados como REVISÃO HUMANA só entram com a sua decisão.

---

## 8. Word e Google Docs

Ao fim da peça, peça o Word: a `tipografia-azul` aplica o padrão do escritório (A4, Lato, azul-marinho, numeração 1./a./i.) e o **realce amarelo** nas marcas. Sem execução de código, a peça fica em Markdown e a formatação fica pendente. O título da ação sai em maiúsculas só na primeira letra das palavras principais, nunca todo em caixa alta.

---

## 9. Retomar um caso em outra conversa

Ao fim de cada etapa, a skill escreve um **resumo de continuidade**. Na conversa nova, cole esse resumo e anexe:
- da inicial: `calculo.json` e `dossie-do-caso.json`;
- da réplica: `fichas.json` e `mapa-argumentos.json`.

A skill seguinte parte deles sem repetir as perguntas. Esses arquivos são roteiro, não prova: tudo é reconferido nos autos.

---

## 10. Limites e o que conferir antes de assinar

- **Citações:** o pacote só cita o que está no acervo dele, e transcrição é conferida letra a letra contra a fonte. O que não está no acervo vira `[CONFERIR]`. Mesmo assim, leia cada precedente citado antes de assinar.
- **Números:** vêm do script. Confira a tabela do cálculo, principalmente a quantidade de parcelas de contrato ativo.
- **Fatos:** nada que seja só relato do cliente deve aparecer como provado.
- **Rito, cidade e decisões marcadas:** sempre suas.
- **Dados pessoais:** a resposta mascara CPF e NB quando não são necessários. Não cole documentos inteiros na conversa sem necessidade.
- **Atualização:** normas, temas do STJ e súmulas mudam. O pacote informa a data da consulta de cada fonte; se a data estiver antiga, avise quem mantém o pacote.

**Boas práticas:**
- Um cliente por conversa.
- Mande os documentos inteiros, não prints.
- Responda as perguntas da skill antes de pedir a peça.
- Desconfie de minuta sem nenhuma marca em caso com documento faltando.
- Problemas e sugestões vão para quem mantém o pacote, com o resumo de continuidade do caso.
