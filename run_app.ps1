# EduAI Student Performance Predictor Launcher
Write-Host "Starting EduAI Student Performance Predictor..." -ForegroundColor Green
Write-Host ""

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Run the Flask app
python app.py

Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Yellow
$null = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")