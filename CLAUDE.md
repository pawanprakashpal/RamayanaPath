# RamayanaPath - Project Guide

## Project Overview
- **Site**: https://ramayanpath.com (Vercel auto-deploy on push to master)
- **Repo**: github.com/pawanprakashpal/RamayanaPath
- **Stack**: Next.js 16 (App Router), TypeScript, Tailwind CSS
- **Purpose**: Read the Ramayana with original verses, Hindi meanings, and English translations

## Content Status

### Tulsidas Ramcharitmanas (5,809 verses)
| Kand | Dohas | Verses | English | Hindi |
|------|-------|--------|---------|-------|
| Bal Kand | 361 | 1,894 | 100% | 7% (doha 22 next) |
| Ayodhya Kand | 326 | 1,619 | 100% | 0% |
| Aranya Kand | 46 | 304 | 100% | 100% |
| Kishkindha Kand | 30 | 186 | 100% | 100% |
| Sundar Kand | 60 | 336 | 100% | 100% |
| Lanka Kand | 121 | 727 | 100% | 100% |
| Uttar Kand | 130 | 743 | 100% | 100% |

### Valmiki Ramayana (20,214 shlokas) - ALL COMPLETE
- 6 Kandas from IIT Kanpur (Sanskrit + English)
- 1 Kanda (Uttara) from WisdomLib (English only)

## Priority TODO
1. **Finish Bal Kand Hindi** — start from doha 22 (130/1894 done)
2. **Finish Ayodhya Kand Hindi** — 0/1619
3. **Audio feature** — IIT Kanpur has mp3 per doha/sarga
4. **Animations** — add UI animations for better experience

## How to Resume Hindi Translations

### Prompt to continue:
```
Continue Hindi translations for RamayanaPath — Bal Kand from doha 22, then Ayodhya Kand. After that, audio feature and animations.
```

### Translation workflow:
1. Read verses from JSON
2. Write a Node.js script that maps verse IDs to Hindi text
3. Run the script to apply translations
4. Commit & push after each batch (~100-160 verses per batch)

### Check progress:
```bash
cd c:/_work/RamayanaPath && node -e "
const fs=require('fs');
['bal-kand','ayodhya-kand','aranya-kand','kishkindha-kand','sundar-kand','lanka-kand','uttar-kand'].forEach(f=>{
  const d=JSON.parse(fs.readFileSync('data/tulsidas/'+f+'.json','utf8'));
  const t=d.dohaGroups.reduce((a,g)=>a+g.verses.length,0);
  const h=d.dohaGroups.reduce((a,g)=>a+g.verses.filter(v=>v.hindiTranslation).length,0);
  if(h<t) console.log(f+': '+h+'/'+t+' ('+Math.round(h/t*100)+'%)');
  else console.log(f+': DONE');
});"
```

## Key Files
- **Data**: `data/tulsidas/{kand-name}.json` (one file per Kand)
- **Valmiki**: `data/valmiki/{kanda-name}/sarga-{NN}.json` (one file per sarga)
- **Manifest**: `data/kands.json`
- **Types**: `src/types/verse.ts`, `src/types/kand.ts`, `src/types/common.ts`
- **Data lib**: `src/lib/data.ts`
- **Verse reader**: `src/app/[kand]/doha/[number]/page.tsx`
- **Sarga reader**: `src/app/[kand]/sarga/[number]/page.tsx`
- **Header**: `src/components/layout/Header.tsx`
- **Version toggle**: `src/components/navigation/VersionSelector.tsx`
- **Verse card**: `src/components/verse/VerseCard.tsx`
- **Footer**: `src/components/layout/Footer.tsx`

## Verse JSON Structure
```json
{
  "id": "sk-1-c1",
  "type": "chaupai",
  "original": "Devanagari text",
  "transliteration": "IAST with diacritics",
  "translation": "English translation",
  "hindiTranslation": "Hindi meaning",
  "lineCount": 4
}
```

## Data Sources & Attribution
- **Tulsidas verses**: IIT Kanpur (ramcharitmanas.iitk.ac.in) — public domain
- **Valmiki shlokas**: IIT Kanpur (valmiki.iitk.ac.in) — Sanskrit + English
- **Valmiki Uttara Kanda**: WisdomLib — Hari Prasad Shastri translation
- **English & Hindi translations**: Original work, generated fresh
- Attribution in footer links to IIT Kanpur sources

## UI Notes
- Ram icon: white silhouette PNG on orange (#f97316) circle
- Card hover border: #fb923c
- Translations collapsible (Hindi collapsed, English open by default)
- Version toggle: Tulsidas/Valmiki via cookie + full page reload

## Dev Commands
```bash
npx next dev --port 3000    # local dev
npx next build               # production build
git push origin master       # auto-deploys to Vercel
```
