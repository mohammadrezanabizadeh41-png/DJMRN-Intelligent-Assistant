"""Local operator manifest metadata only. NOT an OS grant or filesystem proof."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import PureWindowsPath
import re

_ID = re.compile(r"^[a-z][a-z0-9-]{1,31}$", re.ASCII)
_SHA = re.compile(r"^[0-9a-f]{64}$", re.ASCII)


class ManifestError(ValueError):
    pass


@dataclass(frozen=True)
class ApprovedFile:
    file_id: str
    display_name: str
    absolute_path: str  # trusted process only; never serialize to model
    sha256: str
    expected_bytes: int
    volume_serial: int
    file_index: int
    link_count: int = 1

    def __post_init__(self):
        path = PureWindowsPath(self.absolute_path)
        if (not _ID.fullmatch(self.file_id) or not path.is_absolute()
                or path.drive.startswith("\\\\") or not path.drive.endswith(":")
                or path.suffix.lower() != ".md"
                or any(part in ("", ".", "..") for part in path.parts[1:])
                or ":" in str(path)[2:] or "\x00" in str(path)):
            raise ManifestError("INVALID_LOCAL_MD_PATH")
        if (type(self.display_name) is not str or not self.display_name
                or any(ord(c) < 32 for c in self.display_name)):
            raise ManifestError("INVALID_DISPLAY_NAME")
        if type(self.sha256) is not str or not _SHA.fullmatch(self.sha256):
            raise ManifestError("INVALID_SHA256")
        for value in (self.expected_bytes, self.volume_serial, self.file_index):
            if type(value) is not int or value < 0:
                raise ManifestError("INVALID_FILE_IDENTITY")
        if self.expected_bytes > 1024 * 1024 or self.link_count != 1:
            raise ManifestError("INELIGIBLE_FILE")


@dataclass(frozen=True)
class Manifest:
    """Created only by trusted local control after its own file identification."""
    revision: int
    owner_sid: str
    files: tuple[ApprovedFile, ...]

    def __post_init__(self):
        if type(self.revision) is not int or self.revision <= 0:
            raise ManifestError("INVALID_REVISION")
        if not isinstance(self.owner_sid, str) or not self.owner_sid.startswith("S-1-"):
            raise ManifestError("INVALID_OWNER")
        if type(self.files) is not tuple or not 1 <= len(self.files) <= 2:
            raise ManifestError("INVALID_COUNT")
        if len({f.file_id for f in self.files}) != len(self.files):
            raise ManifestError("DUPLICATE_FILE_ID")
        if len({(f.volume_serial, f.file_index) for f in self.files}) != len(self.files):
            raise ManifestError("DUPLICATE_FILE_IDENTITY")

    @property
    def ids(self) -> frozenset[str]:
        return frozenset(f.file_id for f in self.files)

    @property
    def digest(self) -> str:
        # Includes local paths only in local digest. Do not send serialized manifest.
        rows = [[f.file_id, f.absolute_path, f.sha256, f.expected_bytes,
                 f.volume_serial, f.file_index] for f in self.files]
        canonical = json.dumps([self.revision, self.owner_sid, rows],
                               ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def by_id(self, fid: str) -> ApprovedFile:
        for f in self.files:
            if f.file_id == fid:
                return f
        raise ManifestError("UNKNOWN_FILE_ID")
