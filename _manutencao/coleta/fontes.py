"""Fontes de texto normativo: o que baixar, de onde, e como transformar em texto no formato do acervo.

Cada fonte tem dois passos independentes, para que a mesma norma possa ter uma fonte primária e uma
secundária (conferência) de tipos diferentes:

    obter(rede)        -> Documento   bytes brutos + metadados de proveniência (URL, HTTP, Last-Modified, sha256)
    extrair(documento) -> str         texto puro, um parágrafo por linha, linha em branco entre eles

Tipos implementados: `PdfHttp`. `BcbApi` (portal de normativos do Banco Central) e `DouHtml` (Imprensa
Nacional) estão declaradas, mas ainda sem endpoint confirmado: levantam `FontePendente`, que o
coletor trata como "pendente", nunca como aprovação. Para ligar uma delas basta implementar `obter` e
`extrair`; o registro, o manifesto, a comparação e o código de saída não mudam.
"""
import datetime as dt
import gzip
import hashlib
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comum import Limitador  # noqa: E402
import texto_pdf  # noqa: E402

# Cliente identificado. gov.br/inss responde 403 a este tipo de cliente; o coletor NÃO disfarça o
# User-Agent para passar (isso é contornar bloqueio). Fonte com 403 vira FonteErro e a norma entra
# por arquivo local (`--local`), baixado pelo escritório, com o sha256 registrado no manifesto.
CLIENTE = {
    "User-Agent": "acervo-coletor/1.0 (conferencia de normas; contato: escritorio)",
    "Accept": "application/pdf,text/html,application/json;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip",
}


class FonteErro(RuntimeError):
    """Falha de rede ou resposta inválida: a norma sai como ERRO, não como REPROVADA."""


class FontePendente(NotImplementedError):
    """Fonte declarada, ainda sem endpoint confirmado."""


@dataclass
class Documento:
    url: str
    bruto: bytes
    http: int
    content_type: str
    last_modified: str
    obtido_em: str
    sha256: str = field(init=False)

    def __post_init__(self):
        self.sha256 = hashlib.sha256(self.bruto).hexdigest()

    def meta(self):
        return {"url": self.url, "http": self.http, "content_type": self.content_type,
                "last_modified": self.last_modified, "obtido_em": self.obtido_em,
                "bytes": len(self.bruto), "sha256": self.sha256}


class Rede:
    """GET com limite de taxa, retentativa e cabeçalhos de resposta preservados.

    `comum.Rede` descarta os cabeçalhos; aqui `Last-Modified` entra no manifesto.
    """

    def __init__(self, rps=1, headers=None):
        self.limite = Limitador(rps)
        self.headers = {**CLIENTE, **(headers or {})}

    def get(self, url, headers=None, tentativas=4, timeout=120, referer=None):
        h = {**self.headers, **(headers or {})}
        if referer:
            h["Referer"] = referer
        req = urllib.request.Request(url, headers=h)
        ultimo = None
        for n in range(tentativas):
            self.limite.esperar()
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    dados = r.read()
                    if r.headers.get("Content-Encoding") == "gzip":
                        dados = gzip.decompress(dados)
                    return Documento(url, dados, r.status, r.headers.get("Content-Type") or "",
                                     r.headers.get("Last-Modified") or "",
                                     dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
            except urllib.error.HTTPError as e:
                if e.code in (400, 401, 403, 404, 410):  # repetir não adianta; 403 é o bloqueio do gov.br
                    raise FonteErro(f"HTTP {e.code}: {url}") from e
                ultimo = e
            except Exception as e:  # rede, IncompleteRead, timeout
                ultimo = e
            time.sleep(2 * (n + 1) ** 2)
        raise FonteErro(f"falhou após {tentativas} tentativas: {url}: {ultimo}")


class PdfHttp:
    """PDF com camada de texto, por URL fixa. PDF escaneado é recusado (sem OCR: fonte de menor confiança)."""

    tipo = "pdf"

    def __init__(self, url, referer=None):
        self.url, self.referer = url, referer

    def obter(self, rede):
        doc = rede.get(self.url, referer=self.referer)
        if not doc.bruto.startswith(b"%PDF"):
            raise FonteErro(f"resposta não é PDF (HTTP {doc.http}, {doc.content_type!r}, {len(doc.bruto)} bytes): {self.url}")
        return doc

    def extrair(self, doc):
        bruto = pdftotext(doc.bruto)
        if texto_pdf.escaneado(bruto):
            raise FonteErro(f"PDF sem camada de texto suficiente (provável escaneado; exigiria OCR): {doc.url}")
        return texto_pdf.para_acervo(bruto)


class PdfLocal(PdfHttp):
    """PDF já baixado pelo escritório (navegador), para fonte que bloqueia cliente automatizado.

    O caminho e o sha256 vão para o manifesto, marcados como `local`; `Last-Modified` fica vazio porque o
    servidor não foi consultado. Reaproveita `extrair` de `PdfHttp`.
    """

    tipo = "pdf-local"

    def __init__(self, caminho, url_origem):
        super().__init__(url_origem)
        self.caminho = caminho

    def obter(self, rede):
        with open(self.caminho, "rb") as f:
            bruto = f.read()
        if not bruto.startswith(b"%PDF"):
            raise FonteErro(f"arquivo local não é PDF: {self.caminho}")
        agora = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        return Documento(self.url, bruto, 0, "application/pdf", "", agora)


def pdftotext(pdf_bytes):
    """`pdftotext -layout -enc UTF-8`. Sem o `-enc`, o Windows grava Latin-1 e os acentos se perdem."""
    with tempfile.TemporaryDirectory() as tmp:
        caminho = os.path.join(tmp, "a.pdf")
        with open(caminho, "wb") as f:
            f.write(pdf_bytes)
        r = subprocess.run(["pdftotext", "-q", "-layout", "-enc", "UTF-8", caminho, "-"], capture_output=True, timeout=300)
    if r.returncode != 0:
        raise FonteErro(f"pdftotext falhou ({r.returncode}): {r.stderr.decode('utf-8', 'replace')[:200]}")
    return r.stdout.decode("utf-8")  # estrito: byte inválido aqui é erro, não texto trocado


class BcbApi:
    """Texto de um normativo pela interface de dados do portal do Banco Central (id + versão).

    PENDENTE: o endpoint real ainda não foi descoberto. `exibenormativo?tipo=...&numero=...` devolve uma
    casca de 2,8 KB que carrega o texto por JavaScript, e `/api/search/app/normativos/buscanormativo`
    respondeu 405 (HEAD) e "Requisição Inválida" (GET com consulta chutada). Descobrir a chamada que a
    página faz (aba Rede do navegador) e implementar aqui. Serve de fonte primária para 4935 e BCB 96 e
    de segunda fonte para 3954, 4549 e 4753.
    """

    tipo = "api-bcb"

    def __init__(self, tipo_norma, numero, id_portal=None):
        self.tipo_norma, self.numero, self.id_portal = tipo_norma, numero, id_portal

    def obter(self, rede):
        raise FontePendente(f"BcbApi({self.tipo_norma} {self.numero}): endpoint do portal ainda não confirmado")

    def extrair(self, doc):
        raise FontePendente("BcbApi.extrair")


class DouHtml:
    """Ato publicado no DOU (in.gov.br), segunda fonte das INs do INSS.

    PENDENTE: a página HTTP 200 e contém "Art. 1" (testado para a IN 143), mas falta isolar o corpo do ato
    do restante da página e tratar a paginação/versões. Implementar `extrair` com o oráculo HTML existente.
    """

    tipo = "dou"

    def __init__(self, url):
        self.url = url

    def obter(self, rede):
        raise FontePendente(f"DouHtml({self.url}): extração do corpo ainda não implementada")

    def extrair(self, doc):
        raise FontePendente("DouHtml.extrair")
