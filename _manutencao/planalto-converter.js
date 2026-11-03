// ATENÇÃO (30/10/2026): este conversor só reconhece o riscado das tags <strike>, <s> e <del>. O Planalto também risca com
// style="text-decoration:line-through", que aqui é ignorado: texto revogado sai como vigente (LGPD, CPC, Estatuto da Pessoa
// Idosa e Lei 14.690 foram regravados por isso). Para norma nova use _manutencao/coleta/coletar_planalto.py, que trata os
// dois casos e confere o resultado palavra a palavra contra o HTML. Este arquivo fica só como referência.
//
// Converte página do Planalto (HTML windows-1252) em Markdown no formato das normas do pacote.
// Uso: node planalto.js arquivo.htm "Título" "URL" "data" [artigos: "1-30" | "inteiro" | vazio] > saida.md
const fs = require('fs');
const [, , arq, titulo, url, data, recorte] = process.argv;
// Tabela windows-1252 para 0x80-0x9F (o decodificador do Node trata esses bytes como Latin-1).
const W = '€\u0081‚ƒ„…†‡ˆ‰Š‹Œ\u008dŽ\u008f\u0090‘’“”•–—˜™š›œ\u009džŸ';
const fixW = s => s.replace(/[\u0080-\u009f]/g, c => W[c.charCodeAt(0) - 0x80]);
let h = fixW(new TextDecoder('latin1').decode(fs.readFileSync(arq))).replace(/\r?\n/g, ' ');
h = h.replace(/<script[\s\S]*?<\/script>/gi, ' ').replace(/<style[\s\S]*?<\/style>/gi, ' ');
h = h.replace(/<(strike|s|del)\b[^>]*>/gi, '\u0001').replace(/<\/(strike|s|del)>/gi, '\u0002');
h = h.replace(/<br\s*\/?>/gi, ' ').replace(/<\/(p|h\d|div|tr|li)>/gi, '\n').replace(/<[^>]+>/g, '');
const marcas = { acute: '́', grave: '̀', circ: '̂', tilde: '̃', uml: '̈', cedil: '̧' };
const ent = { nbsp: ' ', amp: '&', lt: '<', gt: '>', quot: '"', ordm: 'º', ordf: 'ª', sect: '§', ndash: '–', mdash: '—', ldquo: '“', rdquo: '”', lsquo: '‘', rsquo: '’', deg: '°', middot: '·', hellip: '…', laquo: '«', raquo: '»' };
h = h.replace(/&([a-zA-Z])(acute|grave|circ|tilde|uml|cedil);/g, (m, b, k) => (b + marcas[k]).normalize('NFC'));
h = h.replace(/&(#\d+|[a-z]+);/gi, (m, e) => {
  if (e[0] !== '#') return ent[e] ?? m;
  const n = +e.slice(1);
  return n >= 128 && n <= 159 ? W[n - 0x80] : String.fromCharCode(n); // &#150; = travessão etc.
});
let linhas = h.split('\n').map(l => l.replace(/\s+/g, ' ').trim()).filter(Boolean)
  .map(l => l.replace(/\u0001\s*/g, '~~').replace(/\s*\u0002/g, '~~').replace(/~~~~/g, '').replace(/~~\s*~~/g, ' '))
  .filter(l => !/function\s*\(\s*\)\s*\{|f5_cspm|setCharAt/.test(l));
if (recorte && recorte !== 'inteiro') {
  const want = new Set(); for (const p of recorte.split(',')) { const [a, b] = p.split('-').map(Number); for (let i = a; i <= (b || a); i++) want.add(i); }
  let cur = null; const out = [];
  for (const l of linhas) { const m = l.replace(/~~/g, '').match(/^Art\. ?(\d{1,3}(?:\.\d{3})*)/); if (m) cur = +m[1].replace(/\./g, ''); if (cur !== null && want.has(cur)) out.push(l); }
  linhas = out;
} else if (recorte !== 'inteiro') {
  const i = linhas.findIndex(l => /^Art\. ?1[ºo°]/.test(l.replace(/~~/g, ''))); if (i > 0) linhas = linhas.slice(i);
  const f = linhas.findIndex(l => /^Brasília, \d/.test(l)); if (f > 0) linhas = linhas.slice(0, f);
}
const notas = [...linhas.join(' ').matchAll(/(?:Redação dada|Incluíd[oa]) pel[ao] (?:Lei|Emenda Constitucional|Lei Complementar|Decreto)(?: n[ºo°])? ?([\d.]+)/g)].map(m => m[1]);
const ultima = notas.sort((a, b) => +b.replace(/\./g, '') - +a.replace(/\./g, ''))[0] || '—';
console.log(`# ${titulo}\n\n> Fonte: <${url}>\n> Consulta: ${data} · recorte: ${recorte && recorte !== 'inteiro' ? 'artigos ' + recorte : 'texto integral'} · alteração mais recente pelas notas do texto: ${ultima}\n> Transcrição literal do texto consolidado. Trechos ~~riscados~~ estão revogados ou superados: não os cite como vigentes, mas eles podem reger fatos da sua época (ver "Texto vigente e texto revogado" no protocolo). Conferir a redação vigente ao fato gerador e eventual alteração posterior à data da consulta.\n`);
console.log(linhas.join('\n\n'));
