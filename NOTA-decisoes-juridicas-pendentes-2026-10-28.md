# Nota: decisões jurídicas que ainda dependem do escritório, por tese (28/10/2026)

Complementa `NOTA-decisoes-juridicas-2026-10-28.md` (Súmula 41, juros, Enunciado 162 e D25, já aplicados). Aqui está o que **falta decidir ou confirmar**, separado pela tese a que a decisão pertence. O registro vivo está em `_manutencao/PAINEL.md`. Fontes consultadas em 28/10/2026.

## Atualização de 29/10/2026: respostas do escritório e o que foi aplicado

| Decisão | Resposta do escritório | Aplicado |
|---|---|---|
| D3, D5 | confirmar o marco da biometria; manter o LGPD art. 37 como analogia | sem mudança nos modelos |
| D1 | no RMC só o mínimo da fatura é consignado (o resto é por boleto); o art. 4º da Res. CMN 4.549 não afasta a resolução; manter pela Lei e fundamentar também na resolução | `rmc/`: modelo, SKILL, referências; alerta no script pedindo conferir o boleto nas faturas |
| D19 | manter a tese do teto; não seguir pela nulidade por vício de informação | B2 deixou de bloquear e virou alerta; argumento do trato sucessivo no modelo, com `[VERIFICAR]` |
| D20, D21 | aceitar o limite do cartão como capital; manter os pedidos subsidiários | sem mudança |
| D25 | a tese não se enquadra na suspensão do Tema 1414; manter o prosseguimento por distinção | tópico passou a ser incondicional |
| D8 | não falar da MP 1.393/2026 | verificador reprova a citação |
| D29 | na Tese 1000 não há reaverbação por outro banco | tópico da troca de titularidade retirado do modelo; o script alerta "fora do escopo" |
| D30 | publicação da IN 138 conferida no DOU pelo escritório: 13/12/2022 (art. 40: vigência no ato da publicação) | quatro skills, scripts, testes e peças de exemplo (IN 28 até 12/12/2022) |
| D31 | não sustentar "não havia crédito a migrar"; só a cessão não notificada; consultar petição nova, mais robusta | argumento retirado do migrado; verificador o reprova; **petição nova ainda não localizada** |
| D32 | manter sem o contexto de fraude | sem mudança |
| D7 | não usar o Tema 929 como fundamento | retirado dos quatro modelos, scripts e padrão de peças; verificador reprova |
| D28 | pedir acesso a Lucas sobre as mudanças no modelo | **pendente** |

Observação sobre D30: a primeira resposta do escritório foi 01/12/2022; depois, conferido o DOU, a data passou a 13/12/2022 (republicação), que é a que decorre do art. 40. A edição original (DOU de 11/11/2022) saiu com incorreções.

Observação sobre D1 e D25: o art. 2º-D da Res. CMN 4.549 limita o teto a operações posteriores ao prazo de 90 dias (01/01/2024), e a questão II.b do Tema 1414 trata do prolongamento da dívida frente aos juros do refinanciamento. Ambos continuam sendo os pontos em que o banco ataca; a peça os enfrenta com `[VERIFICAR ANTES DE PROTOCOLAR]`.

As seções abaixo mantêm o texto original, para o histórico.

| Tese | Decisões | Efeito se ficarem sem resposta |
|---|---|---|
| 1. Não contratado (`nao-contratado`) | D3, D5, D18 | peça sai com `[CONFERIR]` |
| 2. RMC / refinanciamento (`rmc`) | D1, D19, D20, D21, D25, D8 | minuta **bloqueada** (D19); `[DECISÃO D1]` |
| 3. Tese 1000 (`tese-1000`) | D28, D29, D30 | skill já aplica as mudanças; troca de titularidade fica `[VERIFICAR]` |
| 4. Migrado (`migrado`) | D31, D32, D30 | peça usa a tese nova, sem precedente |
| 5. Transversais (todas) | D30, D7, D18, D26, D27 | ver seção 5 |

Cada decisão traz: problema, o que a skill faz hoje, opções e recomendação.

---

## 1. Não contratado

As decisões D4 (Súmula 326/STJ) e D6 (art. 400 do CPC no lugar de "inexistência confirmada") já foram aplicadas. Restam três confirmações.

### D3. Biometria da IN 138
- **Problema.** O argumento "sem biometria a partir de jan/2023 descumpre a IN" não se sustenta: a IN 143/2023 prorrogou por 60 dias, contados do DOU de 13/02/2023, os prazos do art. 38 da IN 138, e o art. 5º, § 11 admite "acesso autenticado" na contratação direta ou por canais eletrônicos.
- **Skill hoje.** Trata a biometria com `[CONFERIR]` e prevê o acesso autenticado.
- **Decisão pedida.** Confirmar o cálculo do novo marco pela regra de contagem do escritório.

### D5. LGPD, art. 37, como base da guarda da trilha de auditoria
- **Problema.** Extensão frágil: o artigo trata do registro das operações de tratamento, não da guarda de trilha de consignado.
- **Skill hoje.** Mantém como analogia marcada.
- **Decisão pedida.** Manter como analogia ou retirar. Recomendação: retirar, o CPC (arts. 396 a 404) e o CDC (art. 6º, VIII) já sustentam a exibição.

### D18. Extrato real
- **Problema.** O `extrato.py` foi herdado do AMN e testado aqui só com extrato fictício.
- **Decisão pedida.** Rodar com um PDF real do INSS e comparar a leitura com o PDF. Vale para as quatro skills.

---

## 2. RMC / refinanciamento

### D1. O cartão consignado fora da Res. CMN 4.549 (art. 4º)
- **Problema.** O art. 4º diz que a resolução "não se aplica aos cartões de crédito ... cujos contratos prevejam pagamento das faturas mediante consignação em folha". Os arts. 2º-A a 2º-D (onde está o marco de 200%) são dessa resolução. O banco dirá que o art. 2º-C não alcança o RMC. As petições do AMN citavam "art. 2º-C da Res. 5.112", citação errada que o verificador agora reprova.
- **Skill hoje.** Sustenta o teto no **art. 28, § 1º, da Lei 14.690/2023**, que não traz a exceção, e usa a resolução só como apoio. Responde à condição do § 1º dizendo que o CMN não aprovou limite para o cartão consignado, porque o art. 4º o excluiu. É tese do escritório, sem precedente no acervo.
- **Opções.** (a) manter pela lei, com `[DECISÃO D1]` e `[VERIFICAR]`; (b) retirar o teto de 200% e pedir só nulidade e restituição; (c) outro enquadramento (CDC, art. 51).
- **Recomendação.** (a). O § 1º é lei e a resolução não a restringe. Pesquisar acórdão do TJBA antes de protocolar. Decidir junto com a D25.

### D19. Refinanciamento anterior a 01/01/2024
- **Problema.** O § 1º vale se os limites não forem aprovados em 90 dias da publicação (DOU de 03/10/2023). O art. 2º-D da Res. 4.549 limita o teto às operações posteriores a esse prazo, que terminou em 01/01/2024 pela contagem simples `[VERIFICAR a contagem]`. A petição AMN de referência tem refinanciamento de 10/2023 e marco de 200% de 03/2023.
- **Skill hoje.** O script grava o bloqueio B2 e a minuta sai `BLOQUEADO PARA USO FINAL`.
- **Opções.** (a) tese do teto só para refinanciamentos a partir de 01/01/2024, e nulidade por vício de informação (CDC, arts. 6º, III, e 52) para os anteriores; (b) manter a tese do teto assumindo o risco.
- **Recomendação.** (a), com conferência da contagem do prazo. A peça com (b) tende a ser rejeitada pelo texto do art. 2º-D.

### D20. Capital = limite do cartão
- **Problema.** O art. 2º-A, IV, define valor original como o saldo da operação de crédito; a skill adota o limite do cartão como premissa.
- **Skill hoje.** Declara a premissa e pede as faturas.
- **Decisão pedida.** Aceitar a premissa declarada.

### D21. Pedidos subsidiários de lesão (CC, art. 157) e de revisão
- **Skill hoje.** Vêm do modelo AMN e ficam `[DECISÃO DO ADVOGADO]`.
- **Decisão pedida.** Manter, retirar ou deixar por caso.

### D25. Tema 1414/STJ e a suspensão nacional
- Já descrita na seção 4 da nota anterior (ajuizar e pedir prosseguimento por distinção, ajuizar e aceitar a suspensão, ou aguardar). **Pendente.** Decidir junto com a D1.

### D8. MP 1.393/2026
- Em vigor, **não convertida** (deliberação de 25/09 a 23/11/2026). Alterou a Lei 14.690 (art. 28-A) e o CDC (art. 57), sem tocar o art. 28, § 1º. **Reconsultar a partir de 23/11/2026.**

---

## 3. Tese 1000

### D28. As 18 mudanças em relação ao modelo Maria x BNP
- **Problema.** O modelo aplica a IN 138/2022 a reaverbação de 2018 e afirma "barreira técnica da Dataprev", prática "sistêmica" do banco, dano *in re ipsa* e prazo decenal pelo EAREsp 676.608, que não foi localizado em fonte.
- **Skill hoje.** Norma pela data (IN 28 até 10/11/2022); retira as afirmações sem fonte; dano pela Súmula 40/TJBA; dano moral de R$ 20.000,00; multa de R$ 500,00.
- **Decisão pedida.** Confirmar a lista em `tese-1000/references/02-mudancas-no-modelo.md` (18 linhas e a 19ª, troca de titularidade). Se discordar de uma linha, indicar o número.

### D29. Troca de titularidade: o banco atual responde pelos descontos do anterior?
- **Problema.** Contrato reaverbado em outro banco. O acervo não tem precedente.
- **Skill hoje.** O script mede a norma pela primeira averbação em qualquer banco e **não soma** os descontos do outro banco sem a decisão (`--incluir-outros-bancos`). O modelo traz tópico condicional (IN 138, art. 4º, XVI; CDC, art. 7º, parágrafo único, e art. 25, § 1º).
- **Opções.** (a) pedir só os descontos do banco réu (padrão); (b) incluir os do banco anterior pela cadeia de fornecimento; (c) ajuizar contra os dois bancos.
- **Recomendação.** (a) como padrão, (c) quando o valor justificar; (b) sem precedente expõe a condenação a ilegitimidade.

### D30. Vigência da IN 138 (ver seção 5): decide o intervalo de 11/11 a 30/11/2022.

---

## 4. Migrado

### D31. A tese
- **Problema.** O modelo anterior dizia que nenhuma norma autoriza a migração sem novo consentimento. A IN 138, art. 11, **autoriza** a cessão "desde que atenda às normas do BCB e do CMN", e a IN 28, art. 56, remete à Res. CMN 2.836/2001 (fora do acervo).
- **Skill hoje.** Reconhece que a norma admite a cessão e sustenta que (i) **não havia crédito a migrar**, porque o contrato de origem não existia, e (ii) a cessão não foi notificada ao devedor (CC, arts. 286 e 290). Sem precedente no acervo.
- **Opções.** (a) manter a tese nova; (b) voltar à tese antiga (desmentida pelo texto da norma); (c) pesquisar acórdão do TJBA sobre migração antes de protocolar.
- **Recomendação.** (a) com (c). Confirmar também as 23 mudanças em `migrado/references/02-mudancas-no-modelo.md`: retirada da Res. CMN 4.753/2019 (conta de depósitos, antiga D2), retirada do Acórdão TCU 1.094/2026, honorários só em Justiça Comum.

### D32. Contexto de fraude em escala
- **Problema.** O modelo anterior abre com "Operação Sem Desconto" (R$ 6,3 bilhões; 97%), suspensão de averbações pela Dataprev e Acórdão TCU. A operação apurou **descontos de mensalidades associativas**, não consignados; o restante não foi confirmado.
- **Skill hoje.** Não usa; o verificador reprova a expressão.
- **Decisão pedida.** Manter sem o contexto (recomendado) ou reintroduzir com fonte correta (relatório do TCU ou da CGU, lido por inteiro).

### Precedentes de honorários (tópico só em Justiça Comum)
- **REsp 2.168.312/PR.** Lido o **Informativo 875/STJ** no portal do STJ (3ª Turma, Rel. Min. Humberto Martins, j. 03/11/2025, DJEN 06/11/2025). Tese: o art. 85, § 2º, do CPC não impede somar condenação e proveito econômico. O acórdão em si não foi lido; falta conferir a ementa.
- **REsp 2.062.421/SP.** Citado no modelo anterior, **não localizado** em nenhuma fonte; retirado. Se o escritório tiver o número correto, enviar o acórdão.

---

## 5. Transversais (todas as teses)

- **D30. Vigência da IN 138 (11/11 ou 01/12/2022).** A petição Francisco x Agibank adota IN 28 até 30/11/2022 e IN 138 desde 01/12/2022, sem fonte. O art. 40 da IN 138 diz que ela "entra em vigor no ato da publicação" (DOU de 11/11/2022, republicada em 13/12/2022). As skills usam 11/11/2022 com `[CONFERIR]`; só os contratos de 11/11 a 30/11/2022 mudam de norma. Opções: (a) 11/11/2022 (recomendado); (b) 01/12/2022, se houver fonte (ato do INSS que diferiu a vigência); (c) citar as duas normas no intervalo. Abrir o DOU de 11/11 e de 13/12/2022 para ver se a republicação mudou a vigência.
- **D7. Tema 929/STJ.** Tese ainda não publicada; toda citação sai com `[VERIFICAR ANTES DE PROTOCOLAR]`. Acompanhar.
- **D18. Extrato real do INSS** (ver seção 1).
- **D26. Cadastro de réus.** 13 bancos novos em `reus.json`: conferir CNPJ e endereço no cartão CNPJ da Receita. O cadastro do Itaú (341) vem da petição do Itaucard.
- **D27. FONAJEF.** Faltam as Recomendações, as Sugestões ao GT do CNJ e o resultado da consolidação de 2025. Só serve a processo da Caixa em Juizado Especial Federal.

---

## Para você decidir (resumo por tese)

1. **Não contratado:** D3 (marco da biometria), D5 (retirar LGPD art. 37?), D18.
2. **RMC:** D1 (teto pela lei), D19 (aceitar o bloqueio antes de 01/01/2024), D20, D21, D25.
3. **Tese 1000:** D28 (18 mudanças), D29 (só o banco réu?).
4. **Migrado:** D31 (tese nova e 23 mudanças), D32 (sem o contexto de fraude).
5. **Todas:** D30 (data da IN 138).
