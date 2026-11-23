# PromptShield PowerShell Launcher
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "          PROMPTSHIELD SECURITY SUITE              " -ForegroundColor Green
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "Directory: $ScriptDir" -ForegroundColor Gray
Write-Host "Launching Dashboard..." -ForegroundColor Yellow

python "$ScriptDir\code\app.py"
