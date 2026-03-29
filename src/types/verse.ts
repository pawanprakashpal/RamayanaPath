import { VerseType, Version } from "./common";
import { KandInfo } from "./kand";

export interface BaseVerse {
  id: string;
  type: VerseType;
  original: string;
  transliteration: string;
  translation: string;
  hindiTranslation?: string;
}

export interface TulsidasVerse extends BaseVerse {
  lineCount: number;
}

export interface DohaGroup {
  dohaNumber: number;
  label?: string;
  verses: TulsidasVerse[];
}

export interface TulsidasKandData {
  version: "tulsidas";
  kand: KandInfo & { totalDohas: number };
  dohaGroups: DohaGroup[];
}

export interface ValmikiShloka extends BaseVerse {
  number: number;
  metre?: string;
}

export interface SargaInfo {
  number: number;
  title: string;
  titleSanskrit: string;
  totalShlokas: number;
}

export interface ValmikiSargaData {
  version: "valmiki";
  kanda: KandInfo & { totalSargas: number };
  sarga: SargaInfo;
  shlokas: ValmikiShloka[];
}
