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
  h1='Your stress, like the <em>weather</em>.', comp='Qingqing stays with you, getting to know you — a health companion that gets you.', sub='Reads your Apple Watch. Compared only to you. Stress and Daily Energy, live on your wrist.',
  lead="Clairsy reads heart rate variability and heart rate from your Apple Watch, compares them with your own baseline, and tells you how you're doing right now — Great, Normal, Elevated or Overload. Qingqing changes with you. Everything is calculated on your iPhone and Apple Watch.",
  dl1='Download on the', dl2='App Store', free='Free: see your stress level and Daily Energy %.',
  req='Requires iPhone with iOS 18 or later and a paired Apple Watch (watchOS 11 or later).',
  shotnote='Screenshots from the current app (demo data).',
  trust=[('On-device only','No servers — nothing is uploaded'),('No account','No sign-up, no login'),('No tracking','No ads, no analytics SDKs'),('Read-only Health','Clairsy never writes to Health')],
  fk='FEATURES', fh='Built around your own baseline',
  cards=[('Stress, plain and clear','HRV and resting heart rate become four clear levels — Great, Normal, Elevated, Overload — with a stress index and 7-day average. Quick mood check-ins calibrate it to how you actually feel.'),
         ('5-minute HRV refresh','On Apple Watch Ultra 4 and Series 12, with Recovery HRV authorized, samples arrive about every 5 minutes and Clairsy switches to fast refresh — you’ll see it on Today as “Fast refresh · a few minutes ago.” Watch face and complications refresh too — in our testing, within about 5 minutes of a new sample (occasionally a little later when the system limits background updates).'),
         ('Custom alert frequency','Three stress-alert modes: Low (default) sends one gentle nudge when you move up to Overload; Normal alerts after about 10 minutes in Elevated or Overload; Custom (Membership) reports your current status every 15 minutes to 4 hours. 15- and 30-minute intervals need a fast-refresh watch such as Series 12 or Ultra 4; on Series 11, Ultra 3 and earlier, Custom starts at 1 hour — or use Normal.'),
         ('Daily Energy — plan your day','Each morning Clairsy sets your starting energy from last night’s sleep and recovery. Stress and activity drain it through the day, a nap tops it back up. See how much is left and where you’ll land by tonight, and Qingqing tells you when to push or ease off.'),
         ('Sleep at a glance','Last night’s duration, sleep score, 7-night sleep debt and stages — deep, core, REM and awake — all free, with Qingqing suggesting a bedtime. Membership adds in-depth sleep analysis.'),
         ('Trends you can see','Day, week and month views of your HRV against your baseline, a breakdown of time spent Great, Normal, Elevated and Overload, and a stress heat map that shows when you tend to tense up. Trends are part of Clairsy Membership.'),
         ('Take a breather with Qingqing','When stress spikes, tap Breathe — or jump in straight from a stress alert. The orb swells and settles with your breath while Qingqing breathes along; on Apple Watch, gentle haptics keep the rhythm so you don’t have to watch the screen, and a tap on the orb pauses or resumes. Choose resonance breathing, cyclic sighing, 4-7-8 or box breathing. Afterward, see how your readings changed — and your Today page remembers you just took a breather.'),
         ('Your watch face keeps up','Watch face and complications show your current level, with a one-tap “Measure”, Home Screen widgets, and optional local stress alerts. On Ultra 4 and Series 12, fast refresh keeps it more current.')],
  mh='Free to start, membership when you want more',
  mb='Free: the Today page — stress level, HRV and Daily Energy % — plus sleep duration, score, sleep debt and stages, breathing exercises, Home Screen widgets, free complications and one basic watch face. Clairsy Membership unlocks trends, Daily Energy details, in-depth sleep analysis, custom stress-alert frequency, and all complications and watch faces. Choose a monthly or yearly subscription (7-day free trial for eligible Apple IDs) or Lifetime (one-time purchase). All purchases are handled by Apple; prices are shown on the App Store purchase sheet.',
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
  h1='压力，<br>像<em>天气</em>一样看得见', comp='晴晴慢慢陪着你，做最懂你的健康伙伴。', sub='读你的 Apple Watch，只和你自己比。压力与今日元气，表盘跟着刷新。',
  lead='Clairsy 读取 Apple Watch 记录的心率变异性（HRV）和心率，和你自己的基线比较，告诉你此刻状态——真巴适、hold住、有点烦还是鸭梨大。晴晴的表情会跟着你变。所有计算都在你的 iPhone 和 Apple Watch 上完成。',
  dl1='在 App Store', dl2='下载', free='免费就能看此刻压力和元气百分比。',
  req='需要 iOS 18 或更高版本的 iPhone，并配对 Apple Watch（watchOS 11 或更高版本）。',
  shotnote='截图来自当前版本（演示数据）。',
  trust=[('仅在设备上计算','没有服务器，什么都不上传'),('无需账号','不用注册，不用登录'),('不追踪','无广告，无统计分析 SDK'),('只读健康数据','Clairsy 从不写入「健康」')],
  fk='功能', fh='围绕你自己的基线',
  cards=[('压力一眼看懂','HRV 和静息心率与你的个人基线比较，一眼看出四档：真巴适、hold住、有点烦、鸭梨大，并给出压力指数和 7 日均值。随手打卡此刻感受，帮它校准到你的真实体感。'),
         ('5分钟 HRV 极速刷新','在 Apple Watch Ultra 4 和 Series 12 上授权「恢复 HRV」后，样本最快约 5 分钟一次，Clairsy 自动进入极速刷新——今日页会显示「极速刷新 · N 分钟前」。表盘和复杂功能也会同步刷新，实测新样本后约 5 分钟内跟上（偶尔受系统后台额度影响会稍晚）。'),
         ('自定义通知频率','压力提醒有三档：低频（默认）只在状态升入「鸭梨大」时轻轻提醒一次；普通在「有点烦」或「鸭梨大」持续约 10 分钟后提醒；自定义频率（会员）按 15 分钟到 4 小时的间隔播报此刻状态。15 / 30 分钟需要 Series 12、Ultra 4 等支持极速刷新的手表；Series 11、Ultra 3 及更早机型自定义从 1 小时起，或选普通档。'),
         ('今日元气，安排好你的一天','早上醒来，Clairsy 会根据昨夜睡眠和身体恢复情况，给你今天的元气起点。白天压力、运动会慢慢消耗它，午睡能补回一点。还剩多少、照这个节奏晚上会剩多少，一眼就知道。晴晴会提醒你该冲还是该缓，别等透支了才发现。'),
         ('睡眠一眼看懂','昨夜睡眠时长、睡眠得分、近 7 晚睡眠负债，以及深睡、浅睡、REM、清醒分期，全部免费；晴晴还会建议今晚几点前睡。会员解锁深度睡眠分析。'),
         ('趋势看得见','按日、周、月查看 HRV 与个人基线的对比、真巴适 / hold住 / 有点烦 / 鸭梨大各占多少时间，还有压力热力图，看清自己一般几点最紧绷。趋势为 Clairsy 会员功能。'),
         ('缓一口气，晴晴陪你','压力一上来，点「缓一下」就能开始，压力提醒也能直接跳进来。光球跟着节奏一胀一缩，晴晴陪你一起吸气、呼气。手表上用震动带节奏，不用盯着屏幕，点一下光球就能暂停或继续。共振呼吸、循环叹息、4-7-8、方块呼吸四种方式任选。练完会对比前后的读数，告诉你缓得怎么样，今日页也会留下「刚刚缓过」的记录。'),
         ('表盘跟着变','表盘和复杂功能显示此刻状态，一键「立即测量」；还有主屏幕小组件，以及可选的本地压力提醒。在 Ultra 4、Series 12 上配合极速刷新更及时。')],
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

MASCOT = '<img src="../{up}assets/qingqing.svg" alt="{alt}" width="{s}" height="{s}">'

def page(lang, kind, body, title):
    t=T[lang]; up='../' if kind!='home' else ''
    other='zh' if lang=='en' else 'en'
    rel={'home':'','privacy':'privacy/','terms':'terms/'}[kind]
    hl='en' if lang=='en' else 'zh-Hans'
    n=t['nav']; h='' if kind=='home' else '../'
    nav=f'''<header class="nav wrap"><a class="logo" href="{h}./">{MASCOT.format(up=up,s=36,alt='Qingqing' if lang=='en' else '晴晴')}<span>Clairsy</span></a>
<nav><a href="{h}./#features">{n[0]}</a><a href="{h}./#faq">{n[1]}</a><a href="{h}./#support">{n[2]}</a><a href="{up}../{lang}/privacy/">{n[3]}</a><a href="{up}../{lang}/terms/">{n[4]}</a>
<span class="lang"><a href="{up}../en/{rel}" data-lang="en" class="{'on' if lang=='en' else ''}">EN</a><a href="{up}../zh/{rel}" data-lang="zh" class="{'on' if lang=='zh' else ''}">中文</a></span></nav></header>'''
    foot=f'''<footer><div class="wrap"><div class="frow"><a class="logo sm" href="{h}./">{MASCOT.format(up=up,s=28,alt='Qingqing' if lang=='en' else '晴晴')}<span>Clairsy</span></a>
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
<div class="cta"><a class="appstore" href="{C['app_store_url']}"><img src="{{A}}badge-{'zh-cn' if lang=='zh' else 'en-us'}.svg" alt="{t['dl1']} {t['dl2']}" height="48"></a></div>
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
CARDI=['stress-weather','vigor-sleep','vigor-sleep','hrv','breathe','watch']

def page(lang, kind, body, title):
    t=T[lang]; up='../' if kind!='home' else ''
    A=f'{up}../assets/'
    rel={'home':'','privacy':'privacy/','terms':'terms/'}[kind]
    hl='en' if lang=='en' else 'zh-Hans'
    n=t['nav']; h='' if kind=='home' else '../'
    cur=lambda k:' aria-current="page"' if k==kind else ''
    nav=f'''<header class="top"><div class="nav wrap"><a class="logo" href="{h}./">{MASCOT.format(up=up,s=36,alt='Qingqing' if lang=='en' else '晴晴')}<span>Clairsy</span></a>
<nav id="menu"><a href="{h}./#features">{n[0]}</a><a href="{h}./#faq">{n[1]}</a><a href="{h}./#support">{n[2]}</a><a href="{up}../{lang}/privacy/"{cur('privacy')}>{n[3]}</a><a href="{up}../{lang}/terms/"{cur('terms')}>{n[4]}</a></nav>
<span class="lang"><img src="{A}icons/globe.svg" alt="" aria-hidden="true"><a href="{up}../en/{rel}" data-lang="en" class="{'on' if lang=='en' else ''}" lang="en">EN</a><a href="{up}../zh/{rel}" data-lang="zh" class="{'on' if lang=='zh' else ''}" lang="zh-Hans">中文</a></span>
<button class="burger" aria-label="{LABELS[lang]['menu']}" aria-controls="menu" aria-expanded="false"><span></span><span></span><span></span></button></div></header>'''
    foot=f'''<footer><div class="wrap"><div class="frow"><a class="logo sm" href="{h}./">{MASCOT.format(up=up,s=28,alt='Qingqing' if lang=='en' else '晴晴')}<span>Clairsy</span></a>
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
<div class="cta"><a class="appstore" href="{C['app_store_url']}"><img src="{{A}}badge-{'zh-cn' if lang=='zh' else 'en-us'}.svg" alt="{t['dl1']} {t['dl2']}" height="48"></a></div>
<p class="req">{t['req']}</p></div>
<div class="hvis"><div class="halo"></div>
<div class="dev ph1"><img src="{{A}}vigor{'-en' if lang=='en' else ''}.webp" alt="" width="603" height="1311"></div>
<div class="dev ph2"><img src="{{A}}today-{lang}.webp" alt="Clairsy Today" width="603" height="1311"></div>
<div class="dev wt"><img src="{{A}}watch{'-en' if lang=='en' else ''}.webp" alt="Clairsy on Apple Watch" width="416" height="496"></div>
<img class="mas" src="{{A}}qingqing.svg" alt="" width="135" height="135"></div>
<p class="shotnote">{t['shotnote']}</p></div>
<div class="wrap"><div class="trust">{trust}</div></div></section>
<section id="features" class="wrap sec"><p class="kick">{t['fk']}</p><h2>{t['fh']}</h2><div class="cards">{cards}</div>
<div class="member"><div><span class="mpill">{icon('membership','ic xs')}{L['member']}</span><h3>{t['mh']}</h3></div><p>{t['mb']}</p></div></section>
<section id="faq" class="faqsec"><div class="wrap narrow"><p class="kick">{t['sk']}</p><h2>{t['sh']}</h2><div class="faq">{faq}</div>
<div id="support" class="help"><img class="hm" src="{{A}}qingqing.svg" alt="" width="96" height="96"><div class="ht"><h3>{t['help']}</h3><p>{t['helpb']()}</p><small>{t['dev']()}</small></div>
<a class="mailbtn" href="mailto:{C['support_email']}">{icon('mail','ic w')}{html.escape(C['support_email'])}</a></div></div></section></main>'''
    return page(lang,'home',body,t['title'])

# ---------- v5 Apple-style layout (approved mockup v3) ----------
X={'en':dict(
  dark_h='Compared only to <span>you</span>.',
  dark_p='',
  points=[('Your baseline only','Recovery HRV and resting HR vs your personal baseline; check-ins fine-tune it.'),
          ('Live on your wrist','Watch face and complications refresh when a new sample lands.'),
          ('Never leaves your device','No servers, no account, no tracking.'),
          ('On your wrist','Check-ins help it learn you; a soft nudge when stress rises.')],
  meet_h='Meet Qingqing',
  meet_p='Qingqing lives on your wrist. It smiles when you’re at ease and frowns when stress creeps in. Each morning it tells you how much energy you’ve got, and when you’re running low it nudges you to wrap up early. When you need a breather, it breathes with you; with every check-in, it quietly learns your rhythm. Whenever you need it most, it’s there — quietly caring, always by your side.',
  moods=[('chill','Great'),('steady','Normal'),('tense','Elevated'),('stressed','Overload')],
  priv_h='Private by design.',
  priv_p='Clairsy only reads the Health data you allow it to read, and does all of its calculations on your iPhone and Apple Watch. We have no servers. We never upload your data to us or to anyone else, and we never use it for advertising.',
  priv_link='Read the Privacy Policy ›', breath_alt='Breathing exercise', sleep_alt='Sleep', trends_alt='Trends', hrv_alt='Today · Fast refresh', alerts_alt='Stress alerts'),
 'zh':dict(
  dark_h='只和<span>你自己</span>比。',
  dark_p='',
  points=[('只和自己比','恢复 HRV 与静息心率对照你的个人基线；打卡后还会微调。'),
          ('表盘跟着刷新','新样本一到，表盘和复杂功能跟着更新。'),
          ('数据不出机','无服务器、无账号、无追踪。'),
          ('晴晴在你手腕上','打卡后更懂你，压力大时轻轻喊你缓一口气。')],
  meet_h='认识晴晴',
  meet_p='晴晴是住在你手腕上的小伙伴。你轻松时它眯眼笑，压力一上来它也跟着皱眉。早上它会告诉你今天的元气还剩多少，累了就提醒你早点收工。想缓一缓时，它陪你一呼一吸；每一次打卡，它都悄悄记下，慢慢读懂你的节奏。它总能在你最需要的时候，默默关心你，陪伴你！',
  moods=[('chill','真巴适'),('steady','hold住'),('tense','有点烦'),('stressed','鸭梨大')],
  priv_h='隐私，从设计开始。',
  priv_p='Clairsy 只读取你授权的「健康」数据，所有计算都在你的 iPhone 和 Apple Watch 上完成。我们没有服务器，不会把你的任何数据上传给我们或任何第三方，也不会把数据用于广告。',
  priv_link='阅读隐私政策 ›', breath_alt='呼吸减压', sleep_alt='睡眠', trends_alt='趋势', hrv_alt='今日 · 极速刷新', alerts_alt='压力提醒')}
MEMBER={'en':dict(free_h='Free',mem_h='Clairsy Membership',
  free=['Today page — stress level, HRV and Daily Energy %','Sleep duration, score, sleep debt and stages','Breathing exercises','Home Screen widgets','Free complications and one basic watch face'],
  mem=['Trends','Daily Energy details','In-depth sleep analysis','Custom stress-alert frequency','All complications and watch faces'],
  note='Choose a monthly or yearly subscription (7-day free trial for eligible Apple IDs) or Lifetime (one-time purchase). All purchases are handled by Apple; prices are shown on the App Store purchase sheet.'),
 'zh':dict(free_h='免费',mem_h='Clairsy 会员',
  free=['今日页——压力档位、HRV 和今日元气百分比','睡眠时长、得分、睡眠负债和分期','呼吸减压','主屏幕小组件','免费复杂功能和一款基础表盘'],
  mem=['趋势','元气详情','深度睡眠分析','自定义压力提醒频率','全部复杂功能和表盘'],
  note='可选按月或按年订阅（符合条件的 Apple ID 享 7 天免费试用），或终身买断（一次性购买）。所有购买均由 Apple 处理，价格以 App Store 购买页显示为准。')}
CLOUDS='<div class="cloud c1"></div><div class="cloud c2"></div><div class="cloud c3"></div>'

def home(lang):
    t=T[lang]; x=X[lang]; L=LABELS[lang]; M=MEMBER[lang]; zh=lang=='zh'; sfx='' if zh else '-en'
    shots=[f'<div class="ph"><img src="{{A}}today-{lang}.webp" alt="Clairsy Today" width="603" height="1311" loading="lazy"></div>',
           f'<div class="ph"><img src="{{A}}hrv-{lang}.webp" alt="{x["hrv_alt"]}" width="603" height="1311" loading="lazy"></div>',
           f'<div class="ph"><img src="{{A}}alerts-{lang}.webp" alt="{x["alerts_alt"]}" width="603" height="1311" loading="lazy"></div>',
           f'<div class="ph"><img src="{{A}}vigor{sfx}.webp" alt="Daily Energy" width="603" height="1311" loading="lazy"></div>',
           f'<div class="ph"><img src="{{A}}sleep-{lang}.webp" alt="{x["sleep_alt"]}" width="603" height="1311" loading="lazy"></div>',
           f'<div class="ph"><img src="{{A}}trends-{lang}.webp" alt="{x["trends_alt"]}" width="603" height="1311" loading="lazy"></div>',
           f'<div class="ph"><img src="{{A}}breath-{lang}.webp" alt="{x["breath_alt"]}" width="603" height="1311" loading="lazy"></div>',
           f'<div class="wa"><img src="{{A}}watch{sfx}.webp" alt="Clairsy on Apple Watch" width="416" height="496" loading="lazy"></div>']
    # dual-device: steps with a matching Apple Watch screen show phone + watch together
    WD={0:('ultra','Clairsy Status Gauge face on Apple Watch Ultra'),1:('status','Clairsy on Apple Watch'),2:('alert','Clairsy stress alert on Apple Watch'),3:('vigor','Daily Energy on Apple Watch'),5:('today','Today’s stress timeline on Apple Watch'),6:('breath','Breathe on Apple Watch')}
    for k,(w,alt) in WD.items():
        shots[k]=f'<div class="duo">{shots[k]}<div class="wa"><img src="{{A}}watch-{w}-{lang}.webp" alt="{alt}" width="416" height="496" loading="lazy"></div></div>'
    steps=''.join(f'<div class="step reveal" data-step="{k}"><div class="stept"><span class="n" aria-hidden="true">0{k+1}</span><h3>{a}</h3></div><p>{b}</p><div class="inl">{shots[k]}</div></div>' for k,(a,b) in enumerate(t['cards']))
    frames=''.join(f'<div class="frame{" on" if k==0 else ""}" data-frame="{k}">{s}</div>' for k,s in enumerate(shots))
    dots=''.join(f'<i class="{"on" if k==0 else ""}"></i>' for k in range(len(shots)))
    tiles=''.join(f'<div class="tile reveal"><img class="ti" src="{{A}}icons/{i}.svg" alt="" aria-hidden="true"><b>{a}</b><small>{b}</small></div>' for i,(a,b) in zip(TRUSTI,t['trust']))
    stats=''.join(f'<div class="stat reveal"><b>{t_}</b><small>{d}</small></div>' for t_,d in x['points'])
    dark_lede=(f'<p class="lede reveal">{x["dark_p"]}</p>' if x.get('dark_p') else '')
    moods=''.join(f'<button type="button" class="mood{" on" if k==0 else ""}" data-mood="{mid}" aria-pressed="{"true" if k==0 else "false"}"><img src="{{A}}moods/{mid}.png" alt="" width="56" height="56" loading="lazy"><span>{lab}</span></button>' for k,(mid,lab) in enumerate(x['moods']))
    meet_faces=''.join(f'<img class="meet-face{" on" if k==0 else ""}" data-mood="{mid}" src="{{A}}moods/{mid}.png" alt="" width="220" height="220" loading="lazy">' for k,(mid,_) in enumerate(x['moods']))
    faq=''.join(f'<details{" open" if k<3 else ""}><summary><span class="ib sm">{icon(i)}</span><span class="q">{q}</span><span class="pm" aria-hidden="true"></span></summary><div class="ans"><div><p>{a}</p></div></div></details>' for k,(i,(q,a)) in enumerate(zip(FAQI,t['faq'])))
    body=f'''<main>
<section class="hero">{CLOUDS}<div class="wrap hgrid"><div class="hin">
<svg class="wx ld" style="--d:0" viewBox="0 0 64 44" aria-hidden="true"><circle cx="40" cy="16" r="11" fill="#FFD45C"/><path d="M14 40h30a10 10 0 0 0 1-19.9A13 13 0 0 0 20.5 24 8 8 0 0 0 14 40z" fill="#fff" stroke="#E3EFE8"/></svg>
<p class="eyebrow ld" style="--d:0">{t['badge']}</p><h1 class="ld" style="--d:1">{t['h1'].replace('<br>',' ')}</h1><p class="comp ld" style="--d:2">{t['comp']}</p><p class="lead ld" style="--d:3">{t['lead']}</p>
<div class="cta ld" style="--d:4"><a class="appstore" href="{C['app_store_url']}"><img src="{{A}}badge-{'zh-cn' if zh else 'en-us'}.svg" alt="{t['dl1']} {t['dl2']}" height="48"></a></div>
<p class="req ld" style="--d:5">{t['req']}</p></div>
<div class="hvis"><div class="stage ld" style="--d:5"><div class="glow"></div>
<div class="dev p1" data-px="-0.06"><img src="{{A}}vigor{sfx}.webp" alt="" width="603" height="1311"></div>
<div class="dev p2" data-px="0"><img src="{{A}}today-{lang}.webp" alt="Clairsy Today" width="603" height="1311"></div>
<div class="dev wt" data-px="0.08"><img src="{{A}}watch{sfx}.webp" alt="Clairsy on Apple Watch" width="416" height="496"></div>
<img class="mas" src="{{A}}qingqing.svg" alt="" width="135" height="135"></div></div></div></section>
<section id="qingqing" class="meet"><div class="wrap"><div class="meetcard reveal">
<div class="meetvis"><div class="meet-stage" aria-hidden="true">{meet_faces}</div>
<div class="moods" role="group" aria-label="{x['meet_h']}">{moods}</div></div>
<div class="meettxt"><h2>{x['meet_h']}</h2><p>{x['meet_p']}</p></div>
</div></div></section>
<section id="features" class="feat"><div class="wrap sgrid"><div class="steps"><div class="rail" aria-hidden="true"><i></i></div>{steps}</div><div class="sticky"><div class="devbox">{frames}</div><div class="dots" aria-hidden="true">{dots}</div></div></div></section>
<section id="privacy" class="priv"><div class="wrap"><img class="shield reveal" src="{{A}}icons/in-short-shield.svg" alt="" width="56" height="56"><h2 class="reveal">{x['priv_h']}</h2><p class="lede reveal">{x['priv_p']}</p>
<div class="tiles">{tiles}</div><p class="plink reveal"><a href="privacy/">{x['priv_link']}</a></p></div></section>
<section class="mem"><div class="wrap"><div class="memhead reveal"><span class="mpill">{icon('membership','ic xs')}{L['member']}</span><h2>{t['mh']}</h2></div>
<div class="mcols"><div class="mcol reveal"><h3>{M['free_h']}</h3><ul>{''.join(f'<li>{i}</li>' for i in M['free'])}</ul></div>
<div class="mcol pro reveal"><h3>{M['mem_h']}</h3><ul>{''.join(f'<li>{i}</li>' for i in M['mem'])}</ul></div></div>
<p class="mnote reveal">{M['note']}</p></div></section>
<section id="faq" class="faqsec"><div class="wrap narrow"><p class="kick reveal">{t['sk']}</p><h2 class="reveal">{t['sh']}</h2><div class="faq">{faq}</div>
<div id="support" class="help reveal"><img class="hm" src="{{A}}qingqing.svg" alt="" width="96" height="96"><div class="ht"><h3>{t['help']}</h3><p>{t['helpb']()}</p><small>{t['dev']()}</small></div>
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

# ---------- cache busting: ?v=<content hash> on every local asset URL ----------
import hashlib
def _bust(m):
    url=m.group(2); f=(R/'assets'/url.split('assets/',1)[1])
    v=hashlib.sha256(f.read_bytes()).hexdigest()[:10] if f.is_file() else None
    return f'{m.group(1)}{url}?v={v}"' if v else m.group(0)
for f in list(R.glob('*/index.html'))+list(R.glob('*/*/index.html'))+[R/'index.html']:
    s=f.read_text('utf-8'); n=re.sub(r'((?:src|href)=")((?:\.\./)+assets/[^"?#]+)"',_bust,s)
    if n!=s: f.write_text(n,'utf-8')
print('cache-busted')
