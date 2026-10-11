# Clairsy public website (support · privacy · terms)

Static site, no runtime build. `python3 build.py` (needs `pip install markdown`) regenerates HTML from
`site.config.json` + `content/*.md` (legal text from clairsy `docs/legal`). Commit the generated files; GitHub Pages serves `main` root.

URLs: `/` (auto: saved choice → navigator.language zh* → 中文, else English; `/?lang=zh|en` forces), `/en/`, `/zh/` (home + FAQ + support),
`/en/support/` `/zh/support/` (→ home #support), `/en/privacy/`, `/zh/privacy/`, `/en/terms/`, `/zh/terms/`.

## Placeholders — edit ONLY `site.config.json`, then `python3 build.py`
Unresolved values render highlighted (yellow).
| key | current |
|---|---|
| developer_name / developer_name_zh | [Developer Name] / [开发者姓名] |
| support_email | support@example.com |
| effective_date_en / _zh | [Effective date] / [生效日期] |
| last_updated_en / _zh | [Last updated date] / [更新日期] |
| court_en / court_zh | governing-law court location |
| reply_time_en / _zh | within 3 business days / 3 个工作日内 (support only; legal text keeps its own statutory timing) |
| app_store_url | https://apps.apple.com/ (replace with the app's App Store link) |

App Store badge is a placeholder button — replace with official Apple "Download on the App Store" artwork per Apple's marketing guidelines.
Screenshots in `assets/phone.webp` / `assets/watch.webp` were captured from the current master build (DEBUG `-heroDemo relaxed` / `-watchDemo relaxed`).
