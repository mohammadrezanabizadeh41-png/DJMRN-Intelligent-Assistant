"""Windows batch launcher STATIC assertions. Not cmd.exe execution evidence."""
from pathlib import Path
import hashlib
import unittest

ROOT=Path(__file__).resolve().parent.parent
CMD=ROOT/'G3B-REVIEW-AND-RUN.cmd'
RUNNER=ROOT/'g3b_synthetic_probe.py'

class LauncherStaticReview(unittest.TestCase):
    def test_01_exact_runner_blob_pinned(self):
        data=RUNNER.read_bytes()
        sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\x00'+data).hexdigest()
        self.assertIn(sha,CMD.read_text())

    def test_02_source_preflight_precedes_optin(self):
        text=CMD.read_text()
        self.assertLess(text.index('--verify-source'),text.index('--run-synthetic'))
        self.assertIn('G3B_SOURCE_PREFLIGHT_FAILED',text)
        self.assertIn('G3B_RUNNER_BLOB_MISMATCH',text)

    def test_03_python_alias_workaround(self):
        text=CMD.read_text()
        self.assertIn('py -3 -V >nul 2>nul',text)
        self.assertIn('python -V >nul 2>nul',text)
        self.assertIn('if not defined PYEXE',text)

    def test_04_no_install_or_scheduled_process(self):
        text=CMD.read_text().lower()
        for token in ['winget install','pip install','powershell -enc','curl ','wget ','schtasks','start /b','rmdir /s','del /s','runas ']:
            self.assertNotIn(token,text)

    def test_05_operator_input_inside_runner(self):
        self.assertIn('decision = input("New G3-B consent required.',RUNNER.read_text())
        self.assertIn('if decision != "RUN":',RUNNER.read_text())

    def test_06_no_silent_app_or_model_activation(self):
        text=CMD.read_text().lower()
        for token in ['jan-desktop.exe','ollama serve','lm studio','start jan','agent.py']:
            self.assertNotIn(token,text)

if __name__=='__main__': unittest.main()
