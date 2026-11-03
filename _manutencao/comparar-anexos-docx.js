#!/usr/bin/env node
// Compara anexos em .docx (formulários e tabelas que o órgão publica em Word) com o arquivo .md do pacote.
// Lê o texto de cada parágrafo do .docx e testa se o início dele existe no .md.
//
//   node _manutencao/comparar-anexos-docx.js <pasta-com-docx> <anexos.md>
//
// Precisa de "unzip" (Git Bash/Linux/Mac) ou de "tar" com suporte a zip (Windows 10+) no PATH.
// Os anexos costumam ter vários arquivos .docx: baixe todos para uma pasta (o Portal IN do INSS guarda-os em
// assets/anexos/in/*.docx) e rode uma vez. Resultado esperado: 0 ausentes.
'use strict';
const fs = require('fs'), path = require('path'), cp = require('child_process');
const [, , pasta, md] = process.argv;
if (!pasta || !md) { console.error('Uso: comparar-anexos-docx.js <pasta-com-docx> <anexos.md>'); process.exit(2); }
const norm = s => s.replace(/~~/g, '').replace(/[|*_`]/g, '').replace(/[º°]/g, 'o').replace(/[–—−]/g, '-').replace(/[\s ]+/g, '').toLowerCase();
const P = norm(fs.readFileSync(md, 'utf8'));
const dec = s => s.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&apos;/g, "'").replace(/&#(\d+);/g, (m, n) => String.fromCharCode(+n));
function xmlDoDocx(f) {
  for (const cmd of [['unzip', ['-p', f, 'word/document.xml']], ['tar', ['-xOf', f, 'word/document.xml']]]) {
    try { return cp.execFileSync(cmd[0], cmd[1], { maxBuffer: 1 << 28, stdio: ['ignore', 'pipe', 'ignore'] }).toString('utf8'); } catch (e) { /* tenta o próximo */ }
  }
  return null;
}
let total = 0, falta = 0; const linhas = [];
for (const f of fs.readdirSync(pasta).filter(x => x.toLowerCase().endsWith('.docx')).sort()) {
  const xml = xmlDoDocx(path.join(pasta, f));
  if (!xml) { linhas.push(f.padEnd(24) + ' ERRO ao abrir (instale unzip ou use tar com suporte a zip)'); continue; }
  const paragrafos = [...xml.matchAll(/<w:p[ >][\s\S]*?<\/w:p>/g)].map(m => dec([...m[0].matchAll(/<w:t(?: [^>]*)?>([^<]*)<\/w:t>/g)].map(x => x[1]).join('')).trim()).filter(s => s.length >= 8);
  const ausentes = paragrafos.filter(p => { const n = norm(p); return !P.includes(n.length > 60 ? n.slice(0, 55) : n); });
  total += paragrafos.length; falta += ausentes.length;
  linhas.push(f.padEnd(24) + ' parágrafos ' + String(paragrafos.length).padStart(4) + ' | ausentes ' + String(ausentes.length).padStart(3));
  ausentes.slice(0, 3).forEach(s => linhas.push('     ex.: ' + s.slice(0, 110)));
}
linhas.forEach(l => console.log(l));
console.log('\nTOTAL: ' + total + ' parágrafos oficiais | ausentes no pacote: ' + falta);
process.exitCode = falta ? 1 : 0;
