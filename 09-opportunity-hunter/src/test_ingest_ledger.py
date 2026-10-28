"""OH-05 offline import-to-ledger integration on a temporary SQLite copy."""
import os
import json
import sqlite3
import sys
import tempfile
from pathlib import Path
from contextlib import closing
sys.path.insert(0,str(Path(__file__).resolve().parent))
from ingest import load
from ledger_history import record_with_history

source=Path(os.environ["DJMRN_OH_DB"])
with tempfile.TemporaryDirectory(prefix="djmrn-oh05-ledger-") as temp:
    folder=Path(temp)
    replica=folder/"replica.sqlite3"
    sample=folder/"sample.json"
    with closing(sqlite3.connect(source.as_uri()+"?mode=ro",uri=True)) as src:
        with closing(sqlite3.connect(replica)) as dst:
            src.backup(dst)
    with closing(sqlite3.connect(replica)) as db:
        version=db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()[0]
    assert version=="djmrn.oh.local.v1"
    base={"site":"freelancermap","external_id":"synthetic-oh05-1","title":"Video editing","url":"https://example.invalid/1"}
    second=dict(base,external_id="synthetic-oh05-2",title="Automation")
    sample.write_text(json.dumps({"schema_version":"djmrn.oh.export.v1","opportunities":[base,second]}),encoding="utf-8")
    rows=load(sample)
    first=[record_with_history(str(replica),row) for row in rows]
    repeated=[record_with_history(str(replica),row) for row in rows]
    with closing(sqlite3.connect(replica)) as db, db:
        db.execute("UPDATE opportunities SET status='SENT' WHERE external_id='synthetic-oh05-1'")
    base["title"]="Video editing updated"
    sample.write_text(json.dumps({"schema_version":"djmrn.oh.export.v1","opportunities":[base,second]}),encoding="utf-8")
    updated=[record_with_history(str(replica),row) for row in load(sample)]
    with closing(sqlite3.connect(replica)) as db:
        events=db.execute("SELECT event FROM opportunity_history ORDER BY id").fetchall()
        count=db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
        status=db.execute("SELECT status FROM opportunities WHERE external_id='synthetic-oh05-1'").fetchone()[0]
        integrity=db.execute("PRAGMA integrity_check").fetchone()[0]
    assert [x["event"] for x in first]==["NEW","NEW"]
    assert [x["event"] for x in repeated]==["SEEN","SEEN"]
    assert [x["event"] for x in updated]==["UPDATED","SEEN"]
    assert events==[("NEW",),("NEW",),("UPDATED",)]
    assert count==2 and status=="SENT" and integrity=="ok"
    print("OH_05_LEDGER_INTEGRATION=PASS")
    print("EVENTS=NEW,SEEN,UPDATED")
    print("HISTORY_ROWS=3")
    print("FINAL_COUNT=2")
    print("STATUS_PRESERVED=SENT")
    print("REAL_DATABASE_MODIFIED=NO")
print("TEMP_COPY_CLEANUP=PASS")
