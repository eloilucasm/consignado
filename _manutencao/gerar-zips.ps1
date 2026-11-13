# Gera um zip por skill, com a pasta da skill na raiz do zip (formato de upload de skills do Claude).
#
# Uso (PowerShell, a partir da pasta do pacote):
#   powershell -ExecutionPolicy Bypass -File _manutencao\gerar-zips.ps1 -Saida _entrega
#   powershell -ExecutionPolicy Bypass -File _manutencao\gerar-zips.ps1 -Saida C:\temp\zips -Skills rmc,migrado
#
# Pasta de saída padrão: zips-por-skill\ dentro do pacote. Recria os zips pedidos; não mexe nas skills.
# Usa o tar.exe do Windows 10+ (o "tar" do Git Bash falha em caminhos do Windows).
#
# Carimbo de versão (desde 13/11/2026): no zip, o fim da "description" de cada SKILL.md recebe
#   " Pacote consignado DD/MM/AAAA (abc1234)."  -> data da geração e commit atual do repositório;
#   " Pacote consignado DD/MM/AAAA (abc1234 + alterações não commitadas)."  -> a pasta da skill tem mudança fora do commit.
# O carimbo vai só na cópia que entra no zip: os arquivos do repositório não mudam.
#
# Trava contra cópia desatualizada: antes de gerar, consulta o GitHub (git fetch). Se a cópia local estiver atrás
# do que foi publicado, para sem gerar nada. Sem internet, avisa e segue. -SemConferirGitHub pula a consulta.
param(
  [string]$Raiz = (Split-Path $PSScriptRoot -Parent),
  [string]$Saida = (Join-Path (Split-Path $PSScriptRoot -Parent) 'zips-por-skill'),
  [string[]]$Skills,
  [switch]$SemConferirGitHub
)
$ErrorActionPreference = 'Stop'
Set-Location $Raiz
if (-not [IO.Path]::IsPathRooted($Saida)) { $Saida = Join-Path $Raiz $Saida }
$utf8 = New-Object System.Text.UTF8Encoding($false)

# ---- 1. Trava: a cópia local não pode estar atrás do GitHub
$ramo = (git rev-parse --abbrev-ref HEAD).Trim()
if (-not $SemConferirGitHub) {
  $eap = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
  git fetch origin --quiet 2>&1 | Out-Null
  $ok = ($LASTEXITCODE -eq 0); $ErrorActionPreference = $eap
  if (-not $ok) {
    Write-Warning "Não foi possível consultar o GitHub (sem internet ou sem acesso). Os zips saem sem essa conferência."
  } else {
    $atras = [int](git rev-list --count "HEAD..origin/$ramo")
    if ($atras -gt 0) {
      throw "Esta cópia está desatualizada: o GitHub tem $atras commit(s) que ela não tem (ramo $ramo). Atualize (git pull) antes de gerar os zips. Nada foi gerado."
    }
  }
}

# ---- 2. Carimbo
$hash = (git rev-parse --short HEAD).Trim()
$data = Get-Date -Format 'dd/MM/yyyy'

function Carimbar([string]$arquivo, [string]$carimbo) {
  $txt = [IO.File]::ReadAllText($arquivo, $utf8)
  $nl = if ($txt.Contains("`r`n")) { "`r`n" } else { "`n" }
  $linhas = $txt -split "`r?`n"
  if ($linhas[0].Trim() -ne '---') { throw "$arquivo sem frontmatter" }
  $fim = -1
  for ($i = 1; $i -lt $linhas.Count; $i++) { if ($linhas[$i].Trim() -eq '---') { $fim = $i; break } }
  if ($fim -lt 0) { throw "$arquivo com frontmatter sem fechamento" }
  $d = -1
  for ($i = 1; $i -lt $fim; $i++) { if ($linhas[$i] -match '^description:') { $d = $i; break } }
  if ($d -lt 0) { throw "$arquivo sem description" }
  $valor = ($linhas[$d] -replace '^description:\s*', '').TrimEnd()
  if ($valor -match '^[>|][-+]?$') {
    # bloco dobrado (description: >): acrescenta na última linha indentada do bloco
    $u = $d
    for ($i = $d + 1; $i -lt $fim; $i++) { if ($linhas[$i] -match '^\s+\S') { $u = $i } else { break } }
    if ($u -eq $d) { throw "$arquivo com description em bloco vazio" }
    $linhas[$u] = $linhas[$u].TrimEnd() + $carimbo
    $texto = (($linhas[($d + 1)..$u] | ForEach-Object { $_.Trim() }) -join ' ')
  } elseif ($valor.Length -ge 2 -and $valor.StartsWith('"') -and $valor.EndsWith('"')) {
    $linhas[$d] = 'description: ' + $valor.Substring(0, $valor.Length - 1) + $carimbo + '"'
    $texto = $valor.Substring(1, $valor.Length - 2) + $carimbo
  } else {
    $linhas[$d] = 'description: ' + $valor + $carimbo
    $texto = $valor + $carimbo
  }
  if ($texto.Length -gt 1024) { Write-Warning "$arquivo : description com $($texto.Length) caracteres depois do carimbo (limite 1024)." }
  [IO.File]::WriteAllText($arquivo, ($linhas -join $nl), $utf8)
}

New-Item -ItemType Directory -Force -Path $Saida | Out-Null
$todas = Get-ChildItem -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } | Select-Object -ExpandProperty Name
if ($Skills) { $Skills = $Skills | ForEach-Object { $_ -split ',' } | Where-Object { $_ } } else { $Skills = $todas }
$tmp = Join-Path ([IO.Path]::GetTempPath()) ("gerar-zips-" + [Guid]::NewGuid().ToString('N').Substring(0, 8))
New-Item -ItemType Directory -Force -Path $tmp | Out-Null
try {
  foreach ($s in $Skills) {
    if ($todas -notcontains $s) { Write-Warning "Skill não encontrada: $s"; continue }
    $sujo = [bool](git status --porcelain -- $s)
    $marca = if ($sujo) { "$hash + alterações não commitadas" } else { $hash }
    $carimbo = " Pacote consignado $data ($marca)."
    Copy-Item -Recurse -Force (Join-Path $Raiz $s) (Join-Path $tmp $s)
    Carimbar (Join-Path $tmp "$s\SKILL.md") $carimbo
    $z = Join-Path $Saida "$s.zip"
    if (Test-Path $z) { Remove-Item $z -Force }
    tar.exe -a -c -f $z -C $tmp --exclude '~$*' --exclude '__pycache__' --exclude '*.pyc' $s
    $n = (tar.exe -tf $z | Where-Object { $_ -eq "$s/SKILL.md" }).Count
    '{0,-45} {1,6:N2} MB   SKILL.md na raiz: {2}   carimbo: {3}' -f $s, ((Get-Item $z).Length / 1MB), $n, $marca
  }
} finally {
  Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
