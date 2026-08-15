import type { KandManifestEntry } from "@/types";

export const BASE_URL = "https://ramayanpath.com";

export function absoluteUrl(path: string): string {
  return `${BASE_URL}${path.startsWith("/") ? path : `/${path}`}`;
}

/**
 * Human title for a Tulsidas doha group. Group 0 holds the opening
 * mangalacharan shlokas, so "Doha 0" is both wrong and a wasted title tag.
 */
export function dohaTitle(dohaNumber: number, label?: string | null): string {
  if (label) return label;
  if (dohaNumber === 0) return "Mangalacharan";
  return `Doha ${dohaNumber}`;
}

/** Per-Kand editorial copy used for descriptions, FAQ answers and OG cards. */
interface KandSeoEntry {
  /** What the Kand covers — one sentence, reused in meta descriptions. */
  summary: string;
  /** Well-known passages/episodes searched by name. */
  highlights: string;
  /** Recitation tradition, shown on the paath page where one exists. */
  paathNote?: string;
}

const KAND_SEO: Record<string, KandSeoEntry> = {
  "bal-kand": {
    summary:
      "Bal Kand opens the Ramcharitmanas with the invocation to Ganesha and Saraswati, the Shiva–Sati and Shiva–Parvati narratives, the birth and childhood of Shri Ram and his brothers, the breaking of Shiva's bow at Sita's swayamvar, and the marriage of Ram and Sita.",
    highlights:
      "Mangal Bhavan Amangal Hari, the Shiv-Parvati vivah, Ram Janm, and the Dhanush Yagya",
  },
  "ayodhya-kand": {
    summary:
      "Ayodhya Kand narrates Kaikeyi's two boons, Shri Ram's fourteen-year exile with Sita and Lakshman, the grief and death of King Dasharath, and Bharat's journey to Chitrakoot to plead for Ram's return.",
    highlights: "Ram Vanvas, Kevat Prasang, Dasharath Maran, and Bharat Milap",
  },
  "aranya-kand": {
    summary:
      "Aranya Kand follows Shri Ram's life in the Dandaka forest — the meetings with the sages, the episode of Shurpanakha, Maricha's golden deer, the abduction of Sita by Ravan, the sacrifice of Jatayu, and the grace shown to Shabari.",
    highlights: "Surpanakha Prasang, Maya Mrig, Sita Haran, Jatayu, and Shabari",
  },
  "kishkindha-kand": {
    summary:
      "Kishkindha Kand describes Shri Ram's meeting with Hanuman and Sugriv, the slaying of Bali, the alliance with the vanar army, and the search parties sent in all directions to find Sita.",
    highlights: "Hanuman Milan, Sugriv Maitri, Bali Vadh, and the Sita search",
  },
  "sundar-kand": {
    summary:
      "Sundar Kand recounts Hanuman's leap across the ocean to Lanka, his search for Sita, their meeting in the Ashok Vatika, the burning of Lanka, and his return with Sita's message — the Kand most often recited as a complete paath.",
    highlights:
      "Hanuman's ocean leap, the Ashok Vatika meeting, Lanka Dahan, and the Ram-Sugriv Sanvad",
    paathNote:
      "Sundar Kand is the Kand most often recited on its own, traditionally on Tuesdays and Saturdays — the days associated with Hanuman — and often completed in a single sitting.",
  },
  "lanka-kand": {
    summary:
      "Lanka Kand (Yuddha Kand) covers the building of the Ram Setu, Angad's embassy to Ravan's court, the great war at Lanka, Lakshman's revival by the Sanjeevani herb, the slaying of Kumbhakaran, Meghnad and Ravan, and the return to Ayodhya.",
    highlights:
      "Setu Bandh, Angad Sandesh, Sanjeevani Booti, Kumbhakaran Vadh, and Ravan Vadh",
  },
  "uttar-kand": {
    summary:
      "Uttar Kand describes the coronation of Shri Ram and the establishment of Ram Rajya, followed by the discourses of Kakbhushundi and Garud on bhakti, gyan and the nature of devotion.",
    highlights: "Ram Rajyabhishek, Ram Rajya, and the Kakbhushundi-Garud Sanvad",
  },
};

export function getKandSeo(slug: string): KandSeoEntry | undefined {
  return KAND_SEO[slug];
}

/** FAQPage entries for a Kand landing page. Answers are derived from real counts. */
export function buildKandFaq(
  kand: KandManifestEntry,
  totalDohaGroups: number,
  totalVerses: number
): { question: string; answer: string }[] {
  const seo = getKandSeo(kand.slug);
  const t = kand.tulsidas;
  const v = kand.valmiki;

  const faq = [
    {
      question: `How many dohas are in ${t.name}?`,
      answer: `${t.name} (${t.nameOriginal}) of the Tulsidas Ramcharitmanas has ${t.totalUnits} dohas, grouped into ${totalDohaGroups} sections containing ${totalVerses} individual verses in total — chaupais, dohas, sorathas and chhands.`,
    },
    {
      question: `What happens in ${t.name}?`,
      answer: seo?.summary ?? `${t.name} is one of the seven Kands of the Ramcharitmanas.`,
    },
    {
      question: `How many sargas are in Valmiki's ${v.name}?`,
      answer: `${v.name} (${v.nameOriginal}) of the Valmiki Ramayana has ${v.totalUnits} sargas of Sanskrit shlokas, each available here with an English translation.`,
    },
    {
      question: `Can I read ${t.name} in Hindi and English?`,
      answer: `Yes. Every verse of ${t.name} on RamayanaPath shows the original Awadhi text in Devanagari, a Hindi meaning (अर्थ), an English translation, and IAST transliteration — free and without registration.`,
    },
  ];

  if (seo?.highlights) {
    faq.splice(2, 0, {
      question: `Which famous passages are in ${t.name}?`,
      answer: `${t.name} contains ${seo.highlights}. Each passage can be read verse by verse with its meaning and translation.`,
    });
  }

  return faq;
}

export function faqPageJsonLd(faq: { question: string; answer: string }[]) {
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faq.map((f) => ({
      "@type": "Question",
      name: f.question,
      acceptedAnswer: { "@type": "Answer", text: f.answer },
    })),
  };
}

export function breadcrumbJsonLd(items: { name: string; path: string }[]) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: item.name,
      item: absoluteUrl(item.path),
    })),
  };
}

/** Collapse verse text to a single clean line for meta descriptions. */
export function excerpt(text: string, maxLength: number): string {
  const flat = text.replace(/\s+/g, " ").trim();
  if (flat.length <= maxLength) return flat;
  return `${flat.slice(0, maxLength).replace(/[\s।॥,;-]+$/, "")}…`;
}
