# Mudanças em relação ao modelo AMN v1.4 (não contratado)

O modelo anterior vivia em `modelo_formatado_amn.docx` (que é, no fundo, o texto de **migrado**) e em strings do `gerar.py`. Este modelo em Markdown foi montado em 28/10/2026 a partir desse texto, com as trocas abaixo. Cada troca vem de uma pendência do painel (D1 a D17) ou de um problema encontrado na leitura.

| # | No modelo anterior | Agora | Motivo |
|---|---|---|---|
| 1 | "Ora, Excelência…" | fórmula impessoal | decisão do escritório (28/10/2026) |
| 2 | "dos sérvios" (erro de digitação) | "dos serviços" (citação literal do art. 14 do CDC) | corrigido pelo motor antigo; agora vem do acervo |
| 3 | Menção à "resolução 3.694/09" do Banco Central | retirada | fora do acervo; a Súmula 297 do STJ basta |
| 4 | Dobra fundada na "má-fé" da ré, provada por "rápida pesquisa no PROJUDI" de casos "idênticos e repetitivos" | dobra pelo art. 42, parágrafo único, e pela tese do EAREsp 676.608/RS (boa-fé objetiva), sem o Tema 929 (decisão de 29/10/2026); a frase do PROJUDI saiu | má-fé não é requisito segundo as referências; a frase do PROJUDI é fato não provado e fala em volume de ações |
| 5 | Dano moral "conforme Súmula 326 do STJ" para caráter punitivo | Súmula 40 do TJBA; função pedagógica mantida como decisão do escritório; a Súmula 326 só aparece para dizer que o valor é estimativo e que a condenação inferior não gera sucumbência recíproca | a Súmula 326 trata de sucumbência (D4) |
| 6 | Ementa do TRF-4 inteira, com o item 5 sobre EAREsp 600.663 e modulação de 30/03/2021 | trecho dos itens 1, 3 e 4, sem marca; typo "R10.000,00(dezmilreais)eR20.000,00" corrigido | o item 5 (modulação) não é usado, por decisão do escritório de 29/10/2026; a ementa está no acervo, conferida no portal do TRF-4 (`references/jurisprudencia/ac-5003696-trf4.md`, VERIFICADO) |
| 7 | Tabela de documentos com "Res. CMN 4.753/2019", "LGPD, art. 37" e "Res. BCB 96/2021" como normas de guarda | IN 28/2008 art. 5º, IN 138/2022 art. 5º, Res. CMN 4.935 art. 3º, p. único, art. 429, II e 373, II do CPC | 4.753 trata de conta de depósitos; LGPD art. 37 e Res. BCB 96 não tratam de guarda de trilha (D2 e D5) |
| 8 | Efeito da não apresentação: "Inexistência confirmada", "Prova ausente", "Averbação irregular" | JEC: valoração contra o banco (art. 373, II); Justiça Comum: art. 400 do CPC | "inexistência confirmada" não tem base legal (D6) |
| 9 | Pedido de juntada para todos os ritos | JEC: só como encargo da inversão; Justiça Comum: exibição (arts. 396 a 404 do CPC), sem perícia na inicial (a necessidade fica para a réplica) | decisão do escritório de 28/10/2026 |
| 10 | Tutela: "tutela de evidência" citando o art. 300 | tutela provisória **de urgência**, arts. 294 e 300, e § 3º do art. 300 | o texto antigo misturava evidência e urgência |
| 11 | Prescrição citava "AREsp 738.991/RS" | "EAREsp 738.991/RS", caso de telefonia fixa, por analogia, sem marca (ver item 24) | designação correta (D10) |
| 12 | Aviso do motor sobre "modulação do EAREsp 600.663/RS" para descontos anteriores a 30/03/2021 | pede-se o dobro de todos, sem Tema 929; o tópico da dobra cita o EAREsp 676.608/RS e, para os descontos anteriores a 30/03/2021, apoia a dobra só no art. 42, parágrafo único (bloco `[[SE HÁ DESCONTO ANTES DE 30/03/2021]]`, avisado pelo `calcular.py`) | decisão de 29/10/2026 (substitui a de 28/10/2026); ver item 28 |
| 13 | Honorários "em caso de recurso" (JEC) ou "custas e honorários" (motor) | JEC: nenhum pedido (art. 55 da Lei 9.099); Justiça Comum: art. 85 do CPC | regra do rito |
| 14 | Fatos genéricos: "não sabe usar plataformas digitais…" | mantido como afirmação, sem condicional (decisão do escritório de 28/10/2026: clientes majoritariamente idosos) | presunção pelo perfil; sem prova nos autos. Retirar o parágrafo se o cliente for jovem ou usar banco digital |
| 15 | Fatos sem impugnação por contrato | subtópico "nega, contrato a contrato", com valor liberado do extrato | previne FSC1, FSC2, FSC4 e FSC7 |
| 16 | Estatuto do Idoso | Estatuto da Pessoa Idosa (Lei 10.741/2003, art. 71) | nome atual da lei |
| 17 | Assinaturas e intimações com nomes fixos | subscritores padrão do escritório (Diego Ramos Arléo Barbosa, OAB/BA nº 38.179, e Michael Santos Neves, OAB/BA nº 50.954), nas intimações e na assinatura | `assets/padrao-pecas.md` (subscritores padrão) |
| 18 | Fecho com cidade do autor | juízo e cidade do fecho não se perguntam: saem do `foro` do `calculo.json` (cidade-sede do juízo, pelo endereço do autor) | decisão de 03/11/2026 (substitui a de 28/10/2026) |
| 19 | "em face [RÉU]" sem artigo; título "Da tramitação prioritária" e pedido "b" soltos sem idade de 60 anos; letras dos pedidos pulando; "durante de MM/AAAA"; "(s)" sem resolver; linha de tabela com fundamento sem documento | artigo do `reus.json`; título e pedido dentro do condicional; instruções de acabamento no topo (reletrar, "(s)", "pensionista", rótulo literal do extrato); "no período de" | defeitos vistos em peça gerada do modelo irmão `tese-1000` (08/11/2026) |
| 20 | Tabela de documentos citava IN 28 e IN 138 juntas para todos os contratos | cada linha cita só a norma que algum contrato exige (por contrato, pela data) | contratos de datas diferentes; a IN 138 não vigia antes de 13/12/2022 |
| 21 | Biometria: "jamais forneceu sua imagem facial, dados biométricos…" | "não forneceu, para os contratos impugnados…" | a afirmação ampla pode ser desmentida por contrato anterior |
| 22 | Motivo da Exclusão sempre no modelo | condicionado a [[SE MOTIVO]] (contrato ativo, ou excluído com o campo em branco) | contrato só "Encerrado" não tem o campo a preencher |
| 23 | Obrigação de não fazer sem multa; juros sem ressalva da Lei 14.905 | multa de R$ 1.000,00 por evento (art. 537 do CPC); "observada a Lei 14.905/2024 a partir de 30/08/2024" nos pedidos de restituição e de dano moral | decisões do escritório de 08/11/2026 (PAINEL) |
| 24 | Prescrição só com o EAREsp 738.991/RS | tópico cita a segunda tese do EAREsp 676.608/RS (trecho transcrito, não modulada) e o 738.991 ao lado, sempre prazo decenal | o inteiro teor do 676.608 está no acervo; decisão de 05/11/2026 (decenal) |
| 25 | Audiência: pedido "interesse na audiência de conciliação" em todos os ritos | Justiça Comum: tópico "Da audiência de conciliação e da composição extrajudicial" (desinteresse, e-mails e telefone); JEC: nada se declara | decisão do escritório de 08/11/2026 |
| 26 | Fatos em texto corrido, sem narrativa | tópico "Dos descontos sem contratação: o que o extrato registra, contrato a contrato" (PRIMEIRO a QUINTO), só com dados do extrato; com sinais de cadeia de refinanciamentos, bloco `[[SE HÁ CADEIA]]` que a descreve pelo extrato (o portão que parava a geração saiu em 08/11/2026) | comparativo C x D (08/11/2026) |
| 27 | "Do direito" em tom neutro | frases de ligação e de argumento reescritas (firme e elegante); citações, transcrições, marcas e títulos intactos | decisão do escritório de 08/11/2026 |
| 28 | Frase de modulação só para desconto anterior a 30/03/2021 | acrescentado o ramo "todos os descontos depois de 30/03/2021" | consistência com a `tese-1000` |

## Itens do modelo anterior mantidos com marca de conferência

- Tabela das seis "vantagens" do campo "Motivo da Exclusão": o fundamento 4 (CPC 497 e CC 422) saiu sem marca no modelo atual; o 6 cita o Acórdão 1.094/2026-TCU-Plenário, incluído no acervo em 03/11/2026 (`references/jurisprudencia/acordao-1094-2026-tcu.md`), pelo item 9.3.2.
- Multa diária de R$ 500,00 e prazo de 10 dias úteis do campo "Motivo da Exclusão": mantidos por decisão do escritório.
- Dano moral de R$ 20.000,00: fixo.

## Revisão de 08/11/2026 (comparativo C x D, caso Paraná)

- **Valor liberado zero ou ausente:** o modelo dizia "hipótese compatível com portabilidade ou refinanciamento sem crédito novo ao beneficiário", que entrega a defesa ao banco, e ainda mandava o banco "comprovar o crédito de valor idêntico ao liberado", pedido sem objeto quando o liberado é zero. Agora há dois ramos: com valor positivo, o banco comprova o crédito; com zero ou ausente, "um desconto mensal sem crédito correspondente é o que cabe ao banco explicar (art. 373, II, do CPC)". A linha da tabela de documentos que pede o comprovante do crédito só entra com algum contrato de valor liberado positivo.
- **Alerta trienal (decisão de 08/11/2026):** o script `calcular.py` avisa, com o valor exposto, quando há desconto com mais de 3 anos e nenhum com mais de 5 (o gatilho do tópico de prescrição continua em 5 anos). No caso do Paraná, três contratos de 2022 (R$ 1.077,72 simples) ficam nesse intervalo. O teste cobre o alerta.
- **Cadeia de refinanciamentos (decidido com o usuário):** a narrativa é "nunca contratados", apoiada no termo do cliente que não reconhece os contratos. O portão que mandava parar e perguntar saiu; entrou o bloco `[[SE HÁ CADEIA]]` no tópico narrativo, que descreve a cadeia só pelo extrato (averbações em pares no mesmo dia, mesmas parcelas, valor liberado zero ou ausente) e diz que quem não firmou o primeiro elo não firmou os que dele derivam. O portão só resta para quando o termo do cliente não nega os contratos. O risco que continua: contratos com muitas parcelas pagas sem reclamação (os três de 2022, 12 parcelas) permitem ao banco alegar ratificação.
- **Fica para decisão:** tese da quitação do REsp 1.771.984/RJ (de portabilidade entre bancos, não de refinanciamento interno); inclusão ou não dos três contratos de 2022; pedido de citação eletrônica (art. 246, I, do CPC), que a Peça D tinha.

## Limites

O texto antigo foi lido por inteiro, mas a comparação com o novo é manual. O verificador (fase 5) fará a checagem automática de citações e de remissões.

## Revisão de 16/11/2026

- **Cadeia de portabilidade ou refinanciamento:** a skill não pergunta mais ao advogado (havia formulário "Redigir e descrever a cadeia / Redigir sem narrar / Pausar") e a inicial não narra a cadeia: cada contrato é descrito pelo extrato, e a cadeia fica para a réplica. Saiu o bloco `[[SE HÁ CADEIA]]` e a regra de parar quando o termo não nega os contratos. No `escrutinio.py`, FSC5 (origem de portabilidade ou refinanciamento) e FSC11 (datas próximas) deixaram de ser ATIVADO nas iniciais. Substitui a decisão de 08/11/2026.
