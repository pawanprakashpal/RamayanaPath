export type Lang = "en" | "hi";

export const LANGS: Lang[] = ["en", "hi"];

/** English lives at the root so existing indexed URLs are untouched. */
export function langPath(lang: Lang, path: string): string {
  const clean = path.startsWith("/") ? path : `/${path}`;
  if (lang === "en") return clean === "/" ? "/" : clean;
  return clean === "/" ? "/hi" : `/hi${clean}`;
}

interface Strings {
  tagline: string;
  siteDescription: string;
  dohas: string;
  sargas: string;
  verses: string;
  readPaath: string;
  paathHeading: (kand: string) => string;
  completeText: (dohas: number, verses: number) => string;
  reciteTime: (time: string) => string;
  tapForMeaning: string;
  readDohaByDoha: string;
  backToKand: string;
  allKands: string;
  faqHeading: (kand: string) => string;
  kandSubtitle: string;
  paathSubtitle: string;
  switchLang: string;
  hours: (n: number) => string;
  minutes: (n: number) => string;
}

export const UI: Record<Lang, Strings> = {
  en: {
    tagline: "Read the Ramayana with original verses and English translations",
    siteDescription:
      "Read the Ramayana epic — original verses with English translations from Tulsidas Ramcharitmanas and Valmiki Ramayana.",
    dohas: "Dohas",
    sargas: "Sargas",
    verses: "verses",
    readPaath: "Read the full paath",
    paathHeading: (kand) => `${kand} Paath`,
    completeText: (dohas, verses) =>
      `Complete text — ${dohas} dohas, ${verses} verses, one page.`,
    reciteTime: (time) => `About ${time} to recite.`,
    tapForMeaning: "Tap any verse for its Hindi meaning and English translation.",
    readDohaByDoha: "Read doha by doha instead →",
    backToKand: "Back to the Kand",
    allKands: "All Kands",
    faqHeading: (kand) => `Frequently asked about ${kand}`,
    kandSubtitle: "Ramcharitmanas verses with Hindi meaning & English translation",
    paathSubtitle: "Complete text in one page",
    switchLang: "हिन्दी",
    hours: (n) => `${n} hours`,
    minutes: (n) => `${n} minutes`,
  },
  hi: {
    tagline: "मूल पाठ, हिन्दी अर्थ और अंग्रेज़ी अनुवाद सहित रामायण पढ़ें",
    siteDescription:
      "श्रीरामचरितमानस और वाल्मीकि रामायण — मूल चौपाई, दोहे और श्लोक, हिन्दी अर्थ तथा अंग्रेज़ी अनुवाद के साथ ऑनलाइन पढ़ें।",
    dohas: "दोहे",
    sargas: "सर्ग",
    verses: "पद",
    readPaath: "सम्पूर्ण पाठ पढ़ें",
    paathHeading: (kand) => `${kand} पाठ`,
    completeText: (dohas, verses) =>
      `सम्पूर्ण पाठ — ${dohas} दोहे, ${verses} पद, एक ही पृष्ठ पर।`,
    reciteTime: (time) => `पाठ में लगभग ${time} लगते हैं।`,
    tapForMeaning: "किसी भी पद पर टैप करके उसका हिन्दी अर्थ और अंग्रेज़ी अनुवाद देखें।",
    readDohaByDoha: "दोहा-दर-दोहा पढ़ें →",
    backToKand: "काण्ड पर लौटें",
    allKands: "सभी काण्ड",
    faqHeading: (kand) => `${kand} — सामान्य प्रश्न`,
    kandSubtitle: "श्रीरामचरितमानस — हिन्दी अर्थ और अंग्रेज़ी अनुवाद सहित",
    paathSubtitle: "सम्पूर्ण पाठ एक ही पृष्ठ पर",
    switchLang: "English",
    hours: (n) => `${n} घंटे`,
    minutes: (n) => `${n} मिनट`,
  },
};

export function t(lang: Lang): Strings {
  return UI[lang];
}

/** hreflang map for a page that exists in both languages. */
export function languageAlternates(path: string) {
  return {
    "en-IN": langPath("en", path),
    hi: langPath("hi", path),
    "x-default": langPath("en", path),
  };
}
