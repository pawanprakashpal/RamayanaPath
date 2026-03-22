export interface KandInfo {
  id: string;
  name: string;
  nameHindi?: string;
  nameSanskrit?: string;
  index: number;
}

export interface KandVersionInfo {
  name: string;
  nameOriginal: string;
  totalUnits: number; // dohas for Tulsidas, sargas for Valmiki
  available: boolean;
}

export interface KandManifestEntry {
  index: number;
  slug: string;
  tulsidas: KandVersionInfo;
  valmiki: KandVersionInfo;
}

export interface KandManifest {
  kands: KandManifestEntry[];
}
