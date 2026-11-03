---
name: rmc
description: Redige a petição inicial de nulidade de refinanciamento de cartão consignado RMC/RCC (reserva de margem consignável), cumulada com repetição do indébito em dobro e dano extrapatrimonial, com a tese do marco de 200% da Lei 14.690/2023. Lê o histórico mensal do cartão no extrato do INSS, detecta o refinanciamento, monta a planilha, confere os bloqueios da tese (refinanciamento depois do prazo de 90 dias, 200% atingido antes dele, histórico completo), pergunta o rito (JEC ou Justiça Comum) e a cidade do fecho e entrega minuta em Markdown para a tipografia-azul. Acione com "RMC", "RCC", "cartão consignado", "refinanciamento do cartão", "reserva de margem", "marco de 200%", "Desenrola". Não use para empréstimo não contratado, migrado ou Tese 1000, nem para recurso.
---

# Inicial de refinanciamento de cartão consignado (RMC/RCC)

Redige a inicial de **nulidade de refinanciamento cumulada com repetição do indébito em dobro e dano extrapatrimonial**, para o cartão consignado cujo saldo o banco refinanciou depois de o beneficiário já ter pago mais de 200% do capital. Fontes consultadas em 28/10/2026. Toda peça é minuta: o advogado revisa e assina.

Leia `protocolo/protocolo.md` (regras comuns, portões e marcas) e `assets/padrao-pecas.md` (forma e pedidos de rotina) antes de redigir. Leia `references/01-tese-e-roteiro.md`: ela explica os **quatro pontos jurídicos da tese** (B1 a B4), que o script confere ou avisa.

## Abertura e triagem progressiva

1. Peça só o que falta: ficha de ajuizamento, extrato do INSS do NB do cartão, qualificação do autor. Extraia dos documentos antes de perguntar.
2. Monte o **quadro de fatos** (`protocolo/quadro-de-fatos.md`) e mostre o Painel do Caso. No máximo **três lacunas por rodada**.
3. **Antes de gerar, pergunte sempre ao advogado:** (a) o rito, **JEC ou Justiça Comum**; (b) a **cidade e a UF do fecho**; (c) se houve **ação anterior sobre esse cartão** (entra o tópico de coisa julgada); (d) se, no cartão, só o **mínimo** da fatura é descontado em folha e o restante é pago por boleto (premissa da decisão D1: por isso o art. 4º da Res. CMN 4.549 não afasta a resolução). **Não pergunte D1 nem D25: já decididas pelo escritório em 29/10/2026** (mantém-se o teto pela lei e pela Res. CMN 4.549; a ação não se enquadra na suspensão do Tema 1414, e o tópico de distinção entra sempre). Pergunte também, sem contar nas três lacunas, se o cliente trouxe o **extrato bancário do mês da averbação** e se o banco **entregou contrato ou trilha antes da ação**; passe as respostas ao script (`--rito jec|comum`, `--extrato-bancario sim|nao`, `--dossie-pre-acao`).
4. Um cartão por processo.

## Cálculo

No Cowork, rode e **confira por segunda via**:

```
python3 scripts/calcular_rmc.py --ficha ficha.json --processo N --extrato extrato.pdf --data AAAA-MM-DD --saida pasta/ [--historico-extra historico.csv] [--rito jec|comum] [--extrato-bancario sim|nao] [--dossie-pre-acao]
```

O script lê o cartão e o histórico mensal (`scripts/cartao.py`, requer `pip install pypdf`), detecta o refinanciamento, monta a planilha acumulada, acha o marco de 200%, calcula o dobro e o valor da causa e grava `calculo.json` e `calculo.md` (com a planilha pronta para colar). **Ele para** quando falta histórico, quando não há refinanciamento ou quando o marco de 200% não vem antes dele, e **avisa** quando o refinanciamento é anterior ao prazo de 90 dias do art. 2º-D da Res. CMN 4.549. Sem execução de código, faça a tabela à mão e marque `CÁLCULO A CONFERIR`.

O leitor do extrato foi herdado do pacote AMN e só foi testado aqui com extrato fictício. Confira a primeira leitura real contra o PDF.

## Entrega e portões

Preencha `assets/modelo-inicial-rmc.md` com o quadro de fatos e o `calculo.json`. Ao fim, registre os quatro portões do protocolo. O portão 3 inclui a **checagem pré-recurso** (FSC1 a FSC12, `assets/escrutinio-fsc-vf.md`; o registro fica em `checagem-fsc-vf.md`). Dois portões falhos seguidos: entregue só o diagnóstico ou minuta `BLOQUEADO PARA USO FINAL`.

**Bloqueios específicos:** histórico do cartão incompleto; nenhum refinanciamento no histórico; 200% não atingido antes do refinanciamento; mais de um cartão no mesmo processo; rito ou cidade do fecho não informados; réu sem cadastro em `references/dados/reus.json`.

## Peças e arquivos

| Arquivo | Para quê |
|---|---|
| `assets/modelo-inicial-rmc.md` | modelo da inicial, com condicionais por rito, tutela e coisa julgada |
| `assets/padrao-pecas.md` | endereçamento, qualificação, pedidos de rotina, precedentes e revisão |
| `assets/escrutinio-fsc-vf.md` | FSC1 a FSC12 e VF1 a VF9 antes do ajuizamento e formato do registro |
| `references/01-tese-e-roteiro.md` | a tese, os bloqueios jurídicos e as perguntas típicas |
| `references/02-mudancas-no-modelo.md` | o que mudou em relação ao modelo AMN v1.4 e por quê |
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
