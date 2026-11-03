// Configuração do verificador para o pacote de consignado (direito do consumidor bancário, benefício do INSS).
// Regra de ouro: cada erro que aparece duas vezes vira uma regra nova aqui. Cada regra abaixo nasceu de um
// problema real do modelo AMN v1.4 (ver nao-contratado/references/02-mudancas-no-modelo.md e o PAINEL).
'use strict';

// Termos que não podem voltar em modelo nem em peça gerada.
const PROIBIDOS = [
  { re: /Excel[êe]nt[íi]ssimo|\bExcel[êe]ncia\b|Exmo\.|Meritíssimo|V\. ?Exa/, msg: 'tratamento antigo (decisão de 28/10/2026: fórmula impessoal)' },
  { re: /(?<!n[ãa]o citar a )S[úu]mula 326(?![^.\n]{0,160}sucumb[êe]ncia)/, msg: 'Súmula 326/STJ fora de nota de advertência ou do ponto de sucumbência (ela não trata de caráter punitivo)' },
  { re: /[Ii]nexist[êe]ncia confirmada/, msg: '"inexistência confirmada" como efeito da não exibição (usar o art. 400 do CPC ou a valoração contra o banco)' },
  { re: /4[.]753/, msg: 'Res. CMN 4.753/2019 (trata de conta de depósitos, não de consignado)' },
  { re: /Res(?:olução)?[.]? BCB\s*(?:n[ºo.]?\s*)?96\b/, msg: 'Res. BCB 96/2021 (conta de pagamento; sem norma de guarda de trilha de consignado)' },
  { re: /LGPD,? art[.] 37/, msg: 'LGPD art. 37 como norma de guarda da trilha' },
  { re: /PROJUDI|situações idênticas e repetitivas/, msg: 'fato não provado sobre volume de ações do banco' },
  { re: /3[.]694/, msg: 'Res. 3.694/09, fora do acervo' },
  { re: /\[sic|Tema 925|Nota para o redator/, msg: 'resíduo de rascunho' },
  { re: /Tema (?:Repetitivo )?929/, msg: 'Tema 929/STJ como fundamento (decisão do escritório de 29/10/2026: acórdão não publicado; atualizar quando sair)' },
  { re: /n[ãa]o havia cr[ée]dito a (?:migrar|ceder)|cr[ée]dito que nunca existiu/i, msg: '"não havia crédito a migrar" (decisão do escritório de 29/10/2026: argumento perigoso; só a cessão não notificada, CC art. 290)' },
  { re: /MP 1[.]393|Medida Provis[óo]ria (?:n[ºo.]? ?)?1[.]393/, msg: 'MP 1.393/2026 (decisão do escritório de 29/10/2026: não entra na petição)' },
  { re: /600[.]663/, msg: 'EAREsp 600.663/RS como base de modulação (superada pelo Tema 929; ver protocolo)' },
  { re: /art[.] 2º-C,? (?:da |, )?Res(?:olução|[.])? CMN (?:n[ºo.]? ?)?5[.]112/, msg: '"art. 2º-C da Res. CMN 5.112" (o art. 2º-C é da Res. CMN 4.549, incluído pela 5.112)' },
  { re: /art[.] 292, IV/, msg: 'art. 292, IV, do CPC (divisão/demarcação): inciso errado' },
  { re: /Enunciados? (?:16[12])(?:\s+e\s+16[12])? do FONAJE/, msg: 'Enunciados 161/162 do FONAJE na peça (decisão do escritório de 28/10/2026: não citar)' },
  { re: /pr[áa]tica sist[êe]mica|ilícito de massa/i, msg: 'afirmação sem fonte no acervo (prática "sistêmica" ou "ilícito de massa" do banco)' },
  { re: /nenhuma das normas de reg[êe]ncia autoriza|Opera[çc][ãa]o Sem Desconto/i, msg: 'migração "que nenhuma norma autoriza" (a IN 138, art. 11, e a IN 28, art. 56, admitem a cessão) ou Operação Sem Desconto como contexto de consignado (ela apurou descontos associativos)' },
  { re: /\[(?:VERIFICAR|CONFERIR)[^\]]{0,80}(?:data de publica[çc][ãa]o|DJe|DOU|encontro e data|contagem do prazo|situa[çc][ãa]o do tema)/i, msg: 'marca de data de publicação, vigência ou situação de tema (protocolo, "Datas de julgamento, publicação e vigência": a skill resolve; omita o elemento sem fonte e relate na nota de entrega)' },
  { re: /S[úu]mula 30 (?:da Turma|do TJBA)|desvio produtivo/i, msg: 'Súmula 30/TJBA (desvio produtivo): o escritório não faz reclamação administrativa (decisão de 30/10/2026)' },
  { re: /Lei (?:n[ºo.]? ?)?14[.]905/, msg: 'Lei 14.905/2024 nos pedidos de correção e juros (decisão de 30/10/2026: não se aplica)' },
  { re: /nega a contrata[çc][ãa]o de origem|nega ter firmado esse contrato, com o banco de origem/i, msg: 'migrado: nega-se a migração, não a contratação de origem (decisão de 30/10/2026)' },
  { re: /\[CONFIRMAR COM O CLIENTE/, msg: 'marca de confirmação com o cliente: os fatos do cliente são presumidos (decisão de 30/10/2026)' },
  { re: /(?:^|\n)#{0,3} ?\**A[ÇC][ÃA]O (?:DECLARAT|[A-ZÀ-Ú]{4,} )/, msg: 'nome da ação em caixa alta (decisão de 30/10/2026: só a primeira letra de cada palavra principal em maiúscula)' },
  { re: /honor[áa]rios advocat[íi]cios em caso de recurso|Nestes termos/, msg: 'pedido ou fecho do modelo antigo' },
];

// RMC: o cartão é contrato, então os juros de mora contam da citação (Súmula 33 da Turma de Uniformização do TJBA),
// não do evento danoso (Súmula 54/STJ, responsabilidade extracontratual). Protocolo, "Regras de citação e de pedido vigentes".
const JUROS_RMC = { re: /S[úu]mula 54|juros de mora desde o evento danoso/i, msg: 'RMC com juros desde o evento danoso (Súmula 54/STJ): no RMC os juros contam da citação (Súmula 33/TJBA)' };

// O dano moral é fixo em R$ 20.000,00 (decisão do escritório de 28/10/2026) e tem de aparecer nos três lugares.
// A contagem simples não serve: a ementa do TRF-4 citada na peça também traz R$ 20.000,00.
const DANO_MORAL = [
  { re: /o valor de \*{0,2}R\$ 20[.]000,00/, msg: 'fundamentação sem o dano moral de R$ 20.000,00' },
  { re: /indeniza[çc][ãa]o por danos extrapatrimoniais de \*{0,2}R\$ 20[.]000,00/, msg: 'pedido sem o dano moral fixo de R$ 20.000,00' },
  { re: /dano extrapatrimonial \(R\$ 20[.]000,00\)/, msg: 'valor da causa sem o dano moral fixo de R$ 20.000,00' },
];

module.exports = {
  // As cópias entre skills e o acervo são conferidas pelo manifesto (_acervo/manifesto.json).
  copias: [],

  proprioPorSkill: /^(INDEX|MAPA|ESTRUTURA)\.md$/,

  // Skills sem protocolo/protocolo.md (formatação).
  semProtocolo: ['tipografia-azul'],

  // Skills que não redigem peça (coordenador e triagem): o protocolo comum cita assets/ que elas não carregam.
  semPecas: ['consignado', 'triagem-consignado'],

  descricaoMax: 1024,

  nomes: {
    // Nomes do pacote AMN v1.4 que foram trocados: citá-los é erro.
    antigos: /redacao-nao-contratado|redacao-migrado|redacao-tese1000|redacao-rmc|amn-iniciais-consignado/,
    // Se citada entre crases, a skill precisa existir (o filtro só pega nomes com hífen).
    devemExistir: /^(nao-contratado|rmc|tese-1000|migrado|replica-consignado|triagem-consignado|recurso-inominado-consignado-geolocalizacao|recurso-consignado|tipografia-azul)$/,
    // Skills do plano que ainda não foram criadas: a citação gera aviso, não erro. Remova da lista ao criar.
    planejadas: [],
    // Skills que existem fora do pacote (instaladas à parte no ambiente do escritório): a citação é válida.
    externas: ['tipografia-azul'],
  },

  modelos: {
    naoPeca: /quesitos|roteiro|checklist|INDEX|padrao-pecas/,
    judicial: /inicial|recurso|replica|contrarrazoes|apelacao/,
    // As exigências abaixo valem só para os modelos de inicial (dano moral, valor da causa, honorários do JEC).
    exigeSoEm: /^modelo-inicial/,
    exigeEmTodos: [
      { re: /pede deferimento/, msg: 'sem o fecho "Termos em que, pede deferimento."' },
      ...DANO_MORAL,
      { re: /art[.] 55 da Lei 9[.]099/, msg: 'sem a regra de honorários do primeiro grau do JEC (Lei 9.099/95, art. 55)' },
    ],
    proibeEmTodos: PROIBIDOS,
    remeteAoPadrao: 'padrao-pecas.md',
    exigeNasJudiciais: [
      { re: /Precedentes Judiciais Evocados/i, msg: 'peça judicial sem o tópico de precedentes' },
    ],
    regrasPorArquivo: [
      { arquivo: /modelo-inicial-rmc[.]md$/, proibe: JUROS_RMC.re, msg: JUROS_RMC.msg },
    ],
    avisosCondicionais: [
      { se: /barreira t[ée]cnica/i, exige: /barreira t[ée]cnica[^\n]{0,200}CONFERIR/i, msg: '"barreira técnica" sem a marca [CONFERIR] da fonte (D28)' },
      { se: /Tema 929/, exige: /VERIFICAR ANTES DE PROTOCOLAR/, msg: 'cita o Tema 929/STJ sem a marca [VERIFICAR ANTES DE PROTOCOLAR]' },
      { se: /IN 143|IN PRES\/INSS 138/, exige: /CONFERIR/, msg: 'trata de biometria sem marca [CONFERIR] sobre o prazo prorrogado pela IN 143/2023' },
    ],
  },

  // O pacote usa a verificação "extras" (abaixo), que lê os formatos de arquivo deste pacote.
  citacoes: { ativo: false, tribunais: 'STJ|STF' },

  extras: {
    checagem: {
      arquivo: 'checagem-fsc-vf.md',
      statusFsc: ['ATIVADO', 'OK', 'NAO_SE_APLICA', 'PENDENTE_ADVOGADO'],
      statusVf: ['EXECUTADA', 'NAO_SE_APLICA', 'PENDENTE_ADVOGADO'],
      // FSC3: a inicial abre o ônus pelo art. 14, § 3º, do CDC, pelo art. 429, II, do CPC e pelo Tema 1061/STJ.
      // O RMC não discute assinatura: só o art. 14, § 3º.
      fsc3: {
        padrao: [/art[.] 14, § 3º/, /art[.] 429, II/, /Tema (?:Repetitivo )?1061/],
        rmc: [/art[.] 14, § 3º/],
      },
      // FSC9: o rito se lê do endereçamento (primeiros 800 caracteres da peça).
      // comarca sem Vara do Sistema: o endereçamento é a vara cível, e o JEC se reconhece pelo preâmbulo
      jec: { endereco: /JUIZADO/i, preambulo: /pelo procedimento da Lei nº 9\.099\/95/, proibe: [/Requer-se, também, a exibição dos documentos/, /pede-se perícia grafotécnica/i], msg: 'FSC9: peça de JEC com pedido de exibição ou perícia (não cabe no Juizado)' },
      comum: { exige: [/arts?[.] 396 a 404 do CPC/], msg: 'FSC9: peça de Justiça Comum sem o pedido de exibição (arts. 396 a 404 do CPC)' },
      // FSC1/FSC7: cada contrato do cálculo tem a sua negativa específica.
      negativaPorContrato: /^(nao-contratado|migrado|tese-1000)$/,
    },
    // Artigo citado existe na norma do acervo (confere a existência do artigo, não o texto do parágrafo ou inciso).
    artigos: [
      [/^(CPC|C[óo]digo de Processo Civil)$/, 'cpc.md'],
      [/^(CDC|C[óo]digo de Defesa do Consumidor)$/, 'cdc.md'],
      [/^(CC|C[óo]digo Civil)$/, 'cc.md'],
      [/9[.]099/, 'lei-9099.md'],
      [/10[.]741/, 'lei-10741.md'],
      [/14[.]905/, 'lei-14905.md'],
      [/LGPD|13[.]709/, 'lgpd.md'],
    ],
    // Transcrição literal (modelos e peças geradas): o trecho entre aspas ou em bloco "> " tem de existir no arquivo
    // da norma ou do precedente citado ao lado. Linha com VERIFICAR/CONFERIR rebaixa para aviso.
    transcricoes: {
      arquivo: /[\\/]assets[\\/]modelo-[^\\/]*[.]md$|[\\/]testes[\\/].*[\\/]saida[\\/](inicial|replica|recurso)[^\\/]*[.]md$/,
      minLetras: 20,
      naoFonte: /^(INDEX|datas-citaveis)\.md$/,
      gatilho: /\barts?[.]|S[úu]mula|\b(?:EAREsp|AREsp|EREsp|REsp|AC)\s+\d|ementa/i,
      atribuiDepois: /^\s*\((?:[^)]*,\s*)?(?:arts?[.]|S[úu]mula|par[áa]grafo|§)/i,
      atribuiAntes: /(?:disp[õo]e|prev[êe]|estabelece|determina|enuncia|diz|fixou|firmou|decidiu|segundo o qual|nos termos d[oa]|assim redigid[oa])[^"]{0,60}$/i,
      normas: [
        [/\bCPC\b|C[óo]digo de Processo Civil/, 'cpc.md'],
        [/\bCDC\b|C[óo]digo de Defesa do Consumidor/, 'cdc.md'],
        [/\bCC\b|C[óo]digo Civil/, 'cc.md'],
        [/Constitui[çc][ãa]o|\bCF\b/, 'cf88.md'],
        [/9[.]099/, 'lei-9099.md'],
        [/10[.]741|Estatuto da Pessoa Idosa/, 'lei-10741.md'],
        [/10[.]820/, 'lei-10820.md'],
        [/14[.]690/, 'lei-14690.md'],
        [/14[.]905/, 'lei-14905.md'],
        [/LGPD|13[.]709/, 'lgpd.md'],
        [/\bIN\b[^.;]{0,25}\b138\b|Instru[çc][ãa]o Normativa[^.;]{0,40}\b138\b/, 'in-inss-138-2022-consolidada.md'],
        [/\bIN\b[^.;]{0,25}\b143\b|Instru[çc][ãa]o Normativa[^.;]{0,40}\b143\b/, 'in-inss-143-2023.md'],
        [/\bIN\b[^.;]{0,25}\b28\b|Instru[çc][ãa]o Normativa[^.;]{0,40}\b28\b/, 'in-inss-28-2008-consolidada-2020.md'],
        [/4[.]549/, 'res-cmn-4549-consolidada.md'],
        [/3[.]954/, 'res-cmn-3954-original.md'],
        [/4[.]935/, 'res-cmn-4935.md'],
        [/2[.]836/, 'res-cmn-2836-consolidada.md'],
      ],
      sumulas: [[/S[úu]mulas?[^.;]{0,20}(?:\/|d[oa] )STJ/, 'STJ'], [/S[úu]mulas?[^.;]{0,40}(?:TJBA|Turma de Uniformiza)/, 'TJBA'], [/S[úu]mulas?[^.;]{0,20}(?:\/|d[oa] )STF/, 'STF']],
      precedente: /\b(EAREsp|AREsp|EREsp|REsp|AC|Apela[çc][ãa]o C[íi]vel)\s+(?:n[ºo.]?\s*)?([\d][\d.\-]{6,})/g,
    },
    // Mapa de argumentos (scripts/fichas.py na réplica; montado pela skill no recurso): todo ponto tem resposta e pedido,
    // e cada pedido do mapa aparece em "Dos pedidos" da peça que estiver na mesma pasta.
    mapa: { arquivo: 'mapa-argumentos.json', peca: /^(replica|recurso)[^\\/]*[.]md$/ },
    // Em qual arquivo de references/jurisprudencia procurar a súmula de cada tribunal.
    arquivosJur: { STJ: /stj/i, TJBA: /tjba/i, STF: /stf/i, FONAJE: /fonaje/i },
    // Peças geradas em testes/**/saida/: conferência dos números com o calculo.json que está ao lado.
    pecas: {
      arquivo: /[\\/]testes[\\/].*[\\/]saida[\\/]inicial[^\\/]*[.]md$/,
      calculo: 'calculo.json',
      proibe: [
        { re: /\[\[(?:SE|SENÃO|FIM)/, msg: 'marcador de condicional [[SE…]] sobrando' },
        { re: /�/, msg: 'caractere de substituição (problema de codificação)' },
        { re: /R\$ ?0,00 \(zero reais\)|R\$0,00/, msg: 'valor de modelo (R$ 0,00) não substituído' },
        { re: /\[(?:CONTRATO|NOME DO AUTOR|RÉU|CPF|RG|ENDEREÇO|CEP|CIDADE|NB|QTDE|VALOR[^\]]*|TOTAL[^\]]*)\]/, msg: 'campo de modelo não preenchido' },
        ...PROIBIDOS,
        { ...JUROS_RMC, arquivo: /inicial-rmc[^\\/]*[.]md$/ },
      ],
      exige: [
        { re: /pede deferimento/, msg: 'sem o fecho padrão' },
        ...DANO_MORAL,
        { re: /Dos precedentes judiciais evocados/i, msg: 'sem o tópico de precedentes' },
      ],
    },
  },

  // Registro FSC/VF ao lado de cada peça gerada (escrutinio.py grava; ver assets/escrutinio-fsc-vf.md).
  // A chave `checagem` é lida por verificar-pacote.js junto com extras.pecas.
  // Arquivos congelados (mapa e geolocalização do recurso): o hash tem de bater com testes/mapa/congelados.json.
  congelados: 'testes/mapa/congelados.json',

  // Decisões antigas que não podem voltar às referências da skill de recurso (references/*.md).
  proibeEmReferencias: {
    arquivo: /[\\/]recurso-[^\\/]+[\\/]references[\\/](?!02-mudancas)[^\\/]+[.]md$/,  // o registro de mudanças cita o texto antigo de propósito
    regras: [
      { re: /Citar SEM pedido de verificação, com esta nota de rodapé, exatamente:\s*\n?\s*"BRASIL[^"]*Tema Repetitivo 929/, msg: 'Tema 929/STJ como fundamento citável (decisão D7: não citar)' },
      { re: /Contrato a partir de 11\/11\/2022: IN 138|vigente desde a publicação \(art\. 40\)/, msg: 'IN 138 com vigência em 11/11/2022 (decisão D30: 13/12/2022)' },
      { re: /4[.]753\/2019, art[.] 2º → verifica/, msg: 'Res. CMN 4.753/2019 como base de KYC (decisão D2/D11)' },
    ],
  },

  // Hábitos e erros já eliminados (aviso).
  residuos: [
    [/\bdossiê\b/i, 'termo "dossiê" (usar "quadro de fatos")'],
    [/6 a 8 perguntas|TODAS estas perguntas|Não pule fases/, 'regra antiga de muitas perguntas ou fases obrigatórias'],
  ],
};
