# موتورها، میزبان‌ها، مدل‌ها — تاریخی و جداسازی مفاهیم
هر نام در یکی از دسته‌های `HOST/UI`, `INFERENCE ENGINE`, `MODEL WEIGHTS`, `AGENT CLI`, `EMBEDDING` تعریف می‌شود. مدل/موتور/Agent را یک محصول فرض نکنید. منبع: [Windows Journal](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3) 2026-10-17/19.

## Host و Engine
| نام | evidence تاریخی | وضعیت/محدودیت |
|---|---|---|
| Jan Desktop | INSTALLED/UI LAUNCHED، Local API `127.0.0.1:1337/v1` tested; 내부 llama.cpp reported `0.5.0` build b11146 | API server **قبلاً** مدل‌ها را برگردانده، current RUNNING = UNKNOWN |
| Jan Agent مستقل | نصب/CLI نسخه `jan 0.8.6-64` از **agent-nightly**؛ محدود file-read pilot | nightly risk؛ default safety/tool boundaries independent validation pending |
| llama.cpp standalone | موجود/گزارش‌شده، کار با GGUF/CPU inference قبلاً داشته | lifecycle GPU/system load not current benchmark |
| Ollama | INSTALLED / CLI+SERVICE tested `0.40.6-rc1` | snapshot `ollama list` خالی؛ current model library UNKNOWN |
| LM Studio classic | INSTALLED / UI LAUNCHED | model `google/gemma-4-e4b` download دیده شد اما UI load ~79% stalled؛ NOT PASS |
| LM Studio Bionic | INSTALLED/USER REPORTED UI LAUNCHED | مستقلاً capability agent tool call اثبات نشده |
| Hermes Agent | در Windows قبلی سابقه دارد، **پس از reinstall گزارش NO LONGER PRESENT** | نامزد پژوهش، نه نصب فعلی |

## وزن مدل‌ها (Jan import/list + آزمایش‌های قبلی)
| مدل | evidence | احتیاط |
|---|---|---|
| Jan-v3.5-4B | مدل واردشده؛ پاسخ فارسی و فایل‌خوانی محدود در Jan Agent reported، ~4 tok/s UI snapshot | پایلوت production/reliable agent نیست |
| Gemma 3 1B QAT Q4_0 | واردشده؛ inference user-reported + streaming API basic | license/tool-call competence جداگانه بررسی شود |
| Gemma 3 4B QAT Q4_0 | import؛ basic reply success reported؛ Vulkan ErrorOutOfDeviceMemory در برخی runs، Jinja role alternation failure در Jan Agent | **partial failure** مهم؛ مدل را صرفاً FAILED کلی ننامید |
| Gemma 3 12B Q2_K | import؛ CPU-only پاسخ داده، ~1 tok/s در نمونه گزارش‌شده و کند؛ OOM در یک سناریوی قدیمی | size/RAM/context and quality unbenchmarked fairly |
| all-MiniLM-L6-v2 | در Jan embedding catalog listed | دانلود/استفادهٔ embedding جداگانه **UNVERIFIED** |
| Gemma 4 E4B in LM Studio | file download reported، LOAD STALLED | نه inference success و نه علت خطا قطعی |

## سیاست ارزیابی منصفانه
- گذشته سرمایهٔ شواهد است نه تصمیم. مدل/engine/host نوظهور و حتی گزینهٔ «بدون مدل» را از صفر با همین task، منبع و معیار بسنجید؛ دانلود مدل‌ها فقط در صورت نیاز و اجازه.
- یک مدل/worker سنگین همزمان برای شروع روی 8GB، مگر شواهد بهتر؛ peak RAM، KV cache، context، CPU/GPU, latency, Persian capability, tool correctness و license/Free cost را جدا گزارش کنید.
- از listing Jan، نتیجهٔ API، سرعت یک UI snapshot یا مدل روی دیسک ادعای عامل مستقلِ قابل‌اعتماد نسازید.
