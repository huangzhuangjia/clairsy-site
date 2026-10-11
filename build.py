#!/usr/bin/env python3
"""Tiny static-site build: python3 build.py  (needs: pip install markdown)
Reads site.config.json (ALL placeholders) + content/*.md, writes index.html, en/, zh/."""
import json, re, pathlib, html, markdown
R = pathlib.Path(__file__).parent
C = json.loads((R/'site.config.json').read_text('utf-8'))

def unresolved(v): return v.startswith('[') or 'example.com' in v or v.rstrip('/')=='https://apps.apple.com'
def ph(v):  # highlight unresolved placeholders
    return f'<mark class="ph">{html.escape(v)}</mark>' if unresolved(v) else html.escape(v)
def icon(n,cls='ic'): return f'<img class="{cls}" src="{{A}}icons/{n}.svg" alt="" aria-hidden="true">'

def mail(): e=C['support_email']; return f'<a href="mailto:{e}">{ph(e)}</a>'

T = {
'en': dict(
  name='English', title='Clairsy — Your stress, like the weather',
  nav=['Features','FAQ','Support','Privacy','Terms'],
  badge='Clairsy · HRV stress monitor for Apple Watch',
  h1='Your stress, like the <em>weather</em>.', sub='Read from your Apple Watch, compared only to you.',
  lead="Clairsy reads heart rate variability and heart rate from your Apple Watch, compares them with your own baseline, and tells you how you're doing right now — Chill, Steady, Tense or Stressed. 晴晴 changes with you. Everything is calculated on your iPhone and Apple Watch.",
  dl1='Download on the', dl2='App Store', free='Free to start · 7-day free trial on subscriptions',
  req='Requires iPhone with iOS 18 or later and a paired Apple Watch (watchOS 11 or later).',
  shotnote='Screenshots from the current app (demo data). The app interface is in Simplified Chinese.',
  trust=[('On-device only','No servers — nothing is uploaded'),('No account','No sign-up, no login'),('No tracking','No ads, no analytics SDKs'),('Read-only Health','Clairsy never writes to Health')],
  fk='FEATURES', fh='Built around your own baseline',
  cards=[('Stress, in plain words','HRV and resting heart rate are compared with your personal baseline and turned into four easy levels — Chill, Steady, Tense, Stressed — with a stress index and 7-day average. Quick mood check-ins calibrate it to how you actually feel.'),
         ('Daily Vigor & sleep','Each morning Clairsy sets your Daily Vigor from recovery, sleep and training load, then shows how stress drains it through the day. Sleep duration, score, sleep debt and stages at a glance.'),
         ('Breathe it down','Resonance breathing (4 in, 6 out), cyclic sighing, 4-7-8 and box breathing, with 晴晴 breathing along — on iPhone and Apple Watch. Before-and-after readings show what changed.'),
         ('On your wrist','A watch app with your current level and a one-tap “Measure now”, watch-face complications, Home Screen widgets, and optional local stress alerts.')],
  mh='Free to start, membership when you want more',
  mb='Free: the Today page — stress level, HRV and Daily Vigor % — plus sleep duration, score, sleep debt and stages, breathing exercises, Home Screen widgets, free complications and one basic watch face. Clairsy Membership unlocks trends, Daily Vigor details, in-depth sleep analysis, custom stress-alert frequency, and all complications and watch faces. Choose a monthly or yearly subscription (7-day free trial for eligible Apple IDs) or Lifetime (one-time purchase). All purchases are handled by Apple; prices are shown on the App Store purchase sheet.',
  sk='SUPPORT', sh='Frequently asked questions',
  faq=[('Why do I need an Apple Watch?','Clairsy’s readings come from heart rate variability (HRV) and heart rate that Apple Watch measures and saves to Apple Health. iPhone alone doesn’t record HRV, so stress and HRV readings require a paired Apple Watch (watchOS 11 or later) that you wear. Wearing it overnight helps Clairsy learn your baseline.'),
       ('What is HRV?','Heart rate variability is the small variation in time between heartbeats. Clairsy compares your HRV (SDNN, plus RMSSD on OS versions that support it) and resting heart rate with your own personal baseline — not a population average — to estimate your current stress level. It’s a wellness estimate, not a medical measurement.'),
       ('My data isn’t updating. What should I do?','If you see “not enough data”, wear your Apple Watch for a few days, including overnight, and check that Clairsy has read access in Settings › Privacy &amp; Security › Health › Clairsy. If the watch or complications don’t update, open Clairsy on your iPhone once, make sure your watch is connected, and add a Clairsy complication to your watch face. The system limits background refreshes, so readings may lag by a few minutes.'),
       ('Is my data uploaded?','No. All calculations happen on your iPhone and Apple Watch. Clairsy has no servers and no accounts. See the <a href="../privacy/">Privacy Policy</a> for details.'),
       ('How do I restore purchases?','In Clairsy, go to Settings › Membership › Restore Purchases, or tap Restore Purchases at the top right of the membership screen. Use the same Apple ID you bought with.'),
       ('How do I cancel my subscription?','On your iPhone, go to Settings › [your name] › Subscriptions › Clairsy, or in Clairsy go to Settings › Membership › Manage Subscription. Cancel at least 24 hours before the current period ends to avoid renewal. See Apple’s guide: <a href="https://support.apple.com/en-us/118428">Cancel a subscription from Apple</a>.'),
       ('How do I get a refund?','Apple handles refunds. Visit <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.'),
       ('How do I delete my data?','Delete Clairsy from your iPhone and Apple Watch to erase all of its local data. Clairsy never writes to Health.')],
  help='Still need help?',
  helpb=lambda: f"Email us and we’ll get back to you, usually {ph(C['reply_time_en'])}. Please include your iPhone and Apple Watch models and OS versions.",
  dev=lambda: f"Developer: {ph(C['developer_name'])}",
  foot=['Support','Privacy Policy','Terms of Use'],
  notice='Health notice: Clairsy is for wellness reference only. It is not a medical device and does not diagnose or treat any condition. If you feel unwell, please consult a doctor.',
  tm=lambda: f"Apple, Apple Watch, iPhone, Apple Health and App Store are trademarks of Apple Inc. © {C['year']} {ph(C['developer_name'])}. All rights reserved.",
  privacy='Privacy Policy', terms='Terms of Use'),
'zh': dict(
  name='简体中文', title='Clairsy 晴晴 — Apple Watch 的 HRV 压力监测',
  nav=['功能','常见问题','支持','隐私','条款'],
  badge='Clairsy 晴晴 · Apple Watch 的 HRV 压力监测',
  h1='压力，<br>像<em>天气</em>一样看得见', sub='用 Apple Watch 读懂你的压力，只和你自己比',
  lead='Clairsy 读取 Apple Watch 记录的心率变异性（HRV）和心率，和你自己的基线比较，告诉你此刻状态——真巴适、hold住、有点烦还是鸭梨大。晴晴的表情会跟着你变。所有计算都在你的 iPhone 和 Apple Watch 上完成。',
  dl1='在 App Store', dl2='下载', free='免费开始 · 订阅含 7 天免费试用',
  req='需要 iOS 18 或更高版本的 iPhone，并配对 Apple Watch（watchOS 11 或更高版本）。',
  shotnote='截图来自当前版本（演示数据）。',
  trust=[('仅在设备上计算','没有服务器，什么都不上传'),('无需账号','不用注册，不用登录'),('不追踪','无广告，无统计分析 SDK'),('只读健康数据','Clairsy 从不写入「健康」')],
  fk='功能', fh='围绕你自己的基线',
  cards=[('压力，用大白话说','HRV 和静息心率与你的个人基线比较，换算成四档：真巴适、hold住、有点烦、鸭梨大，并给出压力指数和 7 日均值。随手打卡此刻感受，帮它校准到你的真实体感。'),
         ('今日元气与睡眠','每天早上，Clairsy 根据恢复、睡眠和训练负荷定下今日元气，再显示一天里压力怎样消耗它。睡眠时长、得分、睡眠负债和分期一目了然。'),
         ('呼吸减压','共振呼吸（吸 4 呼 6）、循环叹息、4-7-8 呼吸和方块呼吸，晴晴陪你一起呼吸——iPhone 和 Apple Watch 都能用。缓一下前后的读数变化一看便知。'),
         ('戴在手腕上','手表 App 显示此刻状态，一键「立即测量」；表盘复杂功能、主屏幕小组件，以及可选的本地压力提醒。')],
  mh='免费开始，想要更多再开会员',
  mb='免费：今日页——压力档位、HRV 和今日元气百分比——以及睡眠时长、得分、睡眠负债和分期、呼吸减压、主屏幕小组件、免费复杂功能和一款基础表盘。Clairsy 会员解锁趋势、元气详情、深度睡眠分析、自定义压力提醒频率，以及全部复杂功能和表盘。可选按月或按年订阅（符合条件的 Apple ID 享 7 天免费试用），或终身买断（一次性购买）。所有购买均由 Apple 处理，价格以 App Store 购买页显示为准。',
  sk='支持', sh='常见问题',
  faq=[('为什么需要 Apple Watch？','Clairsy 的读数来自 Apple Watch 测量并存入「健康」的心率变异性（HRV）和心率。只用 iPhone 无法记录 HRV，所以压力和 HRV 读数需要配对并佩戴 Apple Watch（watchOS 11 或更高版本）。夜间佩戴能帮 Clairsy 更快了解你的基线。'),
       ('HRV 是什么？','心率变异性是相邻心跳间隔的细微变化。Clairsy 把你的 HRV（SDNN，在支持的系统版本上还会用 RMSSD）和静息心率与你自己的个人基线——而不是人群平均值——比较，估算你此刻的压力水平。这是健康参考，不是医学测量。'),
       ('数据不更新怎么办？','如果显示「数据不足」，请佩戴 Apple Watch 几天（包括夜间睡觉），并确认已在「设置 › 隐私与安全性 › 健康 › Clairsy」中允许读取。如果手表或复杂功能不更新，请先在 iPhone 上打开一次 Clairsy，确认手表与 iPhone 连接正常，并在表盘上添加 Clairsy 复杂功能。系统会限制后台刷新频率，读数可能有几分钟延迟。'),
       ('数据会上传吗？','不会。所有计算都在你的 iPhone 和 Apple Watch 上完成，Clairsy 没有服务器，也没有账号。详见<a href="../privacy/">隐私政策</a>。'),
       ('如何恢复购买？','在 Clairsy「设置 › 会员 › 恢复购买」中操作，或在会员页右上角点击「恢复购买」。请使用购买时的同一个 Apple ID。'),
       ('如何取消订阅？','iPhone「设置 › [你的姓名] › 订阅 › Clairsy」，或在 Clairsy「设置 › 会员 › 管理订阅」中操作。至少在当前周期结束前 24 小时取消，才不会续费。参见 Apple 说明：<a href="https://support.apple.com/zh-cn/118428">取消 Apple 的订阅</a>。'),
       ('如何退款？','退款由 Apple 处理，请访问 <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>。'),
       ('如何删除我的数据？','在 iPhone 和 Apple Watch 上删除 Clairsy，即可清除它保存的全部本地数据。Clairsy 从不写入「健康」数据。')],
  help='还需要帮助？',
  helpb=lambda: f"给我们发邮件，通常 {ph(C['reply_time_zh'])}回复。请附上你的 iPhone 和 Apple Watch 型号及系统版本。",
  dev=lambda: f"开发者：{ph(C['developer_name_zh'])}",
  foot=['支持','隐私政策','使用条款'],
  notice='健康提示：Clairsy 仅供健康参考，不是医疗器械，不提供诊断或治疗。身体不适请咨询医生。',
  tm=lambda: f"Apple、Apple Watch、iPhone、Apple 健康和 App Store 是 Apple Inc. 的商标。© {C['year']} {ph(C['developer_name_zh'])} 保留所有权利。",
  privacy='隐私政策', terms='使用条款'),
}

MASCOT = '<img src="../{up}assets/qingqing.svg" alt="晴晴" width="{s}" height="{s}">'

def page(lang, kind, body, title):
    t=T[lang]; up='../' if kind!='home' else ''
    other='zh' if lang=='en' else 'en'
    rel={'home':'','privacy':'privacy/','terms':'terms/'}[kind]
    hl='en' if lang=='en' else 'zh-Hans'
    n=t['nav']; h='' if kind=='home' else '../'
    nav=f'''<header class="nav wrap"><a class="logo" href="{h}./">{MASCOT.format(up=up,s=36)}<span>Clairsy</span></a>
<nav><a href="{h}./#features">{n[0]}</a><a href="{h}./#faq">{n[1]}</a><a href="{h}./#support">{n[2]}</a><a href="{up}../{lang}/privacy/">{n[3]}</a><a href="{up}../{lang}/terms/">{n[4]}</a>
<span class="lang"><a href="{up}../en/{rel}" data-lang="en" class="{'on' if lang=='en' else ''}">EN</a><a href="{up}../zh/{rel}" data-lang="zh" class="{'on' if lang=='zh' else ''}">中文</a></span></nav></header>'''
    foot=f'''<footer><div class="wrap"><div class="frow"><a class="logo sm" href="{h}./">{MASCOT.format(up=up,s=28)}<span>Clairsy</span></a>
<div class="flinks"><a href="{h}./#support">{t['foot'][0]}</a><a href="{up}../{lang}/privacy/">{t['foot'][1]}</a><a href="{up}../{lang}/terms/">{t['foot'][2]}</a>{mail()}</div></div>
<hr><p>{t['notice']}</p><p class="tm">{t['tm']()}</p></div></footer>'''
    return f'''<!doctype html><html lang="{hl}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(t['lead'][:150])}">
<link rel="alternate" hreflang="en" href="{up}../en/{rel}"><link rel="alternate" hreflang="zh-Hans" href="{up}../zh/{rel}">
<link rel="icon" href="{up}../assets/qingqing.svg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}../assets/site.css"></head><body class="{kind}">
{nav}{body}{foot}<script src="{up}../assets/lang.js"></script></body></html>'''

def home(lang):
    t=T[lang]
    trust=''.join(f'<div><i></i><b>{a}</b><small>{b}</small></div>' for a,b in t['trust'])
    cards=''.join(f'<div class="card c{i}"><i></i><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(t['cards']))
    faq=''.join(f'<details{" open" if i<3 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(t['faq']))
    body=f'''<main><section class="hero"><div class="wrap hgrid"><div class="hcopy">
<span class="pill"><i></i>{t['badge']}</span><h1>{t['h1']}</h1><p class="lead">{t['lead']}</p>
<div class="cta"><a class="appstore" href="{C['app_store_url']}" title="Placeholder — replace with official Apple badge artwork"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="#fff"/></svg><span><small>{t['dl1']}</small>{t['dl2']}</span></a><span class="free">{t['free']}</span></div>
<p class="req">{t['req']}</p></div>
<div class="hvis"><div class="phone"><img src="../assets/phone.webp" alt="Clairsy Today screen" width="603" height="1311"></div>
<div class="watch"><img src="../assets/watch.webp" alt="Clairsy Apple Watch app" width="416" height="496"></div>
<img class="mas" src="../assets/qingqing.svg" alt="" width="135" height="135"><p class="shotnote">{t['shotnote']}</p></div></div>
<div class="wrap"><div class="trust">{trust}</div></div></section>
<section id="features" class="wrap sec"><p class="kick">{t['fk']}</p><h2>{t['fh']}</h2><div class="cards">{cards}</div>
<div class="member"><h3>{t['mh']}</h3><p>{t['mb']}</p></div></section>
<section id="faq" class="faqsec"><div class="wrap narrow"><p class="kick">{t['sk']}</p><h2>{t['sh']}</h2><div class="faq">{faq}</div>
<div id="support" class="help"><img src="../assets/qingqing.svg" alt="" width="96" height="96"><div><h3>{t['help']}</h3><p>{t['helpb']()}</p><small>{t['dev']()}</small></div>
<a class="mailbtn" href="mailto:{C['support_email']}">{ph(C['support_email'])}</a></div></div></section></main>'''
    return page(lang,'home',body,t['title'])

def legal(lang, kind):
    md=(R/f'content/{kind}-{lang}.md').read_text('utf-8')
    md='\n'.join(l for l in md.splitlines() if not re.match(r'^>\s*(\[DRAFT|【草稿)',l) and 'Postal address' not in l and '联系地址' not in l)
    rep={'[Developer Name]':C['developer_name'],'[开发者姓名]':C['developer_name_zh'],'[Contact Email]':C['support_email'],'[联系邮箱]':C['support_email'],
         '[Effective date]':C['effective_date_en'],'[Last updated date]':C['last_updated_en'],'[生效日期，例如 2026 年 X 月 X 日]':C['effective_date_zh'],'[生效日期]':C['effective_date_zh'],'[更新日期]':C['last_updated_zh'],
         "[the developer's place of residence, e.g. City, Province]":C['court_en'],'[开发者住所地，例如 XX 省 XX 市]':C['court_zh']}
    for k,v in rep.items(): md=md.replace(k,'\x00'+str(list(rep).index(k))+'\x01')
    md=re.sub(r'^(\*\*(Effective date:|生效日期)\*\*.*)$',r'\1  ',md,flags=re.M)
    md=re.sub(r'\]\(\./(privacy|terms)-(en|zh)\.md\)',lambda m:f'](../{m.group(1)}/)',md)
    out=markdown.markdown(md,extensions=['tables'])
    out=re.sub('\x00(\\d+)\x01',lambda m:(mail() if '@' in list(rep.values())[int(m.group(1))] else ph(list(rep.values())[int(m.group(1))])),out)
    out=re.sub(r'<a href="http',r'<a rel="noopener" href="http',out)
    out=re.sub(r'<p><strong>(In short:|一句话概括：)(.*?)</p>',lambda m:f'<div class="short"><span class="ib">{icon("in-short-shield")}</span><p><strong>{m.group(1)}{m.group(2)}</p></div>',out,flags=re.S)
    t=T[lang]; title=t[kind]
    return page(lang,kind,f'<main class="legal"><div class="wrap narrow"><article>{out}</article></div></main>',f'{title} — Clairsy')

# ---------- v4 layout (Figma 360:2) ----------
WEATHER='<svg class="wx" viewBox="0 0 64 44" aria-hidden="true"><circle cx="40" cy="16" r="11" fill="#FFD45C"/><path d="M14 40h30a10 10 0 0 0 1-19.9A13 13 0 0 0 20.5 24 8 8 0 0 0 14 40z" fill="#fff" stroke="#E3EFE8"/></svg>'
LABELS={'en':dict(member='MEMBERSHIP',menu='Menu'),'zh':dict(member='会员',menu='菜单')}
FAQI=['watch','hrv','refresh','upload-off','restore','cancel-subscription','refund','delete-data']
TRUSTI=['on-device','no-account','no-tracking','read-only-health']
CARDI=['stress-weather','vigor-sleep','breathe','watch']

def page(lang, kind, body, title):
    t=T[lang]; up='../' if kind!='home' else ''
    A=f'{up}../assets/'
    rel={'home':'','privacy':'privacy/','terms':'terms/'}[kind]
    hl='en' if lang=='en' else 'zh-Hans'
    n=t['nav']; h='' if kind=='home' else '../'
    cur=lambda k:' aria-current="page"' if k==kind else ''
    nav=f'''<header class="top"><div class="nav wrap"><a class="logo" href="{h}./">{MASCOT.format(up=up,s=36)}<span>Clairsy</span></a>
<nav id="menu"><a href="{h}./#features">{n[0]}</a><a href="{h}./#faq">{n[1]}</a><a href="{h}./#support">{n[2]}</a><a href="{up}../{lang}/privacy/"{cur('privacy')}>{n[3]}</a><a href="{up}../{lang}/terms/"{cur('terms')}>{n[4]}</a></nav>
<span class="lang"><img src="{A}icons/globe.svg" alt="" aria-hidden="true"><a href="{up}../en/{rel}" data-lang="en" class="{'on' if lang=='en' else ''}" lang="en">EN</a><a href="{up}../zh/{rel}" data-lang="zh" class="{'on' if lang=='zh' else ''}" lang="zh-Hans">中文</a></span>
<button class="burger" aria-label="{LABELS[lang]['menu']}" aria-controls="menu" aria-expanded="false"><span></span><span></span><span></span></button></div></header>'''
    foot=f'''<footer><div class="wrap"><div class="frow"><a class="logo sm" href="{h}./">{MASCOT.format(up=up,s=28)}<span>Clairsy</span></a>
<div class="flinks"><a href="{h}./#support">{t['foot'][0]}</a><a href="{up}../{lang}/privacy/">{t['foot'][1]}</a><a href="{up}../{lang}/terms/">{t['foot'][2]}</a>{mail()}</div></div>
<hr><p>{t['notice']}</p><p class="tm">{t['tm']()}</p></div></footer>'''
    return f'''<!doctype html><html lang="{hl}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(re.sub('<[^>]+>','',t['sub']))}">
<link rel="alternate" hreflang="en" href="{up}../en/{rel}"><link rel="alternate" hreflang="zh-Hans" href="{up}../zh/{rel}">
<link rel="icon" href="{A}qingqing.svg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}site.css"></head><body class="{kind}">
{nav}{body.replace('{A}',A)}{foot}<script src="{A}lang.js"></script></body></html>'''

def home(lang):
    t=T[lang]; L=LABELS[lang]
    trust=''.join(f'<div><span class="ib">{icon(i)}</span><b>{a}</b><small>{b}</small></div>' for i,(a,b) in zip(TRUSTI,t['trust']))
    cards=''.join(f'<div class="card c{k}"><div class="chead"><span class="ib lg">{icon(i)}</span><span class="num">0{k+1}</span></div><h3>{a}</h3><p>{b}</p></div>' for k,(i,(a,b)) in enumerate(zip(CARDI,t['cards'])))
    faq=''.join(f'<details{" open" if k<3 else ""}><summary><span class="ib sm">{icon(i)}</span><span class="q">{q}</span><span class="pm" aria-hidden="true"></span></summary><p>{a}</p></details>' for k,(i,(q,a)) in enumerate(zip(FAQI,t['faq'])))
    body=f'''<main><section class="hero"><div class="wrap hgrid"><div class="hcopy">
<span class="pill"><i></i>{t['badge']}</span>{WEATHER}<h1>{t['h1']}</h1><p class="sub">{t['sub']}</p><p class="lead">{t['lead']}</p>
<div class="cta"><a class="appstore" href="{C['app_store_url']}" data-placeholder="{'1' if unresolved(C['app_store_url']) else '0'}" title="Placeholder link — replace with the real App Store URL and official Apple badge artwork"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="#fff"/></svg><span><small>{t['dl1']}</small>{t['dl2']}</span></a><span class="free">{t['free']}</span></div>
<p class="req">{t['req']}</p></div>
<div class="hvis"><div class="halo"></div>
<div class="dev ph1"><img src="{{A}}vigor.webp" alt="" width="603" height="1311"></div>
<div class="dev ph2"><img src="{{A}}today-{lang}.webp" alt="Clairsy Today" width="603" height="1311"></div>
<div class="dev wt"><img src="{{A}}watch.webp" alt="Clairsy on Apple Watch" width="416" height="496"></div>
<img class="mas" src="{{A}}qingqing.svg" alt="" width="135" height="135"></div>
<p class="shotnote">{t['shotnote']}</p></div>
<div class="wrap"><div class="trust">{trust}</div></div></section>
<section id="features" class="wrap sec"><p class="kick">{t['fk']}</p><h2>{t['fh']}</h2><div class="cards">{cards}</div>
<div class="member"><div><span class="mpill">{icon('membership','ic xs')}{L['member']}</span><h3>{t['mh']}</h3></div><p>{t['mb']}</p></div></section>
<section id="faq" class="faqsec"><div class="wrap narrow"><p class="kick">{t['sk']}</p><h2>{t['sh']}</h2><div class="faq">{faq}</div>
<div id="support" class="help"><img class="hm" src="{{A}}qingqing.svg" alt="" width="96" height="96"><div class="ht"><h3>{t['help']}</h3><p>{t['helpb']()}</p><small>{t['dev']()}</small></div>
<a class="mailbtn" href="mailto:{C['support_email']}">{icon('mail','ic w')}{html.escape(C['support_email'])}</a></div></div></section></main>'''
    return page(lang,'home',body,t['title'])

for lang in ('en','zh'):
    for kind,fn in (('home',f'{lang}/index.html'),('privacy',f'{lang}/privacy/index.html'),('terms',f'{lang}/terms/index.html')):
        p=R/fn; p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(home(lang) if kind=='home' else legal(lang,kind),'utf-8')
    for alias in ('support',):
        p=R/f'{lang}/{alias}/index.html'; p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(f'<!doctype html><meta charset="utf-8"><title>Clairsy Support</title><meta http-equiv="refresh" content="0;url=../#support"><link rel="canonical" href="../#support"><a href="../#support">Support</a>','utf-8')
print('built')
