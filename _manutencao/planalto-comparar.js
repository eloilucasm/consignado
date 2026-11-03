// Compara uma norma do pacote com o texto oficial já convertido (planalto-converter.js): lista linhas oficiais ausentes no pacote.
// Uso: node audita-planalto.js oficial.md pacote.md [nome]
const fs = require('fs');
const [, , oficial, pacote, nome = ''] = process.argv;
// Compara sem espaços: o Planalto cola ou separa o número do parágrafo do texto ("§ 2ºQuando" x "§ 2º Quando").
const norm = s => s.replace(/~~/g, '').replace(/[º°]/g, 'o').replace(/[–—−]/g, '-').replace(/[ \s]+/g, '').toLowerCase();
const P = norm(fs.readFileSync(pacote, 'utf8'));
const linhas = fs.readFileSync(oficial, 'utf8').split('\n').slice(5).map(l => l.trim()).filter(Boolean);
const faltam = [];
let art = '';
for (const l of linhas) {
  const m = l.replace(/~~/g, '').match(/^Art\. ?(\d[\d.]*)/); if (m) art = m[1];
  const n = norm(l);
  if (n.length < 30) continue;
  if (!P.includes(n.slice(0, 55))) faltam.push({ art, texto: l.slice(0, 170) });
}
console.log(`${nome}: ${linhas.length} linhas oficiais | ausentes no pacote: ${faltam.length}`);
const porArt = faltam.reduce((a, f) => (a[f.art] = (a[f.art] || 0) + 1, a), {});
console.log('  por artigo:', Object.entries(porArt).slice(0, 25).map(([k, v]) => `art. ${k || '?'}: ${v}`).join(' | '));
faltam.slice(0, 8).forEach(f => console.log('   -', `[art. ${f.art || '?'}]`, f.texto));
fs.writeFileSync(`audit-${nome || 'norma'}.json`, JSON.stringify(faltam, null, 1));
