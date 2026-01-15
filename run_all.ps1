# One-click local workflow runner
# Usage: powershell -ExecutionPolicy Bypass -File .\run_all.ps1

$ErrorActionPreference = "Stop"

Write-Host "Installing dependencies..." 
py -m pip install -r requirements.txt

Write-Host "Running tests..."
py -m pytest -q

Write-Host "Running OpenAI ping (mock by default)..."
if (-not $env:MOCK_OPENAI) { $env:MOCK_OPENAI = "1" }
py scripts/openai_ping.py

Write-Host "Done ✅"
