"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { festivalOn, type Festival } from "@/lib/festivals";

/**
 * The card under the home page heading. Out of season it offers the
 * nine-day navahn parayan plan as what it is, a reading plan; during
 * Navratri it is the Navratri paath, and around Diwali it opens the
 * homecoming - Rama's return to Ayodhya at the start of Uttar Kand.
 *
 * The site is a static export, so the build cannot know the date; the
 * festival is chosen in the browser after mount, and the server-rendered
 * card is the out-of-season one so nothing flashes a wrong festival.
 */
type Copy = {
  title: string;
  sub?: string;
  text: string;
  cta: string;
  href: string;
};

const COPY: Record<"en" | "hi", Record<"default" | Festival["key"], Copy>> = {
  en: {
    default: {
      title: "Navahn Parayan",
      sub: "(नवाह्न पारायण)",
      text: "The complete Ramcharitmanas in nine days, following the traditional विश्राम pauses.",
      cta: "See the nine-day plan →",
      href: "/navahn-parayan",
    },
    navratri: {
      title: "Navratri Ramayana Paath",
      sub: "(नवाह्न पारायण)",
      text: "The complete Ramcharitmanas in nine days, following the traditional विश्राम pauses.",
      cta: "See the nine-day plan →",
      href: "/navahn-parayan",
    },
    diwali: {
      title: "Diwali: Rama returns to Ayodhya",
      sub: "(दीपावली)",
      text: "The homecoming after fourteen years — Bharat's vigil, the pushpak landing, Ayodhya lit for the night the festival remembers. Uttar Kand, dohas 1 to 12.",
      cta: "Read the homecoming →",
      href: "/uttar-kand/doha/1",
    },
  },
  hi: {
    default: {
      title: "नवाह्न पारायण",
      text: "नौ विश्रामों के अनुसार नौ दिनों में सम्पूर्ण मानस का पाठ।",
      cta: "नौ दिन की योजना देखें →",
      href: "/hi/navahn-parayan",
    },
    navratri: {
      title: "नवरात्रि रामायण पाठ",
      text: "नवाह्न पारायण — नौ विश्रामों के अनुसार नौ दिनों में सम्पूर्ण मानस का पाठ।",
      cta: "नौ दिन की योजना देखें →",
      href: "/hi/navahn-parayan",
    },
    diwali: {
      title: "दीपावली: श्रीराम का अयोध्या आगमन",
      text: "चौदह वर्ष बाद घर वापसी — भरत की प्रतीक्षा, पुष्पक का उतरना, दीपों से सजी अयोध्या। उत्तरकाण्ड, दोहा 1 से 12।",
      cta: "आगमन प्रसंग पढ़ें →",
      href: "/hi/uttar-kand/doha/1",
    },
  },
};

export default function SeasonalBanner({ lang }: { lang: "en" | "hi" }) {
  const [festival, setFestival] = useState<Festival["key"] | null>(null);
  useEffect(() => {
    setFestival(festivalOn(new Date()));
  }, []);

  const copy = COPY[lang][festival ?? "default"];

  return (
    <Link href={copy.href} className="block mb-10 group" prefetch={false}>
      <div className="card p-6 flex flex-wrap items-center justify-between gap-4 hover:border-[#fb923c] hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] cursor-pointer transition-all duration-300 ease-out">
        <div>
          <h2 className="text-lg font-semibold mb-1">
            {copy.title}
            {copy.sub && (
              <>
                {" "}
                <span className="font-devanagari font-normal text-[var(--muted)]">{copy.sub}</span>
              </>
            )}
          </h2>
          <p className="text-sm text-[var(--muted)]">{copy.text}</p>
        </div>
        <span className="px-4 py-2 rounded-lg text-sm font-medium bg-[var(--accent)] text-white group-hover:opacity-90 transition-opacity whitespace-nowrap">
          {copy.cta}
        </span>
      </div>
    </Link>
  );
}
