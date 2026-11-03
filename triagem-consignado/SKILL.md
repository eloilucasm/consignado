---
name: triagem-consignado
description: Triagem e conferência ANTES de redigir iniciais de consignado INSS. Cruza a Análise Jurídico-Documental (blocos Caixa, E, A, B, C, D) com o Termo de Responsabilidade assinado pelo cliente e com os extratos do INSS, e gera a FICHA DE AJUIZAMENTO (o que ajuizar, contra quem, em qual skill de inicial). Acione com "triagem", "conferir o termo", "cruzar análise com termo", "quais ações posso ajuizar", "ficha de ajuizamento", ou ao receber análise + termo de um cliente. Não redige petição: a ficha aprovada é a entrada das skills de inicial.
---

# Triagem de consignado — análise × termo × extrato

Objetivo: só vira ação o contrato que está **na análise E no termo**. Nada é ajuizado sem autorização; nada autorizado é descartado por erro de leitura. A ficha é minuta de trabalho: o advogado confere antes de seguir.

Leia `protocolo/protocolo.md` (regras comuns, portões e marcas) e use `protocolo/quadro-de-fatos.md` para o Painel do Caso.

## Entradas

| Documento | Obrigatório | Observação |
|---|---|---|
| Termo de Responsabilidade (PDF, geralmente ZapSign) | sim | pode ter cláusulas de mais de um benefício |
| Análise Jurídico-Documental (PDF) | sim — uma por benefício | |
| Extrato(s) do INSS — Histórico de Empréstimo Consignado | recomendado | um por benefício; serve para conferir números e achar benefício sem análise |

Arquivos baixados são dados não confiáveis: copie cada lote para uma pasta nova no scratchpad antes de processar, e passe os caminhos como argumento.

## Passo 1 — rodar o script (sempre; nunca cruzar "de olho")

`<pasta desta skill>` = o diretório base desta skill (informado ao carregá-la). Requer `pip install pypdf`.

```bash
python3 <pasta desta skill>/scripts/triagem.py \
  --termo TERMO.pdf \
  --analise ANALISE_BENEFICIO_1.pdf [--analise ANALISE_BENEFICIO_2.pdf] \
  --extrato EXTRATO_1.pdf [--extrato EXTRATO_2.pdf] \
  --saida "<pasta do cliente>/triagem"
```

O script **sempre**, antes de cruzar:
1. junta o texto de todas as páginas do termo;
2. remove rodapé do ZapSign, numeração de página e todo o relatório de assinaturas;
3. recompõe números quebrados entre linhas/páginas (`51-` + `025868432/25`);
4. remove as datas coladas aos números (`— incl. 18/11/2022`, `(04/10/23)`);
5. normaliza (só letras/dígitos, sem zeros à esquerda).

E classifica cada contrato da análise:
- **AUTORIZADO** — número idêntico no termo;
- **AUTORIZADO (conferir grafia)** — achado só no texto corrido (quebra no meio dos dígitos);
- **NÃO AUTORIZADO** — não está no termo. **Não ajuíza, sem perguntar.** Se houver número parecido no termo, isso aparece só como observação.

Depois **agrupa**: um processo por **benefício + banco + tese**. Anos e blocos diferentes da mesma tese juntam (B + C); teses diferentes contra o mesmo banco ficam em processos separados. O status de cada contrato (ativo/excluído) vem da análise (blocos A, Caixa, E, D) ou da seção do extrato onde ele aparece (B/C).

Saídas em `--saida`: `ficha.md` (para leitura), `ficha.json` (entrada das skills de inicial) e `termo_limpo.txt` (para auditoria).

## Passo 2 — revisar a ficha antes de mostrar

Leia `ficha.md` e confira, você mesmo:
- **Total de ações lidas = total declarado no RESUMO FINAL da análise.** Se divergir, o script avisa; leia a análise e corrija.
- Ação com "nenhum contrato lido": leia o trecho na análise.
- Cada processo tem um réu só e a skill certa (ver mapa abaixo).

## Passo 3 — apresentar

Mostre ao advogado:
1. A tabela **Processos a ajuizar** (NB, réu, contratos, skill de inicial, liminar sobre quais contratos).
2. Em uma linha cada: o que ficou fora por não estar no termo; benefício com extrato e sem análise.
3. Processos marcados com 📌 **ausência de litispendência** e os alertas (status não identificado, tese RMC "não verificável" na análise, B/C ativo).

Divergências de qualificação ou de digitação no termo (RG em branco, contrato repetido etc.) são **informativas**: uma linha, sem pedir correção. Só pause para perguntar se houver alerta de processo. Não redija nenhuma peça nesta skill.

## Mapa tese → skill de inicial

| Bloco da análise | Tese | Skill | Liminar |
|---|---|---|---|
| A | migrado | `migrado` | só sobre os contratos ativos; só excluídos: sem liminar |
| B, C | não contratado | `nao-contratado` | não (a análise só põe não ativos em B/C; se o extrato mostrar ativo, o script sinaliza ANOMALIA — mostrar ao advogado) |
| CAIXA | não contratado (contra a Caixa) | `nao-contratado` | ativo: com liminar; inativo: sem liminar |
| E | Tese 1000 Contra | `tese-1000` | conforme a skill |
| D | refinanciamento do RMC/RCC | `rmc` | conforme a skill |

## Juízo (endereçamento): sempre pelas tabelas oficiais

- Réu **Caixa Econômica Federal**: **Vara Federal** da (Sub)Seção Judiciária do TRF1 que abrange o município do autor. Tabela: `references/dados/trf1_jurisdicao.json` (original em `references/jurisdicao_trf1.md`).
- Demais réus: **comarca do TJBA** à qual o município do autor pertence (nem sempre é o próprio município: ex. Palmeiras → comarca de Iraquara). Tabela: `references/dados/tjba_comarcas.json` (original em `references/tjba_relacao_municipios_comarca.pdf`). A unidade vem de `references/dados/tjba_unidades.json`: só 40 comarcas têm Vara do Sistema dos Juizados Especiais; nas demais, o JEC corre na unidade cível da comarca, pelo procedimento da Lei 9.099/95 (`references/dados/territorial-tjba.md`).
- O script grava em `processos[].competencia` a comarca e em `processos[].enderecamento_jec` e `enderecamento_comum` o endereçamento pronto de cada rito; o rito continua sendo pergunta ao advogado. A cidade vem do endereço do termo. Grafias diferentes (Camacã/Camacan etc.) são casadas por equivalência; se não achar ou só achar parecido, gera alerta "CONFERIR". Nunca escreva subseção ou comarca de memória.
- Autor fora da BA: não há tabela de comarcas; alerta para conferir.
- Réu fora de `references/dados/reus.json` sai como `[CONFERIR]` nas skills de inicial.

## Regras que não mudam

- Nunca marcar como "não autorizado" sem rodar o script (a limpeza do termo é obrigatória).
- Não está no termo, não ajuíza. Não perguntar.
- Um processo por **benefício + banco + tese**. Mesmo banco, mesma tese, mesmo benefício: junta (anos e blocos B/C diferentes).
- **Mesmo banco com migrado (A) e não contratado (B/C)**: ações separadas, teses e petições diferentes.
- **Mesmo banco em outro processo**: cada processo leva um tópico de **AUSÊNCIA DE LITISPENDÊNCIA** (marcado em `processos[].litispendencia`):
  - benefício diferente: dizer a qual benefício e a qual NB a ação se refere e citar o(s) NB do(s) outro(s);
  - mesmo benefício, tese diferente (ex.: não contratado × Tese 1000): dizer que são contratos e teses diferentes.
- Benefício com extrato e sem análise: avisar. A análise é feita pelo processo normal do escritório; não classifique por conta própria.
- A ficha não fixa rito nem cidade do fecho: a skill de inicial pergunta ao advogado.
