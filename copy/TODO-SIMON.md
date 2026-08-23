# TODO(simon) — everything the service-page copy is waiting on

One consolidated list of every open `TODO(simon)` across the 26 service pages,
grouped by what you need to supply. Page paths are relative to `copy/services/`.

Nothing below blocks sign-off on the writing — the copy is finished and the
mechanical checks pass. These are the holes only you can fill.

---

## 1. Missing embed URLs (7)

3D animation has been dropped as a service (Simon, Aug 2026), so the three 3D
pages and the three missing-example TODOs that went with them are gone. Five
gaps remain from the original set, plus two on the new vodcast page.

| # | Page | What we need |
| --- | --- | --- |
| 1.1 | `aerial-drone-video-production.md` | Embed URL for **The Grand Union Boat Race 2023**. It's on the live aerial page but not in SOURCE-FACTS.md. This is the only TODO sitting inside a table row. |
| 1.2 | `live-action/automotive.md` | Embed URL for the **Nissan Serena** film shown on the live page. |
| 1.3 | `ai-video-production.md` | Embed URL for the **1920s Inspiring Hertfordshire Awards** film. It is the strongest example on the page — the whole body copy is the story of making it — and it currently has no player. |
| 1.4 | `live-action/live-streaming-video-production.md` | One **genuinely streamed** job we can link to. The three films listed are events we filmed, not confirmed streams. The FareShare Sussex & Surrey stream would be ideal. |
| 1.5 | `post-production/bristish-sign-language-bsl-production.md` | A link to any client film that **already carries a Pearldrop BSL overlay**. The three films listed are examples of work that *should* be signed, and the page says so — one real signed film would be far stronger. |
| 1.6 | `live-action/video-podcast-production.md` | **Embed URL for the Heart Radio vodcast with the UK VP of Warner Bros.** This is the page's only example and its whole argument. |
| 1.7 | `live-action/video-podcast-production.md` | **Two more vodcast examples.** Left short rather than padded with unrelated live-action work — a buyer looking for podcast production will spot that instantly. Two more episodes from the Heart Radio run would do. |

## 2. Source-data errors to resolve (1)

| # | Page | What we need |
| --- | --- | --- |
| 2.1 | `live-action/company-and-brand-video-production.md` | The **Novogene** embed ID in SOURCE-FACTS.md is identical to the Healthy Body Healthy Mind trailer ID (`n1snsv8Yww0`). One of the two is wrong. Confirm the correct Novogene URL. |

## 3. Testimonials needing your approval (1)

| # | Page | What we need |
| --- | --- | --- |
| 3.1 | `live-action/live-streaming-video-production.md` | The live page carries a much stronger FareShare quote about a stream ("it looked like the One Show"). It is **not** on the testimonials page, so we haven't used it. Confirm we can, and we'll swap it in for the Herts LEP quote. |

*For the record, no approval needed:* the 21 approved testimonials now cover all
26 pages, 14 used once and 6 used twice. Where a quote appears twice, the two
pages carry **different, non-overlapping verbatim extracts** of it, so no page
repeats a sentence found on another. Sian Teasdale is reserved for the
Activations and launches sample.

## 4. Claims to sanity-check (6)

Two of these are statistics inherited from the live site, four are new precision
we added. None is invented — but all six are the kind of line that should have
your name on it before it ships.

| # | Page | The claim | Status |
| --- | --- | --- | --- |
| 4.1 | `live-action/product-video-production.md` | "roughly three times more likely to buy and around 50% less likely to send it back" | **Verified against the live page** (it says the same thing) but unsourced there too. A citation would make it safe; otherwise consider softening to "the research generally finds…". |
| 4.2 | `live-action/landing-page-video-production.md` | "the numbers say 80% more of them convert" | Same: **on the live page**, no source given. Same decision needed. |
| 4.3 | `live-action/video-production-for-ceremonies-and-conferences.md` | "screens at **Mobile World Congress** in Barcelona" | The live page says "Mobile World Conference". We've written the event's actual name. Confirm that's the one you mean. |
| 4.4 | `live-action/live-streaming-video-production.md` | Bonded 4G/5G backup, hard-wired connection, slides taken as a clean desk feed | Not described anywhere on the live site. This is the paragraph a technical buyer will test you on — confirm it's all standard kit. |
| 4.5 | `aerial-drone-video-production.md` | How far we can go describing **UKPDRA-01** | We've toned the first draft down to "filming close to people and property, where the everyday Open-category rules run out". You're the pilot: give us the actual separation distances and congested-area permissions and we'll put a number in. A number beats an adjective. |
| 4.6 | `post-production/video-subtitling-and-transcription.md` and `post-production/bristish-sign-language-bsl-production.md` | WCAG captions requirement + the UK public-sector accessibility duty; the British Sign Language Act 2022 | Both accurate as written, both **new to these pages**. Flagging because they are legal statements on pages read by compliance people. |

## 5. Decisions needed on the new vodcast page (1)

| # | Page | What we need |
| --- | --- | --- |
| 5.1 | `live-action/video-podcast-production.md` | **The slug.** You said "vodcasts" and the copy uses that word, but search volume is overwhelmingly on *"video podcast"* — hardly anyone types "vodcast". The page is written for `/services/live-action/video-podcast-production/`. Choosing `vodcast-production` instead will cost real traffic. Your call, but it needs making before the page is created in WordPress. |

## 6. Fixed in this pass — no action needed

- **Invented statistic removed.** The internal communications sub-deck read
  "All-staff email. 900 recipients. 11% opened it. Twelve read past the first
  line." Those numbers appear nowhere in the live copy or SOURCE-FACTS.md.
  Replaced with a line that makes the same point without pretending to data.
- **Aerial slug resolved.** The routing table on `live-action/index.md` had a
  TODO asking for the aerial page's slug. It is
  `/services/aerial-drone-video-production/` and the link is now live in the
  table — worth a glance to confirm it matches WordPress.
- **Unverifiable longevity claim removed** from the explainer page ("most
  clients are still using theirs three years later").
- **3D animation dropped.** `copy/services/3d-animation/` deleted (family page,
  STEP-file renders, world-building). Two cross-references removed: the product
  page's "3D from a STEP file" line and the 2D index's link to 3D. 3D was never
  in the header menu, so no navigation change was needed.
- **Vodcasts added** as the fifteenth live-action service. The live-action index
  H1 counted the children, so it now reads "Fifteen kinds…", and a routing row
  was added. The menu item was added to both the desktop mega menu and the
  mobile mirror.
