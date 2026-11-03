#!/usr/bin/env node
// Verificador de consistência de um pacote de skills do Claude. Sem dependências: só Node 18+.
// Parte genérica; as regras do setor jurídico ficam em verificador.config.js (veja o README do kit).
//
//   node _manutencao/verificar-pacote.js                       verifica tudo e mostra o resumo
//   node _manutencao/verificar-pacote.js --detalhe             mostra também os avisos
//   node _manutencao/verificar-pacote.js --raiz <pasta>        pasta do pacote (padrão: a pasta acima de _manutencao)
//   node _manutencao/verificar-pacote.js --config <arquivo>    arquivo de configuração (padrão: verificador.config.js ao lado)
//
// Código de saída: 0 sem erros; 1 com erros. Avisos não reprovam.
'use strict';
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { soLetras } = require('./normalizar');

const args = process.argv.slice(2);
const arg = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null; };
const DETALHE = args.includes('--detalhe');
const RAIZ = path.resolve(arg('--raiz') || path.join(__dirname, '..'));
const CFG = require(path.resolve(arg('--config') || path.join(__dirname, 'verificador.config.js')));
const C = Object.assign({
  copias: [], proprioPorSkill: /^(INDEX|MAPA|ESTRUTURA)\.md$/, semProtocolo: [], descricaoMax: 1024,
  nomes: {}, modelos: null, citacoes: { ativo: false, tribunais: 'STJ|STF' }, residuos: [],
}, CFG);

const erros = [], avisos = [];
const erro = (cat, msg) => erros.push({ cat, msg });
const aviso = (cat, msg) => avisos.push({ cat, msg });
const ler = f => fs.readFileSync(f, 'utf8');
const hash = f => crypto.createHash('md5').update(fs.readFileSync(f)).digest('hex');
const rel = f => path.relative(RAIZ, f).split(path.sep).join('/');
const listar = d => fs.readdirSync(d, { withFileTypes: true }).flatMap(e => { const p = path.join(d, e.name); return e.isDirectory() ? listar(p) : [p]; });
const NL = String.fromCharCode(10), CR = String.fromCharCode(13);

const skills = fs.readdirSync(RAIZ, { withFileTypes: true })
  .filter(d => d.isDirectory() && fs.existsSync(path.join(RAIZ, d.name, 'SKILL.md'))).map(d => d.name).sort();

// ---------- 1. cópias idênticas ----------
for (const c of C.copias) {
  const src = path.join(RAIZ, c.fonte, c.arquivo);
  if (!fs.existsSync(src)) { erro('cópias', `fonte ausente: ${rel(src)}`); continue; }
  for (const s of skills) { const d = path.join(RAIZ, s, c.arquivo); if (fs.existsSync(d) && hash(d) !== hash(src)) erro('cópias', `${rel(d)} difere da fonte (${c.fonte})`); }
}
const normas = new Map();
for (const s of skills) {
  const N = path.join(RAIZ, s, 'references', 'normas'); if (!fs.existsSync(N)) continue;
  for (const f of fs.readdirSync(N)) { if (C.proprioPorSkill.test(f) || !f.endsWith('.md')) continue; const h = hash(path.join(N, f)); if (!normas.has(f)) normas.set(f, new Map()); const m = normas.get(f); if (!m.has(h)) m.set(h, []); m.get(h).push(s); }
}
for (const [f, m] of normas) if (m.size > 1) erro('cópias', `norma ${f} com ${m.size} versões: ` + [...m.values()].map(v => v.length > 3 ? `${v.slice(0, 3).join(', ')}… (${v.length})` : v.join(', ')).join(' | '));

// Jurisprudência: cópias de mesmo nome devem ter as mesmas seções (cópia com seções a mais só gera aviso).
const secoes = txt => { const m = new Map(); txt.split(CR).join('').split(NL + '## ').slice(1).forEach(b => { m.set(b.slice(0, b.indexOf(NL)).trim(), b); }); return m; };
const jur = new Map();
for (const s of skills) {
  const J = path.join(RAIZ, s, 'references', 'jurisprudencia'); if (!fs.existsSync(J)) continue;
  for (const f of fs.readdirSync(J)) { if (!f.endsWith('.md') || C.proprioPorSkill.test(f)) continue; if (!jur.has(f)) jur.set(f, []); jur.get(f).push({ s, p: path.join(J, f), h: hash(path.join(J, f)) }); }
}
for (const [f, copias] of jur) {
  const grupos = new Map(); copias.forEach(c => { if (!grupos.has(c.h)) grupos.set(c.h, []); grupos.get(c.h).push(c); });
  if (grupos.size < 2) continue;
  const base = [...grupos.values()].sort((a, b) => b.length - a.length)[0][0];
  const sb = secoes(ler(base.p));
  for (const c of copias) {
    if (c.h === base.h) continue;
    const sc = secoes(ler(c.p)); const faltam = [...sb.keys()].filter(k => !sc.has(k)); const difere = [...sb.keys()].filter(k => sc.has(k) && sc.get(k) !== sb.get(k));
    if (faltam.length) erro('cópias', 'jurisprudência ' + f + ' em ' + c.s + ' sem as seções: ' + faltam.slice(0, 3).join('; '));
    if (difere.length) erro('cópias', 'jurisprudência ' + f + ' em ' + c.s + ' com texto diferente nas seções: ' + difere.slice(0, 3).join('; '));
    if (!faltam.length && !difere.length) aviso('cópias', 'jurisprudência ' + f + ' em ' + c.s + ' tem seções a mais que a versão majoritária (ok se for de propósito)');
  }
}

// Acervo: cada skill deve ter, igual ao acervo, os arquivos que o manifesto lhe atribui.
const MAN = path.join(RAIZ, '_acervo', 'manifesto.json');
if (fs.existsSync(MAN)) {
  const man = JSON.parse(ler(MAN));
  for (const [chave, lista] of Object.entries(man.arquivos)) {
    const origem = path.join(RAIZ, '_acervo', chave);
    if (!fs.existsSync(origem)) { erro('acervo', 'arquivo do manifesto ausente no acervo: ' + chave); continue; }
    const i = chave.indexOf('/'); const pasta = man.pastas[chave.slice(0, i)];
    for (const s of lista) {
      const d = path.join(RAIZ, s, pasta, chave.slice(i + 1));
      if (!fs.existsSync(d)) erro('acervo', s + ' não tem ' + chave + ' (rode sincronizar-acervo.js --aplicar)');
      else if (hash(d) !== hash(origem)) erro('acervo', s + '/' + pasta + '/' + chave.slice(i + 1) + ' difere do acervo (rode sincronizar-acervo.js; se a edição foi na skill, use --trazer)');
    }
  }
  for (const s of skills) for (const k of ['normas', 'jurisprudencia']) {
    if (!man.pastas[k]) continue;
    const D = path.join(RAIZ, s, man.pastas[k]); if (!fs.existsSync(D)) continue;
    for (const f of fs.readdirSync(D)) {
      if (C.proprioPorSkill.test(f) || !f.endsWith('.md') || !fs.statSync(path.join(D, f)).isFile()) continue;
      if (!(man.arquivos[k + '/' + f] || []).includes(s)) aviso('acervo', s + '/' + man.pastas[k] + '/' + f + ' não está no manifesto (use sincronizar-acervo.js --incluir ou --trazer)');
    }
  }
}

// ESTRUTURA.md: o sumário tem de bater com o tamanho atual de cada norma (número de linhas).
for (const s of skills) {
  const D = path.join(RAIZ, s, 'references', 'normas');
  for (const nomeIdx of ['ESTRUTURA.md', 'MAPA.md']) { const E = path.join(D, nomeIdx); if (!fs.existsSync(E)) continue;
  for (const l of ler(E).split(NL)) {
    const m = l.match(/^`([^`]+[.]md)` · ([0-9]+) linhas/); if (!m) continue;
    const f = path.join(D, m[1]);
    const gerador = nomeIdx === 'MAPA.md' ? 'python3 _manutencao/gerar-mapa.py' : 'node _manutencao/gerar-estrutura.js';
    if (!fs.existsSync(f)) { erro('estrutura', s + ': ' + nomeIdx + ' cita ' + m[1] + ', que não existe (rode ' + gerador + ')'); continue; }
    const n = ler(f).split(NL).length;
    if (n !== Number(m[2])) erro('estrutura', s + ': ' + nomeIdx + ' desatualizado para ' + m[1] + ' (' + m[2] + ' linhas no sumário, ' + n + ' no arquivo). Rode ' + gerador);
  }
  }
}

// ---------- 2. SKILL.md: cabeçalho ----------
function frontmatter(t) {
  const m = t.match(/^---\r?\n([\s\S]*?)\r?\n---/); if (!m) return null;
  const nome = (m[1].match(/^name:\s*["']?([^"'\r\n]+)["']?\s*$/m) || [])[1];
  const d = m[1].match(/^description:\s*(>|\|)?\s*(.*(?:\r?\n(?:[ \t]+.*|))*)/m);
  const desc = d ? d[2].split(/\r?\n/).map(l => l.trim()).filter(Boolean).join(' ').replace(/^["']|["']$/g, '') : '';
  return { nome: nome && nome.trim(), desc };
}
for (const s of skills) {
  const fm = frontmatter(ler(path.join(RAIZ, s, 'SKILL.md')));
  if (!fm) { erro('cabeçalho', `${s}: SKILL.md sem cabeçalho`); continue; }
  if (fm.nome !== s) erro('cabeçalho', `${s}: name="${fm.nome}" difere da pasta`);
  if (!fm.desc) erro('cabeçalho', `${s}: description vazia`);
  else if (fm.desc.length > C.descricaoMax) erro('cabeçalho', `${s}: description com ${fm.desc.length} caracteres (limite ${C.descricaoMax})`);
  else if (fm.desc.length > C.descricaoMax * 0.88) aviso('cabeçalho', `${s}: description com ${fm.desc.length} caracteres, perto do limite`);
  if (C.nomes.comandosInexistentes && C.nomes.comandosInexistentes.test(fm.desc)) aviso('cabeçalho', `${s}: description cita comando que não existe`);
}

// ---------- 3. links e remissões ----------
const vistoNome = new Set();
for (const s of skills) {
  const dir = path.join(RAIZ, s);
  for (const f of listar(dir).filter(f => f.endsWith('.md') && !/[\\/](normas|jurisprudencia|biblioteca)[\\/]/.test(f))) {
    const t = ler(f);
    for (const m of t.matchAll(/\]\(((?:assets|references|protocolo)\/[^)#\s]+)\)/g)) if (!fs.existsSync(path.join(dir, m[1]))) erro('links', `${rel(f)} → ${m[1]} não existe`);
    for (const m of t.matchAll(/`((?:assets|references|protocolo)\/[A-Za-z0-9_./-]+\.md)`/g)) if (!fs.existsSync(path.join(dir, m[1])) && !((C.semPecas || []).includes(s) && m[1].startsWith('assets/'))) erro('links', `${rel(f)} cita ${m[1]}, que não existe`);
    if (C.nomes.antigos && C.nomes.antigos.test(t)) erro('nomes', `${rel(f)} usa nome antigo de skill`);
    if (C.nomes.devemExistir) for (const m of t.matchAll(/`(\/?)([a-z]+(?:-[a-z]+)+)`/g)) { const n = m[2]; if (C.nomes.devemExistir.test(n) && !skills.includes(n) && !(C.nomes.externas || []).includes(n) && !vistoNome.has(rel(f) + n)) { vistoNome.add(rel(f) + n); ((C.nomes.planejadas || []).includes(n) ? aviso : erro)('nomes', `${rel(f)} cita skill ${(C.nomes.planejadas || []).includes(n) ? 'planejada e ainda não criada' : 'inexistente'}: ${n}`); } }
  }
}

// ---------- 4. modelos de peça ----------
const M = C.modelos;
if (M) {
  for (const s of skills) {
    const A = path.join(RAIZ, s, 'assets'); if (!fs.existsSync(A)) continue;
    for (const f of fs.readdirSync(A).filter(f => /^modelo-.*\.md$/.test(f))) {
      const p = path.join(A, f), t = ler(p), r = rel(p);
      if (M.naoPeca && M.naoPeca.test(f)) continue;
      if (!M.exigeSoEm || M.exigeSoEm.test(f)) for (const x of M.exigeEmTodos || []) if (!x.re.test(t)) erro('modelos', `${r}: ${x.msg}`);
      for (const x of M.proibeEmTodos || []) if (x.re.test(t)) erro('modelos', `${r}: ${x.msg}`);
      if (M.remeteAoPadrao && !t.includes(M.remeteAoPadrao) && !(M.remeteAoPadraoExcecao && M.remeteAoPadraoExcecao.test(t))) aviso('modelos', `${r}: não remete ao padrão de peças`);
      if (M.judicial && M.judicial.test(f)) for (const x of M.exigeNasJudiciais || []) if (!x.re.test(t)) erro('modelos', `${r}: ${x.msg}`);
      for (const x of M.regrasPorArquivo || []) if (x.arquivo.test(f) && x.proibe.test(t)) (x.nivel === 'aviso' ? aviso : erro)('modelos', `${r}: ${x.msg}`);
      for (const x of M.avisosCondicionais || []) if (x.se.test(t) && !x.exige.test(t)) aviso('modelos', `${r}: ${x.msg}`);
    }
  }
}

// ---------- 5. citações contra o texto transcrito ----------
if (C.citacoes.ativo) {
  const TRIB = C.citacoes.tribunais, RB = new RegExp('^(?:' + TRIB + ')$');
  for (const s of skills) {
    const J = path.join(RAIZ, s, 'references', 'jurisprudencia'); if (!fs.existsSync(J)) continue;
    const base = fs.readdirSync(J).filter(f => f.endsWith('.md')).map(f => ler(path.join(J, f))).join(NL);
    const arquivos = ['assets', 'references'].flatMap(d => fs.existsSync(path.join(RAIZ, s, d)) ? listar(path.join(RAIZ, s, d)).filter(f => f.endsWith('.md') && !/[\\/](normas|jurisprudencia|biblioteca)[\\/]/.test(f)) : []).concat(path.join(RAIZ, s, 'SKILL.md'));
    const faltas = new Map();
    const reSum = new RegExp('Súmulas? ((?:\\d+(?:, | e )?)+)\\/(' + TRIB + ')', 'g');
    const reTem = new RegExp('(?:(?<![\\d\\/])\\b(' + TRIB + '), Tema ([\\d.]+)(?![\\d.]*\\/)|Tema ([\\d.]+)\\/(' + TRIB + '))', 'g');
    for (const f of arquivos) {
      const t = ler(f);
      for (const m of t.matchAll(reSum)) for (const n of m[1].split(/, | e /).filter(Boolean)) {
        const re = new RegExp('^## Súmula ' + n + '( \\(' + m[2] + '\\))?\\s*$', 'm');
        if (!re.test(base)) { const k = `Súmula ${n}/${m[2]}`; if (!faltas.has(k)) faltas.set(k, []); faltas.get(k).push(rel(f)); }
      }
      for (const m of t.matchAll(reTem)) {
        const trib = m[1] || m[4], n = (m[2] || m[3]).replace(/\./g, '');
        const re = new RegExp('^## Tema( Repetitivo)? ' + n + '(/' + trib + ')?\\b', 'm');
        if (!re.test(base)) { const k = `Tema ${n}/${trib}`; if (!faltas.has(k)) faltas.set(k, []); faltas.get(k).push(rel(f)); }
      }
    }
    for (const [k, v] of faltas) aviso('citações', `${s}: ${k} citado e não transcrito (em ${[...new Set(v)].slice(0, 2).join(', ')}${v.length > 2 ? '…' : ''})`);
  }
}

// ---------- 5b. extras: citações do acervo, peças geradas e conferência com o cálculo ----------
// Comandado por C.extras (ver verificador.config.js). Lê só assets/ e testes/ (modelos, padrão e peças de teste),
// nunca os documentos que discutem erros antigos (references/).
const X = C.extras;
// Transcrição literal: o trecho transcrito de norma ou precedente (bloco "> " depois de linha que cita a fonte,
// ou aspas na mesma linha de uma citação) tem de existir no arquivo do acervo da skill. Compara só as letras
// (soLetras), em pedaços separados por supressão "(...)"; pedaço com menos de TR.minLetras letras não conta.
const TR = X && X.transcricoes;
const cacheLetras = new Map();
const letrasDe = f => { if (!cacheLetras.has(f)) cacheLetras.set(f, soLetras(ler(f))); return cacheLetras.get(f); };
function transcricoes(t, r, nd, jurTodo) {
  const linhas = t.split(NL);
  const jur = jurTodo.filter(([f]) => !TR.naoFonte.test(f));  // índices e listas de datas citam o número sem trazer o texto
  const fontes = trecho => {
    const arqs = new Set(), doPrecedente = new Set(); let precedenteFora = null;
    for (const [re, arq] of TR.normas) if (re.test(trecho) && fs.existsSync(path.join(nd, arq))) arqs.add(path.join(nd, arq));
    for (const [re, trib] of TR.sumulas) if (re.test(trecho)) for (const [f] of jur.filter(([f]) => (X.arquivosJur[trib] || /./).test(f))) arqs.add(path.join(nd, '..', 'jurisprudencia', f));
    for (const m of trecho.matchAll(TR.precedente)) {
      const num = m[2];
      const achados = jur.filter(([, c]) => c.includes(num));
      if (achados.length) achados.forEach(([f]) => doPrecedente.add(path.join(nd, '..', 'jurisprudencia', f))); else precedenteFora = `${m[1]} ${num}`;
    }
    // ementa de precedente: só vale o arquivo do precedente, não a norma que a ementa menciona
    return { arqs: doPrecedente.size ? [...doPrecedente] : [...arqs], precedenteFora };
  };
  const confere = (texto, contexto, i) => {
    if (/\[[^\]]*\]/.test(texto.replace(/\[(?:\.\.\.|…)\]/g, ''))) return;  // placeholder ou condicional do modelo
    const pedacos = texto.split(/\((?:\.\.\.|…)\)|\[(?:\.\.\.|…)\]|\.\.\.|…/).map(soLetras).filter(p => p.length >= TR.minLetras);
    if (!pedacos.length) return;
    let { arqs, precedenteFora } = fontes(contexto);
    if (precedenteFora) arqs = [];  // ementa de precedente: só vale o arquivo do precedente
    const marcada = /VERIFICAR|CONFERIR/.test(contexto);
    const sai = marcada ? aviso : erro;
    if (!arqs.length) { if (precedenteFora) sai('transcrições', `${r}:${i + 1}: transcreve ${precedenteFora}, que não está em references/jurisprudencia`); return; }
    const falta = pedacos.filter(p => !arqs.some(a => letrasDe(a).includes(p)));
    if (falta.length) sai('transcrições', `${r}:${i + 1}: trecho transcrito não confere com ${arqs.map(a => path.basename(a)).join(' ou ')} ("${texto.trim().slice(0, 60)}…")`);
  };
  for (let i = 0; i < linhas.length; i++) {
    const l = linhas[i];
    // bloco "> ": a fonte está na última linha não vazia antes do bloco, terminada em ":"
    if (/^> /.test(l) && (i === 0 || !/^>/.test(linhas[i - 1]))) {
      let j = i; const bloco = [];
      while (j < linhas.length && /^>/.test(linhas[j])) bloco.push(linhas[j++].replace(/^>\s?/, ''));
      let k = i - 1; while (k >= 0 && !linhas[k].trim()) k--;
      if (k >= 0 && /:\s*$/.test(linhas[k]) && !/^\*\*/.test(bloco[0])) {
        const contexto = linhas[k] + ' ' + (k > 0 ? linhas[k - 1] : '') + ' ' + bloco.join(' ').slice(0, 200);
        // cada parágrafo do bloco (separado por linha "> " vazia) é conferido sozinho: o caput e o § 3º podem vir sem o § 1º
        bloco.join(NL).split(/\n\s*\n/).forEach(p => confere(p.replace(/\n/g, ' '), contexto, i));
      }
      i = j - 1; continue;
    }
    // aspas na prosa: só quando a citação vem colada à fonte, "…" (art. N) ou "dispõe que …"
    if (/^>/.test(l) || !TR.gatilho.test(l)) continue;
    for (const m of l.matchAll(/"([^"\n]*)"/g)) {
      if (m[1].length < 20) continue;
      const antes = l.slice(Math.max(0, m.index - 120), m.index), depois = l.slice(m.index + m[0].length, m.index + m[0].length + 60);
      if (!TR.atribuiDepois.test(depois) && !TR.atribuiAntes.test(antes)) continue;
      // "…" (art. N do X): vale a fonte do parêntese; sem lei nele, a da linha (e da anterior)
      const paren = TR.atribuiDepois.test(depois) ? (depois.match(/^\s*\([^)]*\)/) || [''])[0] : '';
      confere(m[1], paren && fontes(paren).arqs.length ? paren : (i > 0 ? linhas[i - 1] + ' ' : '') + l, i);
    }
  }
}
if (X) {
  const fmt = v => v.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const marcada = (t, i) => { const a = t.lastIndexOf(NL, i) + 1, b = t.indexOf(NL, i); return /VERIFICAR|CONFERIR/.test(t.slice(a, b < 0 ? t.length : b)); };
  for (const s of skills) {
    const dir = path.join(RAIZ, s);
    const nd = path.join(dir, 'references', 'normas'), jd = path.join(dir, 'references', 'jurisprudencia');
    const lerDir = d => (fs.existsSync(d) ? fs.readdirSync(d).filter(f => f.endsWith('.md')).map(f => [f, ler(path.join(d, f))]) : []);
    const jur = lerDir(jd);
    const juridTodo = jur.map(x => x[1]).join(NL);
    // além de modelos e peças de teste, os índices (references/normas e references/jurisprudencia) também só podem citar o que existe
    const pecas = listar(dir).filter(f => f.endsWith('.md') && (/[\\/](assets|testes)[\\/]/.test(f) || /[\\/]references[\\/](normas|jurisprudencia)[\\/]INDEX\.md$/.test(f)));
    for (const f of pecas) {
      const t = ler(f), r = rel(f);
      const grave = (m, msg) => ((marcada(t, m.index) ? aviso : erro)('citações', `${r}: ${msg}`));
      // artigos: o artigo citado existe na norma do acervo (confere a existência, não o conteúdo do parágrafo)
      for (const m of t.matchAll(/\barts?\.\s*(\d[\d.]*)[^\n;.)]{0,70}?\b(?:do|da)\s+(CPC|CDC|CC|C[óo]digo Civil|C[óo]digo de Processo Civil|C[óo]digo de Defesa do Consumidor|Lei(?: n[ºo.]?)? ?[\d.]+\/\d{2,4}|LGPD)/g)) {
        const alvo = (X.artigos || []).find(([re]) => re.test(m[2])); if (!alvo) continue;
        const arq = path.join(nd, alvo[1]);
        if (!fs.existsSync(arq)) { grave(m, `cita ${m[0].slice(0, 40)}, mas ${alvo[1]} não está em references/normas`); continue; }
        const num = m[1].replace(/[.]+$/, '');
        if (!new RegExp('^Art[.] ' + num.replace(/[.]/g, '[.]') + '(?![0-9])', 'm').test(ler(arq))) grave(m, `art. ${num} não existe em ${alvo[1]}`);
      }
      // súmulas
      const reS = /S[úu]mulas?\s+((?:\d+(?:,\s*|\s+e\s+(?:S[úu]mulas?\s+)?)?)+)\s*(?:[/]\s*|d[oa]\s+)(STJ|STF|TJBA|Turma de Uniformiza[çc][ãa]o)/g;
      for (const m of t.matchAll(reS)) for (const n of m[1].match(/\d+/g)) {
        const trib = /Turma/.test(m[2]) ? 'TJBA' : m[2];
        const fre = (X.arquivosJur || {})[trib]; const base = jur.filter(([f]) => !fre || fre.test(f)).map(x => x[1]).join(NL);
        if (!new RegExp('^#{1,4}\\s*S[úu]mula (?:n[ºo.]?\\s*)?0*' + n + '\\b', 'mi').test(base)) grave(m, `Súmula ${n}/${trib} citada e não transcrita em references/jurisprudencia`);
      }
      // enunciados do FONAJE: o número existe e está vigente (seção '## Enunciado N' do arquivo fonaje-*)
      for (const m of t.matchAll(/Enunciados?\s+(?:C[íi]veis?\s+)?(?:n[ºo.]?\s*)?(\d+)\s+(?:do|da|d[oa]s?)\s+FONAJE\b(?!F)/gi)) {
        const fon = jur.filter(([f]) => /^fonaje-/i.test(f)).map(x => x[1]).join(NL);
        if (!new RegExp('^## Enunciado ' + m[1] + '$', 'm').test(fon)) grave(m, `Enunciado ${m[1]} do FONAJE não consta como vigente em references/jurisprudencia`);
      }
      // enunciados do FONAJEF (Juizados Federais): arquivo fonajef-*
      for (const m of t.matchAll(/Enunciados?\s+(?:n[ºo.]?\s*)?(\d+)\s+(?:do|da|d[oa]s?)\s+FONAJEF/gi)) {
        const fon = jur.filter(([f]) => /^fonajef-/i.test(f)).map(x => x[1]).join(NL);
        if (!new RegExp('^## Enunciado ' + m[1] + '$', 'm').test(fon)) grave(m, `Enunciado ${m[1]} do FONAJEF não consta como vigente em references/jurisprudencia`);
      }
      // temas
      for (const m of t.matchAll(/Tema\s+(?:Repetitivo\s+)?([\d.]+)(?:\s*[/]\s*|\s+d[oa]\s+)(STJ|STF)/g)) {
        const n = m[1].replace(/[.]/g, '');
        const ok = jur.some(([f, c]) => new RegExp('^tema-' + n + '-', 'i').test(f) || new RegExp('^#{1,3}\\s*Tema (?:Repetitivo )?' + n + '\\b', 'mi').test(c));
        if (!ok) grave(m, `Tema ${n}/${m[2]} citado e não transcrito em references/jurisprudencia`);
      }
      // acórdãos por número (EAREsp, REsp...)
      for (const m of t.matchAll(/\b(EAREsp|AREsp|EREsp|REsp)\s+([\d]{1,3}(?:[.]\d{3})+)\/(\w\w)/g)) if (!juridTodo.includes(m[2])) grave(m, `${m[1]} ${m[2]}/${m[3]} não consta de references/jurisprudencia`);
      if (TR && TR.arquivo.test(f)) transcricoes(t, r, nd, jur);
    }
    // mapa de argumentos (réplica e recurso): todo ponto tem resposta e pedido; com a peça ao lado, cada pedido do mapa está nela
    if (X.mapa) for (const f of listar(dir).filter(f => path.basename(f) === X.mapa.arquivo && /[\\/]saida[\\/]/.test(f))) {
      const r = rel(f); let mapa;
      try { mapa = JSON.parse(ler(f)); } catch (e) { erro('mapa', `${r}: JSON inválido`); continue; }
      for (const x of mapa) {
        if (!x.tese) erro('mapa', `${r}: ponto ${x.n} (${x.defesa}) sem resposta`);
        if (!(x.pedidos || []).length) erro('mapa', `${r}: ponto ${x.n} (${x.defesa}) sem pedido`);
      }
      const peca = fs.readdirSync(path.dirname(f)).find(n => X.mapa.peca.test(n));
      if (peca) {
        const t = ler(path.join(path.dirname(f), peca)), ped = t.slice(t.search(/^#+\s*Dos pedidos/mi));
        for (const x of mapa) for (const p of x.pedido_texto || []) if (!ped.includes(p)) erro('mapa', `${rel(path.join(path.dirname(f), peca))}: o ponto ${x.n} (${x.defesa}) pede "${p}", que não está nos pedidos da peça`);
      }
    }
    // peças geradas
    const PG = X.pecas;
    if (PG) for (const f of pecas.filter(f => PG.arquivo.test(f))) {
      const t = ler(f), r = rel(f);
      for (const x of PG.proibe || []) if ((!x.arquivo || x.arquivo.test(f)) && x.re.test(t)) erro('peças', `${r}: ${x.msg}`);
      for (const x of PG.exige || []) if (!x.re.test(t)) erro('peças', `${r}: ${x.msg}`);
      const marcas = (t.match(/\[(?:VERIFICAR|CONFERIR|PREENCHER|CONFIRMAR|DECISÃO)[^\]]*\]|CÁLCULO A CONFERIR/g) || []).length;
      if (marcas) aviso('peças', `${r}: ${marcas} marca(s) de pendência; a peça não está pronta para protocolo`);
      // registro FSC/VF ao lado da peça
      const CK = X.checagem;
      if (CK) {
        const reg = path.join(path.dirname(f), CK.arquivo);
        if (!fs.existsSync(reg)) erro('checagem', `${r}: sem ${CK.arquivo} ao lado da peça (checagem FSC e VF)`);
        else {
          const rt = ler(reg), rr = rel(reg);
          for (let n = 1; n <= 12; n++) {
            const m = rt.match(new RegExp('[|]\\s*FSC' + n + '\\s*[|]\\s*([A-Z_]+)\\s*[|]'));
            if (!m) erro('checagem', `${rr}: falta a linha FSC${n}`);
            else if (!CK.statusFsc.includes(m[1])) erro('checagem', `${rr}: FSC${n} com status inválido (${m[1]})`);
          }
          for (let n = 1; n <= 9; n++) {
            const m = rt.match(new RegExp('[|]\\s*VF' + n + '\\s*[|]\\s*([A-Z_]+)\\s*[|]'));
            if (!m) erro('checagem', `${rr}: falta a linha VF${n}`);
            else if (!CK.statusVf.includes(m[1])) erro('checagem', `${rr}: VF${n} com status inválido (${m[1]})`);
          }
          for (const re of (CK.fsc3[s] || CK.fsc3.padrao)) if (!re.test(t)) erro('checagem', `${r}: FSC3, a peça não traz ${re}`);
          const jec = CK.jec.endereco.test(t.slice(0, 800)) || Boolean(CK.jec.preambulo && CK.jec.preambulo.test(t));
          if (jec) { for (const re of CK.jec.proibe) if (re.test(t)) erro('checagem', `${r}: ${CK.jec.msg}`); }
          else for (const re of CK.comum.exige) if (!re.test(t)) erro('checagem', `${r}: ${CK.comum.msg}`);
          if (/Portão 3:\*\*\s*PENDENTE/.test(rt)) aviso('checagem', `${rr}: portão 3 pendente (FSC ATIVADO ou PENDENTE_ADVOGADO)`);
          if (/FSC4\s*[|]\s*ATIVADO[^\n]*liberado R\$/.test(rt) && !/DECIS[ÃA]O DO ADVOGADO[^\]]*(devolu|dep[óo]sito|compensa)/i.test(t))
            aviso('checagem', `${r}: FSC4 ativado e a peça não traz o bloco de crédito em conta: confirme que o extrato bancário do mês da averbação não mostrou crédito, ou registre a pendência (VF6, Súmula 42/TJBA)`);
          const cjn = path.join(path.dirname(f), PG.calculo || 'calculo.json');
          if (CK.negativaPorContrato.test(s) && fs.existsSync(cjn)) {
            const cc = JSON.parse(ler(cjn));
            for (const l of (cc.contratos || []).concat(cc.derivados || [])) {
              const num = String(l.contrato).replace(/[.*+?^${}()|[\]\\\/]/g, '\\$&');
              if (!new RegExp('^(?:> )?\\*\\*Contratos? nº[^\\n]*' + num + '[^\\n]*\\*\\*[^\\n]*(?:A parte autora nega|Valem as mesmas afirmações)', 'm').test(t)) erro('checagem', `${r}: FSC1/FSC7, sem negativa específica do contrato ${l.contrato}`);
            }
          }
        }
      }
      const cj = path.join(path.dirname(f), PG.calculo || 'calculo.json');
      if (fs.existsSync(cj)) {
        const c = JSON.parse(ler(cj)); const exigidos = [['valor da causa', c.valor_causa], ['total em dobro', c.total_dobro], ['total descontado', c.total_descontado]];
        for (const l of c.contratos || []) exigidos.push([`total do contrato ${l.contrato}`, l.total], [`dobro do contrato ${l.contrato}`, l.dobro]);
        for (const [nome, v] of exigidos) if (v && !t.includes('R$ ' + fmt(v))) erro('peças', `${r}: ${nome} (R$ ${fmt(v)}) não consta da peça; os números vêm de ${PG.calculo || 'calculo.json'}`);
      }
    }
  }
}

// ---------- 5c. arquivos congelados (mapa) e decisões antigas nas referências ----------
if (C.congelados) for (const s of skills) {
  const cf = path.join(RAIZ, s, C.congelados); if (!fs.existsSync(cf)) continue;
  const cg = JSON.parse(ler(cf));
  for (const [r, h] of Object.entries(cg.hashes || {})) {
    const p = path.join(RAIZ, s, r);
    if (!fs.existsSync(p)) erro('mapa', `${s}/${r}: arquivo do mapa ausente`);
    else if (crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex') !== h) erro('mapa', `${s}/${r}: arquivo do mapa alterado: rode testes/mapa/teste_mapa.py e atualize o hash de propósito`);
  }
}
if (C.proibeEmReferencias) for (const f of listar(RAIZ).filter(f => C.proibeEmReferencias.arquivo.test(f) && !/backup-sincronizacao/.test(f))) {
  const t = ler(f);
  for (const x of C.proibeEmReferencias.regras) if (x.re.test(t)) erro('referências', `${rel(f)}: ${x.msg}`);
}

// ---------- 6. resíduos e hábitos conhecidos ----------
for (const s of skills) for (const f of listar(path.join(RAIZ, s)).filter(f => /SKILL\.md$|[\\/]assets[\\/].*\.md$/.test(f))) { const t = ler(f); for (const [re, msg] of C.residuos) if (re.test(t)) aviso('resíduos', `${rel(f)}: ${msg}`); }

// ---------- 7. quebras de linha ----------
const mistos = [];
for (const f of listar(RAIZ).filter(f => f.endsWith('.md') && !/node_modules|backup-sincronizacao/.test(f))) { const b = fs.readFileSync(f, 'utf8'); const crlf = (b.match(/\r\n/g) || []).length, lf = (b.match(/(?<!\r)\n/g) || []).length; if (crlf && lf) mistos.push(rel(f)); }
if (mistos.length) aviso('quebras de linha', `${mistos.length} arquivo(s) com CRLF e LF misturados (ex.: ${mistos.slice(0, 3).join(', ')})`);

// ---------- 8. cobertura das skills ----------
for (const s of skills) { const p = path.join(RAIZ, s, 'protocolo', 'protocolo.md'); if (!C.semProtocolo.includes(s) && !fs.existsSync(p)) erro('estrutura', `${s}: sem protocolo/protocolo.md`); }
const lixo = listar(RAIZ).filter(f => /[\\/]~\$|\.tmp$|\.bak$/.test(f) && !/backup-sincronizacao/.test(f)); if (lixo.length) aviso('estrutura', `arquivos temporários: ${lixo.map(rel).join(', ')}`);

// ---------- resumo ----------
const por = l => l.reduce((a, x) => (a[x.cat] = (a[x.cat] || 0) + 1, a), {});
console.log(`Pacote: ${skills.length} skills — ${skills.join(', ')}`);
console.log(`\nERROS: ${erros.length}${erros.length ? ' (' + Object.entries(por(erros)).map(([k, v]) => k + ' ' + v).join(', ') + ')' : ''}`);
erros.forEach(e => console.log('  ✗ [' + e.cat + '] ' + e.msg));
console.log(`\nAVISOS: ${avisos.length}${avisos.length ? ' (' + Object.entries(por(avisos)).map(([k, v]) => k + ' ' + v).join(', ') + ')' : ''}`);
if (DETALHE) avisos.forEach(a => console.log('  ! [' + a.cat + '] ' + a.msg)); else if (avisos.length) console.log('  (use --detalhe para listar)');
console.log(erros.length ? '\nRESULTADO: REPROVADO' : '\nRESULTADO: APROVADO' + (avisos.length ? ' com avisos' : ''));
process.exit(erros.length ? 1 : 0);
