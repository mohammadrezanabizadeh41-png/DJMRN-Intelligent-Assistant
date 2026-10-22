"""G3 source-level checks only. These are NOT Windows Win32 tests."""
from __future__ import annotations
import ast
import argparse
import ctypes
import hashlib
from pathlib import Path
from types import SimpleNamespace
import sys
import unittest

SOURCE = Path(__file__).resolve().parent.parent / 'g3_synthetic_probe.py'
TREE = ast.parse(SOURCE.read_text(encoding='utf-8'))
KEEP = {'git_blob_id', 'checked', 'win_handle_number', 'HandleTracker', 'denial', 'run_synthetic'}
NODES = [x for x in TREE.body if isinstance(x, (ast.FunctionDef, ast.ClassDef)) and x.name in KEEP]

class _Hold(RuntimeError):
    def __init__(self, code):
        self.code=code

class _Kernel:
    def CreateFileW(self,*args):
        return 41
    def CloseHandle(self,h):
        return True

SCOPE = {
    'hashlib':hashlib, 'ctypes':ctypes, 'sys':sys,
    'wr': SimpleNamespace(INVALID_HANDLE_VALUE=ctypes.c_void_p(-1).value,
                          VerifiedReaderHold=_Hold)
}
exec(compile(ast.Module(body=NODES, type_ignores=[]), str(SOURCE),'exec'), SCOPE)

class OffdeviceSourceChecks(unittest.TestCase):
    def test_syntax_and_source(self):
        self.assertEqual(SOURCE.read_bytes(), SOURCE.read_text(encoding='utf-8').encode('utf-8'))

    def test_git_blob_calculation(self):
        self.assertEqual(SCOPE['git_blob_id'](b'abc'), hashlib.sha1(b'blob 3\0abc').hexdigest())

    def test_tracker_balances_closes(self):
        spy=SCOPE['HandleTracker'](_Kernel())
        spy.CreateFileW('fake')
        self.assertFalse(spy.balanced())
        spy.CloseHandle(41)
        self.assertTrue(spy.balanced())

    def test_tracker_detects_leak(self):
        spy=SCOPE['HandleTracker'](_Kernel())
        spy.CreateFileW('fake')
        self.assertFalse(spy.balanced())

    def test_denial_behavior(self):
        self.assertEqual(SCOPE['denial'](lambda: (_ for _ in ()).throw(_Hold('OUTSIDE_MANIFEST')),
                                         ('OUTSIDE_MANIFEST',)), 'OUTSIDE_MANIFEST')
        with self.assertRaises(RuntimeError):
            SCOPE['denial'](lambda: None)

    def test_off_windows_gated_before_creating_fixtures(self):
        if sys.platform == 'win32':
            self.skipTest('This suite is strictly off-Windows')
        with self.assertRaisesRegex(RuntimeError,'WINDOWS_ONLY'):
            SCOPE['run_synthetic']()

    def test_no_network_or_recursive_delete_in_source(self):
        code=SOURCE.read_text(encoding='utf-8')
        self.assertNotIn('shutil.rmtree',code)
        self.assertNotIn('requests.',code)
        self.assertNotIn('urlopen(',code)
        self.assertNotIn('subprocess.',code)

if __name__=='__main__':
    unittest.main()
