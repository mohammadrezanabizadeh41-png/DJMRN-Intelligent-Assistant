# REQ-OBS-001 — DJMRN Live Observability Map
**Status:** USER-REQUESTED FUTURE REQUIREMENT / RESEARCHED 2026-10-20 / NOT IMPLEMENTED / NO PROVIDER SELECTED

## نیاز کاربر
DJMRN باید در آینده یک **نقشهٔ زندهٔ مانیتورینگ/Observability** داشته باشد که اجزای واقعی سیستم و ارتباط میان آن‌ها را به‌صورت بصری و نزدیک به لحظه نمایش دهد؛ ترجیحاً در یک صفحهٔ وب و با حداقل مصرف RAM روی لپ‌تاپ.

این نقشه برای «شنود محتوای پیام‌ها» نیست. هدف، دیدن **کارکرد، رابطه، جریان درخواست/پاسخ، سلامت و مصرف منابع** است.

### اجزایی که باید قابل نمایش باشند
- Coordinator / Host / Workflow
- قابلیت‌ها و دستیارهای تخصصی
- موتورهای inference و مدل‌های محلی/ابری
- Search engineها، APIها و سرویس‌های دریافت داده
- ابزارهای retrieval / file / document search
- DB / durable state / queues در صورت وجود
- GitHub / Notion / cloud services / external websites در صورت مشارکت در یک flow
- local processها و remote endpoints با برچسب واضح LOCAL / CLOUD

### هر Node و Edge چه چیزی نشان دهد
- وضعیت: IDLE / RUNNING / WAITING / ERROR / OFFLINE
- مبدأ و مقصد ارتباط
- request / response / tool-call / model-call / data-fetch / state-write
- شروع/پایان و duration/latency
- حجم تقریبی bytes in/out در صورت قابل‌اندازه‌گیری بودن
- نتیجه success/error و error code بدون افشای payload حساس
- CPU/RAM process در صورت موجود بودن
- provider/model/tool name و trace/task ID
- امکان کلیک روی node/edge و دیدن trace جزئی‌تر

## اصل معماری
این قابلیت باید **OBSERVER / PROJECTION** باشد، نه Authority و نه Control Plane.

```
real components ── real work ──> real components
       └──────── telemetry/events ───────> observer/map
```

خرابی یا بسته‌شدن Dashboard نباید اجرای اصلی دستیار را متوقف کند. کنترل‌هایی مثل Pause/Stop/Approve اگر بعداً لازم شدند باید از مسیر مجوزدار جداگانه اضافه شوند.

## قید RAM و اجرای محلی
- اولویت اول: backend نقشه در cloud و فقط instrumentation/exporter سبک روی لپ‌تاپ.
- در حالت quickstart، اگر SDK بتواند مستقیم OTLP صادر کند، Collector محلی اجباری نیست.
- Dashboard در مرورگر preferably on-demand باز شود، نه همیشه باز.
- payload کامل پیام‌ها به‌طور پیش‌فرض ارسال نشود؛ فقط metadata/trace.
- هر Collector/agent محلی فقط پس از اندازه‌گیری واقعی RAM/CPU پذیرفته شود.
- هدف مهندسی پیشنهادی برای بخش محلی observability: کوچک‌تر از 200–300MB در حالت عادی اگر عملی باشد؛ این **target پروژه** است، نه تضمین ابزار.
- هیچ عدد RAM برای SDK/agent بدون benchmark واقعی روی دستگاه canonical نمی‌شود.

## Shortlist فعلی — 2026-10-20

### 1) Grafana Cloud — PRIMARY RESEARCH CANDIDATE
**Fit:** بسیار بالا برای map آماده، cloud-first و RAM کم محلی.

شواهد رسمی فعلی:
- Free plan = $0، no credit card، free forever.
- Application Observability Free: تا 2,232 host-hours/month.
- Cloud Traces Free: تا 50GB ingest/month و 14-day retention.
- Service Map/Node Graph برای service dependencies، request rate، latency و errors.
- OTLP endpoint رسمی دارد و برای development/testing می‌توان SDKهای OpenTelemetry را **مستقیم** به Cloud فرستاد؛ Collector برای quickstart الزامی نیست.

منابع رسمی:
- https://grafana.com/pricing/
- https://grafana.com/products/cloud/free-tier/
- https://grafana.com/docs/grafana-cloud/send-data/otlp/send-data-otlp/
- https://grafana.com/docs/grafana-cloud/observe-and-act/monitor-applications/application-observability/manual/map/

**Activation gates:** user account/access test، geography/region، privacy/data egress، token handling و مشاهدهٔ دقیق limits قبل از اتصال واقعی. هنوز فعال/انتخاب نشده.

### 2) New Relic Free — STRONG ALTERNATIVE
**Fit:** بالا؛ cloud backend + service map + native OTLP.

شواهد رسمی فعلی:
- perpetual Free tier، no credit card.
- 100GB data ingest/month.
- Service Map روابط dynamic بین applications, databases, hosts, servers و external services را نمایش می‌دهد.
- native OTLP ingest دارد؛ OpenTelemetry SDK می‌تواند مستقیم به endpoint ارسال کند، بنابراین Collector محلی لزوماً لازم نیست.

منابع رسمی:
- https://newrelic.com/pricing/free-tier
- https://docs.newrelic.com/docs/new-relic-solutions/new-relic-one/ui-data/service-maps/service-maps/
- https://docs.newrelic.com/docs/opentelemetry/best-practices/opentelemetry-otlp/

**Activation gates:** access/geography/privacy/user test و quota/overage guardrail قبل از استفادهٔ واقعی.

### 3) Uptrace Cloud — TECHNICALLY GOOD / COST STATUS NEEDS RECONCILIATION
**Fit:** از نظر فنی بسیار خوب؛ live service graph + direct OTLP.

شواهد:
- Service Graph زنده از span relationships می‌سازد و request rate/error/p99 را روی edgeها نشان می‌دهد.
- OTLP direct از SDKها پشتیبانی می‌شود.
- Pricing page می‌گوید Cloud free تا 50GB و 5,000 timeseries/month؛ در عین حال برخی صفحات product عبارت 14-day free trial دارند.

منابع:
- https://uptrace.dev/features/service-graph
- https://uptrace.dev/pricing
- https://uptrace.dev/get

**Status:** FREE/COST = **UNVERIFIED-CONFLICTING** تا account-level terms و card/overage رفتار تأیید شود؛ بنابراین فعلاً default نیست.

### 4) Jaeger All-in-One — LOCAL/OFFLINE FALLBACK CANDIDATE
**Fit:** مناسب برای development/local tracing اگر cloud نخواهیم.

شواهد رسمی:
- Windows پشتیبانی می‌شود.
- all-in-one در یک process اجرا می‌شود و transient in-memory storage دارد.
- UI شامل Dependencies/System Architecture graph است.
- در in-memory mode dependency graph از traceهای حافظه on-demand محاسبه می‌شود.
- OTLP ports 4317/4318 را می‌پذیرد.

منابع:
- https://www.jaegertracing.io/docs/2.22/getting-started/
- https://www.jaegertracing.io/docs/2.22/deployment/windows/
- https://www.jaegertracing.io/docs/2.22/faq/

**RAM status:** حداقل RAM رسمی قابل اتکایی پیدا نشد = **UNKNOWN**. چون storage پیش‌فرض حافظه‌ای است، تا benchmark کوچک با trace limit انجام نشود نباید always-on انتخاب شود.

### 5) Custom lightweight web viewer — FALLBACK IF READY-MADE TOOLS FAIL FIT
یک event stream بسیار کوچک (SSE/WebSocket/JSON) + graph در browser. مزیت: فقط metadata مورد نیاز DJMRN، احتمالاً footprint محلی بسیار کم. عیب: کد و نگهداری اختصاصی. قبل از ساخت باید ابزار آماده شکست خورده یا نامناسب ثابت شود.

## گزینه‌های فعلاً کنارگذاشته‌شده
- **Grafana OSS local as default:** حداقل رسمی 512MB RAM و برای small deployment خود Grafana 2–4GB توصیه می‌شود؛ backendهای metrics/logs/traces جداگانه منابع خودشان را می‌خواهند. برای لپ‌تاپ کم‌RAM ما default مناسبی نیست.
- **SigNoz Cloud:** Cloud فعلی از $49/month بعد از trial شروع می‌شود؛ با Free-First پروژه سازگار نیست. Self-host Community وجود دارد اما برای این requirement تا وقتی نیاز اثبات نشده، stack محلی اضافی توجیه ندارد.

منابع:
- https://grafana.com/docs/grafana/latest/setup-grafana/installation/
- https://signoz.io/pricing/

## قرارداد telemetry پیشنهادی اولیه
کمینهٔ event/span:
```
component_id
component_role
location = local|cloud
status
trace_id / parent_trace_id / task_id
from / to
event_type
started_at / ended_at / duration_ms
bytes_in / bytes_out
cpu_pct / ram_mb        # when measurable
provider / model / tool
result = success|error
error_code              # sanitized
```

**Default deny:** prompt متن کامل، document content، secret/token/API key، cookie/session، customer data و credential در telemetry ارسال نشوند مگر policy جداگانه و approval مشخص.

## Acceptance criteria آینده
1. حداقل 5 نوع component واقعی را روی map نشان دهد.
2. ارتباط جهت‌دار و near-live بین componentها دیده شود.
3. local/cloud و provider مشخص باشد.
4. running/idle/error و latency/request rate قابل مشاهده باشد.
5. trace یک task از user/coordinator تا tool/model/search/state قابل دنبال‌کردن باشد.
6. برای processهای محلی RAM/CPU در صورت دسترسی نشان داده شود.
7. بسته‌شدن map هیچ اثر functional روی system نداشته باشد.
8. telemetry حساس redacted/omitted باشد.
9. local observability overhead روی Windows اندازه‌گیری و ثبت شود.
10. provider/quota/cost/privacy/region قبل از activation دوباره live-verified شود.

## ترتیب اجرای آینده
1. ابتدا Grafana Cloud Free را با synthetic telemetry کوچک و **direct OTLP بدون Collector** امتحان کن، اگر account/access/privacy gate پاس شد.
2. همان synthetic flow را با New Relic Free به‌عنوان رقیب مقایسه کن.
3. اگر cloud مناسب نبود، Jaeger All-in-One را فقط on-demand با trace volume محدود benchmark کن.
4. Uptrace فقط بعد از رفع ابهام free-tier/cost.
5. custom viewer فقط اگر گزینهٔ آماده نتوانست requirement را با RAM/هزینه/امنیت مناسب برآورده کند.

این سند **نیاز آینده و shortlist پژوهشی** است؛ مجوز نصب، signup، token creation، ارسال telemetry، cloud activation یا انتخاب معماری نهایی نیست.
