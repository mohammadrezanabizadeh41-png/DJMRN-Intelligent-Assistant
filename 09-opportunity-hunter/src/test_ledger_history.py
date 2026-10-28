import sqlite3
import tempfile
import sys
from contextlib import closing
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from ledger_history import prepare, record_with_history

with tempfile.TemporaryDirectory(prefix="djmrn-oh04-history-") as temp:
    path = str(Path(temp)/"synthetic.sqlite3")
    with closing(sqlite3.connect(path)) as db, db:
        db.execute("CREATE TABLE opportunities(id INTEGER PRIMARY KEY,source_site TEXT NOT NULL,external_id TEXT NOT NULL,canonical_url TEXT,title TEXT NOT NULL,status TEXT NOT NULL DEFAULT 'DISCOVERED',created_utc TEXT NOT NULL,UNIQUE(source_site,external_id))")
    prepare(path)
    item = dict(source_site="freelancermap",external_id="demo-1",title="Original",canonical_url="https://example.invalid/1")
    assert record_with_history(path,item)["event"] == "NEW"
    with closing(sqlite3.connect(path)) as db, db:
        db.execute("UPDATE opportunities SET status='SENT' WHERE external_id='demo-1'")
    assert record_with_history(path,item)["event"] == "SEEN"
    item["title"] = "Revised"
    result = record_with_history(path,item)
    assert result["event"] == "UPDATED" and result["status"] == "SENT"
    with closing(sqlite3.connect(path)) as db:
        row = db.execute("SELECT status,title FROM opportunities").fetchone()
        history = db.execute("SELECT event FROM opportunity_history ORDER BY id").fetchall()
        count = db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    assert row == ("SENT","Revised") and history == [("NEW",),("UPDATED",)] and count == 1
    print("OH_04_HISTORY_SYNTHETIC=PASS")
    print("STATUS_PRESERVED=SENT")
    print("HISTORY_EVENTS=NEW,UPDATED")
    print("FINAL_COUNT=1")
    print("REAL_DATABASE_MODIFIED=NO")
