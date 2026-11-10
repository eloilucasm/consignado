---
name: "tipografia-azul"
description: "Formata peças e documentos jurídicos no padrão Tipografia Azul do AMN (A4, Lato, azul-marinho, numeração 1./a./i.). Use ao redigir ou formatar petição, parecer, contrato, ofício ou rascunho em Word."
---

# Tipografia Azul

Padrão visual dos documentos do escritório. Aplique-o sempre que o pedido for redigir, formatar ou reformatar uma peça ou documento em Word (.docx) ou para abrir no Google Docs. A redação do conteúdo é do usuário, ou sua quando ele pedir. Esta skill trata da forma.

Se o usuário anexar o modelo .dotx ou .docx do escritório, parta dele e preserve seus estilos. Sem anexo, gere o .docx do zero com os valores abaixo (biblioteca `docx` do npm, ver a skill `docx`). O design system "Tipografia Azul", publicado como artefato, é a referência completa; consulte-o se houver dúvida. Os valores abaixo vêm do timbrado do escritório e de uma petição real, revisada à mão.

## Destino: Word ou Google Docs

O usuário prefere o Google Docs. Entregue sempre um .docx, que o Docs abre. Se o destino não estiver claro, assuma Google Docs e diga isso na resposta.

Para Google Docs:
- O Docs não liga a numeração aos estilos e não aceita texto antes do número. Ele também regrava as cores dos Títulos 4 a 6. Aplique numeração, recuos e cores diretamente nos parágrafos, além de usar os estilos do padrão. Gere a numeração 1., a., i. como lista comum.
- Recuo de 4 cm do Título 3 (citação e ementa): ponha `w:ind w:left="2268"` **no próprio parágrafo**, não só no estilo. O Docs pode descartar o recuo de estilo personalizado (estilo de id `Titulo3` ou de nome "Título 3"). Use os ids internos do Word (`Heading1` a `Heading9`, nome "heading 1" a "heading 9"), que o Docs reconhece. O recuo no próprio parágrafo vale também para o Word (passo 4 de "Como trabalhar").
- Cláusulas de contrato: escreva "Cláusula 1ª –" literalmente no texto do Título 8, sem numeração automática.
- Diga ao usuário que o recuo deslocado pode ser reaplicado em Formatar, Alinhar e recuar, Opções de recuo, Recuo especial "Deslocado", se o Docs o alterar na abertura. Se o estilo "Título 1" mudar, use "Atualizar 'Título 1' para corresponder".

Para Word: use numeração automática em lista de vários níveis ligada aos estilos, inclusive "Cláusula %1ª –" no Título 8.

## Página

- A4 retrato. Margens: superior 3,10 cm (1757 twips), esquerda e direita 2,00 cm (1134), inferior 2,54 cm (1440). Cabeçalho e rodapé a 1,27 cm (720).
- "Primeira página diferente" ligada. Cabeçalho e rodapé ficam vazios por padrão: o escritório não usa logotipo no modelo. Não acrescente numeração de página sem pedido.
- Fonte única: Lato (Lato Light e Lato Black quando indicado). Padrão do documento: 12 pt, entrelinha 1,15, justificado, idioma pt-BR.

## Cores

- `navy` #23275f: endereçamento, título da peça, tópicos, subtópicos, número das alíneas, cláusulas, rótulos, ênfases.
- `blue` #3b63af: só a frase que abre o argumento e os destaques simples.
- `ink` #000000: texto corrido, texto das alíneas e notas de rodapé.
- `muted` #666666: observações internas (Título 6). Remova toda observação antes de protocolar ou enviar.
- Papel sempre branco. Não use página amarela nem cabeçalho de rascunho.
- Realce amarelo: só nas marcas de pendência (ver "Marcas de pendência e minuta bloqueada").

## Marcas de pendência e minuta bloqueada

Marcas como `[CONFERIR: …]`, `[PREENCHER: …]`, `[VERIFICAR ANTES DE PROTOCOLAR: …]`, `[DECISÃO DO ADVOGADO: …]`, `[CONFIRMAR …]` e `[CÁLCULO A CONFERIR]` precisam saltar aos olhos no documento:

- Aplique **realce amarelo** de caractere (no Word, `highlight` amarelo; no Google Docs, cor de realce amarela) ao texto inteiro da marca, colchetes incluídos. Nunca pinte a página, o parágrafo inteiro nem o fundo da célula.
- Mantenha a marca no ponto exato em que veio, com o texto completo. Não a omita, não a resuma, não a mova para o fim e não a converta em nota de rodapé.
- Dentro de tabela, de citação (Título 3) ou de nota de rodapé, a marca também leva o realce.
- Peça bloqueada ou com pendências traz no topo uma **Observação interna** (Título 6) com "BLOQUEADO PARA USO FINAL" ou com a lista do que falta. Ela é removida antes de protocolar.
- Toda marca vem **entre colchetes**, inclusive `[CÁLCULO A CONFERIR]`. Se o rascunho trouxer a marca solta ou em itálico (`*CÁLCULO A CONFERIR.*`, de modelo antigo), ponha os colchetes e aplique o realce do mesmo jeito.
- **Confira antes de entregar:** conte as marcas no Markdown (`\[(?:CONFERIR|PREENCHER|VERIFICAR|DECISÃO|CONFIRMAR|CÁLCULO A CONFERIR)[^\]]*\]`) e os trechos com realce amarelo no .docx (no XML, `<w:highlight w:val="yellow"/>`), em `document.xml` e em `footnotes.xml`. Conte cada trecho contínuo de runs com realce como um só: a marca partida em vários runs não conta várias vezes. Os números têm de bater; se não baterem, ache a marca sem realce e corrija. Marca sem realce passa sem a revisora ver.
- Na resposta, diga quantas marcas ficaram no documento. Documento com marca não está pronto para protocolo.

## Estilos (nome no Word)

| Uso | Estilo Word | Formatação |
| --- | --- | --- |
| Endereçamento ao juízo | Título | 14 pt, negrito, navy |
| Nome da peça | Subtítulo | 18 pt, Lato Black, navy |
| Texto corrido | Normal | 12 pt, ink, justificado |
| Tópico | Título 1 | 14 pt, negrito itálico, navy, numeração "1.", recuo deslocado 0,5 cm |
| Subtópico | Título 2 | 12 pt, navy, numeração "a.", recuo deslocado 0,5 cm |
| Citação, ementa de precedente e ementa da própria peça | Título 3 | 12 pt, Lato Light, recuo esquerdo 4 cm (2268 twips), entrelinha simples |
| Destaque simples | Título 4 | 12 pt, blue |
| Destaque forte | Título 5 | 12 pt, Lato Black, blue |
| Observação interna | Título 6 | 11 pt, itálico, muted, 12 pt antes e 4 pt depois |
| Alínea | Título 7 | 12 pt, ink, número navy "i.", recuo esquerdo 2 cm (1134) e deslocado 1 cm (567) |
| Cláusula | Título 8 | 12 pt, negrito, navy, numeração "Cláusula 1ª –" |
| Rótulo de campo | Estilo de caractere Rótulo | negrito, navy |
| Abertura de argumento | Estilo de caractere Abertura de argumento | blue |
| Ênfase | Estilo de caractere Ênfase | navy |
| Ênfase forte | Estilo de caractere Ênfase forte | negrito, navy |
| Nota de rodapé | Texto de nota | 10 pt, ink, entrelinha simples |

Numeração em lista de vários níveis: nível 1 ligado ao Título 1 (decimal "1."), nível 2 ao Título 2 (letra minúscula "a.", reinicia após o nível 1), nível 3 ao Título 7 (romano minúsculo "i.", reinicia após o nível 2). Tópicos e subtópicos: número na margem (0 cm) e texto a 0,5 cm (283 twips), com as linhas seguintes alinhadas ao texto. Alíneas: número a 1 cm (567) e texto a 2 cm (1134), com uma linha em branco entre as alíneas. Nunca digite números à mão (exceto cláusulas no Google Docs). Todos os títulos com "manter com o próximo" e "manter linhas juntas".

## Destaques dentro do parágrafo

- Abertura de argumento: a frase que abre o parágrafo e enuncia a tese vai em Abertura de argumento (blue). Use uma por parágrafo, no máximo.
- Ênfase: expressão importante dentro da frase, em navy.
- Ênfase forte: trecho decisivo, em negrito navy. Padronize sempre em navy; não use negrito preto.
- Nunca sublinhe nem use caixa alta para destacar, salvo a ementa transcrita.

## Citação, ementa e notas de rodapé

- Introduza o bloco com uma linha de rótulo em negrito itálico ("Súmula 84 do STJ"), no texto corrido.
- Escreva a citação ou a ementa em Título 3, justificada, sem aspas. Na ementa, mantenha a caixa alta do original e ponha o trecho decisivo em Ênfase forte.
- Chame a nota de rodapé ao final do bloco.
- **Ementa da própria peça.** O parágrafo que começa com "EMENTA:" (no Markdown, `**EMENTA:** …`, entre o endereçamento e a qualificação) vai em Título 3, com recuo esquerdo de 4 cm, mesmo sem `>` no Markdown. "EMENTA:" fica em Rótulo (negrito navy), e o resto em Lato Light, sem caixa alta, sem rótulo acima e sem nota de rodapé. Não é parágrafo Normal.
- Nota de precedente em padrão ABNT, 10 pt, ink, entrelinha simples: "BRASIL. Superior Tribunal de Justiça. Corte Especial. **Súmula n. 84**. Julgada em: 18 jun. 1993. Publicada no DJ em: 2 jul. 1993." Para acórdão: "BRASIL. Superior Tribunal de Justiça. Segunda Turma. **Recurso Especial n. 1.640.698/SP (2016/0064188-4)**. Relator: Ministro Herman Benjamin. Julgado em: 27 jun. 2017. Publicado no DJe em: 30 jun. 2017."
- Só a espécie e o número vão em negrito. Abrevie os meses. Súmula leva julgamento e publicação; acórdão acrescenta o relator (e o relator para o acórdão, quando houver).
- A petição revisada recua a primeira linha da citação em 4 cm além do recuo esquerdo de 4 cm. Trate como a confirmar: aplique só se o usuário pedir ou se o modelo dele já tiver esse recuo.

## Tabela

Estilo "Quadro AMN". Cabeçalho com fundo navy, texto branco, negrito, 11 pt, repetido a cada página. Células em 11 pt, margens internas de 60 twips (vertical) e 100 (horizontal), só linha horizontal fina em #666666, sem bordas verticais, linhas que não se partem entre páginas. Texto à esquerda, números à direita. Fonte dos dados em nota de rodapé.

Quadro de cronologia da peça: colunas Data (1500 twips), Fato (5338) e Prova (2800).

## Espaçamento

O padrão não usa espaço antes ou depois dos parágrafos. Separe blocos com uma linha em branco (parágrafo vazio de verdade). Exceção: Título 6. Justifique tudo; não centralize títulos. A única exceção é a data do ofício, alinhada à direita.

- Entre qualquer título (Título 1, 2, 7 e 8) e o parágrafo que vem depois, deixe uma linha em branco. Título colado no texto é erro.
- Entre parágrafos de texto corrido, deixe uma linha em branco.
- Entre o fim de uma seção e o título seguinte, deixe uma linha em branco.
- Parágrafo vazio entre blocos é esperado e não deve ser removido na revisão. O que o passo 5 de "Como trabalhar" proíbe é parágrafo vazio dentro do texto de um título.
- Peça de primeira instância: cinco linhas em branco depois do endereçamento, para o protocolo. Se houver ementa da peça, ela vem depois dessas cinco linhas, seguida de uma linha em branco antes da qualificação.
- Peça dirigida a Tribunal: endereçamento, duas linhas em branco, bloco de identificação do processo (rótulo e dado), três linhas em branco, nome da peça, "em face de…" e vocativo.
- Vocativo ("Egrégio Tribunal," e similares): recuos de 720 twips à esquerda e de primeira linha.

## Estrutura por tipo de documento

**Peça processual** (inicial, contestação, alegações, recursos): Título (endereçamento), linhas em branco (ver "Espaçamento"), ementa da peça em Título 3 quando o texto a trouxer (seguida de linha em branco), qualificação em Normal com o nome da parte em negrito e a fórmula de apresentação terminando no verbo da peça, Subtítulo com o nome da peça, "na forma a seguir.", Títulos 1 numerados (Dos Fatos, Do Direito, Dos Pedidos), fecho com assinatura. Títulos de tópico no formato "Da/Do/Dos…"; subtópicos como frases completas que enunciam a tese. Remeta a tópicos assim: "tópico 6, subtópico a".

**Peça com petição de encaminhamento** (recurso que sobe com contrarrazões, por exemplo): duas partes, cada uma com seu endereçamento, corpo, fecho e assinatura. A primeira é a petição de encaminhamento, curta, ao juízo de origem. A segunda é a peça de mérito, ao Tribunal. A quebra de página vem logo depois da assinatura da primeira.

**Parecer ou memorando**: Subtítulo com o nome do documento, campos em linhas seguidas sem linha em branco (Para, De, Assunto, Data, com o rótulo em Rótulo), linha em branco, Títulos 1 numerados (Consulta, Análise, Conclusão). Sem endereçamento ao juízo.

**Contrato, procuração, termo**: Subtítulo com o nome, partes em negrito e frase que remete às cláusulas, Título 8 por cláusula ("Do objeto", "Do prazo"), incisos em Título 7, assinatura de cada parte.

**Ofício e carta**: número em Rótulo, local e data à direita, destinatário com o nome em negrito, assunto em Rótulo, vocativo, texto, fecho ("Atenciosamente,") e assinatura.

**Fecho e assinatura**: "Termos em que, pede deferimento.", linha em branco, "Cidade - UF, dd de mês de aaaa.", duas linhas em branco, nome do advogado em negrito navy, "OAB/UF nº 00.000" em Lato Light 11 pt. Sem linha de assinatura desenhada. Tudo alinhado à esquerda. Todas as linhas do bloco com "manter com o próximo", menos a última, para a assinatura não ficar sozinha em outra página.

## Como trabalhar

1. Identifique o tipo de documento e use a estrutura correspondente. Se o tipo não estiver claro, pergunte uma vez.
2. Use os dados e o texto fornecidos. Faltando nome, data, OAB ou número, deixe o campo evidente ("00 de mês de 0000", "OAB/UF 00.000") e avise na resposta. Não invente fatos, números de processo, precedentes ou nomes. Precedente sem dados completos fica com campo evidente na nota.
3. Aplique apenas estilos do padrão. Nunca formate à mão, salvo o que o Google Docs exige (ver Destino). Se faltar um nível, diga ao usuário.
4. Gere o .docx, converta em PDF, rasterize e olhe cada página: numeração (1., a., i.), margens, linha em branco entre cada título e o texto, quebras de página, títulos sozinhos no fim da página, tabela com cabeçalho em navy, notas de rodapé, assinatura inteira numa página, realce amarelo em todas as marcas de pendência.
   - **Numeração gerada pela biblioteca `docx`:** o Word pode desenhar a numeração errada (por exemplo, "1." no lugar do tópico 8 depois de subtópicos) mesmo com o XML correto e a contagem interna certa. Se o Word estiver disponível, abra o arquivo nele, salve de novo como .docx e só então converta em PDF e entregue. Confira o número de cada tópico na página rasterizada, não no XML.
   - **Recuo da ementa e das citações:** no XML, o parágrafo que começa com "EMENTA:" e todo bloco que veio de `>` no Markdown têm de trazer `<w:ind w:left="2268"/>` no próprio `w:pPr`. Conte os parágrafos com esse recuo no `document.xml` e compare com o número de parágrafos citados (cada parágrafo de bloco `>`, separados por linha `>` vazia) mais um da ementa. Ementa sem recuo é erro.
   - **Linha em branco depois de título:** o parágrafo vazio que separa o título do texto também leva "manter com o próximo"; sem isso, o título fica sozinho no pé da página.
5. Revise o texto antes de entregar: colchetes de modelo esquecidos ("[data da ciência]"; marca de pendência não é esquecimento: fica, com realce), datas incoerentes entre o início e o fecho, parágrafos vazios dentro de títulos, precedentes citados sem nota de rodapé e remissões a tópicos que não existem.
6. Entregue o arquivo e, na resposta, diga em uma ou duas frases o que foi feito e o que ficou como campo a preencher.

## Estilo de redação

Voz formal, terceira pessoa, frases claras de tamanhos variados. Sem emojis. Sem travessões em excesso. Sem clichês de texto gerado por IA. Corrija "1a" para "1ª" e confira concordâncias comuns em fórmulas de abertura ("nos autos", não "neste autos").