"""DJMRN G3-B experimental two-fixture Win32 negative probe. NOT a model tool.

DEFAULT: plan-only.  --run-synthetic still requires the local operator to type RUN.
No Windows execution is authorized by committing this source; separate approval needed.
No Junction creation, OS I/O cancel, third fixture file, administrator or network API.
"""
from __future__ import annotations

import argparse
from contextlib import ExitStack
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from threading import Lock
from unittest.mock import patch

sys.dont_write_bytecode = True

# Exact previous GitHub blobs. Refuse altered project source before importing it.
PINNED = {
    "g3_synthetic_probe.py": "1988282914635940e485dc246a0b6ff0fc87db6b",
    "core/windows_reader.py": "730f35208dd7f3f08cec3260b4fe7ef775d2faa2",
    "core/manifest.py": "f505b0d3c65a8a421684e3055bc3be12ce19a9a7",
    "core/windows_guard.py": "2ad992932489b1f12417c9e5e5eb4a1d2c40d12a",
}


def git_blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def verify_pinned_sources(root: Path) -> None:
    for relative, expected in PINNED.items():
        if git_blob_id((root / relative).read_bytes()) != expected:
            raise ProbeHold("SOURCE_BLOB_MISMATCH")


class ProbeHold(RuntimeError):
    """Only static, sanitized error codes: no paths, usernames or token leakage."""


class DeliveryFence:
    """Only a TEST delivery fence. NOT application consent or OS ReadFile cancel.

    Caller must ensure one owner holds the delivery gate over actual publishing.
    This sample cannot guarantee it once the result has been returned.
    """
    def __init__(self) -> None:
        self._lock = Lock()
        self._revoked = False

    def revoke(self) -> None:
        with self._lock:
            self._revoked = True

    def call(self, read_callback):
        with self._lock:
            if self._revoked:
                raise ProbeHold("REVOKED_BEFORE_READ")
        snapshot = read_callback()
        with self._lock:
            if self._revoked:
                raise ProbeHold("REVOKED_BEFORE_DELIVERY")
            return snapshot  # only within a test call, not a production publisher


def no_network_audit(event: str, _args: tuple) -> None:
    """Fail-closed for Python audit-level socket/process events only; not native egress."""
    if event.startswith("socket.") or event in ("subprocess.Popen", "os.system"):
        raise ProbeHold("PYTHON_NETWORK_OR_PROCESS_DENIED")


def fixture_cleanup(folder: Path | None, created: list[Path]) -> str:
    """No recursive delete. Only own two known filenames and empty directory."""
    if folder is None:
        return "NO_FIXTURE_CREATED"
    try:
        for path in created:
            # Do not follow any inserted symlink or reparse target during cleanup.
            if path.is_symlink():
                return "MANUAL_CLEANUP_REQUIRED"
            if path.is_file():
                path.unlink()
        folder.rmdir()
    except OSError:
        return "MANUAL_CLEANUP_REQUIRED"
    return "OWN_FIXTURES_REMOVED"


def execute_synthetic() -> dict:
    result = {
        "phase": "G3B_TWO_SYNTHETIC_FILES", "device_tested": False,
        "cases": {}, "overall": "G3B_HOLD", "cleanup": "NO_FIXTURE_CREATED",
    }
    def case(name: str, fn) -> bool:
        try:
            detail = fn()
            result["cases"][name] = {"status": "PASS", "detail": str(detail or "OK")}
            return True
        except Exception as exc:
            result["cases"][name] = {"status": "FAIL", "detail": type(exc).__name__}
            return False

    # Zero local file changes until every preflight below has succeeded.
    if sys.platform != "win32":
        raise ProbeHold("WINDOWS_ONLY")
    if sys.version_info < (3, 10):
        raise ProbeHold("PYTHON_TOO_OLD")
    root = Path(__file__).resolve().parent
    verify_pinned_sources(root)
    from core import windows_reader as wr
    from core.windows_guard import WindowsGuardHold, require_verified_read
    from core.manifest import Manifest
    from g3_synthetic_probe import enrollment, FIXTURE_BYTES, HandleTracker

    local = os.environ.get("LOCALAPPDATA", "")
    if not local:
        raise ProbeHold("LOCALAPPDATA_MISSING")
    parent = Path(local) / "Temp"
    if not parent.is_dir() or not parent.drive or str(parent).startswith("\\\\"):
        raise ProbeHold("LOCAL_NTFS_TEMP_REQUIRED")
    wr.validate_local_windows_path(str(parent / "fixture.md"))

    folder = None
    created: list[Path] = []
    sys.addaudithook(no_network_audit)
    try:
        folder = Path(tempfile.mkdtemp(prefix="DJMRN_G3B_SYNTHETIC_", dir=parent))
        alpha, beta = folder / "alpha.md", folder / "beta.md"
        for path, raw in zip((alpha, beta), FIXTURE_BYTES):
            with path.open("xb") as f:
                f.write(raw)
            created.append(path)
        a = enrollment(alpha, "doc-alpha", FIXTURE_BYTES[0])
        b = enrollment(beta, "doc-beta", FIXTURE_BYTES[1])
        Manifest(1, "S-1-5-21-0", (a, b))  # synthetic-only sentinel NOT consent
        result["cases"]["G3B-00"] = {"status": "PASS", "detail": "PINNED_NTFS_TWO_FIXTURES"}
        original_api = wr._api()
        tracker = HandleTracker(original_api)
        with patch.object(wr, "_api", return_value=tracker):
            def positive():
                snaps = [wr.read_approved_file_source_only(x) for x in (a, b)]
                if [x.raw for x in snaps] != list(FIXTURE_BYTES):
                    raise ProbeHold("SNAPSHOT_WRONG_BYTES")
                return "SAME_HANDLE_APPROVED_A_B"
            if not case("G3B-01", positive):
                raise ProbeHold("POSITIVE_CONTROL_FAILED")

            def held_rename():
                # This is a BOUNDED attempted rename, NOT an adversarial race test.
                # Both paths are our existing two fixtures: no third file created.
                with ExitStack() as held:
                    parent_h = wr._checked_handle(tracker, str(folder),
                                          wr.FILE_READ_ATTRIBUTES, True, held)
                    parent_meta = wr._metadata(tracker, parent_h)
                    wr.validate_file_metadata(parent_meta, a, is_parent=True)
                    if wr._require_ntfs(tracker, parent_h) != a.volume_serial:
                        raise ProbeHold("PARENT_VOLUME_CHANGED")
                    if wr._final_path(tracker, parent_h).casefold() != str(folder).casefold():
                        raise ProbeHold("PARENT_CHANGED")
                    leaf_h = wr._checked_handle(tracker, str(alpha),
                       wr.FILE_READ_DATA | wr.FILE_READ_ATTRIBUTES, False, held)
                    wr.validate_file_metadata(wr._metadata(tracker, leaf_h), a, is_parent=False)
                    if wr._final_path(tracker, leaf_h).casefold() != str(alpha).casefold():
                        raise ProbeHold("HELD_LEAF_PATH_CHANGED")
                    try:
                        os.replace(alpha, beta)
                    except OSError as exc:
                        # Explicit Windows sharing/access-denied codes, NOT arbitrary OS error.
                        if getattr(exc, "winerror", None) not in (5, 32):
                            raise ProbeHold("RENAME_UNEXPECTED_ERROR") from None
                    else:
                        raise ProbeHold("UNEXPECTED_RENAME_SUCCEEDED")
                # Full recheck after release. A and B are still the same fixtures.
                for item, expected_raw in ((a, FIXTURE_BYTES[0]), (b, FIXTURE_BYTES[1])):
                    if wr.read_approved_file_source_only(item).raw != expected_raw:
                        raise ProbeHold("POST_RENAME_IDENTITY_CHANGED")
                return "RENAME_BLOCKED_WHILE_HELD"
            if not case("G3B-03", held_rename):
                raise ProbeHold("RENAME_TEST_FAILED")

            def revoke_before():
                gate = DeliveryFence()
                gate.revoke()
                try:
                    gate.call(lambda: wr.read_approved_file_source_only(a))
                except ProbeHold as exc:
                    if str(exc) == "REVOKED_BEFORE_READ":
                        return "TEST_ONLY_PRE_READ_DENIED"
                raise ProbeHold("BEFORE_READ_FAIL_OPEN")
            if not case("G3B-05A", revoke_before):
                raise ProbeHold("REVOKE_BEFORE_FAILED")

            def revoke_during():
                gate = DeliveryFence()
                original_read = wr._read_same_handle
                def test_read(k, handle, length):
                    raw = original_read(k, handle, length)
                    gate.revoke()  # injected between successful read and delivery
                    return raw
                with patch.object(wr, "_read_same_handle", side_effect=test_read):
                    try:
                        gate.call(lambda: wr.read_approved_file_source_only(a))
                    except ProbeHold as exc:
                        if str(exc) == "REVOKED_BEFORE_DELIVERY":
                            return "TEST_ONLY_POST_READ_BLOCKED"
                raise ProbeHold("REVOKED_SNAPSHOT_DELIVERED")
            if not case("G3B-05B", revoke_during):
                raise ProbeHold("REVOKE_DURING_FAILED")

            def unchanged_guard():
                try:
                    require_verified_read()
                except WindowsGuardHold as exc:
                    if exc.code == "FILE_BOUNDARY_UNPROVEN":
                        return "ASSISTANT_FILE_GUARD_CLOSED"
                raise ProbeHold("GUARD_OPEN")
            if not case("G3B-09", unchanged_guard):
                raise ProbeHold("GUARD_CHANGED")
        if not case("G3B-07", lambda: "TRACKED_HANDLES_CLOSED" if tracker.balanced()
                    else (_ for _ in ()).throw(ProbeHold("HANDLE_IMBALANCE"))):
            raise ProbeHold("HANDLE_IMBALANCE")

        # None of the following is a PASS. Never fill these from mock results.
        result["cases"]["G3B-02"] = {"status": "NOT_RUN", "detail": "REAL_REPARSE_REQUIRES_SEPARATE_FIXTURE_DESIGN"}
        result["cases"]["G3B-04"] = {"status": "NOT_RUN", "detail": "ACTIVE_CONCURRENT_RACE_UNTESTED"}
        result["cases"]["G3B-05"] = {"status": "PARTIAL", "detail": "TEST_DELIVERY_FENCE_ONLY_NOT_PRODUCTION_REVOKE"}
        result["cases"]["G3B-06"] = {"status": "NOT_RUN", "detail": "OS_IO_CANCELLATION_DEFERRED"}
        result["cases"]["G3B-08"] = {"status": "PARTIAL", "detail": "PYTHON_AUDIT_ONLY_NO_NATIVE_EGRESS_PROOF"}
        result["device_tested"] = True
        result["overall"] = "G3B_PARTIAL_HOLD"
    except Exception as exc:
        result["overall"] = "FAIL_HOLD"
        result["stop_reason"] = str(exc) if isinstance(exc, ProbeHold) else type(exc).__name__
    finally:
        result["cleanup"] = fixture_cleanup(folder, created)
        if result["cleanup"] != "OWN_FIXTURES_REMOVED":
            result["overall"] = "FAIL_HOLD"
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="DJMRN G3-B synthetic-only candidate")
    parser.add_argument("--run-synthetic", action="store_true",
                        help="Only after separate user authorization for new G3-B Windows run")
    args = parser.parse_args(argv)
    if not args.run_synthetic:
        print("G3-B PLAN ONLY / DEVICE NOT RUN / GUARD CLOSED / NO USER APPROVAL ASSUMED")
        return 0
    try:
        if sys.platform != "win32":
            raise ProbeHold("WINDOWS_ONLY")
        decision = input("New G3-B consent required. Type RUN or Enter to abort: ").strip()
        if decision != "RUN":
            print("G3-B ABORTED / NOTHING EXECUTED")
            return 0
        data = execute_synthetic()
        print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2))
        return 0 if data["overall"] == "G3B_PARTIAL_HOLD" else 2
    except Exception as exc:
        # Full path / winerror details deliberately excluded from response.
        code = str(exc) if isinstance(exc, ProbeHold) else type(exc).__name__
        print(json.dumps({"phase": "G3B_TWO_SYNTHETIC_FILES", "overall": "FAIL_HOLD",
                          "error_code": code if code.isupper() and len(code) < 80 else "CHECK_FAILED"},
                          ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
