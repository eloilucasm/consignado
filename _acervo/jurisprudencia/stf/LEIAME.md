# Biblioteca do STF (consulta; não distribuída às skills)

Gerada em 30/10/2026 por `_manutencao/coleta/coletar_jurisprudencia.py stf`. Resultado da conferência entre fontes:
`RELATORIO-coleta-2026-10-30.md`. Hashes e URLs das fontes: `manifesto-fontes.json` (arquivos brutos em
`_backup/fontes-jurisprudencia-2026-10-30/`).

| Pasta | Conteúdo | Arquivos | Fontes |
|---|---|---|---|
| `sumulas/` | Súmulas 1 a 736, com situação | 736 | BNP/CNJ cruzado com o caderno oficial do STF (PDF) |
| `sumulas-vinculantes/` | Súmulas vinculantes 1 a 62 | 62 | só BNP/CNJ |
| `repercussao-geral/` | Temas de repercussão geral 1 a 1.496 | 1.496 | só BNP/CNJ |

Cada pasta tem `INDEX.md`. **Fora desta biblioteca:** controle concentrado (ADI, ADPF, ADC e ADO, 5.209 registros no BNP).

## Antes de citar

1. **As fichas curadas e a CF vêm primeiro.** Esta biblioteca é o dado oficial, sem a análise do escritório. Na busca de
   30/10/2026, as skills quase não mencionam o STF: fora os textos das leis, 4 arquivos têm uma menção cada.
2. **Súmulas: o que foi cruzado.** O texto do BNP foi comparado com o caderno em cada uma das 734 súmulas que os dois têm:
   732 idênticas (ignorando acento, pontuação e hifenização de linha do PDF). Em duas, o BNP está errado e vale o caderno:
   **Súmula 6** (o BNP traz "antes de 7 por aquele Tribunal" onde o caderno traz "aprovada") e **Súmula 534** (o BNP traz
   "Ddecreto-lei"). Os arquivos mostram a divergência.
3. **Situação.** Vem do BNP. As **Súmulas 152 e 274** (revogadas pelas Súmulas 494 e 549) não estão no BNP e vêm só do
   caderno. O caderno é de **1º/12/2017** (arquivo de 10/11/2022). O BNP dá a **359** como alterada e a **563** e a **584**
   como canceladas, e o caderno não as marca (mudança posterior a 2017 ou nota de outra forma; não verifiquei qual).
   O caderno não permite saber de outras alterações posteriores a 2017: vale a situação do BNP.
4. **Enunciado.** As marcas finais do caderno e do BNP ("(Revogada)", "(Cancelada)", "(Superada)", "(3)" de nota de rodapé) foram
   tiradas do enunciado e levadas para a situação; as aspas duplicadas pelo BNP (`""x""`) foram normalizadas. O registro
   original do CNJ está no fim de cada arquivo, sem alteração.
5. **Súmulas vinculantes e repercussão geral não têm segunda fonte.** Em seis temas de repercussão geral o BNP corta a tese perto
   de 4.000 caracteres: **533, 966, 976, 987, 1031 e 1234** (o arquivo avisa). **178** temas não têm tese no BNP: 133 afetados
   (Leading case afetado, repercussão geral reconhecida), 20 cancelados e 25 em situações variadas (sem repercussão
   geral, em análise, mérito julgado ou acórdão publicado). O tema **1491** não tem texto algum na fonte.
6. **Súmula Vinculante 30:** publicação suspensa em 04/02/2010 (PSV 41); o BNP não traz enunciado.
7. **Datas.** `data_aprovacao` é a "Sessão Plenária" do caderno. As datas de `historico` do registro do CNJ descrevem a
   admissão do registro no BNP, não o julgamento.

## Atualizar

`python3 -I _manutencao/coleta/coletar_jurisprudencia.py --saida <pasta de preparo> stf`. Só substitua os arquivos daqui se a
coleta sair APROVADA. Uma divergência nova entre o BNP e o caderno reprova a coleta até ser lida e, se for erro do BNP,
incluída em `DIVERGENCIAS_STF`.
