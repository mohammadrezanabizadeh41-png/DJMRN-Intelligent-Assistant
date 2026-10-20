& {
    $ErrorActionPreference = 'Stop'
    $downloads = Join-Path $env:USERPROFILE 'Downloads'
    $zip = Join-Path $downloads 'DJMRN-CAP006-Windows-Smoke-20261020.zip'
    $work = Join-Path $downloads 'DJMRN-CAP006-Windows-Smoke'

    if (!(Test-Path -LiteralPath $zip -PathType Leaf)) {
        throw 'STOP: Original ZIP is not in Downloads.'
    }
    if (!(Test-Path -LiteralPath $work -PathType Container)) {
        throw 'STOP: Previously extracted folder was not found.'
    }

    $expectedZip = 'F6228E06B9EFC565C971E08F6404E05F8FC9DBC4E625879D420130A9F0026AF4'
    $actualZip = (Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash
    if ($actualZip -ne $expectedZip) {
        throw "STOP: ZIP hash mismatch. Actual: $actualZip"
    }

    Add-Type -AssemblyName System.IO.Compression
    Add-Type -AssemblyName System.IO.Compression.FileSystem

    Write-Host '=== DJMRN: VERIFY FILES AGAINST THE PINNED ZIP ===' -ForegroundColor Cyan
    $archive = [System.IO.Compression.ZipFile]::OpenRead($zip)
    try {
        $relativeFiles = @(
            'docsearch_v0.py',
            'test_docsearch_v0.py',
            'fixtures/sample_alpha.txt',
            'fixtures/sample_beta.md'
        )

        foreach ($relative in $relativeFiles) {
            $entry = $archive.GetEntry($relative)
            if ($null -eq $entry) {
                throw "STOP: ZIP entry missing: $relative"
            }

            $stream = $entry.Open()
            $sha = [System.Security.Cryptography.SHA256]::Create()
            try {
                $zipEntryHash = [BitConverter]::ToString(
                    $sha.ComputeHash($stream)
                ).Replace('-', '')
            }
            finally {
                $stream.Dispose()
                $sha.Dispose()
            }

            $diskFile = Join-Path $work ($relative.Replace('/', '\'))
            if (!(Test-Path -LiteralPath $diskFile -PathType Leaf)) {
                throw "STOP: Extracted file missing: $relative"
            }

            $diskHash = (Get-FileHash -LiteralPath $diskFile -Algorithm SHA256).Hash
            $diskLength = (Get-Item -LiteralPath $diskFile).Length
            $match = (($diskHash -eq $zipEntryHash) -and ($diskLength -eq $entry.Length))
            Write-Host "$relative : MATCH=$match"

            if (!$match) {
                Write-Host "ZIP:  $zipEntryHash ($($entry.Length) bytes)"
                Write-Host "DISK: $diskHash ($diskLength bytes)"
                throw "STOP: Integrity mismatch for $relative; Python NOT run."
            }
        }
    }
    finally {
        $archive.Dispose()
    }

    Write-Host '=== ALL FOUR ZIP AND DISK FILES MATCH ===' -ForegroundColor Green

    if (Get-Command py -ErrorAction SilentlyContinue) {
        $runner = 'py'
        $runnerArgs = @('-3')
    }
    elseif (Get-Command python -ErrorAction SilentlyContinue) {
        $runner = 'python'
        $runnerArgs = @()
    }
    else {
        throw 'STOP: Existing Python not found. No installation.'
    }

    $oldEncoding = $env:PYTHONIOENCODING
    $oldBytecode = $env:PYTHONDONTWRITEBYTECODE
    try {
        $env:PYTHONIOENCODING = 'utf-8'
        $env:PYTHONDONTWRITEBYTECODE = '1'

        Write-Host '=== PYTHON VERSION ===' -ForegroundColor Cyan
        & $runner @runnerArgs --version
        if ($LASTEXITCODE -ne 0) { throw 'STOP: Python launcher failed.' }

        Write-Host '=== RUNNING 16 SYNTHETIC UNIT TESTS ===' -ForegroundColor Cyan
        & $runner @runnerArgs -m unittest discover -s $work -p 'test_docsearch_v0.py' -v
        if ($LASTEXITCODE -ne 0) { throw 'STOP: Unit tests failed.' }

        Write-Host '=== PERSIAN SEARCH ON SYNTHETIC FILES ===' -ForegroundColor Cyan
        & $runner @runnerArgs (Join-Path $work 'docsearch_v0.py') --root (Join-Path $work 'fixtures') --file 'sample_alpha.txt' --file 'sample_beta.md' --query 'كتاب'
        if ($LASTEXITCODE -ne 0) { throw 'STOP: Synthetic document search failed.' }

        Write-Host '=== DJMRN CAP-006 WINDOWS SMOKE PASSED ===' -ForegroundColor Green
    }
    finally {
        $env:PYTHONIOENCODING = $oldEncoding
        $env:PYTHONDONTWRITEBYTECODE = $oldBytecode
    }
}
