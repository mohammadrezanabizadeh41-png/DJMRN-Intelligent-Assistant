"""Pure off-Windows guard logic and fail-closed negative tests, NOT G3 tests."""
import unittest
import sys
from unittest.mock import patch
from core.windows_reader import (validate_local_windows_path, validate_file_metadata,
                                  VerifiedReaderHold, read_approved_file_source_only,
                                  read_manifest_snapshots_source_only,
                                  FILE_ATTRIBUTE_DIRECTORY, FILE_ATTRIBUTE_REPARSE_POINT)
from core.manifest import Manifest, ApprovedFile


def doc():
    return ApprovedFile('doc-alpha', 'alpha.md', r'C:\Fixtures\alpha.md', 'a'*64,
                        10, 222, 123, 1)


def fakeinfo(**overrides):
    class X: pass
    obj = X()
    for a,b in dict(attributes=0, links=1, volume=222, id_high=0,
                    id_low=123, size_high=0, size_low=10).items():
        setattr(obj,a,overrides.get(a,b))
    return obj

class SourceOnlyReaderTests(unittest.TestCase):
    def test_simple_path(self):
        self.assertEqual(validate_local_windows_path(r'C:\Fixtures\alpha.md'),
                         ('C:\\', 'Fixtures', 'alpha.md'))

    def test_reject_bad_spellings_before_syscalls(self):
        cases=['../other.md', '/tmp/alpha.md', r'\\server\s\alpha.md',
               r'\\?\C:\Fixtures\alpha.md', r'C:\Fixtures\..\secret.md',
               r'C:\Fixtures\file.md:stream', r'C:\Fixtures\NUL.md',
               r'C:\Fixtures\alpha.md ', r'C:\Fixtures\alpha.txt',
               r'C:/Fixtures/alpha.md', r'C:\Fixtures\\alpha.md',
               r'C:\Fixtures\alpha.md.']
        for case in cases:
            with self.subTest(path=case), self.assertRaises(VerifiedReaderHold):
                validate_local_windows_path(case)

    def test_handle_file_identity_checks(self):
        validate_file_metadata(fakeinfo(), doc(), is_parent=False)
        bads=[dict(links=2),dict(volume=1),dict(id_low=124),dict(size_low=100),
              dict(attributes=FILE_ATTRIBUTE_DIRECTORY),
              dict(attributes=FILE_ATTRIBUTE_REPARSE_POINT)]
        for vals in bads:
            with self.subTest(vals=vals), self.assertRaises(VerifiedReaderHold):
                validate_file_metadata(fakeinfo(**vals), doc(), is_parent=False)

    def test_parent_reparse_rejected(self):
        validate_file_metadata(fakeinfo(attributes=FILE_ATTRIBUTE_DIRECTORY),doc(),is_parent=True)
        with self.assertRaises(VerifiedReaderHold):
            validate_file_metadata(fakeinfo(attributes=FILE_ATTRIBUTE_DIRECTORY|FILE_ATTRIBUTE_REPARSE_POINT),
                                   doc(),is_parent=True)

    @unittest.skipUnless(sys.platform == 'win32', 'G3 Windows device tests separately authorized')
    def test_actual_win32_junction_and_race(self):
        self.skipTest('G3 not approved; actual link and race exercises not run')

    def test_offdevice_no_read(self):
        if sys.platform != 'win32':
            with self.assertRaises(VerifiedReaderHold) as c:
                read_approved_file_source_only(doc())
            self.assertEqual(c.exception.code, 'WINDOWS_ONLY')

    def test_selection_rejects_third(self):
        m = Manifest(1,'S-1-5-21-1000',(doc(),))
        with self.assertRaises(VerifiedReaderHold):
            read_manifest_snapshots_source_only(m, ('doc-alpha', 'doc-third'))

if __name__ == '__main__':
    unittest.main()
