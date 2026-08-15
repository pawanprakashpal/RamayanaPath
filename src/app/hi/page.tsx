import Link from "next/link";
import type { Metadata } from "next";
import { getAvailableKands } from "@/lib/data";
import { getKandSeo } from "@/lib/seo";
import { languageAlternates, t } from "@/lib/i18n";

const strings = t("hi");

export const metadata: Metadata = {
  title: "श्रीरामचरितमानस एवं वाल्मीकि रामायण — हिन्दी अर्थ सहित ऑनलाइन पढ़ें",
  description: strings.siteDescription,
  keywords: [
    "श्रीरामचरितमानस",
    "रामचरितमानस हिन्दी अर्थ सहित",
    "सुन्दरकाण्ड पाठ",
    "रामायण ऑनलाइन पढ़ें",
    "वाल्मीकि रामायण हिन्दी",
    "तुलसीदास रामचरितमानस",
  ],
  alternates: {
    canonical: "/hi",
    languages: languageAlternates("/"),
  },
  openGraph: {
    title: "श्रीरामचरितमानस एवं वाल्मीकि रामायण — हिन्दी अर्थ सहित",
    description: strings.siteDescription,
    url: "/hi",
    locale: "hi_IN",
  },
};

export default async function HindiHomePage() {
  const kands = await getAvailableKands();

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12">
      <div className="text-center mb-12">
        <div className="flex justify-center mb-4">
          <div className="w-24 h-24 rounded-full bg-[#f97316] p-4 flex items-center justify-center animate-hero-icon">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src="/ram-icon.png" alt="धनुष-बाण सहित श्रीराम" width="64" height="64" className="w-16 h-16" />
          </div>
        </div>
        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold mb-4 animate-hero-title">
          ॥ श्रीरामचरितमानस ॥
        </h1>
        <p className="text-lg sm:text-xl text-[var(--muted)] max-w-2xl mx-auto mb-4 animate-hero-subtitle">
          {strings.tagline}
        </p>
        <p className="text-sm text-[var(--muted)] mb-6 animate-hero-subtitle">
          <span className="font-semibold text-[var(--foreground)]">6,072</span> पद,{" "}
          <span className="font-semibold text-[var(--foreground)]">7 काण्ड</span> — हिन्दी अर्थ
          और अंग्रेज़ी अनुवाद सहित
        </p>
        <p className="text-base text-[var(--muted)] animate-hero-verse">
          मंगल भवन अमंगल हारी। द्रवउ सो दसरथ अजिर बिहारी॥
        </p>
        <p className="mt-4">
          <Link href="/" className="text-sm text-[var(--accent)] hover:underline">
            Read in English →
          </Link>
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 animate-stagger">
        {kands.map((kand) => {
          const seo = getKandSeo(kand.slug);
          return (
            <div key={kand.slug} className="h-full flex flex-col">
              <Link href={`/hi/${kand.slug}`} className="flex-1">
                <div className="card p-6 h-full flex flex-col hover:border-[#fb923c] hover:shadow-xl hover:-translate-y-1 transition-all duration-300">
                  <h2 className="text-xl font-semibold mb-1">{kand.tulsidas.nameOriginal}</h2>
                  <p className="text-[var(--muted)] text-sm mb-3">{kand.tulsidas.name}</p>
                  <p className="text-sm text-[var(--muted)] mb-4 flex-1 line-clamp-4">
                    {seo?.summaryHi}
                  </p>
                  <div className="flex gap-4 text-xs text-[var(--muted)] border-t border-[var(--card-border)] pt-3 mt-auto">
                    <span>
                      {kand.tulsidas.totalUnits} {strings.dohas}
                    </span>
                    <span>
                      {kand.valmiki.totalUnits} {strings.sargas}
                    </span>
                  </div>
                </div>
              </Link>
              {kand.tulsidas.available && (
                <Link
                  href={`/hi/${kand.slug}/paath`}
                  className="mt-2 text-center text-xs px-3 py-2 rounded-lg border border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors"
                >
                  {strings.readPaath} →
                </Link>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
