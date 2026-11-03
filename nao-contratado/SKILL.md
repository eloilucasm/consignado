---
name: nao-contratado
description: Redige a petição inicial de empréstimo consignado do INSS NÃO CONTRATADO (contrato que o beneficiário nega ter firmado), contra banco, para processos da ficha de ajuizamento (blocos B, C e Caixa). Confere o extrato do INSS, calcula descontos, dobro e valor da causa, pergunta o rito (JEC ou Justiça Comum) e a cidade do fecho, aplica a checagem pré-recurso e entrega minuta em Markdown para a tipografia-azul. Acione com "não contratado", "inicial de consignado", "não reconheço o empréstimo", "descontos que não autorizei", "inicial contra a Caixa", ou ao receber a ficha de um cliente. Não use para contrato migrado, Tese 1000 ou refinanciamento de cartão RMC/RCC, nem para recurso.
---

# Inicial de consignado não contratado

Redige a inicial de **inexistência de relação obrigacional cumulada com repetição do indébito, obrigação de fazer e dano extrapatrimonial**, para o contrato consignado que o beneficiário do INSS nega ter firmado. Fontes consultadas em 28/10/2026. Toda peça é minuta: o advogado revisa e assina.

Leia `protocolo/protocolo.md` (regras comuns, portões e marcas) e `assets/padrao-pecas.md` (forma e pedidos de rotina) antes de redigir.

## Abertura e triagem progressiva

1. Peça só o que falta: ficha de ajuizamento (saída da triagem), extrato do INSS do NB do processo, termo, análise e qualificação do autor. Extraia dos documentos antes de perguntar.
2. Monte o **quadro de fatos** (`protocolo/quadro-de-fatos.md`) e mostre o Painel do Caso. Pergunte no máximo **três lacunas por rodada**.
3. **Antes de gerar, pergunte sempre ao advogado:** (a) o rito, **JEC ou Justiça Comum** (você pode sugerir pelo valor e pela necessidade de prova, mas não escolhe); (b) a **cidade e a UF do fecho**. Pergunte também, sem contar nas três lacunas, se o cliente trouxe o **extrato bancário do mês da averbação** e se o banco **entregou contrato ou trilha antes da ação**; passe as respostas ao script (`--rito jec|comum`, `--extrato-bancario sim|nao`, `--dossie-pre-acao`). O extrato bancário é **recomendado**, não obrigatório: sem ele, registre a pendência e o advogado decide se ajuíza. Se ele mostrar crédito ligado ao contrato, use o bloco `[[SE CRÉDITO EM CONTA]]` do modelo (subtópico dos fatos e pedido 7): a peça reconhece o lançamento, nega a contratação e deixa a marca `[DECISÃO DO ADVOGADO: devolução, depósito em juízo ou compensação]`; nunca escolha por ele.
4. Só entram contratos que estão **na análise e no termo**. Contrato fora do termo não se ajuíza e não se pergunta.

## Cálculo

No Cowork, rode os scripts e **confira por segunda via**:

```
python3 scripts/calcular.py --ficha ficha.json --processo N --extrato extrato.pdf --data AAAA-MM-DD --saida pasta/ [--rito jec|comum] [--extrato-bancario sim|nao] [--dossie-pre-acao]
```

Eles leem o extrato (`scripts/extrato.py`, requer `pip install pypdf`), contam descontos, calculam dobro e valor da causa e gravam `calculo.json` e `calculo.md`. Sem execução de código, faça a tabela à mão, refaça por outro caminho e marque `CÁLCULO A CONFERIR`. O extrato novo deve ter a primeira leitura conferida contra o PDF: o leitor foi herdado do pacote AMN e só foi testado aqui com extrato fictício.

## Entrega e portões

Preencha `assets/modelo-inicial-nao-contratado.md` com o quadro de fatos e o `calculo.json`. Ao fim da resposta, registre os quatro portões do protocolo (passou, pendente ou bloqueado). O portão 3 inclui a **checagem pré-recurso** (FSC1 a FSC12, `assets/escrutinio-fsc-vf.md`; o registro fica em `checagem-fsc-vf.md`), que está em `assets/padrao-pecas.md`, seção 9. Dois portões falhos seguidos: entregue só o diagnóstico ou minuta `BLOQUEADO PARA USO FINAL`.

**Bloqueios específicos:** contrato fora do termo; extrato de outro NB; contrato de bloco B ou C **ativo** no extrato (anomalia: mostre ao advogado antes de seguir); réu sem cadastro em `references/dados/reus.json` (CNPJ e endereço `[CONFERIR]`); rito ou cidade do fecho não informados.

## Peças e arquivos

| Arquivo | Para quê |
|---|---|
| `assets/modelo-inicial-nao-contratado.md` | modelo da inicial, com condicionais por rito, tutela, prescrição e litispendência |
| `assets/padrao-pecas.md` | endereçamento, qualificação, pedidos de rotina, precedentes e revisão |
| `assets/escrutinio-fsc-vf.md` | FSC1 a FSC12 e VF1 a VF9 antes do ajuizamento e formato do registro |
| `references/01-tese-e-roteiro.md` | a tese, os gatilhos e as perguntas típicas |
| `references/02-mudancas-no-modelo.md` | o que mudou em relação ao modelo AMN v1.4 e por quê |
| `references/dados/` | réus (CNPJ e endereço), comarcas do TJBA e subseções do TRF1 |
| `testes/caso-ficticio/` | caso fictício completo para teste |

O juízo vem das tabelas de `references/dados/`, nunca de memória. Réu **Caixa**: Vara Federal. Demais: comarca do TJBA.

## Normas e jurisprudência

Estão em `references/normas/` (texto literal e datado) e `references/jurisprudencia/`. A lista do que **não** cobre está em `protocolo/fontes-e-limites.md`; leia antes de concluir sobre aquela matéria. **Não use o Tema 929/STJ como fundamento** (o acórdão ainda não foi publicado e cabem embargos). A dobra se apoia no texto do art. 42, parágrafo único, do CDC; o escritório atualizará quando o acórdão sair.

## Como buscar norma e precedente

1. **Norma:** abra `references/normas/INDEX.md` (para que serve cada norma). Para achar o artigo **pelo conteúdo**, use `references/normas/MAPA.md` (um dispositivo por linha, com a linha do arquivo); para achar por Livro, Título ou Capítulo, `references/normas/ESTRUTURA.md`. Com execução de código (Cowork), leia só a janela (`Read offset/limit` ou `grep -n "^Art. N"`). No chat, sem execução, procure no arquivo o número do artigo (`Art. N`).
2. **Precedente:** abra `references/jurisprudencia/INDEX.md`, que lista os precedentes **por assunto da peça** e avisa quais o banco pode invocar. Abra só o precedente que vai citar.
3. Cite apenas o que está nesses arquivos. O que não está vira `[CONFERIR]`.

## Formatação

Entregue Markdown. Ofereça gerar o Word com a skill `tipografia-azul`, com **realce amarelo** nas marcas de pendência (decisão do escritório; a `tipografia-azul` ainda não descreve o realce, então passe a instrução junto).
