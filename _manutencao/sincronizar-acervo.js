#!/usr/bin/env node
// Sincroniza o acervo (portatil/_acervo) com as skills, conforme _acervo/manifesto.json.
//
// Por padrão NÃO grava nada: só mostra o que mudaria. Com --aplicar, grava; antes de sobrescrever,
// guarda o arquivo antigo em _manutencao/backup-sincronizacao/<data-hora>/. Nunca apaga arquivo.
//
// Uso (a partir de portatil/):
//   node _manutencao/sincronizar-acervo.js                    # relatório (nada é gravado)
//   node _manutencao/sincronizar-acervo.js --aplicar          # acervo -> skills
//   node _manutencao/sincronizar-acervo.js --skill rural      # restringe a uma skill
//   node _manutencao/sincronizar-acervo.js --arquivo lei-8213 # restringe por trecho do nome
//   node _manutencao/sincronizar-acervo.js --incluir rural normas/lei-9099.md   # skill passa a usar o arquivo
//   node _manutencao/sincronizar-acervo.js --trazer rural normas/lei-9099.md    # skill -> acervo (editou na skill)
const fs = require('fs');
const path = require('path');

const RAIZ = path.resolve(__dirname, '..');
const ACERVO = path.join(RAIZ, '_acervo');
const MANIFESTO = path.join(ACERVO, 'manifesto.json');
const args = process.argv.slice(2);
const flag = n => args.includes(n);
const valor = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null; };

if (!fs.existsSync(MANIFESTO)) { console.error('Manifesto não encontrado: ' + MANIFESTO); process.exit(2); }
const man = JSON.parse(fs.readFileSync(MANIFESTO, 'utf8'));
const pastas = man.pastas; // { protocolo: 'protocolo', pecas: 'assets', normas: 'references/normas', jurisprudencia: 'references/jurisprudencia' }

const iguais = (a, b) => fs.existsSync(a) && fs.existsSync(b) && Buffer.compare(fs.readFileSync(a), fs.readFileSync(b)) === 0;
const destinoNaSkill = (skill, chave) => { const i = chave.indexOf('/'); return path.join(RAIZ, skill, pastas[chave.slice(0, i)], chave.slice(i + 1)); };
const stamp = new Date().toISOString().replace(/[:T]/g, '-').slice(0, 16);
const BACKUP = path.join(RAIZ, '_manutencao', 'backup-sincronizacao', stamp);
function guardar(arquivo, skill, chave) {
  if (!fs.existsSync(arquivo)) return;
  const d = path.join(BACKUP, skill, chave);
  fs.mkdirSync(path.dirname(d), { recursive: true });
  fs.copyFileSync(arquivo, d);
}
const salvarManifesto = () => fs.writeFileSync(MANIFESTO, JSON.stringify(man, null, 1) + String.fromCharCode(10));

// ---------- --incluir <skill> <chave> ----------
if (flag('--incluir')) {
  const i = args.indexOf('--incluir'); const skill = args[i + 1], chave = args[i + 2];
  if (!skill || !chave || !fs.existsSync(path.join(ACERVO, chave))) { console.error('Uso: --incluir <skill> <pasta/arquivo.md> (o arquivo precisa existir no acervo)'); process.exit(2); }
  if (!fs.existsSync(path.join(RAIZ, skill, 'SKILL.md'))) { console.error('Skill não encontrada: ' + skill); process.exit(2); }
  man.arquivos[chave] = Array.from(new Set((man.arquivos[chave] || []).concat(skill))).sort();
  salvarManifesto();
  const dest = destinoNaSkill(skill, chave);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  if (fs.existsSync(dest) && !iguais(dest, path.join(ACERVO, chave))) guardar(dest, skill, chave);
  fs.copyFileSync(path.join(ACERVO, chave), dest);
  console.log('Incluído: ' + chave + ' em ' + skill);
  process.exit(0);
}

// ---------- --trazer <skill> <chave> ----------
if (flag('--trazer')) {
  const i = args.indexOf('--trazer'); const skill = args[i + 1], chave = args[i + 2];
  const origem = skill && chave ? destinoNaSkill(skill, chave) : null;
  if (!origem || !fs.existsSync(origem) || !man.arquivos[chave]) { console.error('Uso: --trazer <skill> <pasta/arquivo.md> (o arquivo precisa estar no manifesto e na skill)'); process.exit(2); }
  const alvo = path.join(ACERVO, chave);
  if (!iguais(origem, alvo)) {
    const d = path.join(BACKUP, '_acervo', chave); fs.mkdirSync(path.dirname(d), { recursive: true }); fs.copyFileSync(alvo, d);
    fs.copyFileSync(origem, alvo);
    console.log('Trazido de ' + skill + ' para o acervo: ' + chave + '. Rode o script (sem --trazer) para propagar às outras skills.');
  } else console.log('Sem diferença: ' + chave);
  process.exit(0);
}

// ---------- relatório / aplicação ----------
const so = valor('--skill'), trecho = valor('--arquivo');
const cont = { igual: 0, ausente: 0, diferente: 0, ausenteNoAcervo: 0 };
const linhas = [];
for (const chave of Object.keys(man.arquivos).sort()) {
  if (trecho && !chave.includes(trecho)) continue;
  const origem = path.join(ACERVO, chave);
  if (!fs.existsSync(origem)) { cont.ausenteNoAcervo++; linhas.push('ERRO   acervo sem o arquivo: ' + chave); continue; }
  for (const skill of man.arquivos[chave]) {
    if (so && skill !== so) continue;
    const dest = destinoNaSkill(skill, chave);
    const estado = !fs.existsSync(dest) ? 'ausente' : iguais(origem, dest) ? 'igual' : 'diferente';
    cont[estado]++;
    if (estado === 'igual') continue;
    linhas.push((estado === 'ausente' ? 'FALTA  ' : 'DIFERE ') + skill.padEnd(26) + chave);
    if (flag('--aplicar')) { if (estado === 'diferente') guardar(dest, skill, chave); fs.mkdirSync(path.dirname(dest), { recursive: true }); fs.copyFileSync(origem, dest); }
  }
}
// arquivos de acervo na skill que não estão no manifesto (aviso)
const avisos = [];
const PROPRIO = /^(INDEX|MAPA|ESTRUTURA)\.md$/;
for (const skill of fs.readdirSync(RAIZ).filter(s => fs.existsSync(path.join(RAIZ, s, 'SKILL.md')))) {
  if (so && skill !== so) continue;
  for (const chave of ['normas', 'jurisprudencia']) {
    const D = path.join(RAIZ, skill, pastas[chave]); if (!fs.existsSync(D)) continue;
    for (const f of fs.readdirSync(D)) {
      if (PROPRIO.test(f) || !fs.statSync(path.join(D, f)).isFile()) continue;
      const k = chave + '/' + f;
      if (!(man.arquivos[k] || []).includes(skill)) avisos.push(skill.padEnd(26) + k + '  (na skill, fora do manifesto: use --incluir ou --trazer)');
    }
  }
}
console.log((flag('--aplicar') ? 'APLICADO' : 'RELATÓRIO (nada foi gravado; use --aplicar)') + ' | iguais ' + cont.igual + ' | faltam ' + cont.ausente + ' | diferem ' + cont.diferente + (cont.ausenteNoAcervo ? ' | acervo incompleto ' + cont.ausenteNoAcervo : ''));
linhas.forEach(l => console.log('  ' + l));
if (avisos.length) { console.log('AVISOS (' + avisos.length + '):'); avisos.forEach(a => console.log('  ' + a)); }
if (flag('--aplicar') && fs.existsSync(BACKUP)) console.log('Backup dos arquivos sobrescritos em: ' + path.relative(RAIZ, BACKUP));
process.exit(cont.diferente + cont.ausente + cont.ausenteNoAcervo > 0 && !flag('--aplicar') ? 1 : 0);
