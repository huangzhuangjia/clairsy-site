# Clairsy public website (support · privacy · terms)

Static site, no runtime build. `python3 build.py` (needs `pip install markdown`) regenerates HTML from
`site.config.json` + `content/*.md` (legal text from clairsy `docs/legal`). Commit the generated files; GitHub Pages serves `main` root.

URLs: `/` (auto: saved choice → navigator.language zh* → 中文, else English; `/?lang=zh|en` forces), `/en/`, `/zh/` (home + FAQ + support),
`/en/support/` `/zh/support/` (→ home #support), `/en/privacy/`, `/zh/privacy/`, `/en/terms/`, `/zh/terms/`.

## Placeholders — edit ONLY `site.config.json`, then `python3 build.py`
Unresolved values render highlighted (yellow).
| key | current |
|---|---|
| developer_name / developer_name_zh | Zhuangjia Huang / 黄壮佳 |
| support_email | huangzhuangjia@gmail.com |
| effective_date_* / last_updated_* | 2026-10-11 |
| court_en / court_zh | Guangzhou, China / 中国广州 |
| reply_time_en / _zh | within 3 business days / 3 个工作日内 (support only; privacy policy commits to 15 business days) |
| app_store_url | **still placeholder** https://apps.apple.com/ — badge shows a dashed yellow outline until replaced |

App Store badge is a placeholder button — replace with official Apple "Download on the App Store" artwork per Apple's marketing guidelines.
Hero images `assets/vigor.webp`, `today-{en,zh}.webp`, `watch.webp` (Figma v4, section 360:2) were captured from the current master build (DEBUG `-heroDemo relaxed` / `-watchDemo relaxed`).
