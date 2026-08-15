export type Version = "tulsidas" | "valmiki";
export type Theme = "light" | "dark";
// The JSON data spells this "soratha"; "sortha" is kept as an alias so older
// records keep type-checking.
export type VerseType = "chaupai" | "doha" | "soratha" | "sortha" | "chhand" | "shloka";

export interface Bookmark {
  id: string;
  version: Version;
  kand: string;
  label: string;
  /** Path back to the passage, e.g. "/sundar-kand/doha/1". */
  href: string;
  timestamp: number;
}

export interface ReadingProgress {
  kand: string;
  version: Version;
  /** Doha number for Tulsidas, Sarga number for Valmiki */
  position: number;
  updatedAt: number;
}
