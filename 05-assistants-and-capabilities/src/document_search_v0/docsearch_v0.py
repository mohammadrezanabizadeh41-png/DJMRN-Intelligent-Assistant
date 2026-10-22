"""DJMRN V0: explicit-allowlist, read-only text lookup. Python standard library only.

Not a sandbox against a hostile process changing filesystem paths concurrently.
No external access, no persistence, and no automatic filesystem recursion.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PureWindowsPath
import re
import sys
import unicodedata

MAX_FILES = 20
MAX_FILE_BYTES = 1024 * 1024  # bound memory and discourage broad private documents
MAX_MATCHES = 100
SUPPORTED_SUFFIXES = frozenset({".txt", ".md", ".csv", ".json"})
DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")
FARSI = str.maketrans({"ي": "ی", "ى": "ی", "ك": "ک"})


class InputRejected(ValueError):
    """An input was outside the deliberately limited V0 contract."""


def normalize(text: str) -> str:
    """Search-only normalization; never modify or rewrite the original text."""
    text = unicodedata.normalize("NFKC", text).translate(FARSI).translate(DIGITS)
    text = text.replace("\u0640", "").replace("\u200c", "")  # Tatweel/ZWNJ: 'می‌رود' ~ 'میرود'
    return re.sub(r"\s+", " ", text).strip().casefold()


def _compact(text: str) -> str:
    # Only for explicitly marked relaxed matches; can match across word boundaries.
    return text.replace(" ", "")


def _safe_file(root: Path, user_path: str) -> tuple[str, Path]:
    if not user_path or any(c in user_path for c in ("\x00", "\r", "\n")):
        raise InputRejected("File name is empty or contains control characters")
    win = PureWindowsPath(user_path)
    if win.is_absolute() or win.drive or user_path.startswith(("/", "\\")):
        raise InputRejected("Only relative file paths are allowed")
    parts = user_path.replace("\\", "/").split("/")
    if not parts or any(p in ("", ".", "..") for p in parts):
        raise InputRejected("Empty, dot or parent path components are not allowed")
    rel = "/".join(parts)
    candidate = root.joinpath(*parts)
    # Reject symlinks and junctions: only regular files below the explicit root.
    cursor = root
    for part in parts:
        cursor = cursor / part
        if cursor.is_symlink() or (hasattr(cursor, "is_junction") and cursor.is_junction()):
            raise InputRejected("Symbolic links or junctions are not allowed")
    try:
        resolved = candidate.resolve(strict=True)
    except (OSError, RuntimeError) as ex:
        raise InputRejected("Requested file does not exist or cannot be resolved") from ex
    if not resolved.is_relative_to(root) or not resolved.is_file():
        raise InputRejected("Requested path is not a regular file within root")
    if resolved.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise InputRejected("Only .txt, .md, .csv, .json files are supported")
    return rel, resolved


def search(root_path: str | Path, selected: list[str], query: str,
           limit: int = 50) -> dict:
    """Return in-memory JSON-safe results; read only the explicitly allowed paths."""
    if not 1 <= limit <= MAX_MATCHES:
        raise InputRejected("Match limit must be between 1 and 100")
    if not selected or len(selected) > MAX_FILES:
        raise InputRejected("Specify between 1 and 20 explicit files")
    needle = normalize(query)
    if not needle:
        raise InputRejected("Search query must not be empty")
    base = Path(root_path)
    if base.is_symlink() or (hasattr(base, "is_junction") and base.is_junction()):
        raise InputRejected("Root must not be a symlink or junction")
    try:
        root = base.resolve(strict=True)
    except (OSError, RuntimeError) as ex:
        raise InputRejected("Root directory does not exist") from ex
    if not root.is_dir():
        raise InputRejected("Root must be an existing directory")
    entries = [_safe_file(root, name) for name in selected]
    if len({p for _, p in entries}) != len(entries):
        raise InputRejected("Duplicate files are not allowed")
    entries.sort(key=lambda item: item[0])

    verified = []
    matches = []
    total_hits = 0
    for rel, file in entries:
        try:
            before = file.stat()
            if before.st_size > MAX_FILE_BYTES:
                raise InputRejected("File exceeds 1 MiB limit")
            raw = file.read_bytes()
            after = file.stat()
        except OSError as ex:
            raise InputRejected("Cannot read a selected file") from ex
        if (len(raw) > MAX_FILE_BYTES or len(raw) != before.st_size or
                after.st_size != before.st_size or after.st_mtime_ns != before.st_mtime_ns):
            raise InputRejected("Selected file changed during reading or exceeds limit")
        try:
            content = raw.decode("utf-8-sig")
        except UnicodeDecodeError as ex:
            raise InputRejected("Selected file is not UTF-8 text") from ex
        digest = hashlib.sha256(raw).hexdigest()
        verified.append({"file": rel, "sha256": digest, "bytes": len(raw)})
        for line_no, line in enumerate(content.splitlines(), 1):
            normalized = normalize(line)
            if not normalized:
                continue
            if needle in normalized:
                mode = "normalized"
            elif _compact(needle) in _compact(normalized):
                mode = "relaxed-whitespace"
            else:
                continue
            total_hits += 1
            if len(matches) < limit:
                matches.append({"file": rel, "line": line_no,
                                "source_sha256": digest, "match_mode": mode,
                                "text": line})
    # Task ID based on request and content fingerprints. Repeatable, no ledger claim.
    fingerprint = json.dumps([needle, verified], ensure_ascii=False,
                             sort_keys=True, separators=(",", ":"))
    task_id = hashlib.sha256(fingerprint.encode("utf-8")).hexdigest()[:20]
    return {"contract_version": "djmrn.document-search.v0",
            "task_id": task_id, "capability": "read-only-line-search",
            "permission_scope": "explicit-files-only/read-only",
            "status": "succeeded", "query": query,
            "normalized_query": needle, "searched": verified,
            "matches": matches, "match_count_returned": len(matches),
            "truncated": total_hits > limit,
            "error": None,
            "note": "relaxed-whitespace matches may cross word boundaries; verify original line"}



def search_preloaded_bytes(documents: list[tuple[str, bytes]], query: str,
                           limit: int = 8) -> dict:
    """Search caller-supplied immutable byte snapshots, with ZERO filesystem reads.

    This is a pure calculation seam for a FUTURE trusted file-handle reader.
    It neither opens paths nor validates who approved these bytes. Its caller
    MUST enforce trusted manifest/file ID, Windows handle identity and grant
    BEFORE supplying data; the current M1 dispatch remains fail-closed.
    Existing search(root, selected, query) and CLI retain their original path
    semantics and do not invoke this entrypoint.
    """
    if type(documents) not in (list, tuple) or not 1 <= len(documents) <= 2:
        raise InputRejected("PRELOADED_FILE_COUNT")
    if type(query) is not str or not 1 <= len(query) <= 512:
        raise InputRejected("PRELOADED_QUERY")
    if any(0xD800 <= ord(char) <= 0xDFFF for char in query):
        raise InputRejected("PRELOADED_QUERY")
    if type(limit) is not int or not 1 <= limit <= 8:
        raise InputRejected("PRELOADED_LIMIT")

    needle = normalize(query)
    if not needle:
        raise InputRejected("PRELOADED_QUERY")
    entries = []
    seen = set()
    for record in documents:
        if type(record) not in (list, tuple) or len(record) != 2:
            raise InputRejected("PRELOADED_RECORD")
        label, raw = record
        if type(label) is not str or not label or any(
            ord(char) < 32 or ord(char) == 127 or
            0xD800 <= ord(char) <= 0xDFFF for char in label
        ):
            raise InputRejected("PRELOADED_LABEL")
        win = PureWindowsPath(label)
        segments = label.replace("\\", "/").split("/")
        if (win.is_absolute() or win.drive or label.startswith(("/", "\\"))
                or any(s in ("", ".", "..") or ":" in s for s in segments)
                or not label.lower().endswith(".md")):
            raise InputRejected("PRELOADED_LABEL")
        label = "/".join(segments)
        if label in seen:
            raise InputRejected("PRELOADED_DUPLICATE")
        seen.add(label)
        if type(raw) is not bytes or len(raw) > MAX_FILE_BYTES:
            raise InputRejected("PRELOADED_BYTES")
        entries.append((label, raw))
    entries.sort(key=lambda item: item[0])

    verified = []
    matches = []
    total_hits = 0
    for label, raw in entries:
        try:
            content = raw.decode("utf-8-sig")
        except UnicodeDecodeError as ex:
            raise InputRejected("PRELOADED_UTF8_INVALID") from ex
        digest = hashlib.sha256(raw).hexdigest()
        verified.append({"file": label, "sha256": digest, "bytes": len(raw)})
        for line_no, line in enumerate(content.splitlines(), 1):
            normalized = normalize(line)
            if not normalized:
                continue
            if needle in normalized:
                mode = "normalized"
            elif _compact(needle) in _compact(normalized):
                mode = "relaxed-whitespace"
            else:
                continue
            total_hits += 1
            if len(matches) < limit:
                matches.append({"file": label, "line": line_no,
                                "source_sha256": digest, "match_mode": mode,
                                "text": line})
    fingerprint = json.dumps([needle, verified], ensure_ascii=False,
                             sort_keys=True, separators=(",", ":"))
    task_id = hashlib.sha256(fingerprint.encode("utf-8")).hexdigest()[:20]
    return {
        "contract_version": "djmrn.document-search.v0",
        "task_id": task_id,
        "capability": "read-only-line-search",
        "permission_scope": "caller-supplied-bytes/NOT-OS-authorized",
        "status": "succeeded",
        "query": query,
        "normalized_query": needle,
        "searched": verified,
        "matches": matches,
        "match_count_returned": len(matches),
        "truncated": total_hits > limit,
        "error": None,
        "note": "Caller alone must verify Windows file identity and user approval; "
                "relaxed-whitespace matches may cross word boundaries",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="DJMRN V0 read-only Persian-aware source search")
    parser.add_argument("--root", required=True, help="Explicit directory containing allowed files")
    parser.add_argument("--file", action="append", required=True,
                        help="Explicit relative path within root; repeat for each file")
    parser.add_argument("--query", required=True, help="Exact text to find with limited normalization")
    parser.add_argument("--limit", type=int, default=50, help="Maximum returned matches (1..100)")
    args = parser.parse_args(argv)
    try:
        result = search(args.root, args.file, args.query, args.limit)
    except InputRejected as ex:
        print(json.dumps({"contract_version": "djmrn.document-search.v0",
                          "status": "rejected", "error": str(ex)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
