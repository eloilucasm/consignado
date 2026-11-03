# Rotina de manutenção do pacote de consignado

Todos os comandos a partir de `consignado-pacote/`. Node 18+ e Python 3 (com `pypdf` só para ler extrato).

## Alterar um arquivo que se repete entre skills (norma, jurisprudência, protocolo, padrão de peças, dados, `extrato.py`)

1. Edite **no acervo** (`_acervo/...`), nunca na cópia da skill.
2. `node _manutencao/sincronizar-acervo.js` mostra o que mudaria (iguais, faltam, diferem). Não grava nada.
3. `node _manutencao/sincronizar-acervo.js --aplicar` copia para as skills. O arquivo antigo vai para `_manutencao/backup-sincronizacao/<data-hora>/`. Nada é apagado.
4. Se mudou uma norma: `node _manutencao/gerar-estrutura.js` e `python3 _manutencao/gerar-mapa.py` (os números de linha do sumário e do mapa mudam). Se um modelo passar a citar artigo novo do Código Civil ou do CPC, acrescente o número em `SELETIVO` no `gerar-mapa.py`.
5. `node _manutencao/verificar-pacote.js --detalhe`. Só entregue com **0 erros**.

Editou direto numa skill por engano: `node _manutencao/sincronizar-acervo.js --trazer <skill> <pasta/arquivo>` leva a edição de volta ao acervo.

## Índice da jurisprudência por assunto

A curadoria está em `_manutencao/gerar-indice-jurisprudencia.py` (lista `DADOS`). Para acrescentar um precedente: ponha o arquivo no acervo (`--incluir`), acrescente a linha em `DADOS`, rode `python3 _manutencao/gerar-indice-jurisprudencia.py` e depois o verificador (ele reprova citação de precedente que não exista ou, no FONAJE, esteja revogado).

## Nova norma ou nova jurisprudência

1. Baixe do site oficial e converta. **Planalto:** acrescente a norma à lista `NORMAS` de `_manutencao/coleta/coletar_planalto.py` e rode `python3 -I _manutencao/coleta/coletar_planalto.py --saida <pasta de preparo> <nome>`; ele grava no formato do acervo, mantém o riscado (`<strike>`, `<s>`, `<del>` e `line-through`) e confere o resultado palavra a palavra contra o HTML (APROVADA/REPROVADA; reprovada não entra no acervo). O `planalto-converter.js` não reconhece o riscado por `style="text-decoration:line-through"`; não o use. **PDF:** `pdftotext -enc UTF-8` (sem `-enc`, o Windows grava Latin-1). **Banco Central:** a API pública do portal de normativos devolve texto e status. **Jurisprudência do STJ:** `python3 -I _manutencao/coleta/coletar_jurisprudencia.py --saida <pasta> stj-temas stj-sumulas` (texto e situação do BNP/CNJ, caderno em PDF e CSV de dados abertos, cruzados entre si); **STF:** `... stf` (súmulas cruzadas com o caderno oficial; vinculantes e repercussão geral só pelo BNP); outros órgãos: `bnp:ORGAO:TIPO` (ver `--bnp-listar`). O BNP corta a tese perto de 4.000 caracteres: o coletor marca o registro e, nos temas do STJ, usa o CSV.
2. Prove a integridade: `node _manutencao/comparar-fonte.js --html pagina.htm --md convertido.md --nome X` (a passada só com letras evita falso ausente por linha quebrada). O `coletar_planalto.py` já faz a conferência do riscado; este teste continua obrigatório.
3. Cabeçalho do arquivo (**front matter YAML obrigatório**): norma = `ato_data`, `publicacao_dou`, `vigencia`, `situacao`, `fonte`, `consulta`; julgado = `data_julgamento`, `data_publicacao_acordao`, `situacao`, `fonte`, `consulta`. Acrescente a entrada em `NORMAS_DADOS`/`FICHAS` de `_manutencao/cabecalhos.py` e rode `python -I _manutencao/cabecalhos.py --gravar` (confere o ato contra o texto; sai com código 1 se faltar campo). Depois `python -I _manutencao/gerar-datas-citaveis.py`, `node _manutencao/gerar-estrutura.js` e `gerar-mapa.py`, porque o cabeçalho desloca as linhas. Corpo do arquivo: fonte (URL), data da consulta, recorte, limites. Atualize `_acervo/fontes-e-limites.md` e o nível no `PAINEL.md` (VERIFICADO, FEITO, PRESUMIDO, ABERTO).
4. Acrescente ao manifesto: `node _manutencao/sincronizar-acervo.js --incluir <skill> normas/<arquivo>.md`.

## Nova skill do pacote

1. Crie a pasta com `SKILL.md` (name igual à pasta) e copie os arquivos do acervo com `--incluir`.
2. Tire a skill de `nomes.planejadas` em `verificador.config.js`.
3. Rode os passos 4 e 5 acima.

## Quando uma regra do verificador muda

`python3 _manutencao/testar-verificador.py --tmp <pasta temporária>` copia o pacote, aplica 28 defeitos, um por vez, e confere que cada um reprova com a mensagem certa. **Cada erro que aparecer duas vezes vira regra nova** em `verificador.config.js`, com um caso novo em `testar-verificador.py`.

## Teste da skill rmc

`python3 rmc/testes/caso-ficticio/teste.py` gera um extrato fictício de cartão, calcula (marco de 200%, dobro, valor da causa) e confere que a variante com refinanciamento antes do prazo de 90 dias sai com o bloqueio B2.

## Teste da skill migrado

`python3 migrado/testes/caso-ficticio/teste.py` gera um extrato fictício com contratos migrados do banco 934 (dois excluídos, um ativo que também aparece no banco anterior) e um contrato sem origem de migração, e confere os números, a troca de titularidade com e sem `--incluir-outros-bancos` e a norma na fronteira de 13/12/2022.

## Teste da skill tese-1000

`python3 tese-1000/testes/caso-ficticio/teste.py` gera um extrato fictício e calcula cinco processos (derivado excluído sob a IN 28; derivado ativo sob a IN 138; dois derivados da mesma raiz; troca de titularidade com e sem `--incluir-outros-bancos`; derivado antes da exclusão da raiz), além da fronteira de 13/12/2022.

## Teste do piloto

`python3 nao-contratado/testes/caso-ficticio/teste.py` gera um extrato fictício, lê, calcula e confere os números.

`python3 nao-contratado/testes/casos-reais/teste_extenso.py` confere o valor por extenso do `calcular.py` contra 74 valores reais de petições do escritório.

## Calendário de vigilância (a preencher no painel)

- Tema 929/STJ: publicação do acórdão e da tese.
- MP 1.393/2026: conversão ou perda de eficácia (a partir de 23/11/2026).
- IN INSS 138/2022: novas alterações (consolidação do INSS).
- Súmulas do TJBA: sessões posteriores a 10/11/2025.
- Salário mínimo: valor para o limite de 40 salários do JEC.

## Tabela de unidades do TJBA (endereçamento)

`_acervo/dados/tjba_unidades.json` e `territorial-tjba.md` saem de `_manutencao/coleta/tjba/` (versão de 03/11/2026). Para refazer, numa pasta de preparo:
1. Baixe o quadro das Varas do Sistema dos Juizados (Portal dos Juizados) e as relações de magistrados por entrância (final do interior, intermediária, inicial; página "Relação de magistrados" do TJBA), e extraia o texto com PyMuPDF (`quadro.txt`, `rel-final-int.txt`, `rel-intermediaria.txt`, `rel-inicial.txt`).
2. `python parse_quadro.py quadro.txt unidades.json`; `python cruzar.py <pasta> <pacote>`; `python gerar_doc.py <pasta> <pacote> <pacote>/_acervo/dados/territorial-tjba.md` (grava também `tjba_unidades.json`).
3. Confira as comarcas da seção 4 do documento e as linhas com `[CONFERIR]`, depois `sincronizar-acervo.js --aplicar` e o verificador.

Quando o TJBA publicar nova Relação Municípios x Comarca, atualize antes o `tjba_comarcas.json`. Salvador (Juizados do Consumidor e Varas de Relações de Consumo) está fixo no `gerar_doc.py`: confira no Portal dos Juizados e na relação da entrância final da capital.

## Transcrição literal

O verificador confere todo trecho entre aspas ou em bloco `> ` atribuído a norma ou precedente nos `assets/modelo-*.md` e nas peças de `testes/**/saida/` (`inicial*`, `replica*`, `recurso*`): cada pedaço (separado por `(...)`) tem de existir, só com as letras, no arquivo do acervo da skill (`extras.transcricoes` em `verificador.config.js`; normalização em `_manutencao/normalizar.js`). Ementa de precedente sem arquivo no acervo reprova. Norma nova citada nos modelos: acrescente a regex do nome e o arquivo em `transcricoes.normas`.

## Linha do tempo e mapa de argumentos

`escrutinio.eventos_dos_contratos()` + `escrutinio.cronologia()` montam a linha do tempo; cada `calcular*.py` acrescenta os eventos da tese e passa a `gravar(..., cronologia)`. Os testes de caso fictício conferem a ordem e os eventos-chave. Na réplica, `fichas.py` grava `mapa-argumentos.json/.md` a partir de `pontos` do `contestacao.json` e do catálogo `references/02-defesas-do-banco.md`; o verificador reprova ponto sem resposta ou sem pedido e, com a peça na mesma pasta, pedido do mapa que não esteja em "Dos pedidos". Linha nova no catálogo que leve a pedido diferente de "procedência": acrescente em `PEDIDO_POR_DEFESA` do `fichas.py`.

## Escrutínio FSC e VF

`python3 _acervo/scripts/escrutinio.py --teste` roda o autoteste do módulo. Cada `calcular*.py` grava `checagem-fsc-vf.md` e `dossie-do-caso.json` ao lado do `calculo.json`; o verificador exige o registro ao lado de cada peça de exemplo (`testes/**/saida/`), as 12 linhas FSC e as 9 linhas VF, o FSC3 na peça, o FSC9 conforme o rito e a negativa específica de cada contrato. Para regenerar os registros de exemplo, rode cada script de cálculo sobre o extrato fictício e copie os dois arquivos para `saida/`.
