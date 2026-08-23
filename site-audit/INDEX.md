# Pearldrop.com — live site audit

Captured **2026-08-23** from the live site at <https://pearldrop.com/>.

Source of truth for the URL list: the Yoast sitemap index at
`https://pearldrop.com/sitemap_index.xml`, which fans out to `page-sitemap.xml` (90),
`post-sitemap.xml` (22), `category-sitemap.xml` (3) and `author-sitemap.xml` (1) —
**116 URLs, all fetched successfully (HTTP 200).**

`https://pearldrop.com/sitemap.xml` and `/wp-sitemap.xml` both 301-redirect; the site
uses Yoast, not the WordPress core sitemap. Crawling every internal link on all 116
pages surfaced no additional live pages — the only off-sitemap targets were comment
pagination (`/slug/2/`), date archives, and three stale links:
`/services/aerial/` → 301 to `/services/aerial-drone-video-production/`,
`/meet-pearldrop/` → 301 to `/about-us/meet-pearldrop/`, and
`/services/photography/architectural/` → **404** (a dead link in the live footer/menu markup).

One markdown file per page lives beside this index, named after the slug.

---

## 1. Every URL found

116 URLs. Slug is the WordPress path; "File" is the capture in this folder.

### Home

| Slug | Title | File |
| --- | --- | --- |
| `/` | Outstanding corporate and charity video production and animation | [home.md](home.md) |

### About us

| Slug | Title | File |
| --- | --- | --- |
| `/about-us/` | About us | [about-us.md](about-us.md) |
| `/about-us/behind-the-scenes/` | Behind-the-scenes | [about-us-behind-the-scenes.md](about-us-behind-the-scenes.md) |
| `/about-us/employment/` | Employment | [about-us-employment.md](about-us-employment.md) |
| `/about-us/employment/junior-editor-and-animator/` | Junior Editor and Animator | [about-us-employment-junior-editor-and-animator.md](about-us-employment-junior-editor-and-animator.md) |
| `/about-us/employment/production-executive/` | Production Executive | [about-us-employment-production-executive.md](about-us-employment-production-executive.md) |
| `/about-us/how-we-work/` | How we work | [about-us-how-we-work.md](about-us-how-we-work.md) |
| `/about-us/meet-pearldrop/` | Meet Pearldrop - a quality Hertfordshire video production company | [about-us-meet-pearldrop.md](about-us-meet-pearldrop.md) |
| `/about-us/memberships/` | Memberships and Accreditations | [about-us-memberships.md](about-us-memberships.md) |
| `/about-us/our-clients/` | Our clients | [about-us-our-clients.md](about-us-our-clients.md) |
| `/about-us/our-showreels/` | Our showreels | [about-us-our-showreels.md](about-us-our-showreels.md) |
| `/about-us/our-values/` | Our values | [about-us-our-values.md](about-us-our-values.md) |
| `/about-us/privacy-policy/` | Privacy Policy | [about-us-privacy-policy.md](about-us-privacy-policy.md) |
| `/about-us/social-media/` | Social Media | [about-us-social-media.md](about-us-social-media.md) |
| `/about-us/sustainability/` | Sustainability | [about-us-sustainability.md](about-us-sustainability.md) |
| `/about-us/terms-of-service/` | Terms of Service | [about-us-terms-of-service.md](about-us-terms-of-service.md) |
| `/about-us/testimonials/` | Testimonials | [about-us-testimonials.md](about-us-testimonials.md) |
| `/about-us/why-video/` | Why video? | [about-us-why-video.md](about-us-why-video.md) |
| `/about-us/why-you-should-hire-pearldrop/` | Why you should hire Pearldrop | [about-us-why-you-should-hire-pearldrop.md](about-us-why-you-should-hire-pearldrop.md) |

### Services

| Slug | Title | File |
| --- | --- | --- |
| `/services/` | Services | [services.md](services.md) |
| `/services/2d-animation/` | 2D Animation | [services-2d-animation.md](services-2d-animation.md) |
| `/services/2d-animation/animated-character-video-production/` | Character animations for your business, brand or charity | [services-2d-animation-animated-character-video-production.md](services-2d-animation-animated-character-video-production.md) |
| `/services/2d-animation/animated-explainer-video-production/` | Animated explainer videos for your business, brand or charity | [services-2d-animation-animated-explainer-video-production.md](services-2d-animation-animated-explainer-video-production.md) |
| `/services/3d-animation/` | 3D Animation | [services-3d-animation.md](services-3d-animation.md) |
| `/services/3d-animation/step-file-renders/` | STEP-file renders | [services-3d-animation-step-file-renders.md](services-3d-animation-step-file-renders.md) |
| `/services/3d-animation/world-building/` | World-building | [services-3d-animation-world-building.md](services-3d-animation-world-building.md) |
| `/services/aerial-drone-video-production/` | Safe, reliable, high-quality aerial/drone video production | [services-aerial-drone-video-production.md](services-aerial-drone-video-production.md) |
| `/services/ai-video-production/` | AI video production for businesses and charities | [services-ai-video-production.md](services-ai-video-production.md) |
| `/services/live-action/` | Live-action | [services-live-action.md](services-live-action.md) |
| `/services/live-action/automotive-video-production/` | Top-quality automotive video production | [services-live-action-automotive-video-production.md](services-live-action-automotive-video-production.md) |
| `/services/live-action/automotive/` | Automotive | [services-live-action-automotive.md](services-live-action-automotive.md) |
| `/services/live-action/case-study-video-production/` | Case study video production for businesses and charities | [services-live-action-case-study-video-production.md](services-live-action-case-study-video-production.md) |
| `/services/live-action/charity-video-production/` | Emotive, powerful and impactful charity video production | [services-live-action-charity-video-production.md](services-live-action-charity-video-production.md) |
| `/services/live-action/company-and-brand-video-production/` | Outstanding video production for company and brand video production | [services-live-action-company-and-brand-video-production.md](services-live-action-company-and-brand-video-production.md) |
| `/services/live-action/high-quality-video-production-for-live-events/` | High-quality video production for live events | [services-live-action-high-quality-video-production-for-live-events.md](services-live-action-high-quality-video-production-for-live-events.md) |
| `/services/live-action/landing-page-video-production/` | Video production for landing pages | [services-live-action-landing-page-video-production.md](services-live-action-landing-page-video-production.md) |
| `/services/live-action/live-streaming-video-production/` | Live-streaming video production for businesses and charities | [services-live-action-live-streaming-video-production.md](services-live-action-live-streaming-video-production.md) |
| `/services/live-action/livestreaming/` | Livestreaming | [services-live-action-livestreaming.md](services-live-action-livestreaming.md) |
| `/services/live-action/product-video-production/` | Top-quality product videos | [services-live-action-product-video-production.md](services-live-action-product-video-production.md) |
| `/services/live-action/promotional-video-production/` | Promotional video production for your business, brand or charity | [services-live-action-promotional-video-production.md](services-live-action-promotional-video-production.md) |
| `/services/live-action/training-video-production/` | Training video production | [services-live-action-training-video-production.md](services-live-action-training-video-production.md) |
| `/services/live-action/video-production-for-activations-and-launches/` | High-quality video production for activations and launches | [services-live-action-video-production-for-activations-and-launches.md](services-live-action-video-production-for-activations-and-launches.md) |
| `/services/live-action/video-production-for-ceremonies-and-conferences/` | Outstanding video production for ceremonies and conferences | [services-live-action-video-production-for-ceremonies-and-conferences.md](services-live-action-video-production-for-ceremonies-and-conferences.md) |
| `/services/live-action/video-production-for-internal-communications/` | Top-quality video production for Internal Communications | [services-live-action-video-production-for-internal-communications.md](services-live-action-video-production-for-internal-communications.md) |
| `/services/photography/` | Photography | [services-photography.md](services-photography.md) |
| `/services/photography/architectural-photography/` | High-quality architectural photography | [services-photography-architectural-photography.md](services-photography-architectural-photography.md) |
| `/services/photography/automotive-photography/` | High-quality automotive photography | [services-photography-automotive-photography.md](services-photography-automotive-photography.md) |
| `/services/photography/headshot-photography/` | Outstanding headshot photography | [services-photography-headshot-photography.md](services-photography-headshot-photography.md) |
| `/services/photography/lifestyle-photography/` | Top-quality lifestyle photography | [services-photography-lifestyle-photography.md](services-photography-lifestyle-photography.md) |
| `/services/photography/live-event-photography/` | Outstanding live event photography | [services-photography-live-event-photography.md](services-photography-live-event-photography.md) |
| `/services/photography/photography-for-conferences-and-ceremonies/` | Outstanding photography for conferences and ceremonies | [services-photography-photography-for-conferences-and-ceremonies.md](services-photography-photography-for-conferences-and-ceremonies.md) |
| `/services/post-production/` | Post-production | [services-post-production.md](services-post-production.md) |
| `/services/post-production/bristish-sign-language-bsl-production/` | High-quality British Sign Language (BSL) video production | [services-post-production-bristish-sign-language-bsl-production.md](services-post-production-bristish-sign-language-bsl-production.md) |
| `/services/post-production/vfx-production/` | Professional visual effects (VFX) production | [services-post-production-vfx-production.md](services-post-production-vfx-production.md) |
| `/services/post-production/video-editing-services/` | High-quality professional video editing services | [services-post-production-video-editing-services.md](services-post-production-video-editing-services.md) |
| `/services/post-production/video-subtitling-and-transcription/` | Video subtitling and transcription | [services-post-production-video-subtitling-and-transcription.md](services-post-production-video-subtitling-and-transcription.md) |

### Sectors (under /services/)

| Slug | Title | File |
| --- | --- | --- |
| `/services/sectors/` | Sectors | [services-sectors.md](services-sectors.md) |
| `/services/sectors/education/` | Education | [services-sectors-education.md](services-sectors-education.md) |
| `/services/sectors/golf-courses/` | Golf Courses | [services-sectors-golf-courses.md](services-sectors-golf-courses.md) |
| `/services/sectors/science-technology/` | Science and Technology | [services-sectors-science-technology.md](services-sectors-science-technology.md) |

### Portfolio

| Slug | Title | File |
| --- | --- | --- |
| `/portfolio/` | Portfolio | [portfolio.md](portfolio.md) |
| `/portfolio/photography-2/` | Photography | [portfolio-photography-2.md](portfolio-photography-2.md) |
| `/portfolio/photography/` | Pearldrop's high-quality photography portfolio | [portfolio-photography.md](portfolio-photography.md) |
| `/portfolio/photography/ai/` | AI | [portfolio-photography-ai.md](portfolio-photography-ai.md) |
| `/portfolio/photography/architectural-photography-portfolio/` | Pearldrop's high-quality architectural photography portfolio | [portfolio-photography-architectural-photography-portfolio.md](portfolio-photography-architectural-photography-portfolio.md) |
| `/portfolio/photography/automotive-photography-portfolio/` | Pearldrop's high-quality automotive photography portfolio | [portfolio-photography-automotive-photography-portfolio.md](portfolio-photography-automotive-photography-portfolio.md) |
| `/portfolio/photography/awards-ceremonies-and-conferences-photography-portfolio/` | High-quality awards ceremonies and conferences photography | [portfolio-photography-awards-ceremonies-and-conferences-photography-portfolio.md](portfolio-photography-awards-ceremonies-and-conferences-photography-portfolio.md) |
| `/portfolio/photography/clients/` | Clients | [portfolio-photography-clients.md](portfolio-photography-clients.md) |
| `/portfolio/photography/hcci-golf-day-2023/` | HCCI Golf Day 2023 | [portfolio-photography-hcci-golf-day-2023.md](portfolio-photography-hcci-golf-day-2023.md) |
| `/portfolio/photography/hcci-summer-party-2023/` | HCCI Summer Party 2023 | [portfolio-photography-hcci-summer-party-2023.md](portfolio-photography-hcci-summer-party-2023.md) |
| `/portfolio/photography/hcci-summer-party-2024/` | HCCI Summer Party 2024 | [portfolio-photography-hcci-summer-party-2024.md](portfolio-photography-hcci-summer-party-2024.md) |
| `/portfolio/photography/hcci-women-in-leadership-conference-2024/` | HCCI Women in Leadership Conference 2024 | [portfolio-photography-hcci-women-in-leadership-conference-2024.md](portfolio-photography-hcci-women-in-leadership-conference-2024.md) |
| `/portfolio/photography/headshot-photography-portfolio/` | Pearldrop's high-quality headshot photography portfolio | [portfolio-photography-headshot-photography-portfolio.md](portfolio-photography-headshot-photography-portfolio.md) |
| `/portfolio/photography/inspiring-herts-awards-2024-launch/` | Inspiring Herts Awards 2024 launch | [portfolio-photography-inspiring-herts-awards-2024-launch.md](portfolio-photography-inspiring-herts-awards-2024-launch.md) |
| `/portfolio/photography/lifestyle-photography-portolio/` | Pearldrop's high-quality lifestyle photography portfolio | [portfolio-photography-lifestyle-photography-portolio.md](portfolio-photography-lifestyle-photography-portolio.md) |
| `/portfolio/photography/live-event-photography-portfolio/` | Pearldrop's high-quality live-event photography portfolio | [portfolio-photography-live-event-photography-portfolio.md](portfolio-photography-live-event-photography-portfolio.md) |
| `/portfolio/plx-awards-2025-tender-submission/` | PLx Awards 2025 Tender Submission | [portfolio-plx-awards-2025-tender-submission.md](portfolio-plx-awards-2025-tender-submission.md) |
| `/portfolio/video/` | Video | [portfolio-video.md](portfolio-video.md) |
| `/portfolio/video/2d-animation/` | 2D animation | [portfolio-video-2d-animation.md](portfolio-video-2d-animation.md) |
| `/portfolio/video/live-action/` | Live-action | [portfolio-video-live-action.md](portfolio-video-live-action.md) |

### Case studies

| Slug | Title | File |
| --- | --- | --- |
| `/case-studies/` | Case studies | [case-studies.md](case-studies.md) |
| `/case-studies/healthy-body-healthy-mind-hertfordshire/` | Healthy Body Healthy Mind Hertfordshire | [case-studies-healthy-body-healthy-mind-hertfordshire.md](case-studies-healthy-body-healthy-mind-hertfordshire.md) |
| `/case-studies/inspiring-hertfordshire-awards/` | Inspiring Hertfordshire Awards | [case-studies-inspiring-hertfordshire-awards.md](case-studies-inspiring-hertfordshire-awards.md) |
| `/case-studies/nv200-campervan/` | NV200 Campervan | [case-studies-nv200-campervan.md](case-studies-nv200-campervan.md) |

### Top-level / utility

| Slug | Title | File |
| --- | --- | --- |
| `/blog/` | Blog | [blog.md](blog.md) |
| `/contact/` | Contact | [contact.md](contact.md) |
| `/home-2/` | Home | [home-2.md](home-2.md) |
| `/main-site-header/` | Main Site Header | [main-site-header.md](main-site-header.md) |
| `/sitemap/` | Sitemap | [sitemap.md](sitemap.md) |

### Category archives

| Slug | Title | File |
| --- | --- | --- |
| `/category/film-term-friday/` | Film Term Friday Archives | [category-film-term-friday.md](category-film-term-friday.md) |
| `/category/production-tips/` | Production tips Archives | [category-production-tips.md](category-production-tips.md) |
| `/category/uncategorized/` | Uncategorized Archives | [category-uncategorized.md](category-uncategorized.md) |

### Author archives

| Slug | Title | File |
| --- | --- | --- |
| `/author/simon_pm_2023/` | Simon, Author at Pearldrop - Video Production Hertfordshire | [author-simon_pm_2023.md](author-simon_pm_2023.md) |

### Blog posts

| Slug | Title | File |
| --- | --- | --- |
| `/%f0%9f%9a%a8-so-heres-a-cautionary-tale-navigating-the-so-saga-in-video-interviews-%f0%9f%9a%a8/` | 🚨 So Here's a Cautionary Tale: Navigating the 'So' Saga in Video Interviews 🚨 | [so-heres-a-cautionary-tale-navigating-the-so-saga-in-video-interviews.md](so-heres-a-cautionary-tale-navigating-the-so-saga-in-video-interviews.md) |
| `/10507-2/` | What It Really Means to Be in the Top 0.1% of ChatGPT Users | [10507-2.md](10507-2.md) |
| `/alan-smithee/` | Alan Smithee | [alan-smithee.md](alan-smithee.md) |
| `/baby/` | Baby | [baby.md](baby.md) |
| `/behind-the-scenes-unveiling-the-magic-with-meet-the-team-videos/` | Humanising your brand with 'Meet the Team' Videos | [behind-the-scenes-unveiling-the-magic-with-meet-the-team-videos.md](behind-the-scenes-unveiling-the-magic-with-meet-the-team-videos.md) |
| `/cheeseplate/` | Cheeseplate | [cheeseplate.md](cheeseplate.md) |
| `/cookie/` | Cookie | [cookie.md](cookie.md) |
| `/dolly/` | Dolly | [dolly.md](dolly.md) |
| `/easter-egg/` | Easter Egg | [easter-egg.md](easter-egg.md) |
| `/film-term-friday-the-c47/` | Film-term Friday: the C47 | [film-term-friday-the-c47.md](film-term-friday-the-c47.md) |
| `/golden-hour/` | Golden Hour | [golden-hour.md](golden-hour.md) |
| `/great-gatsby-on-a-shoestring-how-ai-turned-us-into-1920s-movie-moguls-for-under-60/` | Great Gatsby on a Shoestring: How AI Turned Us into 1920s Movie Moguls for Under $60! | [great-gatsby-on-a-shoestring-how-ai-turned-us-into-1920s-movie-moguls-for-under-60.md](great-gatsby-on-a-shoestring-how-ai-turned-us-into-1920s-movie-moguls-for-under-60.md) |
| `/hollywood-baby/` | Hollywood, baby! | [hollywood-baby.md](hollywood-baby.md) |
| `/how-to-be-interviewed/` | How to be interviewed | [how-to-be-interviewed.md](how-to-be-interviewed.md) |
| `/logline/` | Logline | [logline.md](logline.md) |
| `/the-animated-advantage-why-2d-animation-is-corporate-marketings-secret-sauce/` | The Animated Advantage: Why 2D Animation is Corporate Marketing's Secret Sauce | [the-animated-advantage-why-2d-animation-is-corporate-marketings-secret-sauce.md](the-animated-advantage-why-2d-animation-is-corporate-marketings-secret-sauce.md) |
| `/the-power-of-a-professional-image-why-you-need-outstanding-corporate-headshots/` | The Power of a Professional Image: Why You Need Outstanding Corporate Headshots | [the-power-of-a-professional-image-why-you-need-outstanding-corporate-headshots.md](the-power-of-a-professional-image-why-you-need-outstanding-corporate-headshots.md) |
| `/weve-been-nominated-for-an-award/` | We've been nominated for an award! | [weve-been-nominated-for-an-award.md](weve-been-nominated-for-an-award.md) |
| `/what-makes-2d-animation-a-great-choice-for-your-business/` | What makes 2D animation a great choice for your business? | [what-makes-2d-animation-a-great-choice-for-your-business.md](what-makes-2d-animation-a-great-choice-for-your-business.md) |
| `/what-the-who/` | WHAT THE WHO?? | [what-the-who.md](what-the-who.md) |
| `/winning/` | winning | [winning.md](winning.md) |
| `/woof/` | Woof! | [woof.md](woof.md) |
| `/your-teams-headshots-are-boring-watch-how-we-turned-ours-into-eye-popping-animated-masterpieces/` | Your Team’s Headshots Are Boring - Watch How We Turned Ours into Eye-Popping Animated Masterpieces! | [your-teams-headshots-are-boring-watch-how-we-turned-ours-into-eye-popping-animated-masterpieces.md](your-teams-headshots-are-boring-watch-how-we-turned-ours-into-eye-popping-animated-masterpieces.md) |

---

## 2. Main navigation, exactly as it appears live

Two menus are present in the page markup.

### 2a. Primary menu — the real WordPress menu (`ul#menu-1-a2773b9`)

This is the full tree with real slugs, and is the one to rebuild against.
Three levels deep under Services and Portfolio.

- **About us** — `/about-us/`
  - **Meet Pearldrop** — `/about-us/meet-pearldrop/`
  - **Our showreels** — `/about-us/our-showreels/`
  - **How we work** — `/about-us/how-we-work/`
  - **Our clients** — `/about-us/our-clients/`
  - **Our values** — `/about-us/our-values/`
  - **Testimonials** — `/about-us/testimonials/`
  - **Why video?** — `/about-us/why-video/`
  - **Memberships and Accreditations** — `/about-us/memberships/`
  - **Sustainability** — `/about-us/sustainability/`
  - **Employment** — `/about-us/employment/`
  - **Terms of Service** — `/about-us/terms-of-service/`
  - **Privacy Policy** — `/about-us/privacy-policy/`
- **Services** — `/services/`
  - **Live-action** — `/services/live-action/`
    - **Activations and launches** — `/services/live-action/video-production-for-activations-and-launches/`
    - **Automotive** — `/services/live-action/automotive/`
    - **Case study videos** — `/services/live-action/case-study-video-production/`
    - **Ceremonies and conferences** — `/services/live-action/video-production-for-ceremonies-and-conferences/`
    - **Charity** — `/services/live-action/charity-video-production/`
    - **Company and brand video production** — `/services/live-action/company-and-brand-video-production/`
    - **Internal Communications** — `/services/live-action/video-production-for-internal-communications/`
    - **Landing pages** — `/services/live-action/landing-page-video-production/`
    - **Live-streaming** — `/services/live-action/live-streaming-video-production/`
    - **Live events** — `/services/live-action/high-quality-video-production-for-live-events/`
    - **Product videos** — `/services/live-action/product-video-production/`
    - **Promotional video production** — `/services/live-action/promotional-video-production/`
    - **Training videos** — `/services/live-action/training-video-production/`
  - **2D Animation** — `/services/2d-animation/`
    - **Animated character videos** — `/services/2d-animation/animated-character-video-production/`
    - **Animated explainer videos** — `/services/2d-animation/animated-explainer-video-production/`
  - **3D Animation** — `/services/3d-animation/`
    - **STEP-file renders** — `/services/3d-animation/step-file-renders/`
    - **World-building** — `/services/3d-animation/world-building/`
  - **Aerial/drone video production** — `/services/aerial-drone-video-production/`
  - **Photography** — `/services/photography/`
    - **Architectural photography** — `/services/photography/architectural-photography/`
    - **Conference and ceremony photography** — `/services/photography/photography-for-conferences-and-ceremonies/`
    - **Headshot photography** — `/services/photography/headshot-photography/`
    - **Lifestyle photography** — `/services/photography/lifestyle-photography/`
    - **Live event photography** — `/services/photography/live-event-photography/`
  - **Post-production** — `/services/post-production/`
    - **Professional video editing** — `/services/post-production/video-editing-services/`
    - **Video subtitling and transcription** — `/services/post-production/video-subtitling-and-transcription/`
    - **Professional visual effects (VFX) production** — `/services/post-production/vfx-production/`
- **Portfolio** — `/portfolio/`
  - **Video** — `/portfolio/video/`
    - **Live-action** — `/portfolio/video/live-action/`
    - **2D animation** — `/portfolio/video/2d-animation/`
  - **Photography** — `/portfolio/photography/`
    - **Headshot photography portfolio** — `/portfolio/photography/headshot-photography-portfolio/`
    - **Live-event photography portfolio** — `/portfolio/photography/live-event-photography-portfolio/`
    - **Lifestyle photography portfolio** — `/portfolio/photography/lifestyle-photography-portolio/`
    - **Architectural photography portfolio** — `/portfolio/photography/architectural-photography-portfolio/`
    - **Automotive photography portfolio** — `/portfolio/photography/automotive-photography-portfolio/`
- **Case studies** — `/case-studies/`
  - **Inspiring Hertfordshire Awards** — `/case-studies/inspiring-hertfordshire-awards/`
  - **Healthy Body Healthy Mind Hertfordshire** — `/case-studies/healthy-body-healthy-mind-hertfordshire/`
  - **NV200 Campervan** — `/case-studies/nv200-campervan/`
- **Blog** — `/blog/`
- **Contact** — `/contact/`
- **Home** — `/home-2/`
- **winning** — `/winning/`

> The last two items — **Home** (`/home-2/`) and **winning** (`/winning/`) — sit at
> top level in the menu but are not styled as visible nav items on the live site.
> `/home-2/` is an orphaned duplicate homepage and `/winning/` is a blog post.
> Both look like menu cruft rather than intended navigation.

### 2b. Visible top bar (UAEL nav widget)

The header users actually see is a shorter six-item bar. Note **About Us** here is
a `#` placeholder that opens a dropdown; it does not link to `/about-us/`.

- **About Us** — `#` (no link)
- **Services** — `/services/`
- **Portfolio** — `/portfolio/`
- **Case Studies** — `/case-studies/`
- **Blog** — `/blog/`
- **Contact** — `/contact/`

### 2c. Footer menu

```
Company info      Services              Legal
  Meet Pearldrop    Live-action video     Terms of Service
  Our showreels     2D animation          Privacy Policy
  How we work       3D animation          Sitemap
  Our values        Aerial/drone          Contact us
  Why video?        Photography
  Sustainability
  Employment
```

Footer slugs: `/about-us/meet-pearldrop/`, `/about-us/our-showreels/`,
`/about-us/how-we-work/`, `/about-us/our-values/`, `/about-us/why-video/`,
`/about-us/sustainability/`, `/about-us/employment/`, `/services/live-action/`,
`/services/2d-animation/`, `/services/3d-animation/`,
`/services/aerial-drone-video-production/`, `/services/photography/`,
`/about-us/terms-of-service/`, `/about-us/privacy-policy/`, `/sitemap/`, `/contact/`.

Footer strapline: *"We create top-quality video, animation and photography for your
website, marketing, training and broadcast needs."* — plus a "Signup to our
newsletter" Elementor popup trigger and the copyright line "2026 Pearldrop Ltd".

> Two footer bugs worth carrying over as fixes, not features: the **Aerial/drone**
> text link points at the dead `/services/aerial/`, and the image links behind
> **Live-action video** and **2D animation** point at `/portfolio/video/...` while
> their text links point at `/services/...`.

### 2d. Pages in the sitemap but NOT in the primary or top-bar menu

Excluding blog posts (reachable via `/blog/`) and the category/author archives,
these pages exist and return 200 but are linked from no menu. Each needs a keep,
redirect or delete decision in the rebuild. (`/sitemap/` is the one entry here
that *is* linked — from the footer only.)

- `/about-us/behind-the-scenes/`
- `/about-us/employment/junior-editor-and-animator/`
- `/about-us/employment/production-executive/`
- `/about-us/social-media/`
- `/about-us/why-you-should-hire-pearldrop/`
- `/main-site-header/`
- `/portfolio/photography-2/`
- `/portfolio/photography/ai/`
- `/portfolio/photography/awards-ceremonies-and-conferences-photography-portfolio/`
- `/portfolio/photography/clients/`
- `/portfolio/photography/hcci-golf-day-2023/`
- `/portfolio/photography/hcci-summer-party-2023/`
- `/portfolio/photography/hcci-summer-party-2024/`
- `/portfolio/photography/hcci-women-in-leadership-conference-2024/`
- `/portfolio/photography/inspiring-herts-awards-2024-launch/`
- `/portfolio/plx-awards-2025-tender-submission/`
- `/services/ai-video-production/`
- `/services/live-action/automotive-video-production/`
- `/services/live-action/livestreaming/`
- `/services/photography/automotive-photography/`
- `/services/post-production/bristish-sign-language-bsl-production/`
- `/services/sectors/`
- `/services/sectors/education/`
- `/services/sectors/golf-courses/`
- `/services/sectors/science-technology/`
- `/sitemap/`

The 22 blog posts and the 3 category archives (`/category/film-term-friday/`,
`/category/production-tips/`, `/category/uncategorized/`) plus the author archive
`/author/simon_pm_2023/` are listed in section 1.

---

## 3. Services

Six top-level services, with children as they appear in the menu.

- **Live-action** — `/services/live-action/`
  - Activations and launches — `/services/live-action/video-production-for-activations-and-launches/`
  - Automotive — `/services/live-action/automotive/`
  - Case study videos — `/services/live-action/case-study-video-production/`
  - Ceremonies and conferences — `/services/live-action/video-production-for-ceremonies-and-conferences/`
  - Charity — `/services/live-action/charity-video-production/`
  - Company and brand video production — `/services/live-action/company-and-brand-video-production/`
  - Internal Communications — `/services/live-action/video-production-for-internal-communications/`
  - Landing pages — `/services/live-action/landing-page-video-production/`
  - Live-streaming — `/services/live-action/live-streaming-video-production/`
  - Live events — `/services/live-action/high-quality-video-production-for-live-events/`
  - Product videos — `/services/live-action/product-video-production/`
  - Promotional video production — `/services/live-action/promotional-video-production/`
  - Training videos — `/services/live-action/training-video-production/`
- **2D Animation** — `/services/2d-animation/`
  - Animated character videos — `/services/2d-animation/animated-character-video-production/`
  - Animated explainer videos — `/services/2d-animation/animated-explainer-video-production/`
- **3D Animation** — `/services/3d-animation/`
  - STEP-file renders — `/services/3d-animation/step-file-renders/`
  - World-building — `/services/3d-animation/world-building/`
- **Aerial/drone video production** — `/services/aerial-drone-video-production/`
- **Photography** — `/services/photography/`
  - Architectural photography — `/services/photography/architectural-photography/`
  - Conference and ceremony photography — `/services/photography/photography-for-conferences-and-ceremonies/`
  - Headshot photography — `/services/photography/headshot-photography/`
  - Lifestyle photography — `/services/photography/lifestyle-photography/`
  - Live event photography — `/services/photography/live-event-photography/`
- **Post-production** — `/services/post-production/`
  - Professional video editing — `/services/post-production/video-editing-services/`
  - Video subtitling and transcription — `/services/post-production/video-subtitling-and-transcription/`
  - Professional visual effects (VFX) production — `/services/post-production/vfx-production/`

Three service pages exist but are **not in the menu**:

- `/services/ai-video-production/` — AI video production
- `/services/live-action/automotive-video-production/` — a second automotive page alongside `/services/live-action/automotive/`
- `/services/live-action/livestreaming/` — a near-empty duplicate of `/services/live-action/live-streaming-video-production/` (44 words)
- `/services/post-production/bristish-sign-language-bsl-production/` — British Sign Language (BSL) production; note the typo **"bristish"** in the live slug

Home/Services card taglines as written live:

- Live-action — *"Interviews. Case studies. Awards ceremonies. Products. Training."*
- 2D animation — *"Explainers. Characters. Instructional and training films."*
- Photography — *"Headshots. Portraits. Lifestyle. Packshots. Products. Live events."*

---

## 4. Sectors

Sectors live under Services (`/services/sectors/`) and are **absent from the menu**.
There are exactly three:

| Sector | Slug | Description as written live |
| --- | --- | --- |
| Science & Technology | `/services/sectors/science-technology/` | Biotech, pharma, defence, engineering and manufacturing. |
| Education | `/services/sectors/education/` | Promotional and learning content for schools, colleges and universities. |
| Golf Courses | `/services/sectors/golf-courses/` | Course promos, flyovers, overviews and advice from the Club Pro. |

The sectors landing page also names, in prose, the wider industries worked in:
technology, healthcare, education, entertainment and hospitality.

---

## 5. Case studies

Three, all under `/case-studies/`:

| Case study | Slug | Blurb as written live |
| --- | --- | --- |
| The Inspiring Hertfordshire Awards | `/case-studies/inspiring-hertfordshire-awards/` | We provided a live feed for the big screens on the night, pre-recorded content to launch the evening, a highlights film and event photography. |
| Healthy Body Healthy Mind Hertfordshire | `/case-studies/healthy-body-healthy-mind-hertfordshire/` | A suite of fitness films, starring the Firefighters of Hertfordshire Fire Service. |
| The NV200 Campervan | `/case-studies/nv200-campervan/` | A promotional film with a unique product and a top-class presenter. |

---

## 6. Portfolio

### 6a. Structure

```
/portfolio/
  /portfolio/video/
    /portfolio/video/live-action/
    /portfolio/video/2d-animation/
  /portfolio/photography/
    /portfolio/photography/headshot-photography-portfolio/
    /portfolio/photography/live-event-photography-portfolio/
    /portfolio/photography/lifestyle-photography-portolio/      <- note misspelling "portolio"
    /portfolio/photography/architectural-photography-portfolio/
    /portfolio/photography/automotive-photography-portfolio/
```

Also present but not in the menu:

- `/portfolio/photography-2/` — an orphaned duplicate of the photography index
- `/portfolio/photography/ai/` — AI imagery gallery
- `/portfolio/photography/clients/` — photography client gallery index
- `/portfolio/photography/awards-ceremonies-and-conferences-photography-portfolio/`
- `/portfolio/plx-awards-2025-tender-submission/` — 17 words, looks like a private tender page
- Event galleries: `/portfolio/photography/hcci-golf-day-2023/`, `/hcci-summer-party-2023/`,
  `/hcci-summer-party-2024/`, `/hcci-women-in-leadership-conference-2024/`,
  `/inspiring-herts-awards-2024-launch/`

### 6b. Live-action portfolio items

Filter tabs on the page: All / Promotional / Live-event / Case-studies / Charity / Product / Training.

- Lokkelebury Vineyard
- Grant Palmer Christmas campaign 2025
- biz4Biz Awards 2025
- LSBU Apprenticeships
- Animal Free Research x Rankin
- Animal Free Research - Prof Julian Ma
- Grant Palmer Christmas Campaign 2024
- North Herts College Film Studies Course
- Grant Palmer: Man v Bus
- St John's College Cambridge May Ball 2024
- Grant Palmer Christmas campaign
- QinetiQ Fellows
- Flackwell Heath Golf Club
- Burgers and Barbers
- Fareshare Guildford launch
- Intalink promo
- Lussmans - how to make Coq au Vin
- Orfium and Cavendish Music
- NHC promo
- Local Skills Improvement Programme
- Herts Young Homeless
- Marlo Clarke speaker reel
- Fareshare site tour
- Blesma homepage film
- ENHHT appeal
- The Inspiring Herts Awards 2022
- The Gentlemen Barristas
- London's Greatest Weekends
- Hertfordshire County Show 2024
- Hertfordshire Chamber Golf Day 2022
- IcelandAir - Around the corner
- Snarebrook Preparatory School
- Borough of Broxbourne Awards 2023
- Women in Leadership Conference 2023
- Lost Mountain Moonshine

### 6c. 2D animation portfolio items

Filter tabs: All / Explainer / Character / Promotional.

- OneYMCA Domestic Abuse Helpline
- Hertfordshire County Council Interlink Bus Campaign
- Nordic Dry explainer
- 1YMCA Hertfordshire - Threads of Healing
- Hertfordshire County Council COVID awareness campaign
- Herts Young Homeless: Beth's story
- The Entire History of World Communication
- Herts Young Homeless Support Worker story
- Citizens Advice Harlow
- Easybuild
- Orange Feels Worried
- Meet the Rainbow Drops
- Conidia Fuelstat Result
- Pearldrop landing page video
- Citizens Advice East Herts
- T-Levels overview
- HOP into apprenticeships

Both portfolio pages embed their films from YouTube and Vimeo; the embed URLs are
preserved in the per-page captures.

### 6d. Showreels

`/about-us/our-showreels/` carries a main showreel plus category showreels for
**Live Events**, **2D animation**, **Promotional video** and **Aerial/drone**, and a
"The time tunnel" section of older reels.

---

## 7. Portfolio images

643 unique image URLs across 23 portfolio and case-study pages,
taken from the live markup (including gallery/lightbox sources, not just `<img>` tags).
WordPress size suffixes (`-300x169`) have been normalised away, so these are the
full-size originals. **Not downloaded**, as instructed.

### /case-studies/healthy-body-healthy-mind-hertfordshire/

3 images.

- https://pearldrop.com/wp-content/uploads/2023/03/HB-thumb-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Healthy-Body-thumb-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Team-photo.jpg

### /case-studies/inspiring-hertfordshire-awards/

19 images.

- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-10-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-10.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-11-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-11.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-2-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-3-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-4-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-5-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-5.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-6-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-6.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-7-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-8-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-8.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-9-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-9.jpg

### /case-studies/nv200-campervan/

8 images.

- https://pearldrop.com/wp-content/uploads/2023/03/NV200-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-5.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-6.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-website-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200.jpg

### /portfolio/

2 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Winners.-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/04/2D-animation-example-1.jpg

### /portfolio/photography-2/

14 images.

- https://pearldrop.com/wp-content/uploads/2023/02/Rob-with-camera-lifestyle-small.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/3D-showreel-thumbnail-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/3D-world-building-showreel-1-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Drone-BG-thumb-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Easybuild.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Editing-main-thumb-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Inspiring-Herts-Awards-2022-winners-23.jpg
- https://pearldrop.com/wp-content/uploads/2023/04/2D-animation-example-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Drone.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Herts-Chamebr-Golf-Day-2023-hero-low-res-8.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/James-with-steadicam.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Post-prod2.jpg

### /portfolio/photography/

46 images.

- https://pearldrop.com/wp-content/uploads/2023/02/Katie-headshot-square-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/NV200-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Rob-headshot-square-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/15a-Hoecroft-Nazeing-low-res-8.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/4-The-Chestnuts-Hertford-low-res.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Bridge-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/CandC-main-thumbnail-2-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Georgia-headshot-square-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Health-walk-5-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-5-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IH-22-gallery-6-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Kitchen-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Lifestyle-main-thumb-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Live-events-main-thumb-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/OPES-Dani.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Shotgun.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Timetable.-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Training.-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Wilshere-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Marlo-headshot-square-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/e-nv200-angles-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/e-nv200-beauty-1.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/15a-Hoecroft-Nazeing-low-res-8-q7awqgp8wqtqrvwfrs2a5wvn7gk6bfb3xv7q7hzlk8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/4-The-Chestnuts-Hertford-low-res-q7awqzi0pfjh8354q06tjs4v35zilddqog9ft17q3s.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Bridge-3-q7awse9ayhgyn13ehm4oafbr5z1c50z8vfhnpz4grs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CandC-main-thumbnail-2-t-q7aws9k40baj0za8923jfyig71oi2jgl6s88blbfmw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Cospace-lights-q7awsf755bi8yn21c4jaux37rcwpcq2z7k557932lk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Georgia-headshot-square-1-t-q7awr39dgromiizo41tbtr6pgpgzg5so0yvdq525ew.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Health-walk-5-t-q7awqtuzkfbrafdbmxr24tk3iurbb6rcnocixdg354.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IH-22-gallery-5-1-q7awr7ykexv24ksuclugo800fmttinbbpm4t4iv6js.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IH-22-gallery-6-1-q7awqzi0pfjh8354q06tjs4v35zilddqog9ft17q3s.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Inspiring-Herts-Case-Study-thumb-2-q7awqkglo2yw2bqz5tosfvxhl01n67q1adto4lu0vc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Katie-headshot-square-1-t-q7awpd80xpbp89hs6azy96ua99yrc4ydsftc1vm4tk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Kitchen-3-q7awras2zfyx3eoqw52cdpae7sfx5qmiq039kcr014.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Lifestyle-main-thumb-1-t-q7aws21ehn08g3l5gyuiw0erfypkcymqhr0chdml0o.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Live-events-main-thumb-1-t-q7awrfh9xm5cpghx4p3h863p6psr8856encoyqk160.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/NV200-thumbnail-t-q7awp9go6d6jxtn8s9dfz7sfvqhahcjgfx7e4rrpig.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/OPES-Dani-q7awqb27rqm0u84mopmiqyavn5bz18opx3atbu7ylk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Rob-headshot-square-1-t-q7awpd80xpbp89hs6azy96ua99yrc4ydsftc1vm4tk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Shotgun-q7awqr1gzx7wblhf3ej6fc9pqp57o3g5nae2hjk9ns.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Timetable.-t-q7awsmpunzsjjir447sbev6wifvn2awtwld11grx7s.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Training.-t-q7awqsx5dlagyteosfcfkbsmxgvy3hnmbjp1g3hhbc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Wilshere-1-q7aws8m9th98pdblejowvgqzlnt4uucuunkqubctt4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/e-nv200-angles-2-q81ole9nyj1r9xrkdl0u4rb40lxt5tnxxmxeh5jai0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/e-nv200-beauty-1-q81olpjq8jh759b6jpwcyogn58e7q6wpz6r88h2kfc.jpg

### /portfolio/photography/ai/

116 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Museum-of-London-The-Last-Weekend-Day-3-heroes-low-res-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2024/02/Newscat-header-2.jpg
- https://pearldrop.com/wp-content/uploads/2024/02/Racing-cats-header-tiny.jpg
- https://pearldrop.com/wp-content/uploads/2024/02/Vicatrian-header-3-tiny.jpg
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_film_crew_filming_a_new_compact_electric_street_6772352d-4b92-4433-99bd-eb4561b92418_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_film_crew_filming_a_new_compact_electric_street_6772352d-4b92-4433-99bd-eb4561b92418_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_film_crew_filming_a_new_compact_electric_street_6772352d-4b92-4433-99bd-eb4561b92418_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_film_crew_filming_a_new_compact_electric_street_6772352d-4b92-4433-99bd-eb4561b92418_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_graphic_artist_sits_at_a_desk_in_a_modern_offic_97d5ef2e-a597-4716-9be6-396e8f2a9ad4_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_graphic_artist_sits_at_a_desk_in_a_modern_offic_97d5ef2e-a597-4716-9be6-396e8f2a9ad4_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_graphic_artist_sits_at_a_desk_in_a_modern_offic_97d5ef2e-a597-4716-9be6-396e8f2a9ad4_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_graphic_artist_sits_at_a_desk_in_a_modern_offic_97d5ef2e-a597-4716-9be6-396e8f2a9ad4_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_graphic_artist_sits_at_a_desk_in_a_modern_offic_a061a3bc-3dcc-4911-b628-d598baa11d0d_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_graphic_artist_sits_at_a_desk_in_a_modern_offic_a061a3bc-3dcc-4911-b628-d598baa11d0d_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photograph_of_an_artist_sitting_at_a_desk_in_a__045ce4aa-782f-4880-a84f-b061b655f437_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photograph_of_an_artist_sitting_at_a_desk_in_a__045ce4aa-782f-4880-a84f-b061b655f437_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photograph_of_an_artist_sitting_at_a_desk_in_a__045ce4aa-782f-4880-a84f-b061b655f437_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photograph_of_an_artist_sitting_at_a_desk_in_a__045ce4aa-782f-4880-a84f-b061b655f437_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photograph_of_an_artist_sitting_at_a_desk_in_a_mo_3a4701e9-773b-402c-bc66-ebfe5daf75b2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photograph_of_an_artist_sitting_at_a_desk_in_a_mo_e337ff1b-0a47-478c-8bb4-1b9572cf55f1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photoreal_image_of_an_artist_sits_at_a_desk_in__e79b308c-b3de-43cd-9d64-023cf16c7788_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photoreal_image_of_an_artist_sits_at_a_desk_in__e79b308c-b3de-43cd-9d64-023cf16c7788_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photoreal_image_of_an_artist_sits_at_a_desk_in__e79b308c-b3de-43cd-9d64-023cf16c7788_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_photoreal_image_of_an_artist_sits_at_a_desk_in__e79b308c-b3de-43cd-9d64-023cf16c7788_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_stunning_stag_raising_its_head_out_of_the_heath_1b790547-f3ca-4abb-a2dd-000cd4fd124c_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_stunning_stag_raising_its_head_out_of_the_heath_1b790547-f3ca-4abb-a2dd-000cd4fd124c_1-1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_stunning_stag_raising_its_head_out_of_the_heath_1b790547-f3ca-4abb-a2dd-000cd4fd124c_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_stunning_stag_raising_its_head_out_of_the_heath_1b790547-f3ca-4abb-a2dd-000cd4fd124c_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych._in_frame_one_science_and_technology.__6ad89409-bccb-45c6-ba5a-0bdf45b29108_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych._in_frame_one_science_and_technology.__6ad89409-bccb-45c6-ba5a-0bdf45b29108_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych._in_frame_one_science_and_technology.__6ad89409-bccb-45c6-ba5a-0bdf45b29108_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych._in_frame_one_science_and_technology.__6ad89409-bccb-45c6-ba5a-0bdf45b29108_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych._in_one_frame_science_and_technology.__bc218d84-7678-4253-bb10-29747ca36db2_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych._in_one_frame_science_and_technology.__bc218d84-7678-4253-bb10-29747ca36db2_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych._in_one_frame_science_and_technology.__bc218d84-7678-4253-bb10-29747ca36db2_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych._in_one_frame_science_and_technology.__bc218d84-7678-4253-bb10-29747ca36db2_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych_of_images_representent_science__tecnho_e826fcc5-5a1f-4037-b7ca-4a8f8cae2ac5_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych_of_images_representent_science__tecnho_e826fcc5-5a1f-4037-b7ca-4a8f8cae2ac5_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych_of_images_representent_science__tecnho_e826fcc5-5a1f-4037-b7ca-4a8f8cae2ac5_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_a_triptych_of_images_representent_science__tecnho_e826fcc5-5a1f-4037-b7ca-4a8f8cae2ac5_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_boxer_looking_at_camera_holding_his_gloves_up_rea_eeec364e-f329-4b07-86cc-b193e49c3f64_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_boxer_looking_at_camera_holding_his_gloves_up_rea_eeec364e-f329-4b07-86cc-b193e49c3f64_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_boxer_looking_at_camera_holding_his_gloves_up_rea_eeec364e-f329-4b07-86cc-b193e49c3f64_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_boxer_looking_at_camera_holding_his_gloves_up_rea_eeec364e-f329-4b07-86cc-b193e49c3f64_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_newscaster_in_tv_studio_looking_at_autocue._T_942e3074-f7dc-4f2c-8368-60ae1beeb28e_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_newscaster_in_tv_studio_looking_at_autocue._T_942e3074-f7dc-4f2c-8368-60ae1beeb28e_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_newscaster_in_tv_studio_looking_at_autocue_-_dffd1482-28e3-4a88-9b41-b92d70ad08ad_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_newscaster_in_tv_studio_looking_at_autocue_-_dffd1482-28e3-4a88-9b41-b92d70ad08ad_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_newscaster_in_tv_studio_looking_at_autocue_-_dffd1482-28e3-4a88-9b41-b92d70ad08ad_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_newscaster_in_tv_studio_looking_at_autocue_-_dffd1482-28e3-4a88-9b41-b92d70ad08ad_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_wearing_a_racing_uniform_driving_a_racing_car_5b82a9f2-5bdd-4fcf-a5bf-ce20defa0bcd_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_wearing_a_racing_uniform_driving_a_racing_car_5b82a9f2-5bdd-4fcf-a5bf-ce20defa0bcd_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_wearing_a_racing_uniform_driving_a_racing_car_5b82a9f2-5bdd-4fcf-a5bf-ce20defa0bcd_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_cat_wearing_a_racing_uniform_driving_a_racing_car_5b82a9f2-5bdd-4fcf-a5bf-ce20defa0bcd_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_film_crew_filming_compact_electric_street_sweeper_5e2b0ac8-ba98-414b-8c0f-60e44b1f150d_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_film_crew_filming_compact_electric_street_sweeper_5e2b0ac8-ba98-414b-8c0f-60e44b1f150d_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_film_crew_filming_compact_electric_street_sweeper_5e2b0ac8-ba98-414b-8c0f-60e44b1f150d_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_film_crew_filming_compact_electric_street_sweeper_5e2b0ac8-ba98-414b-8c0f-60e44b1f150d_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_film_crew_filming_compact_electric_street_sweeper_82b71dd8-1cd1-42b6-a6ea-8e978c4c2ef7_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_film_crew_filming_compact_electric_street_sweeper_82b71dd8-1cd1-42b6-a6ea-8e978c4c2ef7_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_film_crew_filming_compact_electric_street_sweeper_82b71dd8-1cd1-42b6-a6ea-8e978c4c2ef7_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_film_crew_filming_compact_electric_street_sweeper_82b71dd8-1cd1-42b6-a6ea-8e978c4c2ef7_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_full-body_shot_of_a_boxer_looking_at_camera_holdi_dd46cb53-c91b-44a7-a1db-921941475e9a_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_full-body_shot_of_a_boxer_looking_at_camera_holdi_dd46cb53-c91b-44a7-a1db-921941475e9a_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_full-body_shot_of_a_boxer_looking_at_camera_holdi_dd46cb53-c91b-44a7-a1db-921941475e9a_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_full-body_shot_of_a_boxer_looking_at_camera_holdi_dd46cb53-c91b-44a7-a1db-921941475e9a_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_full-body_shot_of_a_normal-looking_man_who_is_als_4afa73ef-794b-4cbb-a094-88c69a7001ea_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_full-body_shot_of_a_normal-looking_man_who_is_als_4afa73ef-794b-4cbb-a094-88c69a7001ea_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_full-body_shot_of_a_normal-looking_man_who_is_als_4afa73ef-794b-4cbb-a094-88c69a7001ea_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_full-body_shot_of_a_normal-looking_man_who_is_als_4afa73ef-794b-4cbb-a094-88c69a7001ea_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_victorian_era_cat_wriding_a_bicycle_-v_6_b130c133-9c26-49ca-9c32-c7a4634661e1_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_victorian_era_cat_wriding_a_bicycle_-v_6_bef4b951-2d82-4eec-a695-9bf3f5d86aa9_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_victorian_era_cat_wriding_a_bicycle_-v_6_bef4b951-2d82-4eec-a695-9bf3f5d86aa9_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_victorian_era_cat_wriding_a_bicycle_-v_6_bef4b951-2d82-4eec-a695-9bf3f5d86aa9_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__665c9c2f-ebf7-4278-a9bf-7effece2b92c_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__665c9c2f-ebf7-4278-a9bf-7effece2b92c_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__665c9c2f-ebf7-4278-a9bf-7effece2b92c_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__665c9c2f-ebf7-4278-a9bf-7effece2b92c_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__9bde78a9-46b3-4ff5-8f4f-9f31153bffbb_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__9bde78a9-46b3-4ff5-8f4f-9f31153bffbb_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__9bde78a9-46b3-4ff5-8f4f-9f31153bffbb_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__9bde78a9-46b3-4ff5-8f4f-9f31153bffbb_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__cf50cfcd-5e7f-4861-abdb-da1120b410b6_0.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__cf50cfcd-5e7f-4861-abdb-da1120b410b6_1.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__cf50cfcd-5e7f-4861-abdb-da1120b410b6_2.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who__cf50cfcd-5e7f-4861-abdb-da1120b410b6_3.png
- https://pearldrop.com/wp-content/uploads/2024/02/simon_23326_whole-body_wide_shot_of_a_normal-looking_man_who_is_5fbd6c4e-c69c-4865-af8f-760b947acddc.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futuriist_steven_spielberg-style_movie_post_28759b4e-1c9b-4c1e-9669-933f65a68820_0.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futuriist_steven_spielberg-style_movie_post_28759b4e-1c9b-4c1e-9669-933f65a68820_1.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futuriist_steven_spielberg-style_movie_post_28759b4e-1c9b-4c1e-9669-933f65a68820_2.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futuriist_steven_spielberg-style_movie_post_28759b4e-1c9b-4c1e-9669-933f65a68820_3.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_64319818-587c-4118-8dc5-ec6b6a30e3b8_0.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_64319818-587c-4118-8dc5-ec6b6a30e3b8_1.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_64319818-587c-4118-8dc5-ec6b6a30e3b8_2.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_64319818-587c-4118-8dc5-ec6b6a30e3b8_3.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_6b99f5ac-0d24-4cc3-9941-2889060d2afa_0.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_6b99f5ac-0d24-4cc3-9941-2889060d2afa_1.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_6b99f5ac-0d24-4cc3-9941-2889060d2afa_2.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_6b99f5ac-0d24-4cc3-9941-2889060d2afa_3.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_a4b0f6f4-da81-4f63-814c-16c5864b5f9f_0.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_1980s_futurist_steven_spielberg-style_movie_poste_a4b0f6f4-da81-4f63-814c-16c5864b5f9f_1.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_a_spectacular_glass_bowl_containing_glass_fruit_o_30679a9b-19b0-427d-9c02-932ebe90d9fe_0.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_a_spectacular_glass_bowl_containing_glass_fruit_o_30679a9b-19b0-427d-9c02-932ebe90d9fe_1.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_a_spectacular_glass_bowl_containing_glass_fruit_o_30679a9b-19b0-427d-9c02-932ebe90d9fe_2.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_a_spectacular_glass_bowl_containing_glass_fruit_o_30679a9b-19b0-427d-9c02-932ebe90d9fe_3.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_mixing_a_cocktail._beautiful_coloured_liquids_fly_0b9e8673-e470-4ecd-b8aa-e392abbe1548_2.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_mixing_a_cocktail._beautiful_coloured_liquids_fly_0b9e8673-e470-4ecd-b8aa-e392abbe1548_3.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_mixing_a_cocktail._beautiful_coloured_liquids_fly_923050b6-eb28-4084-93ed-c38ec087801d_0.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_mixing_a_cocktail._beautiful_coloured_liquids_fly_923050b6-eb28-4084-93ed-c38ec087801d_1.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_mixing_a_cocktail._beautiful_coloured_liquids_fly_923050b6-eb28-4084-93ed-c38ec087801d_2.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_mixing_a_cocktail._beautiful_coloured_liquids_fly_923050b6-eb28-4084-93ed-c38ec087801d_3.png
- https://pearldrop.com/wp-content/uploads/2024/03/simon_23326_mixing_a_cocktail._beautiful_coloured_liquids_fly_o_66a2363d-08f8-458d-a431-f03481e6eae4.png

### /portfolio/photography/architectural-photography-portfolio/

33 images.

- https://pearldrop.com/wp-content/uploads/2023/03/15a-Hoecroft-Nazeing-low-res-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/15a-Hoecroft-Nazeing-low-res-8.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/4-The-Chestnuts-Hertford-low-res-7.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/4-The-Chestnuts-Hertford-low-res.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/6-Sandy-Close-Hertford-low-res-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/6-Sandy-Close-Hertford-low-res.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-1-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-chairs.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-corridor.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Dobsons-18-The-Avenue-Potters-Bar-low-res-11.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Dobsons-18-The-Avenue-Potters-Bar-low-res-9.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Dobsons-West-View-Bengeo-low-res-2-v2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Kitchen-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Museum-of-London-The-Last-Weekend-Day-3-heroes-low-res-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/15a-Hoecroft-Nazeing-low-res-3-q7awrnxtn4gxly5mrar4clyuj6n25i2rft82a87hm0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/15a-Hoecroft-Nazeing-low-res-8-q7awqgp8wqtqrvwfrs2a5wvn7gk6bfb3xv7q7hzlk8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/4-The-Chestnuts-Hertford-low-res-7-q7awsiyhwnne92wkq65t4w524we67ihwk2r34cxhwo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/4-The-Chestnuts-Hertford-low-res-q7awqzi0pfjh8354q06tjs4v35zilddqog9ft17q3s.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/6-Sandy-Close-Hertford-low-res-4-q7awrtkus4onjlxfud6vrkjm3hv9fop5gl4z5vz4ko.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/6-Sandy-Close-Hertford-low-res-q7awrcnrd41hqmm0l5vliotbek6nl4tze9e8iwo7oo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Cospace-1-2-q7awrsn0land7zyszus972s5i3zw7zlf4ghhom0iqw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Cospace-chairs-q7awrejfqs42dujaa6ounoc8lbxe0j1g2ip7hglfc8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Cospace-corridor-q7awrcnrd41hqmm0l5vliotbek6nl4tze9e8iwo7oo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Cospace-lights-q7awsf755bi8yn21c4jaux37rcwpcq2z7k557932lk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Dobsons-18-The-Avenue-Potters-Bar-low-res-11-q7awrejfqs42dujaa6ounoc8lbxe0j1g2ip7hglfc8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Dobsons-18-The-Avenue-Potters-Bar-low-res-9-q7awqa4dkwkqim5zu77w6gjf1rgltjkzkynbuk9crs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Dobsons-West-View-Bengeo-low-res-2-v2-q7awrxc7jgtsu1rz8ete1jlgh1cqah42t3qx2ztjvs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Kitchen-3-q7awras2zfyx3eoqw52cdpae7sfx5qmiq039kcr014.jpg

### /portfolio/photography/automotive-photography-portfolio/

23 images.

- https://pearldrop.com/wp-content/uploads/2023/02/NV200-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Museum-of-London-The-Last-Weekend-Day-3-heroes-low-res-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/NV200-5.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/e-nv200-angles-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/e-nv200-angles-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/e-nv200-angles-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/e-nv200-beauty-.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/e-nv200-beauty-1.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/NV200-3-q7awrya1qav35nqm2x80m1cx2f83i67t58eek9s5pk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/NV200-4-q7awqmca1r1gpjo8uui1kvgerrsdllxhyn4n35r8iw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/NV200-5-q7awqwoi4xfm99986gyxuauhb0deya2jo2azd7bwmg.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/NV200-thumbnail-t-q7awp9go6d6jxtn8s9dfz7sfvqhahcjgfx7e4rrpig.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/e-nv200-angles-1-q81olbg5e0xwb3vnu1syfa0q8gbpiqcqx8yy1bnh0o.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/e-nv200-angles-2-q81ole9nyj1r9xrkdl0u4rb40lxt5tnxxmxeh5jai0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/e-nv200-angles-4-q81oli10pv6wkdm3rmnceqcye5fa0m2va5jce9dpt4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/e-nv200-beauty--q81ollsdh7c1utgn5o9uopesrowqvehsmo5abd8548.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/e-nv200-beauty-1-q81olpjq8jh759b6jpwcyogn58e7q6wpz6r88h2kfc.jpg

### /portfolio/photography/awards-ceremonies-and-conferences-photography-portfolio/

97 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Chamber-team.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-WiL-2023-general-low-res-28.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-WiL-2023-general-low-res-6.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-WiL-2023-presenters-low-res-18.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-WiL-2023-presenters-low-res-34.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-WiL-2023-presenters-low-res-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-WiL-2023-presenters-low-res-61.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-WiL-2023-presenters-low-res-64.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-WiL-2023-presenters-low-res-76.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Inspiring-Herts-Awards-2022-general-44.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Inspiring-Herts-Awards-2022-rushes-8.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Inspiring-Herts-Awards-2022-winners-12.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Inspiring-Herts-Awards-2022-winners-14.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Inspiring-Herts-Awards-2022-winners-23.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Inspiring-Herts-Awards-2022-winners-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Museum-of-London-The-Last-Weekend-Day-3-heroes-low-res-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Pearldrop-live-event-portfolio-conference-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/IHA2023-venue.jpg
- https://pearldrop.com/wp-content/uploads/2024/01/IHA2024-launch-low-res-22.jpg
- https://pearldrop.com/wp-content/uploads/2024/01/IHA2024-launch-others-4.jpg
- https://pearldrop.com/wp-content/uploads/2024/08/IHA24-6.jpg
- https://pearldrop.com/wp-content/uploads/2024/08/IHA24-7.jpg
- https://pearldrop.com/wp-content/uploads/2024/08/IHA24-8.jpg
- https://pearldrop.com/wp-content/uploads/2024/08/IHA24.jpg
- https://pearldrop.com/wp-content/uploads/2024/08/IHA24B2.jpg
- https://pearldrop.com/wp-content/uploads/2024/08/IHA24B3.jpg
- https://pearldrop.com/wp-content/uploads/2024/08/IHA24B4.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-10.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-2.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-31.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-42.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-43.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-48.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-51.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-54.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-56.png
- https://pearldrop.com/wp-content/uploads/2026/01/Biz4Biz-Awards-2025-hero-low-res-7.png
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-panels-low-res-15.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-panels-low-res-20.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-panels-low-res-8-1.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-presenters-low-res-11.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-presenters-low-res-19.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-presenters-low-res-2.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-presenters-low-res-23.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-presenters-low-res-32.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-presenters-low-res-34-1.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/CIC-2025-presenters-low-res-34.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-10-rhd11gf39ieebncvt2cwk6j48innj5mof5jygag4iw.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-2-rhd10b26wsts4t0yikhbigyu3kbi4h2hlgulc45g4o.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-31-rhczivwehrp4ammggh6msy9qp7minqzo9235fzcxrc.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-42-rhcziznr93u9l2gzuit52xbl2r3zijellkp3d37d2g.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-43-rhczj1jfmrwu8ae9jjme7wui9iupxxm29u02bn4kq0.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-48-rhczj4cy7a0p74a632u9xe4w1ogtl0x9a7yirh0e7c.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-51-rhczj84aym5uhk4ph4gs7d6qf7yaftc6mqkgokutig.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-54-rhczj9zzca8f4s1z65a1ccpnlzp0v7jnazvfn4s160.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-56-rhczjbvnpyazrzz8v63ahc8ksrfralr3z96elop8tk.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Biz4Biz-Awards-2025-hero-low-res-7-rhd10sx4ini89eb0ma78bugldvvh6q1dzx8tgdeyug.png
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-panels-low-res-15-rhd2gdcdgg3j79egi2nembzylvpegxr9f5os9uyfhk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-panels-low-res-20-rhd2gh3q7s8ohp8zw49wwb1szf6vbq66roaq6ysuso.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-panels-low-res-8-1-rhd2h7f7j58pis6rmfngu4epm7l5b92o7akbmpptyg.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-presenters-low-res-11-rhd2gmqrcsgefd0sz6pob9mkjqf2lwsksg7n2mkhrc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-presenters-low-res-19-rhd2gomfqgiz2ky2o7ixg95hqi5t1b01gpim16hpew.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-presenters-low-res-2-rhd2gizelgb94x69l5361akq66xlr4dnfxlp5iq2g8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-presenters-low-res-23-rhd2grfyaymu1etz7qqt5qfvinrwoeb8h3h2h0diw8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-presenters-low-res-32-rhd2gtbmompeomr8wrk2apyspfin3sip5cs1fkaqjs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-presenters-low-res-34-1-rhd2u9eigb42rt83e2sxgtt6mv8o7wwgnwr3l2czjc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CIC-2025-presenters-low-res-34-rhd2gw5594t9ngn5gary0796hl4qqvtw5qqhve6k14.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Chamber-team-q7awrovntyi7xk49lt5qx3qb4kifd76hrxvjri63fs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-WiL-2023-general-low-res-28-q7awr39dgromiizo41tbtr6pgpgzg5so0yvdq525ew.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-WiL-2023-general-low-res-6-q7awqrzb6r96n7g1xwxszu16c30kvsjvzf1jytivhk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-WiL-2023-presenters-low-res-18-q7awrfh9xm5cpghx4p3h863p6psr8856encoyqk160.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-WiL-2023-presenters-low-res-34-q7aws4ux2543exh20i2elhp584bo01xxi4ysx7iei0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-WiL-2023-presenters-low-res-4-q7aws7ofmn7ydrcyk1aaayzj09xrn594iix9d1e7zc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-WiL-2023-presenters-low-res-61-q7awsls0h5r97wsh9pdoudffx209ult3kgpjk6tbe0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-WiL-2023-presenters-low-res-64-q7awrdlljy2s28knfoa836krzy20stxpqe1q06mtig.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-WiL-2023-presenters-low-res-76-q7awrpti0sji962wgbkdhlhrpydskwa842j18s4p9k.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA2023-venue-q8e3n6fll081s2nczpk371r20nqftbv5mgp0ut4h60.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA2024-launch-low-res-22-qj1fk0cncvms8jj7fdfvwlk1a1dzupuj6h70ktie3s.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA2024-launch-others-4-qj1fl10crf0ytc1yhbac3ub0g2db6ww2bimyam01d4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA24-6-qs0fwjoqb7l7r1uhiej3v5x2i21mtsd25rfd8oo1d4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA24-7-qs0fwlkeovnse9rr7fcd05fzotsd96kiu0qc78l90o.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA24-8-qs0fwmi8vpp2pvqe1xqzkn7ga7nqgvo965dtoijuug.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA24-qs0fwpbrg7sxopmalgyva4hu2d9u3yzg6jca4cfobs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA24B2-qs0fwt347jy2z5gtzildk3jofwrayredj1y81ga3mw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA24B3-qs0fwu0yedzdarfgu1004lb51amo6gi3v6lpiq8pgo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/IHA24B4-qs0fwvwms21xxzcqj1t99ku282delupkjfwoha5x48.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Inspiring-Herts-Awards-2022-general-44-q7awsnnoutttv4pqyq6xzcyd3tr0a00k8q0iiqqj1k.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Inspiring-Herts-Awards-2022-rushes-8-q7aws9k40baj0za8923jfyig71oi2jgl6s88blbfmw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Inspiring-Herts-Awards-2022-winners-12-q7awq4hcfwd0kye6r4s4rhynhg8ejcylk6qeywhpt4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Inspiring-Herts-Awards-2022-winners-14-q7awriasi497oadto8bcxne2yveuvbgdf1b5ekfunc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Inspiring-Herts-Awards-2022-winners-4-q7awqc01yknb5u39j815bg2c8j7c8xsg97yat46kfc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Inspiring-Herts-Case-Study-thumb-2-q7awqkglo2yw2bqz5tosfvxhl01n67q1adto4lu0vc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Pearldrop-live-event-portfolio-conference-2-q7awqo7yff41crlijvbapuzbyjj4104ymwfm1pog6g.jpg

### /portfolio/photography/clients/

10 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Museum-of-London-The-Last-Weekend-Day-3-heroes-low-res-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Herts-Chamebr-Golf-Day-2023-hero-low-res-18.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Summer-party-thumbnail.jpg
- https://pearldrop.com/wp-content/uploads/2024/01/IHA2024-launch-others-4.jpg
- https://pearldrop.com/wp-content/uploads/2024/03/HCCI-WiL-2024-speakers-75.jpg
- https://pearldrop.com/wp-content/uploads/2024/07/Summer-party-games-7.jpg

### /portfolio/photography/hcci-golf-day-2023/

6 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-9.jpg

### /portfolio/photography/hcci-summer-party-2023/

6 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-9.jpg

### /portfolio/photography/hcci-summer-party-2024/

6 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2024/03/HCCI-WiL-2024-speakers-75.jpg

### /portfolio/photography/hcci-women-in-leadership-conference-2024/

6 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2024/03/HCCI-WiL-2024-speakers-75.jpg

### /portfolio/photography/headshot-photography-portfolio/

38 images.

- https://pearldrop.com/wp-content/uploads/2023/02/Crew-composite-1-for-web-v4.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Denise-headshot-square-1-t2.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/James-headshot-square-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Katie-headshot-square-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Rob-headshot-square-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Simon-headshot-square-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Amthal.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Chamber-Alison.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Chamber-Amy.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Dobsons-Helen.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Dobsons-Tasha.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Georgia-headshot-square-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCCI-headshot-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Museum-of-London-The-Last-Weekend-Day-3-heroes-low-res-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/OPES-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/OPES-Dani.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Marlo-laughing.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Marlo-on-stool.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Amthal-q7awrxc7jgtsu1rz8ete1jlgh1cqah42t3qx2ztjvs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Chamber-Alison-q7awr8welrwcg6rh74938prh10p6qcf21qsalstsdk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Chamber-Amy-q7aws05q3yxnsvnvry19r0vu96ytxkf9thpditpdd4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Denise-headshot-square-1-t2-q7awprbls7v02exavz3csla76219jlicudlm911888.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Dobsons-Helen-q7awr39dgromiizo41tbtr6pgpgzg5so0yvdq525ew.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Dobsons-Tasha-q7awriasi497oadto8bcxne2yveuvbgdf1b5ekfunc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Georgia-headshot-square-1-t-q7awr39dgromiizo41tbtr6pgpgzg5so0yvdq525ew.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCCI-headshot-2-q7awr39dgromiizo41tbtr6pgpgzg5so0yvdq525ew.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/James-headshot-square-1-t-q7awq1ntve95m4ia7lk920o9pamaw9nejsryj2lwbs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Katie-headshot-square-1-t-q7awpd80xpbp89hs6azy96ua99yrc4ydsftc1vm4tk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Marlo-laughing-q7ngahsa7q3tax3yz1d8m9dwjunnm3md9qukql0e7c.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Marlo-on-stool-q7ngaiq4ek53mj2ltjrv6r5d58j0tsq3lvi27uz014.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/OPES-2-q7awqzi0pfjh8354q06tjs4v35zilddqog9ft17q3s.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/OPES-Dani-q7awqb27rqm0u84mopmiqyavn5bz18opx3atbu7ylk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Rob-headshot-square-1-t-q7awpd80xpbp89hs6azy96ua99yrc4ydsftc1vm4tk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Simon-headshot-square-1-t-q7awpw0sqe1fogqh4j4hn23i4ze3m310j0v1neu9d4.jpg

### /portfolio/photography/inspiring-herts-awards-2024-launch/

6 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-9.jpg

### /portfolio/photography/lifestyle-photography-portolio/

111 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Capita-100pc-Tablets-low-res-8.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Denise.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Gem-Cable-clean-room-day-1-low-res-64.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Gem-Cable-clean-room-day-1-low-res-8.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-Bus-overview-portraits-low-res-6.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-Daisy-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-getting-on.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-offices-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HHH-Day-1-general-low-res-33.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HHH-Day-1-general-low-res-42.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HHH-Day-1-general-low-res-79.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HHH-Day-1-general-low-res-92.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Health-walk-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Health-walk-3-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Health-walk-5-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Museum-of-London-The-Last-Weekend-Day-3-heroes-low-res-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Timetable.-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Training.-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Wagada-boardroom-19.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Wagada-boardroom-48.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Wagada-general-offie-51.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Walker.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/CAE-having-fun.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/CAE-looking-at-PC-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/CAE-looking-at-PC-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/CAE-looking-at-PC-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/CAE-staircase-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/CAE-staircase-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/CAE-staircase-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Bears-at-the-gym.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Bears-blowing-out-candle.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Bears-in-cafe.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Bears-in-cinema.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-2023-Priory-School-low-res-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-2023-Priory-School-low-res-5.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-2023-Priory-School-low-res-7.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-Farnham-House-Breakout-space-low-res-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-Farnham-House-Meeting-in-cafeteria-high-res-10.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-Farnham-House-Meeting-in-cafeteria-high-res-17.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-Farnham-House-Walking-low-res-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-Occupational-Therapy-low-res-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-rebrand-grass-cutting-low-res-29.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-rebrand-sludge-gulper-low-res-35.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-spring-2023-potholes-Richard-low-res-59.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-spring-2023-potholes-Richard-low-res-64.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-spring-2023-potholes-Richard-low-res-83.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-spring-2023-potholes-low-res-13.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/HCC-spring-2023-potholes-low-res-83.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Steve-2-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Steve-3.jpg
- https://pearldrop.com/wp-content/uploads/2024/02/Cycleway1.jpg
- https://pearldrop.com/wp-content/uploads/2024/02/Cycleway2.jpg
- https://pearldrop.com/wp-content/uploads/2024/02/Cycleway3.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Bears-at-the-gym-qguqrxdejil5m5akhf6bgf10sm8i1uzl7xkague9d4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Bears-blowing-out-candle-qguqs06x40p0kz6h0ye75wbekruloyas8biqwoa2ug.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Bears-in-cafe-qguqs22lhorl873qpz7gavubrjlc4ci8wktpv87ai0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Bears-in-cinema-qguqs4w426vg70zn9ifc0d4pjp7frftfwys6b233zc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CAE-having-fun-q8tnvrs0kxi8umn4kp0ywkoj4zb209s4jqai6gy7zc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CAE-looking-at-PC-1-q8tnvtnoylkthuke9pu81k7gbr1sfnzl7zlh50vfmw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CAE-looking-at-PC-2-q8tnvxf1pxpysaexnrgqbj9apaj9ageiki7f24puy0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CAE-looking-at-PC-3-q8tnw08kafttr4au7aom10johg5cxjppkw5vhylofc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CAE-staircase-1-q8tnw322uxxopy6qqtwhqhu29lrgkn0wla4bxshhwo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CAE-staircase-2-q8tnw5vlfg1jos2nad4dfz4g1rdk7qc3lo2sdmdbe0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/CAE-staircase-3-q8tnw7r9t444bzzwzdxmkynd8j4an4jk9xdrc6aj1k.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Capita-100pc-Tablets-low-res-8-q7awse9ayhgyn13ehm4oafbr5z1c50z8vfhnpz4grs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Cycleway1-qjdclsk1h1quw9o5wec51eq8hd3621jd40a6l9w6aw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Cycleway2-qjdclthvnvs57vmsqwqrlwhp2qyj9qn3g4xo2jus4o.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Cycleway3-qjdclufpuptfjhlflf5e6e95o4twhfqts9l5jttdyg.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Denise-q7awrz7vx4wdh9p8xfmn6j4dnt3gpvbjhd1w1jqrjc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Gem-Cable-clean-room-day-1-low-res-64-q7awsf755bi8yn21c4jaux37rcwpcq2z7k557932lk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Gem-Cable-clean-room-day-1-low-res-8-q7awqetkj2r64nz62r910xcq0otfw13n9lwr8y2dwo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-2023-Priory-School-low-res-4-qguphchbv2tm9sychabvw66p17tolu2g5dq2b7glpk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-2023-Priory-School-low-res-5-qguphfaufkxh8mu90tjrlnh2tdfs8xdn5roir1cf6w.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-2023-Priory-School-low-res-7-qguphi4d031c7gq5kcrnb4rglj1vw0ou65mz6v88o8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-Bus-overview-portraits-low-res-6-q7awq5f6mqeawkctln6rbzq42u3rr22bwbdwg6gbmw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-Farnham-House-Breakout-space-low-res-4-qgupgydr0kabfnitrm8hcrqs4fr6edih3fxs421iaw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-Farnham-House-Meeting-in-cafeteria-high-res-10-qguph179l2e6eheqb5gd2915wlda1gto3tw8jvxbs8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-Farnham-House-Meeting-in-cafeteria-high-res-17-qguph32xyqgr1pc0069m78k33d40gv14s377ifujfs.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-Farnham-House-Walking-low-res-3-qguph6uaq2lwc56je7w4h7lxgwlhbng24lt5fjoyqw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-Occupational-Therapy-low-res-3-qguph9ntakpraz2fxr406owb927kyqr94zrlvdks88.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-buses-1-t-q7awsi0nptm3xgxxvnr6kedljiiszte67y3ln2yw2w.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-buses-Daisy-2-q7awqxmcbrgwkv7v0zdkeslxwe8s5z6a06yguhaig8.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-buses-getting-on-q7awr2bj9xnc6x119jep99f8vblm8goxou7w8v3jl4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-offices-t-q7awr2bj9xnc6x119jep99f8vblm8goxou7w8v3jl4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-rebrand-grass-cutting-low-res-29-qguphkxvkl576am23vzj0m1udonzj4016jlfmp425k.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-rebrand-sludge-gulper-low-res-35-qguphnre539254hynf7eq3c85ua367b86xjw2izvmw.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-spring-2023-potholes-Richard-low-res-59-qguphx5s1flxd84b4j9of0yu3ozrb6cjk82qvalxwo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-spring-2023-potholes-Richard-low-res-64-qguphzzalxpsc207o2hk4i97vuluy9nqkm17b4hre0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-spring-2023-potholes-Richard-low-res-83-qgupi2st6ftnavw47lpftzjlo07ylcyxkzznqydkvc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-spring-2023-potholes-low-res-13-qguphqkwplcx3ydv6yfafkmlxzw6tamf7bicicvp48.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HCC-spring-2023-potholes-low-res-83-qguphtefa3gs2s9rqhn651wzq5iagdxm7pgsy6rilk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HHH-Day-1-general-low-res-33-q7awqq3mt36lzzis8w4juui95b9ugecfb5ql09lnu0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HHH-Day-1-general-low-res-42-q7awqcxw5eolhg1wdqfrvxtstx2pgmw6lclsae5694.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HHH-Day-1-general-low-res-79-q7awsnnoutttv4pqyq6xzcyd3tr0a00k8q0iiqqj1k.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/HHH-Day-1-general-low-res-92-q7awr0fuw9krjp3rkilg49wbojuvt2hh0kwxab6bxk.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Health-walk-1-t-q7awq6d0tkfl86bgg5ldwhhko7z4yr628g1dxgexgo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Health-walk-3-t-q7awsiyhwnne92wkq65t4w524we67ihwk2r34cxhwo.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Health-walk-5-t-q7awqtuzkfbrafdbmxr24tk3iurbb6rcnocixdg354.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Steve-2-1-qh1twu4yqa1c9dp625dqj4y168ze3bg110lo7du6eg.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Steve-3-qh1twhx29fkm2g6x1i3l4q11g8nmb93inc4cyscanc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Timetable.-t-q7awsmpunzsjjir447sbev6wifvn2awtwld11grx7s.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Training.-t-q7awqsx5dlagyteosfcfkbsmxgvy3hnmbjp1g3hhbc.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Wagada-boardroom-19-q7awrfh9xm5cpghx4p3h863p6psr8856encoyqk160.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Wagada-boardroom-48-q7awqyk6ili6wh6hvhs6zadehs45doa0cblybr94a0.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Wagada-general-offie-51-q7aws8m9th98pdblejowvgqzlnt4uucuunkqubctt4.jpg
- https://pearldrop.com/wp-content/uploads/elementor/thumbs/Walker-q7awrmzzgafnac6zwschs47dxsroxsz13okksy8vs8.jpg

### /portfolio/photography/live-event-photography-portfolio/

29 images.

- https://pearldrop.com/wp-content/uploads/2023/03/A-Match-for-Hugh-match-low-res-96.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Amthal-Away-Day-July-2022-20.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Awards-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/FIAS-QinetiQ-Best-of-low-res-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/FIAS-QinetiQ-Best-of-low-res-9.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HCC-buses-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Headshots-carousel.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Pearldrop-live-event-portfolio-golf-day-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/06/Automotive-gallery-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-10.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-4.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-5.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-6.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-7-scaled.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-7.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-8-scaled.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-8.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-9.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/HCCI-Summer-Party-2023-venue-low-res-59.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Herts-Chamebr-Golf-Day-2023-hero-low-res-30-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Herts-Chamebr-Golf-Day-2023-hero-low-res-52-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Herts-Chamebr-Golf-Day-2023-hero-low-res-52.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Herts-Chamebr-Golf-Day-2023-hero-low-res-61-scaled.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Herts-Chamebr-Golf-Day-2023-hero-low-res-61.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/Herts-Chamebr-Golf-Day-2023-hero-low-res-8-1.jpg

### /portfolio/plx-awards-2025-tender-submission/

1 images.

- https://pearldrop.com/wp-content/uploads/2024/03/HCCI-WiL-2024-speakers-75.jpg

### /portfolio/video/

1 images.

- https://pearldrop.com/wp-content/uploads/2023/03/Easybuild.jpg

### /portfolio/video/2d-animation/

17 images.

- https://pearldrop.com/wp-content/uploads/2023/03/CA-East-Herts.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/CA-Harlow-thumbnaill-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Covid-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Easybuild.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/HOP.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Lisa.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Meet-the-rainbow.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Orange-feels-worried.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/T-levels.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/World-Communication.jpg
- https://pearldrop.com/wp-content/uploads/2023/04/2D-animation-example-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Beths-story-1.jpg
- https://pearldrop.com/wp-content/uploads/2024/02/2D-animation-portfolio-thumb-2a.jpg
- https://pearldrop.com/wp-content/uploads/2025/02/1YMCA.jpg
- https://pearldrop.com/wp-content/uploads/2025/02/HCC-buses.jpg
- https://pearldrop.com/wp-content/uploads/2025/02/Nordic-Dry.jpg
- https://pearldrop.com/wp-content/uploads/2026/01/1YMCA-Abuse.png

### /portfolio/video/live-action/

45 images.

- https://pearldrop.com/wp-content/uploads/2023/02/Company-profile-thumnbail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Fuelstat-Result-App-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Healthy-Mind-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Lost-Mountain-1-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/Museum-of-London-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/NV200-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/02/QinetiQ-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Blesma-thumbnail.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Bob-awards.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Conidia-thumbnail-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Cospace-lights.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/ENNHC-thumbnail.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/FIAS-QinetiQ-Best-of-low-res-3.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Fareshare-thumbnail.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Gentlemen-Baristas-thumbnail-t-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Golf.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Herts-County-Show-thumbnail.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Holistic-Herb-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/IcelandAir-thumbnail-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Inspiring-Herts-Awards-2022-winners-23.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/LSIP.-t.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Royston-First.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Studio-cambridge-thumbnail.jpg
- https://pearldrop.com/wp-content/uploads/2023/03/Women-in-leadership-thumbnail-2.jpg
- https://pearldrop.com/wp-content/uploads/2023/04/Meet-James.jpg
- https://pearldrop.com/wp-content/uploads/2023/05/Interlink-film-YouTube-thumbnail.jpg
- https://pearldrop.com/wp-content/uploads/2023/07/NHC1.jpg
- https://pearldrop.com/wp-content/uploads/2023/11/Orfium.jpg
- https://pearldrop.com/wp-content/uploads/2023/11/Snaresbrook-thumb.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Burgers.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/GP-Christmas-thumbnail-1.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Lussman.jpg
- https://pearldrop.com/wp-content/uploads/2023/12/Marlo-1.jpg
- https://pearldrop.com/wp-content/uploads/2024/01/Flackwell-Heath-card-3.jpg
- https://pearldrop.com/wp-content/uploads/2024/06/NHC-film-course-1.jpg
- https://pearldrop.com/wp-content/uploads/2024/09/Live-event-thumnbail-1.jpeg
- https://pearldrop.com/wp-content/uploads/2025/02/Fareshare-Guildford.jpg
- https://pearldrop.com/wp-content/uploads/2025/02/GP-monster.jpg
- https://pearldrop.com/wp-content/uploads/2025/02/GP-race.jpg
- https://pearldrop.com/wp-content/uploads/2025/06/Animal-Free-Research.jpg
- https://pearldrop.com/wp-content/uploads/2025/09/LSBU.png
- https://pearldrop.com/wp-content/uploads/2026/01/GP-xmas-campaign-2025.png
- https://pearldrop.com/wp-content/uploads/2026/01/Lokkelebury-Vineyard.png
- https://pearldrop.com/wp-content/uploads/2026/01/Prof-Ma.png
- https://pearldrop.com/wp-content/uploads/2026/01/biz4Biz-Awards-2025.png

---

## 8. Clients

`/about-us/our-clients/` groups client logos under three headings. Logos carry no
alt text, so these names come from the image filenames and the outbound links.

### Companies (48)

- **1E** — <https://www.1e.com>
- **altium vector logo optimised** — <https://altium.com/>
- **Amazing apprenticeships** — <https://amazingapprenticeships.com/>
- **B3 Living** — <https://www.b3living.org.uk/>
- **Bedfordshire NHS** — <https://www.bedfordshirehospitals.nhs.uk/>
- **Blackbridge Distillery** — <https://blackbridgedistillery.co.uk/>
- **Boldmere Academy** — <https://www.bmet.ac.uk/course/boldmere-st-michaels-fc-football-academy/>
- **Bulletprood** — <https://www.bulletproof.co.uk>
- **CAE** — <https://www.thisiscae.com/>
- **Capita 2** — <https://www.capita.com/>
- **Citizencard** — <https://www.citizencard.com/>
- **Fuelstat** — <https://conidia.com/>
- **Cranfield** — <https://www.cranfield.ac.uk/>
- **Crimson** — <https://www.crimson.co.uk/>
- **Croft** — <https://www.croftcommunications.co.uk/>
- **DLLpng** — <https://www.dllgroup.com/en>
- **Dobsons** — <https://dobsonshome.com>
- **East and North Herts NHS** — <https://www.enherts-tr.nhs.uk/>
- **Elsevier 2** — <https://www.elsevier.com/en-gb>
- **Estu** — <https://www.estuglobal.com/>
- **Eurosite power** — <https://www.eurositepower.co.uk>
- **Exemplas** — <https://www.exemplas.com/>
- **Gem Cable** — <https://www.gemcable.co.uk>
- **HertsChamber Logo 1** — <https://www.hertschamber.com/>
- **Herts County Show** — <https://hertsshow.com/>
- **Helical Former** — <https://www.helicalformer.com>
- **Inverclyde Leisure** — <https://www.inverclydeleisure.com/>
- **Kaizo** — <https://kaizo.co.uk/>
- **Kit and Caboodle** — <https://www.kitandcaboodle.co.uk/>
- **London Luton** — <https://www.airport-luton.com/>
- **London Stansted** — <https://amazingapprenticeshhttps://www.stanstedairport.comips.com/>
- **Museum of London** — <https://www.museumoflondon.org.uk/>
- **Network Homes** — <https://www.networkhomes.org.uk/>
- **Notintheguidebooks** — <https://www.notintheguidebooks.com/>
- **Novogene** — <https://www.novogene.com/eu-en>
- **Oxonoxpng** — <https://oxonox.com/>
- **Pitney Bowes** — <https://www.pitneybowes.com/uk>
- **QinetiQ** — <https://www.qinetiq.com/en/>
- **Server Choice** — <https://www.serverchoice.com/>
- **Sherrards logo navy transparent2182334.1** — <https://sherrards.com/>
- **Snaresbrook Prep** — <https://snaresbrookprep.org/>
- **St George NHS** — <https://www.stgeorges.nhs.uk/>
- **StressballsUK** — <https://www.stressballsuk.com/>
- **Studio Cambridge** — <https://www.studiocambridge.co.uk/>
- **Vanarama** — <https://www.vanarama.com>
- **Viavi Logo** — <https://www.viavisolutions.com/en-uk>
- **WOW** — <https://www.thewowawards.co.uk/>
- **Wagada** — <https://www.wagada.co.uk>

### Government Bodies (10)

- **Ambition Broxbourne** — <https://www.broxbourne.gov.uk/business>
- **Borough of Broxbourne** — <https://www.broxbourne.gov.uk>
- **Dacorum 1** — <https://www.dacorum.gov.uk/>
- **DIT** — <https://www.gov.uk/government/organisations/department-for-international-trade>
- **Herts County Council** — <https://www.altium.comhttps://www.hertfordshire.gov.uk/home.aspx>
- **Herts LEP** — <https://www.hertfordshirelep.com/>
- **Hertsmere 1** — <https://www.hertsmere.gov.uk/home.aspx>
- **St Albans Council** — <https://www.stalbans.gov.uk/>
- **Stevenage Borough Council** — <https://www.stevenage.gov.uk/>
- **Welwyn Hatfield** — <https://www.welhat.gov.uk/>

### Charities (12)

- **Age UK Hertfordshire** — <https://www.ageuk.org.uk/hertfordshire/>
- **Blesma** — <https://blesma.org/>
- **CA East Herts 2** — <https://citizensadviceeastherts.org.uk/>
- **CA Harlow** — *(no link)*
- **Crohns and Colitis UK** — <https://crohnsandcolitis.org.uk>
- **CVSBEH** — <https://cvsbeh.org.uk/>
- **EMMAUS** — <https://emmaus.org.uk/hertfordshire/>
- **Fareshare** — <https://emmaus.org.uk/hertfordshire/>
- **Muscle Help** — <https://www.musclehelp.com/>
- **Rennie Grove** — <https://renniegrove.org/>
- **Soldiering On** — <https://soldieringon.org>
- **Troopaid** — <https://troopaid.info/>

Named in prose on `/about-us/meet-pearldrop/` as relationships worth calling out:
**Johnson & Johnson, QinetiQ, Elsevier, Thomas Pink, Amazing Apprenticeships**, plus
local government bodies and the **Department for Education**.

The homepage logo carousel runs: **Capita, Fareshare, St John's College Cambridge,
University of Hertfordshire, TEDx St Albans, QinetiQ, 1YMCA**.

> Two client links are broken in the live markup: London Stansted
> (`https://amazingapprenticeshhttps://www.stanstedairport.comips.com/`) and
> Hertfordshire County Council
> (`https://www.altium.comhttps://www.hertfordshire.gov.uk/home.aspx`) — both are
> two URLs concatenated. Citizens Advice Harlow has no link at all, and Fareshare
> points at the Emmaus URL.

---

## 9. Testimonials

`/about-us/testimonials/` carries 21 written reviews, each marked "Rated 5 out of 5".
The page states Pearldrop is five-star rated on **Google** and **Bark.com**, and
features a video testimonial from **Hannah at Lokkelbery Vineyard**, winner of the
2024 Lord Lieutenant of Hertfordshire's Entrepreneurs' Challenge.

Full quotes are in [about-us-testimonials.md](about-us-testimonials.md). Attributions:

| # | Attributed to | Organisation |
| --- | --- | --- |
| 1 | Creative Team | St John's College Cambridge May Ball |
| 2 | Callum Huthwaite | Scarab Sweepers |
| 3 | Heather Almond | North Hertfordshire College |
| 4 | Sian Teasdale | Kit and Caboodle |
| 5 | Ellie Weston | Fareshare |
| 6 | Jesse Eyoma | Hertfordshire County Council |
| 7 | Philippa Davis | Helical Former |
| 8 | Simon Littlewood | Estu Global Ltd |
| 9 | Sarah Castleman | Hertfordshire Chamber of Commerce |
| 10 | Colette Cooper | Cariad Marketing |
| 11 | Marcus Hoare | STM Marketing |
| 12 | Helen Dobson | Dobsons Kitchen and Bathroom |
| 13 | Sophie Hudson | Sherrards |
| 14 | Jamie Allam | Amthal Fire and Security |
| 15 | Nick Silverstone | Wagada |
| 16 | Courtney Black | Luton and Dunstable University Hospital |
| 17 | Emma Fisher | St Albans District Chamber of Commerce |
| 18 | Hayley Sherwood | 1Decision Ltd |
| 19 | Lucy Gravatt | Hertfordshire Local Enterprise Partnership |
| 20 | Mark Hanna | Age UK Hertfordshire |
| 21 | Sarah Moreland | Hertfordshire County Show |

---

## 10. Accreditations and memberships

From `/about-us/memberships/`:

- **JOSCAR accredited** — the Joint Supply Chain Accreditation Register, used by prime
  contractors in aerospace, defence and security. Pearldrop is fully JOSCAR-accredited.
- **Patrons of the Hertfordshire Chamber of Commerce** — active in the Hertfordshire
  Chamber of Commerce and Industry since 2010, Patrons since 2012, and supplier of all
  their video and photographic content since.
- **Civil Aviation Authority — Unmanned Aircraft Operational Authorisation, Specific
  Category UKPDRA-01** — Director Simon Mercer has flown drones since 2014 and gained
  CAA commercial accreditation in 2016; described as one of the more wide-ranging
  authorisations, certified to fly where many other licence-holders cannot.
  (Live page has a typo: "Specifc Category".)
- **Wenta Net Zero accreditation scheme** — on the Net Zero journey, currently working
  toward Gold.
- **St Albans District Chamber of Commerce** — members since 2010 and principal supplier
  of video content; have filmed every awards ceremony held since.

---

## 11. Company facts worth keeping

- Founded **January 2003** by **Simon Mercer**, current Managing Director.
- Pivoted to the corporate sector in **2009**.
- Studio: **Stevenage Arts & Leisure Centre, Lytton Way, Stevenage, Hertfordshire, SG1 1LZ**
  — greenscreen studio plus a white infinity cove for headshots.
- **info@pearldrop.com** / **+44 (0)20 3286 3852**
- Socials: LinkedIn (`company/983998`), YouTube (`UC3pdcH9qROC88IkkBaAwvlw`),
  Twitter/X (`@pearldropvideo`), Facebook (`Pearldropvideo`), Instagram (`@pearldropvideo`).
- Team as listed on `/about-us/meet-pearldrop/`:
  - **Denise Austin** — Co-founder and Director
  - **Simon Mercer** — Co-founder and Director
  - **Rob Evans** — Production Manager
  - **Katie Mackenzie** — Senior Production Executive
  - **Tom Fuller** — Animator
- Open roles under `/about-us/employment/`: **Junior Editor and Animator**, **Production Executive**.

---

## 12. Notes on tone

**Overall: warm, plain-spoken British corporate — confident without being slick,
and noticeably friendlier than most production-company copy.**

What is consistent across the site:

- **First person plural throughout.** "We create", "we'd love to hear from you",
  "We love making videos, and we hope we can make yours soon!" The company talks as a
  team of people, never as an abstract brand.
- **Short declarative fragments as taglines.** The service cards are lists of nouns —
  *"Interviews. Case studies. Awards ceremonies. Products. Training."* — which reads
  fast and scans well. This is the most distinctive device in the copy.
- **Direct second person, low pressure.** "Harness the amazing power of video for your
  business." Calls to action are mild and conversational: "Find out more", "See our
  portfolio", "Ready to start our next chapter?", "Let's create something extraordinary
  together!"
- **British English and British specifics** — "-ise" spellings, "programme", and heavy,
  deliberate use of Hertfordshire/St Albans/Stevenage local identity as a credibility signal.
- **Playful where it can afford to be.** The blog is where the personality is loudest:
  a "Film-term Friday" series with one-word titles (*Dolly*, *Cheeseplate*, *Logline*,
  *Golden Hour*, *Woof!*, *Alan Smithee*), emoji in post titles, and headlines like
  *"Your Team's Headshots Are Boring"* and *"Great Gatsby on a Shoestring"*. Marketing
  pages stay straighter than the blog.
- **Credibility by specificity.** Named clients, named accreditations, five-star ratings,
  real numbers, real people with LinkedIn links. Very little vague superlative.

Where the tone slips, and worth watching in a rewrite:

- Several mid-level pages (the Sectors and Portfolio intros in particular) drift into
  generic AI-ish agency filler — *"diversity is at the heart of everything we do"*,
  *"seamlessly navigates the unique needs and nuances of each sector"*,
  *"resonate with audiences"*, *"exceeds expectations"*. These read markedly blander
  than the homepage and the Meet Pearldrop story, which are genuinely good.
- Capitalisation is inconsistent: service cards render lowercase ("live-action",
  "2d animation") while headings elsewhere use title case, and one accreditation
  heading is full caps ("CIVIL AVIATION AUTHORITY").
- The strongest writing on the site is the founding story on `/about-us/meet-pearldrop/`
  — concrete, a bit self-deprecating, with real detail (Joan Rivers, Graham Norton,
  "corporate video was really just the chief executive of the company droning on in
  front of the camera"). That is the voice the rest of the site should be levelled up to.

---

## 13. Capture method

- URL discovery: `sitemap_index.xml` → four child sitemaps; then an internal link crawl
  over all 116 fetched pages to confirm nothing was missing.
- Fetched over plain HTTPS, no JavaScript execution. Content that only appears after a
  client-side fetch would not be captured; nothing on this site appeared to need it,
  but the Elementor galleries were read from the markup rather than the rendered DOM.
- Per-page markdown: header, footer, nav, popups, cookie banner, scripts and styles
  stripped; the remainder converted to markdown preserving headings, lists, links and
  image sources.
- Each file opens with the full URL, the slug, the `<title>`, the `<h1>` and the meta
  description.
