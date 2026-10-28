"""OH-05 offline JSON import. No network and no database writes."""
import json
from pathlib import Path
from urllib.parse import urlsplit

def normalize(item):
    if not isinstance(item, dict):
        raise ValueError("INVALID_ITEM")
    site = item.get("site")
    if site != "freelancermap":
        raise ValueError("UNSUPPORTED_SITE")
    values = {}
    for field in ("external_id", "title"):
        value = item.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError("INVALID_" + field.upper())
        values[field] = value.strip()
    url = item.get("url")
    if url is not None:
        if not isinstance(url, str):
            raise ValueError("INVALID_URL")
        parsed = urlsplit(url)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError("INVALID_URL")
    return {"source_site": site, "external_id": values["external_id"], "title": values["title"], "canonical_url": url}

def load(path):
    data = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict) or data.get("schema_version") != "djmrn.oh.export.v1":
        raise ValueError("INVALID_EXPORT_VERSION")
    rows = data.get("opportunities")
    if not isinstance(rows, list) or len(rows) > 1000:
        raise ValueError("INVALID_ROWS")
    result = [normalize(row) for row in rows]
    keys = [(row["source_site"], row["external_id"]) for row in result]
    if len(keys) != len(set(keys)):
        raise ValueError("DUPLICATE_EXTERNAL_ID")
    return result
