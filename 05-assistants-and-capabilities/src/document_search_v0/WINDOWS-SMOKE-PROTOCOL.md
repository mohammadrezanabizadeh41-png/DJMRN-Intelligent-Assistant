# CAP-006 — Windows 11 synthetic-only smoke protocol (approved preparation)

**Target:** user-owned Windows 11 Pro laptop, no Administrator, no new install. **Permission:** user approved this *synthetic-only* next test in chat 2026-10-20. **Current status: first attempted on user Windows but STOPPED at `fixtures/sample_alpha.txt` extracted SHA mismatch before Python execution; see [NEW-V0002](../../../06-tests-and-evidence/logs/NEW-V0002-20261020.md).**

## Exact source and package identity
- **Canonical GitHub:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` branch `main`; [source](docsearch_v0.py) blob `0376c8d4a800d0a60b5137d08de6071e46178398`; [tests](test_docsearch_v0.py) blob `982a63f72e4fe0f0b080ba57effcf86fa65fc727`.
- Current-chat portable ZIP: `DJMRN-CAP006-Windows-Smoke-20261020.zip`, SHA256 **`f6228e06b9efc565c971e08f6404e05f8fc9dbc4e625879d420130a9f0026af4`**. It contains only those two .py files, 2 artificial fixture texts and a MANIFEST; assembled from files with Git blob SHA matching the canonical GitHub tree. A temporary chat download is **not** permanent authority; recreate from GitHub if needed.
- Before running, user saves this ZIP in the normal `Downloads` directory **with exact filename**. Never fetch alternative unsigned code, install packages or login to additional services automatically.

## One paste into ordinary (non-admin) PowerShell
This command extracts into a **new** Downloads subdirectory, checks archive and file SHA, invokes only the pre-existing Python launcher, tests dummy content and prints results. If the target folder exists already, it intentionally STOPs instead of overwriting.

```powershell
& {
    $ErrorActionPreference = 'Stop'
    $downloads = Join-Path $env:USERPROFILE 'Downloads'
    $zip = Join-Path $downloads 'DJMRN-CAP006-Windows-Smoke-20261020.zip'
    $work = Join-Path $downloads 'DJMRN-CAP006-Windows-Smoke'
    if (-not (Test-Path -LiteralPath $zip -PathType Leaf)) { throw 'STOP: expected ZIP is not in Downloads.' }
    $expectedZip = 'F6228E06B9EFC565C971E08F6404E05F8FC9DBC4E625879D420130A9F0026AF4'
    if ((Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash -ne $expectedZip) { throw 'STOP: ZIP SHA256 mismatch.' }
    if (Test-Path -LiteralPath $work) { throw 'STOP: workspace already exists. No overwrite. Report this.' }
    Expand-Archive -LiteralPath $zip -DestinationPath $work -ErrorAction Stop
    $checks = @{
        'docsearch_v0.py'='61D7E39A2EAB2FA4601596FB327965FBE44443C71C35884E16703CDDA086A8A8'
        'test_docsearch_v0.py'='92EB554296764E2E9AAC0A8B4B7C241891F069A8A338B18BA7E1B1C887187514'
        'fixtures/sample_alpha.txt'='F706A665794E84A8A524B1D6ACE13CF7F9BF4AF2F9D3475CBECD0CC70CDA18174'
        'fixtures/sample_beta.md'='54372DCEA478C475BE5C55730E6349C6AAAA5E70A2C7DC8B36823FA0969288A4'
    }
    foreach ($relative in $checks.Keys) {
        $p = Join-Path $work ($relative.Replace('/','\'))
        if (-not (Test-Path -LiteralPath $p -PathType Leaf)) { throw "STOP: missing $relative" }
        if ((Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash -ne $checks[$relative]) { throw "STOP: file hash mismatch $relative" }
    }
    $runner = if (Get-Command py -ErrorAction SilentlyContinue) { 'py' } elseif (Get-Command python -ErrorAction SilentlyContinue) { 'python' } else { throw 'STOP: No existing Python command available; no installation authorized.' }
    $prefixArgs = if ($runner -eq 'py') { @('-3') } else { @() }
    $oldEncoding = $env:PYTHONIOENCODING
    try {
        $env:PYTHONIOENCODING = 'utf-8'
        Write-Host '=== DJMRN CAP-006: PYTHON VERSION ==='
        & $runner @prefixArgs --version
        if ($LASTEXITCODE -ne 0) { throw 'STOP: existing Python launcher failed.' }
        Write-Host '=== DJMRN CAP-006: 16 SYNTHETIC UNIT TESTS ==='
        & $runner @prefixArgs -m unittest discover -s $work -p 'test_docsearch_v0.py' -v
        if ($LASTEXITCODE -ne 0) { throw 'STOP: unit tests failed.' }
        Write-Host '=== DJMRN CAP-006: SYNTHETIC JSON SEARCH ==='
        & $runner @prefixArgs (Join-Path $work 'docsearch_v0.py') --root (Join-Path $work 'fixtures') --file 'sample_alpha.txt' --file 'sample_beta.md' --query 'كتاب'
        if ($LASTEXITCODE -ne 0) { throw 'STOP: demo search failed.' }
        Write-Host '=== DJMRN CAP-006 WINDOWS SYNTHETIC SMOKE: COMMANDS COMPLETED ==='
        Write-Host 'No real personal files searched; send this console output for evidence.'
    } finally {
        $env:PYTHONIOENCODING = $oldEncoding
    }
}
```

## Expected, failure and evidence
- Expected test: `Ran 16 tests` and `OK` followed by JSON `"status": "succeeded"` and sample results `sample_alpha.txt` line 1 and `sample_beta.md` line 2. Console rendering of Persian may vary; **do not claim Windows PASS until actual output is provided**.
- If ZIP/hash/folder/Python test fails → STOP and send exact error, do not install, recode, change Windows settings, delete files, or expose personal paths. No user-specific identifiers needed in reported logs.
- User may omit real username/home folder when copying the console; GitHub register should receive sanitized evidence only.
- New local extracted folder and Python `__pycache__` are *test-only outputs*. No registry, services or configuration changed by design; automatic deletion is deliberately not performed.
- Do not use other user Documents, Downloads content, private GitHub clone, customer files, live emails or agent-model tools for this smoke.
- Outcome tracking: after actual user run, coordinator creates `NEW-V0002` in [TEST-REGISTER](../../../06-tests-and-evidence/TEST-REGISTER.md) with actual OS/Python/result and commit/readback. Until then `PENDING USER EXECUTION`.

## Repeatability in future sessions
If current-chat ZIP is unavailable, get those **four pinned exact blobs from the canonical GitHub commit** [4d2b9801](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/4d2b9801e3a985fb34462ee912f89d41363a6115), regenerate the ZIP, compute and document its new SHA256; **never fabricate a sandbox link** or ask user to install an unverified third-party tool.

## 2026-10-20: first user Windows attempt and troubleshooting
The user's first copy/paste stopped at `STOP: File hash mismatch: fixtures/sample_alpha.txt` before Python. Assistant original ZIP SHA and *ZIP-entry* SHA match published expected values, but Windows-extracted file hash/length and cause are **UNKNOWN**. Preserve the existing folder; **DO NOT rerun the same folder-creation command, change hash, disable antivirus, delete files or install Python**. Have user run a read-only `Get-FileHash` / `Get-Item Length` diagnostic on that folder and compare the embedded archive entry directly; review output before deciding on new extraction/testing. [Evidence NEW-V0002](../../../06-tests-and-evidence/logs/NEW-V0002-20261020.md).

## Windows integrity gate cleared on follow-up (2026-10-20)
The user ran read-only `ZipArchive` vs already-extracted file SHA256/length check, and **all four entries matched** plus original ZIP SHA. [NEW-V0002 updated evidence](../../../06-tests-and-evidence/logs/NEW-V0002-20261020.md). Earlier mismatch cause remains unknown. **Do not re-extract the ZIP** or rerun the initial creation script because the test folder exists. Instead use the existing `Downloads/DJMRN-CAP006-Windows-Smoke` for Python version + 16 synthetic unittests + one synthetic `--query 'كتاب'` CLI run; maintain original permission/stop gates. Until actual output arrives, the final Windows test is PENDING.
