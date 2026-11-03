# Biblioteca do STJ (consulta; não distribuída às skills)

Gerada em 30/10/2026 por `_manutencao/coleta/coletar_jurisprudencia.py`. Resultado da conferência entre fontes:
`RELATORIO-coleta-2026-10-30.md`. Hashes e URLs das fontes: `manifesto-fontes.json` (os arquivos brutos, 14 MB, estão em
`_backup/fontes-jurisprudencia-2026-10-30/`).

| Pasta | Conteúdo | Arquivos | Fonte do texto |
|---|---|---|---|
| `sumulas/` | Súmulas 1 a 676, com situação (vigente ou cancelada) | 676 | BNP/CNJ; data, órgão, publicação e histórico de redação do caderno oficial do STJ |
| `temas/` | Temas repetitivos | 1.474 | CSV de dados abertos do STJ, conferido contra o BNP |
| `iac/`, `sirdr/`, `puil/` | Incidentes de assunção de competência, suspensões em IRDR e pedidos de uniformização | 22, 11 e 27 | CSV de dados abertos do STJ |

Cada pasta tem um `INDEX.md` de uma linha por precedente. Ficaram de fora as 837 "controvérsias" (fase anterior à afetação)
e 7 linhas sem tipo.

## Antes de citar

1. **As fichas curadas vêm primeiro.** `tema-929-stj.md`, `sumulas-stj.md` e as demais, em `../`, trazem a análise do
   escritório (o que citar e o que não citar). Esta biblioteca é o dado oficial, sem essa análise.
2. **Tema 929:** a situação oficial é "Mérito Julgado" e o CSV e o BNP concordam que a tese ainda não foi publicada. Não é
   fundamento até a publicação do acórdão (decisão do escritório de 29/10/2026).
3. **Seção "Divergência com o BNP/CNJ"** em um tema: o BNP costuma estar alguns dias à frente do CSV (em 30/10/2026,
   8 temas com situação diferente). Conferir no site do STJ antes de protocolar.
4. **`tese_possivelmente_truncada`:** o BNP corta a tese perto de 4.000 caracteres. Nos temas do STJ o texto vem do CSV
   (completo); em registros de outros órgãos coletados pelo BNP, o campo avisa.
5. **Súmulas 650 a 676:** não constam do caderno do STJ (de 04/05/2021); saem sem data da decisão, órgão e publicação.
   Súmulas de 1 a 649: o caderno traz as antigas em MAIÚSCULAS e sem acento; o texto aqui é o do BNP. Quando a grafia do
   caderno difere, a seção "Divergência com o caderno" mostra as duas.
6. **Datas:** `data_decisao` é a que o caderno registra em "Data da Decisão" (na súmula alterada, a da redação em vigor,
   como na 111; a redação anterior fica no histórico). As datas dentro de `historico` do registro do CNJ descrevem a
   admissão do registro no BNP, não o julgamento.

## Para uma skill passar a usar um precedente

Siga a rotina de `_manutencao/ROTINA.md` ("Índice da jurisprudência por assunto"): crie a ficha curada, em arquivo plano
dentro de `_acervo/jurisprudencia/`, a partir do arquivo daqui; acrescente-a ao manifesto com `sincronizar-acervo.js
--incluir` e à lista `DADOS` do `gerar-indice-jurisprudencia.py`; rode o verificador. Não copie a pasta `stj/` inteira para
uma skill: são 12 MB.

## Atualizar

`python3 -I _manutencao/coleta/coletar_jurisprudencia.py --saida <pasta de preparo> stj-temas stj-sumulas`. Só substitua os
arquivos daqui se a coleta sair APROVADA. Outros órgãos e espécies do BNP (TJBA, TRF1, TNU, STF): `--bnp-listar TJBA` e
`bnp:TJBA:SUM,IAC,IRDR,NT`.
