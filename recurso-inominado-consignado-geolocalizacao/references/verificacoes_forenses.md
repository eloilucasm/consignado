# Verificações forenses VF1 a VF9

> Fonte única dos procedimentos de verificação dos documentos do réu. Ler na ETAPA 2-B.
>
> Todas as verificações trabalham sobre documentos JÁ NOS AUTOS e não criam fato ou documento novo (Regra 6). Regras comuns: registrar ID e página de cada dado; nunca afirmar conteúdo de imagem não visualizada; nunca omitir documento do réu por parecer repetitivo.
>
> Origem dos critérios: **[FSCn]** vem do catálogo; **[SKILL]** vinha do SKILL.md; **(proposta)** foi acrescentado na reorganização e precisa ser validado pelo advogado.

## Quando executar cada verificação

| V | Verificação | Executar quando | Alimenta |
|---|---|---|---|
| VF1 | Índice dos autos | Sempre | Todas |
| VF2 | Ficha do contrato | Sempre, para cada contrato impugnado | FSC1, FSC7 |
| VF3 | Cessão de crédito | O extrato INSS mostra "Migrado do contrato X CBC: Y" ou equivalente | FSC5, FSC11 |
| VF4 | Autenticação eletrônica | Há trilha ou assinatura eletrônica | FSC2, FSC10 |
| VF5 | Correspondente bancário | Sempre | FSC10 |
| VF6 | Confronto TED × LIBERADO | O réu juntou TED ou PIX (obrigatória) | FSC4 |
| VF7 | Análise cruzada | Há 2 ou mais contratos com documentação do réu | FSC2, FSC5, FSC10 |
| VF8 | Contratos na mesma data | O extrato INSS mostra 2 ou mais contratos no mesmo dia ou em intervalo curto | FSC11 |
| VF9 | Geolocalização | O contrato, a CCB ou a trilha traz coordenadas, IP ou Cidade-UF | FSC2, FSC10 |

## VF1. Índice dos autos

- Montar o índice real de documentos: ID, data, tipo, quem juntou, páginas. [SKILL]
- Rasterizar e visualizar a 1ª página de cada documento antes de qualquer afirmação. [SKILL]
- O índice é reaproveitado por VF2 a VF9 e pela peça, para citar ID e página.

## VF2. Ficha do contrato

Para cada contrato impugnado, registrar: tipo de assinatura (manuscrita ou eletrônica), coerência de datas (a CCB foi assinada antes de a trilha existir?), dados cadastrais, NB e origem da averbação. [SKILL, FSC7]

- **Assinatura manuscrita:** só perícia grafotécnica dirime a controvérsia de autenticidade. Comparação visual feita pelo juízo não é exame técnico. [FSC1]
- **Assinatura eletrônica:** o que importa é a integridade da trilha (hash, log, plataforma), tratada em VF4. [FSC1]
- **Contraste visual:** reunir as outras assinaturas do autor que constem dos autos (procuração, RG, outros contratos). [FSC1]
- **Quadro comparativo de dados cadastrais:** ficha do réu × documentos reais do autor × divergência × gravidade, com ID e página. [SKILL]

## VF3. Cessão de crédito

Ativar só se o extrato INSS mostrar "Migrado do contrato X CBC: Y" ou equivalente. [FSC5]

- **Eixo EXISTÊNCIA** (arts. 104, II, 107, 108, 166, II e 286–288, CC): há instrumento de cessão ou endosso que identifique este contrato por número, data e valor, com assinatura de cedente e cessionário? [FSC5]
- **Eixo EFICÁCIA** (art. 290, CC): há notificação ao devedor, em forma idônea, anterior aos descontos? [FSC5]
- "Ciência pelos descontos no extrato", "averbação no INSS" ou "registro no SCR" não substituem a notificação. Se a sentença fez essa equiparação, é erro de direito. [FSC5, referencias_juridicas.md]
- Se o réu juntou o mesmo arquivo com nomes distintos para simular endosso ou cessão (hash idêntico), é indício crítico autônomo de apocrifia. [FSC5]

## VF4. Autenticação eletrônica

Extrair, com ID e página: IP, reverse DNS, se o IP é RFC 1918, Cidade-UF (preenchida ou vazia), geolocalização, biometria e liveness, hash e metadados. [SKILL, FSC2]

- Existência de um log não prova a idoneidade do conteúdo do log. [FSC2]
- IP privado (RFC 1918) no log: o registro não traz o IP público da sessão, que identificaria a origem e o assinante. É lacuna do documento do réu (ônus dele) e indício **Relevante**, não Crítico: um celular no Wi-Fi de casa também tem IP privado. Antes de usar, ver se o log diz qual IP registrou (do aparelho ou o que chegou ao servidor). Nunca escrever "impossível para cliente residencial". [FSC2, FSC10]
- Reverse DNS: aponta operadora compatível com cliente residencial ou o próprio correspondente ou banco? [FSC2]
- Biometria válida exige algoritmo, matching score, thresholds, FAR/FRR, liveness com parâmetros técnicos, metadados completos e hash de integridade vinculado ao contrato. Sem relatório técnico, é selfie, não prova de autoria. [FSC2]
- Hash prova a integridade do arquivo depois de assinado, não quem operou o dispositivo. [FSC2]
- Inventário de campos: cada banco registra campos diferentes e os atualiza com frequência. Listar TODOS os campos do log, inclusive os que a skill não conhece, e levar os que não têm coordenada à VF9 (indicadores sem coordenada).
- Classificar cada IP com `python3 scripts/ip_check.py --entrada entrada.json` (offline: pública, rede interna, CGNAT, reservada). A consulta RDAP ao titular do bloco vem ligada por padrão (o IP já consta dos autos; a consulta o envia ao registro público do bloco); `--sem-rdap` a desliga e, se a rede bloquear, o script segue offline e avisa. O titular do bloco não é o titular da linha, e o mesmo IP muda de assinante com o tempo (citar data e hora).
- A localização registrada no log é tratada em VF9.

## VF5. Correspondente bancário

- Extrair sede (UF), CNPJ, contrato de correspondência e credenciamento. [SKILL, FSC10]
- Achado típico: correspondente sediado em UF distante, sem contrato de correspondência ou credenciamento comprovado nos autos. [FSC10]
- Base: Res. CMN 3.954/2011, art. 2º (hoje Res. CMN 4.935/2021, art. 3º); Súmula 479/STJ (`referencias_juridicas.md`).
- O catálogo fala em "credenciamento BACEN"; conferir a terminologia antes de usá-la na peça.

## VF6. Confronto TED × LIBERADO

Obrigatória sempre que o réu juntou TED ou PIX. Extrair a coluna LIBERADO do extrato INSS para o contrato impugnado e confrontar com o valor do TED. [SKILL, FSC4]

1. LIBERADO em branco ou R$ 0,00 (portabilidade pura): o "proveito econômico" é imprestável como fundamento. [FSC4]
2. Valor do TED diferente do LIBERADO: o TED pode não corresponder ao contrato impugnado. [FSC4]
3. Valores coincidentes: depósito em conta não prova que o titular usou o valor nem que autorizou esta contratação. O correntista pode ter sido vítima de terceiro com acesso à conta. [FSC4]
4. Em refinanciamento ou portabilidade, checar se a liberação é só repasse interno para quitar dívida anterior, sem troco real ao consumidor. [FSC4]

## VF7. Análise cruzada entre contratos

Executar com 2 ou mais contratos que tenham documentação do réu. Comparar selfies, IPs, hashes e horários entre os contratos. [SKILL]

- Mesmo arquivo juntado com nomes distintos (hash idêntico): indício crítico. [FSC5]
- Mesma selfie ou imagem em contratos distintos. (proposta)
- Mesmo IP ou dispositivo em contratos de cidades ou datas diferentes. (proposta)
- Horários coincidentes ou incompatíveis entre contratos atribuídos ao mesmo titular. (proposta)
- Mesmo ponto de GPS ou mesmo IP repetido em datas ou contratos diferentes: o `geo_check.py` faz esse cruzamento quando cada evento traz o campo `contrato`. (proposta)

## VF8. Contratos na mesma data

- Gatilho: o extrato INSS mostra 2 ou mais contratos incluídos no mesmo dia ou em intervalo curto. [FSC11]
- Achado: padrão de portabilidade seguida de refinanciamento no mesmo dia (ou o inverso) indica operação em cadeia orquestrada pelo correspondente, incompatível com deliberação livre do consumidor idoso ou hipossuficiente. [FSC11]
- Reforça outros fundamentos; raramente decide sozinho. [FSC11]
- O que é "intervalo curto" não está definido nos arquivos; o advogado define.

## VF9. Geolocalização

Executar quando o contrato, a CCB ou a trilha de assinatura juntada pelo réu trouxer coordenadas, IP ou Cidade-UF. Usa `scripts/geo_check.py`.

**Pressuposto: localização distante da residência, no log do réu, é indício de fraude, e o ônus de explicá-la é do banco** (o documento é dele; Tema 1061/STJ, por analogia; ver `referencias_juridicas.md`). A skill aponta a inconsistência; não pede ao autor que prove a fonte nem a presença. Ressalva de redação: dizer "o log juntado pelo réu registra", sem afirmar a fonte quando o log não a informa.

**Referência única: a residência do autor.** Os autos normalmente não trazem o endereço do ponto de venda ou da "casa de empréstimo", então ele não serve de segundo referencial. Se o contrato foi feito na mesma cidade, a coincidência de município não esclarece nada. O teste decisivo é a distância entre o ponto registrado e a residência, em escala local, e o cruzamento com os demais dados dos autos.

1. Extrair dos autos, com ID e página de cada dado: coordenadas (lat/long), precisão do GPS em metros (se o log informar), IP, Cidade-UF do log, data e hora com fuso, dispositivo e a FONTE da geolocalização (GPS do dispositivo, REDE, que é Wi-Fi ou torre de celular, ou IP). Se o log não disser a fonte, registrar "não identificada". Se houver mais de um contrato, registrar também o número do contrato em cada evento.
2. Extrair a residência do autor (comprovante de residência, inicial, extrato INSS, procuração) com ID e página. Para a distância, a coordenada da residência vem do advogado, copiada de um mapa (com a precisão estimada, se souber), ou do **ponto de assinatura da procuração outorgada ao escritório**, que o advogado declarou ser tomado como o local da residência (feita com o apoio do escritório, a precisão é suficiente para contrastar o log do réu). Nos dois casos, o ponto é a residência: entra em `autor.lat`/`autor.lon` com `fonte` só com ID e página (não escrever na fonte fatos que os autos não trazem, como "feita com apoio do escritório"; Regra 6), sem pendência e sem revisão humana. **Na peça, na legenda, na figura e no quadro, o ponto se chama sempre "residência" ("endereço da residência"), nunca "procuração" ou "ponto de assinatura".** O campo `autor.referencia_de`, de versões anteriores, é ignorado. Não parar a análise por falta de coordenada: sem ela, executar só a comparação por Cidade-UF e registrar a pendência para o cartão de pausa. Não inferir a coordenada a partir do endereço por conta própria (Regra 17). Informar também a Cidade-UF da residência, para o teste de município continuar valendo. Ponto derivado do log do réu nunca serve de referência.
3. Gravar os dados em um JSON no formato de `scripts/exemplo_entrada.json` e rodar:
   `python3 scripts/geo_check.py entrada.json --saida-md quadro_geo.md --saida-json quadro_geo.json`
   (o teste de município usa, por padrão, a malha da Bahia da skill, `assets/ba_municipios.json`; ponto fora da Bahia sai como informativo e o teste de distância decide. Para outro estado, passar `--municipios malha.geojson`).
4. Conferir cada linha do quadro contra a imagem da página citada. Linha que não puder ser confirmada visualmente sai do quadro ou vira REVISÃO HUMANA OBRIGATÓRIA.
5. **Cruzar** o resultado com os demais dados dos autos: compatibilidade espaço-tempo entre os eventos do log, pontos e IPs que se repetem em datas ou contratos diferentes, horário da contratação e fatos já provados nos autos sobre a rotina ou a situação do autor naquele dia. Não introduzir fato novo (Regra 6).
6. Levar o resultado ao quadro de indícios, com a classificação e a fonte de cada coordenada.
7. **Gerar as Figuras Ilustrativas** (para todo evento com resultado DIVERGENTE, de qualquer fonte; ponto repetido gera uma só figura):
   `python3 scripts/geo_figuras.py entrada.json --saida-dir figuras/`
   O conjunto é de **três imagens obrigatórias, nesta ordem**: **A** visão geral dos dois pontos (painel largo de 1.296 x 480 px, offline) com os dois pontos numerados, a linha tracejada com a distância, a escala, a grade métrica e os limites municipais da Bahia (`assets/ba_municipios.json`, derivado da Malha Municipal Digital do IBGE, 2025), com os municípios dos dois pontos em destaque e nomeados; **B** captura de mapa de ruas do local registrado no log; **C** captura de mapa de ruas da residência do autor, com os círculos de 100 m (verde) e 150 m (vermelho tracejado). B e C saem do arquivo `regiao.pmtiles` (convenção: nome exato, raiz da pasta conectada). **Sem o arquivo, a geração para** (código 5) **e o Cowork pergunta ao usuário**: colocar o arquivo ou autorizar expressamente só a visão geral (`--fundo esquema`). Evento fora da área do arquivo sai só com a visão geral e o aviso "FIGURA INCOMPLETA" (`completa: false`), com a mesma pergunta. O script grava `fig_evento<N>_A_visao_geral.png`, `_B_log.png` e `_C_residencia.png`, `figuras.json` (`paineis`, com a ordem e a legenda de cada imagem; município de cada ponto, avisos, `completa` e `nota_rodape`) e `links_coordenadas.md`. A visão geral não precisa de rede nem de navegador e não dispara a Regra 19. Olhar cada imagem antes de usar. Dependências: Pillow e, para B e C, Playwright com Chromium.
   **Nota de rodapé de conferência.** Cada figura traz uma nota com os links do OpenStreetMap e do Google Maps para as duas coordenadas, para o juiz abrir o ponto em mapa com um clique. O ponto de referência é a residência, que já consta dos autos (Regra 17: na peça, sempre "residência").
   **Município de cada ponto.** O script informa em que município da Bahia cai cada coordenada, pelos polígonos do IBGE. A malha é simplificada (tolerância de 40 m; em teste com 784 pontos aleatórios dentro da Bahia, a classificação coincidiu com a da malha completa em todos). Ponto a menos de ~100 m de divisa recebe aviso; ponto fora da Bahia sai sem nome de município. Para atualizar a malha: `python3 scripts/geo_malha.py --construir BA_Municipios_<ano>.shp` (a malha de outro estado exige outro arquivo `.json`). Antes de citar a fonte na peça, ler a Nota Metodológica do IBGE indicada no LEIA-ME da malha.

**Capturas de mapa de ruas (B e C).** O ambiente da skill não tem acesso confiável aos tiles de mapa na internet: a nuvem bloqueia (HTTP 403), o shell do Cowork roda numa máquina virtual separada do computador do usuário e o navegador embutido do Cowork não abre `file://` nem `localhost`. Por isso as capturas vêm de um arquivo local, o `regiao.pmtiles` (guia para gerá-lo, uma vez: `references/mapa_offline_pmtiles.md`), renderizado dentro do Cowork pelo `geo_mapa_pmtiles.py`, sem rede, sem servidor externo e sem clique do advogado. Conferir antes o `regiao.pmtiles` (raiz da pasta conectada), trazendo-o se estiver só no computador do advogado. O `geo_figuras.py` chama o `geo_mapa_pmtiles.py` e o `geo_compor.py`, que grava as imagens A, B e C e a lista `paineis`. Conferir cada imagem (mapa de fundo visível, pontos marcados, distância e atribuição corretas). Teste: o renderizador foi testado num Chromium de teste com um PMTiles sintético; ainda não foi verificado com o arquivo real do Protomaps no Cowork do usuário.

Classificações do quadro:

| Classe | Significado |
|---|---|
| COMPATIVEL | GPS ou REDE dentro do raio da residência (100 m), já descontada a precisão (a da REDE conta em dobro) |
| DIVERGENTE | GPS ou REDE além do limite local da residência (150 m), mesmo na mesma cidade; IP ou fonte não identificada além de 5 km (`LIMITE_IP_KM`); município diferente; pontos incompatíveis entre si no mesmo fluxo; ou ponto fixo e recorrente fora da residência, de qualquer fonte |
| REVISÃO HUMANA OBRIGATÓRIA | Tudo o que cai fora dessas faixas: dado ausente ou inválido, REDE sem precisão informada, faixa entre 100 e 150 m de GPS ou REDE, deslocamento só possível por avião. O script não conclui; sai em caixa alta e vermelho |
| informativo | Contexto sem conclusão: só a cidade coincide; IP ou fonte não identificada até 5 km (aproximação normal, nunca COMPATIVEL); IP repetido em contratos diferentes; ou o ponto recorrente é a própria residência |

**Como tratar a REVISÃO HUMANA OBRIGATÓRIA (Regra 19).** O script emite um aviso em vermelho ao final e uma faixa no topo do quadro quando há ao menos um item. Em cada item, o advogado decide: usar como indício, descartar ou buscar mais elementos nos autos. Até a decisão, o item não entra na peça. Não reclassificar por conta própria nem omitir.

**Fonte REDE (Wi-Fi ou torre).** Trata como o GPS, com duas diferenças: só conclui se o log informar a precisão em metros (sem ela, REVISÃO HUMANA OBRIGATÓRIA) e a margem de precisão é dobrada (`FATOR_PRECISAO_REDE`, 2). Exemplo: rede com precisão de 40 m e autor com 10 m geram margem de 90 m, então só vale DIVERGENTE acima de 240 m e COMPATIVEL até 10 m. O fator 2 é uma proposta conservadora, a validar.

**Indicadores sem coordenada.** Muitos logs não trazem GPS. A fraude pode aparecer por outros campos, e cada banco registra o seu conjunto, que muda com o tempo. O quadro do `geo_check.py` traz a seção "Indicadores sem coordenada" e classifica cada item em três níveis:

| Nível | Quando | Exemplos |
|---|---|---|
| Forte | Objetivamente verificável nos autos e difícil de explicar sem fraude | Selfie ou biometria de outra pessoa, BSSID ou ERB que localiza fora da região do autor, telefone ou e-mail comprovadamente de terceiro |
| Médio | Pesa, mas pede contexto ou outro achado | Aparelho repetido em contratos de terceiros, nome de rede de estabelecimento, telefone cadastrado pouco antes do contrato, correspondente com outros contratos suspeitos |
| Reforço | Não decide sozinho | Fuso diferente, DDD de outro estado, horário atípico, intervalo curto entre etapas, sistema ou navegador diferente do histórico, provedor de outra região |

Como funciona: (a) o script faz as checagens automáticas que não dependem de coordenada (IP interno, CGNAT, fuso, DDD, horário, intervalo, aparelho repetido); (b) os demais campos do log entram na lista `indicadores` do JSON (`campo`, `valor`, `fonte` com ID e página, `avaliacao` opcional) e o script os cruza com `scripts/catalogo_indicadores.json`, que traz a pergunta de verificação de cada tipo; (c) campo que o catálogo não conhece, ou sem `avaliacao`, vira REVISÃO HUMANA OBRIGATÓRIA. Depois de ler o campo nos autos, o advogado preenche `avaliacao` com `INDICIO_FORTE`, `INDICIO_MEDIO`, `REFORCO` ou `SEM_RELEVANCIA`. Campo novo de banco deve ser acrescentado ao catálogo (edição em JSON, sem mexer no código). Indício fraco isolado não prova nada: a peça trabalha a convergência de vários indícios, e um item Forte sem apoio ainda exige cautela. Horário atípico (00h às 5h) e intervalo curto (30 s) são limites propostos, a validar.

Critérios (Regras 16 e 17): a divergência é apontada qualquer que seja a fonte, porque o ônus é do banco; a fonte só decide a redação (GPS e REDE permitem afirmar que o log registra a posição; IP ou fonte não identificada pedem o dilema da Regra 16). O IP repetido em contratos diferentes liga os contratos a uma origem de rede e é reforço. O conjunto de indícios sem coordenada sustenta a tese de fraude apenas pela convergência, nunca pela afirmação de local. Sem ID e página, a coordenada não entra. Coincidência só de cidade nunca é apresentada na peça como compatibilidade.

Limites: o `geo_check.py` não acessa a rede, não geocodifica endereço, não consulta base de IP (o `ip_check.py` consulta o RDAP, salvo com `--sem-rdap`) e não confirma que um endereço existe. O `geo_figuras.py` não acessa a rede: a visão geral vem da malha do IBGE e as capturas B e C, do `regiao.pmtiles` local. A presença do autor no local não é fraude por si só, e o resultado é indício de inconsistência, não prova. Os limiares são parâmetros e podem ser ajustados por linha de comando: raio da residência 100 m (`--raio-residencia-m`), limite local 150 m (`--limite-local-m`), IP ou fonte não identificada 5 km (`LIMITE_IP_KM`, no topo do script), 120 km/h terrestre e 900 km/h máximo. A precisão do GPS informada no log (e a da coordenada do domicílio) é descontada: com 50 m de margem somada, só vale COMPATIVEL até 50 m e só vale DIVERGENTE acima de 200 m. Estão definidos no topo de `geo_check.py`.

## Quadro de indícios

Ao fim da ETAPA 2-B, consolidar os achados de VF1 a VF9 em um quadro único, que alimenta a síntese (2-D) e o mapa de ataque (Etapa 3):

| # | Verificação | Achado | ID e página | Gravidade | Fundamento que alimenta |
|---|---|---|---|---|---|

## Escala de gravidade (proposta, validar)

- **Crítico:** indício objetivamente verificável nos autos e autônomo. Exemplos que o catálogo já trata assim: e-mail ou telefone de terceiro e campo de localização vazio [FSC2]; correspondente sem contrato ou credenciamento comprovado [FSC10]; hash idêntico em arquivos com nomes distintos e ausência de qualquer instrumento de cessão [FSC5]; GPS ou REDE divergente do domicílio (inclusive na mesma cidade, além do limite local), IP ou fonte não identificada além de 5 km, ponto fixo e recorrente fora da residência, ou eventos de GPS fisicamente incompatíveis entre si (VF9).
- **Relevante:** pesa, mas depende de contexto ou de outro achado. Exemplos: IP privado no log (falta o IP público da sessão), Cidade-UF do log diferente do domicílio, datas incoerentes (CCB antes da trilha), dados cadastrais divergentes, biometria sem relatório técnico.
- **Reforço:** não decide sozinho. Exemplos: padrão de contratos na mesma data [FSC11], IP repetido em contratos diferentes e indicadores sem coordenada de nível Reforço (fuso, DDD, horário, intervalo curto).

## Quesitos para perícia (Justiça Comum)

A skill não cria quesitos. Usar os que constam da réplica ou da petição de saneamento. Se não houver, registrar a lacuna no cartão de pausa para o advogado decidir. Perícia que cada verificação pode motivar: assinatura manuscrita (VF2) pede perícia grafotécnica; trilha eletrônica (VF4, VF9) pede perícia em informática forense. [FSC9]

## Pendências de definição (para o advogado)

- VF8: quantos dias configuram "intervalo curto".
- VF7: validar os três critérios marcados como proposta.
- VF5: confirmar a terminologia de "credenciamento".
- Escala de gravidade: validar os três níveis e os exemplos.
- VF9: os limiares de 100 m e 150 m foram definidos pelo advogado. O limite de 150 m é fragilidade provável na peça (precisão do GPS e da coordenada do mapa). Uma amostra de logs reais de casos já julgados permitiria calibrar.
