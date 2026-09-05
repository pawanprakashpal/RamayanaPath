import Link from "next/link";
import type { Metadata } from "next";
import JsonLd from "@/components/seo/JsonLd";
import ParayanPlan from "@/components/parayan/ParayanPlan";
import { BASE_URL, breadcrumbJsonLd, faqPageJsonLd } from "@/lib/seo";
import { languageAlternates } from "@/lib/i18n";

const PATH = "/navahn-parayan";

const TITLE = "Navratri Ramayana Paath — the Nine-Day Navahn Parayan";
const DESCRIPTION =
  "The traditional nine-day division of the Ramcharitmanas, read one section per night of Navratri. Each day's विश्राम pause with its exact doha range, linked to the full text with Hindi meaning and English translation.";

const FAQ = [
  {
    question: "What is navahn parayan?",
    answer:
      "Navahn parayan (नवाह्न पारायण) is the practice of reciting the complete Ramcharitmanas over nine days, following the nine traditional विश्राम (pause) points printed in the text. It is most commonly undertaken during the nine nights of Navratri.",
  },
  {
    question: "How is the Ramcharitmanas divided over the nine days?",
    answer:
      "Days 1 to 3 cover Bal Kand, days 4 to 6 run from Ayodhya Kand into the opening of Aranya Kand, day 7 covers the rest of Aranya Kand and all of Kishkindha Kand, day 8 covers Sundar Kand and Lanka Kand, and day 9 covers Uttar Kand to the close of the work.",
  },
  {
    question: "Can I do the paath in thirty days instead?",
    answer:
      "Yes. The Ramcharitmanas also carries a मासपारायण division of thirty विश्राम points for reading across a month. The nine-day division is the one used during Navratri.",
  },
  {
    question: "Do I need to read at a fixed time each day?",
    answer:
      "There is no fixed rule in the text. The common practice is to keep the same time each day for the nine days, and to complete each day's section in one sitting rather than breaking it up.",
  },
];

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  keywords: [
    "navahn parayan",
    "Navratri Ramayana paath",
    "nine day Ramcharitmanas reading",
    "नवाह्न पारायण",
    "नवरात्रि रामायण पाठ",
    "Ramcharitmanas vishram",
    "Ramcharitmanas nine day plan",
  ],
  alternates: { canonical: PATH, languages: languageAlternates(PATH) },
  openGraph: { type: "article", title: TITLE, description: DESCRIPTION, url: PATH },
  twitter: { card: "summary_large_image", title: TITLE, description: DESCRIPTION },
};

export default function NavahnParayanPage() {
  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-12">
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "Home", path: "/" },
          { name: "Navahn Parayan", path: PATH },
        ])}
      />
      <JsonLd data={faqPageJsonLd(FAQ)} />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "HowTo",
          name: TITLE,
          description: DESCRIPTION,
          url: `${BASE_URL}${PATH}`,
          inLanguage: "en",
          totalTime: "P9D",
          step: [1, 2, 3, 4, 5, 6, 7, 8, 9].map((n) => ({
            "@type": "HowToStep",
            position: n,
            name: `Day ${n}`,
            url: `${BASE_URL}${PATH}#day-${n}`,
          })),
        }}
      />

      <h1 className="text-3xl sm:text-4xl font-bold mb-3">
        Navratri Ramayana Paath{" "}
        <span className="font-devanagari font-normal text-[var(--muted)]">
          (नवाह्न पारायण)
        </span>
      </h1>
      <p className="text-lg text-[var(--muted)] mb-4">
        The complete Ramcharitmanas in nine days — one section for each night of Navratri.
      </p>

      <div className="card p-5 mb-8">
        <p className="text-sm leading-relaxed text-[var(--muted)]">
          The Ramcharitmanas carries its own reading divisions. Alongside the thirty-point
          मासपारायण for reading across a month, it marks nine विश्राम — pauses — that split
          the text into nine days. Those nine are what a Navratri paath follows, and they are
          the divisions set out below, each linked to the full text with Hindi meaning and
          English translation.
        </p>
      </div>

      <ParayanPlan lang="en" />

      <section className="mt-12 card p-6" aria-labelledby="parayan-faq">
        <h2 id="parayan-faq" className="text-xl font-semibold mb-4">
          Frequently asked
        </h2>
        <div className="space-y-4">
          {FAQ.map((item) => (
            <div key={item.question}>
              <h3 className="font-medium">{item.question}</h3>
              <p className="text-sm text-[var(--muted)] mt-1">{item.answer}</p>
            </div>
          ))}
        </div>
      </section>

      <p className="mt-8 text-sm">
        <Link href="/hi/navahn-parayan" className="text-[var(--accent)] hover:underline">
          हिन्दी में पढ़ें →
        </Link>
      </p>
    </div>
  );
}
