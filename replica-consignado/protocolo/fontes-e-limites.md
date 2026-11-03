# Fontes e limites da skill replica-consignado

Data da consulta: 29/10/2026. Níveis de confiança: VERIFICADO, FEITO, PRESUMIDO, ABERTO.

## 1. Normas

As mesmas do `nao-contratado` (cópias do acervo central, mesmo texto e mesma data): CPC, CDC, CC, LGPD, Lei 9.099/1995, Lei 10.741/2003, Lei 14.905/2024 (Planalto, integrais, VERIFICADO); IN INSS/PRES 28/2008 (consolidação de 22/7/2020), INs 131, 136 e 137 de 2022, IN PRES/INSS 138/2022 (consolidada, vigência adotada pelo escritório: 13/12/2022) e IN 143/2023 (gov.br/inss, FEITO); Res. CMN 4.935/2021 e 3.954/2011 original (Banco Central, FEITO).

Dispositivos centrais da réplica, conferidos no texto do acervo: CPC, arts. 3º, 99, §§ 2º e 3º, 341, 350, 351, 411, 412, parágrafo único, 428, 429, 430, 436, 437 e 489, § 1º, VI; CC, arts. 111, 169, 182, 286 a 290 e 368; CDC, arts. 6º, VIII, 14, § 3º, 27 e 42, parágrafo único; Lei 9.099/95, arts. 3º, 35 e 38.

## 2. Jurisprudência

As mesmas do `nao-contratado`, mais o Tema 1414/STJ (para o RMC). Destaques: Tema 1061/STJ (ônus da autenticidade), Súmula 479/STJ e Tema 466/STJ (fortuito interno), Tema 1198/STJ e Súmulas 42 e 46 a 54 do TJBA (litigância e exigências), Súmulas 30 e 40 do TJBA (dano), Enunciados 12, 54 e 70 do FONAJE (perícia informal, complexidade e perícia contábil; encontro e data `[CONFERIR]`), EAREsp 738.991/RS (prazo decenal, por analogia, `[VERIFICAR]`). **Tema 929/STJ: não citar** (decisão do escritório de 29/10/2026).

## 3. Scripts e dados

| Arquivo | Origem | Nível |
|---|---|---|
| `scripts/fichas.py` | escrito para esta skill; testado com caso fictício | FEITO |
| `scripts/escrutinio.py`, `scripts/extrato.py`, `scripts/valores.py` | acervo central do pacote | FEITO (o leitor do extrato só foi testado com extrato fictício: D18) |
| `scripts/geo_check.py`, `scripts/geo_malha.py`, `scripts/ip_check.py`, `scripts/catalogo_indicadores.json` | copiados sem alteração da skill de recurso inominado de consignado | FEITO; limiares (100 m, 150 m, 5 km) definidos pelo advogado naquela skill e ainda sem calibração com logs reais |
| `assets/ba_municipios.json` | Malha Municipal Digital do IBGE (2025), simplificada pela skill de recurso (tolerância de 40 m) | FEITO; ler a nota metodológica do IBGE antes de citar a fonte na peça |

## 4. O que NÃO está no acervo (limites da skill)

| Item | Tratamento |
|---|---|
| Modelo de réplica do escritório | não recebido; o modelo foi montado a partir da skill de recurso e do padrão de peças. Conferir com uma réplica real do escritório antes do uso |
| Figuras de geolocalização (mapas A, B e C) | ficam na skill de recurso; a réplica traz só o quadro do `geo_check.py` |
| Jurisprudência sobre IP privado, biometria sem relatório técnico e geolocalização | nenhuma no acervo; os argumentos são técnicos e do ônus da prova |
| Res. CMN 2.836/2001 (cessão, remissão da IN 28, art. 56) | está no acervo central e nas skills migrado e tese-1000, mas **não foi distribuída a esta**; distribuir com `sincronizar-acervo.js --incluir` antes de citar; até lá, `[CONFERIR]` |
| Escala de gravidade dos indícios | proposta herdada da skill de recurso, a validar pelo escritório |
| Prazo e forma da réplica no JEC | conforme o despacho do juízo; `[CONFERIR]` |
| Art. 369 do CC (requisitos da compensação) | citar só depois de conferir o texto no acervo |
