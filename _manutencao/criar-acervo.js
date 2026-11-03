#!/usr/bin/env node
// Cria o acervo central (_acervo/ + manifesto.json) a partir dos arquivos que já se repetem entre as skills.
// Use UMA vez, quando a duplicação começar a doer. Depois disso, edite o acervo e use sincronizar-acervo.js.
//
//   node _manutencao/criar-acervo.js                    RELATÓRIO: o que entraria no acervo (não grava nada)
//   node _manutencao/criar-acervo.js --aplicar          grava _acervo/ e o manifesto (não altera nenhuma skill)
//   node _manutencao/criar-acervo.js --raiz <pasta>     pasta do pacote (padrão: acima de _manutencao)
//   node _manutencao/criar-acervo.js --prefere-maior    quando há versões diferentes, usa a maior (padrão: a mais comum)
//
// Quando um arquivo existe em versões diferentes, o relatório lista as skills de cada versão. Resolva antes de
// aplicar (ou use --prefere-maior se uma versão for superconjunto da outra) e depois rode
// sincronizar-acervo.js --aplicar para igualar as skills.
'use strict';
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const args = process.argv.slice(2);
const arg = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null; };
const RAIZ = path.resolve(arg('--raiz') || path.join(__dirname, '..'));
const APLICAR = args.includes('--aplicar'), MAIOR = args.includes('--prefere-maior');

// Categorias: pasta no acervo -> pasta dentro de cada skill. "arquivos" limita a nomes exatos; "ignora" exclui por regex.
// Ajuste ao seu projeto (este é o layout do pacote Cortex).
const CATEGORIAS = [
  { acervo: 'protocolo', skill: 'protocolo', arquivos: ['protocolo.md', 'quadro-de-fatos.md'] },
  { acervo: 'pecas', skill: 'assets', arquivos: ['padrao-pecas.md'] },
  { acervo: 'normas', skill: 'references/normas', ignora: /^(INDEX|MAPA|ESTRUTURA)\.md$/ },
  { acervo: 'jurisprudencia', skill: 'references/jurisprudencia', ignora: /^(INDEX|MAPA|ESTRUTURA)\.md$/ },
];

const hash = f => crypto.createHash('md5').update(fs.readFileSync(f)).digest('hex');
const skills = fs.readdirSync(RAIZ, { withFileTypes: true }).filter(d => d.isDirectory() && fs.existsSync(path.join(RAIZ, d.name, 'SKILL.md'))).map(d => d.name).sort();
const mapa = new Map(); // chave do acervo -> Map(hash -> [{skill, arquivo}])
for (const s of skills) for (const c of CATEGORIAS) {
  const D = path.join(RAIZ, s, c.skill); if (!fs.existsSync(D)) continue;
  for (const e of fs.readdirSync(D, { withFileTypes: true })) {
    if (!e.isFile() || !e.name.endsWith('.md')) continue;
    if (c.arquivos && !c.arquivos.includes(e.name)) continue;
    if (c.ignora && c.ignora.test(e.name)) continue;
    const chave = c.acervo + '/' + e.name, p = path.join(D, e.name), h = hash(p);
    if (!mapa.has(chave)) mapa.set(chave, new Map());
    const m = mapa.get(chave); if (!m.has(h)) m.set(h, []); m.get(h).push({ skill: s, arquivo: p });
  }
}

let copias = 0, divergentes = 0, unicos = 0, bytes = 0; const linhas = [];
for (const [chave, m] of [...mapa].sort()) {
  const n = [...m.values()].reduce((a, v) => a + v.length, 0); copias += n; if (n === 1) unicos++;
  if (m.size > 1) { divergentes++; linhas.push('DIVERGE  ' + chave + ' -> ' + [...m.values()].map(v => v.length > 2 ? v.length + ' skills (' + v[0].skill + '…)' : v.map(x => x.skill).join('+')).join(' | ')); }
}
console.log('skills ' + skills.length + ' | arquivos distintos ' + mapa.size + ' | cópias ' + copias + ' | só em uma skill ' + unicos + ' | com mais de uma versão ' + divergentes);
linhas.forEach(l => console.log('  ' + l));

if (!APLICAR) { console.log('\nRELATÓRIO. Nada foi gravado. Use --aplicar para criar _acervo/.'); process.exit(divergentes ? 1 : 0); }

const A = path.join(RAIZ, '_acervo');
if (fs.existsSync(path.join(A, 'manifesto.json'))) { console.error('\n_acervo/manifesto.json já existe. Não sobrescrevo. Apague-o de propósito se for recriar.'); process.exit(2); }
const man = { versao: new Date().toISOString().slice(0, 10), descricao: 'Acervo central. Cada skill recebe cópia dos arquivos listados. Edite aqui e rode sincronizar-acervo.js --aplicar.', pastas: {}, arquivos: {} };
for (const c of CATEGORIAS) man.pastas[c.acervo] = c.skill;
for (const [chave, m] of mapa) {
  const versoes = [...m.values()];
  const escolhida = MAIOR ? versoes.sort((a, b) => fs.statSync(b[0].arquivo).size - fs.statSync(a[0].arquivo).size)[0][0] : versoes.sort((a, b) => b.length - a.length)[0][0];
  const dest = path.join(A, chave); fs.mkdirSync(path.dirname(dest), { recursive: true }); fs.copyFileSync(escolhida.arquivo, dest); bytes += fs.statSync(dest).size;
  man.arquivos[chave] = versoes.flatMap(v => v.map(x => x.skill)).sort();
}
const ord = {}; Object.keys(man.arquivos).sort().forEach(k => ord[k] = man.arquivos[k]); man.arquivos = ord;
fs.writeFileSync(path.join(A, 'manifesto.json'), JSON.stringify(man, null, 1) + String.fromCharCode(10));
console.log('\nAPLICADO: _acervo/ criado com ' + mapa.size + ' arquivos (' + (bytes / 1048576).toFixed(1) + ' MB). As skills não foram alteradas.' + (divergentes ? ' Rode sincronizar-acervo.js para ver quais skills passam a diferir do acervo.' : ''));
