import path from "path";
import { promises as fs } from "fs";
import type { KandManifest, KandManifestEntry, TulsidasKandData, DohaGroup, ValmikiSargaData } from "@/types";

const DATA_DIR = path.join(process.cwd(), "data");

export async function getKandManifest(): Promise<KandManifest> {
  const filePath = path.join(DATA_DIR, "kands.json");
  const raw = await fs.readFile(filePath, "utf-8");
  return JSON.parse(raw);
}

export async function getKandBySlug(slug: string): Promise<KandManifestEntry | null> {
  const manifest = await getKandManifest();
  return manifest.kands.find((k) => k.slug === slug) ?? null;
}

export async function getTulsidasKand(kandSlug: string): Promise<TulsidasKandData | null> {
  const filePath = path.join(DATA_DIR, "tulsidas", `${kandSlug}.json`);
  try {
    const raw = await fs.readFile(filePath, "utf-8");
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

export async function getDohaGroup(kandSlug: string, dohaNumber: number): Promise<DohaGroup | null> {
  const data = await getTulsidasKand(kandSlug);
  if (!data) return null;
  return data.dohaGroups.find((g) => g.dohaNumber === dohaNumber) ?? null;
}

export async function getTulsidasTotalDohas(kandSlug: string): Promise<number> {
  const data = await getTulsidasKand(kandSlug);
  if (!data) return 0;
  return data.kand.totalDohas;
}

export async function getValmikiSarga(kandSlug: string, sargaNumber: number): Promise<ValmikiSargaData | null> {
  // Map tulsidas slug to valmiki folder name
  const valmikiFolderMap: Record<string, string> = {
    "sundar-kand": "sundara-kanda",
    "bal-kand": "bala-kanda",
    "ayodhya-kand": "ayodhya-kanda",
    "aranya-kand": "aranya-kanda",
    "kishkindha-kand": "kishkindha-kanda",
    "lanka-kand": "yuddha-kanda",
    "uttar-kand": "uttara-kanda",
  };
  const folder = valmikiFolderMap[kandSlug] ?? kandSlug;
  const filePath = path.join(DATA_DIR, "valmiki", folder, `sarga-${String(sargaNumber).padStart(2, "0")}.json`);
  try {
    const raw = await fs.readFile(filePath, "utf-8");
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

export async function getValmikiTotalSargas(kandSlug: string): Promise<number> {
  const kand = await getKandBySlug(kandSlug);
  if (!kand) return 0;
  return kand.valmiki.totalUnits;
}

export async function getAvailableKands(): Promise<KandManifestEntry[]> {
  const manifest = await getKandManifest();
  return manifest.kands;
}
