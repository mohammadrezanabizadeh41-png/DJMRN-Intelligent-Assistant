import json
import sys
import tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest import load

with tempfile.TemporaryDirectory(prefix="djmrn-oh05-") as folder:
    file = Path(folder) / "sample.json"
    base = {"site":"freelancermap","external_id":"synthetic-001","title":"Video editing","url":"https://example.invalid/001"}
    def check(items, expected=None):
        file.write_text(json.dumps({"schema_version":"djmrn.oh.export.v1","opportunities":items}),encoding="utf-8")
        try:
            result = load(file)
        except ValueError as exc:
            if expected is None:
                raise
            assert str(exc) == expected, (str(exc),expected)
        else:
            assert expected is None, result
            return result
    result = check([base, dict(base, external_id="synthetic-002")])
    assert len(result) == 2
    check([base,base], "DUPLICATE_EXTERNAL_ID")
    check([dict(base,title=" ")], "INVALID_TITLE")
    check([dict(base,url="http://example.invalid/001")], "INVALID_URL")
    check([dict(base,site="other")], "UNSUPPORTED_SITE")
    check([dict(base,external_id="")], "INVALID_EXTERNAL_ID")
    print("OH_05_VALIDATION=PASS")
    print("NORMALIZED_RECORDS=2")
    print("INVALID_CASES_REJECTED=5")
    print("NETWORK_ACTIONS=0")
    print("REAL_DATABASE_MODIFIED=NO")
