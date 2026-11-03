# Fontes e limites da skill de recurso

Data da consulta: 29/10/2026. A skill tem duas camadas de fonte:

1. `references/referencias_juridicas.md`: lista autorizada de dispositivos e precedentes para o recurso, com a seção
   "Decisões do escritório que prevalecem" (alinhamento de 29/10/2026).
2. `references/normas/` e `references/jurisprudencia/`: cópias do acervo do pacote de consignado (o mesmo texto usado
   na inicial e na réplica). Súmulas do STJ e do TJBA vêm daqui.

| Item | Situação |
|---|---|
| Tema 929/STJ | não citar como fundamento (D7) |
| Tema 1414/STJ | afetado, sem tese; suspensão nacional (exceto cumprimentos de sentença) |
| IN 138/2022 | vigência adotada em 13/12/2022 (D30) |
| Marco da biometria | `[CONFERIR]` pela regra de contagem do escritório (D3) |
| Geolocalização e figuras | scripts e arquivos do mapa **congelados** (`testes/mapa/congelados.json`); limiares definidos pelo advogado, sem calibração com logs reais; figuras B e C exigem `regiao.pmtiles` e Playwright no Cowork |
| Lei 14.063/2020 e MP 2.200-2/2001 | no acervo desde 01/11/2026 (Planalto; 0 parágrafos ausentes nas duas passadas); a Lei 14.063 só por analogia na relação privada |
| Precedentes que as sentenças invocam contra (REsp 1.881.131, AgRg no Ag 955.934, 1ª Turma Recursal/BA) | **fora do acervo**; citar só como constam da sentença recorrida |
| Calibração do catálogo FSC | 2 sentenças (Ilhéus); ficha em `references/calibracao/ficha-de-sentenca.md` |
