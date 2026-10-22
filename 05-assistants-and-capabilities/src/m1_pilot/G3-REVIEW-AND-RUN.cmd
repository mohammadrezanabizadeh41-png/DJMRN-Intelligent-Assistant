@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
if errorlevel 1 (
  echo HOLD: unable to access the G3 script directory.
  pause
  exit /b 2
)
echo.
echo DJMRN G3 - TWO SYNTHETIC WINDOWS FILES ONLY
echo No personal files, network, Jan, Agent, model, installation or admin privileges.
echo The M1 file-access guard will remain CLOSED.
echo.
rem Use an interpreter that actually starts. WindowsApps python.exe aliases can
rem satisfy WHERE yet show "Python was not found" when executed.
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
  echo HOLD: no working Python interpreter found.
  echo Do not install Python or alter Windows settings just for this G3 test.
  echo Report: PYTHON_INTERPRETER_NOT_FOUND.
  pause
  exit /b 2
)
echo Python interpreter found. Starting source-integrity preflight.
"%PYEXE%" %PYARGS% -B g3_synthetic_probe.py
if errorlevel 1 (
  echo HOLD: G3 source integrity or Python environment preflight failed.
  echo Report: G3_PREFLIGHT_FAILED. No synthetic file read test started.
  pause
  exit /b 2
)
echo.
echo Type RUN and Enter to execute only the two synthetic file tests.
echo Press Enter without typing RUN to abort.
set /p "ACK=Decision: "
if /I not "%ACK%"=="RUN" (
  echo ABORTED: no synthetic Windows file test was run.
  pause
  exit /b 0
)
"%PYEXE%" %PYARGS% -B g3_synthetic_probe.py --run-synthetic
set "TEST_EXIT=%errorlevel%"
echo.
echo G3 is PARTIAL/HOLD at best: cancellation and junction/race cases remain untested.
echo Share only sanitized JSON results, never full user directories or account details.
pause
exit /b %TEST_EXIT%
