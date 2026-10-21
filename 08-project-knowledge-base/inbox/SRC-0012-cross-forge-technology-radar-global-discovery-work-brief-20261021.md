DJMRN — WORK DEEP RESEARCH REQUEST DRAFT

عنوان پیشنهادی:
Cross-Forge Technology Radar & High-Impact Project Discovery
شناسایی منابع جهانی انتشار/ترند فناوری و کشف پروژه‌های بسیار ارزشمند برای آیندهٔ DJMRN

پروژهٔ مقصد:
repository_full_name:
mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant

branch:
main

نکته:
قبل از تبدیل این متن به WQ اجرایی، شمارهٔ واقعی WQ بعدی و مسیر متناظر WA را از وضعیت زندهٔ همان مخزن تعیین کن.
هیچ شماره‌ای را از روی این متن حدس نزن.

==================================================
1. مأموریت اصلی
==================================================

یک پژوهش عمیق، مستقل، Technology-Neutral و مبتنی بر منابع روز انجام بده تا:

A) مهم‌ترین سایت‌ها، Forgeها، Model/Project Hubها، Package Registryها، Research Hubها و Community Signal Sourceهایی را که فناوری‌ها و پروژه‌های جدید در آنها ظاهر می‌شوند شناسایی کنی.

B) مشخص کنی برای کشف پروژه‌هایی شبیه مواردی که اخیراً برای DJMRN جالب بوده‌اند، کدام منابع بیشترین Signal-to-Noise را دارند.

نمونهٔ نوع پروژه‌های موردنظر، فقط برای Calibration و نه ایجاد Bias:

- Ruflo / Claude Flow:
  agent orchestration / swarm / MCP / memory / routing

- Ollama / llama.cpp / LM Studio / vLLM / SGLang:
  local/cloud inference / serving / model lifecycle / low-RAM architecture

- Zie619/n8n-workflows:
  workflow/template libraries / automation reuse

هدف محدود به این پروژه‌ها نیست.

باید پروژه‌هایی را پیدا کنی که هنوز کاربر و پروژهٔ DJMRN آنها را نمی‌شناسند.

==================================================
2. سؤال اصلی
==================================================

اگر بخواهیم یک «رادار فناوری جهانی» برای DJMRN داشته باشیم که فناوری‌ها و پروژه‌های جدید، جدی، سریع‌الرشد و واقعاً مفید را زود تشخیص دهد:

- کدام منابع باید دیده شوند؟
- چگونه باید آنها را اولویت‌بندی کرد؟
- اکنون چه پروژه‌های بسیار مهمی در آنها وجود دارد؟
- کدام پروژه‌ها می‌توانند مستقیماً معماری، قابلیت‌ها، هزینه، RAM، بهره‌وری یا فرصت‌های آیندهٔ DJMRN را تغییر دهند؟
- چه چیزهایی فقط Hype هستند و چه چیزهایی Evidence واقعی دارند؟

==================================================
3. پروتکل اجباری پروژه
==================================================

قبل از پژوهش:

1. دقیقاً این repository را verify کن:

mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant

2. branch = main را verify کن.

3. از همان مخزن بخوان:

04-work-research-bridge/REPOSITORY-LOCK.md

04-work-research-bridge/README.md

PROJECT-RULES.md

07-operations-and-continuity/CURRENT-STATUS.md

WQ واقعی مربوط به این درخواست

و اسناد مرتبط معماری/دانشنامه.

4. پروتکل Applied Library + Independent Search مندرج در Work Bridge را کامل رعایت کن.

5. Applied Capability Index و Applied Mission زنده را بخوان.

6. شاخه‌های مرتبط General Discovery و Applied Library را واقعاً مطالعه کن.

7. فناوری موجود در Library را صرفاً دوباره فهرست نکن.

8. سرچ مستقل باید بدون Bias از نامزدهای قبلی انجام شود.

9. Work فقط WA شمارهٔ متناظر را در مسیر مجاز ثبت کند.

10. هیچ فایل پروژهٔ دیگری را تغییر نده.

==================================================
4. اصل مهم: سه نوع Source را جدا کن
==================================================

SOURCE TYPE A — PRIMARY PROJECT / CODE SOURCE

جایی که خود پروژه، کد، release یا artifact اصلی وجود دارد.

مثلاً:
GitHub
GitLab
Codeberg
SourceHut
Bitbucket
Gitee
SourceForge
Hugging Face repositories
و سایر Forgeهای معتبر.

SOURCE TYPE B — DISCOVERY / SIGNAL SOURCE

جایی که می‌فهمیم یک پروژه یا فناوری در حال مطرح‌شدن است.

مثلاً:
GitHub Trending
Hacker News / Show HN
Product Hunt
Lobsters
DEV / Forem
Reddit technical communities
community newsletters
specialized trend pages
developer discussions.

SOURCE TYPE C — PRIMARY VERIFICATION SOURCE

جایی که ادعای پروژه را راستی‌آزمایی می‌کنیم.

مثلاً:
official repository
official documentation
official release notes
model card
official benchmark
research paper
vendor documentation.

قاعده:

Signal Source
↓
Primary Source
↓
Verification
↓
Analysis

نه:

Trending post
↓
Fact

==================================================
5. Forge / Code Hosting Universe
==================================================

حداقل این منابع را بررسی و وضعیت فعلی‌شان را verify کن:

GitHub

GitLab

Codeberg / Forgejo ecosystem

SourceHut

Bitbucket

Gitee

SourceForge

و هر Forge فعال دیگری که independent search نشان دهد برای فناوری‌های جدید ارزش واقعی دارد.

برای هرکدام مشخص کن:

- public-project discovery
- trending/explore capability
- search quality
- stars/forks/watchers equivalent
- release data
- activity metadata
- API
- RSS/webhook if any
- anonymous/public access
- rate limits
- geographic/access concerns
- usefulness for DJMRN Radar.

مهم:

صرف Git hosting بودن کافی نیست.

مثلاً اگر یک Forge پروژه‌های بسیار خوبی دارد ولی mechanism کشف ضعیفی دارد، می‌تواند Secondary Source باشد نه Primary Radar Source.

==================================================
6. GitHub باید عمیق‌تر بررسی شود
==================================================

GitHub فقط با Trending بررسی نشود.

حداقل بررسی کن:

Trending:
daily
weekly
monthly

Repository Search

Topics

Stars

Forks

Recent creation

Recent update

Releases

Release velocity

Issues / PR activity

Contributor activity

Official organization repositories

Awesome lists فقط به عنوان Discovery Signal

GitHub Discussions در صورت ارزش

Search queryهایی مثل:

created:
pushed:
stars:
language:
topic:

را برای Discovery strategy بررسی کن.

هدف:
پروژهٔ بزرگ قدیمی را با پروژهٔ جدیدی که به‌سرعت در حال رشد است اشتباه نگیریم.

==================================================
7. GitLab
==================================================

GitLab نیز مستقل بررسی شود.

از جمله:

Explore/Public Projects
Projects API
Releases API
topics
stars
recent activity
self-managed/open-source ecosystems if discoverable.

بررسی کن آیا GitLab برای Discovery مستقیم ارزش بالایی دارد یا بیشتر Secondary Forge است.

==================================================
8. Codeberg / Forgejo
==================================================

Codeberg و Forgejo ecosystem را جدی ولی بدون پیش‌فرض بررسی کن.

ممکن است پروژه‌های:

privacy-first
open-source
independent
self-hosted

مهمی قبل از مطرح‌شدن در GitHub در این ecosystem ظاهر شوند.

بررسی کن:

Explore
API
RSS
repository activity
release discovery
trend signal

واقعاً چقدر قابل استفاده است.

اگر سرچ مستقل نشان داد Signal پایین است، آن را صریحاً Secondary اعلام کن.

==================================================
9. SourceHut
==================================================

SourceHut را برای پروژه‌های developer-centric و hacker-oriented بررسی کن.

ارزیابی کن:

public projects
discoverability
mailing-list activity
API/feed
releases
serious technical projects

و مشخص کن آیا ارزش inclusion دائمی دارد.

==================================================
10. Bitbucket / Gitee / SourceForge
==================================================

این منابع را صرفاً به خاطر معروف‌بودن وارد Core Radar نکن.

بررسی کن:

آیا واقعاً برای کشف پروژه‌های جدید و نوآور Signal می‌دهند؟

Gitee را مخصوصاً برای ecosystem چین بررسی کن.

Bitbucket را از نظر public innovation discovery در برابر enterprise hosting بسنج.

SourceForge را برای پروژه‌های mature/legacy و release distribution بررسی کن.

==================================================
11. Hugging Face Hub — اولویت بسیار بالا
==================================================

Hugging Face برای DJMRN یک منبع درجه‌اول است.

حداقل بررسی شود:

Models

Datasets

Spaces

Trending Models

Trending Spaces

New Models

Recently Updated

Model Cards

Downloads / Likes

Tasks

Libraries

Organizations

Daily Papers

Trending Papers:
Daily
Weekly
Monthly

Collections

Webhooks/API

برای Modelها مواردی مانند:

parameters
quantization
architecture
modality
license
downloads
likes
hardware implications
inference support
local feasibility

را بررسی کن.

برای Spaces:

AI app / demo / agent / workflow / MCP / media tools

را جست‌وجو کن.

==================================================
12. Research Sources
==================================================

حداقل بررسی شوند:

arXiv

OpenReview

Hugging Face Papers

conference proceedings when relevant

research lab release pages

و سایر منابع معتبر.

اما Paper صرفاً به دلیل novelty نباید پروژهٔ پیشنهادی شود.

باید مشخص شود:

paper only
code available
model available
reproducible
production candidate
experimental only.

==================================================
13. Product / Launch Signals
==================================================

Product Hunt را بررسی کن:

Developer Tools

Open Source

Artificial Intelligence

Workflow Automation

Productivity

Design Tools

Video/Image/Audio AI

Coding

Agents

اما آن را Primary Evidence Source تلقی نکن.

همچنین شرایط فعلی Product Hunt API را بررسی کن، چون ممکن است محدودیت استفادهٔ تجاری داشته باشد.

هر Candidate مهم:

Product Hunt Signal
↓
Official Project
↓
Verify

==================================================
14. Hacker News
==================================================

Hacker News مخصوصاً:

Show HN

Top

New

Best

و discussionهای پروژه‌های فنی را بررسی کن.

هدف:

کشف early technical projects.

HN popularity = signal
نه proof.

برای Candidateهای مهم باید repository/docs اصلی پیدا شود.

==================================================
15. Developer Communities
==================================================

بررسی هدفمند:

Lobsters

DEV / Forem

Reddit engineering/AI/open-source communities

specialized forums

اما فقط برای:

early signal
real-user experience
negative evidence

استفاده شوند.

ادعای فنی باید به Primary Source برگردد.

==================================================
16. Package Registries
==================================================

پروژه‌های مهم همیشه ابتدا در Trending ظاهر نمی‌شوند.

بررسی کن:

PyPI

npm

crates.io

Go packages/ecosystem if useful

Docker Hub

GitHub Container Registry where discoverable

و registryهای تخصصی دیگر.

سیگنال‌های مهم:

new package
rapid downloads
rapid version velocity
new major version
dependency adoption
container activity.

اما package download metrics می‌توانند misleading باشند؛ آنها را تنها معیار popularity نکن.

==================================================
17. AI-specific Hubs خارج از Hugging Face
==================================================

به صورت مستقل وضعیت فعلی این خانواده را بررسی کن:

ModelScope

Kaggle Models

Replicate model ecosystem

OpenRouter model ecosystem صرفاً در صورت relevance

vendor model catalogs

و هر AI Hub معتبر جدید در 2026.

هدف:
کشف مدل/ابزار/اپی که در GitHub/Hugging Face دیده نمی‌شود.

==================================================
18. Vendor Release Sources
==================================================

برای تغییرات بنیادی فناوری، صفحات رسمی این ecosystemها نیز بررسی شوند:

OpenAI

Anthropic

Google / Google DeepMind

Microsoft

Meta

NVIDIA

AMD

Intel

Hugging Face

Cloudflare

Vercel

GitHub

GitLab

Docker

LangChain

Microsoft AI ecosystems

و هر vendor مرتبط دیگری.

اما اینها Radar مکمل‌اند، نه substitute برای open-source discovery.

==================================================
19. حوزه‌های موردعلاقهٔ DJMRN
==================================================

سرچ باید حداقل این حوزه‌ها را پوشش دهد:

Agent systems

Multi-Agent

Assistant platforms

Agent orchestration

Agent runtimes

Agent harnesses

Workflow engines

Automation

Workflow template libraries

MCP

A2A

Agent Skills

Tool protocols

Tool registries

Model routers

AI gateways

Inference engines

Local LLM

Low-RAM inference

Quantization

Model loading/unloading

KV cache

Prefix caching

Multi-model serving

Cloud inference

Serverless AI

Distributed inference

RAG

Retrieval

Knowledge management

Agent memory

Vector search

Databases for AI

Observability

Agent observability

Live system maps

Tracing

Security

Sandboxing

Permission systems

Human approval

Browser agents

Computer-use agents

Coding agents

Code review

Testing agents

Research agents

Search engines

Web research

Crawlers

Scraping

Data ingestion

Technology radar

Trend discovery

Idea generation

AI video

AI image

Image editing

AI audio

Voice/TTS

Music

3D

Web design

Website generation

UI/UX

App generation

No-code / low-code

Freelance automation

Business automation

Personal AI workspaces

Desktop AI

Windows AI

Hybrid local/cloud systems.

==================================================
20. هدف سخت‌افزاری و معماری DJMRN
==================================================

وضعیت واقعی دستگاه را از inventory زنده بخوان.

Known baseline:

Windows 11
Ryzen 5 3500U
Vega 8
8 GiB physical RAM
RAM usable/free محدود.

اما:

Local Hardware Fit

و:

Overall Project Relevance

را از هم جدا کن.

یک پروژه ممکن است روی لپ‌تاپ فعلی اجرا نشود ولی برای:

Cloud runtime
Remote GPU
Future machine
Customer system

ارزش بسیار بالایی داشته باشد.

بنابراین Candidate را فقط به خاطر نیاز GPU حذف نکن.

برچسب مناسب بده:

LOCAL-FIT

LOCAL-CONDITIONAL

CLOUD-FIT

REMOTE-INFRA

FUTURE-HARDWARE

NOT-FIT.

==================================================
21. معماری Hybrid برای ما مهم است
==================================================

به Candidateهایی امتیاز بیشتری بده که بتوانند بخشی از این تصویر باشند:

Local Control
+
Cloud Compute
+
Shared Tool Layer
+
Specialized Assistants
+
Replaceable Models
+
Low Local RAM

ولی نتیجه را از پیش به این architecture مجبور نکن.

اگر گزینهٔ ساده‌تر بهتر است گزارش کن.

==================================================
22. پروژه‌هایی از جنس «معماری را عوض می‌کنند»
==================================================

به‌طور خاص پروژه‌هایی را شکار کن که یکی از این اثرها را دارند:

- کاری را که قبلاً چند سرویس می‌خواست در یک ابزار جمع می‌کنند.
- مصرف RAM یا GPU را معنی‌دار کاهش می‌دهند.
- Local/Cloud switching را آسان می‌کنند.
- مدل‌های متعدد را با یک API واحد ارائه می‌کنند.
- چند Assistant را روی یک model مشترک اجرا می‌کنند.
- orchestration آماده ارائه می‌کنند.
- tool permission / sandboxing را حل می‌کنند.
- workflow library بزرگی فراهم می‌کنند.
- observability آماده دارند.
- deployment بسیار ساده می‌کنند.
- capability جدید برای ویدیو/صدا/تصویر/کد ایجاد می‌کنند.
- پروژه‌ای previously impossible را روی hardware کوچک ممکن می‌کنند.
- هزینهٔ Cloud را معنی‌دار کاهش می‌دهند.
- standard/protocol جدیدی ایجاد می‌کنند.
- Agent/AI interoperability را بهتر می‌کنند.

اینها برای ما مهم‌تر از یک library کوچک معمولی هستند.

==================================================
23. Hype Detection
==================================================

برای هر Candidate جدی:

Marketing claim

را از:

Measured fact

جدا کن.

مثلاً:

“352x faster”

باید مشخص شود:

352x چه چیزی؟

micro-benchmark؟
overall app؟
specific parser؟
specific WASM operation؟

همین‌طور:

“75% cheaper”
“10x faster”
“100 agents”
“production ready”
“self learning”
“zero RAM”

نباید بدون context تکرار شوند.

==================================================
24. Evidence Quality
==================================================

برای هر پروژهٔ Top:

repository exists

recent commit

release history

documentation

license

tests/CI

issues

contributors

actual implementation

benchmarks

external evidence if available

را بررسی کن.

اگر README ادعایی دارد ولی implementation یا benchmark پیدا نشد:

PROJECT-CLAIM / UNVERIFIED

بنویس.

==================================================
25. Momentum را فقط با Star نسنج
==================================================

برای پروژه‌های تازه:

absolute stars

و:

growth velocity

را جدا کن.

اگر داده موجود بود:

stars/day

fork growth

release cadence

commit activity

issue activity

contributors

cross-source mentions

download growth

model downloads

HN/Product Hunt signal

را بررسی کن.

یک پروژه با 2,000 star و رشد 1,500 در یک هفته ممکن است برای Radar مهم‌تر از پروژهٔ 100,000-star قدیمی باشد.

==================================================
26. Cross-Source Confirmation
==================================================

اگر یک پروژه هم‌زمان در:

GitHub Trending
Hacker News
Product Hunt
Hugging Face
Reddit

دیده شد، به عنوان چند پروژه حساب نشود.

یک Entity:

Project X

با Signals متعدد ایجاد کن.

Cross-source appearance یک Momentum Signal است.

==================================================
27. Time Windows
==================================================

پژوهش را حداقل در چند horizon انجام بده:

HOT NOW:
تقریباً 7–30 روز اخیر

BREAKOUT:
تقریباً 90 روز اخیر

RECENT FOUNDATIONAL:
تقریباً 12 ماه اخیر

MATURE BUT STRATEGIC:
پروژه‌های قدیمی‌تری که اکنون برای DJMRN مهم شده‌اند.

هدف این است که نه فقط تازه‌های یک روز، و نه فقط پروژه‌های قدیمی معروف دیده شوند.

==================================================
28. Candidate Scoring
==================================================

یک Scoring Model قابل توضیح طراحی کن.

حداقل عوامل:

DJMRN relevance

technical leverage

novelty

actual capability

maturity

evidence quality

momentum

local/hybrid/cloud fit

RAM implications

Windows compatibility

free/open-source value

license

API/standard integration

MCP/A2A/tool compatibility

security

privacy

replaceability

maintenance/activity

complexity

operational cost.

Weightها را خودت براساس مأموریت پیشنهاد کن و دلیل بده.

Score جای Judgment را نگیرد.

==================================================
29. مواردی که امتیاز منفی می‌گیرند
==================================================

صرفاً Hype

no code

abandoned repo

license unclear

security concerns

unknown cost

paid-only with no compelling benefit

huge local resource requirement without remote route

unmaintainable complexity

duplicate of stronger existing capability

README-only implementation

fake benchmark

unsafe autonomous permissions

strong vendor lock-in

را صریحاً نشان بده.

==================================================
30. خروجی Source Landscape
==================================================

یک Matrix بساز:

Source / Platform

Source type:
Forge / AI Hub / Registry / Signal / Research / Vendor

Best use

Trending/Discovery

API

RSS/Webhook

Auth required?

Free public read?

Rate-limit concern

Commercial-use concern

Geography/access concern

Signal quality

Noise level

DJMRN priority:
P0 / P1 / P2 / Skip

و توضیح بده کدام منابع باید Core Radar باشند.

==================================================
31. پیشنهاد اولیهٔ منابع Core
==================================================

اینها فقط Seed هستند؛ مستقل verify کن:

GitHub Trending/Search/Releases

Hugging Face Models/Spaces/Papers

GitLab public projects/releases

Hacker News / Show HN

Product Hunt Developer/Open Source

PyPI

npm

crates.io

Docker Hub

arXiv/OpenReview

official vendor releases.

سپس بررسی کن:

Codeberg
SourceHut
Bitbucket
Gitee
SourceForge
Lobsters
DEV
Reddit
ModelScope
Kaggle
و منابع جدیدتر

آیا باید Core یا Secondary باشند.

==================================================
32. Candidate Discovery Output
==================================================

بعد از Source mapping، واقعاً Candidate کشف کن.

فقط یک فهرست از سایت‌ها تحویل نده.

حداقل:

20–40 پروژهٔ جدی

را از sweep اولیه استخراج کن.

بعد:

Top 10–15

را برای Deep Evaluation انتخاب کن.

عدد دقیق را می‌توانی براساس کیفیت نتایج تنظیم کنی؛ کیفیت مهم‌تر از پرکردن سهمیه است.

==================================================
33. Deep Evaluation هر Top Candidate
==================================================

برای هر Candidate برتر ثبت کن:

Name

Canonical repository/product

Category

First/recent signal source

Official source

What it actually is

What is genuinely new

Why it is receiving attention

What claim is marketing

What implementation is verified

Architecture

Local / Cloud / Hybrid

Windows

RAM implications

GPU requirement

Free status

License

Paid dependency

API

MCP / A2A / standards

Security/permissions

Maintenance/activity

Maturity

Potential DJMRN use

Overlap with existing DJMRN research

Could replace what?

Could complement what?

Major risks

Unknowns

Recommended status.

==================================================
34. Recommended Status Labels
==================================================

برای Top Candidates یکی از این statusها را پیشنهاد بده:

IMMEDIATE-RESEARCH

PILOT-CANDIDATE-LATER

ARCHITECTURE-INSPIRATION

WORKFLOW/RESOURCE-LIBRARY

WATCH

CLOUD-FUTURE

LOCAL-FUTURE

NOT-YET-MATURE

HYPE / LOW-EVIDENCE

NOT-RELEVANT

REJECT

ولی اینها recommendation پژوهشی‌اند، نه project approval.

==================================================
35. نگاه ویژه به RAM
==================================================

برای پروژهٔ ما این سؤال بسیار مهم است:

آیا این فناوری می‌تواند قابلیت جدید بدهد بدون اینکه RAM لپ‌تاپ را دائماً مصرف کند؟

خصوصاً پیدا کن:

on-demand runtimes

serverless systems

cloud-hosted systems

model unload/TTL

JIT loading

lightweight local proxies

browser-based tools

remote inference

thin clients

logical agents without resident models.

اگر RAM رسمی وجود ندارد:

RAM = UNKNOWN / BENCHMARK REQUIRED

حدس نزن.

==================================================
36. نگاه ویژه به Free-First
==================================================

برای سرویس‌ها:

Free

Renewable Free Tier

Free credit

Trial

Paid

را جدا کن.

بررسی:

card requirement

overage

auto-charge

quota reset

region

commercial use

privacy.

UNKNOWN COST / REGION
=
DENY ACTIVATION

اما Candidate پژوهشی می‌تواند باقی بماند.

==================================================
37. Licensing
==================================================

Open Source را دقیق بررسی کن.

MIT
Apache-2.0
BSD
GPL/AGPL
source-available
proprietary

را قاطی نکن.

اگر “open source” در marketing آمده ولی license OSI-compatible نیست، توضیح بده.

==================================================
38. Security
==================================================

Trending بودن = Trusted نیست.

برای Candidateهای دارای:

Shell

Browser control

Filesystem write

Credential access

MCP tools

Agent autonomy

Code execution

Package install

باید risk را برجسته کنی.

هیچ repository ناشناخته اجرا یا نصب نشود.

==================================================
39. Supply Chain
==================================================

بررسی کن:

maintainer identity

release provenance

package names

typosquatting risk

dependency activity

security advisories

signed releases if relevant.

اما این پژوهش metadata/read-only است.

==================================================
40. Discovery Sources را خودکار قابل استفاده بسنج
==================================================

هدف بلندمدت Technology Radar است.

بنابراین برای هر source بگو آیا بعدها می‌تواند از طریق:

API

RSS

Atom

Webhook

Search endpoint

scheduled query

official feed

به صورت automation-safe استفاده شود.

Scraping آخرین گزینه باشد.

==================================================
41. خروجی مخصوص Technology Radar آینده
==================================================

در پایان پیشنهاد بده Core Radar آینده چه Source Set اولیه‌ای داشته باشد.

مثلاً:

P0:
5–8 منبع بسیار قوی

P1:
منابع تخصصی تکمیلی

P2:
منابع occasional/manual.

هدف پوشش حداکثری با Noise کم است.

==================================================
42. ایده‌پردازی از Candidateها
==================================================

فقط نگویید «این پروژه خوب است».

برای Top Candidates بررسی کن آیا ترکیب آنها با یکدیگر ایدهٔ معماری یا capability جدیدی می‌دهد.

مثلاً:

New Agent Harness
+
Local Model Router
+
Workflow Library
+
Cloud Observability

↓

Possible DJMRN Architecture Pattern

یا:

New low-RAM engine
+
Assistant Profiles

↓

More local assistants without more resident models.

حداقل چند Cross-Technology Combination با ارزش واقعی پیشنهاد بده.

==================================================
43. ارتباط با نیازهای فعلی DJMRN
==================================================

Candidateها را نسبت به این Future Tracks نیز بسنج:

Multi-persona assistants

Workflow reuse/discovery

Technology Radar

Hybrid local/cloud inference

Low-RAM architecture

MCP/tool core

Dual chat surfaces

Agent orchestration

Observability map

Research curator

Opportunity discovery

Freelance automation.

اما مجبور نیست همهٔ Candidateها به همهٔ اینها ربط داشته باشند.

==================================================
44. Negative Findings
==================================================

گزارش باید پروژه‌هایی را که مشهور ولی برای ما نامناسب‌اند نیز ثبت کند.

مثلاً:

Very popular
BUT
Linux-only GPU server
AND
no realistic current use

یا:

Amazing demo
BUT
no code/license/docs.

Negative evidence ارزش دارد.

==================================================
45. نتیجهٔ نهایی مورد انتظار
==================================================

گزارش نهایی باید چهار لایه داشته باشد:

LAYER 1 — SOURCE MAP

بهترین جاهای جهان برای پیدا کردن فناوری و پروژهٔ جدید کجا هستند؟

LAYER 2 — DISCOVERY

چه پروژه‌های مهمی الان باید بشناسیم؟

LAYER 3 — DEEP EVALUATION

کدام پروژه‌ها واقعاً جدی‌اند و Hype نیستند؟

LAYER 4 — DJMRN IMPACT

از هرکدام چه چیزی می‌توانیم یاد بگیریم، استفاده کنیم، بعداً آزمایش کنیم یا وارد معماری آینده کنیم؟

==================================================
46. Executive Shortlist
==================================================

در ابتدای WA یک Shortlist بسیار روشن بده:

TOP 5:
بالاترین ارزش فوری پژوهشی برای DJMRN

NEXT 5:
ارزش بالا ولی نیازمند بلوغ/شرایط

WATCH:
پروژه‌هایی که باید زیر نظر بمانند

و دلیل هر مورد را بسیار کوتاه بگو.

بعد Deep Report بیاید.

==================================================
47. Source Quality
==================================================

برای ادعاهای مهم:

Official repository
Official docs
Official release
Official paper

را ترجیح بده.

Search result snippets
social posts
Reddit
Product Hunt
HN

فقط signal/supporting evidence باشند.

==================================================
48. Applied Library Integration
==================================================

طبق پروتکل Work:

Applied Capability Index و Mission را بخوان.

برای هر Candidate مشخص کن:

EXISTING-IN-LIBRARY

EXISTING-ENRICHED

NEW-CANDIDATE

UNVERIFIED.

نام‌های جدید را فقط به خاطر جدید بودن بهتر ندان.

نامزدهای قبلی را هم فقط به خاطر history برتر ندان.

==================================================
49. Mandatory Receipts
==================================================

WA باید طبق README دارای:

APPLIED_LIBRARY_READ_RECEIPT

INDEPENDENT_SEARCH_RECEIPT

MERGED_CANDIDATE_MATRIX

باشد.

لینک/نسخه/تاریخ منابع واقعاً خوانده‌شده را ثبت کن.

==================================================
50. حدود اختیار
==================================================

این مأموریت فقط:

Research
Search
Read
Compare
Evaluate
Report

است.

انجام نده:

Install
Clone/run untrusted repository
Download executable/model
Create account
Create API token
Activate cloud
Use paid API
Spend credit
Modify Windows
Change Notion
Change code
Deploy
Import workflow
Connect provider
Run benchmark on user laptop.

==================================================
51. خروجی پروژه
==================================================

Work فقط پاسخ متناظر:

04-work-research-bridge/responses/WA####.md

را در همان repository صحیح ایجاد کند.

هیچ فایل دیگری را تغییر نده.

بعد از Commit:

همان WA را از همان repository read back کن.

رسید نهایی Chat باید طبق Work protocol شامل:

repository_full_name

WQ####/WA####

SUCCESS / PARTIAL / BLOCKED

actual commit SHA

response blob SHA

readback VERIFIED / NOT VERIFIED

باشد.

==================================================
52. پرسش نهایی که گزارش باید جواب دهد
==================================================

اگر DJMRN بخواهد از امروز یک سیستم دائمی برای کشف «پروژه‌هایی که واقعاً آینده را تغییر می‌دهند» بسازد:

- کجا باید نگاه کند؟
- چه چیزهایی را اندازه بگیرد؟
- چه منابعی Noise هستند؟
- چه پروژه‌هایی همین حالا ارزش توجه دارند؟
- کدامشان با محدودیت RAM و معماری Hybrid ما سازگارند؟
- کدامشان فقط برای Cloud/Future Hardware مناسب‌اند؟
- از کدام‌ها باید capability بگیریم؟
- از کدام‌ها فقط Architecture Pattern یاد بگیریم؟
- کدام‌ها ارزش Pilot آینده دارند؟
- چه چیزهایی را باید فقط Watch کنیم؟

هدف نهایی:
نه ساخت یک فهرست طولانی از لینک‌ها،
بلکه ایجاد یک نقشهٔ قابل اعتماد برای:

DISCOVER
→ VERIFY
→ RANK
→ UNDERSTAND
→ CONNECT TO DJMRN
→ WATCH / RESEARCH / PILOT LATER

است.