# Diretrizes de replicação do framework de skills jurídicas

Escrito em 01/11/2026 para quem vai montar um pacote de skills do Claude para outro ramo do direito ou outro escritório.

**Relação com o kit.** O método de base está no kit de replicação (`AMN/_kit-replicacao/BRIEFING-REPLICACAO-FRAMEWORK.md` e `README.md`), escrito em 28/10/2026 a partir do pacote previdenciário Cortex. Estas diretrizes são a **segunda camada**. Trazem o que o pacote de consignado acrescentou e provou entre 28/10 e 01/11/2026. Leia o briefing primeiro. Quando os dois divergirem, valem estas diretrizes.

Todo arquivo citado existe em `consignado-pacote/` e pode ser conferido lá.

---

## 1. O que está provado e o que não está

| Afirmação | Situação em 01/11/2026 |
|---|---|
| A arquitetura em camadas funciona e se repete em dois ramos (previdenciário, consignado) | **provado** |
| As regras do verificador disparam quando o erro aparece | **provado**: 46 defeitos plantados, todos reprovados (`testar-verificador.py`) |
| Cálculo, datas e checagem saem de script testado | **provado** em casos fictícios das quatro teses |
| Uma peça real, de ponta a ponta, sai pronta para revisão | **não provado**: nenhum caso real passou pelo coordenador |
| O motor (verificador, sincronizador, protocolo base) é independente do setor | **parcial**: o motor é genérico, mas parte das regras do consignado está no código, não só na configuração |

Replique o método com confiança. Não prometa ao novo escritório resultado em caso real antes do piloto real (seção 9).

---

## 2. Os doze invariantes

Valem em qualquer ramo. Cada um tem o mecanismo que o garante: uma regra que só existe no texto da skill depende da disciplina do modelo, e não se considera garantida.

| # | Invariante | Por quê | Mecanismo que o garante |
|---|---|---|---|
| 1 | **Nada citado de memória.** Norma e precedente só do acervo da skill; o resto vira `[CONFERIR]` | O risco em direito é citar com segurança o que não existe ou mudou | Verificador: citação sem arquivo no acervo reprova |
| 2 | **Transcrição é literal.** Todo trecho entre aspas ou em bloco `>` atribuído a norma ou precedente existe, letra a letra, no arquivo do acervo | Existir o arquivo não basta: a ementa pode ter sido parafraseada ou adulterada | Verificador, seção de transcrições (`extras.transcricoes`), com normalização em `normalizar.js` |
| 3 | **Número só de script.** Total, dobro, valor da causa e datas vêm de `calculo.json` | Número digitado à mão é o erro que mais custa | Verificador confere cada valor da peça contra o `calculo.json` ao lado |
| 4 | **Fato tem estado e proveniência** (`confirmado`, `relatado`, `inferido`, `desconhecido`, com documento e página) | Relato do cliente não é prova | Quadro de fatos obrigatório; portão 1 |
| 5 | **A sentença que perderíamos vem antes da peça.** Catálogo de fundamentos de sentença desfavorável (FSC) e verificações forenses (VF) do ramo, aplicados antes de redigir | A peça se defende do que realmente derruba casos no juízo local | `escrutinio.py` grava a checagem; verificador exige as linhas e o tratamento na peça |
| 6 | **Regra vigente separada do histórico de decisões.** O protocolo traz só a regra; data, motivo e alternativa ficam no painel e nas notas | Regras empilhadas com datas confundem o modelo quando o contexto enche | Seção "Regras de citação e de pedido vigentes" do protocolo; `PAINEL.md` |
| 7 | **Presunções do escritório explícitas.** O que o escritório presume (e por isso não marca) está listado, e cede ao documento | Sem isso, a peça vira um mar de `[CONFERIR]` que ninguém lê | Seção "Presunções do escritório" do protocolo |
| 8 | **O advogado decide o que é dele.** Rito, local do fecho, escolhas de risco e tratamento de valores recebidos são perguntados, nunca inferidos | Decisão operacional arbitrária é passivo do escritório | Portão 1; marca `[DECISÃO DO ADVOGADO]`; coordenador proibido de responder por conta própria |
| 9 | **Todo ponto tem pedido e todo pedido tem ponto** | Fundamento sem pedido não rende; pedido sem fundamento é atacável | Mapa de argumentos (`mapa-argumentos.json`); verificador confere contra "Dos pedidos" |
| 10 | **Bloqueio honesto.** Dois portões falhos: só diagnóstico ou minuta `BLOQUEADO PARA USO FINAL` | Não existe "completar com algo plausível" | Protocolo, portão 4 |
| 11 | **Cada regra do verificador é provada por um defeito plantado** | Regra que não dispara dá falsa segurança (aconteceu, seção 10) | `testar-verificador.py`: cópia limpa passa e cada defeito reprova com a mensagem certa |
| 12 | **Passagem entre skills com rota fechada.** O coordenador entrega processo, tese, etapa, documentos, respostas e bloqueios antes de a especialista começar | Sem rota, o coordenador simula a especialista ou pula portões | `roteamento.json` e Painel do Caso (`consignado/SKILL.md`, seção 5) |

---

## 3. Arquitetura de referência

A coluna "Do setor" diz o que se refaz a cada ramo. O resto se copia.

| Camada | Arquivos no consignado | Genérico | Do setor |
|---|---|---|---|
| Acervo fechado | `_acervo/normas/`, `_acervo/jurisprudencia/` (cabeçalho YAML com datas e nível), `datas-citaveis.md` | formato do arquivo, cabeçalho, níveis, scripts de coleta e prova | as normas e os precedentes |
| Distribuição | `_acervo/manifesto.json`, `sincronizar-acervo.js` (relatório, backup, `--trazer`) | inteiro | a lista de quem recebe o quê |
| Protocolo comum | `_acervo/protocolo/protocolo.md`, `quadro-de-fatos.md` | abertura, quadro, fontes, portões, marcas, dados pessoais, formato | presunções, regras vigentes, tabela de normas por data, regras de cálculo |
| Padrão de peças | `_acervo/pecas/padrao-pecas.md` | estrutura, checklist da seção 9, precedentes evocados | pedidos de rotina, prova por rito, assinaturas |
| Contraditório antecipado | `_acervo/pecas/escrutinio-fsc-vf.md`, `_acervo/scripts/escrutinio.py` | formato (FSC/VF, status, registro, portão 3), linha do tempo | o catálogo FSC e as verificações VF do ramo |
| Cálculo e fatos | `*/scripts/calcular*.py`, `extrato.py` | contrato de saída (`calculo.json`, `dossie-do-caso.json`, `checagem-fsc-vf.md`), segunda via de todo total | a leitura do documento-base e as regras de conta |
| Skills especialistas | uma por tese e etapa (`nao-contratado`, `migrado`, `tese-1000`, `rmc`, `replica-consignado`, `recurso-…`) | esqueleto do `SKILL.md`, pausas, portões | modelo de peça, roteiro da tese |
| Coordenador e triagem | `consignado/`, `triagem-consignado/` | roteamento por etapa e tese, rota fechada, perguntar uma vez | tabela de roteamento e documentos de entrada |
| Verificação | `verificar-pacote.js`, `verificador.config.js`, `normalizar.js`, `testar-verificador.py` | motor e tipos de regra | as regras proibidas e exigidas do ramo |
| Governança | `PAINEL.md`, `ROTINA.md`, notas de decisão na raiz, `APRENDIZADOS-PARA-O-KIT.md` | formato | conteúdo |

**Corte de skill.** No consignado, o corte é **tese × etapa**: quatro iniciais por tese, uma réplica e um recurso. Funcionou melhor que o corte por função (extração, pesquisa, redação, revisão em skills separadas), porque cada passagem entre skills perde contexto. As fases de função continuam existindo, mas **dentro** da skill, apoiadas em scripts.

---

## 4. Ordem de construção e critério de saída de cada fase

| Fase | Entrega | Só avance quando |
|---|---|---|
| 0. Segurança | pasta nova, backup do material de origem, `.editorconfig` (LF, UTF-8) | o material antigo está intocado |
| 1. Inventário | lista de toda citação dos modelos atuais do escritório (`inventario-citacoes.py`) | cada citação tem origem conhecida |
| 2. Acervo | normas e precedentes com fonte oficial, prova de integridade e cabeçalho | `comparar-fonte.js` aprovado em toda norma; datas no cabeçalho |
| 3. Protocolo e padrão | protocolo, quadro de fatos, padrão de peças, **presunções e regras vigentes** do escritório | o escritório leu e aprovou as presunções |
| 4. Piloto | uma skill de inicial completa, com script de cálculo e caso fictício | teste de regressão passando; verificador com 0 erros |
| 5. Engenharia | manifesto, sincronizador, verificador com as regras do ramo, teste do verificador | todo defeito plantado reprova |
| 6. Contraditório | catálogo FSC e VF do ramo, a partir de **sentenças reais desfavoráveis** do escritório | cada FSC tem gatilho e lugar na peça; o script grava a checagem |
| 7. Demais skills | uma por tese; depois réplica e recurso | cada uma com caso fictício e teste |
| 8. Coordenador | triagem e roteamento | teste de roteamento com documentos fictícios |
| 9. Piloto real | três casos reais, um de cada tese principal, revisados pelo advogado | ficha de avaliação (briefing, seção 16) preenchida |
| 10. Entrega | zips, manual, calendário de vigilância | painel sem `PRESUMIDO` sem dono e data |

No consignado, as fases 6 e 9 ficaram para depois das skills. O certo é a fase 6 antes da 7: o catálogo FSC muda o modelo de peça, e refazer modelos custa mais que esperar.

---

## 5. Como montar as peças próprias do ramo

### 5.1 Catálogo "a sentença que perderíamos" (FSC)

1. Reúna de 10 a 30 sentenças **desfavoráveis** do juízo onde o escritório atua.
2. Para cada uma, extraia a razão de decidir em uma frase. Agrupe as iguais.
3. Cada grupo vira um FSC com:
   - **gatilho:** o fato do caso que o ativa;
   - **onde a peça trata:** o tópico do modelo;
   - **o que o script consegue apurar sozinho.**
4. Status possíveis: `ATIVADO`, `OK`, `NAO_SE_APLICA`, `PENDENTE_ADVOGADO`. Um FSC `ATIVADO` sem tratamento na peça deixa o portão 3 pendente.
5. O mesmo catálogo serve à réplica (prevenir) e ao recurso (atacar a razão de decidir).

Modelo: `_acervo/pecas/escrutinio-fsc-vf.md` (FSC1 a FSC12).

### 5.2 Verificações forenses (VF)

São o que se confere nos documentos da parte contrária: ficha do contrato, dados cadastrais, autenticação e log, TED ou pagamento, correspondente, cessão, análise cruzada, datas.
- Cada achado leva fonte (ID e página) e gravidade: `CRÍTICO`, `RELEVANTE`, `REFORÇO`, `PROCESSUAL` ou `ALERTA_CONTRA`.
- `ALERTA_CONTRA` é o achado que pesa contra o cliente e **exige decisão expressa**.

Modelo: `replica-consignado/scripts/fichas.py`.

### 5.3 Presunções e regras vigentes do escritório

Pergunte ao escritório, por escrito, o que ele presume em todo caso: renda, ciência, ausência de contato prévio, valores fixos (como o dano moral) e o que nunca cita.
- Grave isso no protocolo em duas seções: **presunções de fato**, que cedem ao documento, e **regras de citação e de pedido**, em tabela.
- Data e motivo de cada decisão vão para o painel, não para a regra.

### 5.4 Script de cálculo

Contrato mínimo de saída, válido para qualquer ramo:
- `calculo.json`: todos os números da peça, com a marca `CÁLCULO A CONFERIR`;
- `calculo.md`: tabela para o advogado;
- `checagem-fsc-vf.md` e `dossie-do-caso.json`, gravados por `escrutinio.gravar()`, com a **linha do tempo** (`escrutinio.cronologia()`).

Regras:
- Todo total tem segunda via (soma por outro caminho).
- Toda data que decide norma, prazo ou tese entra na linha do tempo com fonte e efeito jurídico.
- Sem histórico completo, o script **trava**; não estima.

### 5.5 Catálogo de defesas da parte contrária e mapa de argumentos

- Tabela com código, alegação típica, resposta, fonte no acervo e FSC prevenido. Modelo: `replica-consignado/references/02-defesas-do-banco.md`.
- O advogado registra os pontos da contestação com o código (ou `NOVO`). O script monta o mapa ponto → resposta → prova → pedido.
- Defesa fora do catálogo sai com `[DECISÃO DO ADVOGADO]`. Se aparecer duas vezes, vira linha do catálogo.

---

## 6. Verificação: tipos de regra e como acrescentar

| Tipo | O que confere | Exemplo no consignado |
|---|---|---|
| Existência | citação tem arquivo e dispositivo no acervo | artigo, súmula, tema, acórdão por número |
| Transcrição | o texto citado existe no arquivo | ementa do TRF-4; tese do EAREsp 676.608 |
| Número | valor da peça é o do `calculo.json` | valor da causa, dobro por contrato |
| Estrutura | peça tem o que o escritório exige | fecho, tópico de precedentes, negativa por contrato |
| Proibição | o que não pode voltar | Tema 929 como fundamento; MP não aplicável; tratamento antigo |
| Coerência | ligações entre artefatos | registro FSC/VF ao lado da peça; pedidos do mapa na peça |
| Cópias | arquivo distribuído igual ao acervo | protocolo, padrão, scripts sincronizados |

Para acrescentar uma regra:
1. Escreva a regra em `verificador.config.js`. Use o motor só se o tipo for novo.
2. Acrescente em `testar-verificador.py` um defeito que a viole.
3. Rode o teste: a cópia limpa passa e o defeito reprova com a mensagem certa.
4. **Teste a mutação, não só a regra.** Se a comparação ignora pontuação ou prefixo, uma troca como "independe" para "depende" pode não alterar nada. Prefira trocar palavras inteiras.

Regra de ouro (vem do kit): **cada erro que aparece duas vezes vira regra nova**.

---

## 7. Governança

- **Decisão do escritório:**
  1. nota com problema, opções e recomendação (exemplo: `NOTA-revisao-encadeamento-2026-10-29.md`);
  2. redação proposta pronta para colar (`NOTA-redacao-R4-R7-2026-11-01.md`);
  3. aceite;
  4. aplicação em todos os arquivos afetados;
  5. registro no painel como resolvido.

  Nunca aplique antes do aceite. Nunca deixe a regra antiga em outro arquivo: procure todas as ocorrências antes de fechar.
- **Níveis de confiança:** `VERIFICADO` (segunda via), `FEITO`, `PRESUMIDO` (com dono e data), `ABERTO`. Não escreva "conferido" sem evidência.
- **Fonte bloqueada:** portais de tribunal podem barrar acesso automático com desafio anti-robô. A skill não contorna o desafio. Registra a URL oficial e pede o documento ao escritório. O escritório traz o PDF, a ficha entra com nível `VERIFICADO` e o caminho do arquivo.
- **Edição em arquivo distribuído:** sempre no acervo. Se editou na skill por engano, use `sincronizar-acervo.js --trazer`. Antes de `--aplicar`, rode o relatório e confira que só os seus arquivos diferem. Se outra pessoa estiver editando o acervo, espere.
- **Calendário de vigilância:** temas afetados, medidas provisórias, consolidações de instrução normativa, súmulas locais e valores anuais (salário mínimo). Fica na `ROTINA.md`, com dono.

---

## 8. Passagem entre skills

O coordenador não redige. Antes de passar a vez, fecha a rota de cada processo:
- benefício, réu, tese, etapa e skill;
- contratos (todos na análise e no termo);
- documentos e arquivos de entrada;
- respostas do advogado: rito, local, extrato bancário, documentos pré-ação;
- bloqueios.

No Cowork, a rota fica em `roteamento.json`; no chat, uma linha por processo no Painel do Caso. Um campo obrigatório vazio vira pergunta, e o processo não segue. A especialista é lida **por inteiro** antes de ser executada, e os portões e pausas dela continuam valendo.

---

## 9. Critérios de aceite (somam-se aos do briefing, seção 16)

1. `testar-verificador.py` com todos os defeitos reprovados e a cópia limpa aprovada.
2. Toda transcrição dos modelos confere com o acervo (0 erros na seção de transcrições).
3. Autoteste do módulo de checagem passando (`escrutinio.py --teste`). Autoteste que falha em silêncio é defeito.
4. Teste de caso fictício de cada skill conferindo também a linha do tempo e, na réplica, o mapa de argumentos.
5. Nenhuma regra do protocolo contradiz um modelo. Confira por busca: juros, dobra, valores fixos, termos proibidos.
6. Todo fundamento do modelo leva a um pedido do modelo. Exemplo: rebater o pedido de má-fé e ter o pedido de rejeição.
7. Piloto real com três casos, com a ficha de avaliação preenchida, antes de liberar à equipe.

---

## 10. Erros desta fase e como evitar (continuação do briefing, seção 14, e do `APRENDIZADOS-PARA-O-KIT.md`)

17. **Autoteste quebrado sem ninguém ver.** O autoteste do `escrutinio.py` esperava FSC8 pendente, mas uma decisão do escritório mudou para OK, e ninguém rodou o teste. **Evite:** rode os autotestes no fim de toda rodada, junto com o verificador.
18. **Teste que não testava.** A troca "independe" por "depende" passou, porque a comparação só por letras acha "depende" dentro de "independe". **Evite:** veja cada defeito novo falhar antes de confiar nele.
19. **Ementa transcrita sem o acórdão no acervo.** Três modelos citavam a ementa do TRF-4 sem o arquivo. **Evite:** a regra de transcrição reprova isso. Ao trazer o acórdão, leia a ementa **inteira**: dois itens dela eram contrários à tese, e o arquivo registra até onde se pode transcrever.
20. **Protocolo e modelo em conflito.** O protocolo mandava Súmula 54 para os juros, e o modelo do RMC usava a Súmula 33/TJBA por decisão do escritório. **Evite:** o critério de aceite 5. Regra com exceção por tese fica na tabela de regras vigentes, com a exceção escrita.
21. **Fundamento sem pedido.** A réplica rebatia o pedido de má-fé do banco, mas não pedia a rejeição. **Evite:** o mapa de argumentos e a regra de coerência.
22. **Script de skill que é cópia do acervo.** Editar o `fichas.py` na skill reprovou o verificador ("difere do acervo"). **Evite:** consulte o manifesto antes de editar; se errou, use `--trazer`.
23. **Divergência de dado de precedente entre fontes.** Uma nota dizia um relator, e o acervo sugeria outro. O inteiro teor resolveu: a anotação do repositório oficial se referia ao grupo de processos julgados juntos, não ao paradigma. **Evite:** relator, data e modulação só se afirmam com o acórdão lido.
24. **Leitura de PDF com `python -I`.** O modo isolado ignora a biblioteca instalada com `pip --user`. **Evite:** copie o PDF para uma pasta isolada e rode sem `-I`, só lendo texto.

---

## 11. O que falta para o kit ser um framework autônomo

1. **Separar o motor das regras.** Hoje o motor tem trechos do consignado: a negativa por contrato, as linhas FSC/VF e o FSC9 por rito. Esses trechos devem passar para a configuração, como o kit já fez com as regras de previdência.
2. **Levar ao kit as peças novas.** Entram `normalizar.js`, a seção de transcrições e a de mapa do verificador, `escrutinio.py` em versão genérica (FSC/VF e cronologia sem as regras do consignado) e o formato `mapa-argumentos.json`.
3. **Atualizar o briefing do kit** com as seções 2, 5 e 9 destas diretrizes, ou anexar este arquivo ao kit.
4. **Fazer o piloto real** (fase 9) e registrar o resultado aqui.

Enquanto os itens 1 e 2 não forem feitos, replicar significa copiar o pacote de consignado e podar o que é do setor, usando a coluna "Do setor" da seção 3 como lista do que trocar.
