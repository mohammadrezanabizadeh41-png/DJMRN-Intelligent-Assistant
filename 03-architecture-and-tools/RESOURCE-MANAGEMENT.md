# پایهٔ مدیریت منابع Windows — ضرورت و دامنه
نیاز اعلام‌شده: قبل از چند دستیار سنگین، مصرف واقعی RAM/CPU و پردازه‌ها مدیریت شود تا مرورگر و کار روزمره لطمه نبینند. تحقیقات Applied A0010/A0011 دربارهٔ گزینه‌های آماده vs controller کوچک قبلاً ثبت شده‌اند؛ **manager تصویب/نصب نشده**.

## سؤال‌های تصمیم
- چه چیزی در Windows Task Manager/Task Scheduler/PowerShell/Job Objects/engine model unload و برنامه‌های آماده از قبل هست؟
- کدام بخش واقعاً به هماهنگ‌کنندهٔ کوچک نیاز دارد (admission control, queue, owned-child lifecycle, documentable restart state)؟
- آیا با حذف loading همزمان و انتخاب مدل سبک مسئله حل می‌شود؟
- چه ابزار Windows-native ساده‌تر از سرویس دائمی است؟
- آیا idle overhead میزبان از منفعت آن کمتر است؟
- fail modes: OOM, GPU UMA, pagefile thrash, process orphan, failed stop, task retry duplicate, post-crash unknown external effect؛ چگونه safe stop/recover می‌شود؟

## معیار خروج تحقیق
مقایسهٔ همان fixtures با گزینهٔ deterministic no-manager، ابزار آماده و minimal custom controller؛ گزارش cost/fit/observability/reversibility و هزینه نگهداری. بدون benchmark لپ‌تاپ، برتری memory claim نکنید. ماشین **8GiB installed** با ~2-3 GiB usual free در snapshots، نه 6GiB physical.

[Applied A0011 archived raw](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Research-Bridge/blob/main/responses/A0011.md) فقط ورودی مطالعه است؛ انتخاب معماری و مجوز ساخت نیست.
