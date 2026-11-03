#!/usr/bin/env node
// Mostra o texto visível de uma página HTML salva (sem menu, script e estilo) e filtra por expressão regular.
// Serve para ler páginas de tribunais e de órgãos sem abrir o navegador: salve a página com curl e rode aqui.
//
//   node _manutencao/extrair-texto-html.js pagina.html                   texto todo (primeiras 120 linhas)
//   node _manutencao/extrair-texto-html.js pagina.html "Tese|Situação"   só as linhas que casam
//   node _manutencao/extrair-texto-html.js pagina.html "Tema" --depois 30   a primeira linha que casa e as 30 seguintes
//
// Páginas do STF carregam as abas por AJAX: o texto das decisões e dos andamentos está em
//   https://portal.stf.jus.br/processos/abaDecisoes.asp?incidente=N&imprimir=1  (e abaAndamentos.asp, abaInformacoes.asp)
// Salve essas URLs com um Referer da página do processo. Um HTML de 10 KB que diz "Default error page" é o firewall do site, não a página.
'use strict';
const fs = require('fs');
const [, , arquivo, filtro] = process.argv;
const args = process.argv.slice(2);
const depois = args.includes('--depois') ? +args[args.indexOf('--depois') + 1] : null;
if (!arquivo) { console.error('Uso: extrair-texto-html.js pagina.html ["regex"] [--depois N]'); process.exit(2); }
const h = fs.readFileSync(arquivo, 'utf8');
const t = h.replace(/<script[\s\S]*?<\/script>/gi, ' ').replace(/<style[\s\S]*?<\/style>/gi, ' ')
  .replace(/<\/(p|div|tr|li|h\d|table)>/gi, '\n').replace(/<br\s*\/?>/gi, '\n').replace(/<[^>]+>/g, ' ')
  .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&#39;/g, "'").replace(/&quot;/g, '"');
const L = t.split('\n').map(l => l.replace(/\s+/g, ' ').trim()).filter(Boolean);
if (/error page|Access Denied|Just a moment/i.test(L.slice(0, 15).join(' ')) && h.length < 20000) console.error('AVISO: parece página de bloqueio (firewall), não o conteúdo.');
if (!filtro || filtro.startsWith('--')) { console.log(L.slice(0, 120).join('\n')); }
else {
  const re = new RegExp(filtro, 'i');
  if (depois !== null) { const i = L.findIndex(l => re.test(l)); console.log(i < 0 ? 'não achou' : L.slice(i, i + depois + 1).join('\n')); }
  else L.forEach((l, i) => { if (re.test(l)) console.log(i + ': ' + l.slice(0, 300)); });
}
