---
name: catalogo_fundamentos_sentenca
description: >
  Catálogo dos fundamentos de improcedência (total ou parcial) que os juízos de
  1º grau empregam em ações de empréstimo consignado do INSS fraudado/migrado,
  com a estratégia de ataque de cada um no recurso (Recurso Inominado no JEC ou
  Apelação na Justiça Comum). Calibração inicial extraída de 2 sentenças reais
  (comarca de Ilhéus/BA, 3ª VSJ), articulada com as verificações VF1 a VF9 de
  verificacoes_forenses.md (cessão de crédito, extrato INSS, correspondente
  bancário, autenticação eletrônica). Ler na ETAPA 2, depois de identificar o desfecho e o rito. Fonte
  de ESTRATÉGIA, não de citações — precedentes só de referencias_juridicas.md
  ou dos autos; qualquer outro entra marcado [VERIFICAR ANTES DE PROTOCOLAR].
---

# Catálogo: Fundamentos de Improcedência em Consignado → Ataque no Recurso

## PARTE 0 — Diagnóstico em três passos (sempre nesta ordem)

**Passo 1 — Qual o rito?** Define o NOME da peça e o cardápio de institutos.
JEC → Recurso Inominado (10 dias úteis, arts. 42 e 12-A, Lei 9.099/95). Justiça Comum →
Apelação (15 dias úteis, art. 1.003, § 5º, CPC). Ver `estrutura_recurso.md`.

**Passo 2 — Qual o desfecho?** Define o OBJETO do recurso.

| Desfecho | O que a sentença fez | O que o recurso ataca |
|---|---|---|
| **IMPROCEDÊNCIA TOTAL** | Validou a contratação/cessão; negou o vício | O **mérito** (FSC1–FSC7, FSC9–FSC11) e, na sequência, o dano moral (FSC8) |
| **PARCIAL** | Reconheceu a inexistência/nulidade, mas **negou o dano moral** | **Somente o dano moral** (FSC8). NÃO se reabre o mérito já ganho |
| **EXTINÇÃO SEM MÉRITO** | Extinguiu por exigência não cumprida, inépcia, falta de interesse ou "litigância predatória" | A **anulação** da sentença terminativa (FSC12) e, se a causa estiver madura, o julgamento direto do mérito (art. 1.013, § 3º, I, CPC) |

> **Regra de ouro do objeto:** contra sentença parcial, reabrir a inexistência já
> reconhecida é erro — dá munição para recurso adesivo do réu. O foco é o dano moral.

**Passo 3 — Quais fundamentos a sentença usou?** Mapear entre FSC1 e FSC12.
Cada um vira um tópico das razões, atacado individualmente (dialeticidade — art.
1.010, II e III, CPC; no JEC, art. 42 c/c devolução plena).

**Passo 4 — Viabilidade + exposição** (Parte 3). Viabilidade: chance de reverter a
sentença. Exposição: custo para o autor se perder. JEC: sucumbência recursal de
10–20% (art. 55, Lei 9.099/95). Justiça Comum: honorários recursais (art. 85, §
11, CPC) somam-se aos já fixados. Nenhum desses riscos existe no 1º grau.

---

## PARTE 1 — Os dois cenários, lado a lado

### Cenário A — Recurso contra IMPROCEDÊNCIA TOTAL
1. Síntese do erro da sentença em uma frase.
2. **Erro de direito na distribuição do ônus** (FSC3) — abre, contamina o resto.
3. **Erro de fato na valoração da assinatura/autenticação eletrônica** (FSC1, FSC2).
4. **Erro de fato no "proveito econômico"** (FSC4) — sem confronto TED × LIBERADO.
5. **Erro na aceitação da cessão/migração sem cadeia documental** (FSC5, FSC11), quando aplicável.
6. **Afastamento da "impugnação genérica"/"não impugnação específica"** (FSC7) — aqui entra a impugnação específica que faltou na réplica de 1º grau.
7. Neutralização do "silêncio"/"impugnação tardia" (FSC6).
8. Reconhecido o vício → **dano moral** (FSC8).
9. *(Justiça Comum, se cabível)* **Cerceamento de defesa** (FSC9) como preliminar, antes do mérito.
10. Prequestionamento.

### Cenário B — Recurso contra sentença PARCIAL (só dano moral)
1. Delimitação: o vício já foi reconhecido; devolve-se só o dano moral.
2. **Dano moral em desconto indevido de verba alimentar** (FSC8) — tese central: Súmula 40 do TJBA e as particularidades do caso; *in re ipsa* subsidiário (questão aberta no Tema 1414/STJ, III.d).
3. Afastamento dos precedentes de "mero aborrecimento"/"mero inadimplemento contratual" que a sentença invocou.
4. Prequestionamento (+ uniformização, se JEC; ou preparação para eventual REsp/RE, se Justiça Comum).

---

## PARTE 2 — Catálogo de fundamentos

### FSC1 — "A assinatura confere a olho com o RG/CNH — dispensa perícia"
*Visto em:* Sentença 1 (proc. 0006139-27.2026.8.05.0103, Geraldo Joaquim Cruz Neto)
— "instrumento contratual assinado (...) com assinatura idêntica àquela contida
em seu documento de identidade pessoal (...) e não impugnado especificamente
pela parte autora".

**O erro:** comparação visual de assinatura feita pelo próprio juízo (leigo ou
togado), sem qualquer exame técnico, elevada à categoria de prova plena de
autoria. É exatamente o que a verificação VF2 (campo "Tipo de assinatura")
manda verificar antes de qualquer peça: se a assinatura é **manuscrita** (de
punho), só perícia grafotécnica dirime a controvérsia sobre autenticidade
(inclusive falsificação sofisticada por decalque/imitação, indetectável a
olho nu por leigo); se é **eletrônica**, a "semelhança visual" sequer é o
exame pertinente — o que importa é a integridade da trilha (hash, log,
plataforma de assinatura), matéria de perícia em informática forense.

**Ataque:**
- Comparação grafológica a olho nu, por quem não é perito, não tem valor
  probatório técnico — é subjetiva e falível mesmo para peritos sem exame
  laboratorial (grafoscopia: pressão do traço, ductus, ritmo, ataques e remates).
- **Autoria controvertida desde a inicial.** A negativa de contratação na inicial já põe em
  controvérsia a autoria do documento que o réu viria a juntar; a tese da parte, considerada em
  conjunto, é incompatível com a autenticidade (lógica do art. 341, III, CPC). Contestada a
  autenticidade, o ônus de prová-la é de quem produziu o documento (art. 429, II, CPC; Tema
  1061/STJ, que trata exatamente de assinatura em contrato bancário).
- **Revaloração, não impugnação nova.** O recurso não "supre" a impugnação que faltou na réplica
  (risco de preclusão: arts. 411, III, 430 e 1.014, CPC). Ele demonstra que a prova JÁ nos autos
  não sustenta a conclusão da sentença: aponta, um a um, os elementos do próprio documento que
  tornam a assinatura duvidosa (traço, posição, confronto com outras assinaturas do autor nos
  autos: procuração, RG, outros contratos). É questão de valoração da prova, devolvida ao órgão
  recursal (art. 1.013, § 1º, CPC).
- **JEC:** perícia grafotécnica é vedada (art. 35, IV, Lei 9.099/95) — mas isso
  reforça que o juízo não podia dar por resolvida, a olho, controvérsia que o
  próprio rito impede de instruir com perícia. Nesse cenário, o correto é a
  inversão do ônus (FSC3) fazer o réu arcar com a fragilidade probatória, não
  o juízo suprir a lacuna com exame leigo.
- **Justiça Comum:** aqui a perícia grafotécnica é não só cabível como
  RECOMENDADA — se não foi deferida/realizada, isso é cerceamento de defesa
  (FSC9), preliminar a arguir antes do mérito.
**Viabilidade:** MÉDIA — depende de haver, nos próprios autos, outras assinaturas
do autor para contraste visual reforçando a divergência. Sem contraponto
documental robusto, cai para MÉDIA ou FRACA no JEC (sem perícia, é discurso vs.
discurso).

---

### FSC2 — "Múltiplas camadas de segurança eletrônica" = prova plena de autoria
*Visto em:* Sentença 2 (proc. 0005566-86.2026.8.05.0103, Gildásio Antônio de
Souza x Banrisul) — plataforma BemSign, biometria facial (liveness),
geolocalização, hash criptográfico, tudo somado e chamado de "rastreabilidade
técnica completa", "múltiplas camadas de segurança".

**O erro:** a sentença descreve a EXISTÊNCIA dos elementos técnicos (log,
biometria, hash) e conclui, sem qualquer exame de conteúdo, que eles PROVAM
autoria. É a falácia de tratar a quantidade de metadados como sinônimo de
qualidade probatória. A verificação VF4 é categórica: biometria válida
exige elementos específicos e verificáveis — algoritmo, matching score,
thresholds, FAR/FRR, liveness detection com parâmetros técnicos, metadados
completos, hash de integridade vinculado ao contrato. A sentença apenas
relata que o réu "informou" ter esses elementos — sem que a peça técnica
(relatório com score, IP, reverse DNS, geolocalização em coordenadas
conferíveis) tenha sido de fato reexaminada linha a linha.

**Ataque:**
- Distinguir **existência de um log** de **idoneidade do conteúdo do log**: a
  sentença presumiu a segunda a partir da primeira. Reexaminar (VF4, já
  ancorado nos autos): o IP registrado é privado (RFC 1918)? Se for, o
  log não traz o IP público da sessão, que permitiria identificar a origem e o assinante: é
  lacuna do documento do réu (ônus dele), não prova de que o cliente não estava em casa. Um
  celular no Wi-Fi de casa tem IP privado; não afirmar "impossível para cliente residencial". Reverse DNS aponta operadora compatível com
  cliente residencial ou com o próprio correspondente/banco? O campo
  Cidade-UF está preenchido ou vazio? A geolocalização tem precisão
  suficiente para fixar endereço, ou é um raio de centenas de metros?
- Biometria facial com liveness SEM relatório técnico (score, threshold,
  FAR/FRR, timestamp integrado) é apenas selfie com nome sofisticado — não
  prova que quem apareceu na câmera foi o autor autorizando aquele contrato
  específico, e menos ainda afasta montagem/reaproveitamento de imagem.
- Hash criptográfico prova a integridade do ARQUIVO após assinado — não prova
  QUEM operou o dispositivo no momento da assinatura.
- **Geolocalização (VF9):** confrontar a localização que o próprio
  log do réu registra com o endereço da residência do autor, constante dos autos
  (distância em escala local, não só o município), os eventos do log entre si
  (compatibilidade espaço-tempo) e a repetição de pontos e IPs em datas ou
  contratos diferentes. A divergência é apontada qualquer que seja a fonte (ônus do banco,
  Regra 16; o log é documento do réu e vale por inteiro contra ele: art. 412, parágrafo único,
  CPC, indivisibilidade); mesma cidade não
  afasta a divergência, porque a operação pode ter ocorrido em loja do próprio
  município. Localização de IP ou fonte não identificada é divergente acima de
  5 km, e o ônus de explicá-la é do banco (Regra 16). Localização por rede (Wi-Fi ou torre) conta como
  GPS se o log informar a precisão (margem dobrada). Sem coordenada, a
  tese se apoia na convergência de indicadores (Wi-Fi, aparelho, telefone,
  fuso, horário, correspondente), classificados em Forte, Médio e Reforço
  (VF9).
  Modelo de parágrafo em `estrutura_recurso.md`, subseção IV.3.
- **JEC:** perícia em informática forense é vedada — a fragilidade não
  reexaminada tecnicamente deveria ter militado pela inversão do ônus (FSC3),
  não pela presunção de idoneidade.
- **Justiça Comum:** requerer perícia em informática forense (com os quesitos já
  formulados nos autos) se não foi produzida — cerceamento de defesa (FSC9).
**Viabilidade:** MÉDIA, tendendo a FRACA quando NÃO há lacuna de IP/geoloc
incompatível para contrapor; sobe a FORTE quando a análise cruzada (VF7, VF4) revela
indício técnico concreto (e-mail ou telefone de terceiro, campo de localização vazio, log sem IP público) ou
quando a VF9 revela divergência de GPS em relação à residência (inclusive
dentro da mesma cidade), ponto de GPS recorrente fora da residência, ou
eventos de GPS fisicamente incompatíveis entre si. Divergência de IP ou fonte não identificada (acima de 5 km) também eleva, porque o ônus de explicar o
ponto é do banco; o risco é o julgador aceitar a imprecisão do IP como explicação, e a peça responde
com o dilema da Regra 16. Indicadores sem coordenada só elevam
quando houver ao menos um de nível Forte apoiado por outros.

---

### FSC3 — Recusa da inversão do ônus por "falta de verossimilhança" (art. 373, I, CPC)
*Visto em:* Sentença 2 — "Não consigo extrair a mais mínima verossimilhança nas
afirmações autorais, o que desautoriza a inversão do ônus da prova."

**Erro de direito.** Deve **abrir** as razões — contamina toda a valoração
seguinte, porque, uma vez negada a inversão, a sentença passou a exigir do
autor prova de fato negativo (que não contratou).

**Ataque:**
- A verossimilhança, em ação de consignado não reconhecido, está na própria
  natureza da alegação (fato negativo) somada à hipossuficiência técnica e
  informacional do consumidor: logs, IP, plataforma de assinatura, dados do
  correspondente e trilha de biometria estão sob domínio EXCLUSIVO do réu.
- **Inversão legal, que dispensa a do art. 6º, VIII (abrir por aqui).** No fato do serviço, o
  fornecedor só se exime se provar a inexistência do defeito ou a culpa exclusiva do consumidor
  ou de terceiro (art. 14, § 3º, CDC): o ônus é do banco por força de lei, não por decisão do juiz.
  Somar o art. 429, II, CPC (autenticidade contestada: ônus de quem produziu o documento) e o
  Tema 1061/STJ. A recusa da inversão judicial, portanto, não muda o resultado.
- Art. 6º, VIII, CDC → inversão *ope judicis* (depende de decisão, com verossimilhança OU
  hipossuficiência, requisitos alternativos). Não sustentar que é "de pleno direito". O ataque é
  outro: exigir verossimilhança do próprio mérito antes de distribuir o ônus é raciocínio
  circular, e a hipossuficiência técnica (logs, IP, biometria sob domínio do réu) basta sozinha.
- Art. 373, § 1º, CPC (subsidiário): distribuição dinâmica também aponta para
  quem tem aptidão para a prova — o réu, não o autor.
- Súmula 479/STJ: fraude de terceiro é fortuito interno, não afasta a responsabilidade
  objetiva; reforça o art. 14, § 3º, CDC.
**Viabilidade:** FORTE — erro de direito bem definido, presente na maioria dos
casos calibrados até aqui.

---

### FSC4 — "Proveito econômico comprovado" sem confronto TED × LIBERADO

> Súmulas do TJBA ligadas a este fundamento: 42 (contra o recorrente; exige o confronto TED × LIBERADO). Ver `referencias_juridicas.md`.
*Visto em:* Sentença 1 ("disponibilização do valor do empréstimo na conta
bancária de titularidade da parte requerente, que coincide exatamente com a
conta (...) do benefício previdenciário") e Sentença 2 ("comprovante de TED no
valor de R$ 2.034,54 para conta corrente de titularidade da parte autora").

**O erro:** a sentença aceita o TED/depósito como prova bastante de proveito
econômico sem executar a verificação VF6 — confrontar o valor do TED com
a coluna **LIBERADO** do extrato INSS. Isso é decisivo em três hipóteses que a
sentença não examinou:
1. Se o LIBERADO estiver em branco/R$ 0,00 (portabilidade pura), o "proveito
   econômico" é imprestável como fundamento — não houve troco algum.
2. Se o valor do TED divergir do LIBERADO, o TED pode não corresponder ao
   contrato exatamente impugnado (substituição de objeto).
3. Mesmo com valores coincidentes, depósito em conta não prova que o TITULAR
   moveu/usou o valor, nem que autorizou a contratação especificamente
   impugnada — o correntista pode ter sido vítima de terceiro com acesso à
   própria conta (ex.: aplicativo/senha comprometidos), hipótese em que o
   crédito cai na conta da vítima sem que ela tenha contratado.

**Ataque:**
- Reexecutar a VF6: extrair o LIBERADO do extrato INSS para o contrato
  especificamente impugnado e confrontar com o TED juntado pelo réu.
- Se houver refinanciamento/portabilidade (Sentença 2 menciona "quitação de
  contrato anterior no valor de R$ 6.577,43"), checar se a "liberação" é, na
  prática, mero repasse interno para quitar dívida anterior — sem troco real
  ao consumidor — o que esvazia o argumento de proveito econômico livre.
- Depósito em conta ≠ consentimento na contratação: reforçar que a análise da
  sentença confundiu o EFEITO financeiro do contrato com a PROVA de quem o
  celebrou.
**Viabilidade:** FRACA se o valor recebido é integralmente compatível e sem
qualquer indício de portabilidade pura/divergência — recorrer tende à
confirmação. FORTE ou MÉDIA sempre que o confronto da VF6 revelar divergência de
valores, LIBERADO zerado, ou portabilidade disfarçada de crédito novo.

---

### FSC5 — Refinanciamento/portabilidade aceito sem exame da cadeia de cessão
*Visto em:* Sentença 2 — "Comprovação de refinanciamento de contrato anterior"
listada como prova de regularidade, sem qualquer exame da cadeia.

**Ataque (ativar só se o extrato INSS mostrar "Migrado do contrato X CBC: Y"
ou equivalente — VF3):**
- Reexaminar o Eixo EXISTÊNCIA (arts. 104, II, 107, 108, 166, II,
  286–288, CC): há instrumento de cessão/endosso identificando este contrato
  por número, data e valor, com assinatura de cedente e cessionário?
- Reexaminar o Eixo EFICÁCIA (art. 290, CC): há notificação ao
  devedor, em forma idônea, anterior aos descontos?
- **Nunca aceitar "ciência pelos descontos no extrato" ou "averbação no INSS"
  como substitutas da notificação** — se a sentença fez essa equiparação, é
  erro de direito a atacar de frente.
- Se o réu juntou o mesmo arquivo com nomes distintos para simular
  endosso/cessão (hash idêntico) — indício crítico autônomo de apocrifia.
**Viabilidade:** varia conforme a força documental da cessão nos autos —
FORTE se ausente qualquer instrumento; FRACA se a cessão está formalmente
completa e a sentença apenas a resumiu corretamente.

---

### FSC6 — "Impugnação tardia" do autor usada contra a verossimilhança
*Visto em:* Sentença 2 — contrato de 2023, impugnado em 2026; a sentença trata
o lapso como indício de ausência de vício de consentimento.

**Ataque:**
- O desconto consignado é descontado automaticamente do benefício, sem
  necessidade de ação do titular — o consumidor médio não confere mensalmente
  a Carta de Concessão/HISCON linha a linha; a ciência efetiva costuma ocorrer
  quando o total descontado se torna perceptível ou ao consultar o Meu INSS.
- Separar as pretensões:
  (a) **declaração de inexistência** do contrato não consentido: não prescreve (negócio
      inexistente ou nulo não convalesce pelo tempo, art. 169, CC);
  (b) **repetição do indébito e dano moral**: prescrevem. Prazo e termo inicial são DECISÃO DO
      ADVOGADO (pendência): art. 27, CDC (5 anos, fato do serviço, a partir do conhecimento do
      dano e da autoria) ou art. 205, CC (10 anos); em desconto mensal, discutir se cada parcela
      tem prazo próprio. Não citar posição do STJ sobre o termo inicial; se o advogado fornecer o
      acórdão, citar com os dados que ele indicar.
- "Impugnação tardia" dentro do prazo não é fundamento de mérito: é, no máximo, prescrição de
  parcelas antigas, que tem regime próprio e não se confunde com falta de verossimilhança.
- Silêncio sem ciência inequívoca não é anuência nem *supressio* (que exige
  inércia voluntária e ciente, do titular do direito, não do consumidor leigo).
**Viabilidade:** MÉDIA — argumento sólido em tese, mas juízos que já usaram esse
fundamento tendem a repeti-lo; reforçar com a mecânica do desconto automático.

---

### FSC7 — "Não impugnação específica" da réplica (art. 341, CPC contra o autor)
*Visto em:* Sentença 1 — "não impugnado especificamente pela parte autora".

**Atenção — autocrítica necessária:** este fundamento aponta, tipicamente, para
uma fragilidade da PRÓPRIA réplica apresentada no 1º grau (rebate genérico, sem
impugnar documento a documento). O recurso enfrenta essa lacuna pela
revaloração da prova dos autos, nunca como impugnação nova, fato ou documento novo.

**Ataque:**
- Reexaminar TODOS os documentos do réu já juntados (VF1 e VF2: índice
  real, rasterização, ficha do contrato) e, agora sim, impugnar
  especificamente cada um: tipo de assinatura, coerência de datas
  (CCB assinada antes da trilha existir?), dados cadastrais divergentes,
  IP/geolocalização, correspondente bancário.
- **Risco de preclusão, a enfrentar de frente.** Documento particular não impugnado presume-se
  autêntico (art. 411, III, CPC); a falsidade tem momento próprio (art. 430); questão de fato
  não proposta no 1º grau só entra no recurso por força maior (art. 1.014). O art. 1.013, § 1º,
  devolve as questões "suscitadas e discutidas", não questões novas. Logo, NUNCA escrever que o
  recurso "supre a impugnação que faltou" nem que "o que não foi dito pode ser dito agora".
- **Como contornar:** (a) a autoria estava controvertida desde a inicial (negativa de
  contratação; lógica do art. 341, III, CPC), então não há fato novo; (b) a tese do recurso é de
  revaloração: o documento, tal como está nos autos, não prova o que a sentença diz (questão
  devolvida, art. 1.013, § 1º); (c) o ônus da autenticidade era do réu (art. 429, II, CPC; Tema
  1061/STJ) e, no fato do serviço, o da regularidade também (art. 14, § 3º, CDC); (d) o próprio
  documento do réu traz as inconsistências e vale por inteiro contra ele (art. 412, parágrafo
  único, CPC).
**Viabilidade:** este fundamento por si não define a viabilidade — ele qualifica o
RISCO de que os fundamentos FSC1/FSC2/FSC4 sejam mantidos se a impugnação
específica no recurso não for robusta. Tratar como sinal de alerta para
redigir a Seção de impugnação específica com o máximo de detalhe factual.

---

### FSC8 — Dano moral negado como "mero dissabor"/"mero inadimplemento contratual"

> Súmulas ligadas a este fundamento: 40 do TJBA (contra: desconto indevido, por si só, não é dano moral; demonstrar a particularidade do caso), 30 e 31 do TJBA e 362/STJ (a favor). Ver `referencias_juridicas.md`.
*Visto em:* Sentença 2 — cadeia de precedentes de "mero dissabor", "mero
inadimplemento contratual", risco de "banalização do instituto".

**Ataque (núcleo do Cenário B, e capítulo final do Cenário A):**
- O desconto indevido incide sobre **verba de natureza alimentar** (benefício
  previdenciário) — não é inadimplemento contratual comum, é subtração mensal
  e automática de renda de subsistência, muitas vezes de idoso/hipossuficiente,
  sem qualquer possibilidade de o titular impedir o desconto na origem.
  Distinguir expressamente dos precedentes que tratam de mero atraso/
  inadimplemento em relação contratual regular.
- Particularidades primeiro (Súmula 40 do TJBA admite o dano quando demonstradas): natureza alimentar,
  valor e duração dos descontos, idade, reclamação prévia sem resposta, comprometimento da renda.
- Subsidiariamente, dano in re ipsa: o desconto não consentido em benefício previdenciário, mês a mês, é
  violação a direito da personalidade que dispensa prova de prejuízo além do próprio desconto. Ressalvar
  que a questão está em aberto no Tema 1414/STJ (III.d) e não apresentá-la como entendimento pacífico.
- Precedentes de "mero dissabor" tratam de contratempos pontuais em relação
  contratual válida — aqui a premissa (contrato válido) é exatamente o que
  está sendo impugnado; se o mérito for revertido, o precedente invocado pela
  sentença perde a pertinência (raciocínio condicional a explicitar nas razões).
- **Valor:** manter o da inicial, sem alterar.
**Viabilidade:** MÉDIA — parte das Turmas/Câmaras ainda resiste ao dano in re ipsa
puro; reforçar com a natureza alimentar do desconto (diferencial forte do
consignado frente à conta fraudulenta comum) eleva a chance de êxito.

---

### FSC9 — Cerceamento de defesa *(módulo exclusivo da Justiça Comum)*
*Gatilho:* a réplica requereu perícia (grafotécnica, se houver assinatura
manuscrita; informática forense, se eletrônica; contábil; documentoscópica)
e/ou exibição de documentos, e o juízo julgou
antecipadamente sem apreciar ou sem deferir o pedido, ou deferiu e não
intimou/viabilizou a produção.

**Ataque (preliminar, antes do mérito):**
- Art. 370 c/c art. 464, CPC: cabe ao juiz determinar as provas necessárias
  ao julgamento; o julgamento antecipado do mérito (art. 355, I) pressupõe que
  a prova documental já seja suficiente — o que é incompatível com
  controvérsia sobre autenticidade de assinatura/autoria de contratação
  eletrônica não dirimível sem exame técnico.
- Indeferimento de perícia relevante e específica, sem fundamentação
  proporcional, é nulidade por cerceamento de defesa (violação ao
  contraditório e à ampla prova, art. 5º, LV, CF).
- **Pedido:** primeiro a anulação da sentença com retorno para instrução
  (produção da perícia requerida); subsidiariamente, o enfrentamento direto do
  mérito com base no que já consta dos autos.
**Viabilidade:** FORTE quando a perícia foi expressamente requerida e simplesmente
ignorada; MÉDIA se o requerimento foi genérico ou tardio.

---

### FSC10 — Correspondente bancário / IP RFC 1918 / geolocalização não enfrentados
*Gatilho:* a sentença nem menciona esses elementos, apesar de estarem nos autos
(VF4 e VF5).

**Ataque:** reexecutar a VF4 (reverse DNS; IP privado no log = log sem o IP
público da sessão, lacuna do réu, nunca "impossível para cliente residencial") e a VF5 (correspondente sediado
em UF distante, sem contrato de correspondência ou credenciamento BACEN
comprovado — Res. CMN 3.954/2011, art. 2º (hoje Res. CMN 4.935/2021, art. 3º); Súmula 479/STJ). Indícios não
enfrentados pela sentença são omissão de fundamentação relevante a suprir
agora, com base no que já está nos autos. Se o log registra localização
incompatível com o domicílio e a sentença não a enfrentou, incluir o quadro
da VF9 (ver FSC2).
**Viabilidade:** FORTE quando o indício é objetivamente verificável (correspondente em outro estado sem
credenciamento comprovado; localização do log divergente da residência; dado de terceiro no
cadastro). IP privado isolado é MÉDIA: depende de saber qual IP o log registra.

---

### FSC11 — Contratos incluídos na mesma data / padrão de portabilidade + refinanciamento
*Gatilho:* extrato INSS mostra dois ou mais contratos incluídos no mesmo dia
ou em intervalo curto, sem exame pela sentença (VF8).

**Ataque:** padrão sistêmico de portabilidade seguida de refinanciamento no
mesmo dia (ou vice-versa) é indício de operação em cadeia orquestrada pelo
correspondente, incompatível com deliberação livre e refletida do consumidor
idoso/hipossuficiente sobre múltiplas obrigações simultâneas.
**Viabilidade:** MÉDIA — reforça outros fundamentos, raramente decide sozinho.

---

### FSC12 — "Litigância predatória" / exigências de autenticidade da postulação / má-fé

> Súmulas do TJBA ligadas a este fundamento (todas contra o recorrente; texto em
> `jurisprudencia/sumulas-tjba-turma-uniformizacao.md`): 42 (negar contratação provada = indício de má-fé), 46 e 54
> (múltiplas ações semelhantes; fracionamento), 47 (distribuição atípica), 51 (documentos
> desatualizados ou ilegíveis; mandado de constatação), 52 (ações idênticas em estados diferentes),
> 53 (confirmação pessoal do autor em caso suspeito). Precedente vinculante: Tema 1198/STJ.

*Gatilho:* a sentença (a) extingue o processo sem mérito porque o autor não atendeu exigência
(comparecimento pessoal, procuração ou documentos atualizados, comprovante de residência legível,
emenda da inicial), ou por "litigância predatória"/"demanda fraudulenta"; ou (b) julga improcedente
e aplica multa por litigância de má-fé (Súmula 42; arts. 80 e 81, CPC); ou (c) usa o volume de ações
do escritório como fundamento.

*Ainda não visto nas sentenças de calibração (Parte 5); fundamento previsto a partir das súmulas.*

**Travas de exposição do escritório (valem acima de todo o resto deste FSC):**
1. **Gatilho estrito.** Só ativar se a sentença usou expressamente o fundamento. Em qualquer outro
   caso, a peça NÃO toca em litigância predatória, abusiva ou de massa, nem para se antecipar.
2. **Passo zero é interno.** O levantamento sobre outras ações vai só para o cartão de pausa. Nunca
   escrever na peça quantas ações o autor ou o escritório têm, nem que "há outras ações sobre
   contratos diferentes".
3. **Nada sobre a colheita da procuração.** Não invocar a trilha de assinatura da procuração, o
   local onde foi assinada nem qualquer apoio do escritório para provar a autenticidade da
   postulação (isso expõe o escritório e a tese da residência da VF9 ao mesmo tempo).
4. **Tom sóbrio.** Sem adjetivos sobre o juízo e sem defesa, em tese, da advocacia de massa ou
   das práticas do escritório. Cobrar as condições do Tema 1198 no caso concreto, e só.

**Passo zero, obrigatório (antes de qualquer ataque):** levantar nos autos, com ID e página, (i) a
exigência feita, sua fundamentação e o prazo; (ii) o que o autor fez em resposta; (iii) se a sentença
aponta outras ações do autor e se são sobre o MESMO contrato (duplicidade real: viabilidade FRACA) ou
sobre contratos diferentes. Resultado só para o cartão de pausa (trava 2). Nunca afirmar que não
há outras ações sem que os autos o mostrem.

**Ataque:**
- **Tema 1198/STJ fixa as condições, e a sentença precisa cumpri-las.** A exigência extra só cabe
  diante de *indícios* de litigância abusiva, com decisão *fundamentada*, razoável no caso concreto
  e respeitando a distribuição do ônus da prova. Exigência genérica, de modelo, igual para todos os
  processos do escritório, não aponta indício do caso: é exigência sem fundamento (art. 93, IX, CF;
  art. 489, § 1º, CPC). E a parte final da tese impede usar a exigência para transferir ao autor o
  ônus que é do banco (art. 14, § 3º, CDC; art. 429, II, CPC).
- **Autenticidade da postulação já demonstrada nos autos.** Só com o que a exigência pediu e o autor
  cumpriu (documento de identidade, comprovante de residência, comparecimento, emenda), com ID e
  página. Se a exigência foi cumprida e a sentença extinguiu mesmo assim, é erro manifesto. Nada
  sobre como a procuração foi colhida (trava 3).
- **Súmulas 46, 47, 52 e 54 pressupõem ações semelhantes ou idênticas, com vantagem indevida.** A
  sentença precisa apontar, no caso, quais ações e qual vantagem; sem isso, não há o pressuposto.
  O argumento de que contratos diferentes não configuram fracionamento é DISPUTADO: só usar se a
  sentença acusou fracionamento expressamente, falando do caso concreto (este contrato, seus
  descontos e documentos próprios), nunca da prática de ajuizar uma ação por contrato.
- **Súmula 53 trata de "casos suspeitos de fraude"** da parte autora; aqui a fraude alegada é contra o
  autor, praticada no contrato do banco. Não confundir a fraude que o processo apura com suspeita
  sobre quem a denuncia.
- **Súmula 51** autoriza exigir documento idôneo quando o juntado é desatualizado, ilegível ou
  adulterado; não autoriza extinguir sem antes indicar o defeito e dar prazo (art. 321, CPC).
- **Multa por má-fé (Súmula 42).** A súmula exige que "restar provado" o negócio e a
  "disponibilização de seu numerário". Se a VF6 mostra divergência TED × LIBERADO, portabilidade
  sem troco ou crédito não comprovado, a premissa cai. Má-fé exige dolo, não se presume; negar
  autoria de documento cuja autenticidade se impugna é exercício do direito de ação. Pedir, no
  mínimo, o afastamento da multa, mesmo se mantida a improcedência.
- **Volume de ações do escritório:** se a sentença o usou, responder só que a tese do Tema 1198
  exige indício no caso concreto, sem discutir números nem a atuação do escritório. [Votos do
  julgamento disseram que o número de ações não basta, mas isso não está na tese; não citar.]

**Rito.** JEC: a extinção sem mérito (art. 51, Lei 9.099/95) desafia recurso inominado; pedir a
anulação e o retorno para instrução, ou o julgamento do mérito se a causa estiver madura. Justiça
Comum: apelação contra sentença terminativa (art. 485, CPC); pedir a cassação e, estando a causa em
condições, o julgamento imediato do mérito (art. 1.013, § 3º, I, CPC).

**Viabilidade:** FORTE quando a exigência foi cumprida, ou quando a decisão não apontou indício
concreto do caso; MÉDIA quando a exigência era fundamentada mas desproporcional, ou foi cumprida em
parte; FRACA quando a sentença aponta ação anterior sobre o MESMO contrato, ou exigência clara,
fundamentada e ignorada pelo autor. Multa por má-fé: FORTE se a VF6 derruba a premissa da Súmula
42; FRACA se o crédito integral chegou à conta do autor sem nenhum indício técnico de fraude.
**FSC12 FRACA → ALERTA no cartão de pausa:** recomendar não recorrer ou limitar o recurso à multa
por má-fé (se houver premissa para atacá-la). Recurso fraco nesse tema expõe o autor a multa
mantida ou majorada e o escritório a mais escrutínio.

---

## PARTE 3 — Viabilidade e exposição

Duas perguntas separadas, respondidas cada uma por si no cartão de pausa:

- **Viabilidade** (FORTE, MÉDIA, FRACA): qual a chance de o recurso reverter a sentença.
- **Exposição** (BAIXA, MÉDIA, ALTA): quanto custa ao autor perder.

Um caso pode ser forte e caro, ou fraco e barato. Uma resposta não substitui a outra.

### 3.1 Viabilidade por fundamento

Atribuir cada nível por critério verificável nos autos, com uma linha de
justificativa e ID e página do achado que a sustenta.

| Fundamento | Papel na agregação | FORTE quando | MÉDIA quando | FRACA quando |
|---|---|---|---|---|
| FSC1 assinatura a olho | autônomo | (sem hipótese forte isolada no catálogo) | há outras assinaturas do autor nos autos reforçando a divergência | no JEC, sem contraponto documental (discurso contra discurso); ou assinatura manuscrita comparável e sem outro vício técnico |
| FSC2 múltiplas camadas | autônomo | indício técnico concreto (e-mail ou telefone de terceiro, campo vazio, log sem IP público); VF9 com divergência de GPS, ponto recorrente fora da residência ou GPS incompatível entre si; autenticação sem perícia e sem contraponto documental do réu | log descrito tecnicamente, mas não auditado a fundo | nenhum IP interno nem geolocalização incompatível para contrapor |
| FSC3 ônus da prova | autônomo | recusa da inversão sem base concreta (erro de direito) | | |
| FSC4 proveito econômico | autônomo | VF6 revela divergência de valores, LIBERADO zerado ou portabilidade disfarçada (FORTE ou MÉDIA, conforme o achado) | | valor recebido integralmente compatível, sem indício de portabilidade pura ou divergência |
| FSC5 cessão | autônomo | ausente qualquer instrumento de cessão | intermediário: um dos eixos ausente ou frágil (avaliar caso a caso e justificar) | cessão formalmente completa (eixos EXISTÊNCIA e EFICÁCIA) e a sentença apenas a resumiu |
| FSC6 impugnação tardia | autônomo | | argumento sólido em tese, mas juízos tendem a repeti-lo; reforçar com a mecânica do desconto automático | |
| FSC7 não impugnação específica | qualificador, não pontua | | | |
| FSC8 dano moral | consequente (linha própria) | | parte das Turmas e Câmaras resiste ao dano in re ipsa puro; a natureza alimentar do desconto eleva a chance | |
| FSC9 cerceamento (só Justiça Comum) | via alternativa | perícia expressamente requerida e ignorada | requerimento genérico ou tardio | |
| FSC10 correspondente, IP, geolocalização | eleva FSC2 | indício objetivamente verificável (correspondente em outro estado sem credenciamento comprovado; localização divergente) | | |
| FSC11 contratos na mesma data | reforço, não pontua | | reforça outros fundamentos, raramente decide sozinho | |
| FSC12 litigância predatória / exigências / má-fé | autônomo (na extinção sem mérito, é a única linha do mérito recursal) | exigência cumprida; ou decisão sem indício concreto do caso; Súmula 42 sem a premissa (VF6) | exigência fundamentada mas desproporcional, ou cumprida em parte | ação anterior sobre o MESMO contrato; exigência clara ignorada; crédito integral recebido sem indício técnico |

### 3.2 Como agregar

1. Só entram os fundamentos que são *ratio decidendi*, isto é, que sozinhos ou em
   conjunto sustentam a improcedência (identificados na ETAPA 2-A). Reforço
   retórico da sentença não entra, embora deva ser atacado se houver espaço.
2. **Viabilidade do mérito = a do elo mais fraco** entre os fundamentos
   autônomos (FSC1 a FSC6 e FSC12) que a sentença usou como *ratio*. Na extinção sem mérito,
   a viabilidade é a do FSC12; a multa por má-fé tem linha própria. Para reverter, é
   preciso derrubar todos os que sozinhos sustentam a improcedência.
3. FSC10 e FSC11 não pontuam à parte: já aparecem nos critérios de FSC2 e FSC5.
4. FSC7 não pontua. Funciona como alerta: exige impugnação específica minuciosa.
5. FSC9 (só Justiça Comum) é via alternativa de anulação. Se for FORTE, registrar
   no cartão ao lado do mérito, sem alterar a viabilidade do mérito.
6. **Dano moral (FSC8)** tem linha própria. Na sentença parcial é a única linha.

### 3.3 Exposição

Entradas: rito, gratuidade (deferida, indeferida ou não comprovada nos autos),
valor da causa ou da condenação e honorários já fixados.

| Nível | Quando |
|---|---|
| BAIXA | gratuidade deferida e extensível ao recurso (a sucumbência fica com exigibilidade suspensa, art. 98, § 3º, CPC; se isso se aplica ao art. 55 da Lei 9.099/95 é posição do advogado, que decide no cartão) |
| MÉDIA | sem gratuidade, com sucumbência estimada abaixo do valor de corte definido pelo advogado (**pendência: R$ ___**) |
| ALTA | sem gratuidade e sucumbência estimada igual ou acima do corte; ou gratuidade indeferida, revogada ou não comprovada nos autos (por precaução) |

Estimar a sucumbência em reais e mostrar no cartão. JEC: 10 a 20% do valor da
condenação ou, sem condenação, da causa (art. 55, Lei 9.099/95). Justiça Comum:
majoração dos honorários já fixados na sentença (art. 85, § 11, CPC), sem ultrapassar, somados, o limite de 20% do
art. 85, § 2º, CPC. Sem valor de causa ou condenação nos
autos, pedir o dado ao advogado.

### 3.4 Matriz de alerta

| Viabilidade \ Exposição | BAIXA | MÉDIA | ALTA |
|---|---|---|---|
| FORTE | Recorrer | Recorrer | Recorrer, informando o custo possível |
| MÉDIA | Recorrer com ressalva ao autor | Recorrer com ressalva ao autor | ALERTA: ciência expressa do autor |
| FRACA | ALERTA: ciência expressa do autor | ALERTA: ciência expressa do autor | ALERTA: tende a não recorrer; só com decisão expressa do autor |

ALERTA é um bloco em caixa alta no cartão de pausa, antes do pedido de
confirmação. Se a viabilidade for FRACA em qualquer linha (mérito ou dano moral),
vale o alerta mesmo que as outras linhas sejam melhores. A matriz e o valor de
corte são propostas a validar pelo advogado.

> **JEC:** sucumbência recursal é risco inexistente no 1º grau (art. 55, Lei
> 9.099/95, 10 a 20%). **Justiça Comum:** honorários recursais se somam aos já
> fixados na sentença (art. 85, § 11, CPC). Explicitar o risco ao autor, com o
> valor estimado.

---

## PARTE 4 — Observações estratégicas transversais

1. **A fragilidade pode estar na sentença OU na réplica anterior (ou nas
   duas).** Quando a sentença registra "não impugnado especificamente" (FSC7),
   o recurso precisa fazer, agora, o trabalho que a réplica não fez —
   reexame forense completo dos documentos do réu (VF1 a VF9), sempre ancorado
   no que já está nos autos.
2. **O diferencial do consignado frente à conta fraudulenta comum é a
   natureza alimentar da verba.** Isso fortalece o dano moral (FSC8) e também
   argumenta contra o "silêncio"/"impugnação tardia" (FSC6): o consumidor não
   tem como impedir o desconto na origem, só descobri-lo depois.
3. **Precedentes.** Só citar afirmativamente os que constarem de
   `referencias_juridicas.md` ou dos próprios autos (inclusive os que a
   sentença usou contra — servem para confronto/distinguishing). Qualquer
   outro entra marcado **[VERIFICAR ANTES DE PROTOCOLAR]**.
4. **Prazo e preparo.** JEC: 10 dias úteis (arts. 42 e 12-A, Lei 9.099/95), preparo em 48h
   salvo gratuidade. Justiça Comum: 15 dias úteis (art. 1.003, § 5º, CPC),
   preparo conforme lei estadual de custas, salvo gratuidade. Tempestividade presumida (não perguntar
   data de ciência). Sem gratuidade nos autos, pedir no recurso (art. 99, caput e § 7º, CPC).

---

## PARTE 5 — Índice das sentenças analisadas (calibração)

| # | Autor | Réu | Vara | Desfecho | Fundamentos | Viabilidade |
|---|---|---|---|---|---|---|
| 1 | Geraldo Joaquim Cruz Neto | (banco não identificado no trecho lido) | 3ª VSJ Ilhéus | Improc. total | FSC1, FSC4, FSC7 | MÉDIA ou FRACA (depende de contraponto documental à assinatura) |
| 2 | Gildásio Antônio de Souza | Banco do Estado do RS S.A. (Banrisul) | 3ª VSJ Ilhéus | Improc. total | FSC2, FSC3, FSC4, FSC5, FSC6, FSC8 | MÉDIA (reexame técnico do log pode subir para FORTE) |

> Padrão observado até aqui: 3ª VSJ Ilhéus (juízas leigos diversos, juízas de
> direito Raquel Ramires François e Théa Cristina Muniz Cunha Santos) tende a
> aceitar a documentação técnica do réu (assinatura, biometria, TED) como
> suficiente quando a réplica não impugna especificamente cada elemento — e a
> negar a inversão do ônus por "falta de verossimilhança" mesmo em relação de
> consumo. Catálogo a ser enriquecido a cada nova sentença mandada para
> calibração.
