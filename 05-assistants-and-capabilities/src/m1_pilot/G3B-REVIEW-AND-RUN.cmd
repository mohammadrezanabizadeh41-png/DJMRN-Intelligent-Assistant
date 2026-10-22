@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
if errorlevel 1 (
  echo HOLD: G3-B folder not found. Nothing executed.
  pause
  exit /b 2
)
echo.
echo DJMRN G3-B - TWO SYNTHETIC WINDOWS FILES ONLY
echo Test-only candidate, NOT a model or Jan assistant.
echo Creates only alpha.md and beta.md in its own temporary NTFS directory.
echo Attempts one rename/replacement between those synthetic files while handles are held.
echo No personal files, accounts, network requests, installation, admin or system changes.
echo The assistant file-access guard stays CLOSED.
echo Real Junction, concurrent-race, OS cancellation and native egress remain untested.
echo This new G3-B Windows execution requires separate user approval.
echo.
set "PYEXE="
set "PYARGS="
py -3 -V >nul 2>nul
if not errorlevel 1 (
  set "PYEXE=py"
  set "PYARGS=-3"
)
if not defined PYEXE (
  python -V >nul 2>nul
  if not errorlevel 1 set "PYEXE=python"
)
if not defined PYEXE (
  if exist "%LOCALAPPDATA%\Programs\Python\Python314\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python314\python.exe" -V >nul 2>nul
    if not errorlevel 1 set "PYEXE=%LOCALAPPDATA%\Programs\Python\Python314\python.exe"
  )
)
if not defined PYEXE (
  echo HOLD: no working Python interpreter found. Do not install or change settings.
  pause
  exit /b 2
)
rem Verify the reviewed G3B runner itself BEFORE importing it or attempting fixtures.
"%PYEXE%" %PYARGS% -B -c "import hashlib,pathlib,sys;d=pathlib.Path('g3b_synthetic_probe.py').read_bytes();h=hashlib.sha1(b'blob '+str(len(d)).encode('ascii')+bytes([0])+d).hexdigest();sys.exit(0 if h=='db2a96eb7cc34ea6b8986ba3214dece0aa94cb35' else 2)"
if errorlevel 1 (
  echo HOLD: G3B_RUNNER_BLOB_MISMATCH or file absent. No test executed.
  pause
  exit /b 2
)
rem Check the pinned G3 and core file blobs with no fixture creation.
"%PYEXE%" %PYARGS% -B g3b_synthetic_probe.py --verify-source
if errorlevel 1 (
  echo HOLD: G3B_SOURCE_PREFLIGHT_FAILED. No test executed.
  pause
  exit /b 2
)
echo.
echo SOURCE REVIEW PASS. The program has NOT run Windows file tests.
echo Only proceed after new, separate approval for G3-B Windows testing.
echo Press Enter at the next prompt to abort. Type RUN only after that approval.
echo.
"%PYEXE%" %PYARGS% -B g3b_synthetic_probe.py --run-synthetic
set "TEST_EXIT=%errorlevel%"
echo.
echo G3-B is PARTIAL/HOLD at best: some security cases remain NOT_RUN.
echo Report only sanitized JSON, not local paths or device identifiers.
pause
exit /b %TEST_EXIT%
