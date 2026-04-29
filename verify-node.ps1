<#
verify-node.ps1 - Verify manifest signature and asset SHA-256 hashes (PowerShell)
Usage: .\verify-node.ps1 [-ManifestPath manifest.json] [-SignaturePath manifest.sig]
Environment overrides:
  $env:LIBRARIAN_PUB  - path to PEM public key for OpenSSL verification
  $env:LIBRARIAN_PUB_GPG - path to GPG public key for GPG verification (optional)
#>

[CmdletBinding()]
param(
    [string]$ManifestPath = "manifest.json",
    [string]$SignaturePath = "manifest.sig"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Write-Host "Starting repository verification (PowerShell)"

if (-Not (Test-Path -Path $ManifestPath)) {
    Write-Error "Manifest not found: $ManifestPath"
    exit 2
}
if (-Not (Test-Path -Path $SignaturePath)) {
    Write-Error "Signature not found: $SignaturePath"
    exit 2
}

$pubPem = $env:LIBRARIAN_PUB
$pubGpg = $env:LIBRARIAN_PUB_GPG

$useOpenSsl = $false
$useGpg = $false

# Check availability
if ($pubPem -and (Test-Path $pubPem) -and (Get-Command openssl -ErrorAction SilentlyContinue)) {
    $useOpenSsl = $true
}
if ($pubGpg -and (Test-Path $pubGpg) -and (Get-Command gpg -ErrorAction SilentlyContinue)) {
    $useGpg = $true
}
# Allow gpg verify via keyring if gpg exists and no PEM provided
if (-Not $useOpenSsl -and -Not $useGpg -and (Get-Command gpg -ErrorAction SilentlyContinue)) {
    $useGpg = $true
}

if ($useOpenSsl) {
    Write-Host "Verifying manifest signature with OpenSSL using key: $pubPem"
    $proc = Start-Process -FilePath openssl -ArgumentList "dgst","-sha256","-verify","$pubPem","-signature","$SignaturePath","$ManifestPath" -NoNewWindow -Wait -PassThru -RedirectStandardOutput stdout.txt -RedirectStandardError stderr.txt
n    $out = Get-Content stdout.txt -Raw -ErrorAction SilentlyContinue
    $err = Get-Content stderr.txt -Raw -ErrorAction SilentlyContinue
    if ($proc.ExitCode -eq 0) {
        Write-Host "Signature verification: OK"
    } else {
        Write-Error "Signature verification: FAILED"
        if ($out) { Write-Host $out }
        if ($err) { Write-Host $err }
        exit 3
    }
} elseif ($useGpg) {
    if ($pubGpg -and (Test-Path $pubGpg)) {
        Write-Host "Importing GPG public key from: $pubGpg"
        & gpg --import $pubGpg | Out-Null
    }
    Write-Host "Verifying manifest signature with GPG"
    try {
        & gpg --verify $SignaturePath $ManifestPath 2>&1 | Write-Host
        if ($LASTEXITCODE -ne 0) { throw "GPG verify failed" }
        Write-Host "GPG signature: OK"
    } catch {
        Write-Error "GPG signature: FAILED"
        exit 3
    }
} else {
    Write-Error "No verification method available. Provide LIBRARIAN_PUB (PEM) or LIBRARIAN_PUB_GPG (GPG) and ensure openssl or gpg is installed."
    exit 4
}

# Verify asset SHA256 hashes
Write-Host "Verifying asset hashes from $ManifestPath"

try {
    $manifestJson = Get-Content -Raw -Path $ManifestPath | ConvertFrom-Json
} catch {
    Write-Error "Failed to read or parse manifest JSON"
    exit 5
}

$fail = $false
foreach ($asset in $manifestJson.assets) {
    $path = $asset.path
    $expected = $asset.sha256
    if (-not $path) { Write-Host "Skipping asset with no path"; continue }
    if (-not (Test-Path -Path $path)) { Write-Error "MISSING: $path"; $fail = $true; continue }
    try {
        $hash = Get-FileHash -Algorithm SHA256 -Path $path
        $actual = $hash.Hash.ToLower()
    } catch {
        Write-Error "FAILED to compute hash for $path"
        $fail = $true
        continue
    }
    if ($actual -ne $expected.ToLower()) {
        Write-Error "MISMATCH: $path"
        Write-Host "  expected: $expected"
        Write-Host "  actual:   $actual"
        $fail = $true
    } else {
        Write-Host "OK: $path"
    }
}

if ($fail) {
    Write-Error "One or more asset verifications failed"
    exit 6
}

Write-Host "All verifications passed"
exit 0
