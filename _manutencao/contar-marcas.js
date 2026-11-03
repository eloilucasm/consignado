#!/usr/bin/env node
// Conta as marcas de pendência (por padrão [CONFERIR]) em todo o pacote, por categoria, para triagem.
// Troca a estimativa ("a maioria é campo do caso") por um número conferido.
//
//   node _manutencao/contar-marcas.js                     resumo por categoria
//   node _manutencao/contar-marcas.js --listar especificas   lista as pendências específicas ([CONFERIR: ...])
//   node _manutencao/contar-marcas.js --listar outros        lista o que não caiu em nenhuma categoria
//   node _manutencao/contar-marcas.js --marca "\[PREENCHER"  conta outra marca (regex)
//   node _manutencao/contar-marcas.js --raiz <pasta>
//
// Categorias (heurística, revise a lista de "especificas" e "outros" à mão):
//   campo de modelo/painel  -> ocorrência em assets/ (campo que o Claude preenche com o caso)
//   instrução de uso        -> frase que ensina a usar a marca ("marque", "permanecem", "vira"...)
//   pendência específica    -> marca com dois-pontos [CONFERIR: ...]: pergunta concreta sobre uma fonte
//   outros                  -> resto (tabelas de painel em references/, notas)
// Normas e jurisprudência são ignoradas (texto literal).
'use strict';
const fs = require('fs'), path = require('path');
const args = process.argv.slice(2);
const arg = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null; };
const RAIZ = path.resolve(arg('--raiz') || path.join(__dirname, '..'));
const MARCA = new RegExp(arg('--marca') || '\\[CONFERIR', 'g');
const LISTAR = arg('--listar');
const IGNORA_DIR = /^(normas|jurisprudencia|biblioteca|_manutencao|_acervo|_kit-replicacao|node_modules|backup-sincronizacao)$/;
const INSTRUCAO = /(marque|marcar|marca |permanecem|preservam|vira|vire|fica |ficam|como `?\[|use `?\[|grafad|negrito|realce|amarelo|substituir|trocar|em vez de)/i;

const arquivos = [];
(function walk(d) { for (const e of fs.readdirSync(d, { withFileTypes: true })) { const p = path.join(d, e.name); if (e.isDirectory()) { if (!IGNORA_DIR.test(e.name)) walk(p); } else if (e.name.endsWith('.md') && !/^(MANUAL|BRIEFING.*)\.md$/.test(e.name)) arquivos.push(p); } })(RAIZ);

const cat = { 'campo de modelo/painel (assets)': [], 'instrução de uso': [], 'pendência específica': [], 'outros': [] };
let total = 0, comMarca = 0;
for (const f of arquivos) {
  const rel = path.relative(RAIZ, f).split(path.sep).join('/'); let n = 0;
  fs.readFileSync(f, 'utf8').split(String.fromCharCode(10)).forEach((l, i) => {
    const ms = l.match(MARCA); if (!ms) return; n += ms.length; total += ms.length;
    const item = { n: ms.length, txt: rel + ':' + (i + 1) + ' ' + l.trim().replace(/\s+/g, ' ').slice(0, 150) };
    let c;
    if (/\/assets\//.test('/' + rel)) c = 'campo de modelo/painel (assets)';
    else if (INSTRUCAO.test(l) && !/\[CONFERIR:/.test(l)) c = 'instrução de uso';
    else if (/\[CONFERIR:/.test(l)) c = 'pendência específica';
    else c = 'outros';
    cat[c].push(item);
  });
  if (n) comMarca++;
}
console.log(`arquivos varridos ${arquivos.length} | com a marca ${comMarca} | ocorrências ${total}`);
for (const [k, v] of Object.entries(cat)) console.log('  ' + String(v.reduce((a, x) => a + x.n, 0)).padStart(5) + '  ' + k);
if (LISTAR) { const alvo = LISTAR.startsWith('espec') ? 'pendência específica' : 'outros'; console.log('\n' + alvo + ':'); cat[alvo].forEach(x => console.log('  ' + x.txt)); }
