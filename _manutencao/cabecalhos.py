#!/usr/bin/env python3
"""Cabeçalho (front matter YAML) de toda norma e jurisprudência do acervo.

  python _manutencao/cabecalhos.py --gravar    grava/atualiza o cabeçalho das normas e das fichas feitas à mão
  python _manutencao/cabecalhos.py             valida todos os arquivos de norma e jurisprudência (código 1 se faltar campo)

Os arquivos baixados por máquina (jurisprudencia/stf, jurisprudencia/stj) já nascem com cabeçalho; aqui só se validam.
Datas em ISO (AAAA-MM-DD). Valor vazio só é aceito onde o fato não existe (tema não julgado) ou a fonte não o traz
(listado como LACUNA DA FONTE, nunca preenchido de memória). O corpo dos arquivos não é alterado.
"""
import glob, json, os, re, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACERVO = os.path.join(RAIZ, '_acervo')
NORMAS = os.path.join(ACERVO, 'normas')
JUR = os.path.join(ACERVO, 'jurisprudencia')

CLAUSULA = re.compile(r'((?:Esta|Este|Esta Lei|Este Decreto|Esta Resolução|Esta Instrução Normativa)[^.\n]{0,40}entra(?:rá)? em vigor[^\n]{0,260})', re.I)

# ato = data do ato; dou = publicação; para os atos de norma o ato é conferido contra "Brasília, <data>" do texto quando existe.
NORMAS_DADOS = {
    'cc.md': dict(numero='10.406/2002', especie='lei', ato='2002-01-10', dou='2002-01-11', situacao='vigente (consolidado)'),
    'cdc.md': dict(numero='8.078/1990', especie='lei', ato='1990-09-11', dou='1990-09-12', situacao='vigente (consolidado)'),
    'cf88.md': dict(numero='CF/1988', especie='constituição', ato='1988-10-05', dou='1988-10-05', situacao='vigente (consolidada)', vigencia='a partir da promulgação (05/10/1988)'),
    'cpc.md': dict(numero='13.105/2015', especie='lei', ato='2015-03-16', dou='2015-03-17', situacao='vigente (consolidado)'),
    'dec-12797.md': dict(numero='12.797/2025', especie='decreto', ato='2025-12-23', dou='2025-12-24', situacao='vigente'),
    'lei-10741.md': dict(numero='10.741/2003', especie='lei', ato='2003-10-01', dou='2003-10-03', situacao='vigente (consolidada)'),
    'lei-10820.md': dict(numero='10.820/2003', especie='lei', ato='2003-12-17', dou='2003-12-18', situacao='vigente (consolidada)'),
    'lei-14063.md': dict(numero='14.063/2020', especie='lei', ato='2020-09-23', dou='2020-09-24', situacao='vigente (consolidada)', vigencia='na data da publicação (art. 20): 2020-09-24', observacao='âmbito: interações com entes públicos, atos de pessoas jurídicas e saúde; não é regra geral para relação privada'),
    'mp-2200-2.md': dict(numero='2.200-2/2001', especie='medida provisória', ato='2001-08-24', dou='2001-08-27', situacao='vigente (consolidada); em vigor por força do art. 2º da EC 32/2001', vigencia='na data da publicação (art. 20): 2001-08-27'),
    'lei-14690.md': dict(numero='14.690/2023', especie='lei', ato='2023-10-03', dou='2023-10-03', situacao='vigente (consolidada)', observacao='DOU de 3.10.2023, edição extra', vigencia='art. 37: na data da publicação (2023-10-03) quanto aos demais dispositivos; 180 dias após a publicação quanto ao art. 30'),
    'lei-14905.md': dict(numero='14.905/2024', especie='lei', ato='2024-06-28', dou='2024-07-01', situacao='vigente', efeitos='art. 5º: na publicação (2024-07-01) quanto ao § 2º do art. 406 do CC; 60 dias depois (2024-08-30, contagem simples) quanto ao resto'),
    'lei-9099.md': dict(numero='9.099/1995', especie='lei', ato='1995-09-26', dou='1995-09-27', situacao='vigente (consolidada)'),
    'lgpd.md': dict(numero='13.709/2018', especie='lei', ato='2018-08-14', dou='2018-08-15', situacao='vigente (consolidada)', vigencia='art. 65 (escalonada; redações sucessivas, ler o artigo no texto): 2018-12-28 para os arts. 55-A a 55-L, 58-A e 58-B; 2021-08-01 para os arts. 52 a 54; os demais artigos conforme o inciso II vigente'),
    'res-bcb-96-2021.md': dict(numero='BCB 96/2021', especie='resolução', orgao='Banco Central do Brasil', ato='2021-05-19', dou='2021-05-21', situacao='vigente; alterada pelas Res. BCB 365/2023, 476/2025 e 518/2025', vigencia='ver texto; alterações com efeitos em 2024-07-01 e 2025-12-01', observacao='trata de conta de pagamento; não trata de consignado', fonte='https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=96'),
    'res-cmn-2836-consolidada.md': dict(numero='CMN 2.836/2001', especie='resolução', orgao='Conselho Monetário Nacional', ato='2001-05-30', dou='2001-05-31', situacao='vigente (consolidada; alterada pelas Res. CMN 2.843/2001 e 3.998/2011)', vigencia='na data da publicação (art. 11): 2001-05-31', observacao='DOU de 31/5/2001, Edição Extra, p. 18; fonte: portal de normativos do BCB, "Revogado: falso"', fonte='https://normativos.bcb.gov.br/Lists/Normativos/Attachments/47140/Res_2836_v3_L.pdf'),
    'res-cmn-3954-original.md': dict(numero='CMN 3.954/2011', especie='resolução', orgao='Conselho Monetário Nacional', ato='2011-02-24', dou='2011-02-25', situacao='revogada: arts. 2º e 3º originais a partir de 2022-02-01 pela Res. CMN 4.935; norma revogada pela Res. BCB 277/2022 (2022-12-31)', vigencia='redação original; rege fatos até 2022-01-31'),
    'res-cmn-4549-consolidada.md': dict(numero='CMN 4.549/2017', especie='resolução', orgao='Conselho Monetário Nacional', ato='2017-01-26', dou='2017-01-30', situacao='vigente (consolidada, com arts. 2º-A a 2º-D da Res. CMN 5.112/2023)'),
    'res-cmn-4753-consolidada.md': dict(numero='CMN 4.753/2019', especie='resolução', orgao='Conselho Monetário Nacional', ato='2019-09-26', dou='2019-09-30', situacao='vigente (consolidada)', observacao='trata de conta de depósitos; não serve de base para consignado'),
    'res-cmn-4935.md': dict(numero='CMN 4.935/2021', especie='resolução', orgao='Conselho Monetário Nacional', ato='2021-07-29', dou='2021-08-02', situacao='vigente', vigencia='em vigor desde 2022-02-01', fonte='https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20CMN&numero=4935'),
    'in-inss-138-2022-consolidada.md': dict(numero='PRES/INSS 138/2022', especie='instrução normativa', orgao='INSS', ato='2022-11-10', dou='2022-12-13', situacao='vigente (consolidada, atualizada até 2026)', vigencia='no ato da publicação (art. 40): 2022-12-13', observacao='republicação no DOU nº 233 de 13/12/2022 (decisão D30 do escritório); a original saiu no DOU de 2022-11-11 com incorreções'),
    'in-inss-143-2023.md': dict(numero='PRES/INSS 143/2023', especie='instrução normativa', orgao='INSS', ato='2023-02-10', dou='2023-02-13', situacao='vigente', vigencia='na data da publicação (art. 4º): 2023-02-13', observacao='DOU nº 31, Seção 1, p. 72; prorroga por 60 dias os prazos do art. 38 da IN 138'),
    'in-inss-28-2008-consolidada-2020.md': dict(numero='INSS/PRES 28/2008', especie='instrução normativa', orgao='INSS', ato='2008-05-16', dou='2008-05-19', situacao='revogada pela IN 138 a partir de 2022-12-13; rege contratos até 2022-12-12', observacao='DOU nº 94, Seção 1, p. 102/104; consolidação de 22/07/2020 (DOU nº 140 de 23/07/2020) sem as INs de 2022'),
    'in-inss-alteradoras-da-in28-2022.md': dict(numero='PRES/INSS 131, 136 e 137/2022', especie='instrução normativa', orgao='INSS', ato='2022-03-25', dou='', situacao='alteram a IN 28; perdem a vigência com a revogação da IN 28 em 2022-12-13', observacao='atos: IN 131 de 2022-03-25; IN 136 de 2022-08-11; IN 137 de 2022-09-14; o texto não traz a data do DOU de cada uma; cite pela data do ato', lacuna_fonte='data do DOU de cada IN', fonte='https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/instrucao-normativa/2022/'),
}

MESES = {'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12}


def ler(p):
    return open(p, encoding='utf-8', errors='replace').read()


def corpo(s):
    m = re.match(r'---\r?\n.*?\r?\n---\r?\n?', s, re.S)
    return s[m.end():] if m else s


def yaml(d):
    out = ['---']
    for k, v in d.items():
        if isinstance(v, bool):
            out.append(f'{k}: {str(v).lower()}')
        elif isinstance(v, (int, float)):
            out.append(f'{k}: {v}')
        elif v in ('', None):
            out.append(f'{k}: ')
        elif re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(v)):
            out.append(f'{k}: {v}')
        else:
            out.append(f'{k}: {json.dumps(v, ensure_ascii=False)}')
    out.append('---')
    return '\n'.join(out) + '\n'


def brasilia_iso(s):
    m = re.search(r'Bras[íi]lia ?,? (\d+)[ºo°]? de (\w+) de (\d{4})', s)
    if m and m.group(2).lower() in MESES:
        return f'{m.group(3)}-{MESES[m.group(2).lower()]:02d}-{int(m.group(1)):02d}'
    return None


def campos_cabecalho(s):
    fonte = re.search(r'Fonte:\*{0,2}\s*<?(https?://[^\s>)]+)', s)
    cons = re.search(r'Consulta: (\d{4}-\d{2}-\d{2})', s)
    nivel = re.search(r'N[íi]vel no painel: ([A-Z]+)', s)
    alt = re.search(r'alteração mais recente pelas notas do texto: ([\d.]+)', s)
    return (fonte.group(1) if fonte else ''), (cons.group(1) if cons else ''), (nivel.group(1) if nivel else ''), (alt.group(1) if alt else '')


def titulo(s):
    m = re.search(r'^# (.+)$', corpo(s), re.M)
    return m.group(1).strip() if m else ''


def gravar_normas(erros):
    for n, d in NORMAS_DADOS.items():
        p = os.path.join(NORMAS, n)
        s = ler(p)
        c = corpo(s)
        # confere o ato contra "Brasília, <data>" do texto, quando for de lei/decreto
        b = brasilia_iso(c)
        if b and d['especie'] in ('lei', 'decreto') and b != d['ato']:
            erros.append(f'{n}: ato {d["ato"]} diverge de "Brasília, ..." do texto ({b})')
        vig = d.get('vigencia')
        if not vig:
            cl = CLAUSULA.findall(c)
            vig = cl[-1].strip() if cl else ''
        fonte, cons, nivel, alt = campos_cabecalho(c)
        fonte = d.get('fonte') or fonte
        fm = {
            'titulo': titulo(c), 'tipo': 'norma', 'especie': d['especie'], 'numero': d['numero'],
            'orgao': d.get('orgao', 'Presidência da República / Congresso Nacional' if d['especie'] in ('lei', 'decreto', 'constituição') else ''),
            'ato_data': d['ato'], 'publicacao_dou': d['dou'], 'vigencia': vig, 'efeitos': d.get('efeitos', ''),
            'situacao': d['situacao'], 'ultima_alteracao_nas_notas': alt, 'fonte': fonte, 'consulta': cons,
            # Planalto: conferida contra a página (coletor + comparar-fonte.js), por isso VERIFICADO; PDF fica FEITO até segunda leitura
            'nivel': d.get('nivel') or nivel or ('VERIFICADO' if 'planalto.gov.br' in fonte else 'FEITO'), 'observacao': d.get('observacao', ''), 'lacuna_fonte': d.get('lacuna_fonte', ''),
        }
        fm = {k: v for k, v in fm.items() if v != '' or k in ('publicacao_dou',)}
        open(p, 'w', encoding='utf-8', newline='').write(yaml(fm) + c.lstrip('\n') if False else yaml(fm) + '\n' + c.lstrip('\n'))


def machine_tema(n):
    s = ler(os.path.join(JUR, 'stj', 'temas', f'tema-{n}.md'))
    g = lambda k: (re.search(r'^%s: "?([^"\n]*)"?' % k, s, re.M) or [None, ''])[1].strip()
    return dict(situacao=g('situacao'), data_julgamento=g('data_julgamento'), data_publicacao_acordao=g('data_publicacao_acordao'),
                tese_publicada=(g('tese_publicada') == 'true'), orgao_julgador=g('orgao_julgador'))


ORG = {'S1': 'Primeira Seção', 'S2': 'Segunda Seção', 'S3': 'Terceira Seção', 'CE': 'Corte Especial'}

FICHAS = {
    'tema-1061-stj.md': ('tema', 1061, dict(relator='Min. Marco Aurélio Bellizze', paradigma='REsp 1.846.649/MA (TJMA)')),
    'tema-1076-stj.md': ('tema', 1076, dict(paradigma='REsp 1.850.512/SP (TJSP)')),
    'tema-1198-stj.md': ('tema', 1198, dict(relator='Min. Moura Ribeiro', paradigma='REsp 2.021.665/MS (TJMS)')),
    'tema-1414-stj.md': ('tema', 1414, dict(relator='Min. Raul Araújo')),
    'tema-466-stj.md': ('tema', 466, dict(relator='Min. Luis Felipe Salomão', paradigma='REsp 1.197.929/PR e REsp 1.199.782/PR (TJPR)')),
    'tema-929-stj.md': ('tema', 929, dict(nao_citar=True, motivo_nao_citar='decisão do escritório de 29/10/2026: acórdão não publicado, podem caber embargos')),
}
OUTROS = {
    'sumula-326-stj.md': dict(tipo='súmula', tribunal='STJ', numero='326', orgao_julgador='Corte Especial', data_julgamento='2006-05-22', publicacao='DJ de 07/06/2006, p. 240', situacao='vigente'),
    'sumulas-stj.md': dict(tipo='compilação de súmulas', tribunal='STJ', fonte='https://www.stj.jus.br (lista oficial de verbetes) e arquivo do advogado (súmulas 1 a 10)', consulta='2026-10-18', abrange='1 a 10, 43, 54, 297, 362 e 479', situacao='vigentes na consulta', observacao='as 676 súmulas completas estão em stj/sumulas/ (biblioteca de consulta); as datas citáveis estão em datas-citaveis.md'),
    'earesp-738991-stj.md': dict(tipo='acórdão', tribunal='STJ', numero='EAREsp 738.991/RS', orgao_julgador='Corte Especial', relator='Min. Og Fernandes', data_julgamento='2019-02-20', data_publicacao_acordao='2019-06-11', fonte_nivel='VERIFICADO no Informativo de Jurisprudência n. 651 do STJ (portal oficial): Rel. Min. Og Fernandes, Corte Especial, por maioria, j. 20/02/2019, DJe 11/06/2019', situacao='julgado (por maioria)', observacao='caso de telefonia fixa; uso no consignado é por analogia', fonte='https://informativos.trilhante.com.br/julgados/stj-earesp-738991-rs'),
    'resp-2168312-pr-stj.md': dict(tipo='acórdão', tribunal='STJ', numero='REsp 2.168.312/PR', orgao_julgador='Terceira Turma', relator='Min. Humberto Martins', data_julgamento='2025-11-03', data_publicacao_acordao='2025-11-06', publicacao='DJEN de 06/11/2025; Informativo 875/STJ de 03/02/2026', fonte_nivel='VERIFICADO no Informativo de Jurisprudência n. 875 do STJ (portal oficial): destaque e informações do inteiro teor lidos; o acórdão em si não foi lido', situacao='julgado', fonte='https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&livre=%270875%27.cod.'),
    'earesp-676608-stj.md': dict(tipo='acórdão', tribunal='STJ', numero='EAREsp 676.608/RS', orgao_julgador='Corte Especial', relator='Min. Og Fernandes', data_julgamento='2020-10-21', data_publicacao_acordao='2021-03-30', publicacao='DJe de 30/03/2021', fonte_nivel='VERIFICADO no inteiro teor certificado do acórdão (documento 1498374, PDF trazido pelo escritório): ementa, acórdão e certidão lidos', situacao='julgado; citado na repetição em dobro (decisão R7, 01/11/2026)', fonte='https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?num_registro=201500497769&dt_publicacao=30%2F03%2F2021', consulta='2026-11-01', nivel='VERIFICADO'),
    'ac-5003696-trf4.md': dict(tipo='acórdão', tribunal='TRF-4', numero='AC 5003696-87.2023.4.04.7118/RS', orgao_julgador='Terceira Turma', relator='Roger Raupp Rios', data_julgamento='2025-05-13', data_publicacao_acordao='2025-05-13', fonte_nivel='VERIFICADO no portal de jurisprudência do TRF-4 (eproc): ementa e dados do julgamento lidos; o voto não foi lido', situacao='julgado', fonte='https://jurisprudencia.trf4.jus.br/eproc2trf4/externo_controlador.php?acao=jurisprudencia@jurisprudencia/pesquisar', consulta='2026-11-01', nivel='VERIFICADO'),
    'sumulas-tjba-turma-uniformizacao.md': dict(tipo='compilação de súmulas', tribunal='TJBA', orgao_julgador='Turma de Uniformização das Turmas Recursais', abrange='1 a 55', ultima_sessao='2025-11-10', fonte='arquivo fornecido pelo advogado', consulta='2026-10-28', situacao='vigentes, salvo as revogadas 3 e 22', observacao='sem data por súmula; a referência não leva data de publicação; súmula 45 alterada em 2025-09-03', lacuna_fonte='verificar no site do TJBA súmula posterior a 2025-11-10 (fonte não permite checagem automática)'),
    'fonaje-enunciados-civeis.md': dict(tipo='compilação de enunciados', tribunal='FONAJE', abrange='1 a 178', mais_recente='Enunciado 178, 57º Encontro (Rio Branco/AC, 2026-05-27 a 2026-05-29)', situacao='139 vigentes; 39 revogados/cancelados/substituídos ao fim do arquivo', fonte='https://www.cnj.jus.br/programas-e-acoes/juizados-especiais/enunciados-fonaje/enunciados-civeis/', consulta='2026-10-28', nivel='FEITO', observacao='sem força de lei nem de súmula vinculante', lacuna_fonte='datas de vários encontros (ver fonaje-encontros.md)'),
    'fonajef-enunciados.md': dict(tipo='compilação de enunciados', tribunal='FONAJEF', abrange='1 a 226 (até o XVIII FONAJEF)', situacao='210 vigentes; 16 revogados/cancelados/substituídos ao fim do arquivo', fonte='https://www.ajufe.org.br/foruns/fonajef/enunciados-fonajef', consulta='2026-10-28', nivel='FEITO', observacao='só para processo da Caixa em Juizado Especial Federal; encontro com mês e ano, sem dia', lacuna_fonte='Recomendações, Sugestões ao GT do CNJ e consolidação de 2025'),
    'fonaje-encontros.md': dict(tipo='tabela de encontros', tribunal='FONAJE/FONAJEF', fonte='https://www.cnj.jus.br/programas-e-acoes/juizados-especiais/enunciados-fonaje/enunciados-civeis/ e https://www.ajufe.org.br/foruns/fonajef', situacao='FONAJEF completo (mês e ano); FONAJE parcial', consulta='2026-10-28', nivel='FEITO', lacuna_fonte='data de vários encontros do FONAJE (nenhuma fonte consultada traz lista oficial); na nota de rodapé omitir encontro e data'),
}


def gravar_fichas(erros):
    for n, (t, num, extra) in FICHAS.items():
        p = os.path.join(JUR, n)
        c = corpo(ler(p))
        m = machine_tema(num)
        fonte, cons, nivel, _ = campos_cabecalho(c)
        fm = {'titulo': titulo(c), 'tipo': 'tema repetitivo', 'tribunal': 'STJ', 'numero': str(num), 'orgao_julgador': ORG.get(m['orgao_julgador'], m['orgao_julgador']),
              'situacao': m['situacao'], 'data_julgamento': m['data_julgamento'], 'data_publicacao_acordao': m['data_publicacao_acordao'],
              'tese_publicada': m['tese_publicada']}
        fm.update(extra)
        fm.update({'fonte': fonte, 'consulta': cons or '2026-10-28', 'nivel': nivel or 'VERIFICADO', 'biblioteca': f'stj/temas/tema-{num}.md'})
        # confere o cabeçalho contra a prosa da ficha
        for iso, rot in ((m['data_julgamento'], 'Julgamento'), (m['data_publicacao_acordao'], 'Acórdão')):
            if iso:
                br = f'{iso[8:]}/{iso[5:7]}/{iso[:4]}'
                if br not in c:
                    erros.append(f'{n}: data {br} ({rot}) da biblioteca não aparece na ficha')
        open(p, 'w', encoding='utf-8', newline='').write(yaml(fm) + '\n' + c.lstrip('\n'))
    for n, d in OUTROS.items():
        p = os.path.join(JUR, n)
        c = corpo(ler(p))
        fonte, cons, nivel, _ = campos_cabecalho(c)
        d = dict(d)
        fm = {'titulo': titulo(c)}
        fm.update(d)
        fm.setdefault('fonte', fonte); fm.setdefault('consulta', cons); fm.setdefault('nivel', nivel or 'FEITO')
        fm = {k: v for k, v in fm.items() if v != ''}
        open(p, 'w', encoding='utf-8', newline='').write(yaml(fm) + '\n' + c.lstrip('\n'))


def fm_de(p):
    s = ler(p)
    m = re.match(r'---\r?\n(.*?)\r?\n---', s, re.S)
    d = {}
    if m:
        for l in m.group(1).split('\n'):
            k, _, v = l.partition(':')
            if k and not k.startswith(' '):
                d[k.strip()] = v.strip().strip('"')
    return d if m else None


def validar():
    faltas, lacunas = [], []
    # normas
    for p in sorted(glob.glob(os.path.join(NORMAS, '*.md'))):
        n = os.path.basename(p); d = fm_de(p)
        if d is None:
            faltas.append(f'normas/{n}: sem cabeçalho'); continue
        for k in ('titulo', 'tipo', 'numero', 'ato_data', 'vigencia', 'situacao', 'fonte', 'consulta'):
            if not d.get(k):
                if k == 'vigencia':
                    lacunas.append(f'normas/{n}: sem cláusula de vigência extraída (ler o artigo final)')
                else:
                    faltas.append(f'normas/{n}: campo vazio: {k}')
        if not d.get('publicacao_dou'):
            (lacunas if d.get('lacuna_fonte') else faltas).append(f'normas/{n}: publicacao_dou vazio' + (f' (lacuna da fonte: {d["lacuna_fonte"]})' if d.get('lacuna_fonte') else ''))
    # fichas à mão
    for p in sorted(glob.glob(os.path.join(JUR, '*.md'))):
        n = os.path.basename(p)
        if n in ('INDEX.md', 'LEIAME.md', 'datas-citaveis.md'):
            continue
        d = fm_de(p)
        if d is None:
            faltas.append(f'jurisprudencia/{n}: sem cabeçalho'); continue
        for k in ('titulo', 'tipo', 'tribunal', 'situacao', 'fonte', 'consulta'):
            if not d.get(k):
                faltas.append(f'jurisprudencia/{n}: campo vazio: {k}')
        if d.get('tipo') in ('tema repetitivo', 'acórdão') and d.get('situacao', '').lower() not in ('afetado', 'em julgamento') and d.get('nao_citar') != 'true':
            for k in ('data_julgamento', 'data_publicacao_acordao'):
                if not d.get(k):
                    faltas.append(f'jurisprudencia/{n}: campo vazio: {k}')
    # bibliotecas de máquina (informativo, não bloqueia: lacunas da fonte)
    sem_pub = []
    for p in glob.glob(os.path.join(JUR, 'stj', 'temas', 'tema-*.md')):
        d = fm_de(p)
        if d is None:
            faltas.append(f'stj/temas/{os.path.basename(p)}: sem cabeçalho'); continue
        if d.get('situacao', '') not in ('Afetado', 'Em Julgamento', 'Cancelado') and d.get('data_julgamento') and not d.get('data_publicacao_acordao'):
            sem_pub.append(os.path.basename(p))
    for sub in ('stj/iac', 'stj/puil', 'stj/sirdr', 'stj/sumulas', 'stf/repercussao-geral', 'stf/sumulas', 'stf/sumulas-vinculantes'):
        arqs = [x for x in glob.glob(os.path.join(JUR, sub, '*.md')) if os.path.basename(x) != 'INDEX.md']
        sem = [os.path.basename(x) for x in arqs if fm_de(x) is None]
        if sem:
            faltas.append(f'{sub}: {len(sem)} arquivo(s) sem cabeçalho: {sem[:5]}')
    s_sem = [os.path.basename(x) for x in glob.glob(os.path.join(JUR, 'stj', 'sumulas', 'sumula-*.md')) if not fm_de(x).get('data_decisao')]
    if s_sem:
        lacunas.append(f'stj/sumulas: {len(s_sem)} súmula(s) sem data da decisão (650 a 676: caderno do STJ defasado; fonte BNP só traz o texto)')
    if sem_pub:
        lacunas.append(f'stj/temas: {len(sem_pub)} tema(s) julgado(s) sem data de publicação do acórdão na fonte: {sorted(sem_pub)}')
    return faltas, lacunas


if __name__ == '__main__':
    if '--gravar' in sys.argv:
        erros = []
        gravar_normas(erros); gravar_fichas(erros)
        for e in erros:
            print('DIVERGÊNCIA:', e)
        print('Cabeçalhos gravados.' if not erros else 'Gravado com divergências (acima).')
    faltas, lacunas = validar()
    for f in faltas:
        print('FALTA:', f)
    for l in lacunas:
        print('LACUNA DA FONTE:', l)
    print(f'{len(faltas)} falta(s); {len(lacunas)} lacuna(s) da fonte.')
    sys.exit(1 if faltas else 0)
