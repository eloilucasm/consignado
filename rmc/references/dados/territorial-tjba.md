# Base territorial do TJBA para o Juizado Especial Cível (comarcas e unidades)

> Fontes oficiais do TJBA consultadas em 03/11/2026 (lista na seção 6). Município → comarca: "Relação Municípios x Comarca" do TJBA, de 15/03/2023 (`_acervo/dados/tjba_comarcas.json`). Unidades: quadro das Varas do Sistema dos Juizados de 17/04/2026, páginas de endereços do Portal dos Juizados (capital e interior) e relações de magistrados por entrância de 22/09/2026 (final do interior e intermediária) e 02/10/2026 (inicial), que listam também as unidades vagas.
> Só dados de unidade. Os documentos de origem trazem nomes de magistrados e servidores, que não foram copiados.

## 1. Regra de endereçamento no Juizado Especial Cível (consignado contra banco)

1. **Ache a comarca** do município de residência do autor no índice da seção 5 (`grep -n "Nome do município"`). A comarca nem sempre é o próprio município.
2. **Comarca com Vara do Sistema dos Juizados Especiais** (seção 2; 40 comarcas): a petição vai à Vara do Sistema. Com mais de uma vara, o número sai na distribuição: deixe `[N]ª`. Em Salvador, a ação de consumo contra banco vai às **Varas do Sistema dos Juizados Especiais do Consumidor** (1ª a 20ª).
3. **Comarca sem Vara do Sistema** (seção 3; as demais): não há unidade própria de Juizado. A Lei de Organização Judiciária da Bahia (Lei 10.845/2007, arts. 107 e 156) e a Lei estadual 7.033/1997 (art. 22) mandam que a causa da Lei 9.099/95 seja processada e decidida pelo juiz da comarca, **com a classe do Procedimento do Juizado Especial**. A petição vai à unidade cível da comarca: a **Vara de Jurisdição Plena** (entrância inicial e parte da intermediária) ou a **Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais** (havendo varas especializadas). Onde o TJBA instituiu Juizado Especial Adjunto por decreto, ele funciona anexado a essa mesma vara (seção 3, coluna "Adjunto").
4. No corpo da petição, diga que a ação segue o **procedimento da Lei 9.099/95**: é isso que dá a classe do Juizado na comarca sem Vara do Sistema.
5. Réu Caixa: Justiça Federal (`territorial-ba.md`), não esta tabela.

**Decisão do escritório (03/11/2026).** Aprovada a forma desta tabela: nas 40 comarcas da seção 2, a Vara do Sistema dos Juizados Especiais; nas demais, a unidade cível da comarca (Vara de Jurisdição Plena ou Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais), com o procedimento da Lei 9.099/95 indicado no corpo da petição.

**Para os scripts:** `references/dados/tjba_unidades.json` traz, por comarca, a entrância e o endereçamento pronto do JEC e da Justiça Comum (`jec.enderecamento`, `comum.enderecamento`). A comarca do município continua em `tjba_comarcas.json`.

## 2. Comarcas com Vara do Sistema dos Juizados Especiais (40)

Nome oficial das unidades (competência cível e criminal no interior). Fonte: quadro de 17/04/2026 e Portal dos Juizados.

| Comarca | Entrância | Unidade(s) do Juizado | Endereçamento no JEC | Endereçamento na Justiça Comum |
|---|---|---|---|---|
| Alagoinhas | Final | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE ALAGOINHAS - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE ALAGOINHAS - BA |
| Barreiras | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE BARREIRAS - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE BARREIRAS - BA |
| Bom Jesus da Lapa | Final | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE BOM JESUS DA LAPA - BA | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTES DE TRABALHO DA COMARCA DE BOM JESUS DA LAPA - BA |
| Brumado | Final | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE BRUMADO - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE BRUMADO - BA |
| Camaçari | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE CAMAÇARI - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE CAMAÇARI - BA |
| Canavieiras | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE CANAVIEIRAS - BA | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS, CONSUMIDOR, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO DA COMARCA DE CANAVIEIRAS - BA |
| Cícero Dantas | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE CÍCERO DANTAS - BA | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE CÍCERO DANTAS - BA |
| Conceição do Coité | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE CONCEIÇÃO DO COITÉ - BA | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE CONCEIÇÃO DO COITÉ - BA |
| Euclides da Cunha | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE EUCLIDES DA CUNHA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE EUCLIDES DA CUNHA - BA |
| Eunápolis | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE EUNÁPOLIS - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE EUNÁPOLIS - BA |
| Feira de Santana | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais; 3ª Vara do Sistema dos Juizados Especiais; 4ª Vara do Sistema dos Juizados Especiais; 5ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE FEIRA DE SANTANA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE FEIRA DE SANTANA - BA |
| Gandu | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE GANDU - BA | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE GANDU - BA |
| Guanambi | Final | 1ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA 1ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE GUANAMBI - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE GUANAMBI - BA |
| Ilhéus | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais; 3ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE ILHÉUS - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE ILHÉUS - BA |
| Ipiaú | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE IPIAÚ - BA | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE IPIAÚ - BA |
| Ipirá | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE IPIRÁ - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE IPIRÁ - BA |
| Irecê | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE IRECÊ - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE IRECÊ - BA |
| Itaberaba | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE ITABERABA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE ITABERABA - BA |
| Itabuna | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais; 3ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE ITABUNA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE ITABUNA - BA |
| Itamaraju | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE ITAMARAJU - BA | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTRO POR ORDEM ALFABÉTICA DE COMARCA PÚBLICO E ACIDENTE DE TRABALHO DA COMARCA DE ITAMARAJU - BA |
| Itapetinga | Intermediária | 1ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA 1ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE ITAPETINGA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE ITAPETINGA - BA |
| Jacobina | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE JACOBINA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE JACOBINA - BA |
| Jequié | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE JEQUIÉ - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE JEQUIÉ - BA |
| Juazeiro | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE JUAZEIRO - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE JUAZEIRO - BA |
| Lauro de Freitas | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE LAURO DE FREITAS - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE LAURO DE FREITAS - BA |
| Livramento de Nossa Senhora | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE LIVRAMENTO DE NOSSA SENHORA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE LIVRAMENTO DE NOSSA SENHORA - BA |
| Luís Eduardo Magalhães | Final | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE LUÍS EDUARDO MAGALHÃES - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE LUÍS EDUARDO MAGALHÃES - BA |
| Paulo Afonso | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE PAULO AFONSO - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE PAULO AFONSO - BA |
| Porto Seguro | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE PORTO SEGURO - BA | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS E REGISTROS PÚBLICOS DA COMARCA DE PORTO SEGURO - BA |
| Riachão do Jacuípe | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE RIACHÃO DO JACUÍPE - BA | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE RIACHÃO DO JACUÍPE - BA |
| Salvador | Final | 1ª a 20ª Vara do Sistema dos Juizados Especiais do Consumidor; 1ª a 8ª de Causas Comuns; 1ª de Trânsito; 1ª e 2ª da Fazenda Pública | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DO CONSUMIDOR DA COMARCA DE SALVADOR - BA | AO JUÍZO DA [N]ª VARA DE RELAÇÕES DE CONSUMO DA COMARCA DE SALVADOR - BA |
| Santa Maria da Vitória | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE SANTA MARIA DA VITÓRIA - BA | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE SANTA MARIA DA VITÓRIA - BA |
| Santo Antônio de Jesus | Final | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE SANTO ANTÔNIO DE JESUS - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE SANTO ANTÔNIO DE JESUS - BA |
| Santo Estevão | Intermediária | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE SANTO ESTEVÃO - BA | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE SANTO ESTEVÃO - BA |
| Senhor do Bonfim | Final | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE SENHOR DO BONFIM - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE SENHOR DO BONFIM - BA |
| Serrinha | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE SERRINHA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE SERRINHA - BA |
| Simões Filho | Final | 1ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA 1ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE SIMÕES FILHO - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE SIMÕES FILHO - BA |
| Teixeira de Freitas | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE TEIXEIRA DE FREITAS - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE TEIXEIRA DE FREITAS - BA |
| Valença | Final | Vara do Sistema dos Juizados Especiais | AO JUÍZO DA VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE VALENÇA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE VALENÇA - BA |
| Vitória da Conquista | Final | 1ª Vara do Sistema dos Juizados Especiais; 2ª Vara do Sistema dos Juizados Especiais; 3ª Vara do Sistema dos Juizados Especiais | AO JUÍZO DA [N]ª VARA DO SISTEMA DOS JUIZADOS ESPECIAIS DA COMARCA DE VITÓRIA DA CONQUISTA - BA | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE VITÓRIA DA CONQUISTA - BA |

**Salvador (capital).** Varas do Sistema dos Juizados Especiais do **Consumidor**: 1ª a 20ª. As 1ª a 18ª substituíram os antigos Juizados de Defesa do Consumidor (Brotas, extensões NAJ e UNIJORGE, Juizado Modelo Federação, Universo). Há também as de **Causas Comuns** (1ª a 8ª), **Trânsito** (1ª) e **Fazenda Pública** (1ª e 2ª), e seis criminais. A ação de consumo contra banco vai às do Consumidor, por distribuição.

## 3. Comarcas sem Vara do Sistema dos Juizados (162)

A causa do Juizado tramita na unidade cível da comarca, com a classe do Procedimento do Juizado Especial (seção 1, item 3).

Nestas comarcas, a mesma unidade cível recebe a ação no JEC e na Justiça Comum; o que muda é o procedimento indicado no corpo da petição.

| Comarca | Entrância | Unidade cível | Adjunto | Endereçamento |
|---|---|---|---|---|
| Amargosa | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE AMARGOSA - BA |
| Amélia Rodrigues | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE AMÉLIA RODRIGUES - BA |
| Anagé | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 812/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ANAGÉ - BA |
| Andaraí | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ANDARAÍ - BA |
| Antas | Inicial | Vara de Jurisdição Plena | decretos de 08/09/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ANTAS - BA |
| Araci | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ARACI - BA |
| Baianópolis | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE BAIANÓPOLIS - BA |
| Barra | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE BARRA - BA |
| Barra da Estiva | Inicial | Vara de Jurisdição Plena | decretos de 08/09/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE BARRA DA ESTIVA - BA |
| Barra do Choça | Inicial | Vara de Jurisdição Plena | decretos de 08/09/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE BARRA DO CHOÇA - BA |
| Barra do Mendes | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE BARRA DO MENDES - BA |
| Belmonte | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE BELMONTE - BA |
| Belo Campo | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE BELO CAMPO - BA |
| Buerarema | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE BUERAREMA - BA |
| Cachoeira | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE CACHOEIRA - BA |
| Caculé | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CACULÉ - BA |
| Caetité | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE CAETITÉ - BA |
| Camacan | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE CAMACAN - BA [CONFERIR: seção 4] |
| Camamu | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CAMAMU - BA |
| Campo Formoso | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública | — | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE CAMPO FORMOSO - BA |
| Canarana | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CANARANA - BA |
| Candeias | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Fazenda Pública | — | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE CANDEIAS - BA |
| Cândido Sales | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CÂNDIDO SALES - BA |
| Cansanção | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CANSANÇÃO - BA |
| Capela do Alto Alegre | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CAPELA DO ALTO ALEGRE - BA |
| Capim Grosso | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE CAPIM GROSSO - BA |
| Caravelas | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CARAVELAS - BA |
| Carinhanha | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CARINHANHA - BA |
| Casa Nova | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE CASA NOVA - BA |
| Castro Alves | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CASTRO ALVES - BA |
| Catu | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE CATU - BA |
| Central | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CENTRAL - BA |
| Chorrochó | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 813/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CHORROCHÓ - BA |
| Coaraci | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE COARACI - BA |
| Cocos | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 814/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE COCOS - BA |
| Conceição do Almeida | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CONCEIÇÃO DO ALMEIDA - BA |
| Conceição do Jacuípe | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CONCEIÇÃO DO JACUÍPE - BA |
| Conde | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CONDE - BA |
| Condeúba | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CONDEÚBA - BA |
| Coração de Maria | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CORAÇÃO DE MARIA - BA |
| Coribe | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CORIBE - BA |
| Correntina | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 815/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CORRENTINA - BA |
| Cotegipe | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE COTEGIPE - BA |
| Cruz das Almas | Final | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública | — | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE CRUZ DAS ALMAS - BA |
| Curaçá | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE CURAÇÁ - BA |
| Dias D’Ávila | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE DIAS D’ÁVILA - BA |
| Encruzilhada | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ENCRUZILHADA - BA |
| Entre Rios | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE ENTRE RIOS - BA |
| Esplanada | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ESPLANADA - BA |
| Formosa do Rio Preto | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE FORMOSA DO RIO PRETO - BA |
| Gentio do Ouro | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE GENTIO DO OURO - BA |
| Governador Mangabeira | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE GOVERNADOR MANGABEIRA - BA |
| Guaratinga | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE GUARATINGA - BA |
| Iaçu | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE IAÇU - BA |
| Ibicaraí | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE IBICARAÍ - BA |
| Ibirapuã | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE IBIRAPUÃ - BA |
| Ibirataia | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE IBIRATAIA - BA |
| Ibotirama | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE IBOTIRAMA - BA |
| Igaporã | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 816/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE IGAPORÃ - BA |
| Iguaí | Inicial | Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE IGUAÍ - BA |
| Inhambupe | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE INHAMBUPE - BA |
| Iraquara | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE IRAQUARA - BA |
| Irará | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE IRARÁ - BA |
| Itabela | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITABELA - BA |
| Itacaré | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITACARÉ - BA |
| Itagibá | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITAGIBÁ - BA |
| Itajuípe | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITAJUÍPE - BA |
| Itambé | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITAMBÉ - BA |
| Itanhém | Inicial | Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE ITANHÉM - BA |
| Itaparica | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE ITAPARICA - BA |
| Itapicuru | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITAPICURU - BA |
| Itarantim | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITARANTIM - BA |
| Itiúba | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITIÚBA - BA |
| Itororó | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITORORÓ - BA |
| Ituaçu | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITUAÇU - BA |
| Ituberá | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE ITUBERÁ - BA |
| Jacaraci | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE JACARACI - BA |
| Jaguaquara | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE JAGUAQUARA - BA |
| Jaguarari | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE JAGUARARI - BA |
| Jeremoabo | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE JEREMOABO - BA |
| Jitaúna | Inicial | Vara de Jurisdição Plena | decretos de 08/09/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE JITAÚNA - BA |
| João Dourado | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE JOÃO DOURADO - BA |
| Laje | Inicial | Vara de Jurisdição Plena | decretos de 08/09/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE LAJE - BA |
| Lapão | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE LAPÃO - BA |
| Lençóis | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE LENÇÓIS - BA |
| Macarani | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 817/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MACARANI - BA |
| Macaúbas | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública | — | AO JUÍZO DA [N]ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE MACAÚBAS - BA |
| Mairi | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MAIRI - BA |
| Maracás | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 818/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MARACÁS - BA |
| Maragogipe | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MARAGOGIPE - BA |
| Mata de São João | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE MATA DE SÃO JOÃO - BA |
| Medeiros Neto | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MEDEIROS NETO - BA |
| Miguel Calmon | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MIGUEL CALMON - BA |
| Monte Santo | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MONTE SANTO - BA |
| Morro do Chapéu | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE MORRO DO CHAPÉU - BA |
| Mucuri | Inicial | Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE MUCURI - BA |
| Mundo Novo | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE MUNDO NOVO - BA |
| Muritiba | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MURITIBA - BA |
| Mutuípe | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE MUTUÍPE - BA |
| Nazaré | Intermediária | Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS, ACIDENTE DE TRABALHO E FAZENDA PÚBLICA DA COMARCA DE NAZARÉ - BA |
| Nova Soure | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE NOVA SOURE - BA |
| Nova Viçosa | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE NOVA VIÇOSA - BA |
| Olindina | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE OLINDINA - BA |
| Oliveira dos Brejinhos | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE OLIVEIRA DOS BREJINHOS - BA |
| Palmas de Monte Alto | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE PALMAS DE MONTE ALTO - BA |
| Paramirim | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE PARAMIRIM - BA |
| Paripiranga | Inicial | Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE PARIPIRANGA - BA |
| Piatã | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE PIATÃ - BA |
| Pilão Arcado | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE PILÃO ARCADO - BA |
| Pindobaçu | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE PINDOBAÇU - BA |
| Piritiba | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE PIRITIBA - BA |
| Planalto | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 819/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE PLANALTO - BA |
| Poções | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE POÇÕES - BA |
| Pojuca | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE POJUCA - BA |
| Prado | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE PRADO - BA |
| Presidente Jânio Quadros | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE PRESIDENTE JÂNIO QUADROS - BA |
| Queimadas | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE QUEIMADAS - BA |
| Remanso | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE REMANSO - BA |
| Retirolândia | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE RETIROLÂNDIA - BA |
| Riachão das Neves | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE RIACHÃO DAS NEVES - BA |
| Riacho de Santana | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE RIACHO DE SANTANA - BA |
| Ribeira do Pombal | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE RIBEIRA DO POMBAL - BA |
| Rio Real | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE RIO REAL - BA |
| Ruy Barbosa | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE RUY BARBOSA - BA |
| Santa Bárbara | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SANTA BÁRBARA - BA |
| Santa Cruz Cabrália | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SANTA CRUZ CABRÁLIA - BA |
| Santa Inês | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SANTA INÊS - BA |
| Santa Rita de Cássia | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SANTA RITA DE CÁSSIA - BA |
| Santa Terezinha | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SANTA TEREZINHA - BA [CONFERIR: seção 4] |
| Santaluz | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SANTALUZ - BA |
| Santana | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SANTANA - BA |
| Santo Amaro | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE SANTO AMARO - BA |
| São Desidério | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SÃO DESIDÉRIO - BA |
| São Felipe | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SÃO FELIPE - BA |
| São Félix (São Félix/Cachoeira na tabela de 2023) | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SÃO FÉLIX - BA [CONFERIR: seção 4] |
| São Francisco do Conde | Inicial | Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE SÃO FRANCISCO DO CONDE - BA |
| São Gonçalo dos Campos | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Registros Públicos | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS E REGISTROS PÚBLICOS DA COMARCA DE SÃO GONÇALO DOS CAMPOS - BA |
| São Sebastião do Passé | Inicial | Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais | — | AO JUÍZO DA VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS E COMERCIAIS DA COMARCA DE SÃO SEBASTIÃO DO PASSÉ - BA |
| Sapeaçu | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SAPEAÇU - BA |
| Saúde | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SAÚDE - BA |
| Seabra | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE SEABRA - BA |
| Sento Sé | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SENTO SÉ - BA |
| Serra Dourada | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 820/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SERRA DOURADA - BA |
| Sobradinho | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE SOBRADINHO - BA |
| Tanhaçu | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE TANHAÇU - BA |
| Tanque Novo | Inicial | Vara de Jurisdição Plena | Decreto Judiciário 821/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE TANQUE NOVO - BA |
| Taperoá | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE TAPEROÁ - BA |
| Teofilândia | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE TEOFILÂNDIA - BA |
| Terra Nova | Inicial | Vara de Jurisdição Plena | decretos de 08/09/2022 | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE TERRA NOVA - BA |
| Tremedal (Tremedal/Belo Campo na tabela de 2023) | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE TREMEDAL - BA [CONFERIR: seção 4] |
| Tucano | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE TUCANO - BA |
| Uauá | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE UAUÁ - BA |
| Ubaíra | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE UBAÍRA - BA |
| Ubaitaba | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE UBAITABA - BA |
| Ubatã | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE UBATÃ - BA |
| Una | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE UNA - BA |
| Urandi | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE URANDI - BA |
| Uruçuca | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE URUÇUCA - BA |
| Utinga | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE UTINGA - BA |
| Valente | Intermediária | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE VALENTE - BA |
| Wenceslau Guimarães | Inicial | Vara de Jurisdição Plena | — | AO JUÍZO DA VARA DE JURISDIÇÃO PLENA DA COMARCA DE WENCESLAU GUIMARÃES - BA |
| Xique-xique | Intermediária | 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho | — | AO JUÍZO DA 1ª VARA DOS FEITOS RELATIVOS ÀS RELAÇÕES DE CONSUMO, CÍVEIS, COMERCIAIS, REGISTROS PÚBLICOS E ACIDENTE DE TRABALHO DA COMARCA DE XIQUE-XIQUE - BA |

"Adjunto" traz só os Juizados Especiais Adjuntos achados em decreto. Comarca sem decreto achado também julga a causa da Lei 9.099/95 pela regra dos arts. 107 e 156 da Lei 10.845/2007; a falta do decreto não muda o endereçamento.

## 4. Divergências e pontos a conferir

- **Tabela município → comarca de 15/03/2023.** As relações de 2026 não mostraram comarca desativada depois dela, mas a tabela é anterior a três anos de atos. Refaça o cruzamento quando o TJBA publicar relação nova.
- **São Félix e Tremedal.** A tabela de 2023 traz "São Félix/Cachoeira" e "Tremedal/Belo Campo", porque a Resolução TJBA 13/2019 desativa as duas automaticamente quando o juiz titular for removido ou promovido. Nas relações de 2026 ambas ainda aparecem como comarcas de Jurisdição Plena, São Félix com o titular vago e juiz designado. `[CONFERIR: se a desativação já ocorreu, use a comarca agrupadora (Cachoeira; Belo Campo)]`.
- **Grafias.** "Camacã" (tabela de 2023) aparece como **Camacan** nas relações de 2026, e "Santa Teresinha" como **Santa Terezinha**. O endereçamento usa a grafia de 2026.
- **Presidente Dutra.** Comarca desativada (Resolução 06/2017), agrupada a **Irecê**.
- **Grafia de município diferente da base da Justiça Federal (`territorial-ba.md`).** A tabela do TJBA escreve "Brotas de Macaúbas", "Muquém de São Francisco", "Oliveira de Brejinhos", "Camacã" e "Santa Teresinha"; a base federal, "Brotas da Macaúbas", "Muquém do São Francisco", "Oliveira dos Brejinhos", "Camacan" e "Santa Terezinha". Barro Preto aparece duas vezes na tabela do TJBA ("Barro Preto (Governador Lomanto Júnior)" e "Governador Lomanto Júnior (Barro Preto)"), por isso o índice tem 418 linhas para 417 municípios. Busque pelo começo do nome.
- **Varas criminais** não entram na tabela: só a unidade cível recebe a ação de consignado.

Comarcas desativadas lidas na relação da entrância inicial (02/10/2026), com a agrupadora: 62. Elas já estão absorvidas pela tabela município → comarca e não recebem petição.

## 5. Índice por município

Município — comarca — unidade que recebe a causa do Juizado.

- Abaíra — Piatã — Vara de Jurisdição Plena
- Abaré — Chorrochó — Vara de Jurisdição Plena
- Acajutiba — Esplanada — Vara de Jurisdição Plena
- Adustina — Paripiranga — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Água Fria — Irará — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Aiquara — Itagibá — Vara de Jurisdição Plena
- Alagoinhas — Alagoinhas — Vara do Sistema dos Juizados Especiais
- Alcobaça — Prado — Vara de Jurisdição Plena
- Almadina — Coaraci — Vara de Jurisdição Plena
- Amargosa — Amargosa — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Amélia Rodrigues — Amélia Rodrigues — Vara de Jurisdição Plena
- América Dourada — João Dourado — Vara de Jurisdição Plena
- Anagé — Anagé — Vara de Jurisdição Plena
- Andaraí — Andaraí — Vara de Jurisdição Plena
- Andorinha — Senhor do Bonfim — Vara do Sistema dos Juizados Especiais
- Angical — Barreiras — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Anguera — Feira de Santana — Varas do Sistema dos Juizados Especiais (1ª a 5ª)
- Antas — Antas — Vara de Jurisdição Plena
- Antônio Cardoso — Santo Estevão — Vara do Sistema dos Juizados Especiais
- Antônio Gonçalves — Campo Formoso — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública
- Aporá — Esplanada — Vara de Jurisdição Plena
- Apuarema — Jequié — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Araçás — Alagoinhas — Vara do Sistema dos Juizados Especiais
- Aracatu — Brumado — Vara do Sistema dos Juizados Especiais
- Araci — Araci — Vara de Jurisdição Plena
- Aramari — Alagoinhas — Vara do Sistema dos Juizados Especiais
- Arataca — Camacan — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Aratuípe — Nazaré — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Aurelino Leal — Ubaitaba — Vara de Jurisdição Plena
- Baianópolis — Baianópolis — Vara de Jurisdição Plena
- Baixa Grande — Ipirá — Vara do Sistema dos Juizados Especiais
- Banzaê — Ribeira do Pombal — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Barra — Barra — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Barra da Estiva — Barra da Estiva — Vara de Jurisdição Plena
- Barra do Choça — Barra do Choça — Vara de Jurisdição Plena
- Barra do Mendes — Barra do Mendes — Vara de Jurisdição Plena
- Barra do Rocha — Ipiaú — Vara do Sistema dos Juizados Especiais
- Barreiras — Barreiras — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Barro Alto — Canarana — Vara de Jurisdição Plena
- Barro Preto (Governador Lomanto Júnior) — Itabuna — Varas do Sistema dos Juizados Especiais (1ª a 3ª)
- Barrocas — Serrinha — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Belmonte — Belmonte — Vara de Jurisdição Plena
- Belo Campo — Belo Campo — Vara de Jurisdição Plena
- Biritinga — Serrinha — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Boa Nova — Poções — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Boa Vista do Tupim — Itaberaba — Vara do Sistema dos Juizados Especiais
- Bom Jesus da Lapa — Bom Jesus da Lapa — Vara do Sistema dos Juizados Especiais
- Bom Jesus da Serra — Poções — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Boninal — Piatã — Vara de Jurisdição Plena
- Bonito — Utinga — Vara de Jurisdição Plena
- Boquira — Macaúbas — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública
- Botuporã — Tanque Novo — Vara de Jurisdição Plena
- Brejões — Amargosa — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Brejolândia — Serra Dourada — Vara de Jurisdição Plena
- Brotas de Macaúbas — Oliveira dos Brejinhos — Vara de Jurisdição Plena
- Brumado — Brumado — Vara do Sistema dos Juizados Especiais
- Buerarema — Buerarema — Vara de Jurisdição Plena
- Buritirama — Barra — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Caatiba — Barra do Choça — Vara de Jurisdição Plena
- Cabaceiras do Paraguaçu — Muritiba — Vara de Jurisdição Plena
- Cachoeira — Cachoeira — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Caculé — Caculé — Vara de Jurisdição Plena
- Caém — Jacobina — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Caetanos — Poções — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Caetité — Caetité — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Cafarnaum — Morro do Chapéu — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Cairu — Valença — Vara do Sistema dos Juizados Especiais
- Caldeirão Grande — Saúde — Vara de Jurisdição Plena
- Camacã — Camacan — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Camaçari — Camaçari — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Camamu — Camamu — Vara de Jurisdição Plena
- Campo Alegre de Lourdes — Remanso — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Campo Formoso — Campo Formoso — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública
- Canápolis — Santana — Vara de Jurisdição Plena
- Canarana — Canarana — Vara de Jurisdição Plena
- Canavieiras — Canavieiras — Vara do Sistema dos Juizados Especiais
- Candeal — Riachão do Jacuípe — Vara do Sistema dos Juizados Especiais
- Candeias — Candeias — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Fazenda Pública
- Candiba — Guanambi — Vara do Sistema dos Juizados Especiais
- Cândido Sales — Cândido Sales — Vara de Jurisdição Plena
- Cansanção — Cansanção — Vara de Jurisdição Plena
- Canudos — Uauá — Vara de Jurisdição Plena
- Capela do Alto Alegre — Capela do Alto Alegre — Vara de Jurisdição Plena
- Capim Grosso — Capim Grosso — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Caraíbas — Anagé — Vara de Jurisdição Plena
- Caravelas — Caravelas — Vara de Jurisdição Plena
- Cardeal da Silva — Entre Rios — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Carinhanha — Carinhanha — Vara de Jurisdição Plena
- Casa Nova — Casa Nova — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Castro Alves — Castro Alves — Vara de Jurisdição Plena
- Catolândia — São Desidério — Vara de Jurisdição Plena
- Catu — Catu — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Caturama — Paramirim — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Central — Central — Vara de Jurisdição Plena
- Chorrochó — Chorrochó — Vara de Jurisdição Plena
- Cícero Dantas — Cícero Dantas — Vara do Sistema dos Juizados Especiais
- Cipó — Nova Soure — Vara de Jurisdição Plena
- Coaraci — Coaraci — Vara de Jurisdição Plena
- Cocos — Cocos — Vara de Jurisdição Plena
- Conceição da Feira — São Gonçalo dos Campos — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Registros Públicos
- Conceição do Almeida — Conceição do Almeida — Vara de Jurisdição Plena
- Conceição do Coité — Conceição do Coité — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Conceição do Jacuípe — Conceição do Jacuípe — Vara de Jurisdição Plena
- Conde — Conde — Vara de Jurisdição Plena
- Condeúba — Condeúba — Vara de Jurisdição Plena
- Contendas do Sincorá — Ituaçu — Vara de Jurisdição Plena
- Coração de Maria — Coração de Maria — Vara de Jurisdição Plena
- Cordeiros — Condeúba — Vara de Jurisdição Plena
- Coribe — Coribe — Vara de Jurisdição Plena
- Coronel João Sá — Jeremoabo — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Correntina — Correntina — Vara de Jurisdição Plena
- Cotegipe — Cotegipe — Vara de Jurisdição Plena
- Cravolândia — Santa Inês — Vara de Jurisdição Plena
- Crisópolis — Olindina — Vara de Jurisdição Plena
- Cristópolis — Barreiras — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Cruz das Almas — Cruz das Almas — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública
- Curaçá — Curaçá — Vara de Jurisdição Plena
- Dário Meira — Itagibá — Vara de Jurisdição Plena
- Dias D’Ávila — Dias D’Ávila — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Dom Basílio — Livramento de Nossa Senhora — Vara do Sistema dos Juizados Especiais
- Dom Macedo Costa — Santo Antônio de Jesus — Vara do Sistema dos Juizados Especiais
- Elísio Medrado — Santa Terezinha — Vara de Jurisdição Plena
- Encruzilhada — Encruzilhada — Vara de Jurisdição Plena
- Entre Rios — Entre Rios — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Érico Cardoso — Paramirim — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Esplanada — Esplanada — Vara de Jurisdição Plena
- Euclides da Cunha — Euclides da Cunha — Vara do Sistema dos Juizados Especiais
- Eunápolis — Eunápolis — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Fátima — Cícero Dantas — Vara do Sistema dos Juizados Especiais
- Feira da Mata — Carinhanha — Vara de Jurisdição Plena
- Feira de Santana — Feira de Santana — Varas do Sistema dos Juizados Especiais (1ª a 5ª)
- Filadélfia — Campo Formoso — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública
- Firmino Alves — Itororó — Vara de Jurisdição Plena
- Floresta Azul — Ibicaraí — Vara de Jurisdição Plena
- Formosa do Rio Preto — Formosa do Rio Preto — Vara de Jurisdição Plena
- Gandu — Gandu — Vara do Sistema dos Juizados Especiais
- Gavião — Capela do Alto Alegre — Vara de Jurisdição Plena
- Gentio do Ouro — Gentio do Ouro — Vara de Jurisdição Plena
- Glória — Paulo Afonso — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Gongogi — Ubaitaba — Vara de Jurisdição Plena
- Governador Lomanto Júnior (Barro Preto) — Itabuna — Varas do Sistema dos Juizados Especiais (1ª a 3ª)
- Governador Mangabeira — Governador Mangabeira — Vara de Jurisdição Plena
- Guajeru — Caculé — Vara de Jurisdição Plena
- Guanambi — Guanambi — Vara do Sistema dos Juizados Especiais
- Guaratinga — Guaratinga — Vara de Jurisdição Plena
- Heliópolis — Cícero Dantas — Vara do Sistema dos Juizados Especiais
- Iaçu — Iaçu — Vara de Jurisdição Plena
- Ibiassucê — Caculé — Vara de Jurisdição Plena
- Ibicaraí — Ibicaraí — Vara de Jurisdição Plena
- Ibicoara — Barra da Estiva — Vara de Jurisdição Plena
- Ibicuí — Iguaí — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Ibipeba — Barra do Mendes — Vara de Jurisdição Plena
- Ibipitanga — Macaúbas — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública
- Ibiquera — Ruy Barbosa — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Ibirapitanga — Ubatã — Vara de Jurisdição Plena
- Ibirapuã — Ibirapuã — Vara de Jurisdição Plena
- Ibirataia — Ibirataia — Vara de Jurisdição Plena
- Ibitiara — Seabra — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Ibititá — Irecê — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Ibotirama — Ibotirama — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Ichu — Riachão do Jacuípe — Vara do Sistema dos Juizados Especiais
- Igaporã — Igaporã — Vara de Jurisdição Plena
- Igrapiúna — Camamu — Vara de Jurisdição Plena
- Iguaí — Iguaí — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Ilhéus — Ilhéus — Varas do Sistema dos Juizados Especiais (1ª a 3ª)
- Inhambupe — Inhambupe — Vara de Jurisdição Plena
- Ipecaetá — Santo Estevão — Vara do Sistema dos Juizados Especiais
- Ipiaú — Ipiaú — Vara do Sistema dos Juizados Especiais
- Ipirá — Ipirá — Vara do Sistema dos Juizados Especiais
- Ipupiara — Oliveira dos Brejinhos — Vara de Jurisdição Plena
- Irajuba — Santa Inês — Vara de Jurisdição Plena
- Iramaia — Barra da Estiva — Vara de Jurisdição Plena
- Iraquara — Iraquara — Vara de Jurisdição Plena
- Irará — Irará — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Irecê — Irecê — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Itabela — Itabela — Vara de Jurisdição Plena
- Itaberaba — Itaberaba — Vara do Sistema dos Juizados Especiais
- Itabuna — Itabuna — Varas do Sistema dos Juizados Especiais (1ª a 3ª)
- Itacaré — Itacaré — Vara de Jurisdição Plena
- Itaetê — Andaraí — Vara de Jurisdição Plena
- Itagi — Jequié — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Itagibá — Itagibá — Vara de Jurisdição Plena
- Itagimirim — Eunápolis — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Itaguaçu da Bahia — Xique-xique — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Itaju do Colônia — Itororó — Vara de Jurisdição Plena
- Itajuípe — Itajuípe — Vara de Jurisdição Plena
- Itamaraju — Itamaraju — Vara do Sistema dos Juizados Especiais
- Itamari — Gandu — Vara do Sistema dos Juizados Especiais
- Itambé — Itambé — Vara de Jurisdição Plena
- Itanagra — Mata de São João — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Itanhém — Itanhém — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Itaparica — Itaparica — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Itapé — Itabuna — Varas do Sistema dos Juizados Especiais (1ª a 3ª)
- Itapebi — Eunápolis — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Itapetinga — Itapetinga — Vara do Sistema dos Juizados Especiais
- Itapicuru — Itapicuru — Vara de Jurisdição Plena
- Itapitanga — Coaraci — Vara de Jurisdição Plena
- Itaquara — Jaguaquara — Vara de Jurisdição Plena
- Itarantim — Itarantim — Vara de Jurisdição Plena
- Itatim — Santa Terezinha — Vara de Jurisdição Plena
- Itiruçu — Jaguaquara — Vara de Jurisdição Plena
- Itiúba — Itiúba — Vara de Jurisdição Plena
- Itororó — Itororó — Vara de Jurisdição Plena
- Ituaçu — Ituaçu — Vara de Jurisdição Plena
- Ituberá — Ituberá — Vara de Jurisdição Plena
- Iuiú — Carinhanha — Vara de Jurisdição Plena
- Jaborandi — Coribe — Vara de Jurisdição Plena
- Jacaraci — Jacaraci — Vara de Jurisdição Plena
- Jacobina — Jacobina — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Jaguaquara — Jaguaquara — Vara de Jurisdição Plena
- Jaguarari — Jaguarari — Vara de Jurisdição Plena
- Jaguaripe — Nazaré — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Jandaíra — Rio Real — Vara de Jurisdição Plena
- Jequié — Jequié — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Jeremoabo — Jeremoabo — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Jiquiriçá — Ubaíra — Vara de Jurisdição Plena
- Jitaúna — Jitaúna — Vara de Jurisdição Plena
- João Dourado — João Dourado — Vara de Jurisdição Plena
- Juazeiro — Juazeiro — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Jucuruçu — Itamaraju — Vara do Sistema dos Juizados Especiais
- Jussara — Irecê — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Jussari — Buerarema — Vara de Jurisdição Plena
- Jussiape — Livramento de Nossa Senhora — Vara do Sistema dos Juizados Especiais
- Lafaiete Coutinho — Jaguaquara — Vara de Jurisdição Plena
- Lagoa Real — Caetité — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Laje — Laje — Vara de Jurisdição Plena
- Lajedão — Ibirapuã — Vara de Jurisdição Plena
- Lajedinho — Ruy Barbosa — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Lajedo do Tabocal — Jaguaquara — Vara de Jurisdição Plena
- Lamarão — Santa Bárbara — Vara de Jurisdição Plena
- Lapão — Lapão — Vara de Jurisdição Plena
- Lauro de Freitas — Lauro de Freitas — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Lençóis — Lençóis — Vara de Jurisdição Plena
- Licínio de Almeida — Jacaraci — Vara de Jurisdição Plena
- Livramento de Nossa Senhora — Livramento de Nossa Senhora — Vara do Sistema dos Juizados Especiais
- Luís Eduardo Magalhães — Luís Eduardo Magalhães — Vara do Sistema dos Juizados Especiais
- Macajuba — Ruy Barbosa — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Macarani — Macarani — Vara de Jurisdição Plena
- Macaúbas — Macaúbas — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho; 2ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Fazenda Pública
- Macururé — Chorrochó — Vara de Jurisdição Plena
- Madre de Deus — Salvador — Varas do Sistema dos Juizados Especiais do Consumidor (1ª a 20ª)
- Maetinga — Condeúba — Vara de Jurisdição Plena
- Maiquinique — Macarani — Vara de Jurisdição Plena
- Mairi — Mairi — Vara de Jurisdição Plena
- Malhada — Carinhanha — Vara de Jurisdição Plena
- Malhada de Pedras — Brumado — Vara do Sistema dos Juizados Especiais
- Manoel Vitorino — Jequié — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Mansidão — Santa Rita de Cássia — Vara de Jurisdição Plena
- Maracás — Maracás — Vara de Jurisdição Plena
- Maragogipe — Maragogipe — Vara de Jurisdição Plena
- Maraú — Itacaré — Vara de Jurisdição Plena
- Marcionílio Souza — Iaçu — Vara de Jurisdição Plena
- Mascote — Camacan — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Mata de São João — Mata de São João — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Matina — Riacho de Santana — Vara de Jurisdição Plena
- Medeiros Neto — Medeiros Neto — Vara de Jurisdição Plena
- Miguel Calmon — Miguel Calmon — Vara de Jurisdição Plena
- Milagres — Amargosa — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Mirangaba — Jacobina — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Mirante — Poções — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Monte Santo — Monte Santo — Vara de Jurisdição Plena
- Morpará — Ibotirama — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Morro do Chapéu — Morro do Chapéu — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Mortugaba — Jacaraci — Vara de Jurisdição Plena
- Mucugê — Andaraí — Vara de Jurisdição Plena
- Mucuri — Mucuri — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Mulungu do Morro — Morro do Chapéu — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Mundo Novo — Mundo Novo — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Muniz Ferreira — Nazaré — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Muquém de São Francisco — Ibotirama — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Muritiba — Muritiba — Vara de Jurisdição Plena
- Mutuípe — Mutuípe — Vara de Jurisdição Plena
- Nazaré — Nazaré — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Nilo Peçanha — Taperoá — Vara de Jurisdição Plena
- Nordestina — Queimadas — Vara de Jurisdição Plena
- Nova Canaã — Iguaí — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Nova Fátima — Capela do Alto Alegre — Vara de Jurisdição Plena
- Nova Ibiá — Gandu — Vara do Sistema dos Juizados Especiais
- Nova Itarana — Amargosa — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Nova Redenção — Andaraí — Vara de Jurisdição Plena
- Nova Soure — Nova Soure — Vara de Jurisdição Plena
- Nova Viçosa — Nova Viçosa — Vara de Jurisdição Plena
- Novo Horizonte — Seabra — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Novo Triunfo — Antas — Vara de Jurisdição Plena
- Olindina — Olindina — Vara de Jurisdição Plena
- Oliveira de Brejinhos — Oliveira dos Brejinhos — Vara de Jurisdição Plena
- Ouriçangas — Irará — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Ourolândia — Jacobina — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Palmas de Monte Alto — Palmas de Monte Alto — Vara de Jurisdição Plena
- Palmeiras — Iraquara — Vara de Jurisdição Plena
- Paramirim — Paramirim — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Paratinga — Bom Jesus da Lapa — Vara do Sistema dos Juizados Especiais
- Paripiranga — Paripiranga — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Pau Brasil — Camacan — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Paulo Afonso — Paulo Afonso — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Pé de Serra — Riachão do Jacuípe — Vara do Sistema dos Juizados Especiais
- Pedrão — Irará — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Pedro Alexandre — Jeremoabo — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Piatã — Piatã — Vara de Jurisdição Plena
- Pilão Arcado — Pilão Arcado — Vara de Jurisdição Plena
- Pindaí — Guanambi — Vara do Sistema dos Juizados Especiais
- Pindobaçu — Pindobaçu — Vara de Jurisdição Plena
- Pintadas — Ipirá — Vara do Sistema dos Juizados Especiais
- Piraí do Norte — Gandu — Vara do Sistema dos Juizados Especiais
- Piripá — Condeúba — Vara de Jurisdição Plena
- Piritiba — Piritiba — Vara de Jurisdição Plena
- Planaltino — Maracás — Vara de Jurisdição Plena
- Planalto — Planalto — Vara de Jurisdição Plena
- Poções — Poções — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Pojuca — Pojuca — Vara de Jurisdição Plena
- Ponto Novo — Saúde — Vara de Jurisdição Plena
- Porto Seguro — Porto Seguro — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Potiraguá — Itarantim — Vara de Jurisdição Plena
- Prado — Prado — Vara de Jurisdição Plena
- Presidente Dutra — Irecê — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Presidente Jânio Quadros — Presidente Jânio Quadros — Vara de Jurisdição Plena
- Presidente Tancredo Neves — Valença — Vara do Sistema dos Juizados Especiais
- Queimadas — Queimadas — Vara de Jurisdição Plena
- Quijingue — Euclides da Cunha — Vara do Sistema dos Juizados Especiais
- Quixabeira — Capim Grosso — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Rafael Jambeiro — Castro Alves — Vara de Jurisdição Plena
- Remanso — Remanso — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Retirolândia — Retirolândia — Vara de Jurisdição Plena
- Riachão das Neves — Riachão das Neves — Vara de Jurisdição Plena
- Riachão do Jacuípe — Riachão do Jacuípe — Vara do Sistema dos Juizados Especiais
- Riacho de Santana — Riacho de Santana — Vara de Jurisdição Plena
- Ribeira do Amparo — Nova Soure — Vara de Jurisdição Plena
- Ribeira do Pombal — Ribeira do Pombal — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Ribeirão do Largo — Encruzilhada — Vara de Jurisdição Plena
- Rio de Contas — Livramento de Nossa Senhora — Vara do Sistema dos Juizados Especiais
- Rio do Antônio — Caculé — Vara de Jurisdição Plena
- Rio do Pires — Paramirim — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Rio Real — Rio Real — Vara de Jurisdição Plena
- Rodelas — Chorrochó — Vara de Jurisdição Plena
- Ruy Barbosa — Ruy Barbosa — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Salinas da Margarida — Nazaré — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Salvador — Salvador — Varas do Sistema dos Juizados Especiais do Consumidor (1ª a 20ª)
- Santa Bárbara — Santa Bárbara — Vara de Jurisdição Plena
- Santa Brígida — Paulo Afonso — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Santa Cruz Cabrália — Santa Cruz Cabrália — Vara de Jurisdição Plena
- Santa Cruz da Vitória — Ibicaraí — Vara de Jurisdição Plena
- Santa Inês — Santa Inês — Vara de Jurisdição Plena
- Santa Luzia — Camacan — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Santa Maria da Vitória — Santa Maria da Vitória — Vara do Sistema dos Juizados Especiais
- Santa Rita de Cássia — Santa Rita de Cássia — Vara de Jurisdição Plena
- Santa Teresinha — Santa Terezinha — Vara de Jurisdição Plena
- Santaluz — Santaluz — Vara de Jurisdição Plena
- Santana — Santana — Vara de Jurisdição Plena
- Santanópolis — Irará — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Santo Amaro — Santo Amaro — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Santo Antônio de Jesus — Santo Antônio de Jesus — Vara do Sistema dos Juizados Especiais
- Santo Estevão — Santo Estevão — Vara do Sistema dos Juizados Especiais
- São Desidério — São Desidério — Vara de Jurisdição Plena
- São Domingos — Valente — Vara de Jurisdição Plena
- São Felipe — São Felipe — Vara de Jurisdição Plena
- São Félix — São Félix (ver seção 4) — Vara de Jurisdição Plena
- São Félix do Coribe — Santa Maria da Vitória — Vara do Sistema dos Juizados Especiais
- São Francisco do Conde — São Francisco do Conde — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- São Gabriel — Irecê — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- São Gonçalo dos Campos — São Gonçalo dos Campos — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais e Registros Públicos
- São José da Vitória — Buerarema — Vara de Jurisdição Plena
- São José do Jacuípe — Capim Grosso — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- São Miguel das Matas — Laje — Vara de Jurisdição Plena
- São Sebastião do Passé — São Sebastião do Passé — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Sapeaçu — Sapeaçu — Vara de Jurisdição Plena
- Sátiro Dias — Inhambupe — Vara de Jurisdição Plena
- Saubara — Santo Amaro — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Saúde — Saúde — Vara de Jurisdição Plena
- Seabra — Seabra — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Sebastião Laranjeiras — Palmas de Monte Alto — Vara de Jurisdição Plena
- Senhor do Bonfim — Senhor do Bonfim — Vara do Sistema dos Juizados Especiais
- Sento Sé — Sento Sé — Vara de Jurisdição Plena
- Serra do Ramalho — Bom Jesus da Lapa — Vara do Sistema dos Juizados Especiais
- Serra Dourada — Serra Dourada — Vara de Jurisdição Plena
- Serra Preta — Feira de Santana — Varas do Sistema dos Juizados Especiais (1ª a 5ª)
- Serrinha — Serrinha — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Serrolândia — Jacobina — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Simões Filho — Simões Filho — Vara do Sistema dos Juizados Especiais
- Sítio do Mato — Bom Jesus da Lapa — Vara do Sistema dos Juizados Especiais
- Sítio do Quinto — Jeremoabo — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Sobradinho — Sobradinho — Vara de Jurisdição Plena
- Souto Soares — Iraquara — Vara de Jurisdição Plena
- Tabocas do Brejo Velho — Serra Dourada — Vara de Jurisdição Plena
- Tanhaçu — Tanhaçu — Vara de Jurisdição Plena
- Tanque Novo — Tanque Novo — Vara de Jurisdição Plena
- Tanquinho — Santa Bárbara — Vara de Jurisdição Plena
- Taperoá — Taperoá — Vara de Jurisdição Plena
- Tapiramutá — Mundo Novo — Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos, Acidente de Trabalho e Fazenda Pública
- Teixeira de Freitas — Teixeira de Freitas — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Teodoro Sampaio — Terra Nova — Vara de Jurisdição Plena
- Teofilândia — Teofilândia — Vara de Jurisdição Plena
- Teolândia — Wenceslau Guimarães — Vara de Jurisdição Plena
- Terra Nova — Terra Nova — Vara de Jurisdição Plena
- Tremedal — Tremedal (ver seção 4) — Vara de Jurisdição Plena
- Tucano — Tucano — Vara de Jurisdição Plena
- Uauá — Uauá — Vara de Jurisdição Plena
- Ubaíra — Ubaíra — Vara de Jurisdição Plena
- Ubaitaba — Ubaitaba — Vara de Jurisdição Plena
- Ubatã — Ubatã — Vara de Jurisdição Plena
- Uibaí — Irecê — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Umburanas — Jacobina — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Una — Una — Vara de Jurisdição Plena
- Urandi — Urandi — Vara de Jurisdição Plena
- Uruçuca — Uruçuca — Vara de Jurisdição Plena
- Utinga — Utinga — Vara de Jurisdição Plena
- Valença — Valença — Vara do Sistema dos Juizados Especiais
- Valente — Valente — Vara de Jurisdição Plena
- Várzea da Roça — Mairi — Vara de Jurisdição Plena
- Várzea do Poço — Mairi — Vara de Jurisdição Plena
- Várzea Nova — Jacobina — Varas do Sistema dos Juizados Especiais (1ª a 2ª)
- Varzedo — Santo Antônio de Jesus — Vara do Sistema dos Juizados Especiais
- Vera Cruz — Itaparica — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho
- Vereda — Itanhém — Vara dos Feitos Relativos às Relações de Consumo, Cíveis e Comerciais
- Vitória da Conquista — Vitória da Conquista — Varas do Sistema dos Juizados Especiais (1ª a 3ª)
- Wagner — Utinga — Vara de Jurisdição Plena
- Wanderley — Cotegipe — Vara de Jurisdição Plena
- Wenceslau Guimarães — Wenceslau Guimarães — Vara de Jurisdição Plena
- Xique-xique — Xique-xique — 1ª Vara dos Feitos Relativos às Relações de Consumo, Cíveis, Comerciais, Registros Públicos e Acidente de Trabalho

## 6. Fontes (consulta em 03/11/2026)

- Quadro das Varas do Sistema dos Juizados Especiais, 17/04/2026: <https://www.tjba.jus.br/juizadosespeciais/wp-content/uploads/2026/04/quadro-17-04-2026.pdf>
- Portal dos Juizados Especiais, endereços do interior e da Região Metropolitana: <https://www.tjba.jus.br/juizadosespeciais/enderecos-e-telefones-interior/>; da capital: <https://www.tjba.jus.br/juizadosespeciais/enderecos-e-telefones-capital/>
- Relações de magistrados (entrância final do interior e intermediária, 22/09/2026; inicial, 02/10/2026) e de unidades vagas com designação (22/09/2026): <https://www.tjba.jus.br/portal/relacao-de-magistrados/>
- Relação Municípios x Comarca, 15/03/2023: <https://www.tjba.jus.br/portal/wp-content/uploads/2023/03/Relacao-Municipios-Comarca.pdf> (mesmo arquivo de `triagem-consignado/references/tjba_relacao_municipios_comarca.pdf`)
- Decretos Judiciários 812 a 821, de 18/11/2022 (DJe 3220, de 21/11/2022), que instituem Juizados Especiais Adjuntos e citam os arts. 107 e 156 da Lei 10.845/2007 e o art. 22 da Lei 7.033/1997: <https://www.tjba.jus.br/portal/wp-content/uploads/2022/12/Juizados-adjuntos.pdf>
- Notícia do TJBA de 08/09/2022 sobre os Juizados Adjuntos de Antas, Barra da Estiva, Barra do Choça, Jitaúna, Laje e Terra Nova: <https://www.tjba.jus.br/portal/pjba-institui-juizados-especiais-adjuntos-civel-e-criminal-em-seis-comarcas-do-interior/>
- Corregedoria, comarcas agregadas e desativadas: <https://www.tjba.jus.br/corregedoria/comarcas/>
