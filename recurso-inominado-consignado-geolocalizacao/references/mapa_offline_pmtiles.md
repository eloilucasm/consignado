# Mapa de ruas offline (PMTiles) para a Figura Ilustrativa

Objetivo: a Figura Ilustrativa sair com mapa de ruas real, sem internet na hora de gerar, sem servidor e sem clique do advogado. O Cowork renderiza o mapa na própria máquina virtual a partir de um arquivo local.

## Como funciona

1. O advogado gera **uma única vez**, no computador dele (que tem internet), um arquivo `regiao.pmtiles` com o mapa de ruas da região onde ocorrem os casos.
2. O arquivo fica na raiz da pasta conectada ao Cowork, com o nome exato `regiao.pmtiles` (ver passo 6). Não vai dentro da skill: o upload de skill tem limite de 30 MB.
3. Na VF9, o `geo_figuras.py` (modo `auto`, o padrão) exige o `regiao.pmtiles` e chama o `geo_mapa_pmtiles.py`. Para cada figura com os dois pontos dentro da área do arquivo, saem três imagens obrigatórias, separadas e em ordem: `fig_evento<N>_A_visao_geral.png` (visão geral sobre a malha do IBGE), `_B_log.png` (captura de mapa do local do log) e `_C_residencia.png` (captura de mapa da residência), com a legenda de cada uma em `figuras.json`, campo `paineis`. Ponto fora da área sai só com a visão geral e o aviso "FIGURA INCOMPLETA".
4. Dados: OpenStreetMap, no formato do mapa-base do Protomaps (ODbL). A figura leva a atribuição "© OpenStreetMap contributors, Protomaps".

## O que o advogado faz (uma vez, uns 15 minutos)

**1. Baixar o programa `pmtiles`.** Em https://github.com/protomaps/go-pmtiles/releases, baixar a versão do seu sistema (Windows: arquivo `.zip` com `Windows_x86_64`) e extrair o `pmtiles.exe` numa pasta de trabalho.

**2. Pegar o endereço da base mais recente.** Abrir https://maps.protomaps.com/builds e copiar o endereço (`.pmtiles`) da compilação mais recente. Não baixar o arquivo inteiro: ele tem cerca de 120 GB. O programa baixa só o pedaço da sua região.

**3. Escolher a região.** Já vêm prontos, em `assets/mapa/regioes/`, o contorno da **Bahia inteira** (`bahia.geojson`) e o da Região Geográfica Intermediária de Ilhéus-Itabuna (`ilheus_itabuna.geojson`, 51 municípios), ambos derivados da malha do IBGE, com um único contorno simplificado e folga de cerca de 1 km nas bordas. Para outra região: `python3 scripts/geo_malha.py --listar-regioes` e depois `--regiao-rgint "Nome"` ou `--regiao-municipios "Ilhéus,Itabuna"` (`--regiao-saida arquivo.geojson`). Quanto maior a região e o zoom, maior o arquivo.

**4. Medir antes de baixar (importante para a Bahia inteira).** O tamanho da Bahia no zoom 14 não foi medido por mim, e cada nível de zoom a mais costuma dobrar o arquivo. Na pasta do `pmtiles.exe`, rodar `pmtiles extract --help` e, se existir a opção `--dry-run`, o comando do passo 5 com ela: o programa informa quantos tiles e quantos bytes baixaria, sem baixar. Decidir assim:
   - até uns 2 GB no zoom 14: seguir com a Bahia inteira;
   - acima disso: repetir a medição com `--maxzoom=13` (as quadras ficam menos detalhadas, mas ruas e avenidas permanecem) ou usar só a região de Ilhéus-Itabuna;
   - não usar `--maxzoom` abaixo de 13: o mapa fica sem as ruas locais.
   Arquivos grandes não prejudicam a velocidade da figura (o mapa lê só os trechos de que precisa), mas demoram a baixar e a enviar ao Cowork.

**5. Gerar o arquivo.**
`pmtiles extract ENDEREÇO-DA-BUILD regiao.pmtiles --region=bahia.geojson --maxzoom=14`
(para a região menor: `--region=ilheus_itabuna.geojson`). Se o `--region` der erro, usar a caixa da Bahia: `--bbox=-46.5772,-18.3486,-37.3411,-8.5328` no lugar de `--region` (inclui pedaços dos estados vizinhos e aumenta o arquivo). Se a conexão cair no meio, rodar o mesmo comando de novo.

**6. Entregar à skill.** **Não colocar dentro da skill** (limite de 30 MB no upload): deixar o arquivo na **raiz da pasta conectada ao Cowork (a pasta de trabalho), com o nome exato `regiao.pmtiles`**. Essa é a convenção; outro nome não é aceito. A skill procura, nesta ordem: o caminho dado em `--pmtiles`, a variável `GEO_PMTILES`, `assets/mapa/regiao.pmtiles`, a raiz da pasta de trabalho, `/mnt/<pasta>/`, `/sessions/<sessão>/mnt/<pasta>/` (onde o Cowork monta a pasta conectada) e uma subpasta abaixo da pasta de trabalho, sempre com o nome exato `regiao.pmtiles` e cabeçalho PMTiles v3. Como a pasta conectada fica no computador do advogado, o Cowork precisa trazer o arquivo (uns 150 MB) para o ambiente antes de rodar a figura; a skill manda procurá-lo e trazê-lo. Se o Cowork não enxergar o arquivo, dizer a ele o caminho completo.

## O que o Cowork faz

Rodar `python3 scripts/geo_figuras.py entrada.json --saida-dir figuras/` (modo `auto`). Antes, procurar o arquivo `regiao.pmtiles` (no ambiente e, se houver pasta conectada, nela) e trazê-lo. Se, mesmo assim, não existir, **a geração para** (código de saída 5, nenhuma figura gerada) e o Cowork pergunta ao usuário: colocar o arquivo na pasta conectada ou autorizar expressamente só a visão geral esquemática (`--fundo esquema`). Se existir, olhar cada PNG: mapa de fundo visível, pontos marcados, círculos de 100 m e 150 m na captura da residência, distância e atribuição. Conferir o aviso `ponto fora da área do arquivo PMTiles`: então o evento sai só com a visão geral ("FIGURA INCOMPLETA") e o Cowork pergunta ao usuário. Dependências: Pillow, Playwright (Python) e um Chromium (já presentes no ambiente de execução; se faltarem, o script avisa e o evento sai só com a visão geral, marcado "FIGURA INCOMPLETA").

## Limites e o que ainda não foi verificado

- O pipeline (servidor local com Range, MapLibre, fontes e ícones locais, captura, composição) foi testado num Chromium de teste com um PMTiles **sintético**, no esquema de camadas do Protomaps. Não foi testado com um arquivo real do Protomaps nem no Cowork do advogado.
- Os endereços e as opções do `pmtiles extract` vêm da documentação do Protomaps na data desta versão; podem mudar. Em caso de divergência, vale `pmtiles extract --help`.
- A figura com mapa de ruas só vale para pontos dentro da área do arquivo. Fora dela, o evento sai só com a visão geral (limites municipais do IBGE), marcado "FIGURA INCOMPLETA".
- Os nomes de rua do mapa vêm do OpenStreetMap e podem estar desatualizados ou incompletos. A figura é ilustrativa e a legenda diz isso.
