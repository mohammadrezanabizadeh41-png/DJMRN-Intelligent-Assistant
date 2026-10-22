@echo off
setlocal
cd /d "%~dp0"
echo.
echo DJMRN G3 - SYNTHETIC WINDOWS 11 PROBE ONLY
echo No Jan, agent, account, personal files or network use.
echo Only two temporary synthetic Markdown files will be created.
echo The M1 assistant file-access guard remains CLOSED.
echo.
where python >nul 2>nul
if errorlevel 1 (
  echo HOLD: Python command not found. Nothing executed.
  pause
  exit /b 2
)
python -B g3_synthetic_probe.py
if errorlevel 1 (
  echo HOLD: source integrity or Python environment check failed.
  pause
  exit /b 2
)
echo.
echo To ABORT without running Windows file tests, press ENTER.
echo To APPROVE this narrow synthetic test, type RUN and press ENTER.
set /p ACK=Decision:
if /I not "%ACK%"=="RUN" (
  echo ABORTED: no Windows test was run.
  pause
  exit /b 0
)
python -B g3_synthetic_probe.py --run-synthetic
set "TEST_EXIT=%errorlevel%"
echo.
echo Result above is PARTIAL G3 at best. Cancellation and reparse race remain NOT RUN.
echo Do NOT send personal path or device identifiers when reporting.
pause
exit /b %TEST_EXIT%
