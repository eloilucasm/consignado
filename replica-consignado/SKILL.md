---
name: replica-consignado
description: Redige a RÉPLICA (impugnação à contestação) em ação de empréstimo consignado do INSS (não contratado, migrado, Tese 1000 ou RMC) contra banco. Fixa o escopo pela inicial, monta o índice dos autos, faz as verificações forenses VF1 a VF9 sobre os documentos do banco (ficha do contrato, dados cadastrais, autenticação, IP e geolocalização, TED × valor liberado, correspondente, cessão, análise cruzada, mesma data), responde ponto a ponto cada preliminar e alegação, pausa para o advogado e entrega minuta em Markdown para a tipografia-azul. Acione com "réplica", "impugnação à contestação", "o banco contestou", "responder a contestação do consignado". Não use para petição inicial nem para recurso.
---

# Réplica em ação de consignado

Redige a **impugnação à contestação** do banco. É a última oportunidade de impugnar especificamente os documentos do banco antes da sentença: documento particular não impugnado se considera autêntico (CPC, art. 411, III), e a impugnação de autenticidade precisa de argumentação específica (art. 436, parágrafo único). Fontes consultadas em 29/10/2026. Toda peça é minuta: o advogado revisa e assina.

Leia `protocolo/protocolo.md` (regras comuns, portões e marcas), `assets/padrao-pecas.md` (forma e pedidos de rotina) e `references/01-roteiro-e-vf.md` (etapas, verificações e regras da réplica) antes de redigir.

## Etapas

1. **Escopo.** Leia a **inicial** primeiro: contratos impugnados, rito, pedidos e cidade do fecho. Se o advogado trouxer o `dossie-do-caso.json` da inicial, use-o (checagem FSC, residência, extrato bancário). Sem ele, extraia do processo. Leia o extrato do INSS e anote a origem da averbação de cada contrato.
2. **Índice dos autos (VF1)** e **lista dos pontos da contestação**: cada preliminar e cada alegação de fato, com ID e página. Abra a primeira página de cada documento do banco antes de afirmar o que é.
3. **Fichas e quadro de indícios.** Registre os dados dos documentos do banco em `contestacao.json` (formato em `references/01-roteiro-e-vf.md`, seção 3) e rode:

```
python3 scripts/fichas.py --extrato extrato.pdf --contestacao contestacao.json --saida pasta/
python3 scripts/ip_check.py --entrada geo.json --sem-rdap   (se o log traz IP; lê eventos[].ip do mesmo arquivo do geo_check; sem --sem-rdap consulta o titular do bloco)
python3 scripts/geo_check.py geo.json --saida-md quadro_geo.md --saida-json quadro_geo.json   (se o log traz coordenadas, IP ou Cidade-UF)
```

   Requer `pip install pypdf`. Sem execução de código, monte as fichas e o quadro à mão, pelo mesmo roteiro, e marque `CONFERIR`.
   Registre também, em `pontos` do `contestacao.json`, cada preliminar e alegação com o código do catálogo (`P1`…, `M1`…; `NOVO` se não estiver lá) e o ID e a página. O `fichas.py` grava o **mapa de argumentos** (`mapa-argumentos.md` e `.json`): ponto, resposta e fonte do catálogo, provas dos autos e o pedido da réplica que atende o ponto; acrescenta sozinho os contratos sem defesa (M11) e a substituição de objeto (M12).
4. **Cartão de pausa (obrigatório).** Mostre ao advogado, antes de redigir: escopo e contratos sem defesa; quadro de indícios por gravidade; resultado de VF4 e VF9, com os itens de **REVISÃO HUMANA OBRIGATÓRIA** em bloco próprio; o **mapa de argumentos** (cada ponto da contestação com a resposta de `references/02-defesas-do-banco.md`, a prova e o pedido); e as decisões pendentes, inclusive todo ponto `NOVO`. **ALERTA_CONTRA** (TED igual ao valor liberado, na conta do benefício) exige decisão expressa sobre o valor (Súmula 42 do TJBA). Pergunte o rito, se não estiver claro nos autos, e a cidade e a UF do fecho. **Só redija depois da confirmação.**
5. **Redação** com `assets/modelo-replica-consignado.md`: um subtópico por preliminar e por alegação efetivamente feitas; um subtópico por contrato, com os achados e ID e página de cada dado. Cada subtópico abre pela resposta (a conclusão do ponto), dá a norma ou o precedente do mapa, aplica aos documentos do caso e fecha no pedido correspondente. Todo pedido do mapa entra em "Dos pedidos"; pedido sem ponto no mapa não entra.

## Regras que não se quebram

- Ponto a ponto: nada da contestação sem resposta, nada respondido que o banco não alegou.
- Impugnação específica de cada documento; contratos diferentes nunca se misturam; o banco que defende outro contrato não defendeu o impugnado (art. 341 do CPC).
- Nada sobre imagem, selfie ou assinatura sem visualizar a página.
- Geolocalização: "o log juntado pelo réu registra"; referência sempre a **residência**, com ID e página; REVISÃO HUMANA OBRIGATÓRIA não entra sem decisão.
- JEC: sem pedido de exibição, perícia ou ofício. Justiça Comum: reiterar exibição e perícia com quesitos.
- Nada sobre outras ações do autor ou do escritório, nem sobre a colheita da procuração.
- Valores e pedidos da inicial não mudam. **Não use o Tema 929/STJ como fundamento** (acórdão não publicado).

## Entrega e portões

Registre ao fim os quatro portões do protocolo. O portão 3 inclui a projeção dos fundamentos de sentença (`references/01-roteiro-e-vf.md`, seção 7): cada FSC que a réplica deve prevenir, com a resposta na peça. Dois portões falhos seguidos: entregue só o diagnóstico ou minuta `BLOQUEADO PARA USO FINAL`.

**Bloqueios específicos:** inicial não lida; documento do banco citado sem ID e página; contrato da contestação não conferido contra a inicial; cartão de pausa não confirmado.

## Peças e arquivos

| Arquivo | Para quê |
|---|---|
| `assets/modelo-replica-consignado.md` | modelo da réplica, com condicionais por rito, preliminares e achados |
| `assets/padrao-pecas.md` | endereçamento, pedidos de rotina, precedentes e revisão |
| `assets/escrutinio-fsc-vf.md` | FSC e VF na inicial; o registro da inicial é ponto de partida da réplica |
| `assets/ba_municipios.json` | malha municipal da Bahia (IBGE) usada pelo `geo_check.py` |
| `references/01-roteiro-e-vf.md` | etapas, formato do `contestacao.json`, VF1 a VF9, gravidade, regras e projeção FSC |
| `references/02-defesas-do-banco.md` | defesas típicas do banco e a resposta de cada uma, com a fonte |
| `scripts/fichas.py` | fichas dos contratos e quadro de indícios (VF2, VF3, VF5 a VF8) |
| `scripts/ip_check.py`, `scripts/geo_check.py`, `scripts/geo_malha.py`, `scripts/catalogo_indicadores.json` | VF4 e VF9 (IP e geolocalização) |
| `testes/caso-ficticio/` | caso fictício com teste de regressão |

## Normas e jurisprudência

Estão em `references/normas/` (texto literal e datado) e `references/jurisprudencia/`. A lista do que **não** cobre está em `protocolo/fontes-e-limites.md`. Para achar norma pelo conteúdo, `references/normas/MAPA.md`; por estrutura, `references/normas/ESTRUTURA.md`; precedente por assunto, `references/jurisprudencia/INDEX.md`. Cite apenas o que está nesses arquivos; o que não está vira `[CONFERIR]`.

## Formatação

Entregue Markdown. Ofereça gerar o Word com a skill `tipografia-azul`, com **realce amarelo** nas marcas de pendência (passe a instrução junto, porque a `tipografia-azul` ainda não descreve o realce).
