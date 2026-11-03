# Gera um zip por skill, com a pasta da skill na raiz do zip (formato de upload de skills do Claude).
#
# Uso (PowerShell, a partir da pasta do pacote):
#   powershell -ExecutionPolicy Bypass -File _manutencao\gerar-zips.ps1
#   powershell -ExecutionPolicy Bypass -File _manutencao\gerar-zips.ps1 -Saida C:\temp\zips -Skills rural,prev
#
# Pasta de saída padrão: zips-por-skill\ dentro do pacote. Recria os zips pedidos; não mexe nas skills.
# Usa o tar.exe do Windows 10+ (o "tar" do Git Bash falha em caminhos do Windows).
param(
  [string]$Raiz = (Split-Path $PSScriptRoot -Parent),
  [string]$Saida = (Join-Path (Split-Path $PSScriptRoot -Parent) 'zips-por-skill'),
  [string[]]$Skills
)
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force -Path $Saida | Out-Null
Set-Location $Raiz
$todas = Get-ChildItem -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } | Select-Object -ExpandProperty Name
if ($Skills) { $Skills = $Skills | ForEach-Object { $_ -split ',' } | Where-Object { $_ } } else { $Skills = $todas }
foreach ($s in $Skills) {
  if ($todas -notcontains $s) { Write-Warning "Skill não encontrada: $s"; continue }
  $z = Join-Path $Saida "$s.zip"
  if (Test-Path $z) { Remove-Item $z -Force }
  tar.exe -a -c -f $z --exclude '~$*' $s
  $n = (tar.exe -tf $z | Where-Object { $_ -eq "$s/SKILL.md" }).Count
  '{0,-28} {1,6:N2} MB   SKILL.md na raiz: {2}' -f $s, ((Get-Item $z).Length / 1MB), $n
}
