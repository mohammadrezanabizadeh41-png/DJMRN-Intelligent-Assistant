"""OH-25: explicitly approved, two-ID guarded detail import into existing DJMRN SQLite.

No network or outreach. Source data are two independently SHA-pinned OH07 captures.
Retains a verified physical SQLite backup even if the write transaction fails.
"""
import argparse
import hashlib
import importlib.util
import json
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

PARSER_SHA256 = 'f5d26fa1c341cbcbaa69075cb3320bd58f39731c78700fcb944754e670e91061'
TARGETS = {
    '3066367': (43, '4ac5cb2a96a9ebe7d38a5b0db9408631cab4f1de14088e1bf227065da847d39d'),
    '3066375': (36, '907565709d7a8851c606da04994d44beffc6a07bae17c7a30a7e9fc022c41310'),
}
CORE = ('metadata', 'opportunities', 'opportunity_history', 'outbound_attempts')
EXPECTED = {'opportunities': 44, 'opportunity_history': 44, 'outbound_attempts': 0}
TOKEN = 'OH25-STORE-TWO-DETAILS'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def table_rows(db, table):
    return db.execute('SELECT * FROM ' + table + ' ORDER BY rowid').fetchall()


def fingerprint(db, table):
    return hashlib.sha256(repr(table_rows(db, table)).encode('utf-8')).hexdigest()


def state(db):
    tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if not set(CORE + ('opportunity_details',)).issubset(tables):
        raise RuntimeError('MISSING_EXPECTED_TABLES')
    if db.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
        raise RuntimeError('INTEGRITY_CHECK_FAILED')
    if db.execute('SELECT value FROM metadata WHERE key=?', ('schema_version',)).fetchone() != ('djmrn.oh.local.v1',):
        raise RuntimeError('SCHEMA_VERSION_FAILED')
    columns = [r[1] for r in db.execute('PRAGMA table_info(opportunity_details)')]
    if columns != ['opportunity_id', 'official_id', 'structured_json']:
        raise RuntimeError('DETAIL_COLUMNS_CHANGED')
    indices = {r[1] for r in db.execute('PRAGMA index_list(opportunity_details)') if r[2] == 1}
    if 'ux_detail_official' not in indices:
        raise RuntimeError('DETAIL_UNIQUE_INDEX_MISSING')
    if db.execute('PRAGMA foreign_key_check').fetchall():
        raise RuntimeError('FOREIGN_KEY_CHECK_FAILED')
    for name, count in EXPECTED.items():
        if db.execute('SELECT COUNT(*) FROM ' + name).fetchone()[0] != count:
            raise RuntimeError('UNEXPECTED_TABLE_COUNT_' + name)
    details = db.execute('SELECT COUNT(*) FROM opportunity_details').fetchone()[0]
    if details not in (2, 4):
        raise RuntimeError('UNEXPECTED_DETAIL_COUNT')
    return {name: fingerprint(db, name) for name in CORE + ('opportunity_details',)}


def load(parser_path, detail_paths):
    if digest(parser_path) != PARSER_SHA256:
        raise RuntimeError('PARSER_SHA_MISMATCH')
    spec = importlib.util.spec_from_file_location('djmrn_oh23', parser_path)
    parser = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parser)
    if len(detail_paths) != 2:
        raise RuntimeError('EXACTLY_TWO_CAPTURE_PATHS_REQUIRED')
    objects = {}
    for path in detail_paths:
        raw = Path(path).read_bytes()
        d = json.loads(raw.decode('utf-8-sig'))
        obj = parser.parse(d)
        official = obj.get('official_id')
        if official not in TARGETS or official in objects:
            raise RuntimeError('UNEXPECTED_OR_DUPLICATE_CAPTURE')
        if hashlib.sha256(raw).hexdigest() != TARGETS[official][1]:
            raise RuntimeError('CAPTURE_HASH_MISMATCH')
        if 'Similar projects' in (obj.get('application_form') or ''):
            raise RuntimeError('FORM_CONTAMINATION')
        objects[official] = obj
    if set(objects) != set(TARGETS):
        raise RuntimeError('CAPTURE_SET_INCOMPLETE')
    return objects


def reconcile(db, objects):
    for official, obj in objects.items():
        rows = db.execute('''SELECT id FROM opportunities WHERE source_site=?
            AND (external_id=? OR external_id=? OR canonical_url=?)''',
            (obj['site'], obj['export_external_id'], official, obj['url'])).fetchall()
        if rows != [(TARGETS[official][0],)]:
            raise RuntimeError('IDENTITY_NOT_UNIQUE_' + official)
        other = db.execute('SELECT opportunity_id FROM opportunity_details WHERE official_id=?', (official,)).fetchall()
        if other and other != [(TARGETS[official][0],)]:
            raise RuntimeError('OFFICIAL_ID_COLLISION_' + official)
        current = db.execute('SELECT official_id, structured_json FROM opportunity_details WHERE opportunity_id=?',
            (TARGETS[official][0],)).fetchone()
        payload = json.dumps(obj, sort_keys=True, ensure_ascii=False)
        if current is not None and current != (official, payload):
            raise RuntimeError('EXISTING_DETAIL_CONFLICT_' + official)


def run(a):
    if a.approve != TOKEN:
        raise RuntimeError('EXPLICIT_TWO_DETAIL_APPROVAL_REQUIRED')
    dbpath = Path(a.database).resolve(strict=True)
    backup_dir = Path(a.backups).resolve(strict=True)
    if not backup_dir.is_dir():
        raise RuntimeError('BACKUP_DIRECTORY_INVALID')
    if dbpath.parent == backup_dir:
        raise RuntimeError('BACKUP_MUST_BE_SEPARATE_FROM_DATABASE')
    objects = load(a.parser, a.details)
    ro_uri = dbpath.as_uri() + '?mode=ro'
    rw_uri = dbpath.as_uri() + '?mode=rw'
    with closing(sqlite3.connect(ro_uri, uri=True, timeout=10)) as ro:
        ro.execute('PRAGMA query_only=ON')
        original = state(ro)
        reconcile(ro, objects)
        fd, backup_name = tempfile.mkstemp(prefix='opportunities-pre-oh25-', suffix='.sqlite3', dir=str(backup_dir))
        import os
        os.close(fd)
        backup = Path(backup_name)
        print('OH25_BACKUP_FILE=' + str(backup), flush=True)
        with closing(sqlite3.connect(backup)) as dest:
            ro.backup(dest)
        with closing(sqlite3.connect(backup.as_uri() + '?mode=ro', uri=True)) as copy:
            if state(copy) != original:
                raise RuntimeError('BACKUP_SNAPSHOT_MISMATCH')
            reconcile(copy, objects)
        print('OH25_BACKUP_VERIFIED=PASS', flush=True)
    with closing(sqlite3.connect(rw_uri, uri=True, timeout=10, isolation_level=None)) as db:
        db.execute('PRAGMA foreign_keys=ON')
        db.execute('BEGIN IMMEDIATE')
        try:
            if state(db) != original:
                raise RuntimeError('DATABASE_CHANGED_AFTER_BACKUP')
            reconcile(db, objects)
            before_old = db.execute('''SELECT opportunity_id, official_id, structured_json
                FROM opportunity_details WHERE opportunity_id NOT IN (36,43) ORDER BY opportunity_id''').fetchall()
            count_before = db.execute('SELECT COUNT(*) FROM opportunity_details').fetchone()[0]
            events = []
            for official, obj in objects.items():
                local_id = TARGETS[official][0]
                payload = json.dumps(obj, sort_keys=True, ensure_ascii=False)
                old = db.execute('SELECT official_id,structured_json FROM opportunity_details WHERE opportunity_id=?',
                    (local_id,)).fetchone()
                if old is None:
                    db.execute('INSERT INTO opportunity_details(opportunity_id,official_id,structured_json) VALUES(?,?,?)',
                        (local_id, official, payload))
                    events.append('NEW')
                elif old == (official, payload):
                    events.append('SEEN')
                else:
                    raise RuntimeError('UNEXPECTED_DETAIL_CONFLICT')
            if events not in (['NEW', 'NEW'], ['SEEN', 'SEEN']):
                raise RuntimeError('PARTIAL_IMPORT_NOT_ALLOWED')
            if db.execute('''SELECT opportunity_id, official_id, structured_json
                FROM opportunity_details WHERE opportunity_id NOT IN (36,43) ORDER BY opportunity_id''').fetchall() != before_old:
                raise RuntimeError('EXISTING_DETAILS_CHANGED')
            if any(fingerprint(db, name) != original[name] for name in CORE):
                raise RuntimeError('CORE_ROWS_CHANGED')
            new_count = db.execute('SELECT COUNT(*) FROM opportunity_details').fetchone()[0]
            if new_count != (count_before + 2 if events[0] == 'NEW' else count_before) or new_count != 4:
                raise RuntimeError('DETAIL_COUNT_MISMATCH')
            if db.execute('PRAGMA foreign_key_check').fetchall():
                raise RuntimeError('FOREIGN_KEY_FAILURE')
            if db.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                raise RuntimeError('PRECOMMIT_INTEGRITY_FAILURE')
            db.execute('COMMIT')
        except BaseException:
            db.execute('ROLLBACK')
            raise
        print('OH25_EVENTS=' + ','.join(events), flush=True)
        print('OH25_PRODUCTION_DETAIL_ROWS=' + str(new_count), flush=True)
    with closing(sqlite3.connect(ro_uri, uri=True)) as verify:
        final = state(verify)
        for table in CORE:
            if final[table] != original[table]:
                raise RuntimeError('POSTCOMMIT_CORE_CHANGED; RETAIN_BACKUP=' + str(backup))
        reconcile(verify, objects)
        if verify.execute('SELECT COUNT(*) FROM opportunity_details').fetchone()[0] != 4:
            raise RuntimeError('POSTCOMMIT_DETAIL_COUNT_BAD; RETAIN_BACKUP=' + str(backup))
    print('OH25_POSTCOMMIT_INTEGRITY=PASS')
    print('OH25_CORE_ROWS_UNCHANGED=YES')
    print('OH25_BACKUP_RETAINED=YES')
    print('OUTBOUND_ACTIONS=0')
    print('OH25_PRODUCTION_DETAIL_IMPORT=PASS')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--database', required=True)
    ap.add_argument('--parser', required=True)
    ap.add_argument('--backups', required=True)
    ap.add_argument('--details', nargs=2, required=True)
    ap.add_argument('--approve', default='')
    run(ap.parse_args())


if __name__ == '__main__':
    main()
