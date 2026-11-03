---
name: tese-1000
description: Redige a petição inicial da Tese 1000 Contra: contrato derivado com sufixo numérico (_0001, _0002…) averbado no INSS sobre o número-raiz de um contrato já excluído, sem nova contratação, com ação de inexistência, repetição em dobro e dano extrapatrimonial. Lê o extrato do INSS, localiza o derivado e a raiz, mede o intervalo entre exclusão e reinclusão, calcula descontos, dobro e valor da causa, escolhe a norma pela data da reaverbação (IN 28/2008 até 12/12/2022; IN 138/2022 desde 13/12/2022), pergunta o rito (JEC ou Justiça Comum) e a cidade do fecho e entrega minuta em Markdown para a tipografia-azul. Acione com "tese 1000", "1000 contra", "contrato derivado", "reaverbação com sufixo", "número-raiz". Não use para contrato não contratado comum, migrado ou refinanciamento de cartão RMC/RCC, nem para recurso.
---

# Inicial da Tese 1000 Contra

Redige a inicial de **inexistência de relação jurídica cumulada com repetição do indébito em dobro, obrigação de fazer e dano extrapatrimonial**, para o contrato **derivado** (número-raiz + sufixo) que o banco averbou depois de excluir o contrato-raiz, sem nova contratação. Fontes consultadas em 28/10/2026. Toda peça é minuta: o advogado revisa e assina.

Leia `protocolo/protocolo.md` (regras comuns, portões e marcas) e `assets/padrao-pecas.md` (forma e pedidos de rotina) antes de redigir. Leia `references/01-tese-e-roteiro.md`: ela explica a tese, a escolha da norma pela data e o que a peça **não** pode afirmar.

## Abertura e triagem progressiva

1. Peça só o que falta: ficha de ajuizamento, extrato do INSS do NB do processo, qualificação do autor. Extraia dos documentos antes de perguntar.
2. Monte o **quadro de fatos** (`protocolo/quadro-de-fatos.md`) e mostre o Painel do Caso. No máximo **três lacunas por rodada**.
3. **Antes de gerar, pergunte sempre ao advogado:** (a) o rito, **JEC ou Justiça Comum**; (b) a **cidade e a UF do fecho**. Pergunte também, sem contar nas três lacunas, se o cliente trouxe o **extrato bancário do mês da averbação** e se o banco **entregou contrato ou trilha antes da ação**; passe as respostas ao script (`--rito jec|comum`, `--extrato-bancario sim|nao`, `--dossie-pre-acao`). O extrato bancário é **recomendado**, não obrigatório: sem ele, registre a pendência e o advogado decide se ajuíza. Se ele mostrar crédito ligado ao contrato, use o bloco `[[SE CRÉDITO EM CONTA]]` do modelo (subtópico dos fatos e pedido 7): a peça reconhece o lançamento, nega a contratação e deixa a marca `[DECISÃO DO ADVOGADO: devolução, depósito em juízo ou compensação]`; nunca escolha por ele.
4. **Leia o extrato antes de gerar.** Veja o contrato-raiz e o derivado e procure o que a narrativa padrão não cobre: derivado depois refinanciado, vários derivados (_0002, _0003) de uma mesma raiz, valor liberado incomum. Escreva só o que o extrato mostra e avise o advogado de que o parágrafo é seu.

## Cálculo

No Cowork, rode e **confira por segunda via**:

```
python3 scripts/calcular_1000.py --ficha ficha.json --processo N --extrato extrato.pdf --data AAAA-MM-DD --saida pasta/ [--rito jec|comum] [--extrato-bancario sim|nao] [--dossie-pre-acao]
python3 scripts/diagramas_1000.py --calculo pasta/calculo.json --saida pasta/figuras --fonte "ID __, p. __"
```

O script lê o extrato (`scripts/extrato.py`, requer `pip install pypdf`), acha cada derivado e a sua raiz, mede o intervalo entre a exclusão da raiz e a averbação do derivado, conta os descontos, calcula o dobro e o valor da causa e grava `calculo.json` e `calculo.md`. Se o mesmo derivado aparece em **outro banco** (troca de titularidade), o script **não soma** os descontos do outro banco e alerta; só a decisão do advogado liga `--incluir-outros-bancos`. Sem execução de código, faça a tabela à mão e marque `CÁLCULO A CONFERIR`. O leitor do extrato foi herdado do pacote AMN e só foi testado aqui com extrato fictício: confira a primeira leitura real contra o PDF.

## Entrega e portões

Preencha `assets/modelo-inicial-tese-1000.md` com o quadro de fatos e o `calculo.json`. Ao fim, registre os quatro portões do protocolo. O portão 3 inclui a **checagem pré-recurso** (FSC1 a FSC12, `assets/escrutinio-fsc-vf.md`; o registro fica em `checagem-fsc-vf.md`). Dois portões falhos seguidos: entregue só o diagnóstico ou minuta `BLOQUEADO PARA USO FINAL`.

**Bloqueios específicos:** nenhum derivado no extrato; mesmo número em outro banco (fora do escopo: na Tese 1000 o contrato não é reaverbado por outro banco; verifique se é o caso de migrado); contrato-raiz não localizado; derivado averbado **antes** da exclusão da raiz (rever a narrativa); mais de uma raiz no processo; réu sem cadastro em `references/dados/reus.json`; rito ou cidade do fecho não informados.

## Peças e arquivos

| Arquivo | Para quê |
|---|---|
| `assets/modelo-inicial-tese-1000.md` | modelo da inicial, com condicionais por rito, data da reaverbação, tutela, prescrição e litispendência |
| `assets/padrao-pecas.md` | endereçamento, qualificação, pedidos de rotina, precedentes e revisão |
| `assets/escrutinio-fsc-vf.md` | FSC1 a FSC12 e VF1 a VF9 antes do ajuizamento e formato do registro |
| `references/01-tese-e-roteiro.md` | a tese, a escolha da norma pela data, o que não afirmar e as perguntas típicas |
| `scripts/diagramas_1000.py` | figuras "Anatomia da reaverbação" e "Linha do tempo" (PNG) a partir do `calculo.json`; requer Pillow; entregue as imagens junto com a peça |
| `references/02-mudancas-no-modelo.md` | o que mudou em relação ao modelo do escritório (Maria x BNP) e ao AMN v1.4, e por quê |
| `references/dados/` | réus, comarcas do TJBA e subseções do TRF1 |
| `testes/caso-ficticio/` | caso fictício completo para teste |

O juízo vem das tabelas de `references/dados/`, nunca de memória. Réu **Caixa**: Vara Federal. Demais: comarca do TJBA.

## Normas e jurisprudência

Estão em `references/normas/` (texto literal e datado) e `references/jurisprudencia/`. A lista do que **não** cobre está em `protocolo/fontes-e-limites.md`; leia antes de concluir sobre aquela matéria. **Não use o Tema 929/STJ como fundamento** (o acórdão ainda não foi publicado e cabem embargos). A dobra se apoia no texto do art. 42, parágrafo único, do CDC; o escritório atualizará quando o acórdão sair.

## Como buscar norma e precedente

1. **Norma:** abra `references/normas/INDEX.md` (para que serve cada norma). Para achar o artigo **pelo conteúdo**, use `references/normas/MAPA.md` (um dispositivo por linha, com a linha do arquivo); para achar por Livro, Título ou Capítulo, `references/normas/ESTRUTURA.md`. Com execução de código (Cowork), leia só a janela (`Read offset/limit` ou `grep -n "^Art. N"`). No chat, sem execução, procure no arquivo o número do artigo (`Art. N`).
2. **Precedente:** abra `references/jurisprudencia/INDEX.md`, que lista os precedentes **por assunto da peça** e avisa quais o banco pode invocar. Abra só o precedente que vai citar.
3. Cite apenas o que está nesses arquivos. O que não está vira `[CONFERIR]`.

## Formatação

Entregue Markdown. Ofereça gerar o Word com a skill `tipografia-azul`, com **realce amarelo** nas marcas de pendência (decisão do escritório; passe a instrução junto).
