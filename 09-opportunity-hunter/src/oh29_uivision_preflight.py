"""OH-29: bounded, read-only Ui.Vision CLI/Windows OpportunityHunter preflight.

Does not launch Chrome/Ui.Vision, inspect cookies, read credentials, alter SQLite,
or write anything. GitHub source only; Windows execution requires user receipt.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import sqlite3
from contextlib import closing

EXPECTED_TABLES = ('opportunities', 'opportunity_history', 'opportunity_details', 'outbound_attempts')
MACRO_NAMES = (
    'DJMRN-OH07-Freelancermap-Single-Detail-ReadOnly.json',
    'DJMRN-OH05-Freelancermap-Export-Pilot.json',
)


def bounded_launch_pages(roots):
    """Scan at most 60 immediate subfolders per root; never descend farther."""
    found = set()
    for base in roots:
        if not base.is_dir() or base.is_symlink():
            continue
        target = base / 'ui.vision.html'
        if target.is_file():
            found.add(str(target.resolve()))
        try:
            children = sorted((p for p in base.iterdir() if p.is_dir() and not p.is_symlink()), key=lambda p: p.name.casefold())
            for folder in children[:60]:
                target = folder / 'ui.vision.html'
                if target.is_file():
                    found.add(str(target.resolve()))
        except OSError:
            continue
    return sorted(found)[:10]


def inspect_local(environ, database):
    env = {str(k).upper(): str(v) for k, v in environ.items()}
    home = Path(env.get('USERPROFILE') or str(Path.home()))
    local = Path(env.get('LOCALAPPDATA') or str(home / 'AppData' / 'Local'))
    program = Path(env.get('PROGRAMFILES') or 'C:/Program Files')
    program86 = Path(env.get('PROGRAMFILES(X86)') or 'C:/Program Files (x86)')
    project = local / 'DJMRN' / 'OpportunityHunter'
    chrome_options = (
        program / 'Google/Chrome/Application/chrome.exe',
        program86 / 'Google/Chrome/Application/chrome.exe',
        local / 'Google/Chrome/Application/chrome.exe',
    )
    chrome = next((str(p) for p in chrome_options if p.is_file()), None)
    if not chrome:
        from_path = shutil.which('chrome.exe', path=env.get('PATH'))
        if from_path:
            chrome = str(Path(from_path))
    roots = (
        home / 'Downloads', home / 'Documents', home / 'Desktop',
        project / 'exports', home / 'uivision',
    )
    launches = bounded_launch_pages(roots)
    macro_roots = (
        home / 'uivision' / 'macros', home / 'Documents' / 'uivision' / 'macros',
        project / 'exports',
    )
    macros = {name: [str(folder / name) for folder in macro_roots if (folder / name).is_file()] for name in MACRO_NAMES}
    dbpath = Path(database)
    if not dbpath.is_file():
        raise RuntimeError('PRODUCTION_DB_MISSING')
    uri = dbpath.resolve(strict=True).as_uri() + '?mode=ro'
    with closing(sqlite3.connect(uri, uri=True, timeout=6)) as db:
        db.execute('PRAGMA query_only=ON')
        if db.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise RuntimeError('DB_INTEGRITY_FAILED')
        version = db.execute('SELECT value FROM metadata WHERE key=?', ('schema_version',)).fetchone()
        if version != ('djmrn.oh.local.v1',):
            raise RuntimeError('DB_SCHEMA_UNEXPECTED')
        counts = {name: db.execute('SELECT COUNT(*) FROM '+name).fetchone()[0] for name in EXPECTED_TABLES}
    if counts != {'opportunities':44, 'opportunity_history':44, 'opportunity_details':4, 'outbound_attempts':0}:
        raise RuntimeError('DB_COUNTS_CHANGED_REVIEW_REQUIRED:' + json.dumps(counts, sort_keys=True))
    return {
        'chrome_found': bool(chrome), 'chrome_path': chrome,
        'cli_launch_page_found': bool(launches), 'cli_launch_page_paths': launches,
        'local_macro_files': macros,
        'macro_in_browser_storage': 'UNVERIFIED',
        'cli_run_tested': False,
        'db_counts': counts,
        'database_access': 'READ_ONLY',
        'outbound_actions': 0,
        'next_gate': ('CLI_LAUNCH_SMOKE_PILOT' if chrome and launches else
                      'GENERATE_UIVISION_API_HTML_ONCE' if chrome else 'VERIFY_CHROME_EXECUTABLE'),
    }


def main():
    a = argparse.ArgumentParser(description='OH-29 read-only CLI discovery, no browser launch')
    a.add_argument('--database', required=True)
    opts = a.parse_args()
    info = inspect_local(os.environ, opts.database)
    print('OH29_WINDOWS_INVENTORY=PASS')
    print('CHROME_FOUND=' + ('YES' if info['chrome_found'] else 'NO'))
    print('CHROME_PATH=' + str(info['chrome_path'] or 'NOT_FOUND'))
    print('UIVISION_CLI_HTML_FOUND=' + ('YES' if info['cli_launch_page_found'] else 'NO'))
    print('UIVISION_CLI_HTML_PATHS=' + json.dumps(info['cli_launch_page_paths'], ensure_ascii=False))
    print('LOCAL_MACROS=' + json.dumps(info['local_macro_files'], ensure_ascii=False, sort_keys=True))
    print('BROWSER_MACROS_VERIFIED=NO')
    print('CLI_INVOCATION_VERIFIED=NO')
    print('SQLITE_COUNTS=' + json.dumps(info['db_counts'], sort_keys=True))
    print('NEXT_GATE=' + info['next_gate'])
    print('PRODUCTION_SQLITE_WRITES=0; OUTBOUND_ACTIONS=0')


if __name__ == '__main__':
    main()
