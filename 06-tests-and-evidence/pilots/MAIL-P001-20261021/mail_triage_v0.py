"""DJMRN MAIL-P001 -- synthetic-only, offline stdlib triage demo.

Never logs in, downloads, browses, sends, or requests real account permissions.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

BLOCKED = ('us residents only', 'paypal only', 'iran not eligible', 'requires us tax id', 'فقط ساکنان آمریکا')
SUSPICIOUS = ('ignore previous instructions', 'send your password', 'share your otp', 'کد یکبارمصرف را ارسال کن')
FOLLOWUP = ('re:', 'reply:', 'follow-up:', 'پاسخ:', 'پیگیری:')
WORK = ('wordpress', 'python', 'voiceover', 'voice over', 'video editing', 'subtitle', 'logo design', 'طراحی لوگو', 'ساخت سایت', 'تولید محتوا', 'پروژه', 'animation', 'api integration')
OTHER = ('newsletter', 'promotion', 'weekly digest', 'news update', 'تبلیغات', 'خبرنامه')


def classify(record):
    subject = record['subject'].casefold()
    body = record['body'].casefold()
    all_text = subject + '\n' + body
    flags = []
    if any(word in all_text for word in SUSPICIOUS):
        flags.append('UNTRUSTED_INSTRUCTION')
    if any(word in all_text for word in BLOCKED):
        return 'BLOCKED_OR_VERIFY', flags
    if any(subject.startswith(word) for word in FOLLOWUP) or 'client replied' in all_text:
        return 'FOLLOW_UP', flags
    if any(word in all_text for word in WORK):
        return 'OPPORTUNITY_REVIEW', flags
    if any(word in all_text for word in OTHER):
        return 'OTHER', flags
    return 'NEEDS_REVIEW', flags


def extract_budget(body):
    """Conservative dollar-amount example. This is NOT a full contract parser."""
    m = re.search(r'\$\s*([0-9][0-9,]*)', body)
    if not m:
        return None
    return {'amount': int(m.group(1).replace(',', '')),
            'currency': 'USDT' if 'usdt' in body.casefold() else 'USD'}


def analyze(records):
    """Report each source item, group email and portal copies by declared fixture key.

    Uses only local, synthetic supplied records. Never infers real sender identity.
    """
    seen = set()
    observations = []
    for item in records:
        rid = item['id']
        if rid in seen:
            raise ValueError('Duplicate fixture id: ' + rid)
        seen.add(rid)
        if not item['url'].startswith('https://') or '.example/' not in item['url']:
            raise ValueError('Non-fixture URL rejected: ' + rid)
        category, flags = classify(item)
        observations.append({
            'id': rid, 'offer_id': item.get('offer_id', rid), 'kind': item['kind'],
            'category': category, 'flags': flags, 'url': item['url'],
            'subject': item['subject'], 'date': item['received_at'],
            'budget': extract_budget(item['body']),
            'body_complete_in_fixture': bool(item['body'].strip()),
        })
    grouped = {}
    for row in observations:
        key = row['offer_id']
        grouped.setdefault(key, []).append(row)
    canonical = []
    for key, versions in grouped.items():
        selected = next((x for x in versions if x['kind'] == 'portal'), versions[0])
        canonical.append({'offer_id': key, 'selected_source': selected['id'],
                          'category': selected['category'], 'source_count': len(versions),
                          'source_ids': [v['id'] for v in versions],
                          'flags': sorted(set(f for v in versions for f in v['flags'])),
                          'url': selected['url'], 'date': selected['date'],
                          'budget': selected['budget']})
    return {'input_count': len(records), 'unique_offers': len(grouped),
            'source_counts': dict(Counter(o['kind'] for o in observations)),
            'category_counts': dict(Counter(o['category'] for o in canonical)),
            'observations': observations, 'canonical': canonical,
            'no_real_account_access': True, 'no_send_capability': True}


def report_md(result):
    lines = [
        '# گزارش نمونهٔ فرصت‌ها — دادهٔ کاملاً ساختگی', '',
        '> این خروجی صرفاً آزمایش بدون اتصال Gmail، بدون مدل هوش مصنوعی و بدون ورود به سایت است.', '',
        f"- رکوردهای ورودی: {result['input_count']}",
        f"- فرصت‌ها/رشته‌های یکتا بر اساس کلیدهای ساختگی: {result['unique_offers']}",
        f"- دسته‌ها: {', '.join(k+'='+str(v) for k,v in sorted(result['category_counts'].items()))}",
        '', '| دسته | شناسهٔ فرصت ساختگی | منبع منتخب | بودجهٔ استخراج‌شده | تعداد منابع | نشانی ساختگی |',
        '|---|---|---|---:|---|',
    ]
    for x in result['canonical']:
        lines.append(f"| {x['category']} | {x['offer_id']} | {x['selected_source']} | {x['budget']['amount']} {x['budget']['currency'] if x['budget'] else ''} | {x['source_count']} | {x['url']} |" if x['budget'] else f"| {x['category']} | {x['offer_id']} | {x['selected_source']} | نامشخص | {x['source_count']} | {x['url']} |")
    lines += ['', '**محدودیت‌های آزمون:** طبقه‌بندی قاعده‌محور؛ ارزیابی حقوقی/پرداخت یا استخراج کامل قرارداد نیست؛'
              ' هیچ دقت واقعی روی ایمیل‌های حقیقی یا معیار مصرف RAM ویندوز اثبات نشده است.', '']
    return '\n'.join(lines)


def main():
    folder = Path(__file__).resolve().parent
    records = json.loads((folder / 'synthetic_inbox.json').read_text(encoding='utf-8'))
    result = analyze(records)
    print(report_md(result), end='')

if __name__ == '__main__':
    main()
