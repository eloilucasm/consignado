# Base territorial do TJSC (Santa Catarina) para o endereçamento (comarcas e unidades)

> Fonte: TJSC: "Composição das Comarcas" (circunscrição, entrância, comarca, municípios), arquivo fornecido pelo escritório (_manutencao/coleta/tjsc/fonte-tjsc-composicao-comarcas.md), recebido em 22/11/2026. Municípios conferidos com a lista do IBGE (API de localidades, consulta em 22/11/2026). Gerado por `_manutencao/coleta/territorial_ufs.py`.
> Só dados de unidade. Telefones e endereços dos fóruns ficam na fonte.

## 1. Regra de endereçamento

1. **Ache a comarca** do município de residência do autor no índice da seção 4 (`grep -n "Nome do município"`). A comarca nem sempre é o próprio município.
2. O endereçamento pronto do JEC e da Justiça Comum está em `references/dados/tjsc_unidades.json` (`jec.enderecamento`, `comum.enderecamento`); `[N]` é o número da unidade, que sai na distribuição (`__`).
3. A cidade do fecho é a sede da comarca (ou do foro), com a UF: `sede - SC`.
4. Linha com "conferir" vira pendência da triagem: o advogado confirma a unidade antes de protocolar.
5. Réu Caixa: Justiça Federal (TRF4), que **não tem tabela** neste pacote: a subseção é pendência a conferir.

**Pendente de aprovação do escritório** (a forma do endereçamento destes estados ainda não foi aprovada, como foi a do TJBA em 03/11/2026).

## 2. Limites da fonte

- A fonte traz só a composição das comarcas (município → comarca e entrância). Nenhuma unidade (Juizado ou vara) consta: os endereçamentos seguem um padrão pela entrância e estão todos marcados "conferir".
- Florianópolis é a Comarca da Capital (foros Central, Continente, Norte da Ilha, Des. Eduardo Luz e outros); Joinville e Blumenau têm foros especiais listados na fonte.

## 3. Comarcas (113)

| Comarca | Entrância | JEC | Justiça Comum | Conferir |
|---|---|---|---|---|
| Abelardo Luz | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ABELARDO LUZ - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ABELARDO LUZ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Anchieta | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ANCHIETA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ANCHIETA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Anita Garibaldi | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ANITA GARIBALDI - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ANITA GARIBALDI - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Araquari | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ARAQUARI - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ARAQUARI - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Araranguá | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ARARANGUÁ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ARARANGUÁ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Armazém | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ARMAZÉM - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ARMAZÉM - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Ascurra | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ASCURRA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ASCURRA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Balneário Camboriú | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BALNEÁRIO CAMBORIÚ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BALNEÁRIO CAMBORIÚ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Balneário Piçarras | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BALNEÁRIO PIÇARRAS - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BALNEÁRIO PIÇARRAS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Barra Velha | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BARRA VELHA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BARRA VELHA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Biguaçu | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BIGUAÇU - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BIGUAÇU - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Blumenau | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BLUMENAU - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BLUMENAU - SC | a comarca tem também Foro Universitario; a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Bom Retiro | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BOM RETIRO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BOM RETIRO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Braço do Norte | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BRAÇO DO NORTE - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BRAÇO DO NORTE - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Brusque | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BRUSQUE - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BRUSQUE - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Caçador | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAÇADOR - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CAÇADOR - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Camboriú | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMBORIÚ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CAMBORIÚ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Campo Belo do Sul | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPO BELO DO SUL - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAMPO BELO DO SUL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Campo Erê | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPO ERÊ - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAMPO ERÊ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Campos Novos | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPOS NOVOS - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CAMPOS NOVOS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Canoinhas | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CANOINHAS - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CANOINHAS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Capinzal | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAPINZAL - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CAPINZAL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Capivari de Baixo | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAPIVARI DE BAIXO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAPIVARI DE BAIXO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Catanduvas | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CATANDUVAS - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CATANDUVAS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Chapecó | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CHAPECÓ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CHAPECÓ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Concórdia | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CONCÓRDIA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CONCÓRDIA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Coronel Freitas | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CORONEL FREITAS - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CORONEL FREITAS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Correia Pinto | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CORREIA PINTO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CORREIA PINTO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Criciúma | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CRICIÚMA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CRICIÚMA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Cunha Porã | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CUNHA PORÃ - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CUNHA PORÃ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Curitibanos | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CURITIBANOS - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CURITIBANOS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Descanso | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE DESCANSO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE DESCANSO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Dionísio Cerqueira | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE DIONÍSIO CERQUEIRA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE DIONÍSIO CERQUEIRA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Capital | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DA CAPITAL - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DA CAPITAL - SC | Capital: foros Foro Central, Foro Des. Eduardo Luz, Foro Distrital Do Continente, Foro Do Norte Da Ilha, Foro Est.Bancario, Das Turmas E Da Veefm, Turmas Recursais; confira o foro pelo bairro do autor; a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Forquilhinha | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE FORQUILHINHA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE FORQUILHINHA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Fraiburgo | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE FRAIBURGO - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE FRAIBURGO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Garopaba | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GAROPABA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE GAROPABA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Garuva | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GARUVA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE GARUVA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Gaspar | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GASPAR - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE GASPAR - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Guabiruba | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUABIRUBA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE GUABIRUBA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Guaramirim | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUARAMIRIM - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE GUARAMIRIM - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Herval d'Oeste | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE HERVAL D'OESTE - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE HERVAL D'OESTE - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Ibirama | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IBIRAMA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IBIRAMA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Içara | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IÇARA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IÇARA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Imaruí | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IMARUÍ - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE IMARUÍ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Imbituba | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IMBITUBA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IMBITUBA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Indaial | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE INDAIAL - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE INDAIAL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Ipumirim | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IPUMIRIM - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE IPUMIRIM - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Itá | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITÁ - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITÁ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Itaiópolis | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAIÓPOLIS - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITAIÓPOLIS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Itajaí | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAJAÍ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITAJAÍ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Itapema | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAPEMA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITAPEMA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Itapiranga | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAPIRANGA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITAPIRANGA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Itapoá | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAPOÁ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITAPOÁ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Ituporanga | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITUPORANGA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITUPORANGA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Jaguaruna | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JAGUARUNA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE JAGUARUNA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Jaraguá do Sul | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JARAGUÁ DO SUL - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE JARAGUÁ DO SUL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Joaçaba | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JOAÇABA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE JOAÇABA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Joinville | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JOINVILLE - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE JOINVILLE - SC | a comarca tem também Foro Fazendario; a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Lages | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LAGES - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE LAGES - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Laguna | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LAGUNA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE LAGUNA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Lauro Müller | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LAURO MÜLLER - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE LAURO MÜLLER - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Lebon Régis | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LEBON RÉGIS - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE LEBON RÉGIS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Mafra | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MAFRA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MAFRA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Maravilha | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MARAVILHA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MARAVILHA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Meleiro | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MELEIRO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MELEIRO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Modelo | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MODELO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MODELO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Mondaí | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MONDAÍ - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MONDAÍ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Navegantes | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NAVEGANTES - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE NAVEGANTES - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Orleans | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ORLEANS - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ORLEANS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Otacílio Costa | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE OTACÍLIO COSTA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE OTACÍLIO COSTA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Palhoça | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PALHOÇA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PALHOÇA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Palmitos | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PALMITOS - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PALMITOS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Papanduva | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PAPANDUVA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PAPANDUVA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Penha | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PENHA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PENHA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Pinhalzinho | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PINHALZINHO - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PINHALZINHO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Pomerode | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE POMERODE - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE POMERODE - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Ponte Serrada | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PONTE SERRADA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PONTE SERRADA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Porto Belo | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PORTO BELO - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PORTO BELO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Porto União | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PORTO UNIÃO - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PORTO UNIÃO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Presidente Getúlio | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PRESIDENTE GETÚLIO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PRESIDENTE GETÚLIO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Quilombo | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE QUILOMBO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE QUILOMBO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Rio do Campo | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO DO CAMPO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO DO CAMPO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Rio do Oeste | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO DO OESTE - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO DO OESTE - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Rio do Sul | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO DO SUL - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE RIO DO SUL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Rio Negrinho | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO NEGRINHO - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE RIO NEGRINHO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Santa Cecília | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA CECÍLIA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SANTA CECÍLIA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Santa Rosa do Sul | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA ROSA DO SUL - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SANTA ROSA DO SUL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Santo Amaro da Imperatriz | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTO AMARO DA IMPERATRIZ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SANTO AMARO DA IMPERATRIZ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São Bento do Sul | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO BENTO DO SUL - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO BENTO DO SUL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São Carlos | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO CARLOS - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO CARLOS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São Domingos | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO DOMINGOS - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO DOMINGOS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São Francisco do Sul | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO FRANCISCO DO SUL - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO FRANCISCO DO SUL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São João Batista | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOÃO BATISTA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO JOÃO BATISTA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São Joaquim | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOAQUIM - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO JOAQUIM - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São José | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOSÉ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO JOSÉ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São José do Cedro | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOSÉ DO CEDRO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO JOSÉ DO CEDRO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São Lourenço do Oeste | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO LOURENÇO DO OESTE - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO LOURENÇO DO OESTE - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| São Miguel do Oeste | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO MIGUEL DO OESTE - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO MIGUEL DO OESTE - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Seara | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SEARA - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SEARA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Sombrio | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SOMBRIO - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SOMBRIO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Taió | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TAIÓ - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TAIÓ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Tangará | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TANGARÁ - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TANGARÁ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Tijucas | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TIJUCAS - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TIJUCAS - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Timbó | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TIMBÓ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TIMBÓ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Trombudo Central | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TROMBUDO CENTRAL - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TROMBUDO CENTRAL - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Tubarão | Especial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TUBARÃO - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TUBARÃO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Turvo | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TURVO - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TURVO - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Urubici | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE URUBICI - SC | AO JUÍZO DA VARA ÚNICA DA COMARCA DE URUBICI - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Urussanga | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE URUSSANGA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE URUSSANGA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Videira | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE VIDEIRA - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE VIDEIRA - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Xanxerê | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE XANXERÊ - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE XANXERÊ - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |
| Xaxim | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE XAXIM - SC | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE XAXIM - SC | a fonte do TJSC só traz a composição das comarcas: confira a unidade do Juizado (Juizado próprio ou adjunto à vara) e o nome e o número da vara cível |

## 4. Índice por município (295)

- Abdon Batista → Anita Garibaldi
- Abelardo Luz → Abelardo Luz
- Agrolândia → Trombudo Central
- Agronômica → Rio do Sul
- Água Doce → Joaçaba
- Águas de Chapecó → São Carlos
- Águas Frias → Pinhalzinho
- Águas Mornas → Santo Amaro da Imperatriz
- Alfredo Wagner → Bom Retiro
- Alto Bela Vista → Concórdia
- Anchieta → Anchieta
- Angelina → Santo Amaro da Imperatriz
- Anita Garibaldi → Anita Garibaldi
- Anitápolis → Santo Amaro da Imperatriz
- Antônio Carlos → Biguaçu
- Apiúna → Ascurra
- Arabutã → Ipumirim
- Araquari → Araquari
- Araranguá → Araranguá
- Armazém → Armazém
- Arroio Trinta → Videira
- Arvoredo → Seara
- Ascurra → Ascurra
- Atalanta → Ituporanga
- Aurora → Rio do Sul
- Balneário Arroio do Silva → Araranguá
- Balneário Barra do Sul → Araquari
- Balneário Camboriú → Balneário Camboriú
- Balneário Gaivota → Sombrio
- Balneário Piçarras → Balneário Piçarras
- Balneário Rincão → Içara
- Bandeirante → São Miguel do Oeste
- Barra Bonita → São Miguel do Oeste
- Barra Velha → Barra Velha
- Bela Vista do Toldo → Canoinhas
- Belmonte → Descanso
- Benedito Novo → Timbó
- Biguaçu → Biguaçu
- Blumenau → Blumenau
- Bocaina do Sul → Lages
- Bombinhas → Porto Belo
- Bom Jardim da Serra → São Joaquim
- Bom Jesus → Xanxerê
- Bom Jesus do Oeste → Modelo
- Bom Retiro → Bom Retiro
- Botuverá → Brusque
- Braço do Norte → Braço do Norte
- Braço do Trombudo → Trombudo Central
- Brunópolis → Campos Novos
- Brusque → Brusque
- Caçador → Caçador
- Caibi → Palmitos
- Calmon → Caçador
- Camboriú → Camboriú
- Campo Alegre → São Bento do Sul
- Campo Belo do Sul → Campo Belo do Sul
- Campo Erê → Campo Erê
- Campos Novos → Campos Novos
- Canelinha → Tijucas
- Canoinhas → Canoinhas
- Capão Alto → Campo Belo do Sul
- Capinzal → Capinzal
- Capivari de Baixo → Capivari de Baixo
- Catanduvas → Catanduvas
- Caxambu do Sul → Chapecó
- Celso Ramos → Anita Garibaldi
- Cerro Negro → Campo Belo do Sul
- Chapadão do Lageado → Ituporanga
- Chapecó → Chapecó
- Cocal do Sul → Urussanga
- Concórdia → Concórdia
- Cordilheira Alta → Chapecó
- Coronel Freitas → Coronel Freitas
- Coronel Martins → São Domingos
- Correia Pinto → Correia Pinto
- Corupá → Jaraguá do Sul
- Criciúma → Criciúma
- Cunha Porã → Cunha Porã
- Cunhataí → São Carlos
- Curitibanos → Curitibanos
- Descanso → Descanso
- Dionísio Cerqueira → Dionísio Cerqueira
- Dona Emma → Presidente Getúlio
- Doutor Pedrinho → Timbó
- Entre Rios → São Domingos
- Ermo → Turvo
- Erval Velho → Herval d'Oeste
- Faxinal dos Guedes → Xanxerê
- Flor do Sertão → Maravilha
- Florianópolis → Capital
- Formosa do Sul → Quilombo
- Forquilhinha → Forquilhinha
- Fraiburgo → Fraiburgo
- Frei Rogério → Curitibanos
- Galvão → São Domingos
- Garopaba → Garopaba
- Garuva → Garuva
- Gaspar → Gaspar
- Governador Celso Ramos → Biguaçu
- Grão-Pará → Braço do Norte
- Gravatal → Armazém
- Guabiruba → Guabiruba
- Guaraciaba → São Miguel do Oeste
- Guaramirim → Guaramirim
- Guarujá do Sul → São José do Cedro
- Guatambú → Chapecó
- Herval d'Oeste → Herval d'Oeste
- Ibiam → Tangará
- Ibicaré → Joaçaba
- Ibirama → Ibirama
- Içara → Içara
- Ilhota → Gaspar
- Imaruí → Imaruí
- Imbituba → Imbituba
- Imbuia → Ituporanga
- Indaial → Indaial
- Iomerê → Videira
- Ipira → Capinzal
- Iporã do Oeste → Mondaí
- Ipuaçu → São Domingos
- Ipumirim → Ipumirim
- Iraceminha → Maravilha
- Irani → Concórdia
- Irati → Quilombo
- Irineópolis → Porto União
- Itá → Itá
- Itaiópolis → Itaiópolis
- Itajaí → Itajaí
- Itapema → Itapema
- Itapiranga → Itapiranga
- Itapoá → Itapoá
- Ituporanga → Ituporanga
- Jaborá → Catanduvas
- Jacinto Machado → Turvo
- Jaguaruna → Jaguaruna
- Jaraguá do Sul → Jaraguá do Sul
- Jardinópolis → Coronel Freitas
- Joaçaba → Joaçaba
- Joinville → Joinville
- José Boiteux → Ibirama
- Jupiá → São Lourenço do Oeste
- Lacerdópolis → Capinzal
- Lages → Lages
- Laguna → Laguna
- Lajeado Grande → Xaxim
- Laurentino → Rio do Oeste
- Lauro Müller → Lauro Müller
- Lebon Régis → Lebon Régis
- Leoberto Leal → Ituporanga
- Lindóia do Sul → Ipumirim
- Lontras → Rio do Sul
- Luiz Alves → Navegantes
- Luzerna → Joaçaba
- Macieira → Caçador
- Mafra → Mafra
- Major Gercino → São João Batista
- Major Vieira → Canoinhas
- Maracajá → Araranguá
- Maravilha → Maravilha
- Marema → Xaxim
- Massaranduba → Guaramirim
- Matos Costa → Porto União
- Meleiro → Meleiro
- Mirim Doce → Taió
- Modelo → Modelo
- Mondaí → Mondaí
- Monte Carlo → Fraiburgo
- Monte Castelo → Papanduva
- Morro da Fumaça → Urussanga
- Morro Grande → Meleiro
- Navegantes → Navegantes
- Nova Erechim → Pinhalzinho
- Nova Itaberaba → Pinhalzinho
- Nova Trento → São João Batista
- Nova Veneza → Criciúma
- Novo Horizonte → São Lourenço do Oeste
- Orleans → Orleans
- Otacílio Costa → Otacílio Costa
- Ouro → Capinzal
- Ouro Verde → Abelardo Luz
- Paial → Chapecó
- Painel → Lages
- Palhoça → Palhoça
- Palma Sola → Anchieta
- Palmeira → Otacílio Costa
- Palmitos → Palmitos
- Papanduva → Papanduva
- Paraíso → São Miguel do Oeste
- Passo de Torres → Santa Rosa do Sul
- Passos Maia → Ponte Serrada
- Paulo Lopes → Garopaba
- Pedras Grandes → Tubarão
- Penha → Penha
- Peritiba → Concórdia
- Pescaria Brava → Laguna
- Petrolândia → Ituporanga
- Pinhalzinho → Pinhalzinho
- Pinheiro Preto → Tangará
- Piratuba → Capinzal
- Planalto Alegre → Chapecó
- Pomerode → Pomerode
- Ponte Alta → Correia Pinto
- Ponte Alta do Norte → Curitibanos
- Ponte Serrada → Ponte Serrada
- Porto Belo → Porto Belo
- Porto União → Porto União
- Pouso Redondo → Trombudo Central
- Praia Grande → Santa Rosa do Sul
- Presidente Castello Branco → Concórdia
- Presidente Getúlio → Presidente Getúlio
- Presidente Nereu → Rio do Sul
- Princesa → São José do Cedro
- Quilombo → Quilombo
- Rancho Queimado → Santo Amaro da Imperatriz
- Rio das Antas → Caçador
- Rio do Campo → Rio do Campo
- Rio do Oeste → Rio do Oeste
- Rio dos Cedros → Timbó
- Rio do Sul → Rio do Sul
- Rio Fortuna → Braço do Norte
- Rio Negrinho → Rio Negrinho
- Rio Rufino → Urubici
- Riqueza → Mondaí
- Rodeio → Ascurra
- Romelândia → Anchieta
- Salete → Taió
- Saltinho → Campo Erê
- Salto Veloso → Videira
- Sangão → Jaguaruna
- Santa Cecília → Santa Cecília
- Santa Helena → Descanso
- Santa Rosa de Lima → Braço do Norte
- Santa Rosa do Sul → Santa Rosa do Sul
- Santa Terezinha → Rio do Campo
- Santa Terezinha do Progresso → Maravilha
- Santiago do Sul → Quilombo
- Santo Amaro da Imperatriz → Santo Amaro da Imperatriz
- São Bento do Sul → São Bento do Sul
- São Bernardino → Campo Erê
- São Bonifácio → Santo Amaro da Imperatriz
- São Carlos → São Carlos
- São Cristóvão do Sul → Curitibanos
- São Domingos → São Domingos
- São Francisco do Sul → São Francisco do Sul
- São João Batista → São João Batista
- São João do Itaperiú → Barra Velha
- São João do Oeste → Itapiranga
- São João do Sul → Santa Rosa do Sul
- São Joaquim → São Joaquim
- São José → São José
- São José do Cedro → São José do Cedro
- São José do Cerrito → Lages
- São Lourenço do Oeste → São Lourenço do Oeste
- São Ludgero → Braço do Norte
- São Martinho → Armazém
- São Miguel da Boa Vista → Maravilha
- São Miguel do Oeste → São Miguel do Oeste
- São Pedro de Alcântara → São José
- Saudades → Pinhalzinho
- Schroeder → Guaramirim
- Seara → Seara
- Serra Alta → Modelo
- Siderópolis → Criciúma
- Sombrio → Sombrio
- Sul Brasil → Modelo
- Taió → Taió
- Tangará → Tangará
- Tigrinhos → Maravilha
- Tijucas → Tijucas
- Timbé do Sul → Turvo
- Timbó → Timbó
- Timbó Grande → Santa Cecília
- Três Barras → Canoinhas
- Treviso → Criciúma
- Treze de Maio → Jaguaruna
- Treze Tílias → Joaçaba
- Trombudo Central → Trombudo Central
- Tubarão → Tubarão
- Tunápolis → Itapiranga
- Turvo → Turvo
- União do Oeste → Coronel Freitas
- Urubici → Urubici
- Urupema → São Joaquim
- Urussanga → Urussanga
- Vargeão → Ponte Serrada
- Vargem → Campos Novos
- Vargem Bonita → Catanduvas
- Vidal Ramos → Ituporanga
- Videira → Videira
- Vitor Meireles → Presidente Getúlio
- Witmarsum → Presidente Getúlio
- Xanxerê → Xanxerê
- Xavantina → Seara
- Xaxim → Xaxim
- Zortéa → Campos Novos
