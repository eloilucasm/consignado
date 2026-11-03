# Escrutínio da inicial: FSC e VF antes do ajuizamento

Consulta: 29/10/2026. Origem: catálogo de fundamentos de sentença (FSC1 a FSC12) e verificações forenses (VF1 a VF9) da skill de recurso inominado de consignado, adaptados à **petição inicial**. Este arquivo é cópia da matriz do pacote; edite a matriz, não a cópia.

## Para que serve

Na inicial ainda não há contestação nem documentos do banco. A pergunta aqui é outra: **que sentença de improcedência esta inicial permitiria, e o que a impede desde já?** Cada FSC vira uma prevenção na peça; cada VF vira o que dá para verificar **antes** de ajuizar, com o extrato do INSS, os documentos do cliente e o que o banco tiver entregado fora do processo.

As VF completas (sobre os documentos que o banco junta com a contestação) são da **réplica** e do **recurso**. Na inicial, não classifique geolocalização, IP ou biometria, não use a escala de gravidade do recurso e não afirme o que só o contrato do banco mostraria.

## Como usar (portão 3 do protocolo)

1. Rode o script de cálculo da skill. Ele grava em `calculo.json` a lista `checagem_fsc`, com o que o extrato permite apurar sozinho (FSC4, FSC5, FSC6, FSC11 e alertas de roteamento).
2. Complete com o quadro de fatos o que o script não vê (ciência, reclamação prévia, extrato bancário, documentos do cliente).
3. Para cada FSC, registre um status: **ATIVADO** (o risco existe neste caso e a peça precisa tratá-lo), **OK** (tratado na peça), **NÃO SE APLICA** (com o motivo em uma linha) ou **PENDENTE DO ADVOGADO** (depende de decisão ou de documento).
4. Grave o registro em `checagem-fsc-vf.md`, ao lado da peça, no formato do fim deste arquivo. FSC **ATIVADO** que a peça não trata deixa o portão 3 **pendente**.
5. Nada deste registro entra na peça. Ele é instrução de trabalho e entrada da réplica e do recurso.

## 1. FSC: o que a inicial faz para prevenir cada fundamento

| FSC | Sentença que perderíamos | Prevenção na inicial | Gatilho e conferência |
|---|---|---|---|
| **FSC1** assinatura "confere a olho" | o juiz compara a assinatura do contrato com a do RG e dispensa perícia | negar a autoria **contrato a contrato**, declarando que a parte não assinou instrumento algum; com isso a autenticidade fica controvertida desde a inicial (lógica do art. 341, III, do CPC) e o ônus passa ao banco (art. 429, II, do CPC; Tema 1061/STJ). Não descrever a assinatura que não se viu | sempre; conferir que cada número de contrato aparece na negativa |
| **FSC2** "múltiplas camadas" de segurança eletrônica | log, selfie e hash aceitos como prova plena | declarar que a parte não usou plataforma digital, não forneceu imagem facial, biometria, token ou senha (fato presumido do escritório para clientes idosos) e controverter **por antecipação** a autenticação eletrônica que o banco juntar. Não descrever log que não existe nos autos | sempre; se houver dossiê pré-ação do banco, ver VF4 e VF9 abaixo |
| **FSC3** recusa da inversão do ônus | o juiz nega a inversão por "falta de verossimilhança" e exige do autor prova de fato negativo | **abrir** a matéria pelo ônus **legal**: art. 14, § 3º, do CDC, art. 429, II, do CPC e Tema 1061/STJ; só depois o art. 6º, VIII, do CDC (inversão judicial, requisitos alternativos) | sempre; o verificador confere os três dispositivos na peça |
| **FSC4** "proveito econômico comprovado" | o banco junta TED para a conta do autor e o juiz conclui que houve contratação | tratar o **valor liberado** do extrato do INSS e o **extrato bancário do cliente** do mês da averbação (VF6). Liberado zero ou em branco: registrar (portabilidade pura não gera crédito). Crédito na conta: a peça **não pode negar** que o dinheiro chegou; trata do valor (devolução, depósito ou compensação com a restituição) por decisão do advogado | script: `LIBERADO_ZERO`, `LIBERADO_POSITIVO` ou `SEM_DADO`; quadro: extrato bancário |
| **FSC5** cessão/portabilidade aceita sem exame da cadeia | o juiz aceita "refinanciamento" ou "migração" como prova de regularidade | se a origem da averbação for migração, portabilidade ou refinanciamento, questionar a cadeia: existência do crédito cedido e eficácia perante o devedor (arts. 286 a 290 do CC). No `migrado` é a tese; nas demais, é alerta de que o caso pode ser de outra skill | script: `origem_averbacao` |
| **FSC6** "impugnação tardia" | o lapso entre contrato e ação vira indício de que houve contratação | registrar **quando e como** a parte soube dos descontos; separar a declaração de inexistência (não convalesce, art. 169 do CC) da repetição e do dano (prescrevem). Prazo e termo inicial são decisão do advogado | script: desconto com mais de 5 anos; quadro: data da ciência |
| **FSC7** "não impugnação específica" | a réplica rebate de forma genérica e o juiz presume autênticos os documentos do banco (art. 411, III, do CPC) | na inicial: negativa específica por contrato (FSC1) e pedido de que o banco junte cada documento com a contestação, para a réplica impugnar um a um. **O risco maior é da réplica**: o registro desta checagem segue para ela | sempre; alerta para a réplica |
| **FSC8** dano moral como "mero dissabor" | o juiz reconhece a inexistência e nega o dano | natureza alimentar do benefício, valor e duração dos descontos, idade, e reclamação prévia ao banco, se houver; Súmula 40 do TJBA exige as particularidades do caso | script: período e total; quadro: reclamação prévia |
| **FSC9** cerceamento de defesa (só Justiça Comum) | julgamento antecipado sem a perícia | Justiça Comum: pedir **já na inicial** exibição (arts. 396 a 404 do CPC) e perícia com quesitos (grafotécnica ou informática forense). Sem o pedido na inicial e na réplica, o cerceamento não se sustenta no recurso | rito; o verificador confere |
| **FSC10** correspondente, IP e geolocalização não enfrentados | a sentença ignora a origem da contratação | pedir que o banco junte a identificação do correspondente (contrato de correspondência, sede, CNPJ) e a trilha completa da autenticação, com IP público, localização e data e hora; JEC: como encargo da contestação; Justiça Comum: também por exibição. Registrar a **residência** do cliente com ID e página, para a VF9 da réplica | sempre; quadro: residência |
| **FSC11** contratos na mesma data | operação em cadeia (portabilidade e refinanciamento) não examinada | descrever, só pelo extrato, os contratos incluídos no mesmo dia ou em poucos dias, em qualquer banco. É reforço: não sustenta a tese sozinho | script: mesmo dia = alerta; até 7 dias = reforço |
| **FSC12** litigância predatória, exigências, má-fé | extinção por documentos ou multa por má-fé (Súmulas 42, 46, 47, 51 a 54 do TJBA; Tema 1198/STJ) | documentos de identidade e residência **atuais e legíveis**; procuração atualizada; **um processo por benefício + banco + tese**; nada na peça sobre quantas ações o autor ou o escritório têm, nem sobre como a procuração foi colhida. Se o dinheiro chegou à conta do cliente (FSC4) e a peça negar tudo, abre-se a Súmula 42 do TJBA | quadro: documentos; script: FSC4 |

**Súmula 42 do TJBA** (texto do acervo): "É indicativo de litigância de má fé, a negativa pelo autor de contratação de empréstimo consignado, quando restar provado no curso da ação a realização do negócio jurídico e a disponibilização de seu numerário." É o ponto em que FSC4 e FSC12 se encontram: o extrato bancário do cliente deve ser visto **antes** de ajuizar.

## 2. Onde cada FSC é tratado no modelo de cada skill

| FSC | `nao-contratado` | `migrado` | `tese-1000` | `rmc` |
|---|---|---|---|---|
| 1, 2, 7 | "A parte autora nega, contrato a contrato, a existência de manifestação de vontade" | "A parte autora nega a contratação de origem e a migração" | subtópico da negativa de manifestação de vontade quanto ao derivado | fatos: refinanciamento sem proposta, sem nova assinatura e sem repasse |
| 3 | "A responsabilidade do banco é objetiva…" e "Da inversão do ônus da prova" | idem | idem | "Da inversão do ônus da prova" |
| 4 | negativa (valor liberado) e tabela de documentos (comprovante do crédito) | idem | idem | fatos (sem repasse no refinanciamento) e tabela de documentos |
| 5 | alerta de roteamento (origem de migração) | tópico da migração e da cessão (arts. 286 e 290 do CC) | descrição pelo extrato; outro banco = fora do escopo | não se aplica, salvo origem de cessão no extrato |
| 6 | fatos (ciência) e "A pretensão não está prescrita" | idem | idem | fatos (ciência); prescrição só se o advogado pedir dobro antigo |
| 8 | "O dano extrapatrimonial é devido…" | idem | idem | subtópico do dano extrapatrimonial |
| 9, 10 | "Da inversão do ônus da prova" e "A exibição dos documentos e a perícia são necessárias" (só Justiça Comum) | idem | idem | idem, com perícia contábil |
| 11 | fatos, só pelo extrato | idem | a tese já é de mesma data (exclusão e reinclusão) | fatos, se houver |
| 12 | documentos e lista de documentos; nada sobre outras ações | idem | idem | idem |

## 3. VF antes do ajuizamento

| VF | No recurso | Na inicial | Fonte | Se não houver o dado |
|---|---|---|---|---|
| **VF1** índice dos autos | índice dos documentos dos autos | índice dos documentos do cliente, com a identificação provisória que receberão na juntada | pasta do caso | — |
| **VF2** ficha do contrato | assinatura, datas e dados cadastrais do contrato juntado | só se o banco entregou o contrato antes da ação (pedido prévio, consumidor.gov, Procon): impugnar especificamente já na inicial | dossiê pré-ação | "não aplicável: fica para a réplica" |
| **VF3** cessão de crédito | eixos existência e eficácia sobre o instrumento juntado | origem "Migrado do contrato X CBC: Y" no extrato: banco de origem, contrato de origem, datas | extrato do INSS | — |
| **VF4** autenticação eletrônica | IP, biometria, hash e campos do log | só com dossiê pré-ação: listar os campos, sem classificar | dossiê pré-ação | "fica para a réplica" |
| **VF5** correspondente bancário | sede, CNPJ, contrato de correspondência | só com dossiê pré-ação; sempre pedir que o banco o identifique | dossiê pré-ação | pedido na peça |
| **VF6** TED × liberado | valor do TED juntado × coluna "liberado" | **extrato bancário do cliente** do mês da averbação × valor liberado do extrato do INSS: houve crédito? de quanto? | extrato bancário (pedir ao cliente) | **PENDENTE DO ADVOGADO** (ver Súmula 42) |
| **VF7** análise cruzada | selfies, IPs e hashes entre contratos | contratos do mesmo banco no extrato: datas, valores e origens que se repetem | extrato do INSS | — |
| **VF8** mesma data | inclusões no mesmo dia ou em intervalo curto | mesma regra, em **todos** os bancos do extrato: mesmo dia = alerta; até 7 dias = reforço (parâmetro do escritório) | extrato do INSS | — |
| **VF9** geolocalização | coordenadas do log × residência | só **preparar**: residência com ID e página e, se o advogado der, a coordenada | comprovante de residência | registrar a lacuna para a réplica |

## 4. Formato do registro `checagem-fsc-vf.md`

```markdown
# Checagem FSC e VF: [identificador do caso] — [skill] — [data]

| FSC | Status | Achado (com fonte) | Onde a peça trata |
|---|---|---|---|
| FSC1 | OK | negativa por contrato (3 contratos) | negativa específica |
| FSC4 | ATIVADO | contrato X: liberado R$ 2.034,54; extrato bancário: crédito de R$ 2.034,54 em 15/03/2024 (ID provisório 7) | [DECISÃO DO ADVOGADO: devolução ou compensação] |
| … (FSC1 a FSC12, todas as linhas) | | | |

| VF | Status | Achado |
|---|---|---|
| VF1 | executada | 6 documentos |
| VF2 | não aplicável | sem dossiê pré-ação; fica para a réplica |
| … (VF1 a VF9) | | |

Para a réplica: [o que a réplica deve conferir primeiro, por exemplo FSC7 e VF6 com o TED que o banco juntar].
```
