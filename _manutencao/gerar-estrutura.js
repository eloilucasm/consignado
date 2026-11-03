#!/usr/bin/env node
// Gera references/normas/ESTRUTURA.md em cada skill: sumário de cada norma (Parte/Livro/Título/Capítulo)
// com intervalo de linhas e de artigos, para ler só a janela necessária (Read offset/limit) em vez da norma inteira.
// Não altera nenhum texto de norma. Uso: node _manutencao/gerar-estrutura.js [--skill nome]
const fs = require('fs'), path = require('path');
const RAIZ = path.resolve(__dirname, '..');
const i = process.argv.indexOf('--skill'); const so = i >= 0 ? process.argv[i + 1] : null;
const PROPRIO = /^(INDEX|MAPA|ESTRUTURA)\.md$/;
const CAB = /^(?:~~)?(PARTE|LIVRO|TÍTULO|CAPÍTULO)\b(.*)$/i;
const ART = /^(?:~~)?Art\. ?(\d+(?:\.\d+)*)\s*([ºo°])?(?:-([A-Z]))?/;
const nivel = r => ({ PARTE: 0, LIVRO: 1, TÍTULO: 2, CAPÍTULO: 3 })[r.toUpperCase()];

function mapear(arq) {
  const L = fs.readFileSync(arq, 'utf8').split(/\r?\n/);
  const titulo = (L[0] || '').replace(/^#\s*/, '');
  const arts = []; // [linha, rotulo]
  const cabs = []; // {lin, nivel, rotulo}
  L.forEach((t, k) => {
    const a = ART.exec(t); if (a) arts.push([k + 1, 'Art. ' + a[1] + (a[2] ? 'º' : '') + (a[3] ? '-' + a[3] : '')]);
    const c = CAB.exec(t.trim()); if (!c || t.length > 160) return;
    let nome = (c[1].toUpperCase() + c[2]).trim().replace(/^[–—-]\s*/, '');
    const resto = c[2].trim();
    if (!resto || /^[IVXLCDM]+(-[A-Z])?$/i.test(resto) || /^ÚNICO$/i.test(resto) || /^GERAL$/i.test(resto) || /^ESPECIAL$/i.test(resto)) { // título na linha seguinte
      let j = k + 1; while (j < L.length && !L[j].trim()) j++;
      const prox = L[j] && L[j].trim();
      if (prox && prox.length <= 160 && !ART.test(prox) && !CAB.test(prox)) nome += ' — ' + prox.replace(/~~/g, '');
    }
    cabs.push({ lin: k + 1, niv: nivel(c[1]), nome: nome.replace(/~~/g, '') });
  });
  const total = L.length;
  const linhas = cabs.map((c, n) => {
    const fim = (cabs[n + 1] ? cabs[n + 1].lin : total + 1) - 1;
    const dentro = arts.filter(([l]) => l >= c.lin && l <= fim);
    const faixa = dentro.length ? (dentro[0][1] === dentro.at(-1)[1] ? dentro[0][1] : dentro[0][1] + ' a ' + dentro.at(-1)[1]) : 's/ artigos';
    return { ...c, fim, faixa };
  });
  return { titulo, total, linhas, temArts: arts.length };
}

const cab = `# Estrutura das normas (sumário com linhas)

Gerado por \`node _manutencao/gerar-estrutura.js\` (não edite à mão). Os números são **linhas do arquivo**.

**Regra:** nunca leia uma norma inteira. Ache o dispositivo aqui, depois leia só a janela (Read com offset/limit) ou use \`grep -n "^Art. 73"\`. Nas normas sem divisão (portarias curtas), \`grep -n\` direto. Conferir a redação vigente ao fato gerador continua valendo.
`;

let n = 0;
for (const skill of fs.readdirSync(RAIZ).filter(s => fs.existsSync(path.join(RAIZ, s, 'SKILL.md')))) {
  if (so && skill !== so) continue;
  const D = path.join(RAIZ, skill, 'references', 'normas'); if (!fs.existsSync(D)) continue;
  const arqs = fs.readdirSync(D).filter(f => f.endsWith('.md') && !PROPRIO.test(f)).sort();
  if (!arqs.length) continue;
  let out = cab;
  for (const f of arqs) {
    const m = mapear(path.join(D, f));
    out += `\n## ${m.titulo}\n\`${f}\` · ${m.total} linhas\n\n`;
    if (!m.linhas.length) { out += m.total > 150 && m.temArts ? '_Sem divisão em títulos/capítulos no texto: use `grep -n "^Art. N"`._\n' : '_Norma curta: leia inteira ou use `grep -n`._\n'; continue; }
    for (const c of m.linhas) out += `${'  '.repeat(Math.max(0, c.niv - (m.linhas[0].niv)))}- L${c.lin}–${c.fim} · ${c.nome} (${c.faixa})\n`;
  }
  fs.writeFileSync(path.join(D, 'ESTRUTURA.md'), out); n++;
}
console.log(`ESTRUTURA.md gerado em ${n} skill(s).`);
