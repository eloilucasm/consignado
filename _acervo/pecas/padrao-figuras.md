# Padrão das figuras das peças — consignado

Vale para toda figura (diagrama, linha do tempo, quadro em imagem) que uma skill do pacote gera para entrar numa peça. O desenho segue `scripts/figuras.py`: use os blocos de lá em vez de desenhar à mão, e a figura sai neste padrão. Em conflito, prevalece este arquivo. Hoje gera figura: `tese-1000` (`scripts/diagramas_1000.py`) e `rmc` (`scripts/diagramas_rmc.py`).

## 1. Tamanho

- **17 cm de largura a 300 dpi (2008 px).** É a largura útil da página A4 da `tipografia-azul` (21 cm menos as margens de 2 cm). A altura acompanha o conteúdo.
- **Insira na peça com 17 cm de largura, sem redimensionar.** Se a imagem for reduzida no Word, a fonte encolhe junto.
- O verificador do pacote reprova PNG de figura (`fig_*.png`) fora de 2008 px e 300 dpi.

## 2. Fonte

Lato, como na peça. Tamanhos em pt **no papel** (o corpo da peça é 12 pt):

| Uso | Tamanho |
|---|---|
| Título (faixa azul, caixa alta, negrito) | 12 pt |
| Título de caixa | 11 pt, negrito |
| Número de contrato em destaque | 13 pt, negrito (reduz até 10 pt se não couber) |
| Texto, rótulos, subtítulo | 10 pt |
| Rodapé (fonte do dado) e número do marco | 9 pt |

**Nada abaixo de 9 pt.** O módulo não gera fonte menor que isso.

## 3. Cores

Da `tipografia-azul`: azul-marinho (#1F2A44) para a estrutura (faixa do título, caixas, marcos neutros); **vermelho (#B3261E) só para o que a figura quer provar** (o sufixo do derivado, a reaverbação, o período dos descontos); cinza (#6B7079) para o rodapé e os traços neutros. Fundo branco.

## 4. Composição

- **Nada sobreposto.** O texto quebra linha dentro do espaço dele; nenhum rótulo fica em cima de seta, caixa ou outro rótulo. O que liga duas caixas vai numa faixa de destaque abaixo delas, em largura total, e não sobre a seta.
- Caixas lado a lado têm a mesma altura e o mesmo título curto (o detalhe vai na primeira linha do texto), para que os números fiquem alinhados.
- **Linha do tempo: marcos com espaço igual, em ordem cronológica, numerados.** Não use escala proporcional ao tempo: marcos que distam dias se amontoam e um período de meses ocupa o eixo todo. O tempo entre dois marcos vai escrito sobre o eixo ("9 dias", "mesmo dia", "1 ano e 4 meses"); intervalo acima de 60 dias, em anos e meses.
- **Gráfico (bloco `grafico`):** linha mês a mês em largura total, com grade leve. Nada escrito dentro da área do gráfico: os valores do eixo vão à esquerda, o rótulo da referência horizontal (ex.: "200%") à direita, e cada marco vertical recebe um número numa faixa acima da área, explicado na legenda (bloco `legenda`) abaixo. Mês ausente no documento interrompe a linha (não se interpola) e é dito na legenda. O fundo vermelho-claro marca só o período que a figura prova.
- Uma frase de conclusão, em negrito, depois do desenho (por exemplo: "Reaverbado 1 dia depois da exclusão da raiz.").

## 5. Recorte de documento

Recorte (bloco `documento`) é a imagem do próprio documento, rasterizada do PDF, para provar um lançamento (ex.: a linha do cartão e a competência do refinanciamento no extrato do INSS).

- O trecho é achado pelas coordenadas do texto no PDF, nunca à mão livre. Inclui o cabeçalho da tabela só se ele estiver logo acima; não se emendam pedaços distantes da página.
- **Só reproduz o documento.** Nada é escrito por cima; o único acréscimo permitido é **um** contorno vermelho discreto em volta da linha que a figura prova. Sem marca-texto, setas ou traços.
- Largura total da figura (17 cm a 300 dpi). A letra do recorte é a do documento: o mínimo de 9 pt vale para o que a figura escreve (título, frase, rodapé), não para o documento reproduzido.
- Rodapé: "Fonte: Histórico de Empréstimo Consignado do INSS, anexo", com a página, e a nota de que só o contorno foi acrescentado. Extrato digitalizado (sem texto): o recorte não sai automaticamente; faça-o à mão no mesmo padrão.

## 6. Texto

- Plural certo: "1 dia", "17 parcelas", nunca "dia(s)" ou "parcela(s)".
- Valor com "R$" junto do número (espaço inseparável): "R$ 12,20" não se parte na quebra de linha.
- Datas como no documento de origem (dd/mm/aaaa; competência em mm/aaaa, com a palavra "competência").
- Sem marca de pendência (`[CONFERIR]`, `[DECISÃO DO ADVOGADO]`) dentro da figura: pendência fica no texto da peça.

## 7. Fonte do dado

- Rodapé com a origem e (nas figuras desenhadas) a frase "Figura elaborada a partir do extrato; não introduz fato novo."
- **Na inicial, o documento é citado como anexo, sem ID**: o processo ainda não existe. Em peça de processo em curso (réplica, recurso), cite o ID e a página.
- A figura só reproduz o que está no documento. Nada de dado inferido ou de outro processo.

## 8. Na peça

- Cada figura entra logo depois do parágrafo que a anuncia, com legenda "Figura N: …" (a legenda vem do `figuras.json`).
- A figura ilustra; o argumento continua no texto.
- Entregue os PNG junto com a minuta.
