# Origem dos scripts de coleta

Estes scripts derivam do repositório https://github.com/ctresb/leis (licença MIT, Copyright (c) 2026 João Davi). O texto
da licença está em `LICENSE-ctresb-leis.txt` e deve acompanhar qualquer redistribuição.

| Arquivo | Origem |
|---|---|
| `html2md.py`, `comum.py` | cópias de `scripts/` do repositório |
| `coletar_planalto.py` | derivado de `scripts/baixar_planalto.py` |
| `coletar_jurisprudencia.py` | derivado de `scripts/baixar_jurisprudencia.py`, com outra arquitetura (BNP/CNJ como fonte do texto e da situação, caderno em PDF e CSV de dados abertos como conferência) |
| `auditar_conversao.py` | próprio (não existe no repositório) |

As alterações estão descritas no cabeçalho de cada arquivo derivado. Os dados baixados (leis, súmulas, temas) são texto de
fontes oficiais; o repositório ctresb não foi usado como fonte de texto, só como origem dos conversores.
