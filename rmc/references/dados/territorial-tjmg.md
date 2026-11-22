# Base territorial do TJMG (Minas Gerais) para o endereçamento (comarcas e unidades)

> Fonte: TJMG: guia das comarcas (fórum, órgãos, "Municípios e Distritos Integrantes"), arquivo fornecido pelo escritório (_manutencao/coleta/tjmg/fonte-tjmg-comarcas.md), recebido em 22/11/2026. Municípios conferidos com a lista do IBGE (API de localidades, consulta em 22/11/2026). Gerado por `_manutencao/coleta/territorial_ufs.py`.
> Só dados de unidade. Telefones e endereços dos fóruns ficam na fonte.

## 1. Regra de endereçamento

1. **Ache a comarca** do município de residência do autor no índice da seção 4 (`grep -n "Nome do município"`). A comarca nem sempre é o próprio município.
2. O endereçamento pronto do JEC e da Justiça Comum está em `references/dados/tjmg_unidades.json` (`jec.enderecamento`, `comum.enderecamento`); `[N]` é o número da unidade, que sai na distribuição (`__`).
3. A cidade do fecho é a sede da comarca (ou do foro), com a UF: `sede - MG`.
4. Linha com "conferir" vira pendência da triagem: o advogado confirma a unidade antes de protocolar.
5. Réu Caixa: Justiça Federal (TRF6), que **não tem tabela** neste pacote: a subseção é pendência a conferir.

**Decisão do escritório (22/11/2026).** Aprovada a forma do endereçamento desta tabela; as linhas com "conferir" continuam pendência do caso concreto.

## 2. Limites da fonte

- A fonte é um PDF convertido, com tabelas quebradas: a comarca de cada município saiu da tabela "Municípios e Distritos Integrantes" da seção da comarca; o que ficou fora da tabela está na coluna "conferir".
- Juizado: "Unidade Jurisdicional Única" ou unidades numeradas, como aparecem na seção da comarca. Onde a fonte não lista Juizado, a linha diz "conferir".
- Justiça Comum: a Vara Única ou as varas cíveis da seção da comarca.

Municípios a conferir:

- Amparo do Serra: município sem comarca na fonte: confira a comarca

## 3. Comarcas (297)

| Comarca | Entrância | JEC | Justiça Comum | Conferir |
|---|---|---|---|---|
| Abaeté | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ABAETÉ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ABAETÉ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Abre Campo | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ABRE CAMPO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE ABRE CAMPO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Santa Margarida, Sericita |
| Açucena | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE AÇUCENA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE AÇUCENA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Águas Formosas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ÁGUAS FORMOSAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ÁGUAS FORMOSAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Aimorés | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE AIMORÉS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE AIMORÉS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Aiuruoca | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE AIURUOCA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE AIURUOCA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Além Paraíba | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ALÉM PARAÍBA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE ALÉM PARAÍBA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude |
| Alfenas | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ALFENAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ALFENAS - MG |  |
| Almenara | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ALMENARA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE ALMENARA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude |
| Alpinópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ALPINÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ALPINÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: São José da Barra |
| Alto Rio Doce | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ALTO RIO DOCE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ALTO RIO DOCE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Alvinópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ALVINÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ALVINÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Andradas | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ANDRADAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE ANDRADAS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Andrelândia | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ANDRELÂNDIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ANDRELÂNDIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Araçuaí | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ARAÇUAÍ - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES CRIMINAIS DA COMARCA DE ARAÇUAÍ - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Criminais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Araguari | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ARAGUARI - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ARAGUARI - MG |  |
| Araxá | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ARAXÁ - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ARAXÁ - MG |  |
| Arcos | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ARCOS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE ARCOS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte cita o Juizado Especial sem a unidade jurisdicional |
| Areado | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE AREADO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE AREADO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Arinos | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ARINOS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ARINOS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Baependi | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BAEPENDI - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BAEPENDI - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Bambuí | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BAMBUÍ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BAMBUÍ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Barão de Cocais | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BARÃO DE COCAIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BARÃO DE COCAIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Barbacena | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE BARBACENA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BARBACENA - MG |  |
| Barroso | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BARROSO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BARROSO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Belo Horizonte | Especial | AO JUÍZO DA [N]ª UNIDADE JURISDICIONAL CÍVEL DO JUIZADO ESPECIAL DA COMARCA DE BELO HORIZONTE - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BELO HORIZONTE - MG | Belo Horizonte: confira a unidade jurisdicional cível (há unidades regionais, como a do Barreiro) |
| Belo Vale | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BELO VALE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BELO VALE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Betim | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE BETIM - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BETIM - MG |  |
| Bicas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BICAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BICAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Boa Esperança | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BOA ESPERANÇA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE BOA ESPERANÇA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Bocaiúva | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE BOCAIÚVA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE BOCAIÚVA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude |
| Bom Despacho | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BOM DESPACHO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE BOM DESPACHO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Bom Sucesso | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BOM SUCESSO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BOM SUCESSO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Bonfim | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BONFIM - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BONFIM - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Bonfinópolis de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BONFINÓPOLIS DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BONFINÓPOLIS DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Borda da Mata | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BORDA DA MATA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BORDA DA MATA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Botelhos | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BOTELHOS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BOTELHOS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Brasília de Minas | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BRASÍLIA DE MINAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE BRASÍLIA DE MINAS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Brazópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BRAZÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BRAZÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Brumadinho | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BRUMADINHO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE BRUMADINHO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Bueno Brandão | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BUENO BRANDÃO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BUENO BRANDÃO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Buenópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BUENÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BUENÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Buritis | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BURITIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE BURITIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Cabo Verde | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CABO VERDE - MG | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CABO VERDE - MG | a fonte não traz vara cível desta comarca; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Cachoeira de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CACHOEIRA DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CACHOEIRA DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Caeté | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAETÉ - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE CAETÉ - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Caldas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CALDAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CALDAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Camanducaia | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMANDUCAIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAMANDUCAIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Cambuí | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMBUÍ - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE CAMBUÍ - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Criminais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Cambuquira | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMBUQUIRA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAMBUQUIRA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Campanha | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPANHA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAMPANHA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Campestre | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPESTRE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAMPESTRE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Campina Verde | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPINA VERDE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAMPINA VERDE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Campo Belo | ? | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE CAMPO BELO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CAMPO BELO - MG |  |
| Campos Altos | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPOS ALTOS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAMPOS ALTOS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Campos Gerais | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPOS GERAIS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE CAMPOS GERAIS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Canápolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CANÁPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CANÁPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Candeias | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CANDEIAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CANDEIAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Capelinha | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAPELINHA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE CAPELINHA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Capinópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAPINÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAPINÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Carandaí | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARANDAÍ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CARANDAÍ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Carangola | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE CARANGOLA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE CARANGOLA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais |
| Caratinga | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE CARATINGA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CARATINGA - MG |  |
| Carlos Chagas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARLOS CHAGAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CARLOS CHAGAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Carmo da Mata | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARMO DA MATA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CARMO DA MATA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Carmo de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARMO DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CARMO DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Carmo do Cajuru | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARMO DO CAJURU - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CARMO DO CAJURU - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Carmo do Paranaíba | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARMO DO PARANAÍBA - MG | AO JUÍZO DA VARA CÍVEL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE CARMO DO PARANAÍBA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Carmo do Rio Claro | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARMO DO RIO CLARO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CARMO DO RIO CLARO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Carmópolis de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARMÓPOLIS DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CARMÓPOLIS DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Cássia | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CÁSSIA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE CÁSSIA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Cataguases | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE CATAGUASES - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CATAGUASES - MG |  |
| Caxambu | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAXAMBU - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CAXAMBU - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Cláudio | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CLÁUDIO - MG | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CLÁUDIO - MG | a fonte não traz vara cível desta comarca; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Conceição das Alagoas | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CONCEIÇÃO DAS ALAGOAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE CONCEIÇÃO DAS ALAGOAS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Pirajuba |
| Conceição do Mato Dentro | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CONCEIÇÃO DO MATO DENTRO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CONCEIÇÃO DO MATO DENTRO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Conceição do Rio Verde | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CONCEIÇÃO DO RIO VERDE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CONCEIÇÃO DO RIO VERDE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Congonhas | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CONGONHAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE CONGONHAS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte cita o Juizado Especial sem a unidade jurisdicional |
| Conquista | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CONQUISTA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CONQUISTA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Conselheiro Lafaiete | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE CONSELHEIRO LAFAIETE - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CONSELHEIRO LAFAIETE - MG |  |
| Conselheiro Pena | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CONSELHEIRO PENA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE CONSELHEIRO PENA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Contagem | Especial | AO JUÍZO DA [N]ª UNIDADE JURISDICIONAL CÍVEL DO JUIZADO ESPECIAL DA COMARCA DE CONTAGEM - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CONTAGEM - MG |  |
| Coração de Jesus | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CORAÇÃO DE JESUS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CORAÇÃO DE JESUS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Corinto | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CORINTO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CORINTO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Coromandel | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE COROMANDEL - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE COROMANDEL - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Coronel Fabriciano | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE CORONEL FABRICIANO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CORONEL FABRICIANO - MG |  |
| Cristina | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CRISTINA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CRISTINA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Cruzília | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CRUZÍLIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE CRUZÍLIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Curvelo | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE CURVELO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CURVELO - MG |  |
| Diamantina | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE DIAMANTINA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE DIAMANTINA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; municípios achados fora da tabela da comarca, conferir: Felício dos Santos, São Gonçalo do Rio Preto, Gouveia, Monjolos, Presidente Kubitschek, Senador Modestino Gonçalves |
| Divino | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE DIVINO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE DIVINO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Divinópolis | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE DIVINÓPOLIS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE DIVINÓPOLIS - MG |  |
| Dores do Indaiá | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE DORES DO INDAIÁ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE DORES DO INDAIÁ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Elói Mendes | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ELÓI MENDES - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ELÓI MENDES - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Entre Rios de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ENTRE RIOS DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ENTRE RIOS DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ervália | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ERVÁLIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ERVÁLIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Esmeraldas | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ESMERALDAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE ESMERALDAS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Espera Feliz | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ESPERA FELIZ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ESPERA FELIZ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Espinosa | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ESPINOSA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ESPINOSA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Estrela do Sul | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ESTRELA DO SUL - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ESTRELA DO SUL - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Eugenópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE EUGENÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE EUGENÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Extrema | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE EXTREMA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE EXTREMA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ferros | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE FERROS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE FERROS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Formiga | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE FORMIGA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE FORMIGA - MG |  |
| Francisco Sá | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE FRANCISCO SÁ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE FRANCISCO SÁ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Frutal | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE FRUTAL - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE FRUTAL - MG | municípios achados fora da tabela da comarca, conferir: Comendador Gomes, Fronteira, Planura |
| Galiléia | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GALILÉIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE GALILÉIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Governador Valadares | Especial | AO JUÍZO DA [N]ª UNIDADE JURISDICIONAL CÍVEL DO JUIZADO ESPECIAL DA COMARCA DE GOVERNADOR VALADARES - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE GOVERNADOR VALADARES - MG |  |
| Grão Mogol | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GRÃO MOGOL - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE GRÃO MOGOL - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Guanhães | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUANHÃES - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE GUANHÃES - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Guapé |
| Guaranésia | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUARANÉSIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE GUARANÉSIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Guarani | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUARANI - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE GUARANI - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Guaxupé | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE GUAXUPÉ - MG | AO JUÍZO DA [N]ª VARA CÍVEL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE GUAXUPÉ - MG | varas cíveis com competências diferentes: 1ª Vara Cível e da Infância e da Juventude; 2ª Vara Cível e de Cartas Precatórias Cíveis |
| Ibiá | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IBIÁ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE IBIÁ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Pratinha |
| Ibiraci | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IBIRACI - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE IBIRACI - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ibirité | ? | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE IBIRITÉ - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IBIRITÉ - MG |  |
| Igarapé | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IGARAPÉ - MG | AO JUÍZO DA [N]ª VARA CÍVEL E JUIZADO ESPECIAL CÍVEL DA COMARCA DE IGARAPÉ - MG | varas cíveis com competências diferentes: 1ª Vara Cível e Juizado Especial Cível; 2ª Vara Cível, da Infância e da Juventude e Juizado Especial Criminal; a fonte cita o Juizado Especial sem a unidade jurisdicional |
| Iguatama | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IGUATAMA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE IGUATAMA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Inhapim | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE INHAPIM - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE INHAPIM - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ipanema | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IPANEMA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE IPANEMA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ipatinga | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE IPATINGA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IPATINGA - MG |  |
| Itabira | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ITABIRA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITABIRA - MG |  |
| Itabirito | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITABIRITO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE ITABIRITO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Itaguara | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAGUARA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITAGUARA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Itajubá | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ITAJUBÁ - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITAJUBÁ - MG |  |
| Itamarandiba | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAMARANDIBA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITAMARANDIBA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Itambacuri | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAMBACURI - MG | AO JUÍZO DA VARA CÍVEL DA COMARCA DE ITAMBACURI - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Itamogi | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAMOGI - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITAMOGI - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Itamonte | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAMONTE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITAMONTE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Itanhandu | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITANHANDU - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITANHANDU - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Itanhomi | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITANHOMI - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITANHOMI - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Itapagipe | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAPAGIPE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITAPAGIPE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: São Francisco de Sales |
| Itapecerica | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITAPECERICA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITAPECERICA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Camacho, São Sebastião do Oeste |
| Itaúna | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ITAÚNA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITAÚNA - MG |  |
| Ituiutaba | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE ITUIUTABA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITUIUTABA - MG |  |
| Itumirim | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITUMIRIM - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE ITUMIRIM - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Iturama | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ITURAMA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ITURAMA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Jaboticatubas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JABOTICATUBAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE JABOTICATUBAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Jacinto | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JACINTO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE JACINTO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Jacuí | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JACUÍ - MG | AO JUÍZO DA VARA CÍVEL DA COMARCA DE JACUÍ - MG | a fonte não traz vara cível desta comarca; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Jacutinga | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JACUTINGA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE JACUTINGA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Jaíba | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JAÍBA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE JAÍBA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Janaúba | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE JANAÚBA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE JANAÚBA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais |
| Januária | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE JANUÁRIA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, DE FAMÍLIA E DE CARTAS PRECATÓRIAS CÍVEIS DA COMARCA DE JANUÁRIA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, de Família e de Cartas Precatórias Cíveis; 2ª Vara Cível e da Infância e da Juventude Cível |
| Jequeri | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JEQUERI - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE JEQUERI - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Jequitinhonha | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JEQUITINHONHA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE JEQUITINHONHA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| João Monlevade | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE JOÃO MONLEVADE - MG | AO JUÍZO DA [N]ª VARA CÍVEL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE JOÃO MONLEVADE - MG | varas cíveis com competências diferentes: 1ª Vara Cível e da Infância e da Juventude; 2ª Vara Cível e de Família, Sucessões e Ausências |
| João Pinheiro | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JOÃO PINHEIRO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE JOÃO PINHEIRO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Juatuba | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JUATUBA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE JUATUBA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Florestal |
| Juiz de Fora | Especial | AO JUÍZO DA [N]ª UNIDADE JURISDICIONAL CÍVEL DO JUIZADO ESPECIAL DA COMARCA DE JUIZ DE FORA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE JUIZ DE FORA - MG |  |
| Lagoa da Prata | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LAGOA DA PRATA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE LAGOA DA PRATA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte cita o Juizado Especial sem a unidade jurisdicional |
| Lagoa Santa | ? | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE LAGOA SANTA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE LAGOA SANTA - MG |  |
| Lajinha | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LAJINHA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE LAJINHA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Lambari | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LAMBARI - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE LAMBARI - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Lavras | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE LAVRAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE LAVRAS - MG |  |
| Leopoldina | ? | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE LEOPOLDINA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE LEOPOLDINA - MG |  |
| Lima Duarte | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LIMA DUARTE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE LIMA DUARTE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Luz | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LUZ - MG | AO JUÍZO DA VARA CÍVEL DA COMARCA DE LUZ - MG | a fonte não traz vara cível desta comarca; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Córrego Danta |
| Machado | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MACHADO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE MACHADO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Malacacheta | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MALACACHETA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MALACACHETA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Manga | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MANGA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MANGA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Manhuaçu | ? | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE MANHUAÇU - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MANHUAÇU - MG |  |
| Manhumirim | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MANHUMIRIM - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL, DA INFÂNCIA E DA JUVENTUDE E DO JUIZADO ESPECIAL DA COMARCA DE MANHUMIRIM - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal, da Infância e da Juventude e do Juizado Especial; 2ª Vara Cível, Criminal, de Execuções Penais e do Juizado Especial Criminal; a fonte cita o Juizado Especial sem a unidade jurisdicional; municípios achados fora da tabela da comarca, conferir: Martins Soares |
| Mantena | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE MANTENA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE MANTENA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude |
| Mar de Espanha | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MAR DE ESPANHA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MAR DE ESPANHA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Mariana | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MARIANA - MG | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MARIANA - MG | a fonte não traz vara cível desta comarca; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Martinho Campos | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MARTINHO CAMPOS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MARTINHO CAMPOS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Mateus Leme | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MATEUS LEME - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE MATEUS LEME - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Matias Barbosa | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MATIAS BARBOSA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MATIAS BARBOSA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Matozinhos | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MATOZINHOS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE MATOZINHOS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Medina | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MEDINA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MEDINA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Comercinho, Itaobim |
| Mercês | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MERCÊS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MERCÊS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Mesquita | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MESQUITA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MESQUITA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Minas Novas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MINAS NOVAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MINAS NOVAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Miradouro | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MIRADOURO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MIRADOURO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Miraí | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MIRAÍ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MIRAÍ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: São Sebastião da Vargem Alegre |
| Montalvânia | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MONTALVÂNIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MONTALVÂNIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Monte Alegre de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MONTE ALEGRE DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MONTE ALEGRE DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Monte Azul | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MONTE AZUL - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MONTE AZUL - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Monte Belo | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MONTE BELO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MONTE BELO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Monte Carmelo | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MONTE CARMELO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE MONTE CARMELO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Monte Santo de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MONTE SANTO DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MONTE SANTO DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Montes Claros | Especial | AO JUÍZO DA [N]ª UNIDADE JURISDICIONAL CÍVEL DO JUIZADO ESPECIAL DA COMARCA DE MONTES CLAROS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MONTES CLAROS - MG |  |
| Monte Sião | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MONTE SIÃO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MONTE SIÃO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Morada Nova de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MORADA NOVA DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MORADA NOVA DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Muriaé | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE MURIAÉ - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MURIAÉ - MG |  |
| Mutum | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MUTUM - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MUTUM - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Muzambinho | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MUZAMBINHO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE MUZAMBINHO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Nanuque | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE NANUQUE - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE NANUQUE - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais |
| Natércia | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NATÉRCIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE NATÉRCIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Nepomuceno | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NEPOMUCENO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE NEPOMUCENO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Nova Era | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NOVA ERA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE NOVA ERA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Bela Vista de Minas |
| Nova Lima | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE NOVA LIMA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE NOVA LIMA - MG |  |
| Nova Ponte | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NOVA PONTE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE NOVA PONTE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Nova Resende | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NOVA RESENDE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE NOVA RESENDE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Nova Serrana | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE NOVA SERRANA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE NOVA SERRANA - MG |  |
| Novo Cruzeiro | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NOVO CRUZEIRO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE NOVO CRUZEIRO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Oliveira | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE OLIVEIRA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE OLIVEIRA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude |
| Ouro Branco | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE OURO BRANCO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE OURO BRANCO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ouro Fino | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE OURO FINO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE OURO FINO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ouro Preto | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE OURO PRETO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE OURO PRETO - MG |  |
| Palma | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PALMA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PALMA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Paracatu | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE PARACATU - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PARACATU - MG |  |
| Pará de Minas | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE PARÁ DE MINAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PARÁ DE MINAS - MG |  |
| Paraguaçu | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PARAGUAÇU - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PARAGUAÇU - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Paraisópolis | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PARAISÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PARAISÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Paraopeba | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PARAOPEBA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PARAOPEBA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Passa Quatro | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PASSA QUATRO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PASSA QUATRO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Passa Tempo | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PASSA TEMPO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PASSA TEMPO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Passos | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE PASSOS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PASSOS - MG |  |
| Patos de Minas | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE PATOS DE MINAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PATOS DE MINAS - MG |  |
| Patrocínio | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE PATROCÍNIO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PATROCÍNIO - MG |  |
| Peçanha | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PEÇANHA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE PEÇANHA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Virgolândia |
| Pedra Azul | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PEDRA AZUL - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE PEDRA AZUL - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Pedralva | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PEDRALVA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PEDRALVA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Pedro Leopoldo | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE PEDRO LEOPOLDO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE PEDRO LEOPOLDO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais |
| Perdizes | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PERDIZES - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PERDIZES - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Perdões | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PERDÕES - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PERDÕES - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Piranga | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PIRANGA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PIRANGA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Pirapetinga | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PIRAPETINGA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PIRAPETINGA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Pirapora | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE PIRAPORA - MG | AO JUÍZO DA [N]ª VARA CÍVEL E DE FAMÍLIA DA COMARCA DE PIRAPORA - MG | varas cíveis com competências diferentes: 1ª Vara Cível e de Família; 2ª Vara Cível e da Infância e da Juventude |
| Pitangui | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PITANGUI - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL, E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE PITANGUI - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal, e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Criminais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Piumhi | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PIUMHI - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE PIUMHI - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Poço Fundo | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE POÇO FUNDO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE POÇO FUNDO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Poços de Caldas | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE POÇOS DE CALDAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE POÇOS DE CALDAS - MG |  |
| Pompéu | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE POMPÉU - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE POMPÉU - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ponte Nova | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE PONTE NOVA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PONTE NOVA - MG | municípios achados fora da tabela da comarca, conferir: Santa Cruz do Escalvado |
| Porteirinha | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PORTEIRINHA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PORTEIRINHA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade; municípios achados fora da tabela da comarca, conferir: Riacho dos Machados, Serranópolis de Minas |
| Pouso Alegre | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE POUSO ALEGRE - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE POUSO ALEGRE - MG |  |
| Prados | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PRADOS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PRADOS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Prata | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PRATA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PRATA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Pratápolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PRATÁPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PRATÁPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Presidente Olegário | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PRESIDENTE OLEGÁRIO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE PRESIDENTE OLEGÁRIO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Raul Soares | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RAUL SOARES - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RAUL SOARES - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Resende Costa | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RESENDE COSTA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RESENDE COSTA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Resplendor | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RESPLENDOR - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RESPLENDOR - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ribeirão das Neves | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE RIBEIRÃO DAS NEVES - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE RIBEIRÃO DAS NEVES - MG |  |
| Rio Casca | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO CASCA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO CASCA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Rio Novo | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO NOVO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO NOVO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Rio Paranaíba | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO PARANAÍBA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO PARANAÍBA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Rio Pardo de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO PARDO DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO PARDO DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Rio Piracicaba | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO PIRACICABA - MG | AO JUÍZO DA VARA CÍVEL DA COMARCA DE RIO PIRACICABA - MG | a fonte não traz vara cível desta comarca; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Rio Pomba | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO POMBA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO POMBA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Rio Preto | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO PRETO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO PRETO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Rio Vermelho | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO VERMELHO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE RIO VERMELHO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Sabará | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE SABARÁ - MG | AO JUÍZO DA [N]ª VARA CÍVEL E DA INFÂNCIA E DA 2ª VARA CÍVEL E DE EXECUÇÕES FISCAIS DA COMARCA DE SABARÁ - MG |  |
| Sabinópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SABINÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SABINÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Sacramento | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SACRAMENTO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE SACRAMENTO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Salinas | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SALINAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE SALINAS - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Santa Bárbara | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA BÁRBARA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SANTA BÁRBARA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Santa Luzia | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE SANTA LUZIA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SANTA LUZIA - MG |  |
| Santa Maria do Suaçuí | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA MARIA DO SUAÇUÍ - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SANTA MARIA DO SUAÇUÍ - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Santa Rita de Caldas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA RITA DE CALDAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SANTA RITA DE CALDAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Santa Rita do Sapucaí | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE SANTA RITA DO SAPUCAÍ - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE SANTA RITA DO SAPUCAÍ - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude |
| Santa Vitória | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA VITÓRIA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SANTA VITÓRIA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Santo Antônio do Monte | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTO ANTÔNIO DO MONTE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SANTO ANTÔNIO DO MONTE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Santos Dumont | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE SANTOS DUMONT - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE SANTOS DUMONT - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; municípios achados fora da tabela da comarca, conferir: Aracitaba, Ewbank da Câmara, Oliveira Fortes |
| São Domingos do Prata | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO DOMINGOS DO PRATA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO DOMINGOS DO PRATA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São Francisco | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO FRANCISCO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE SÃO FRANCISCO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São Gonçalo do Sapucaí | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO GONÇALO DO SAPUCAÍ - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE SÃO GONÇALO DO SAPUCAÍ - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São Gotardo | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO GOTARDO - MG | AO JUÍZO DA VARA CÍVEL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE SÃO GOTARDO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São João da Ponte | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOÃO DA PONTE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO JOÃO DA PONTE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São João del Rei | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE SÃO JOÃO DEL REI - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO JOÃO DEL REI - MG | municípios achados fora da tabela da comarca, conferir: Tiradentes |
| São João do Paraíso | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOÃO DO PARAÍSO - MG | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SÃO JOÃO DO PARAÍSO - MG | a fonte não traz vara cível desta comarca; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São João Evangelista | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOÃO EVANGELISTA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO JOÃO EVANGELISTA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São João Nepomuceno | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOÃO NEPOMUCENO - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DA INFÂNCIA E DA JUVENTUDE DA COMARCA DE SÃO JOÃO NEPOMUCENO - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e da Infância e da Juventude; 2ª Vara Cível, Criminal e de Execuções Penais; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São Lourenço | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE SÃO LOURENÇO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO LOURENÇO - MG |  |
| São Romão | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO ROMÃO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO ROMÃO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São Roque de Minas | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO ROQUE DE MINAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SÃO ROQUE DE MINAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| São Sebastião do Paraíso | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE SÃO SEBASTIÃO DO PARAÍSO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO SEBASTIÃO DO PARAÍSO - MG | municípios achados fora da tabela da comarca, conferir: São Tomás de Aquino |
| Senador Firmino | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SENADOR FIRMINO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SENADOR FIRMINO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Serro | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SERRO - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SERRO - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Sete Lagoas | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE SETE LAGOAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SETE LAGOAS - MG |  |
| Silvianópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SILVIANÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE SILVIANÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Taiobeiras | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TAIOBEIRAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TAIOBEIRAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Tarumirim | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TARUMIRIM - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TARUMIRIM - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Teixeiras | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TEIXEIRAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TEIXEIRAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Teófilo Otoni | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE TEÓFILO OTONI - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TEÓFILO OTONI - MG |  |
| Timóteo | ? | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE TIMÓTEO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TIMÓTEO - MG |  |
| Tiros | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TIROS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TIROS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Tombos | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TOMBOS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TOMBOS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Três Corações | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE TRÊS CORAÇÕES - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TRÊS CORAÇÕES - MG |  |
| Três Marias | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TRÊS MARIAS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TRÊS MARIAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Três Pontas | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TRÊS PONTAS - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TRÊS PONTAS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Tupaciguara | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TUPACIGUARA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE TUPACIGUARA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Turmalina | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TURMALINA - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE TURMALINA - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Ubá | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE UBÁ - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE UBÁ - MG |  |
| Uberaba | Especial | AO JUÍZO DA [N]ª UNIDADE JURISDICIONAL CÍVEL DO JUIZADO ESPECIAL DA COMARCA DE UBERABA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE UBERABA - MG |  |
| Uberlândia | ? | AO JUÍZO DA [N]ª UNIDADE JURISDICIONAL CÍVEL DO JUIZADO ESPECIAL DA COMARCA DE UBERLÂNDIA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE UBERLÂNDIA - MG |  |
| Unaí | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE UNAÍ - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE UNAÍ - MG |  |
| Varginha | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE VARGINHA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE VARGINHA - MG |  |
| Várzea da Palma | Segunda | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE VÁRZEA DA PALMA - MG | AO JUÍZO DA [N]ª VARA CÍVEL, CRIMINAL E DE EXECUÇÕES PENAIS DA COMARCA DE VÁRZEA DA PALMA - MG | varas cíveis com competências diferentes: 1ª Vara Cível, Criminal e de Execuções Penais; 2ª Vara Cível, Criminal e da Infância e da Juventude; a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Vazante | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE VAZANTE - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE VAZANTE - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Vespasiano | Especial | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE VESPASIANO - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE VESPASIANO - MG |  |
| Viçosa | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE VIÇOSA - MG | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE VIÇOSA - MG |  |
| Virginópolis | Primeira | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE VIRGINÓPOLIS - MG | AO JUÍZO DA VARA ÚNICA DA COMARCA DE VIRGINÓPOLIS - MG | a fonte não lista unidade do Juizado Especial nesta comarca: confira a unidade |
| Visconde do Rio Branco | Segunda | AO JUÍZO DA UNIDADE JURISDICIONAL ÚNICA DO JUIZADO ESPECIAL DA COMARCA DE VISCONDE DO RIO BRANCO - MG | AO JUÍZO DA VARA CÍVEL, DA INFÂNCIA E DA JUVENTUDE E DE PRECATÓRIAS DA COMARCA DE VISCONDE DO RIO BRANCO - MG | municípios achados fora da tabela da comarca, conferir: Guiricema |

## 4. Índice por município (852)

- Abadia dos Dourados → Coromandel
- Abaeté → Abaeté
- Abre Campo → Abre Campo
- Acaiaca → Ponte Nova
- Açucena → Açucena
- Água Boa → Capelinha
- Água Comprida → Uberaba
- Aguanil → Campo Belo
- Águas Formosas → Águas Formosas
- Águas Vermelhas → Pedra Azul
- Aimorés → Aimorés
- Aiuruoca → Aiuruoca
- Alagoa → Itamonte
- Albertina → Jacutinga
- Além Paraíba → Além Paraíba
- Alfenas → Alfenas
- Alfredo Vasconcelos → Barbacena
- Almenara → Almenara
- Alpercata → Governador Valadares
- Alpinópolis → Alpinópolis
- Alterosa → Areado
- Alto Caparaó → Manhumirim
- Alto Jequitibá → Manhumirim
- Alto Rio Doce → Alto Rio Doce
- Alvarenga → Tarumirim
- Alvinópolis → Alvinópolis
- Alvorada de Minas → Serro
- Andradas → Andradas
- Andrelândia → Andrelândia
- Angelândia → Capelinha
- Antônio Carlos → Barbacena
- Antônio Dias → Coronel Fabriciano
- Antônio Prado de Minas → Eugenópolis
- Araçaí → Paraopeba
- Aracitaba → Santos Dumont
- Araçuaí → Araçuaí
- Araguari → Araguari
- Arantina → Andrelândia
- Araponga → Ervália
- Araporã → Tupaciguara
- Arapuá → Rio Paranaíba
- Araújos → Nova Serrana
- Araxá → Araxá
- Arceburgo → Monte Santo de Minas
- Arcos → Arcos
- Areado → Areado
- Argirita → Leopoldina
- Aricanduva → Itamarandiba
- Arinos → Arinos
- Astolfo Dutra → Cataguases
- Ataléia → Teófilo Otoni
- Augusto de Lima → Buenópolis
- Baependi → Baependi
- Baldim → Sete Lagoas
- Bambuí → Bambuí
- Bandeira → Almenara
- Bandeira do Sul → Campestre
- Barão de Cocais → Barão de Cocais
- Barão do Monte Alto → Palma
- Barbacena → Barbacena
- Barra Longa → Ponte Nova
- Barroso → Barroso
- Bela Vista de Minas → Nova Era
- Belmiro Braga → Matias Barbosa
- Belo Horizonte → Belo Horizonte
- Belo Oriente → Açucena
- Belo Vale → Belo Vale
- Berilo → Minas Novas
- Berizal → Taiobeiras
- Bertópolis → Águas Formosas
- Betim → Betim
- Bias Fortes → Barbacena
- Bicas → Bicas
- Biquinhas → Morada Nova de Minas
- Boa Esperança → Boa Esperança
- Bocaina de Minas → Aiuruoca
- Bocaiúva → Bocaiúva
- Bom Despacho → Bom Despacho
- Bom Jardim de Minas → Andrelândia
- Bom Jesus da Penha → Nova Resende
- Bom Jesus do Amparo → Barão de Cocais
- Bom Jesus do Galho → Caratinga
- Bom Repouso → Cambuí
- Bom Sucesso → Bom Sucesso
- Bonfim → Bonfim
- Bonfinópolis de Minas → Bonfinópolis de Minas
- Bonito de Minas → Januária
- Borda da Mata → Borda da Mata
- Botelhos → Botelhos
- Botumirim → Grão Mogol
- Brasilândia de Minas → João Pinheiro
- Brasília de Minas → Brasília de Minas
- Brás Pires → Senador Firmino
- Braúnas → Mesquita
- Brazópolis → Brazópolis
- Brumadinho → Brumadinho
- Bueno Brandão → Bueno Brandão
- Buenópolis → Buenópolis
- Bugre → Inhapim
- Buritis → Buritis
- Buritizeiro → Pirapora
- Cabeceira Grande → Unaí
- Cabo Verde → Cabo Verde
- Cachoeira da Prata → Sete Lagoas
- Cachoeira de Minas → Cachoeira de Minas
- Cachoeira de Pajeú → Pedra Azul
- Cachoeira Dourada → Capinópolis
- Caetanópolis → Paraopeba
- Caeté → Caeté
- Caiana → Espera Feliz
- Cajuri → Viçosa
- Caldas → Caldas
- Camacho → Itapecerica
- Camanducaia → Camanducaia
- Cambuí → Cambuí
- Cambuquira → Cambuquira
- Campanário → Itambacuri
- Campanha → Campanha
- Campestre → Campestre
- Campina Verde → Campina Verde
- Campo Azul → Brasília de Minas
- Campo Belo → Campo Belo
- Campo do Meio → Campos Gerais
- Campo Florido → Uberaba
- Campos Altos → Campos Altos
- Campos Gerais → Campos Gerais
- Canaã → Viçosa
- Canápolis → Canápolis
- Cana Verde → Perdões
- Candeias → Candeias
- Cantagalo → Peçanha
- Caparaó → Espera Feliz
- Capela Nova → Carandaí
- Capelinha → Capelinha
- Capetinga → Cássia
- Capim Branco → Matozinhos
- Capinópolis → Capinópolis
- Capitão Andrade → Itanhomi
- Capitão Enéas → Francisco Sá
- Capitólio → Piumhi
- Caputira → Abre Campo
- Caraí → Novo Cruzeiro
- Caranaíba → Carandaí
- Carandaí → Carandaí
- Carangola → Carangola
- Caratinga → Caratinga
- Carbonita → Itamarandiba
- Careaçu → São Gonçalo do Sapucaí
- Carlos Chagas → Carlos Chagas
- Carmésia → Ferros
- Carmo da Cachoeira → Varginha
- Carmo da Mata → Carmo da Mata
- Carmo de Minas → Carmo de Minas
- Carmo do Cajuru → Carmo do Cajuru
- Carmo do Paranaíba → Carmo do Paranaíba
- Carmo do Rio Claro → Carmo do Rio Claro
- Carmópolis de Minas → Carmópolis de Minas
- Carneirinho → Iturama
- Carrancas → Itumirim
- Carvalhópolis → Machado
- Carvalhos → Aiuruoca
- Casa Grande → Conselheiro Lafaiete
- Cascalho Rico → Estrela do Sul
- Cássia → Cássia
- Cataguases → Cataguases
- Catas Altas → Santa Bárbara
- Catas Altas da Noruega → Conselheiro Lafaiete
- Catuji → Novo Cruzeiro
- Catuti → Porteirinha
- Caxambu → Caxambu
- Cedro do Abaeté → Abaeté
- Central de Minas → Mantena
- Centralina → Canápolis
- Chácara → Juiz de Fora
- Chalé → Lajinha
- Chapada do Norte → Minas Novas
- Chapada Gaúcha → Arinos
- Chiador → Mar de Espanha
- Cipotânea → Alto Rio Doce
- Claraval → Ibiraci
- Claro dos Poções → Montes Claros
- Cláudio → Cláudio
- Coimbra → Viçosa
- Coluna → São João Evangelista
- Comendador Gomes → Frutal
- Comercinho → Medina
- Conceição da Aparecida → Carmo do Rio Claro
- Conceição da Barra de Minas → São João del Rei
- Conceição das Alagoas → Conceição das Alagoas
- Conceição das Pedras → Natércia
- Conceição de Ipanema → Ipanema
- Conceição do Mato Dentro → Conceição do Mato Dentro
- Conceição do Pará → Pitangui
- Conceição do Rio Verde → Conceição do Rio Verde
- Conceição dos Ouros → Cachoeira de Minas
- Cônego Marinho → Januária
- Confins → Pedro Leopoldo
- Congonhal → Pouso Alegre
- Congonhas → Congonhas
- Congonhas do Norte → Conceição do Mato Dentro
- Conquista → Conquista
- Conselheiro Lafaiete → Conselheiro Lafaiete
- Conselheiro Pena → Conselheiro Pena
- Consolação → Paraisópolis
- Contagem → Contagem
- Coqueiral → Boa Esperança
- Coração de Jesus → Coração de Jesus
- Cordisburgo → Paraopeba
- Cordislândia → São Gonçalo do Sapucaí
- Corinto → Corinto
- Coroaci → Peçanha
- Coromandel → Coromandel
- Coronel Fabriciano → Coronel Fabriciano
- Coronel Murta → Araçuaí
- Coronel Pacheco → Juiz de Fora
- Coronel Xavier Chaves → Resende Costa
- Córrego Danta → Luz
- Córrego do Bom Jesus → Cambuí
- Córrego Fundo → Formiga
- Córrego Novo → Caratinga
- Couto de Magalhães de Minas → Diamantina
- Crisólita → Águas Formosas
- Cristais → Campo Belo
- Cristália → Grão Mogol
- Cristiano Otoni → Conselheiro Lafaiete
- Cristina → Cristina
- Crucilândia → Bonfim
- Cruzeiro da Fortaleza → Patrocínio
- Cruzília → Cruzília
- Cuparaque → Conselheiro Pena
- Curral de Dentro → Taiobeiras
- Curvelo → Curvelo
- Datas → Diamantina
- Delfim Moreira → Itajubá
- Delfinópolis → Cássia
- Delta → Uberaba
- Descoberto → São João Nepomuceno
- Desterro de Entre Rios → Entre Rios de Minas
- Desterro do Melo → Barbacena
- Diamantina → Diamantina
- Diogo de Vasconcelos → Mar de Espanha
- Dionísio → São Domingos do Prata
- Divinésia → Ubá
- Divino → Divino
- Divino das Laranjeiras → Galiléia
- Divinolândia de Minas → Virginópolis
- Divinópolis → Divinópolis
- Divisa Alegre → Pedra Azul
- Divisa Nova → Cabo Verde
- Divisópolis → Almenara
- Dom Bosco → Bonfinópolis de Minas
- Dom Cavati → Inhapim
- Dom Joaquim → Conceição do Mato Dentro
- Dom Silvério → Alvinópolis
- Dom Viçoso → Carmo de Minas
- Dona Euzébia → Cataguases
- Dores de Campos → Prados
- Dores de Guanhães → Guanhães
- Dores do Indaiá → Dores do Indaiá
- Dores do Turvo → Senador Firmino
- Doresópolis → Piumhi
- Douradoquara → Monte Carmelo
- Durandé → Manhumirim
- Elói Mendes → Elói Mendes
- Engenheiro Caldas → Tarumirim
- Engenheiro Navarro → Bocaiúva
- Entre Folhas → Caratinga
- Entre Rios de Minas → Entre Rios de Minas
- Ervália → Ervália
- Esmeraldas → Esmeraldas
- Espera Feliz → Espera Feliz
- Espinosa → Espinosa
- Espírito Santo do Dourado → Silvianópolis
- Estiva → Pouso Alegre
- Estrela Dalva → Pirapetinga
- Estrela do Indaiá → Dores do Indaiá
- Estrela do Sul → Estrela do Sul
- Eugenópolis → Eugenópolis
- Ewbank da Câmara → Santos Dumont
- Extrema → Extrema
- Fama → Paraguaçu
- Faria Lemos → Carangola
- Felício dos Santos → Diamantina
- Felisburgo → Jequitinhonha
- Felixlândia → Curvelo
- Fernandes Tourinho → Tarumirim
- Ferros → Ferros
- Fervedouro → Carangola
- Florestal → Juatuba
- Formiga → Formiga
- Formoso → Buritis
- Fortaleza de Minas → Jacinto
- Fortuna de Minas → Sete Lagoas
- Francisco Badaró → Minas Novas
- Francisco Dumont → Bocaiúva
- Franciscópolis → Malacacheta
- Francisco Sá → Francisco Sá
- Frei Gaspar → Itambacuri
- Frei Inocêncio → Governador Valadares
- Frei Lagonegro → Peçanha
- Fronteira → Frutal
- Fronteira dos Vales → Águas Formosas
- Fruta de Leite → Salinas
- Frutal → Frutal
- Funilândia → Sete Lagoas
- Galiléia → Galiléia
- Gameleiras → Monte Azul
- Glaucilândia → Montes Claros
- Goiabeira → Conselheiro Pena
- Goianá → Rio Novo
- Gonçalves → Paraisópolis
- Gonzaga → Virginópolis
- Gouveia → Diamantina
- Governador Valadares → Governador Valadares
- Grão Mogol → Grão Mogol
- Grupiara → Estrela do Sul
- Guanhães → Guanhães
- Guapé → Guanhães
- Guaraciaba → Ponte Nova
- Guaraciama → Bocaiúva
- Guaranésia → Guaranésia
- Guarani → Guarani
- Guarará → Bicas
- Guarda-Mor → Vazante
- Guaxupé → Guaxupé
- Guidoval → Ubá
- Guimarânia → Patrocínio
- Guiricema → Visconde do Rio Branco
- Gurinhatã → Ituiutaba
- Heliodora → Natércia
- Iapu → Inhapim
- Ibertioga → Barbacena
- Ibiá → Ibiá
- Ibiaí → Coração de Jesus
- Ibiracatu → São João da Ponte
- Ibiraci → Ibiraci
- Ibirité → Ibirité
- Ibitiúra de Minas → Andradas
- Ibituruna → Bom Sucesso
- Icaraí de Minas → São Francisco
- Igarapé → Igarapé
- Igaratinga → Pará de Minas
- Iguatama → Iguatama
- Ijaci → Lavras
- Ilicínea → Boa Esperança
- Imbé de Minas → Caratinga
- Inconfidentes → Ouro Fino
- Indaiabira → Taiobeiras
- Indianópolis → Araguari
- Ingaí → Itumirim
- Inhapim → Inhapim
- Inhaúma → Sete Lagoas
- Inimutaba → Curvelo
- Ipaba → Ipatinga
- Ipanema → Ipanema
- Ipatinga → Ipatinga
- Ipiaçu → Capinópolis
- Ipuiúna → Santa Rita de Caldas
- Iraí de Minas → Monte Carmelo
- Itabira → Itabira
- Itabirinha → Mantena
- Itabirito → Itabirito
- Itacambira → Montes Claros
- Itacarambi → Januária
- Itaguara → Itaguara
- Itaipé → Novo Cruzeiro
- Itajubá → Itajubá
- Itamarandiba → Itamarandiba
- Itamarati de Minas → Cataguases
- Itambacuri → Itambacuri
- Itambé do Mato Dentro → Itabira
- Itamogi → Itamogi
- Itamonte → Itamonte
- Itanhandu → Itanhandu
- Itanhomi → Itanhomi
- Itaobim → Medina
- Itapagipe → Itapagipe
- Itapecerica → Itapecerica
- Itapeva → Camanducaia
- Itatiaiuçu → Itaúna
- Itaú de Minas → Pratápolis
- Itaúna → Itaúna
- Itaverava → Conselheiro Lafaiete
- Itinga → Araçuaí
- Itueta → Resplendor
- Ituiutaba → Ituiutaba
- Itumirim → Itumirim
- Iturama → Iturama
- Itutinga → Itumirim
- Jaboticatubas → Jaboticatubas
- Jacinto → Jacinto
- Jacuí → Jacuí
- Jacutinga → Jacutinga
- Jaguaraçu → Timóteo
- Jaíba → Jaíba
- Jampruca → Itambacuri
- Janaúba → Janaúba
- Januária → Januária
- Japaraíba → Lagoa da Prata
- Japonvar → Brasília de Minas
- Jeceaba → Entre Rios de Minas
- Jenipapo de Minas → Minas Novas
- Jequeri → Jequeri
- Jequitaí → Pirapora
- Jequitibá → Sete Lagoas
- Jequitinhonha → Jequitinhonha
- Jesuânia → Lambari
- Joaíma → Jequitinhonha
- Joanésia → Mesquita
- João Monlevade → João Monlevade
- João Pinheiro → João Pinheiro
- Joaquim Felício → Buenópolis
- Jordânia → Jacinto
- José Gonçalves de Minas → Turmalina
- Josenópolis → Grão Mogol
- José Raydan → Santa Maria do Suaçuí
- Juatuba → Juatuba
- Juiz de Fora → Juiz de Fora
- Juramento → Montes Claros
- Juruaia → Muzambinho
- Juvenília → Montalvânia
- Ladainha → Teófilo Otoni
- Lagamar → Presidente Olegário
- Lagoa da Prata → Lagoa da Prata
- Lagoa dos Patos → Coração de Jesus
- Lagoa Dourada → São João del Rei
- Lagoa Formosa → Patos de Minas
- Lagoa Grande → Presidente Olegário
- Lagoa Santa → Lagoa Santa
- Lajinha → Lajinha
- Lambari → Lambari
- Lamim → Conselheiro Lafaiete
- Laranjal → Muriaé
- Lassance → Várzea da Palma
- Lavras → Lavras
- Leandro Ferreira → Pitangui
- Leme do Prado → Turmalina
- Leopoldina → Leopoldina
- Liberdade → Aiuruoca
- Lima Duarte → Lima Duarte
- Limeira do Oeste → Iturama
- Lontra → São João da Ponte
- Luisburgo → Manhuaçu
- Luislândia → Brasília de Minas
- Luminárias → Lavras
- Luz → Luz
- Machacalis → Águas Formosas
- Machado → Machado
- Madre de Deus de Minas → Andrelândia
- Malacacheta → Malacacheta
- Mamonas → Espinosa
- Manga → Manga
- Manhuaçu → Manhuaçu
- Manhumirim → Manhumirim
- Mantena → Mantena
- Maravilhas → Pitangui
- Mar de Espanha → Mar de Espanha
- Maria da Fé → Cristina
- Mariana → Mariana
- Marilac → Governador Valadares
- Mário Campos → Ibirité
- Maripá de Minas → Bicas
- Marliéria → Timóteo
- Marmelópolis → Itajubá
- Martinho Campos → Martinho Campos
- Martins Soares → Manhumirim
- Mata Verde → Almenara
- Materlândia → Sabinópolis
- Mateus Leme → Mateus Leme
- Mathias Lobato → Governador Valadares
- Matias Barbosa → Matias Barbosa
- Matias Cardoso → Jaíba
- Matipó → Abre Campo
- Mato Verde → Monte Azul
- Matozinhos → Matozinhos
- Matutina → São Gotardo
- Medeiros → Bambuí
- Medina → Medina
- Mendes Pimentel → Mantena
- Mercês → Mercês
- Mesquita → Mesquita
- Minas Novas → Minas Novas
- Minduri → Cruzília
- Mirabela → Montes Claros
- Miradouro → Miradouro
- Miraí → Miraí
- Miravânia → Manga
- Moeda → Belo Vale
- Moema → Bom Despacho
- Monjolos → Diamantina
- Monsenhor Paulo → Campanha
- Montalvânia → Montalvânia
- Monte Alegre de Minas → Monte Alegre de Minas
- Monte Azul → Monte Azul
- Monte Belo → Monte Belo
- Monte Carmelo → Monte Carmelo
- Monte Formoso → Jequitinhonha
- Monte Santo de Minas → Monte Santo de Minas
- Montes Claros → Montes Claros
- Monte Sião → Monte Sião
- Montezuma → Rio Pardo de Minas
- Morada Nova de Minas → Morada Nova de Minas
- Morro da Garça → Curvelo
- Morro do Pilar → Conceição do Mato Dentro
- Munhoz → Bueno Brandão
- Muriaé → Muriaé
- Mutum → Mutum
- Muzambinho → Muzambinho
- Nacip Raydan → Peçanha
- Nanuque → Nanuque
- Naque → Açucena
- Natalândia → Bonfinópolis de Minas
- Natércia → Natércia
- Nazareno → São João del Rei
- Nepomuceno → Nepomuceno
- Ninheira → São João del Rei
- Nova Belém → Mantena
- Nova Era → Nova Era
- Nova Lima → Nova Lima
- Nova Módica → Itambacuri
- Nova Ponte → Nova Ponte
- Nova Porteirinha → Janaúba
- Nova Resende → Nova Resende
- Nova Serrana → Nova Serrana
- Nova União → Caeté
- Novo Cruzeiro → Novo Cruzeiro
- Novo Oriente de Minas → Teófilo Otoni
- Novorizonte → Salinas
- Olaria → Lima Duarte
- Olhos-d'Água → Bocaiúva
- Olímpio Noronha → Lambari
- Oliveira → Oliveira
- Oliveira Fortes → Santos Dumont
- Onça de Pitangui → Pará de Minas
- Oratórios → Ponte Nova
- Orizânia → Divino
- Ouro Branco → Ouro Branco
- Ouro Fino → Ouro Fino
- Ouro Preto → Ouro Preto
- Ouro Verde de Minas → Teófilo Otoni
- Padre Carvalho → Salinas
- Padre Paraíso → Araçuaí
- Paineiras → Abaeté
- Pains → Arcos
- Pai Pedro → Porteirinha
- Paiva → Santos Dumont
- Palma → Palma
- Palmópolis → Almenara
- Papagaios → Pitangui
- Paracatu → Paracatu
- Pará de Minas → Pará de Minas
- Paraguaçu → Paraguaçu
- Paraisópolis → Paraisópolis
- Paraopeba → Paraopeba
- Passabém → Ferros
- Passa Quatro → Passa Quatro
- Passa Tempo → Passa Tempo
- Passa Vinte → Aiuruoca
- Passos → Passos
- Patis → Montes Claros
- Patos de Minas → Patos de Minas
- Patrocínio → Patrocínio
- Patrocínio do Muriaé → Eugenópolis
- Paula Cândido → Viçosa
- Paulistas → São João Evangelista
- Pavão → Teófilo Otoni
- Peçanha → Peçanha
- Pedra Azul → Pedra Azul
- Pedra Bonita → Abre Campo
- Pedra do Anta → Teixeiras
- Pedra do Indaiá → Santo Antônio do Monte
- Pedra Dourada → Tombos
- Pedralva → Pedralva
- Pedras de Maria da Cruz → Januária
- Pedrinópolis → Perdizes
- Pedro Leopoldo → Pedro Leopoldo
- Pedro Teixeira → Lima Duarte
- Pequeri → Bicas
- Pequi → Pará de Minas
- Perdigão → Nova Serrana
- Perdizes → Perdizes
- Perdões → Perdões
- Periquito → Governador Valadares
- Pescador → Itambacuri
- Piau → Rio Novo
- Piedade de Caratinga → Caratinga
- Piedade de Ponte Nova → Jequeri
- Piedade do Rio Grande → Barbacena
- Piedade dos Gerais → Bonfim
- Pimenta → Formiga
- Pingo-d'Água → Caratinga
- Pintópolis → São Francisco
- Piracema → Passa Tempo
- Pirajuba → Conceição das Alagoas
- Piranga → Piranga
- Piranguçu → Itajubá
- Piranguinho → Brazópolis
- Pirapetinga → Pirapetinga
- Pirapora → Pirapora
- Piraúba → Guarani
- Pitangui → Pitangui
- Piumhi → Piumhi
- Planura → Frutal
- Poço Fundo → Poço Fundo
- Poços de Caldas → Poços de Caldas
- Pocrane → Ipanema
- Pompéu → Pompéu
- Ponte Nova → Ponte Nova
- Ponto Chique → Brasília de Minas
- Ponto dos Volantes → Araçuaí
- Porteirinha → Porteirinha
- Porto Firme → Piranga
- Poté → Teófilo Otoni
- Pouso Alegre → Pouso Alegre
- Pouso Alto → São Lourenço
- Prados → Prados
- Prata → Prata
- Pratápolis → Pratápolis
- Pratinha → Ibiá
- Presidente Bernardes → Piranga
- Presidente Juscelino → Curvelo
- Presidente Kubitschek → Diamantina
- Presidente Olegário → Presidente Olegário
- Prudente de Morais → Matozinhos
- Quartel Geral → Dores do Indaiá
- Queluzito → Conselheiro Lafaiete
- Raposos → Nova Lima
- Raul Soares → Raul Soares
- Recreio → Leopoldina
- Reduto → Manhuaçu
- Resende Costa → Resende Costa
- Resplendor → Resplendor
- Ressaquinha → Barbacena
- Riachinho → Bonfinópolis de Minas
- Riacho dos Machados → Porteirinha
- Ribeirão das Neves → Ribeirão das Neves
- Ribeirão Vermelho → Lavras
- Rio Acima → Nova Lima
- Rio Casca → Rio Casca
- Rio Doce → Ponte Nova
- Rio do Prado → Almenara
- Rio Espera → Conselheiro Lafaiete
- Rio Manso → Bonfim
- Rio Novo → Rio Novo
- Rio Paranaíba → Rio Paranaíba
- Rio Pardo de Minas → Rio Pardo de Minas
- Rio Piracicaba → Rio Piracicaba
- Rio Pomba → Rio Pomba
- Rio Preto → Rio Preto
- Rio Vermelho → Rio Vermelho
- Ritápolis → São João del Rei
- Rochedo de Minas → São João Nepomuceno
- Rodeiro → Ubá
- Romaria → Monte Carmelo
- Rosário da Limeira → Muriaé
- Rubelita → Salinas
- Rubim → Almenara
- Sabará → Sabará
- Sabinópolis → Sabinópolis
- Sacramento → Sacramento
- Salinas → Salinas
- Salto da Divisa → Jacinto
- Santa Bárbara → Santa Bárbara
- Santa Bárbara do Leste → Caratinga
- Santa Bárbara do Monte Verde → Rio Preto
- Santa Bárbara do Tugúrio → Barbacena
- Santa Cruz de Minas → São João del Rei
- Santa Cruz de Salinas → Salinas
- Santa Cruz do Escalvado → Ponte Nova
- Santa Efigênia de Minas → Virginópolis
- Santa Fé de Minas → São Romão
- Santa Helena de Minas → Águas Formosas
- Santa Juliana → Nova Ponte
- Santa Luzia → Santa Luzia
- Santa Margarida → Abre Campo
- Santa Maria de Itabira → Itabira
- Santa Maria do Salto → Jacinto
- Santa Maria do Suaçuí → Santa Maria do Suaçuí
- Santana da Vargem → Três Pontas
- Santana de Cataguases → Cataguases
- Santana de Pirapama → Sete Lagoas
- Santana do Deserto → Matias Barbosa
- Santana do Garambéu → Barbacena
- Santana do Jacaré → Campo Belo
- Santana do Manhuaçu → Manhuaçu
- Santana do Paraíso → Ipatinga
- Santana do Riacho → Jaboticatubas
- Santana dos Montes → Conselheiro Lafaiete
- Santa Rita de Caldas → Santa Rita de Caldas
- Santa Rita de Ibitipoca → Barbacena
- Santa Rita de Jacutinga → Rio Preto
- Santa Rita de Minas → Caratinga
- Santa Rita do Itueto → Resplendor
- Santa Rita do Sapucaí → Santa Rita do Sapucaí
- Santa Rosa da Serra → Campos Altos
- Santa Vitória → Santa Vitória
- Santo Antônio do Amparo → Bom Sucesso
- Santo Antônio do Aventureiro → Além Paraíba
- Santo Antônio do Grama → Rio Casca
- Santo Antônio do Itambé → Serro
- Santo Antônio do Jacinto → Jacinto
- Santo Antônio do Monte → Santo Antônio do Monte
- Santo Antônio do Retiro → Rio Pardo de Minas
- Santo Antônio do Rio Abaixo → Ferros
- Santo Hipólito → Corinto
- Santos Dumont → Santos Dumont
- São Bento Abade → Três Corações
- São Brás do Suaçuí → Entre Rios de Minas
- São Domingos das Dores → Inhapim
- São Domingos do Prata → São Domingos do Prata
- São Félix de Minas → Mantena
- São Francisco → São Francisco
- São Francisco de Paula → Oliveira
- São Francisco de Sales → Itapagipe
- São Francisco do Glória → Miradouro
- São Geraldo → Coração de Jesus
- São Geraldo da Piedade → Governador Valadares
- São Geraldo do Baixio → Galiléia
- São Gonçalo do Abaeté → Patos de Minas
- São Gonçalo do Pará → Pará de Minas
- São Gonçalo do Rio Abaixo → Santa Bárbara
- São Gonçalo do Rio Preto → Diamantina
- São Gonçalo do Sapucaí → São Gonçalo do Sapucaí
- São Gotardo → São Gotardo
- São João Batista do Glória → Passos
- São João da Lagoa → Coração de Jesus
- São João da Mata → Silvianópolis
- São João da Ponte → São João da Ponte
- São João das Missões → Manga
- São João del Rei → São João del Rei
- São João do Manhuaçu → Manhuaçu
- São João do Manteninha → Mantena
- São João do Oriente → Inhapim
- São João do Pacuí → Coração de Jesus
- São João do Paraíso → São João do Paraíso
- São João Evangelista → São João Evangelista
- São João Nepomuceno → São João Nepomuceno
- São Joaquim de Bicas → Igarapé
- São José da Barra → Alpinópolis
- São José da Lapa → Vespasiano
- São José da Safira → Governador Valadares
- São José da Varginha → Pará de Minas
- São José do Alegre → Pedralva
- São José do Divino → Itambacuri
- São José do Goiabal → São Domingos do Prata
- São José do Jacuri → Peçanha
- São José do Mantimento → Lajinha
- São Lourenço → São Lourenço
- São Miguel do Anta → Viçosa
- São Pedro da União → Guaxupé
- São Pedro dos Ferros → Rio Casca
- São Pedro do Suaçuí → Peçanha
- São Romão → São Romão
- São Roque de Minas → São Roque de Minas
- São Sebastião da Bela Vista → Santa Rita do Sapucaí
- São Sebastião da Vargem Alegre → Miraí
- São Sebastião do Anta → Inhapim
- São Sebastião do Maranhão → Santa Maria do Suaçuí
- São Sebastião do Oeste → Itapecerica
- São Sebastião do Paraíso → São Sebastião do Paraíso
- São Sebastião do Rio Preto → Ferros
- São Sebastião do Rio Verde → São Lourenço
- São Tiago → São João del Rei
- São Tomás de Aquino → São Sebastião do Paraíso
- São Tomé das Letras → Três Corações
- São Vicente de Minas → Andrelândia
- Sapucaí-Mirim → Paraisópolis
- Sardoá → Virginópolis
- Sarzedo → Ibirité
- Sem-Peixe → Alvinópolis
- Senador Amaral → Cambuí
- Senador Cortes → Mar de Espanha
- Senador Firmino → Senador Firmino
- Senador José Bento → Pouso Alegre
- Senador Modestino Gonçalves → Diamantina
- Senhora de Oliveira → Piranga
- Senhora do Porto → Guanhães
- Senhora dos Remédios → Barbacena
- Sericita → Abre Campo
- Seritinga → Aiuruoca
- Serra Azul de Minas → Serro
- Serra da Saudade → Dores do Indaiá
- Serra dos Aimorés → Nanuque
- Serra do Salitre → Patrocínio
- Serrania → Alfenas
- Serranópolis de Minas → Porteirinha
- Serranos → Aiuruoca
- Serro → Serro
- Sete Lagoas → Sete Lagoas
- Setubinha → Malacacheta
- Silveirânia → Rio Pomba
- Silvianópolis → Silvianópolis
- Simão Pereira → Matias Barbosa
- Simonésia → Manhuaçu
- Sobrália → Tarumirim
- Soledade de Minas → São Lourenço
- Tabuleiro → Rio Pomba
- Taiobeiras → Taiobeiras
- Taparuba → Ipanema
- Tapira → Araxá
- Tapiraí → Bambuí
- Taquaraçu de Minas → Caeté
- Tarumirim → Tarumirim
- Teixeiras → Teixeiras
- Teófilo Otoni → Teófilo Otoni
- Timóteo → Timóteo
- Tiradentes → São João del Rei
- Tiros → Tiros
- Tocantins → Ubá
- Tocos do Moji → Borda da Mata
- Toledo → Extrema
- Tombos → Tombos
- Três Corações → Três Corações
- Três Marias → Três Marias
- Três Pontas → Três Pontas
- Tumiritinga → Conselheiro Pena
- Tupaciguara → Tupaciguara
- Turmalina → Turmalina
- Turvolândia → Silvianópolis
- Ubá → Ubá
- Ubaí → Brasília de Minas
- Ubaporanga → Caratinga
- Uberaba → Uberaba
- Uberlândia → Uberlândia
- Umburatiba → Águas Formosas
- Unaí → Unaí
- União de Minas → Iturama
- Uruana de Minas → Arinos
- Urucânia → Jequeri
- Urucuia → Arinos
- Vargem Alegre → Caratinga
- Vargem Bonita → São Roque de Minas
- Vargem Grande do Rio Pardo → Rio Pardo de Minas
- Varginha → Varginha
- Varjão de Minas → Patos de Minas
- Várzea da Palma → Várzea da Palma
- Varzelândia → São João da Ponte
- Vazante → Vazante
- Verdelândia → Janaúba
- Veredinha → Turmalina
- Veríssimo → Uberaba
- Vermelho Novo → Raul Soares
- Vespasiano → Vespasiano
- Viçosa → Viçosa
- Vieiras → Miradouro
- Virgem da Lapa → Araçuaí
- Virgínia → Itanhandu
- Virginópolis → Virginópolis
- Virgolândia → Peçanha
- Visconde do Rio Branco → Visconde do Rio Branco
- Volta Grande → Além Paraíba
- Wenceslau Braz → Itajubá
