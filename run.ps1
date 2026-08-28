$ErrorActionPreference = "Stop"

if (-not (Test-Path ".venv\Scripts\python.exe")) {
    Write-Host "Virtual environment not found."
    Write-Host "Create it with: python -m venv .venv"
    exit 1
}

.\.venv\Scripts\python.exe src\main.py
