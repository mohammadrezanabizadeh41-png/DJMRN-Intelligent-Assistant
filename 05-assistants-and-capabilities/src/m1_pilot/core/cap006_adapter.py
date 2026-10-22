"""Read-only legacy CAP-006 result validation/mapping, NO live call enabled.

The legacy CAP-006 algorithm itself remains unchanged. An approved file-ID
manifest and Win32 guarded read must precede any real search. Since the existing
CAP-006 reopens a path, it is UNSAFE to call it solely after path prechecks.
This adapter intentionally exposes only pure mapping of an already sourced
legacy result. A future trusted reader must independently prove same-byte
identity before wiring real search.
"""
from __future__ import annotations

import re

from .manifest import Manifest

_SHA = re.compile(r"^[0-9a-f]{64}$", re.ASCII)


class InvalidLegacyResult(ValueError):
    pass


def map_legacy_result(legacy: dict, manifest: Manifest, approved_ids: tuple[str, ...],
                      *, response_byte_limit: int = 16 * 1024,
                      max_line_bytes: int = 1024) -> dict:
    """Pure translator, not file reader or verification of source identity."""
    if not isinstance(legacy, dict) or legacy.get("status") != "succeeded":
        raise InvalidLegacyResult("CAP_NOT_SUCCESS")
    if not 1 <= len(approved_ids) <= 2 or len(set(approved_ids)) != len(approved_ids):
        raise InvalidLegacyResult("SCOPE")
    if not set(approved_ids).issubset(manifest.ids):
        raise InvalidLegacyResult("UNKNOWN_FILE_ID")
    by_display = {manifest.by_id(fid).display_name: manifest.by_id(fid)
                  for fid in approved_ids}
    if len(by_display) != len(approved_ids):
        raise InvalidLegacyResult("AMBIGUOUS_DISPLAY_NAME")
    searched = legacy.get("searched")
    found = legacy.get("matches")
    if type(searched) is not list or type(found) is not list or len(found) > 8:
        raise InvalidLegacyResult("CAP_OUTPUT_SHAPE")
    if len(searched) != len(approved_ids):
        raise InvalidLegacyResult("CAP_SEARCHED_SCOPE")
    source = []
    seen = set()
    for item in searched:
        if type(item) is not dict or item.get("file") not in by_display:
            raise InvalidLegacyResult("UNEXPECTED_FILE")
        spec = by_display[item["file"]]
        if (item["file"] in seen or item.get("sha256") != spec.sha256
                or type(item.get("bytes")) is not int
                or item["bytes"] != spec.expected_bytes):
            raise InvalidLegacyResult("SOURCE_IDENTITY_MISMATCH")
        seen.add(item["file"])
        source.append({"file_id": spec.file_id, "display_name": spec.display_name,
                       "sha256": spec.sha256, "bytes": spec.expected_bytes})
    hits = []
    for m in found:
        if type(m) is not dict or m.get("file") not in seen:
            raise InvalidLegacyResult("UNEXPECTED_MATCH_FILE")
        spec = by_display[m["file"]]
        txt = m.get("text")
        if (type(txt) is not str or type(m.get("line")) is not int or m["line"] < 1
                or len(txt.encode("utf-8")) > max_line_bytes
                or m.get("source_sha256") != spec.sha256
                or m.get("match_mode") not in ("normalized", "relaxed-whitespace")):
            raise InvalidLegacyResult("UNVERIFIED_MATCH")
        hits.append({"file_id": spec.file_id, "line": m["line"], "text": txt,
                     "source_sha256": spec.sha256, "match_mode": m["match_mode"]})
    result = {"searched": source, "matches": hits, "truncated": legacy.get("truncated")}
    if type(result["truncated"]) is not bool:
        raise InvalidLegacyResult("INVALID_TRUNCATION")
    import json
    if len(json.dumps(result, ensure_ascii=False).encode("utf-8")) > response_byte_limit:
        raise InvalidLegacyResult("OUTPUT_LIMIT")
    return result
