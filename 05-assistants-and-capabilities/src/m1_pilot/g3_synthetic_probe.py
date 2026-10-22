"""DJMRN G3 synthetic-only Win32 probe. NOT a production file reader.

Default invocation is PLAN ONLY. --run-synthetic is an explicit future user-local
execution action. Creates at most TWO synthetic .md files in a unique local temp
folder, performs narrow source-only negative tests, and deletes ONLY its own
known fixture names and directory (no recursive removal).

Never integrates with SearchSession, Jan, CAP path search, external accounts or model.
"""
from __future__ import annotations

import argparse
import ctypes
from contextlib import ExitStack
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile

# Avoid generating __pycache__ files in the user's checkout.
sys.dont_write_bytecode = True

# Git blob SHA1 values independently read from the canonical private GitHub repo.
PINNED_BLOBS = {
    "core/windows_reader.py": "730f35208dd7f3f08cec3260b4fe7ef775d2faa2",
    "core/manifest.py": "f505b0d3c65a8a421684e3055bc3be12ce19a9a7",
    "core/windows_guard.py": "2ad992932489b1f12417c9e5e5eb4a1d2c40d12a",
}
FIXTURE_BYTES = (
    "# DJMRN Test A\nalpha fixture ONLY\n".encode("utf-8"),
    "# DJMRN Test B\nbeta fixture ONLY\n".encode("utf-8"),
)


def git_blob_id(source: bytes) -> str:
    header = b"blob " + str(len(source)).encode("ascii") + b"\0"
    return hashlib.sha1(header + source).hexdigest()


def verify_local_sources() -> None:
    root = Path(__file__).resolve().parent
    for name, sha in PINNED_BLOBS.items():
        if git_blob_id((root / name).read_bytes()) != sha:
            raise RuntimeError("SOURCE_BLOB_MISMATCH:" + name)


# Verify source bytes BEFORE importing potentially altered local project modules.
verify_local_sources()

from core.manifest import ApprovedFile, Manifest
from core import windows_reader as wr
from core.windows_guard import WindowsGuardHold, require_verified_read

def checked(condition: bool, code: str) -> None:
    if not condition:
        raise RuntimeError(code)


def win_handle_number(h: object) -> int:
    if isinstance(h, int):
        return h
    return int(ctypes.cast(h, ctypes.c_void_p).value or 0)


class HandleTracker:
    """Intercept ONLY CreateFileW/CloseHandle in the isolated test run."""
    def __init__(self, api):
        self.api = api
        self.opened: list[int] = []
        self.closed: list[int] = []

    def __getattr__(self, key):
        return getattr(self.api, key)

    def CreateFileW(self, *args):
        h = self.api.CreateFileW(*args)
        n = win_handle_number(h)
        if n not in (0, wr.INVALID_HANDLE_VALUE):
            self.opened.append(n)
        return h

    def CloseHandle(self, h):
        result = self.api.CloseHandle(h)
        if result:
            self.closed.append(win_handle_number(h))
        return result

    def balanced(self) -> bool:
        from collections import Counter
        return bool(self.opened) and Counter(self.opened) == Counter(self.closed)


def enrollment(path: Path, id: str, fake_bytes: bytes) -> ApprovedFile:
    """Enroll only our just-created synthetic file, via real OS handles."""
    wr.validate_local_windows_path(str(path))
    k = wr._api()
    with ExitStack() as stack:
        h = wr._checked_handle(k, str(path), wr.FILE_READ_ATTRIBUTES,
                               False, stack)
        info = wr._metadata(k, h)
        checked(k.GetFileType(h) == wr.FILE_TYPE_DISK, "ENROLL_NOT_DISK")
        checked(not info.attributes & (wr.FILE_ATTRIBUTE_DIRECTORY |
                     wr.FILE_ATTRIBUTE_REPARSE_POINT | wr.FILE_ATTRIBUTE_OFFLINE),
                "ENROLL_UNSAFE_ATTR")
        checked(info.links == 1, "ENROLL_HARDLINK")
        serial = wr._require_ntfs(k, h)
        checked(serial == info.volume, "ENROLL_VOLUME")
        checked(wr._final_path(k, h).casefold() == str(path).casefold(),
                "ENROLL_FINAL_PATH")
        size = (int(info.size_high) << 32) | int(info.size_low)
        checked(size == len(fake_bytes) and size <= wr.MAX_BYTES,
                "ENROLL_SIZE")
        index = (int(info.id_high) << 32) | int(info.id_low)
        return ApprovedFile(id, path.name, str(path),
                            hashlib.sha256(fake_bytes).hexdigest(),
                            size, int(info.volume), index, int(info.links))


def denial(fn, expected_codes: tuple[str, ...] | None = None) -> str:
    try:
        fn()
    except wr.VerifiedReaderHold as e:
        if expected_codes is not None:
            checked(e.code in expected_codes, "UNEXPECTED_DENIAL:" + e.code)
        return e.code
    raise RuntimeError("FAIL_OPEN")


def run_synthetic() -> dict:
    report: dict = {"project": "DJMRN", "phase": "G3_SYNTHETIC_PROBE",
                    "source": "GitHub pinned source", "cases": {},
                    "overall": "PARTIAL_OR_FAIL", "device_tested": False}

    def run_case(name: str, callback) -> None:
        try:
            detail = callback()
            report["cases"][name] = {"status": "PASS", "detail": str(detail or "OK")}
        except Exception as e:
            report["cases"][name] = {"status": "FAIL", "detail": type(e).__name__}
            raise

    # NEVER create a fixture if the environment is not explicitly Windows.
    checked(sys.platform == "win32", "WINDOWS_ONLY")
    checked(sys.version_info >= (3, 10), "PYTHON_VERSION")
    run_case("G3-00A", verify_local_sources)

    # LOCALAPPDATA is the only selectable fixture parent. Reject UNC/network/temp redirection.
    local_app_data = os.environ.get("LOCALAPPDATA", "")
    checked(bool(local_app_data), "LOCALAPPDATA_ABSENT")
    parent = Path(local_app_data) / "Temp"
    checked(parent.is_dir() and parent.drive and not str(parent).startswith("\\\\"),
            "LOCAL_TEMP_UNAVAILABLE")
    wr.validate_local_windows_path(str(parent / "fake.md"))
    folder = Path(tempfile.mkdtemp(prefix="DJMRN_G3_SYNTHETIC_", dir=parent))
    alpha, beta = folder / "alpha.md", folder / "beta.md"
    created: list[Path] = []
    try:
        for path, raw in zip((alpha, beta), FIXTURE_BYTES):
            with path.open("xb") as f:
                f.write(raw)
            created.append(path)
        a = enrollment(alpha, "doc-alpha", FIXTURE_BYTES[0])
        b = enrollment(beta, "doc-beta", FIXTURE_BYTES[1])
        manifest = Manifest(1, "S-1-5-21-0", (a, b))  # test sentinel, NOT real consent
        report["cases"]["G3-00B"] = {"status": "PASS", "detail": "NTFS_HANDLE_ENROLLMENT"}

        from unittest.mock import patch
        native = wr._api()
        tracker = HandleTracker(native)
        with patch.object(wr, "_api", return_value=tracker):
            def happy():
                rows = wr.read_manifest_snapshots_source_only(manifest,
                                                               ("doc-alpha", "doc-beta"))
                checked(len(rows) == 2 and all(r.raw == raw for r, raw in zip(rows, FIXTURE_BYTES)),
                        "SNAPSHOT_DIFFERENCE")
                checked(all(r.sha256 == hashlib.sha256(r.raw).hexdigest() for r in rows),
                        "SHA_DIFFERENCE")
                return "TWO_SAME_HANDLE_SNAPSHOTS"
            run_case("G3-01", happy)
            run_case("G3-02", lambda: denial(
                lambda: wr.read_manifest_snapshots_source_only(
                    manifest, ("doc-alpha", "doc-third")), ("OUTSIDE_MANIFEST",)))
            run_case("G3-02B", lambda: denial(
                lambda: wr.read_manifest_snapshots_source_only(
                    manifest, ("doc-alpha", "doc-alpha")), ("INVALID_SELECTION",)))

            def guard():
                try:
                    require_verified_read(manifest, ("doc-alpha",))
                except WindowsGuardHold as e:
                    checked(e.code == "FILE_BOUNDARY_UNPROVEN", "GUARD_CHANGED")
                    return "M1_STILL_BLOCKED"
                raise RuntimeError("GUARD_OPENED")
            run_case("G3-07", guard)

            def mutate():
                # Same length; this must hit the SHA verification, not just size.
                different = FIXTURE_BYTES[0].replace(b"alpha", b"omega")
                checked(len(different) == len(FIXTURE_BYTES[0]), "BAD_FIXTURE")
                alpha.write_bytes(different)
                return denial(lambda: wr.read_approved_file_source_only(a),
                              ("HASH_MISMATCH", "FILE_MUTATED"))
            run_case("G3-03", mutate)

            def replaced():
                # Uses the SAME two fixtures, never writes a third .md file.
                os.replace(beta, alpha)
                return denial(lambda: wr.read_approved_file_source_only(a),
                              ("IDENTITY_OR_SIZE", "FILE_PATH_CHANGED"))
            run_case("G3-04", replaced)

        run_case("G3-06", lambda: checked(tracker.balanced(), "HANDLE_LEAK"))
        report["cases"]["G3-05"] = {"status": "NOT_RUN", "detail": "CANCELLATION_UNIMPLEMENTED"}
        report["cases"]["G3-04B"] = {"status": "NOT_RUN", "detail": "REPARSE_AND_CONCURRENT_RACE"}
        report["cases"]["G3-08"] = {"status": "PARTIAL", "detail": "NO_NETWORK_CODE; NOT_MONITORED"}
        report["device_tested"] = True
        report["overall"] = "PARTIAL_G3_HOLD"
    finally:
        # No recursive deletion; remove only fixture paths created by this invocation.
        # If a failure prevents cleanup, leave the folder for user's manual inspection.
        try:
            for path in created:
                if path.is_symlink():
                    continue
                if path.exists() and path.is_file():
                    path.unlink()
            folder.rmdir()
            report["cleanup"] = "OWN_FIXTURES_REMOVED"
        except OSError:
            report["cleanup"] = "MANUAL_CLEANUP_NEEDED"
    return report


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="DJMRN Windows G3 synthetic only")
    p.add_argument("--run-synthetic", action="store_true",
                   help="Execute narrow local Win32 test after user's approval")
    args = p.parse_args(argv)
    if not args.run_synthetic:
        print("G3 PLAN ONLY. No device test executed. Use --run-synthetic only after approval.")
        return 0
    try:
        result = run_synthetic()
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0 if result["overall"] == "PARTIAL_G3_HOLD" else 2
    except Exception as e:
        # Never print filesystem paths, usernames or secrets in error report.
        print(json.dumps({"phase": "G3_SYNTHETIC_PROBE", "overall": "FAIL_HOLD",
                          "error_type": type(e).__name__,
                          "error_code": e.code if isinstance(e, wr.VerifiedReaderHold) else "CHECK_FAILED"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
