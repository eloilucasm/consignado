#!/usr/bin/env python3
"""Gera _acervo/jurisprudencia/datas-citaveis.md: datas e notas de rodapé prontas de tudo que os modelos citam.

As bibliotecas do STJ e do STF (stj/, stf/) não vão para as skills; este arquivo vai. Assim a skill lê a data de
julgamento, a de publicação e a situação num lugar só, sem consultar a web e sem pedir conferência ao advogado.
Lacuna vira "SEM DADO" na tabela e o script sai com código 1 (o verificador trata como erro).

Uso (a partir de consignado-pacote/):  python _manutencao/gerar-datas-citaveis.py
"""
import glob, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACERVO = os.path.join(RAIZ, '_acervo')
JUR = os.path.join(ACERVO, 'jurisprudencia')
SAIDA = os.path.join(JUR, 'datas-citaveis.md')


def ler(p):
    return open(p, encoding='utf-8', errors='replace').read()


def campo(s, k):
    m = re.search(r'^%s: "?([^"\n]*)"?\s*$' % k, s, re.M)
    return m.group(1).strip() if m else ''


def br(iso):
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', iso or '')
    return f'{m.group(3)}/{m.group(2)}/{m.group(1)}' if m else ''


MESES = ['jan.', 'fev.', 'mar.', 'abr.', 'maio', 'jun.', 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.']


def abnt(iso):
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', iso or '')
    return f'{int(m.group(3))} {MESES[int(m.group(2)) - 1]} {m.group(1)}' if m else ''


ORGAOS = {'S1': 'Primeira Seção', 'S2': 'Segunda Seção', 'S3': 'Terceira Seção', 'CE': 'Corte Especial'}

# 1. o que os modelos citam
texto = ''
for p in glob.glob(os.path.join(RAIZ, '*', 'assets', 'modelo-*.md')):
    texto += ler(p)
sumulas = sorted({int(n) for n in re.findall(r'S[úu]mulas? (\d+)(?:/STJ| do STJ)', texto)})
temas = sorted({int(n.replace('.', '')) for n in re.findall(r'Tema (?:Repetitivo )?(\d[\d.]*)(?:/STJ)?', texto) if n.replace('.', '').isdigit()})
temas = [t for t in temas if t != 929]  # decisão do escritório de 29/10/2026: Tema 929 não é citado

faltam = []
linhas = []
rodapes = []

L = linhas.append
L('# Datas citáveis — o que a skill escreve sem consultar a web nem pedir conferência')
L('')
L('> Gerado por `_manutencao/gerar-datas-citaveis.py` a partir das bibliotecas do STJ e do STF (coleta de 30/10/2026). **Não edite à mão**: edite a fonte e rode o script.')
L('> Regra de uso: data daqui entra na peça **sem marca**. Campo vazio aqui = a skill omite o elemento na nota de rodapé e relata a lacuna na entrega (protocolo, "Datas de julgamento, publicação e vigência").')
L('')
L('## Súmulas do STJ')
L('')
L('| Súmula | Situação | Órgão | Data da decisão | Publicação (DJe e revistas) |')
L('|---|---|---|---|---|')
for n in sumulas:
    p = os.path.join(JUR, 'stj', 'sumulas', f'sumula-{n}.md')
    if not os.path.exists(p):
        faltam.append(f'Súmula {n}/STJ: arquivo ausente'); L(f'| {n} | SEM DADO | | | |'); continue
    s = ler(p)
    pub = re.search(r'Publica[çc][ãa]o: (.+)', s)
    dec = br(campo(s, 'data_decisao'))
    pub_t = pub.group(1).strip() if pub else ''
    mm = re.match(r'(DJE?) DATA:(\d{2}/\d{2}/\d{4})(?: PG:0*(\d+))?', pub_t)
    if mm:
        pub_t = ('DJe' if mm.group(1) == 'DJE' else 'DJ') + ' de ' + mm.group(2) + (f', p. {mm.group(3)}' if mm.group(3) else '')
    if not dec or not pub_t:
        faltam.append(f'Súmula {n}/STJ: data da decisão ou publicação')
    L(f'| {n} | {campo(s, "situacao")} | {campo(s, "orgao_julgador").title()} | {dec or "SEM DADO"} | {pub_t or "SEM DADO"} |')
    if dec:
        rodapes.append(f'- Súmula {n}/STJ: BRASIL. Superior Tribunal de Justiça. Súmula n. {n}. {campo(s, "orgao_julgador").title()}, julgada em {dec}' + (f'. {pub_t}.' if pub_t else '.'))

L('')
L('## Temas repetitivos do STJ')
L('')
L('| Tema | Situação | Órgão | Julgamento | Publicação do acórdão | Tese publicada | Fonte lida em |')
L('|---|---|---|---|---|---|---|')
for n in temas:
    p = os.path.join(JUR, 'stj', 'temas', f'tema-{n}.md')
    if not os.path.exists(p):
        faltam.append(f'Tema {n}/STJ: arquivo ausente'); L(f'| {n} | SEM DADO | | | | | |'); continue
    s = ler(p)
    sit = campo(s, 'situacao'); j = br(campo(s, 'data_julgamento')); pu = br(campo(s, 'data_publicacao_acordao'))
    julgado = sit not in ('Afetado', 'Em Julgamento')
    if julgado and (not j or not pu):
        faltam.append(f'Tema {n}/STJ: julgado sem data de julgamento ou de publicação')
    L(f'| {n} | {sit} | {ORGAOS.get(campo(s, "orgao_julgador"), campo(s, "orgao_julgador"))} | {j or ("n/a (não julgado)" if not julgado else "SEM DADO")} | {pu or ("n/a (não julgado)" if not julgado else "SEM DADO")} | {campo(s, "tese_publicada")} | {br(campo(s, "baixado_em"))} |')
    if julgado and j:
        rodapes.append(f'- Tema {n}/STJ: BRASIL. Superior Tribunal de Justiça. {ORGAOS.get(campo(s, "orgao_julgador"), "")}. Tema Repetitivo {n}. Julgado em: {abnt(campo(s, "data_julgamento"))}.' + (f' Publicado no DJe em: {abnt(campo(s, "data_publicacao_acordao"))}.' if pu else ''))

L('')
L('## Outros julgados citados nos modelos')
L('')
L('| Julgado | Julgamento | Publicação | Nível da fonte |')
L('|---|---|---|---|')
L('| EAREsp 738.991/RS (STJ, Corte Especial, Min. Og Fernandes, por maioria) | 20/02/2019 | DJe 11/06/2019 | VERIFICADO no Informativo 651/STJ (portal oficial). Aplicação ao consignado é por analogia (caso de telefonia fixa) |')
L('| REsp 2.168.312/PR (STJ, Terceira Turma, Min. Humberto Martins) | 03/11/2025 | DJEN 06/11/2025; Informativo 875/STJ, 03/02/2026 | VERIFICADO no Informativo 875/STJ (portal oficial); destaque conferido, acórdão não lido. Cite o Informativo |')
L('| EAREsp 676.608/RS (STJ, Corte Especial, Min. Og Fernandes, por maioria) | 21/10/2020 | DJe 30/03/2021 | VERIFICADO no inteiro teor certificado (`earesp-676608-stj.md`). Primeira tese na repetição em dobro; modulada para pagamentos posteriores a 30/03/2021 |')
L('| AC 5003696-87.2023.4.04.7118/RS (TRF-4, Terceira Turma, Rel. Roger Raupp Rios) | 13/05/2025 | 13/05/2025 (portal do TRF-4) | VERIFICADO no portal de jurisprudência do TRF-4 (ementa); arquivo `ac-5003696-trf4.md`. Transcrever só os itens 1, 3 e 4 da ementa |')
L('')
L('## Súmulas da Turma de Uniformização do TJBA e enunciados do FONAJE')
L('')
L('A fonte (`sumulas-tjba-turma-uniformizacao.md`) traz o texto e a data da última sessão (10/11/2025), sem data por súmula. A referência da súmula do TJBA e do enunciado do FONAJE **não leva data de publicação**: cite órgão e número. Encontro e data do FONAJE só quando constarem de `fonaje-encontros.md`.')
L('')
L('## Notas de rodapé prontas (copie; elas usam só dado preenchido)')
L('')
for r in rodapes:
    L(r)
L('')

# 2. normas
L('## Normas: publicação e vigência')
L('')
L('| Arquivo | Publicação (DOU) | Observação |')
L('|---|---|---|')
FIXAS = {
    'in-inss-138-2022-consolidada.md': ('13/12/2022 (republicação; a original, de 11/11/2022, saiu com incorreções)', 'vigência no ato da publicação (art. 40); decisão D30 do escritório'),
    'in-inss-28-2008-consolidada-2020.md': ('ato de 16/05/2008; DOU nº 94, de 19/05/2008, Seção 1, p. 102/104', 'revogada pela IN 138; vale para contratos até 12/12/2022 (D30: a IN 138 vige desde 13/12/2022). A consolidação é de 22/07/2020 (DOU nº 140, de 23/07/2020)'),
    'in-inss-alteradoras-da-in28-2022.md': ('IN 131: ato de 25/03/2022; IN 136: ato de 11/08/2022; IN 137: ato de 14/09/2022', 'o texto não traz a data do DOU de cada uma; cite pela data do ato. IN 134/2022 não está no acervo e a skill não a cita'),
    'lei-14905.md': ('01/07/2024', 'ato de 28/06/2024; efeitos: ver nota abaixo da tabela'),
    'in-inss-143-2023.md': ('13/02/2023 (DOU nº 31, Seção 1, p. 72)', 'vigência na publicação (art. 4º); prorroga por 60 dias os prazos do art. 38 da IN 138'),
}
for p in sorted(glob.glob(os.path.join(ACERVO, 'normas', '*.md'))):
    n = os.path.basename(p)
    s = ler(p)
    if n in FIXAS:
        L(f'| {n} | {FIXAS[n][0]} | {FIXAS[n][1]} |'); continue
    m = re.search(r'DOU de ([\d./]*\d)', s)
    if not m:
        m = re.search(r'DOU n[ºo] \d+,? de ([\d./]+)', s)
    if m:
        L(f'| {n} | {m.group(1).replace(".", "/")} | rodapé do texto |')
    else:
        faltam.append(f'norma {n}: sem data de publicação no texto'); L(f'| {n} | SEM DADO | |')
L('')
L('Lei 14.905/2024: efeitos do novo § 2º do art. 406 do CC na publicação (01/07/2024); demais dispositivos 60 dias depois (30/08/2024 pela contagem simples). Lei 14.690/2023: art. 28, § 1º, 90 dias a partir de 03/10/2023, isto é, 01/01/2024.')

open(SAIDA, 'w', encoding='utf-8', newline='\n').write('\n'.join(linhas) + '\n')
print(f'Gravado {SAIDA}: {len(sumulas)} súmulas, {len(temas)} temas, {len(rodapes)} notas prontas.')
if faltam:
    print('LACUNAS:'); [print('  -', f) for f in faltam]; sys.exit(1)
