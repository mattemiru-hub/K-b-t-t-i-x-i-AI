param(
  [Parameter(Mandatory = $true)]
  [string]$WorkbookPath,
  [string]$PreviewPath,
  [string]$DashboardSheet = "00_Executive_Dashboard",
  [string]$DashboardRange = "A1:AG47",
  [switch]$SkipRefresh
)

$ErrorActionPreference = "Stop"

function Invoke-Retry([scriptblock]$Block, [int]$Tries = 8, [int]$DelayMs = 1500) {
  for ($i = 1; $i -le $Tries; $i++) {
    try { return & $Block } catch {
      if ($i -eq $Tries) { throw }
      Start-Sleep -Milliseconds $DelayMs
    }
  }
}

$fullPath = (Resolve-Path -LiteralPath $WorkbookPath).Path
if (-not $PreviewPath) {
  $PreviewPath = [System.IO.Path]::ChangeExtension($fullPath, ".png")
}
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $true
$excel.DisplayAlerts = $false
$excel.ScreenUpdating = $true

try {
  $wb = $excel.Workbooks.Open($fullPath)
  if ($wb -eq $null) { $wb = $excel.ActiveWorkbook }
  if ($wb -eq $null) { throw "Could not open workbook: $fullPath" }
  $dash = $wb.Worksheets($DashboardSheet)
  $dash.Activate()
  try { $excel.ActiveWindow.WindowState = -4143 } catch {}
  try { $excel.ActiveWindow.DisplayGridlines = $false } catch {}
  try { $excel.ActiveWindow.Zoom = 85 } catch {}
  try { $excel.Calculation = -4105 } catch {}
  if (-not $SkipRefresh) {
    try { $wb.RefreshAll() } catch {}
    try { $excel.CalculateUntilAsyncQueriesDone() } catch {}
    Start-Sleep -Seconds 8
    try { $excel.CalculateFullRebuild() } catch {}
    Start-Sleep -Seconds 5
  } else {
    try { $excel.CalculateFull() } catch {}
    Start-Sleep -Seconds 3
  }

  $range = $dash.Range($DashboardRange)
  Invoke-Retry { $range.Select() } | Out-Null
  Invoke-Retry { $excel.Selection.CopyPicture(1, -4147) } | Out-Null
  $co = Invoke-Retry { $dash.ChartObjects().Add(0, 0, $range.Width, $range.Height) }
  Invoke-Retry { $co.Chart.Paste() } | Out-Null
  Invoke-Retry { [void]$co.Chart.Export($PreviewPath, "PNG") } | Out-Null
  $co.Delete()
  $wb.Save()

  Write-Output "Preview: $PreviewPath"
  Write-Output "Queries: $($wb.Queries.Count)"
  Write-Output "ModelTables: $($wb.Model.ModelTables.Count)"
  Write-Output "Relationships: $($wb.Model.ModelRelationships.Count)"
  Write-Output "Measures: $($wb.Model.ModelMeasures.Count)"
} finally {
  if ($wb) { try { $wb.Close($true) } catch {} }
  try { $excel.Quit() } catch {}
}
