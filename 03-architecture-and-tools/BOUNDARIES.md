# مرزهای منطقی احتمالی — نه میکروسرویس و نه اجزای ساخته‌شده
- **Intent/Task:** درخواست فارسی با شناسه/اولویت و محدودهٔ عملیات مجاز.
- **Executor:** deterministic function یا caller مدل/Agent انتخابی، تنها در محدودهٔ مجوز.
- **Resource Controller:** بودجه RAM/CPU، صف و lifecycle فرایندهایی که خود برنامه مالکشان است؛ از دسترسی kill فرایندهای unrelated خودداری.
- **Tool Adapter:** فقط API/فایل/وب رسمی مجاز، explicit credentials خارج از GitHub، timeout/retry/least privilege.
- **Knowledge Retriever:** خواندن منابع canonical و projection read-only قابل بازسازی؛ source/page/id/version/revision/hash و stale flag.
- **Durable State:** اگر برای job واقعی نیاز شد یک authority واحد؛ receipt/idempotency/reconcile پیش از sending externally. هیچ DB جدید انتخاب نشده.
- **Observer:** test, outcome, log, cost, resource usage؛ خروجی را با evidence و date ثبت کند.

این‌ها **semantic boundaries** هستند، نه تأیید ساخت چند کلاس/سرویس/Agent. ابتدا محصول آماده یا یک جریان سادهٔ کاملاً قابل آزمون را بیازمایید. برای هر domain purpose, I/O, ownership, auth و dependencies را هنگام طراحی نهایی بنویسید.
