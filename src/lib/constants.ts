export const SITE_NAME = "RamayanaPath";
export const SITE_DESCRIPTION = "Read the Ramayana epic — original verses with English translations from Tulsidas Ramcharitmanas and Valmiki Ramayana.";

export const VERSION_LABELS = {
  tulsidas: "Tulsidas (Ramcharitmanas)",
  valmiki: "Valmiki (Sanskrit)",
} as const;

export const VERSE_TYPE_LABELS = {
  chaupai: "Chaupai",
  doha: "Doha",
  sortha: "Sortha",
  chhand: "Chhand",
  shloka: "Shloka",
} as const;

export const VERSE_TYPE_COLORS = {
  chaupai: "bg-saffron-100 text-saffron-800 dark:bg-saffron-900 dark:text-saffron-200",
  doha: "bg-amber-100 text-amber-800 dark:bg-amber-900 dark:text-amber-200",
  sortha: "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
  chhand: "bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200",
  shloka: "bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200",
} as const;

export const DEFAULT_VERSION = "tulsidas" as const;
export const VERSION_COOKIE = "ramayana-version";
