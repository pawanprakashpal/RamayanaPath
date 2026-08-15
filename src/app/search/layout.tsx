import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Search Ramayana Verses — Ramcharitmanas & Valmiki Ramayana",
  description:
    "Search 26,000+ verses of the Ramayana by keyword, name or verse number. Works across Awadhi and Sanskrit original text, IAST transliteration, Hindi meaning and English translation.",
  keywords: [
    "search Ramcharitmanas verses",
    "Valmiki Ramayana shloka search",
    "Ramayana verse finder",
    "Ramcharitmanas doha by number",
  ],
  alternates: { canonical: "/search" },
};

export default function SearchLayout({ children }: { children: React.ReactNode }) {
  return children;
}
