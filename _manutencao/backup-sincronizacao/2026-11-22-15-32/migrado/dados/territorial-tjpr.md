# Base territorial do TJPR (Paraná) para o endereçamento (comarcas e unidades)

> Fonte: TJPR: "Fóruns e Juizados Especiais (endereços e telefones)", arquivo fornecido pelo escritório (_manutencao/coleta/tjpr/fonte-tjpr-foruns-juizados.md), recebido em 22/11/2026. Municípios conferidos com a lista do IBGE (API de localidades, consulta em 22/11/2026). Gerado por `_manutencao/coleta/territorial_ufs.py`.
> Só dados de unidade. Telefones e endereços dos fóruns ficam na fonte.

## 1. Regra de endereçamento

1. **Ache a comarca** do município de residência do autor no índice da seção 4 (`grep -n "Nome do município"`). A comarca nem sempre é o próprio município.
2. O endereçamento pronto do JEC e da Justiça Comum está em `references/dados/tjpr_unidades.json` (`jec.enderecamento`, `comum.enderecamento`); `[N]` é o número da unidade, que sai na distribuição (`__`).
3. A cidade do fecho é a sede da comarca (ou do foro), com a UF: `sede - PR`.
4. Linha com "conferir" vira pendência da triagem: o advogado confirma a unidade antes de protocolar.
5. Réu Caixa: Justiça Federal (TRF4), que **não tem tabela** neste pacote: a subseção é pendência a conferir.

**Pendente de aprovação do escritório** (a forma do endereçamento destes estados ainda não foi aprovada, como foi a do TJBA em 03/11/2026).

## 2. Limites da fonte

- A fonte traz só os Juizados (unidade, endereço e jurisdição). A vara cível da Justiça Comum não consta: o endereçamento da Justiça Comum é genérico e marcado "conferir".
- Região Metropolitana de Curitiba: Curitiba (Foro Central) e os foros regionais aparecem como unidades próprias, com o fecho na cidade do foro.

Municípios a conferir:

- Pinhal de São Bento: consta das jurisdições de Ampére e Santo Antônio do Sudoeste: confira a comarca
- Saudade do Iguaçu: consta das jurisdições de Chopinzinho e São João: confira a comarca
- Sulina: consta das jurisdições de Chopinzinho e São João: confira a comarca
- São Jorge d'Oeste: consta das jurisdições de Dois Vizinhos e São João: confira a comarca

## 3. Comarcas (159)

| Comarca | Entrância | JEC | Justiça Comum | Conferir |
|---|---|---|---|---|
| Almirante Tamandaré | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE ALMIRANTE TAMANDARÉ DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE ALMIRANTE TAMANDARÉ DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Altônia | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ALTÔNIA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE ALTÔNIA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Alto Paraná | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ALTO PARANÁ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE ALTO PARANÁ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Alto Piquiri | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ALTO PIQUIRI - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE ALTO PIQUIRI - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ampére | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE AMPÉRE - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE AMPÉRE - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Andirá | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ANDIRÁ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ANDIRÁ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Antonina | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ANTONINA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ANTONINA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Apucarana | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE APUCARANA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE APUCARANA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Arapongas | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ARAPONGAS - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ARAPONGAS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Arapoti | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ARAPOTI - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE ARAPOTI - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Araucária | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE ARAUCÁRIA DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE ARAUCÁRIA DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Assaí | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ASSAÍ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ASSAÍ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Assis Chateaubriand | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ASSIS CHATEAUBRIAND - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ASSIS CHATEAUBRIAND - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Astorga | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ASTORGA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ASTORGA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Bandeirantes | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BANDEIRANTES - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BANDEIRANTES - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Barbosa Ferraz | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BARBOSA FERRAZ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE BARBOSA FERRAZ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Barracão | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BARRACÃO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE BARRACÃO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Bela Vista do Paraíso | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BELA VISTA DO PARAÍSO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE BELA VISTA DO PARAÍSO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Bocaiúva do Sul | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE BOCAIÚVA DO SUL - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE BOCAIÚVA DO SUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cambará | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMBARÁ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CAMBARÁ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cambé | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMBÉ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CAMBÉ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Campina da Lagoa | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPINA DA LAGOA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CAMPINA DA LAGOA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Campina Grande do Sul | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE CAMPINA GRANDE DO SUL DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE CAMPINA GRANDE DO SUL DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Campo Largo | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE CAMPO LARGO DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE CAMPO LARGO DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Campo Mourão | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAMPO MOURÃO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CAMPO MOURÃO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cândido de Abreu | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CÂNDIDO DE ABREU - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CÂNDIDO DE ABREU - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cantagalo | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CANTAGALO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CANTAGALO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Capanema | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAPANEMA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CAPANEMA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Capitão Leônidas Marques | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CAPITÃO LEÔNIDAS MARQUES - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CAPITÃO LEÔNIDAS MARQUES - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Carlópolis | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CARLÓPOLIS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CARLÓPOLIS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cascavel | Final | AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL DA COMARCA DE CASCAVEL - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CASCAVEL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Castro | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CASTRO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CASTRO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Catanduvas | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CATANDUVAS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CATANDUVAS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Centenário do Sul | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CENTENÁRIO DO SUL - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CENTENÁRIO DO SUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cerro Azul | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CERRO AZUL - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CERRO AZUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Chopinzinho | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CHOPINZINHO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CHOPINZINHO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cianorte | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CIANORTE - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CIANORTE - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cidade Gaúcha | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CIDADE GAÚCHA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CIDADE GAÚCHA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Clevelândia | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CLEVELÂNDIA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CLEVELÂNDIA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Colombo | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE COLOMBO DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE COLOMBO DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Colorado | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE COLORADO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE COLORADO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Congonhinhas | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CONGONHINHAS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CONGONHINHAS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Corbélia | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CORBÉLIA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CORBÉLIA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cornélio Procópio | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CORNÉLIO PROCÓPIO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CORNÉLIO PROCÓPIO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Coronel Vivida | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CORONEL VIVIDA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CORONEL VIVIDA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Cruzeiro do Oeste | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CRUZEIRO DO OESTE - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE CRUZEIRO DO OESTE - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Curitiba | Final | AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL DO FORO CENTRAL DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO CENTRAL DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | Curitiba: a fonte lista o 1º Juizado Especial Cível (Matéria Bancária) e Juizados regionais por bairro (Sítio Cercado, Santa Felicidade, CIC, Pinheirinho); confira a unidade pela matéria e pelo bairro do autor; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Curiúva | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE CURIÚVA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE CURIÚVA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Dois Vizinhos | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE DOIS VIZINHOS - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE DOIS VIZINHOS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Engenheiro Beltrão | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ENGENHEIRO BELTRÃO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE ENGENHEIRO BELTRÃO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Faxinal | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE FAXINAL - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE FAXINAL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Fazenda Rio Grande | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE FAZENDA RIO GRANDE DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE FAZENDA RIO GRANDE DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Formosa do Oeste | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE FORMOSA DO OESTE - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE FORMOSA DO OESTE - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Foz do Iguaçu | Final | AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL DA COMARCA DE FOZ DO IGUAÇU - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE FOZ DO IGUAÇU - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Francisco Beltrão | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE FRANCISCO BELTRÃO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE FRANCISCO BELTRÃO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Goioerê | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GOIOERÊ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE GOIOERÊ - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Grandes Rios | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GRANDES RIOS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE GRANDES RIOS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Guaíra | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUAÍRA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE GUAÍRA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Guaraniaçu | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUARANIAÇU - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE GUARANIAÇU - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Guarapuava | ? | AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUARAPUAVA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE GUARAPUAVA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Guaratuba | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE GUARATUBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE GUARATUBA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ibaiti | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IBAITI - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IBAITI - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ibiporã | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IBIPORÃ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IBIPORÃ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Icaraíma | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ICARAÍMA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE ICARAÍMA - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Imbituva | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IMBITUVA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE IMBITUVA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ipiranga | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IPIRANGA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE IPIRANGA - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Iporã | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IPORÃ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE IPORÃ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Irati | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IRATI - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IRATI - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Iretama | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IRETAMA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE IRETAMA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ivaiporã | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE IVAIPORÃ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE IVAIPORÃ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Jacarezinho | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JACAREZINHO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE JACAREZINHO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Jaguapitã | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JAGUAPITÃ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE JAGUAPITÃ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Jaguariaíva | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JAGUARIAÍVA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE JAGUARIAÍVA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Jandaia do Sul | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JANDAIA DO SUL - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE JANDAIA DO SUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Joaquim Távora | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE JOAQUIM TÁVORA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE JOAQUIM TÁVORA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Lapa | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE LAPA DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE LAPA DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Laranjeiras do Sul | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LARANJEIRAS DO SUL - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE LARANJEIRAS DO SUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Loanda | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE LOANDA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE LOANDA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Londrina | Final | AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL DA COMARCA DE LONDRINA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE LONDRINA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Mallet | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MALLET - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MALLET - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Mamborê | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MAMBORÊ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MAMBORÊ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Mandaguaçu | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MANDAGUAÇU - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MANDAGUAÇU - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Mandaguari | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MANDAGUARI - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MANDAGUARI - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Mangueirinha | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MANGUEIRINHA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MANGUEIRINHA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Manoel Ribas | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MANOEL RIBAS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MANOEL RIBAS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Marechal Cândido Rondon | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MARECHAL CÂNDIDO RONDON - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MARECHAL CÂNDIDO RONDON - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Marialva | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MARIALVA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MARIALVA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Marilândia do Sul | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MARILÂNDIA DO SUL - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MARILÂNDIA DO SUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Maringá | Final | AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL DA COMARCA DE MARINGÁ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MARINGÁ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Marmeleiro | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MARMELEIRO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MARMELEIRO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Matelândia | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MATELÂNDIA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MATELÂNDIA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Matinhos | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MATINHOS - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MATINHOS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Medianeira | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MEDIANEIRA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE MEDIANEIRA - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Morretes | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE MORRETES - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE MORRETES - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Nova Esperança | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NOVA ESPERANÇA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE NOVA ESPERANÇA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Nova Fátima | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NOVA FÁTIMA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE NOVA FÁTIMA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Nova Londrina | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE NOVA LONDRINA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE NOVA LONDRINA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ortigueira | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ORTIGUEIRA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE ORTIGUEIRA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Palmas | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PALMAS - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PALMAS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Palmeira | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PALMEIRA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PALMEIRA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Palmital | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PALMITAL - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PALMITAL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Palotina | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PALOTINA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PALOTINA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Paraíso do Norte | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PARAÍSO DO NORTE - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PARAÍSO DO NORTE - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Paranacity | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PARANACITY - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PARANACITY - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Paranaguá | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PARANAGUÁ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PARANAGUÁ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Paranavaí | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PARANAVAÍ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PARANAVAÍ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Pato Branco | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PATO BRANCO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PATO BRANCO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Peabiru | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PEABIRU - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PEABIRU - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Pérola | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PÉROLA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PÉROLA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Pinhais | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE PINHAIS DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE PINHAIS DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Pinhão | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PINHÃO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PINHÃO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Piraí do Sul | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PIRAÍ DO SUL - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PIRAÍ DO SUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Piraquara | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE PIRAQUARA DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE PIRAQUARA DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Pitanga | ? | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PITANGA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PITANGA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ponta Grossa | Final | AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL DA COMARCA DE PONTA GROSSA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PONTA GROSSA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Porecatu | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PORECATU - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE PORECATU - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Primeiro de Maio | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PRIMEIRO DE MAIO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PRIMEIRO DE MAIO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Prudentópolis | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE PRUDENTÓPOLIS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE PRUDENTÓPOLIS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Quedas do Iguaçu | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE QUEDAS DO IGUAÇU - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE QUEDAS DO IGUAÇU - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Realeza | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE REALEZA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE REALEZA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Rebouças | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE REBOUÇAS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE REBOUÇAS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Reserva | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RESERVA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE RESERVA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ribeirão Claro | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIBEIRÃO CLARO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE RIBEIRÃO CLARO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ribeirão do Pinhal | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIBEIRÃO DO PINHAL - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE RIBEIRÃO DO PINHAL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Rio Branco do Sul | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO BRANCO DO SUL - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE RIO BRANCO DO SUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Rio Negro | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE RIO NEGRO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE RIO NEGRO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Rolândia | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ROLÂNDIA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE ROLÂNDIA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Salto do Lontra | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SALTO DO LONTRA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SALTO DO LONTRA - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Santa Fé | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA FÉ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SANTA FÉ - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Santa Helena | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA HELENA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SANTA HELENA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Santa Isabel do Ivaí | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA ISABEL DO IVAÍ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SANTA ISABEL DO IVAÍ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Santa Mariana | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTA MARIANA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SANTA MARIANA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Santo Antônio da Platina | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTO ANTÔNIO DA PLATINA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SANTO ANTÔNIO DA PLATINA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Santo Antônio do Sudoeste | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SANTO ANTÔNIO DO SUDOESTE - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SANTO ANTÔNIO DO SUDOESTE - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| São Jerônimo da Serra | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JERÔNIMO DA SERRA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SÃO JERÔNIMO DA SERRA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| São João | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOÃO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SÃO JOÃO - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| São João do Ivaí | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOÃO DO IVAÍ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SÃO JOÃO DO IVAÍ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| São João do Triunfo | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO JOÃO DO TRIUNFO - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SÃO JOÃO DO TRIUNFO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| São José dos Pinhais | Final | AO JUÍZO DO [N]º JUIZADO ESPECIAL CÍVEL DO FORO REGIONAL DE SÃO JOSÉ DOS PINHAIS DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DO FORO REGIONAL DE SÃO JOSÉ DOS PINHAIS DA COMARCA DA REGIÃO METROPOLITANA DE CURITIBA - PR | foro regional: confira a denominação do foro na Comarca da Região Metropolitana de Curitiba; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| São Mateus do Sul | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO MATEUS DO SUL - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SÃO MATEUS DO SUL - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| São Miguel do Iguaçu | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SÃO MIGUEL DO IGUAÇU - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SÃO MIGUEL DO IGUAÇU - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Sarandi | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SARANDI - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE SARANDI - PR | a fonte não traz a unidade do Juizado desta comarca; Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Sengés | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SENGÉS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SENGÉS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Sertanópolis | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SERTANÓPOLIS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SERTANÓPOLIS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Siqueira Campos | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE SIQUEIRA CAMPOS - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE SIQUEIRA CAMPOS - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Teixeira Soares | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TEIXEIRA SOARES - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE TEIXEIRA SOARES - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Telêmaco Borba | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TELÊMACO BORBA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TELÊMACO BORBA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Terra Boa | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TERRA BOA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE TERRA BOA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Terra Rica | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TERRA RICA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE TERRA RICA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Terra Roxa | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TERRA ROXA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE TERRA ROXA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Tibagi | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TIBAGI - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE TIBAGI - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Toledo | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TOLEDO - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE TOLEDO - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Tomazina | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE TOMAZINA - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE TOMAZINA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Ubiratã | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE UBIRATÃ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE UBIRATÃ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Umuarama | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE UMUARAMA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE UMUARAMA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| União da Vitória | Final | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE UNIÃO DA VITÓRIA - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE UNIÃO DA VITÓRIA - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Uraí | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE URAÍ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE URAÍ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Wenceslau Braz | Intermediária | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE WENCESLAU BRAZ - PR | AO JUÍZO DA [N]ª VARA CÍVEL DA COMARCA DE WENCESLAU BRAZ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |
| Xambrê | Inicial | AO JUÍZO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE XAMBRÊ - PR | AO JUÍZO DA VARA CÍVEL DA COMARCA DE XAMBRÊ - PR | Justiça Comum: a fonte do TJPR só traz os Juizados; confira o nome e o número da vara cível |

## 4. Índice por município (399)

- Abatiá → Ribeirão do Pinhal
- Adrianópolis → Bocaiúva do Sul
- Agudos do Sul → Fazenda Rio Grande
- Almirante Tamandaré → Almirante Tamandaré
- Altamira do Paraná → Campina da Lagoa
- Altônia → Altônia
- Alto Paraíso → Xambrê
- Alto Paraná → Alto Paraná
- Alto Piquiri → Alto Piquiri
- Alvorada do Sul → Bela Vista do Paraíso
- Amaporã → Paranavaí
- Ampére → Ampére
- Anahy → Corbélia
- Andirá → Andirá
- Ângulo → Santa Fé
- Antonina → Antonina
- Antônio Olinto → São Mateus do Sul
- Apucarana → Apucarana
- Arapongas → Arapongas
- Arapoti → Arapoti
- Arapuã → Ivaiporã
- Araruna → Peabiru
- Araucária → Araucária
- Ariranha do Ivaí → Ivaiporã
- Assaí → Assaí
- Assis Chateaubriand → Assis Chateaubriand
- Astorga → Astorga
- Atalaia → Nova Esperança
- Balsa Nova → Campo Largo
- Bandeirantes → Bandeirantes
- Barbosa Ferraz → Barbosa Ferraz
- Barracão → Barracão
- Barra do Jacaré → Andirá
- Bela Vista da Caroba → Ampére
- Bela Vista do Paraíso → Bela Vista do Paraíso
- Bituruna → União da Vitória
- Boa Esperança → Mamborê
- Boa Esperança do Iguaçu → Dois Vizinhos
- Boa Ventura de São Roque → Pitanga
- Boa Vista da Aparecida → Capitão Leônidas Marques
- Bocaiúva do Sul → Bocaiúva do Sul
- Bom Jesus do Sul → Barracão
- Bom Sucesso → Jandaia do Sul
- Bom Sucesso do Sul → Pato Branco
- Borrazópolis → Faxinal
- Braganey → Corbélia
- Brasilândia do Sul → Alto Piquiri
- Cafeara → Centenário do Sul
- Cafelândia → Corbélia
- Cafezal do Sul → Iporã
- Califórnia → Marilândia do Sul
- Cambará → Cambará
- Cambé → Cambé
- Cambira → Apucarana
- Campina da Lagoa → Campina da Lagoa
- Campina do Simão → Guarapuava
- Campina Grande do Sul → Campina Grande do Sul
- Campo Bonito → Guaraniaçu
- Campo do Tenente → Rio Negro
- Campo Largo → Campo Largo
- Campo Magro → Almirante Tamandaré
- Campo Mourão → Campo Mourão
- Cândido de Abreu → Cândido de Abreu
- Candói → Guarapuava
- Cantagalo → Cantagalo
- Capanema → Capanema
- Capitão Leônidas Marques → Capitão Leônidas Marques
- Carambeí → Castro
- Carlópolis → Carlópolis
- Cascavel → Cascavel
- Castro → Castro
- Catanduvas → Catanduvas
- Centenário do Sul → Centenário do Sul
- Cerro Azul → Cerro Azul
- Céu Azul → Matelândia
- Chopinzinho → Chopinzinho
- Cianorte → Cianorte
- Cidade Gaúcha → Cidade Gaúcha
- Clevelândia → Clevelândia
- Colombo → Colombo
- Colorado → Colorado
- Congonhinhas → Congonhinhas
- Conselheiro Mairinck → Ibaiti
- Contenda → Lapa
- Corbélia → Corbélia
- Cornélio Procópio → Cornélio Procópio
- Coronel Domingos Soares → Palmas
- Coronel Vivida → Coronel Vivida
- Corumbataí do Sul → Barbosa Ferraz
- Cruzeiro do Iguaçu → Dois Vizinhos
- Cruzeiro do Oeste → Cruzeiro do Oeste
- Cruzeiro do Sul → Paranacity
- Cruz Machado → União da Vitória
- Cruzmaltina → Faxinal
- Curitiba → Curitiba
- Curiúva → Curiúva
- Diamante D'Oeste → Santa Helena
- Diamante do Norte → Nova Londrina
- Diamante do Sul → Guaraniaçu
- Dois Vizinhos → Dois Vizinhos
- Douradina → Umuarama
- Doutor Camargo → Maringá
- Doutor Ulysses → Cerro Azul
- Enéas Marques → Francisco Beltrão
- Engenheiro Beltrão → Engenheiro Beltrão
- Entre Rios do Oeste → Marechal Cândido Rondon
- Esperança Nova → Pérola
- Espigão Alto do Iguaçu → Quedas do Iguaçu
- Farol → Campo Mourão
- Faxinal → Faxinal
- Fazenda Rio Grande → Fazenda Rio Grande
- Fênix → Engenheiro Beltrão
- Fernandes Pinheiro → Teixeira Soares
- Figueira → Curiúva
- Floraí → Nova Esperança
- Flor da Serra do Sul → Barracão
- Floresta → Maringá
- Florestópolis → Porecatu
- Flórida → Santa Fé
- Formosa do Oeste → Formosa do Oeste
- Foz do Iguaçu → Foz do Iguaçu
- Foz do Jordão → Guarapuava
- Francisco Alves → Iporã
- Francisco Beltrão → Francisco Beltrão
- General Carneiro → União da Vitória
- Godoy Moreira → São João do Ivaí
- Goioerê → Goioerê
- Goioxim → Cantagalo
- Grandes Rios → Grandes Rios
- Guaíra → Guaíra
- Guairaçá → Terra Rica
- Guamiranga → Imbituva
- Guapirama → Joaquim Távora
- Guaporema → Cidade Gaúcha
- Guaraci → Jaguapitã
- Guaraniaçu → Guaraniaçu
- Guarapuava → Guarapuava
- Guaraqueçaba → Antonina
- Guaratuba → Guaratuba
- Honório Serpa → Mangueirinha
- Ibaiti → Ibaiti
- Ibema → Catanduvas
- Ibiporã → Ibiporã
- Icaraíma → Icaraíma
- Iguaraçu → Astorga
- Iguatu → Corbélia
- Imbaú → Telêmaco Borba
- Imbituva → Imbituva
- Inácio Martins → Irati
- Inajá → Paranacity
- Indianópolis → Cianorte
- Ipiranga → Ipiranga
- Iporã → Iporã
- Iracema do Oeste → Formosa do Oeste
- Irati → Irati
- Iretama → Iretama
- Itaguajé → Colorado
- Itaipulândia → São Miguel do Iguaçu
- Itambaracá → Andirá
- Itambé → Marialva
- Itapejara d'Oeste → Pato Branco
- Itaperuçu → Rio Branco do Sul
- Itaúna do Sul → Nova Londrina
- Ivaí → Imbituva
- Ivaiporã → Ivaiporã
- Ivaté → Icaraíma
- Ivatuba → Maringá
- Jaboti → Tomazina
- Jacarezinho → Jacarezinho
- Jaguapitã → Jaguapitã
- Jaguariaíva → Jaguariaíva
- Jandaia do Sul → Jandaia do Sul
- Janiópolis → Campo Mourão
- Japira → Ibaiti
- Japurá → Cianorte
- Jardim Alegre → Ivaiporã
- Jardim Olinda → Paranacity
- Jataizinho → Uraí
- Jesuítas → Formosa do Oeste
- Joaquim Távora → Joaquim Távora
- Jundiaí do Sul → Ribeirão do Pinhal
- Juranda → Ubiratã
- Jussara → Cianorte
- Kaloré → Jandaia do Sul
- Lapa → Lapa
- Laranjal → Palmital
- Laranjeiras do Sul → Laranjeiras do Sul
- Leópolis → Cornélio Procópio
- Lidianópolis → Ivaiporã
- Lindoeste → Cascavel
- Loanda → Loanda
- Lobato → Santa Fé
- Londrina → Londrina
- Luiziana → Campo Mourão
- Lunardelli → São João do Ivaí
- Lupionópolis → Centenário do Sul
- Mallet → Mallet
- Mamborê → Mamborê
- Mandaguaçu → Mandaguaçu
- Mandaguari → Mandaguari
- Mandirituba → Fazenda Rio Grande
- Manfrinópolis → Barracão
- Mangueirinha → Mangueirinha
- Manoel Ribas → Manoel Ribas
- Marechal Cândido Rondon → Marechal Cândido Rondon
- Maria Helena → Umuarama
- Marialva → Marialva
- Marilândia do Sul → Marilândia do Sul
- Marilena → Nova Londrina
- Mariluz → Cruzeiro do Oeste
- Maringá → Maringá
- Mariópolis → Clevelândia
- Maripá → Palotina
- Marmeleiro → Marmeleiro
- Marquinho → Laranjeiras do Sul
- Marumbi → Jandaia do Sul
- Matelândia → Matelândia
- Matinhos → Matinhos
- Mato Rico → Pitanga
- Mauá da Serra → Marilândia do Sul
- Medianeira → Medianeira
- Mercedes → Marechal Cândido Rondon
- Mirador → Paraíso do Norte
- Miraselva → Porecatu
- Missal → Medianeira
- Moreira Sales → Goioerê
- Morretes → Morretes
- Munhoz de Melo → Santa Fé
- Nossa Senhora das Graças → Santa Fé
- Nova Aliança do Ivaí → Paranavaí
- Nova América da Colina → Assaí
- Nova Aurora → Formosa do Oeste
- Nova Cantu → Campina da Lagoa
- Nova Esperança → Nova Esperança
- Nova Esperança do Sudoeste → Salto do Lontra
- Nova Fátima → Nova Fátima
- Nova Laranjeiras → Laranjeiras do Sul
- Nova Londrina → Nova Londrina
- Nova Olímpia → Cidade Gaúcha
- Nova Prata do Iguaçu → Salto do Lontra
- Nova Santa Bárbara → São Jerônimo da Serra
- Nova Santa Rosa → Marechal Cândido Rondon
- Nova Tebas → Manoel Ribas
- Novo Itacolomi → Apucarana
- Ortigueira → Ortigueira
- Ourizona → Mandaguaçu
- Ouro Verde do Oeste → Toledo
- Paiçandu → Maringá
- Palmas → Palmas
- Palmeira → Palmeira
- Palmital → Palmital
- Palotina → Palotina
- Paraíso do Norte → Paraíso do Norte
- Paranacity → Paranacity
- Paranaguá → Paranaguá
- Paranapoema → Paranacity
- Paranavaí → Paranavaí
- Pato Bragado → Marechal Cândido Rondon
- Pato Branco → Pato Branco
- Paula Freitas → União da Vitória
- Paulo Frontin → Mallet
- Peabiru → Peabiru
- Perobal → Umuarama
- Pérola → Pérola
- Pérola d'Oeste → Capanema
- Piên → Rio Negro
- Pinhais → Pinhais
- Pinhalão → Tomazina
- Pinhal de São Bento → Ampére (conferir)
- Pinhão → Pinhão
- Piraí do Sul → Piraí do Sul
- Piraquara → Piraquara
- Pitanga → Pitanga
- Pitangueiras → Rolândia
- Planaltina do Paraná → Santa Isabel do Ivaí
- Planalto → Capanema
- Ponta Grossa → Ponta Grossa
- Pontal do Paraná → Matinhos
- Porecatu → Porecatu
- Porto Amazonas → Palmeira
- Porto Barreiro → Laranjeiras do Sul
- Porto Rico → Loanda
- Porto Vitória → União da Vitória
- Prado Ferreira → Porecatu
- Pranchita → Santo Antônio do Sudoeste
- Presidente Castelo Branco → Nova Esperança
- Primeiro de Maio → Primeiro de Maio
- Prudentópolis → Prudentópolis
- Quarto Centenário → Goioerê
- Quatiguá → Joaquim Távora
- Quatro Barras → Campina Grande do Sul
- Quatro Pontes → Marechal Cândido Rondon
- Quedas do Iguaçu → Quedas do Iguaçu
- Querência do Norte → Loanda
- Quinta do Sol → Engenheiro Beltrão
- Quitandinha → Rio Negro
- Ramilândia → Matelândia
- Rancho Alegre → Uraí
- Rancho Alegre D'Oeste → Goioerê
- Realeza → Realeza
- Rebouças → Rebouças
- Renascença → Francisco Beltrão
- Reserva → Reserva
- Reserva do Iguaçu → Pinhão
- Ribeirão Claro → Ribeirão Claro
- Ribeirão do Pinhal → Ribeirão do Pinhal
- Rio Azul → Rebouças
- Rio Bom → Marilândia do Sul
- Rio Bonito do Iguaçu → Laranjeiras do Sul
- Rio Branco do Ivaí → Grandes Rios
- Rio Branco do Sul → Rio Branco do Sul
- Rio Negro → Rio Negro
- Rolândia → Rolândia
- Roncador → Iretama
- Rondon → Cidade Gaúcha
- Rosário do Ivaí → Grandes Rios
- Sabáudia → Arapongas
- Salgado Filho → Barracão
- Salto do Itararé → Siqueira Campos
- Salto do Lontra → Salto do Lontra
- Santa Amélia → Bandeirantes
- Santa Cecília do Pavão → São Jerônimo da Serra
- Santa Cruz de Monte Castelo → Loanda
- Santa Fé → Santa Fé
- Santa Helena → Santa Helena
- Santa Inês → Colorado
- Santa Isabel do Ivaí → Santa Isabel do Ivaí
- Santa Izabel do Oeste → Realeza
- Santa Lúcia → Capitão Leônidas Marques
- Santa Maria do Oeste → Pitanga
- Santa Mariana → Santa Mariana
- Santa Mônica → Santa Isabel do Ivaí
- Santana do Itararé → Wenceslau Braz
- Santa Tereza do Oeste → Cascavel
- Santa Terezinha de Itaipu → Foz do Iguaçu
- Santo Antônio da Platina → Santo Antônio da Platina
- Santo Antônio do Caiuá → Alto Paraná
- Santo Antônio do Paraíso → Congonhinhas
- Santo Antônio do Sudoeste → Santo Antônio do Sudoeste
- Santo Inácio → Colorado
- São Carlos do Ivaí → Paraíso do Norte
- São Jerônimo da Serra → São Jerônimo da Serra
- São João → São João
- São João do Caiuá → Alto Paraná
- São João do Ivaí → São João do Ivaí
- São João do Triunfo → São João do Triunfo
- São Jorge d'Oeste → Dois Vizinhos (conferir)
- São Jorge do Ivaí → Mandaguaçu
- São Jorge do Patrocínio → Altônia
- São José da Boa Vista → Wenceslau Braz
- São José das Palmeiras → Santa Helena
- São José dos Pinhais → São José dos Pinhais
- São Manoel do Paraná → Cianorte
- São Mateus do Sul → São Mateus do Sul
- São Miguel do Iguaçu → São Miguel do Iguaçu
- São Pedro do Iguaçu → Toledo
- São Pedro do Ivaí → Jandaia do Sul
- São Pedro do Paraná → Loanda
- São Sebastião da Amoreira → Assaí
- São Tomé → Cianorte
- Sapopema → Curiúva
- Sarandi → Sarandi
- Saudade do Iguaçu → Chopinzinho (conferir)
- Sengés → Sengés
- Serranópolis do Iguaçu → Medianeira
- Sertaneja → Cornélio Procópio
- Sertanópolis → Sertanópolis
- Siqueira Campos → Siqueira Campos
- Sulina → Chopinzinho (conferir)
- Tamarana → Londrina
- Tamboara → Paranavaí
- Tapejara → Cruzeiro do Oeste
- Tapira → Cidade Gaúcha
- Teixeira Soares → Teixeira Soares
- Telêmaco Borba → Telêmaco Borba
- Terra Boa → Terra Boa
- Terra Rica → Terra Rica
- Terra Roxa → Terra Roxa
- Tibagi → Tibagi
- Tijucas do Sul → São José dos Pinhais
- Toledo → Toledo
- Tomazina → Tomazina
- Três Barras do Paraná → Catanduvas
- Tunas do Paraná → Bocaiúva do Sul
- Tuneiras do Oeste → Cruzeiro do Oeste
- Tupãssi → Assis Chateaubriand
- Turvo → Guarapuava
- Ubiratã → Ubiratã
- Umuarama → Umuarama
- União da Vitória → União da Vitória
- Uniflor → Nova Esperança
- Uraí → Uraí
- Ventania → Tibagi
- Vera Cruz do Oeste → Matelândia
- Verê → Dois Vizinhos
- Virmond → Cantagalo
- Vitorino → Pato Branco
- Wenceslau Braz → Wenceslau Braz
- Xambrê → Xambrê
