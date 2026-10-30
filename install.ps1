# Copies every skill in ./skills into the user's Claude Code skills folder.
param([string]$Target = (Join-Path $HOME ".claude\skills"))

$src = Join-Path $PSScriptRoot "skills"
New-Item -ItemType Directory -Force -Path $Target | Out-Null
Get-ChildItem $src -Directory | ForEach-Object {
    $dest = Join-Path $Target $_.Name
    if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
    Copy-Item -Recurse $_.FullName $dest
    Write-Host "installed $($_.Name)"
}
