# Aprendizados deste projeto que valem para o kit de replicação

Colhidos em 28/10/2026 ao construir o pacote de consignado. Servem para o briefing (seção 14, "Erros que cometemos") e para os scripts do kit.

## Nos scripts

1. **`comparar-fonte.js`**: o comparador estrito acusou 105 parágrafos "ausentes" na Lei 10.741. Causa: o HTML do Planalto quebra o parágrafo em duas linhas e usa um traço que a normalização não cobre. Solução adotada: segunda passada só com letras, e só conta como ausente o que falha nas duas.
2. **Saída no Windows**: `print` de script Python, quando redirecionado, sai em cp1252. Todo script que escreve texto em português deve fazer `sys.stdout.reconfigure(encoding="utf-8")`.
3. **Verificador**: o teste "súmula ou tema citado existe" do kit exige o formato `## Súmula N` e `## Tema N`. Os arquivos reais vêm em outros formatos (`### SÚMULA 43`, `## Súmula nº 01`, arquivo `tema-929-stj.md`). A seção `extras` do verificador aceita esses formatos e separa por tribunal.
4. **Contagem de ocorrências é regra fraca**: exigir "R$ 20.000,00 três vezes" passou mesmo com um valor trocado, porque uma ementa citada também trazia R$ 20.000,00. A regra boa exige o valor **no contexto** (fundamentação, pedido e valor da causa) e é provada pelo teste.
5. **Provar a regra**: o teste do verificador achou essa brecha na primeira rodada. Rodar `testar-verificador.py` depois de cada regra nova.
6. **Número da peça vem do `calculo.json`**: o verificador confere que cada total, dobro e valor da causa que aparece na peça é o que o script calculou. Número digitado à mão é o erro que mais custa.
7. **Intervalo de busca de artigo**: a expressão "art. N … do CPC" não pode atravessar `;`, `.` ou `)`, ou liga um artigo de uma oração à norma de outra.

## Na construção

8. **O modelo do escritório pode não ser o que o nome diz.** O `.docx` chamado de "não contratado" era o texto de "migrado", e o motor trocava trechos por código. Ler o arquivo e o gerador juntos antes de decidir o que é fonte.
9. **Fonte pública com acesso automático bloqueado**: o portal de normativos do Banco Central tem interface de dados que devolve texto, id e status de revogação (`Revogado: falso`, normas vinculadas), mesmo quando a página pública só carrega por script. O STJ bloqueia download automático (403): usar páginas de tema e súmula pela ferramenta de busca e marcar a fonte secundária.
10. **Consolidação com nome enganoso**: o arquivo da IN 138 "alterada 19-5-2026" já incorporava a IN 213 de 17/8/2026. Conferir o texto, não o nome do arquivo.
11. **A revogação pode vir de norma de outro assunto**: a Res. CMN 3.954 (correspondentes) foi revogada pela Res. BCB 277 (câmbio), por lista no art. 86. Ler a norma revogadora.
12. **Citação "existe" não é citação "está certa"**: das 58 citações das skills do AMN, todas tinham arquivo no acervo no fim, mas várias estavam usadas para o fim errado (Súmula 326 para caráter punitivo; Res. CMN 4.753 para consignado; art. 4º da Res. CMN 4.549 afasta justamente o consignado). O teste de existência é só o piso; o resto é leitura jurídica.
13. **Ambiente**: `python3 -I` ignora o `site-packages` do usuário. Para ler arquivo não confiável com biblioteca instalada com `pip --user`, rode sem `-I` e evite executar código do arquivo.
14. **Erros meus de processo** (para o briefing): caminhos temporários na raiz do disco (bloqueados pela permissão); patch por heredoc com escapes duplicados que gravou caracteres de controle no lugar de `\b`. Gravar arquivo com a ferramenta de edição, não por heredoc com regex.
15. **O portal de repetitivos do STJ responde a `curl`** (`processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?novaConsulta=true&tipo_pesquisa=T&cod_tema_inicial=N&cod_tema_final=N`), em ISO-8859-1: decodificar como `iso-8859-1`, não como UTF-8. Traz situação, tese, anotações, suspensão e datas de cada recurso afetado. O que continua bloqueado é a página de súmulas (`scon.stj.jus.br`, desafio do Cloudflare). Rever o item 9, que dizia que o STJ bloqueia download automático.
16. **Fonte do forum importa:** para enunciados do FONAJEF, a lista do CJF (110) e a do TRF1 (138, de 2014) estavam defasadas; a página da Ajufe tinha os 226. Comparar a numeração máxima antes de adotar uma fonte.
