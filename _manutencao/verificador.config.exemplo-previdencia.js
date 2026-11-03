// Configuração do verificador para o pacote Cortex (direito previdenciário). Serve de EXEMPLO:
// copie para verificador.config.js no novo projeto e troque as regras pelas do novo setor.
'use strict';
module.exports = {
  // Arquivos que devem ser idênticos em todas as skills que os têm. A skill "fonte" é a referência.
  copias: [
    { arquivo: 'protocolo/protocolo.md', fonte: 'prev' },
    { arquivo: 'protocolo/quadro-de-fatos.md', fonte: 'prev' },
    { arquivo: 'assets/padrao-pecas.md', fonte: 'estagiario-peticoes' },
  ],
  // Arquivos de references/normas que são de cada skill (não entram na comparação de cópias).
  proprioPorSkill: /^(INDEX|MAPA|ESTRUTURA)\.md$/,
  // Skills que não têm protocolo/protocolo.md (por exemplo, a de formatação).
  semProtocolo: ['timbrado-sca'],
  descricaoMax: 1024,

  nomes: {
    // Nomes de skill que já foram trocados: citá-los é erro.
    antigos: /(^|[^a-z])segurado-especial-rural|cortex-maternidade/,
    // Comandos que não existem na descrição (aviso).
    comandosInexistentes: /(^|[ (])\/(cnis|decisor|peticionar|recurso|especial|bpc|rural|incapacidade|pcd|raio-x|raiox|atendimentopcd|ifbra)\b/,
    // Se um desses nomes aparecer entre crases, a skill precisa existir.
    devemExistir: /^(raio-x-cnis|calculos-previdenciarios|decisor-aposentadoria|aposentadoria-pcd|aposentadoria-especial|beneficios-incapacidade|bpc-loas|auxilio-acidente|pensao-por-morte|salario-maternidade|recurso-inss|estagiario-peticoes|timbrado-sca)$/,
  },

  modelos: {
    // Modelos em assets/modelo-*.md que NÃO são peça (não passam pelas regras abaixo).
    naoPeca: /quesitos|roteiro|autodeclaracao|declaracao-testemunhal|dossie|parecer|checklist|INDEX|padrao-pecas/,
    // Modelos de peça judicial (exigem o tópico de precedentes).
    judicial: /peticao-inicial|recurso-inominado|replica|contrarrazoes|embargos/,
    exigeEmTodos: [
      { re: /pede deferimento/, msg: 'sem fecho "Termos em que, pede deferimento."' },
    ],
    proibeEmTodos: [
      { re: /Nestes termos|\[Local\], \[data\]|\{\{Local\}\}/, msg: 'fecho antigo' },
      { re: /xcelent[ií]ssim|Exmo\.|Meritíssimo|V\. ?Exa|ILUSTRÍSSIMO/i, msg: 'endereçamento ou tratamento antigo' },
    ],
    remeteAoPadrao: 'padrao-pecas.md',
    remeteAoPadraoExcecao: /^# Mandado/,
    exigeNasJudiciais: [
      { re: /Precedentes Judiciais Evocados/i, msg: 'peça judicial sem o tópico de precedentes' },
    ],
    regrasPorArquivo: [
      { arquivo: /peticao-inicial/, proibe: /condena[çc][ãa]o (do r[ée]u|do INSS) (nos [ôo]nus|em honor)/i, msg: 'pede honorários/sucumbência no 1º grau do JEF' },
    ],
    avisosCondicionais: [
      { se: /EC 113/, exige: /EC 136/, msg: 'cita EC 113/2021 sem a nota da EC 136/2025' },
    ],
  },

  // Confere súmulas e temas citados contra o texto transcrito em references/jurisprudencia (seções "## Súmula N", "## Tema N").
  citacoes: { ativo: true, tribunais: 'TNU|STJ|STF' },

  // Hábitos e erros já eliminados que não devem voltar (aviso).
  residuos: [
    [/pelo o método|o o método/, 'texto "pelo o método"'],
    [/R\$ 1\.518|379,50/, 'salário mínimo de 2025 como se fosse 2026'],
    [/6 a 8 perguntas|TODAS estas perguntas|Não pule fases/, 'regra antiga de muitas perguntas ou fases obrigatórias'],
    [/\bdossiê\b/i, 'termo "dossiê" (usar "quadro de fatos")'],
  ],
};
