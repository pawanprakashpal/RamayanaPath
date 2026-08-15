import path from "path";
import { promises as fs } from "fs";
import { getKandManifest } from "./data";
import { dohaTitle } from "./seo";
import type { TulsidasKandData, ValmikiSargaData, Version } from "@/types";

const DATA_DIR = path.join(process.cwd(), "data");

export interface SearchRecord {
  id: string;
  version: Version;
  kandSlug: string;
  /** Display name of the Kand in the relevant recension. */
  kandName: string;
  /** Doha number for Tulsidas, sarga number for Valmiki. */
  unit: number;
  /** "Doha 5", "Mangalacharan", "Sarga 12". */
  unitLabel: string;
  href: string;
  type: string;
  original: string;
  transliteration: string;
  translation: string;
  hindiTranslation: string;
  /** Latin fields, lowercased and stripped of diacritics, for matching. */
  haystackLatin: string;
  /** Devanagari fields, whitespace-normalised, for matching. */
  haystackDeva: string;
}

/**
 * "sañjīvanī" and "Sanjivani" must match each other, so IAST diacritics are
 * folded away on both the index and the query side.
 */
export function foldLatin(text: string): string {
  return text
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "")
    .toLowerCase();
}

function normaliseDeva(text: string): string {
  return text.replace(/\s+/g, " ").trim();
}

let indexPromise: Promise<SearchRecord[]> | null = null;

/**
 * Builds the index once per server instance. 26k verses across ~25MB of JSON is
 * far too much to ship to the browser, so matching happens here; the read cost
 * is paid on the first search after a cold start and reused after that.
 */
export function getSearchIndex(): Promise<SearchRecord[]> {
  if (!indexPromise) {
    indexPromise = buildIndex().catch((err) => {
      // Don't cache a failed build — the next request should retry.
      indexPromise = null;
      throw err;
    });
  }
  return indexPromise;
}

async function buildIndex(): Promise<SearchRecord[]> {
  const manifest = await getKandManifest();
  const records: SearchRecord[] = [];

  for (const kand of manifest.kands) {
    if (kand.tulsidas.available) {
      const raw = await readJson<TulsidasKandData>(
        path.join(DATA_DIR, "tulsidas", `${kand.slug}.json`)
      );
      for (const group of raw?.dohaGroups ?? []) {
        const label = dohaTitle(group.dohaNumber, group.label);
        for (const verse of group.verses) {
          records.push(
            toRecord({
              id: verse.id,
              version: "tulsidas",
              kandSlug: kand.slug,
              kandName: kand.tulsidas.name,
              unit: group.dohaNumber,
              unitLabel: label,
              href: `/${kand.slug}/doha/${group.dohaNumber}`,
              type: verse.type,
              original: verse.original,
              transliteration: verse.transliteration,
              translation: verse.translation,
              hindiTranslation: verse.hindiTranslation,
            })
          );
        }
      }
    }

    if (kand.valmiki.available) {
      const folder = valmikiFolder(kand.slug);
      const dir = path.join(DATA_DIR, "valmiki", folder);
      let files: string[] = [];
      try {
        files = (await fs.readdir(dir)).filter((f) => f.endsWith(".json"));
      } catch {
        files = [];
      }
      for (const file of files) {
        const raw = await readJson<ValmikiSargaData>(path.join(dir, file));
        if (!raw) continue;
        for (const shloka of raw.shlokas) {
          records.push(
            toRecord({
              id: shloka.id,
              version: "valmiki",
              kandSlug: kand.slug,
              kandName: kand.valmiki.name,
              unit: raw.sarga.number,
              unitLabel: `Sarga ${raw.sarga.number}`,
              href: `/${kand.slug}/sarga/${raw.sarga.number}`,
              type: shloka.type,
              original: shloka.original,
              transliteration: shloka.transliteration,
              translation: shloka.translation,
              hindiTranslation: shloka.hindiTranslation,
            })
          );
        }
      }
    }
  }

  return records;
}

function toRecord(
  input: Omit<SearchRecord, "haystackLatin" | "haystackDeva" | "hindiTranslation" | "transliteration" | "translation"> & {
    transliteration?: string;
    translation?: string;
    hindiTranslation?: string;
  }
): SearchRecord {
  const transliteration = input.transliteration ?? "";
  const translation = input.translation ?? "";
  const hindiTranslation = input.hindiTranslation ?? "";

  return {
    ...input,
    transliteration,
    translation,
    hindiTranslation,
    haystackLatin: foldLatin(`${translation} ${transliteration}`),
    haystackDeva: normaliseDeva(`${input.original} ${hindiTranslation}`),
  };
}

async function readJson<T>(filePath: string): Promise<T | null> {
  try {
    return JSON.parse(await fs.readFile(filePath, "utf-8")) as T;
  } catch {
    return null;
  }
}

function valmikiFolder(kandSlug: string): string {
  const map: Record<string, string> = {
    "sundar-kand": "sundara-kanda",
    "bal-kand": "bala-kanda",
    "ayodhya-kand": "ayodhya-kanda",
    "aranya-kand": "aranya-kanda",
    "kishkindha-kand": "kishkindha-kanda",
    "lanka-kand": "yuddha-kanda",
    "uttar-kand": "uttara-kanda",
  };
  return map[kandSlug] ?? kandSlug;
}

// --- Querying -------------------------------------------------------------

export interface SearchHit {
  id: string;
  version: Version;
  kandName: string;
  unitLabel: string;
  href: string;
  type: string;
  original: string;
  transliteration: string;
  translation: string;
  hindiTranslation: string;
  score: number;
}

export interface SearchOutcome {
  hits: SearchHit[];
  total: number;
  /** Set when the query looked like a verse reference, e.g. "sundar kand doha 5". */
  reference?: { label: string; href: string };
}

const DEVANAGARI = /\p{Script=Devanagari}/u;

export async function searchVerses(
  rawQuery: string,
  options: { version?: Version | "all"; limit?: number } = {}
): Promise<SearchOutcome> {
  const query = rawQuery.trim();
  const limit = options.limit ?? 40;
  const versionFilter = options.version ?? "all";

  if (query.length < 2) return { hits: [], total: 0 };

  const index = await getSearchIndex();
  const reference = await matchReference(query);

  const isDeva = DEVANAGARI.test(query);
  const terms = (isDeva ? normaliseDeva(query) : foldLatin(query))
    .split(/\s+/)
    .filter((t) => t.length > 0);
  const phrase = isDeva ? normaliseDeva(query) : foldLatin(query);

  const scored: SearchHit[] = [];

  for (const record of index) {
    if (versionFilter !== "all" && record.version !== versionFilter) continue;

    const haystack = isDeva ? record.haystackDeva : record.haystackLatin;

    // Every term must appear — precision matters more than recall when a
    // single word can return thousands of verses.
    let matchesAll = true;
    for (const term of terms) {
      if (!haystack.includes(term)) {
        matchesAll = false;
        break;
      }
    }
    if (!matchesAll) continue;

    let score = 1;
    if (haystack.includes(phrase)) score += 6;
    // Whole-word hits beat matches buried inside longer words.
    for (const term of terms) {
      if (new RegExp(`(^|\\s)${escapeRegExp(term)}($|\\s|[।॥,.;:!?])`).test(haystack)) {
        score += 2;
      }
    }
    // A hit in the original verse is more meaningful than one in a translation.
    const originalHay = isDeva ? normaliseDeva(record.original) : foldLatin(record.transliteration);
    if (originalHay.includes(phrase)) score += 3;

    scored.push({
      id: record.id,
      version: record.version,
      kandName: record.kandName,
      unitLabel: record.unitLabel,
      href: record.href,
      type: record.type,
      original: record.original,
      transliteration: record.transliteration,
      translation: record.translation,
      hindiTranslation: record.hindiTranslation,
      score,
    });
  }

  scored.sort((a, b) => b.score - a.score);

  return {
    hits: scored.slice(0, limit),
    total: scored.length,
    reference,
  };
}

function escapeRegExp(text: string): string {
  return text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** Recognises "sundar kand doha 5", "bal kand sarga 12", "doha 40". */
async function matchReference(query: string): Promise<SearchOutcome["reference"]> {
  const match = /(doha|sarga|shloka|chaupai)\s*(\d{1,3})/i.exec(query);
  if (!match) return undefined;

  const unitWord = match[1].toLowerCase();
  const unit = parseInt(match[2], 10);
  const isSarga = unitWord === "sarga" || unitWord === "shloka";

  const manifest = await getKandManifest();
  const folded = foldLatin(query);
  const kand =
    manifest.kands.find((k) => folded.includes(foldLatin(k.slug.replace(/-/g, " ")))) ??
    manifest.kands.find((k) => folded.includes(foldLatin(k.tulsidas.name))) ??
    manifest.kands.find((k) => folded.includes(foldLatin(k.valmiki.name)));

  if (!kand) return undefined;

  if (isSarga) {
    if (unit < 1 || unit > kand.valmiki.totalUnits) return undefined;
    return {
      label: `${kand.valmiki.name} — Sarga ${unit}`,
      href: `/${kand.slug}/sarga/${unit}`,
    };
  }

  if (unit < 0 || unit > kand.tulsidas.totalUnits) return undefined;
  return {
    label: `${kand.tulsidas.name} — ${dohaTitle(unit)}`,
    href: `/${kand.slug}/doha/${unit}`,
  };
}
