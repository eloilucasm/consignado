---
name: migrado
description: Redige a petição inicial de empréstimo consignado MIGRADO: contrato que o beneficiário nega ter firmado e que foi averbado no INSS com origem "Migrado do contrato … CBC: …", isto é, vindo de outra instituição por troca de titularidade ou cessão, sem nova manifestação de vontade. Lê o extrato do INSS, identifica a origem da migração e o banco anterior, calcula descontos, dobro, proveito econômico dos contratos ativos e valor da causa, escolhe a norma pela data (IN 28/2008 até 12/12/2022; IN 138/2022 desde 13/12/2022), pergunta o rito (JEC ou Justiça Comum) e a cidade do fecho e entrega minuta em Markdown para a tipografia-azul. Acione com "migrado", "migração de contrato", "migrado do contrato", "troca de titularidade", "CBC", "cessão de consignado". Não use para contrato não contratado sem migração, Tese 1000 ou refinanciamento de cartão RMC/RCC, nem para recurso.
---

# Inicial de consignado migrado

Redige a inicial de **inexistência de relação jurídica e nulidade da migração, cumulada com repetição do indébito em dobro, obrigação de fazer e dano extrapatrimonial**, para o contrato que o INSS registra como "Migrado do contrato … CBC: …" e que o beneficiário nega ter firmado. Fontes consultadas em 28/10/2026. Toda peça é minuta: o advogado revisa e assina.

Leia `protocolo/protocolo.md` (regras comuns, portões e marcas) e `assets/padrao-pecas.md` (forma e pedidos de rotina) antes de redigir. Leia `references/01-tese-e-roteiro.md`: ela explica **por que a migração, por si, é permitida pela norma do INSS** e onde a tese realmente se apoia.

## Abertura e triagem progressiva

1. Peça só o que falta: ficha de ajuizamento, extrato do INSS do NB do processo, qualificação do autor. Extraia dos documentos antes de perguntar.
2. Monte o **quadro de fatos** (`protocolo/quadro-de-fatos.md`) e mostre o Painel do Caso. No máximo **três lacunas por rodada**.
3. **Antes de gerar, pergunte sempre ao advogado:** (a) o rito, **JEC ou Justiça Comum**; (b) a **cidade e a UF do fecho**; (c) se declara **interesse ou desinteresse** na audiência de conciliação (Justiça Comum). Pergunte também, sem contar nas três lacunas, se o cliente trouxe o **extrato bancário do mês da averbação** e se o banco **entregou contrato ou trilha antes da ação**; passe as respostas ao script (`--rito jec|comum`, `--extrato-bancario sim|nao`, `--dossie-pre-acao`). O extrato bancário é **recomendado**, não obrigatório: sem ele, registre a pendência e o advogado decide se ajuíza. Se ele mostrar crédito ligado ao contrato, use o bloco `[[SE CRÉDITO EM CONTA]]` do modelo (subtópico dos fatos e pedido 7): a peça reconhece o lançamento, nega a contratação e deixa a marca `[DECISÃO DO ADVOGADO: devolução, depósito em juízo ou compensação]`; nunca escolha por ele.
4. Só entram contratos que estão **na análise e no termo**.

## Cálculo

No Cowork, rode e **confira por segunda via**:

```
python3 scripts/calcular_migrado.py --ficha ficha.json --processo N --extrato extrato.pdf --data AAAA-MM-DD --saida pasta/ [--incluir-outros-bancos] [--rito jec|comum] [--extrato-bancario sim|nao] [--dossie-pre-acao]
```

O script lê o extrato (`scripts/extrato.py`, requer `pip install pypdf`), confere se cada contrato tem origem "Migrado do contrato … CBC: …", extrai o contrato e o banco de origem, procura o mesmo número no banco anterior, conta os descontos, calcula o dobro, o proveito econômico dos contratos ativos (parcelas vincendas) e o valor da causa. Os descontos registrados no banco anterior **não são somados** sem a decisão do advogado (`--incluir-outros-bancos`). Sem execução de código, faça a tabela à mão e marque `CÁLCULO A CONFERIR`. O leitor do extrato foi herdado do pacote AMN e só foi testado aqui com extrato fictício: confira a primeira leitura real contra o PDF.

## Entrega e portões

Preencha `assets/modelo-inicial-migrado.md` com o quadro de fatos e o `calculo.json`. Ao fim, registre os quatro portões do protocolo. O portão 3 inclui a **checagem pré-recurso** (FSC1 a FSC12, `assets/escrutinio-fsc-vf.md`; o registro fica em `checagem-fsc-vf.md`). Dois portões falhos seguidos: entregue só o diagnóstico ou minuta `BLOQUEADO PARA USO FINAL`.

**Bloqueios específicos:** contrato sem origem de migração no extrato (rever a tese: pode ser não contratado comum); contrato fora do termo; migração de outro banco sem decisão do advogado sobre os descontos do banco anterior; réu sem cadastro em `references/dados/reus.json`; rito ou cidade do fecho não informados.

## Peças e arquivos

| Arquivo | Para quê |
|---|---|
| `assets/modelo-inicial-migrado.md` | modelo da inicial, com condicionais por rito, data da averbação, tutela, prescrição, LGPD e honorários |
| `assets/padrao-pecas.md` | endereçamento, qualificação, pedidos de rotina, precedentes e revisão |
| `assets/escrutinio-fsc-vf.md` | FSC1 a FSC12 e VF1 a VF9 antes do ajuizamento e formato do registro |
| `references/01-tese-e-roteiro.md` | a tese, a migração na norma, o que não afirmar e as perguntas típicas |
| `references/02-mudancas-no-modelo.md` | o que mudou em relação ao modelo do escritório (Francisco x Agibank) e ao AMN v1.4, e por quê |
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
