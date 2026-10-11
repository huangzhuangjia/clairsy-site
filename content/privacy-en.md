
# Clairsy Privacy Policy

> [DRAFT – replace every `[…]` placeholder and delete this line before publishing]

**Effective date:** [Effective date]
**Last updated:** [Last updated date]

Clairsy (the "App") is developed and operated by an individual developer, **[Developer Name]** ("we", "us", or the "Developer"). This policy explains how the App handles your information. It is written to meet the App Store Review Guidelines, Apple's HealthKit requirements, and applicable privacy laws, including China's Personal Information Protection Law (PIPL).

**In short: Clairsy only reads the Health data you allow it to read, and does all of its calculations on your iPhone and Apple Watch. We have no servers. We never upload your data to us or to anyone else, and we never use it for advertising.**

---

## 1. Who we are and how to contact us

- Developer / personal information handler: [Developer Name] (individual developer)
- Email: [Contact Email]
- Postal address: [Optional – postal address; may be omitted if not public]

We will reply to your email within **15 business days** of receiving it.

## 2. What we process and why

### 2.1 Apple Health data (sensitive personal information; requires your separate, explicit permission)

Only after you grant permission in the system prompt, the App **reads (read-only)** the following HealthKit data types:

| Data type | Purpose |
|---|---|
| Heart rate variability (HRV, SDNN) | Compared with your personal baseline to estimate your current stress level |
| Recovery HRV (RMSSD; requested separately, only on OS versions that support it) | Makes stress estimates more timely |
| Resting heart rate | Stress level and "Daily Energy" estimates |
| Heart rate | Stress level, overnight heart-rate chart, energy drain estimate |
| Sleep analysis (stages and duration) | Sleep score, sleep-stage analysis, starting point of Daily Energy |
| Respiratory rate (during sleep) | Recovery assessment for Daily Energy |
| Sleeping wrist temperature | Recovery assessment for Daily Energy |
| Workouts (time and duration) | Training load and energy estimates |
| Workout effort (Apple rating / estimated rating) | Training load estimate |
| Step count | Activity and energy drain estimates |
| Active energy | Activity and energy drain estimates |

The App also reads the **source device information** attached to these samples (for example, the Apple Watch model). It uses this only to show which device the data came from.

**The App never writes any data to Health.** You can grant access to only some data types. Anything you don't allow is left out of the calculations, and the related features may show "not enough data".

**Why sensitive data is necessary, and how it affects you:** health data is sensitive personal information. The App's core features (stress level, Daily Energy, sleep analysis) can't work without it. All processing happens locally on your devices, and we cannot see or obtain this data.

**How we obtain separate consent:** when you first open the App, we ask you to agree to this Policy. At the "Connect Health" step of onboarding you then tap that button and switch on each data type in Apple's Health permission sheet; this is your **separate consent** to reading the Health data above (sensitive personal information). If you decline this Policy, you can still explore the App in Browse mode, and the App reads no Health data.

### 2.2 Information you create in the App (stored on your device only)

- **Mood check-ins** (the feeling you choose and the time): used to calibrate stress estimates to how you actually feel. Because mood records reflect your wellbeing, we treat them as **sensitive personal information**; they stay on your device.
- **Breathing session history** (time and duration of your most recent 100 sessions): used to show your practice history and before/after changes.
- **App settings**: appearance, stress-alert frequency, sleep-need duration, and similar preferences.
- **Computed results and caches**: stress level, Daily Energy, a 30-day HRV sample cache, your personal baselines, and so on. These make the App load faster and feed the Home Screen widgets and watch complications.
- **Membership status**: whether you have an active subscription, its expiry date, and whether you bought Lifetime, the one-time purchase (from Apple's purchase records; see 2.3).

### 2.3 Purchases (handled by Apple)

Subscriptions and Lifetime (one-time purchase) are sold through **Apple In-App Purchase**. Apple handles payment, billing, and refunds. **We never receive** your Apple ID, name, payment method, or billing details. On your device, the App uses Apple's StoreKit to read your purchase entitlements (product ID, expiry date, refund status) so it can unlock membership features. Apple's handling of this information is covered by the [Apple Privacy Policy](https://www.apple.com/legal/privacy/).

### 2.4 Notifications

If you allow notifications, the App creates **local notifications** (such as stress alerts) on your device. It does not use any remote push server. Notification content (for example, your current stress level) may appear on your Lock Screen. You can change this in Settings › Notifications › Clairsy.

### 2.5 What we do not collect

The App **does not** collect your name, phone number, email, contacts, photos, precise or approximate location, or advertising identifier (IDFA), and it does not track you across other apps or websites. The App has **no user accounts** and contains **no third-party analytics, advertising, crash-reporting, or other third-party SDKs**.

## 3. Where your information is stored and for how long

- **Location:** everything above is stored only in the App's private storage on your iPhone and Apple Watch, including a shared container used by the same developer's App Group. Data syncs between your iPhone and your Apple Watch over Apple's system channel (WatchConnectivity), **directly between your own devices**. It never passes through any server of ours.
- **We have no servers.** Your data is never uploaded to the cloud, and the App does not save it to iCloud itself.
- **System backups:** if you use iCloud Backup or computer backups for your iPhone, your backup settings may include the App's local data. Apple and your device manage those backups; we cannot access them.
- **Retention:** the HRV sample cache keeps only the last 30 days, and breathing history keeps only the last 100 sessions. All other local data stays until you delete the App.
- **International transfers:** we do not transfer your personal information anywhere, including across borders.

## 4. Sharing and disclosure

We **do not** share, transfer, or publicly disclose your personal information to any third party. We **do not** sell your data, and we do not use Health data for advertising, marketing, or data mining. We simply never receive it.

The App contains links to external websites (for example, doi.org links to the research papers cited on the breathing page). These open in your system browser, and each site's own privacy policy applies.

## 5. Your rights and how to delete your data

- **Access and correction:** all of your data is shown in the App, and you can view and manage the underlying health data in Apple's Health app.
- **Withdraw permission:** at any time, turn off access to any data type in Settings › Privacy & Security › Health › Clairsy, and turn off notifications in Settings › Notifications › Clairsy. Withdrawing permission does not affect processing that already happened while permission was granted.
- **Withdraw consent to this Policy:** in the App, go to Settings › About › Withdraw Privacy Consent. The App immediately stops reading Health data, clears the on-device results computed from it, and switches to Browse mode. Your mood check-ins and breathing history stay on your device (deleting the App removes them). You can agree again in the same place.
- **Copy / portability:** your raw Health data can be exported from Apple's Health app; everything the App records stays on your device and is visible in the App.
- **Explanation:** you may email us to ask us to explain this Policy or how the App processes personal information.
- **Next of kin:** if a user has passed away, their next of kin may contact us at the email in Section 1 to exercise the rights provided by law.
- **Deletion:** **delete the App** from your iPhone (and Apple Watch) to erase all of its locally stored data. Copies in system backups follow your backup settings. The App never writes to Health, so deleting it does not affect your Health data.
- **Account:** there is no account to close. Manage or cancel subscriptions in Settings › [your name] › Subscriptions.
- **Other requests:** for questions, complaints, or to exercise any other legal right, email us at the address in Section 1. Because we hold none of your data, you can usually handle these requests yourself on your device, as described above.

### Complaints

Send complaints or reports to [Contact Email]; we will reply within **15 business days** after verifying your request. If you are not satisfied, you may complain to the competent authority (in mainland China, the cyberspace, industry and information technology, or market regulation authorities; elsewhere, your local data protection authority) or bring a claim before a competent court.

## 6. Automated assessment

On your device, the App **automatically** compares your HRV, heart rate, and other data with your personal baseline to produce reference results such as your stress level, Daily Energy, and sleep score. You can see how these are calculated in the App's “How it’s calculated” explanations. These results are for your own reference only. They are **not** used to make any decision that significantly affects your rights or interests, and they are not given to anyone.

## 7. Health disclaimer

The App provides **wellness estimates** based on wearable data. It is **not a medical device** and does not diagnose, treat, or prevent any condition. If you feel unwell, please consult a doctor.

## 8. Minors and children

- The App is designed for adults and is **not directed to children under 14** (under 13 in the United States).
- If you are under 14, use the App only **after a parent or guardian has read and agreed to this Policy**, and under their guidance; the guardian's agreement is the separate consent to processing the child's Health data. If you are 14 to 17, we recommend reading this Policy with a guardian.
- Data never leaves the device, so we cannot know a user's age and do not knowingly collect children's personal information. A guardian can turn off Health access in iOS Settings or delete the App at any time to erase all App data.
- Guardians who believe a child's information may be involved can contact us at the email in Section 1.

## 9. Changes to this policy

When we update this policy, we will publish the new version in the App and change the "Last updated" date above. If an update involves a material change in purposes, methods, or data types (for example, adding cloud sync in the future), we will tell you **prominently** (such as with an in-app prompt) after you update the App, and ask for your consent again where required. For a **major version** change (new data types, purposes, third parties, or cloud sync), we will show the key changes the next time you open the App and ask for your consent again; if you decline, you can keep using Browse mode.

## Appendix 1: Personal information inventory

| Feature | Data | Sensitive | Source | Stored | Retention | Leaves device |
|---|---|---|---|---|---|---|
| Stress level | HRV (SDNN / RMSSD), resting heart rate, heart rate | Yes | Health (read-only) | On device | HRV cache 30 days; others until you delete the App | No |
| Daily Energy | Sleep analysis, respiratory rate, sleeping wrist temperature, workouts and effort, steps, active energy | Yes | Health (read-only) | On device | Until you delete the App | No |
| Sleep analysis | Sleep stages and duration, overnight heart rate | Yes | Health (read-only) | On device | Until you delete the App | No |
| Data source display | Source device model | No | Health sample metadata | On device | Until you delete the App | No |
| Personal calibration | Mood check-ins (feeling, time) | Yes | You enter it | On device | Until you delete the App | No |
| Breathing | Session time and duration | No | Created in the App | On device | Last 100 sessions | No |
| Membership | Product ID, expiry date, refund status | No | Apple StoreKit | On device | Until you delete the App | No |
| Watch sync | The results and check-ins above | As above | Created in the App | Your iPhone and Apple Watch | As above | Only between your own devices |

## Appendix 2: System permissions

| Permission | Purpose | When we ask | If you decline | How to turn off |
|---|---|---|---|---|
| Health (read) | See Appendix 1 | After you agree to this Policy, when you tap "Connect Health" in onboarding | Related readings show "not enough data" | Settings › Privacy & Security › Health › Clairsy |
| Notifications | Local stress alerts | When you tap "Turn on stress alerts" in onboarding, or in Settings | No alerts | Settings › Notifications › Clairsy |

The App **does not request** location, camera, microphone, contacts, photos, Bluetooth, or ad-tracking (ATT) permission.

## Appendix 3: Third parties and SDKs

- **Third-party SDKs:** none. The App contains no analytics, advertising, crash-reporting, sign-in, payment, or push SDKs.
- **Providing personal information to third parties:** none.
- **Apple Inc.** (an independent handler of personal information, not our processor): when you buy a membership through the App Store, Apple handles payment, billing, renewals, and refunds under its own privacy policy; we never receive your Apple ID or payment details. Health, iCloud Backup, and WatchConnectivity are Apple system services managed by Apple and your device. See the [Apple Privacy Policy](https://www.apple.com/legal/privacy/).
- **External links** (such as doi.org) open in your system browser; no personal information is passed.

---

Questions? Contact: [Contact Email]


