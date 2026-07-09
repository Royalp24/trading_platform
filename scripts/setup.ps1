$ErrorActionPreference = "Stop"
$RepositoryRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $RepositoryRoot

if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "Created .env from .env.example; replace placeholder secrets before deployment."
}

Write-Host "Foundation setup complete. Run: docker compose up --build"
