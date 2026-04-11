# RamayanaPath - Project Guide

## Project Overview

- **Site**: <https://ramayanpath.com> (Vercel auto-deploy on push to master)
- **Repo**: github.com/pawanprakashpal/RamayanaPath (PUBLIC)
- **Stack**: Next.js 16 (App Router), TypeScript, Tailwind CSS
- **Purpose**: Read the Ramayana with original verses, Hindi meanings, and English translations

## Content Status

### Tulsidas Ramcharitmanas — 6,072 verses, 100% translated

| Kand | Groups | Verses | Shlokas (group 0) | English | Hindi |
|------|--------|--------|-------------------|---------|-------|
| Bal Kand | 362 | 1,951 | 7 | 100% | 100% |
| Ayodhya Kand | 327 | 1,622 | 3 | 100% | 100% |
| Aranya Kand | 47 | 326 | 2 | 100% | 100% |
| Kishkindha Kand | 31 | 190 | 1 | 100% | 100% |
| Sundar Kand | 61 | 343 | 3 | 100% | 100% |
| Lanka Kand | 122 | 785 | 3 | 100% | 100% |
| Uttar Kand | 131 | 855 | 3 | 100% | 100% |

### Valmiki Ramayana — 20,214 shlokas, ALL COMPLETE

- 6 Kandas from IIT Kanpur (Sanskrit + English)
- 1 Kanda (Uttara) from WisdomLib (English only)

## QA Completed (April 2026)

- Split 136 combined dohas (ka/kha/ga/gha) into individual verses
- Split 29 combined chhands into proper 4-line verses
- Added Hanuman Vandana shloka to Sundar Kand
- Added mangalacharan opening shlokas to all 7 Kands (group 0)
- Fixed 695 Ayodhya Kand verses (dohas 187-326) with proper Hindi meanings
- Security audit: rate limiting, security headers, npm vulnerabilities fixed

## Features Implemented

- **TTS Audio**: Azure Neural voices (hi-IN-MadhurNeural, en-US-Andrew) with browser TTS fallback
- **Language toggle**: Original / Hindi / English for TTS playback
- **Play All**: Sequential verse playback with auto-scroll and active verse highlight (pulse)
- **Share button**: WhatsApp, X/Twitter, Copy Link (native share on mobile)
- **Keyboard navigation**: ← → arrow keys for prev/next doha
- **Reading progress**: Saves last-read doha per Kand in localStorage, "Continue Reading" button
- **SEO**: Sitemap, robots.txt, OG image, JSON-LD (WebSite + BreadcrumbList + CreativeWork), canonical URLs
- **Google Search Console**: Verified, sitemap submitted
- **About page**: /about with mission, sources, verse table
- **Animations**: Hero entrance, staggered cards, verse hover, details expand, TTS pulse
- **Security**: Rate limiting (20 req/min/IP on TTS), security headers, SSML escaping
- **PWA**: manifest.json, icons, installable

## Remaining TODO

### 1. Soratha Identification (IN PROGRESS — 79% done)

62 sorathas identified from Gita Press text across all 7 Kands:

- Bal Kand: 23, Ayodhya: 11, Aranya: 6, Kishkindha: 1, Sundar: 2, Lanka: 5, Uttar: 13
- **Done**: 49 sorathas retyped from "doha" to "soratha" (84 individual verses)
- **Remaining**: 13 sorathas missing from JSON data entirely (need source Devanagari text):
  - Ayodhya Kand: dohas 25, 100, 126, 151, 176, 201, 251, 276, 301, 326 (10 missing)
  - Aranya Kand: 1 unnumbered soratha after doha 21 ("mukti janma mahi jani")
  - Sundar/Lanka boundary: 1 unnumbered ("sindhu bacana suni")
  - Ayodhya conclusion: 1 unnumbered ("uma rama guna guRha")
- **Gita Press digital**: https://archive.org/details/RamcharitmanasGitapressEnglish (full text available as djvu.txt)
- **Reference PDF**: ~/Downloads/Sunderkand-Gitapress-Gorakhpur.pdf (Sundar Kand only)

### 2. Valmiki Content Expansion (future)

- Currently complete but could add Hindi translations for Valmiki shlokas

## Environment Variables

```
AZURE_SPEECH_KEY=<Azure Speech Services key>    # .env (gitignored)
AZURE_SPEECH_REGION=centralindia                 # .env (gitignored)
```

Also set on Vercel → Settings → Environment Variables.

- Azure F0 free tier: 500K chars/month, never charges, falls back to browser TTS when exhausted

## Key Files

- **Data**: `data/tulsidas/{kand-name}.json`, `data/valmiki/{kanda-name}/sarga-{NN}.json`
- **Manifest**: `data/kands.json`
- **Types**: `src/types/verse.ts`, `src/types/kand.ts`, `src/types/common.ts`
- **Data lib**: `src/lib/data.ts`
- **Constants**: `src/lib/constants.ts`
- **Layout**: `src/app/layout.tsx` (root metadata, JSON-LD WebSite, Google verification)
- **Home**: `src/app/page.tsx`
- **About**: `src/app/about/page.tsx`
- **Doha page**: `src/app/[kand]/doha/[number]/page.tsx` (TTS, share, keyboard nav, JSON-LD)
- **Kand page**: `src/app/[kand]/page.tsx` (continue reading)
- **Sarga page**: `src/app/[kand]/sarga/[number]/page.tsx`
- **TTS API**: `src/app/api/tts/route.ts` (Azure + rate limiter)
- **TTS Provider**: `src/components/verse/TtsProvider.tsx` (Azure → browser fallback)
- **TTS Controls**: `src/components/verse/TtsControls.tsx` (lang toggle + play all)
- **Speak Button**: `src/components/verse/SpeakButton.tsx` (per-verse play/stop)
- **Verse Card**: `src/components/verse/VerseCard.tsx`
- **Verse Highlight**: `src/components/verse/VerseHighlight.tsx` (active TTS ring)
- **Share**: `src/components/verse/ShareButton.tsx`
- **Reading Progress**: `src/components/verse/ReadingProgress.tsx`
- **Continue Reading**: `src/components/navigation/ContinueReading.tsx`
- **Keyboard Nav**: `src/components/navigation/KeyboardNav.tsx`
- **SEO**: `src/app/sitemap.ts`, `src/app/robots.ts`, `src/app/opengraph-image.tsx`
- **JSON-LD**: `src/components/seo/JsonLd.tsx`
- **Header**: `src/components/layout/Header.tsx`
- **Footer**: `src/components/layout/Footer.tsx`
- **Globals CSS**: `src/app/globals.css` (animations, verse styles)
- **Security**: `next.config.ts` (security headers)

## Verse JSON Structure

```json
{
  "id": "sk-1-c1",
  "type": "chaupai",        // chaupai | doha | chhand | shloka | soratha
  "original": "Devanagari text",
  "transliteration": "IAST with diacritics",
  "translation": "English translation",
  "hindiTranslation": "Hindi meaning",
  "lineCount": 4
}
```

## Translation Workflow

1. Read verses from JSON: `data/tulsidas/{kand-name}.json`
2. Write a Node.js script at `c:/tmp/` that maps verse IDs to Hindi/English text
3. Run the script to apply translations
4. Build: `npm run build`
5. Commit & push: auto-deploys to Vercel

## Dev Commands

```bash
cd c:/_work/RamayanaPath
npx next dev --port 3000    # local dev
npm run build                # production build
git push origin master       # auto-deploys to Vercel
```

## Data Sources

- **Tulsidas verses**: IIT Kanpur (ramcharitmanas.iitk.ac.in)
- **Gita Press Gorakhpur**: Authoritative reference for verse structure and numbering
- **Valmiki shlokas**: IIT Kanpur (valmiki.iitk.ac.in)
- **Valmiki Uttara Kanda**: WisdomLib — Hari Prasad Shastri translation
- **Translations**: Original work

## UI Notes

- Ram icon: white silhouette PNG on orange (#f97316) circle, gentle float animation
- Card hover: border #fb923c, lift + shadow
- Translations collapsible (Hindi collapsed, English open by default)
- Version toggle: Tulsidas/Valmiki via cookie + full page reload
- Dark mode: toggle in header, persisted in localStorage
- Animations respect `prefers-reduced-motion`
