"""DJMRN G2A PROTOTYPE: read *only* the already-approved file identity by Win32 handle.

Not called by SearchSession. No Windows G3 test, no user file permissions granted.
Windows native implementation intentionally separate from the fail-closed guard.
"""
from __future__ import annotations

import ctypes
from ctypes import wintypes
from contextlib import ExitStack
from dataclasses import dataclass
import hashlib
from pathlib import PureWindowsPath
import re
import sys

from .manifest import ApprovedFile, Manifest

MAX_BYTES = 1024 * 1024
FILE_READ_DATA = 0x0001
FILE_READ_ATTRIBUTES = 0x0080
FILE_SHARE_READ = 0x0001
OPEN_EXISTING = 3
FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
FILE_ATTRIBUTE_DIRECTORY = 0x00000010
FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400
FILE_ATTRIBUTE_OFFLINE = 0x00001000
FILE_TYPE_DISK = 1
INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value
_BAD_SEGMENT = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_DOS_DEVICE = re.compile(r'(?i)^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?$')


class VerifiedReaderHold(RuntimeError):
    def __init__(self, code: str):
        self.code = code
        super().__init__(code)


@dataclass(frozen=True)
class VerifiedSnapshot:
    file_id: str
    display_name: str
    sha256: str
    raw: bytes

    @property
    def bytes_count(self) -> int:
        return len(self.raw)


class _FILETIME(ctypes.Structure):
    _fields_ = [('low', wintypes.DWORD), ('high', wintypes.DWORD)]


class _BY_HANDLE_FILE_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('attributes', wintypes.DWORD),
        ('created', _FILETIME),
        ('accessed', _FILETIME),
        ('modified', _FILETIME),
        ('volume', wintypes.DWORD),
        ('size_high', wintypes.DWORD),
        ('size_low', wintypes.DWORD),
        ('links', wintypes.DWORD),
        ('id_high', wintypes.DWORD),
        ('id_low', wintypes.DWORD),
    ]


def validate_local_windows_path(path: str) -> tuple[str, ...]:
    """Reject UNC/extended/device/ADS/relative/ambiguous Windows path spellings.

    This is a lexical filter, not evidence that the directory is safe.
    """
    if type(path) is not str or len(path) > 260 or not re.match(r'^[A-Za-z]:\\', path):
        raise VerifiedReaderHold('PATH_FORM')
    if '/' in path or path.startswith('\\\\'):
        raise VerifiedReaderHold('PATH_FORM')
    parsed = PureWindowsPath(path)
    if not parsed.is_absolute() or len(parsed.parts) < 2:
        raise VerifiedReaderHold('PATH_FORM')
    names = path[3:].split('\\')
    if any(not n or n in ('.', '..') or n[-1] in ('.', ' ') or
           _BAD_SEGMENT.search(n) or _DOS_DEVICE.match(n) for n in names):
        raise VerifiedReaderHold('PATH_COMPONENT')
    if not names[-1].lower().endswith('.md'):
        raise VerifiedReaderHold('EXTENSION')
    if path != str(parsed):  # reject redundant separator/canonicalization surprises
        raise VerifiedReaderHold('PATH_CANONICAL')
    return parsed.parts


def validate_file_metadata(meta: object, expected: ApprovedFile, *, is_parent: bool) -> None:
    """Pure verification of an already-opened handle's BY_HANDLE_FILE_INFORMATION."""
    if meta.attributes & (FILE_ATTRIBUTE_REPARSE_POINT | FILE_ATTRIBUTE_OFFLINE):
        raise VerifiedReaderHold('REPARSE_OR_OFFLINE')
    if is_parent:
        if not meta.attributes & FILE_ATTRIBUTE_DIRECTORY:
            raise VerifiedReaderHold('NOT_DIRECTORY')
        return
    if meta.attributes & FILE_ATTRIBUTE_DIRECTORY or meta.links != 1:
        raise VerifiedReaderHold('DIRECTORY_OR_HARDLINK')
    index = (int(meta.id_high) << 32) | int(meta.id_low)
    size = (int(meta.size_high) << 32) | int(meta.size_low)
    if (meta.volume != expected.volume_serial or index != expected.file_index
            or size != expected.expected_bytes or size > MAX_BYTES):
        raise VerifiedReaderHold('IDENTITY_OR_SIZE')


def _api():
    if sys.platform != 'win32':
        raise VerifiedReaderHold('WINDOWS_ONLY')
    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.CreateFileW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
                                   ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD,
                                   wintypes.HANDLE]
    kernel.CreateFileW.restype = wintypes.HANDLE
    kernel.GetFileInformationByHandle.argtypes = [wintypes.HANDLE,
                                                  ctypes.POINTER(_BY_HANDLE_FILE_INFORMATION)]
    kernel.GetFileInformationByHandle.restype = wintypes.BOOL
    kernel.GetFileType.argtypes = [wintypes.HANDLE]
    kernel.GetFileType.restype = wintypes.DWORD
    kernel.GetVolumeInformationByHandleW.argtypes = [wintypes.HANDLE, wintypes.LPWSTR,
                                                     wintypes.DWORD, ctypes.POINTER(wintypes.DWORD),
                                                     ctypes.c_void_p, ctypes.c_void_p,
                                                     wintypes.LPWSTR, wintypes.DWORD]
    kernel.GetVolumeInformationByHandleW.restype = wintypes.BOOL
    kernel.GetFinalPathNameByHandleW.argtypes = [wintypes.HANDLE, wintypes.LPWSTR,
                                                 wintypes.DWORD, wintypes.DWORD]
    kernel.GetFinalPathNameByHandleW.restype = wintypes.DWORD
    kernel.ReadFile.argtypes = [wintypes.HANDLE, ctypes.c_void_p, wintypes.DWORD,
                                ctypes.POINTER(wintypes.DWORD), ctypes.c_void_p]
    kernel.ReadFile.restype = wintypes.BOOL
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel.CloseHandle.restype = wintypes.BOOL
    return kernel


def _checked_handle(k, name: str, access: int, directory: bool, stack: ExitStack):
    flags = FILE_FLAG_OPEN_REPARSE_POINT | (FILE_FLAG_BACKUP_SEMANTICS if directory else 0)
    h = k.CreateFileW(name, access, FILE_SHARE_READ, None, OPEN_EXISTING, flags, None)
    if not h or h == INVALID_HANDLE_VALUE:
        raise VerifiedReaderHold('CREATE_FILE_DENIED')
    stack.callback(k.CloseHandle, h)
    return h


def _metadata(k, handle):
    meta = _BY_HANDLE_FILE_INFORMATION()
    if not k.GetFileInformationByHandle(handle, ctypes.byref(meta)):
        raise VerifiedReaderHold('HANDLE_METADATA')
    return meta


def _final_path(k, handle):
    buffer = ctypes.create_unicode_buffer(32768)
    n = k.GetFinalPathNameByHandleW(handle, buffer, len(buffer), 0)
    if not n or n >= len(buffer):
        raise VerifiedReaderHold('FINAL_PATH')
    if not buffer.value.startswith('\\\\?\\'):
        raise VerifiedReaderHold('FINAL_PATH')
    return buffer.value[4:]


def _require_ntfs(k, handle):
    fs = ctypes.create_unicode_buffer(64)
    volume = wintypes.DWORD()
    if not k.GetVolumeInformationByHandleW(handle, None, 0, ctypes.byref(volume),
                                            None, None, fs, len(fs)):
        raise VerifiedReaderHold('VOLUME_UNAVAILABLE')
    if fs.value.upper() != 'NTFS':
        raise VerifiedReaderHold('NOT_NTFS')
    return volume.value


def _read_same_handle(k, handle, expected_size: int) -> bytes:
    if expected_size > MAX_BYTES:
        raise VerifiedReaderHold('OVERSIZE')
    result = bytearray()
    while len(result) < expected_size:
        chunk = min(65536, expected_size - len(result))
        buf = ctypes.create_string_buffer(chunk)
        got = wintypes.DWORD()
        if not k.ReadFile(handle, buf, chunk, ctypes.byref(got), None):
            raise VerifiedReaderHold('READ_FAILED')
        if got.value == 0 or got.value > chunk:
            raise VerifiedReaderHold('SHORT_READ')
        result.extend(buf.raw[:got.value])
    # Read one extra byte to detect growth without reopening by path.
    last = ctypes.create_string_buffer(1)
    extra = wintypes.DWORD()
    if not k.ReadFile(handle, last, 1, ctypes.byref(extra), None):
        raise VerifiedReaderHold('EOF_CHECK_FAILED')
    if extra.value != 0:
        raise VerifiedReaderHold('FILE_GREW')
    return bytes(result)


def read_approved_file_source_only(expected: ApprovedFile) -> VerifiedSnapshot:
    """PROTOTYPE ONLY: can open/read on Windows if someone calls explicitly.

    NOT wired to tool dispatch. Intended for synthetic G3 after separate approval.
    Never expose this as a model tool or use it as the permission oracle.
    """
    parts = validate_local_windows_path(expected.absolute_path)
    k = _api()
    with ExitStack() as stack:
        # Keep every parent handle open and non-shareable for rename/delete.
        for i in range(1, len(parts)):
            parent = str(PureWindowsPath(*parts[:i]))
            directory = _checked_handle(k, parent, FILE_READ_ATTRIBUTES, True, stack)
            info = _metadata(k, directory)
            validate_file_metadata(info, expected, is_parent=True)
            _require_ntfs(k, directory)
            if _final_path(k, directory).casefold() != parent.casefold():
                raise VerifiedReaderHold('PARENT_PATH_CHANGED')
        handle = _checked_handle(k, expected.absolute_path,
                                 FILE_READ_DATA | FILE_READ_ATTRIBUTES, False, stack)
        if k.GetFileType(handle) != FILE_TYPE_DISK:
            raise VerifiedReaderHold('NOT_DISK_FILE')
        info = _metadata(k, handle)
        validate_file_metadata(info, expected, is_parent=False)
        if _require_ntfs(k, handle) != expected.volume_serial:
            raise VerifiedReaderHold('WRONG_VOLUME')
        if _final_path(k, handle).casefold() != expected.absolute_path.casefold():
            raise VerifiedReaderHold('FILE_PATH_CHANGED')
        raw = _read_same_handle(k, handle, expected.expected_bytes)
        after = _metadata(k, handle)
        validate_file_metadata(after, expected, is_parent=False)
        if (after.modified.low, after.modified.high) != (info.modified.low, info.modified.high):
            raise VerifiedReaderHold('FILE_MUTATED')
        digest = hashlib.sha256(raw).hexdigest()
        if digest != expected.sha256:
            raise VerifiedReaderHold('HASH_MISMATCH')
        return VerifiedSnapshot(expected.file_id, expected.display_name, digest, raw)


def read_manifest_snapshots_source_only(manifest: Manifest,
                                         selected: tuple[str, ...]) -> tuple[VerifiedSnapshot, ...]:
    """Not a permission check; CALLER must separately check trusted grant/revoke.

    The production dispatcher currently never calls this prototype.
    """
    if not 1 <= len(selected) <= 2 or len(set(selected)) != len(selected):
        raise VerifiedReaderHold('INVALID_SELECTION')
    if not set(selected).issubset(manifest.ids):
        raise VerifiedReaderHold('OUTSIDE_MANIFEST')
    snapshots = tuple(read_approved_file_source_only(manifest.by_id(fid)) for fid in selected)
    if len({(s.file_id, s.sha256) for s in snapshots}) != len(snapshots):
        raise VerifiedReaderHold('DUPLICATE_SNAPSHOT')
    return snapshots
