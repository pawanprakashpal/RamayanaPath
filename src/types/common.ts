export type Version = "tulsidas" | "valmiki";
export type Theme = "light" | "dark";
export type VerseType = "chaupai" | "doha" | "sortha" | "chhand" | "shloka";

export interface Bookmark {
  id: string;
  version: Version;
  kand: string;
  label: string;
  timestamp: number;
}

export interface ReadingProgress {
  kand: string;
  version: Version;
  /** Doha number for Tulsidas, Sarga number for Valmiki */
  position: number;
  updatedAt: number;
}
