#!/usr/bin/env node
/**
 * Turns the two data-reading API routes into static files, so the site can be
 * served as a pure static export with no Node origin.
 *
 * On Vercel these were Next route handlers reading ./data at request time. A
 * Cloudflare Worker cannot bundle 25 MB of verse JSON, so the data is reshaped
 * here, at build time, into exactly what each caller needs:
 *
 *   public/meanings/<kand>/<doha>.json  - what /api/meaning returned, fetched
 *                                         by PaathMeaning when a reader opens
 *                                         a verse. No function involved at all.
 *
 *   public/search/index.json            - the searchable fields plus enough
 *                                         text to render a result, read by the
 *                                         search Function. Display text is
 *                                         truncated: a result snippet does not
 *                                         need the whole shloka, and the full
 *                                         text is one click away on the page.
 *
 * Run before `next build`. Both outputs are deterministic, so rebuilding them
 * on every deploy costs nothing and they can never drift from the data.
 */

import { promises as fs } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const ROOT = process.cwd();
const DATA = path.join(ROOT, "data");
const PUBLIC = path.join(ROOT, "public");

/** Mirrors the mapping in src/lib/data.ts. */
const VALMIKI_FOLDER = {
  "sundar-kand": "sundara-kanda",
  "bal-kand": "bala-kanda",
  "ayodhya-kand": "ayodhya-kanda",
  "aranya-kand": "aranya-kanda",
  "kishkindha-kand": "kishkindha-kanda",
  "lanka-kand": "yuddha-kanda",
  "uttar-kand": "uttara-kanda",
};

/** Mirrors foldLatin in src/lib/search.ts - IAST diacritics folded away. */
function foldLatin(text) {
  return text.normalize("NFD").replace(/\p{Diacritic}/gu, "").toLowerCase();
}

function normaliseDeva(text) {
  return text.replace(/\s+/g, " ").trim();
}

/** Mirrors dohaTitle in src/lib/seo.ts. */
function dohaTitle(dohaNumber, label) {
  if (label) return label;
  return dohaNumber === 0 ? "Mangalacharan" : `Doha ${dohaNumber}`;
}

async function readJson(file) {
  try {
    return JSON.parse(await fs.readFile(file, "utf-8"));
  } catch {
    return null;
  }
}

async function writeJson(file, value) {
  await fs.mkdir(path.dirname(file), { recursive: true });
  await fs.writeFile(file, JSON.stringify(value), "utf-8");
}

/** A result snippet, not the whole verse. */
function clip(text, max) {
  const t = (text ?? "").trim();
  return t.length <= max ? t : t.slice(0, max);
}

async function main() {
  const manifest = await readJson(path.join(DATA, "kands.json"));
  if (!manifest?.kands) throw new Error("data/kands.json not readable");

  let meaningFiles = 0;
  const index = [];

  for (const kand of manifest.kands) {
    // ---- Tulsidas: meanings per doha group, and search records ----
    if (kand.tulsidas?.available) {
      const data = await readJson(path.join(DATA, "tulsidas", `${kand.slug}.json`));
      for (const group of data?.dohaGroups ?? []) {
        await writeJson(
          path.join(PUBLIC, "meanings", kand.slug, `${group.dohaNumber}.json`),
          {
            verses: group.verses.map((v) => ({
              id: v.id,
              transliteration: v.transliteration ?? "",
              hindiTranslation: v.hindiTranslation ?? "",
              translation: v.translation ?? "",
            })),
          }
        );
        meaningFiles++;

        const label = dohaTitle(group.dohaNumber, group.label);
        for (const verse of group.verses) {
          index.push(record({
            id: verse.id,
            version: "tulsidas",
            kandName: kand.tulsidas.name,
            unitLabel: label,
            href: `/${kand.slug}/doha/${group.dohaNumber}`,
            type: verse.type,
            original: verse.original,
            transliteration: verse.transliteration,
            translation: verse.translation,
            hindiTranslation: verse.hindiTranslation,
          }));
        }
      }
    }

    // ---- Valmiki: search records only; there is no meaning panel ----
    if (kand.valmiki?.available) {
      const dir = path.join(DATA, "valmiki", VALMIKI_FOLDER[kand.slug] ?? kand.slug);
      let files = [];
      try {
        files = (await fs.readdir(dir)).filter((f) => f.endsWith(".json"));
      } catch {
        files = [];
      }
      for (const file of files) {
        const raw = await readJson(path.join(dir, file));
        for (const shloka of raw?.shlokas ?? []) {
          index.push(record({
            id: shloka.id,
            version: "valmiki",
            kandName: kand.valmiki.name,
            unitLabel: `Sarga ${raw.sarga.number}`,
            href: `/${kand.slug}/sarga/${raw.sarga.number}`,
            type: shloka.type,
            original: shloka.original,
            transliteration: shloka.transliteration,
            translation: shloka.translation,
            hindiTranslation: shloka.hindiTranslation,
          }));
        }
      }
    }
  }

  await writeJson(path.join(PUBLIC, "search", "index.json"), index);

  const bytes = (await fs.stat(path.join(PUBLIC, "search", "index.json"))).size;
  console.log(`  meanings : ${meaningFiles} files`);
  console.log(`  search   : ${index.length} records, ${(bytes / 1024 / 1024).toFixed(1)} MB`);
}

/**
 * Short keys because this file is fetched whole by the search Function; the
 * names cost more than the data at 26k records.
 */
function record(v) {
  const transliteration = v.transliteration ?? "";
  const translation = v.translation ?? "";
  const hindiTranslation = v.hindiTranslation ?? "";
  const original = v.original ?? "";
  return {
    i: v.id,
    v: v.version,
    kn: v.kandName,
    ul: v.unitLabel,
    h: v.href,
    t: v.type,
    o: clip(original, 220),
    tr: clip(transliteration, 220),
    tl: clip(translation, 260),
    hi: clip(hindiTranslation, 260),
    // Match against the untruncated text, so a word late in a long shloka is
    // still findable even though the snippet stops short.
    hl: foldLatin(`${translation} ${transliteration}`),
    hd: normaliseDeva(`${original} ${hindiTranslation}`),
  };
}

/**
 * Next 16 writes eight segment-level RSC payloads per page for its client
 * router - __next._tree.txt, __next._full.txt and one per route segment. At
 * 2,867 pages that is ~23,000 extra files and about a gigabyte, which puts the
 * export over Cloudflare Pages' 20,000 file limit on its own.
 *
 * They only speed up in-app navigation, and the shared-layout links already
 * carry prefetch={false} after the CDN request work, so little is lost:
 * without them the router falls back to a normal page load, which for a site
 * people reach from search and read a page at a time is what happens anyway.
 * The per-page .txt beside each .html is kept - that is the page payload.
 */
export async function pruneSegmentPayloads(dir) {
  let removed = 0;
  async function walk(d) {
    let entries;
    try {
      entries = await fs.readdir(d, { withFileTypes: true });
    } catch {
      return;
    }
    for (const e of entries) {
      const full = path.join(d, e.name);
      if (e.isDirectory()) {
        if (e.name.startsWith("__next.")) {
          const count = await countFiles(full);
          await fs.rm(full, { recursive: true, force: true });
          removed += count;
        } else {
          await walk(full);
        }
      } else if (e.name.startsWith("__next.") && e.name.endsWith(".txt")) {
        await fs.rm(full, { force: true });
        removed++;
      }
    }
  }
  async function countFiles(d) {
    let n = 0;
    for (const e of await fs.readdir(d, { withFileTypes: true })) {
      n += e.isDirectory() ? await countFiles(path.join(d, e.name)) : 1;
    }
    return n;
  }
  await walk(dir);
  return removed;
}

// Only generate when run directly: prune-export.mjs imports the helper above
// and must not set the whole build going again.
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch((err) => {
    console.error(err);
    process.exit(1);
  });
}
