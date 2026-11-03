'use strict';
// Normalização de texto usada para comparar transcrições com o acervo.
// norm: ignora espaços, marcas de revogação (~~), pipes, ênfase e maiúsculas; º/° viram "o" e travessões viram "-".
// soLetras: só letras, sem acento; pega diferença de quebra de linha, pontuação e numeração.
const norm = s => s.replace(/~~/g, '').replace(/[|*_`]/g, '').replace(/[º°]/g, 'o').replace(/[–—−]/g, '-').replace(/[\s ]+/g, '').toLowerCase();
const soLetras = s => s.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-zA-Z]/g, '').toLowerCase();
module.exports = { norm, soLetras };
