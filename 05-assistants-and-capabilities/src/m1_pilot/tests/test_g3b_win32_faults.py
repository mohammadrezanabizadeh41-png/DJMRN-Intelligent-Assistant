"""G3-B test-only fault injection for the *existing* Windows reader.

Run in a FULL repo checkout: cd 05-assistants-and-capabilities/src/m1_pilot
    python -B -m unittest tests/test_g3b_win32_faults.py -v
No files are created, no Win32 API called, no network operations performed.
Tests are deterministic simulations, NOT Windows security evidence.
"""
from __future__ import annotations

import ast
from contextlib import contextmanager
import hashlib
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from core.manifest import ApprovedFile
from core import windows_reader as wr

FILE = r"C:\G3Fixture\alpha.md"
DATA = b"# DJMRN synthetic G3-B\n"
SERIAL = 112233
INDEX = 4321


class FakeKernel:
    """In-memory API-double; never calls kernel32. Only supports this test path."""

    def __init__(self):
        self.handles: dict[int, str] = {}
        self.opened: list[int] = []
        self.closed: list[int] = []
        self.sharing: list[tuple[str, int, int]] = []
        self.read_handles: list[int] = []
        self.case = "normal"
        self.read_completed = False
        self.next_handle = 50

    def CreateFileW(self, name, access, sharing, security, disposition, flags, template):
        assert disposition == wr.OPEN_EXISTING
        assert flags & wr.FILE_FLAG_OPEN_REPARSE_POINT
        assert sharing == wr.FILE_SHARE_READ
        self.next_handle += 1
        handle = self.next_handle
        self.handles[handle] = name
        self.opened.append(handle)
        self.sharing.append((name, sharing, flags))
        return handle

    def GetFileType(self, handle):
        assert self.handles[handle] == FILE
        return wr.FILE_TYPE_DISK

    def CloseHandle(self, handle):
        if handle not in self.handles or handle in self.closed:
            raise AssertionError("bad CloseHandle")
        self.closed.append(handle)
        return True

    def metadata(self, kernel, handle):
        path = self.handles[handle]
        leaf = path == FILE
        attributes = 0 if leaf else wr.FILE_ATTRIBUTE_DIRECTORY
        if self.case == "ancestor_reparse" and path == r"C:\G3Fixture":
            attributes |= wr.FILE_ATTRIBUTE_REPARSE_POINT
        if self.case == "file_reparse" and leaf:
            attributes |= wr.FILE_ATTRIBUTE_REPARSE_POINT
        file_index = INDEX if leaf else 1
        if self.case == "postread_index_changed" and leaf and self.read_completed:
            file_index += 1
        return SimpleNamespace(attributes=attributes, links=1,
                               volume=SERIAL, id_high=0, id_low=file_index,
                               size_high=0, size_low=len(DATA) if leaf else 0,
                               modified=SimpleNamespace(low=123, high=0))

    def final_path(self, kernel, handle):
        path = self.handles[handle]
        if self.case == "ancestor_redirect" and path == r"C:\G3Fixture":
            return r"C:\AnotherFixture"
        if self.case == "file_redirect" and path == FILE:
            return r"C:\G3Fixture\other.md"
        return path

    def ntfs(self, kernel, handle):
        return SERIAL

    def read(self, kernel, handle, length):
        assert length == len(DATA)
        assert self.handles[handle] == FILE
        self.read_handles.append(handle)
        if self.case == "read_error":
            raise wr.VerifiedReaderHold("SIMULATED_READ_ERROR")
        self.read_completed = True
        if self.case == "wrong_bytes":
            return b"X" * len(DATA)
        return DATA

    def balanced(self):
        return sorted(self.opened) == sorted(self.closed)


@contextmanager
def fake_reader(kernel):
    with patch.multiple(wr, _api=lambda: kernel, _metadata=kernel.metadata,
                        _final_path=kernel.final_path, _require_ntfs=kernel.ntfs,
                        _read_same_handle=kernel.read):
        yield


def approved_file():
    return ApprovedFile("doc-alpha", "alpha.md", FILE,
                        hashlib.sha256(DATA).hexdigest(), len(DATA), SERIAL, INDEX, 1)


def simulate_release_after_read(read_callable, canceled):
    """Test-only *delivery* gate, NOT reader cancellation or OS interruption."""
    if canceled():
        raise wr.VerifiedReaderHold("REVOKED_BEFORE_READ")
    result = read_callable()
    if canceled():
        raise wr.VerifiedReaderHold("REVOKED_BEFORE_DELIVERY")
    return result


class WindowsReaderInjectionTests(unittest.TestCase):
    def check_case(self, fault, wanted=None):
        kernel = FakeKernel()
        kernel.case = fault
        with fake_reader(kernel):
            if wanted:
                with self.assertRaises(wr.VerifiedReaderHold) as e:
                    wr.read_approved_file_source_only(approved_file())
                self.assertEqual(e.exception.code, wanted)
            else:
                snap = wr.read_approved_file_source_only(approved_file())
                self.assertEqual(snap.raw, DATA)
                self.assertEqual(snap.sha256, hashlib.sha256(DATA).hexdigest())
        self.assertTrue(kernel.balanced(), "all acquired handles must close")
        self.assertTrue(all(s == wr.FILE_SHARE_READ for _, s, _ in kernel.sharing))
        return kernel

    def test_01_same_handle_and_cleanup(self):
        k = self.check_case("normal")
        self.assertEqual(len(k.read_handles), 1)
        self.assertEqual(k.handles[k.read_handles[0]], FILE)
        self.assertEqual(len(k.opened), 3)  # root + parent directory + file

    def test_02_ancestor_reparse_refused(self):
        k = self.check_case("ancestor_reparse", "REPARSE_OR_OFFLINE")
        self.assertEqual(k.read_handles, [])

    def test_03_ancestor_redirect_refused(self):
        k = self.check_case("ancestor_redirect", "PARENT_PATH_CHANGED")
        self.assertEqual(k.read_handles, [])

    def test_04_file_reparse_refused(self):
        k = self.check_case("file_reparse", "REPARSE_OR_OFFLINE")
        self.assertEqual(k.read_handles, [])

    def test_05_file_final_path_redirect_refused(self):
        k = self.check_case("file_redirect", "FILE_PATH_CHANGED")
        self.assertEqual(k.read_handles, [])

    def test_06_identity_change_during_read_refused(self):
        k = self.check_case("postread_index_changed", "IDENTITY_OR_SIZE")
        self.assertEqual(len(k.read_handles), 1)

    def test_07_wrong_bytes_hash_refused(self):
        k = self.check_case("wrong_bytes", "HASH_MISMATCH")
        self.assertEqual(len(k.read_handles), 1)

    def test_08_read_error_closes_all_handles(self):
        k = self.check_case("read_error", "SIMULATED_READ_ERROR")
        self.assertEqual(len(k.read_handles), 1)

    def test_09_revoke_before_read_withholds_delivery(self):
        called = []
        with self.assertRaisesRegex(wr.VerifiedReaderHold, "REVOKED_BEFORE_READ"):
            simulate_release_after_read(lambda: called.append(1), lambda: True)
        self.assertEqual(called, [])

    def test_10_revoke_during_mock_read_withholds_delivery(self):
        flags = {"revoked": False}
        def fake_read():
            flags["revoked"] = True
            return DATA
        with self.assertRaisesRegex(wr.VerifiedReaderHold, "REVOKED_BEFORE_DELIVERY"):
            simulate_release_after_read(fake_read, lambda: flags["revoked"])

    def test_11_no_revoke_mock_delivers(self):
        self.assertEqual(simulate_release_after_read(lambda: DATA, lambda: False), DATA)

    def test_12_no_network_symbols_in_checked_source(self):
        src = Path(wr.__file__).read_text(encoding="utf-8")
        tree = ast.parse(src)
        forbidden = {"socket", "requests", "urllib", "http", "ftplib", "subprocess"}
        mods = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                mods.update(alias.name.partition(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                mods.add(node.module.partition(".")[0])
        self.assertFalse(mods & forbidden)
        # Static absence is not process-level egress monitoring.


if __name__ == "__main__":
    unittest.main()
