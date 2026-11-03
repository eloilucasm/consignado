#!/usr/bin/env node
// Prova de integridade de um texto de norma convertido. Dois testes, sempre os dois:
//
//  1) página oficial (HTML) -> arquivo convertido: todo parágrafo da página existe no convertido?
//     node _manutencao/comparar-fonte.js --html pagina.htm --md convertido.md [--nome CPC]
//     Detecta o defeito clássico da conversão: parágrafos que vêm logo depois de quadros somem em silêncio.
//     (HTML do Planalto vem em windows-1252; o script já trata o travessão e as entidades.)
//
//  2) recorte antigo -> texto integral novo: toda linha do recorte antigo existe no integral?
//     node _manutencao/comparar-fonte.js --recorte antigo.md --integral novo.md [--nome CPC]
//
// A comparação ignora espaços, marcas de revogação (~~), pipes e maiúsculas, e confere o prefixo de 50 caracteres.
// A maior parte dos "ausentes" costuma ser diferença de espaçamento ou de travessão: confira o texto antes de concluir que falta algo.
'use strict';
const fs = require('fs');
const args = process.argv.slice(2);
const arg = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null; };
const nome = arg('--nome') || '';
// Segunda passada, só com letras (soLetras): pega o falso ausente de linha quebrada no HTML e de traço fora da lista de norm.
// Só conta como ausente o que falha nas duas passadas.
const { norm, soLetras } = require('./normalizar');
const PREFIXO = 50;
const PREFIXO_LETRAS = 40;

function relatorio(titulo, total, falta) {
  console.log(`${nome.padEnd(12)} ${titulo}: ${String(total).padStart(6)} | ausentes: ${falta.length}`);
  falta.slice(0, 8).forEach(l => console.log('    - ' + l.slice(0, 150)));
  if (falta.length > 8) console.log('    … e mais ' + (falta.length - 8));
  process.exitCode = falta.length ? 1 : 0;
}

if (arg('--html') && arg('--md')) {
  const W = '€\u0081‚ƒ„…†‡ˆ‰Š‹Œ\u008dŽ\u008f\u0090‘’“”•–—˜™š›œ\u009džŸ'; // windows-1252, 0x80-0x9F
  let t = fs.readFileSync(arg('--html')).toString('latin1').replace(/[\u0080-\u009f]/g, c => W[c.charCodeAt(0) - 128]);
  const marca = { acute: '́', grave: '̀', circ: '̂', tilde: '̃', uml: '̈' };
  t = t.replace(/&([aeiouAEIOU])(acute|grave|circ|tilde|uml);/g, (m, b, k) => (b + marca[k]).normalize('NFC'))
       .replace(/&([cC])cedil;/g, (m, c) => c === 'c' ? 'ç' : 'Ç').replace(/&([nN])tilde;/g, (m, c) => c === 'n' ? 'ñ' : 'Ñ');
  const dec = s => s.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&#(\d+);/g, (m, n) => String.fromCharCode(+n));
  const sem = t.replace(/<script[\s\S]*?<\/script>/gi, ' ').replace(/<style[\s\S]*?<\/style>/gi, ' ').replace(/<\/(p|div|tr|li|h\d|table|center)>/gi, '\n').replace(/<br\s*\/?>/gi, '\n').replace(/<[^>]+>/g, ' ');
  const paras = dec(sem).split('\n').map(l => l.replace(/\s+/g, ' ').trim()).filter(l => l.length >= 45);
  const md = fs.readFileSync(arg('--md'), 'utf8');
  const M = norm(md), ML = soLetras(md);
  relatorio('parágrafos da página', paras.length, paras.filter(l => !M.includes(norm(l).slice(0, PREFIXO)) && !ML.includes(soLetras(l).slice(0, PREFIXO_LETRAS))));
} else if (arg('--recorte') && arg('--integral')) {
  const I = norm(fs.readFileSync(arg('--integral'), 'utf8'));
  const linhas = fs.readFileSync(arg('--recorte'), 'utf8').split('\n').map(l => l.trim()).filter(l => l.length > 40 && !l.startsWith('>') && !l.startsWith('#'));
  relatorio('linhas do recorte', linhas.length, linhas.filter(l => !I.includes(norm(l).slice(0, 55))));
} else {
  console.error('Uso:\n  --html pagina.htm --md convertido.md [--nome X]\n  --recorte antigo.md --integral novo.md [--nome X]');
  process.exit(2);
}
