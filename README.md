# RamayanPath

Read the Ramayana with original verses, Hindi meanings, and English translations.

**Live**: [ramayanpath.com](https://ramayanpath.com)

A Next.js reading platform for the Indian epic Ramayana, supporting both
Goswami Tulsidas's *Ramcharitmanas* (Awadhi) and Maharshi Valmiki's *Ramayana*
(Sanskrit). Trilingual presentation, neural text-to-speech, and a focus on
making the text approachable for modern readers.

## Content

| Edition | Verses / Shlokas | Translation status |
| --- | --- | --- |
| Tulsidas Ramcharitmanas | 6,072 verses across 7 Kands | Hindi + English: 100% |
| Valmiki Ramayana | 20,214 shlokas across 7 Kandas | English: 100%, Hindi: ~73% |

Sources: IIT Kanpur, Gita Press, ramcharit.in, BharatDiscovery (cited on the
[About page](https://ramayanpath.com/about)).

## Features

- **Trilingual reading** — original Devanagari + Hindi meaning + English translation
- **Neural TTS** — Azure `hi-IN-MadhurNeural` and `en-US-Andrew` voices, with
  per-verse and "Play All" sequential playback; falls back to browser speech
  synthesis when the Azure quota is exhausted
- **Language-aware playback** — toggle between Original / हिन्दी / English for TTS
- **Reading progress** — last-read doha is saved per Kand in `localStorage`,
  with a "Continue Reading" button on each Kand page
- **Keyboard navigation** — `←` / `→` for prev/next doha
- **Share** — WhatsApp, X/Twitter, Copy Link, native share on mobile
- **Dark mode** — toggle in header, persisted in `localStorage`
- **PWA** — installable, offline-capable manifest
- **SEO** — sitemap, robots.txt, Open Graph image, JSON-LD
  (`WebSite` + `BreadcrumbList` + `CreativeWork`), canonical URLs
- **Accessibility** — animations respect `prefers-reduced-motion`
- **Security** — security headers, SSML escaping, rate limiting on the TTS API

## Tech stack

- **Framework**: [Next.js 16](https://nextjs.org) (App Router) + TypeScript
- **Styling**: Tailwind CSS v4
- **Hosting**: Vercel (auto-deploy on push to `master`)
- **TTS**: Azure Speech Services (F0 free tier, 500K chars/month)
- **Data**: Static JSON files in `data/`, no database

## Project structure

```text
data/
  tulsidas/{kand}.json         # Doha groups + chaupais + dohas/sorathas
  valmiki/{kanda}/sarga-NN.json # Sanskrit + transliteration + translations
  kands.json                    # Manifest of all 7 Kandas (both editions)

src/
  app/                          # Next.js App Router pages
    [kand]/doha/[number]/       # Tulsidas doha view
    [kand]/sarga/[number]/      # Valmiki sarga view
    api/tts/                    # Azure TTS proxy with rate limiter
  components/verse/             # VerseCard, TtsProvider, SpeakButton, etc.
  lib/data.ts                   # Data loaders
```

## Development

```bash
git clone https://github.com/pawanprakashpal/RamayanaPath.git
cd RamayanaPath
npm install

# Optional: Azure TTS env vars (without these, browser TTS is used)
echo "AZURE_SPEECH_KEY=your-key" >> .env
echo "AZURE_SPEECH_REGION=centralindia" >> .env

npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

```bash
npm run build  # production build
npm run lint   # ESLint
```

## Notable engineering work

- **Soratha identification**: 62 verses across all 7 Kands were originally
  mistyped as "doha" in the IIT Kanpur source. Identified them by parsing the
  Gita Press Ramcharitmanas full text on archive.org for `So.:` markers and
  cross-referenced against BharatDiscovery and Ramcharit.in.
- **Valmiki Hindi pipeline**: Built a curl-based scraper for ramcharit.in (the
  default browser-style headers bypass Mod_Security where bare `curl` returns
  406). Parser handles ॥N॥ shloka markers including combined-shloka ranges
  (`॥N-M॥`). Applied across ~14,800 shlokas.
- **TTS playback bug**: Fixed an issue where the active verse card would
  visually disappear during playback. Root cause was the staggered entrance
  animation's `opacity: 0` base style being exposed when the `tts-active`
  class replaced the `fadeInUp` animation. Fixed by switching the entrance
  animation to `animation-fill-mode: backwards` so the natural `opacity: 1`
  state applies after entry.

## Status

Active personal project. Tulsidas Ramcharitmanas is fully translated and
proofread (April 2026 QA pass). Valmiki Hindi translations are at ~73% — the
remaining gaps (Yuddha sargas 26-29 & 72-128, Uttara sargas 30-131) are not
yet published on ramcharit.in and need an alternative source.

## License

The Sanskrit and Awadhi source texts are public domain. Hindi and English
translations are sourced from the references cited on the About page, used
under fair use for non-commercial educational presentation. Application code
is provided as-is without a formal license.
