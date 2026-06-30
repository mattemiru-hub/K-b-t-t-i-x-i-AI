param(
  [string]$TargetRoot = "$env:USERPROFILE\\.codex\\skills"
)

$ErrorActionPreference = "Stop"

$source = Split-Path -Parent $PSScriptRoot
$skillName = Split-Path -Leaf $source
$target = Join-Path $TargetRoot $skillName

if (-not (Test-Path -LiteralPath $TargetRoot)) {
  New-Item -ItemType Directory -Path $TargetRoot | Out-Null
}

robocopy $source $target /MIR /XD .git __pycache__ | Out-Null

Write-Output "Installed skill to: $target"
