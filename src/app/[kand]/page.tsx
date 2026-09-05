import { notFound } from "next/navigation";
import Link from "next/link";
import type { Metadata } from "next";
import { getKandBySlug, getTulsidasKand, getValmikiSargaNumbers } from "@/lib/data";
import ContinueReading from "@/components/navigation/ContinueReading";
import VersionSwitch from "@/components/navigation/VersionSwitch";
import JsonLd from "@/components/seo/JsonLd";
import {
  BASE_URL,
  breadcrumbJsonLd,
  buildKandFaq,
  dohaTitle,
  faqPageJsonLd,
  getKandSeo,
} from "@/lib/seo";
import { languageAlternates } from "@/lib/i18n";

interface KandPageProps {
  params: Promise<{ kand: string }>;
}

export async function generateStaticParams() {
  const { getKandManifest } = await import("@/lib/data");
  const manifest = await getKandManifest();
  return manifest.kands.map((k) => ({ kand: k.slug }));
}

export async function generateMetadata({ params }: KandPageProps): Promise<Metadata> {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);
  if (!kand) return {};

  const seo = getKandSeo(kandSlug);
  const title = `${kand.tulsidas.name} (${kand.tulsidas.nameOriginal}) — Full Text with Hindi & English Translation`;
  const description = `Read all ${kand.tulsidas.totalUnits} dohas of ${kand.tulsidas.name} from the Tulsidas Ramcharitmanas — original Awadhi text in Devanagari, Hindi meaning (अर्थ) and English translation for every verse, plus ${kand.valmiki.name} (${kand.valmiki.totalUnits} sargas) of the Valmiki Ramayana in Sanskrit.${seo ? ` ${seo.summary}` : ""}`;

  return {
    title,
    description: description.slice(0, 320),
    keywords: [
      `${kand.tulsidas.name} full text`,
      `${kand.tulsidas.name} in Hindi and English`,
      `${kand.tulsidas.name} paath`,
      `Ramcharitmanas ${kand.tulsidas.name}`,
      kand.tulsidas.nameOriginal,
      `${kand.valmiki.name} Valmiki Ramayana`,
      `${kand.valmiki.name} Sanskrit shloka with English translation`,
    ],
    alternates: { canonical: `/${kandSlug}`, languages: languageAlternates(`/${kandSlug}`) },
    openGraph: { type: "article", title, description: description.slice(0, 200), url: `/${kandSlug}` },
    twitter: { card: "summary_large_image", title, description: description.slice(0, 200) },
  };
}

export default async function KandPage({ params }: KandPageProps) {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);

  if (!kand) notFound();

  const [data, sargaNumbers] = await Promise.all([
    getTulsidasKand(kandSlug),
    getValmikiSargaNumbers(kandSlug),
  ]);

  if (!data) notFound();

  const seo = getKandSeo(kandSlug);
  const totalVerses = data.dohaGroups.reduce((sum, g) => sum + g.verses.length, 0);
  const faq = buildKandFaq(kand, data.dohaGroups.length, totalVerses);

  return (
    <div>
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "Home", path: "/" },
          { name: kand.tulsidas.name, path: `/${kandSlug}` },
        ])}
      />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "Chapter",
          name: kand.tulsidas.name,
          alternateName: kand.tulsidas.nameOriginal,
          position: kand.index,
          url: `${BASE_URL}/${kandSlug}`,
          inLanguage: ["awa", "hi", "en"],
          abstract: seo?.summary,
          isPartOf: {
            "@type": "Book",
            name: "Ramcharitmanas",
            alternateName: "श्रीरामचरितमानस",
            author: { "@type": "Person", name: "Goswami Tulsidas" },
            inLanguage: "awa",
            url: BASE_URL,
          },
          hasPart: {
            "@type": "Chapter",
            name: kand.valmiki.name,
            alternateName: kand.valmiki.nameOriginal,
            inLanguage: ["sa", "en"],
            isPartOf: {
              "@type": "Book",
              name: "Valmiki Ramayana",
              author: { "@type": "Person", name: "Maharshi Valmiki" },
              inLanguage: "sa",
            },
          },
        }}
      />
      <JsonLd data={faqPageJsonLd(faq)} />

      {/* One h1, always the Ramcharitmanas name — this is the page's search
          identity, and the version toggle below only swaps the listing. */}
      <div className="mb-8 animate-fade-in">
        <h1 className="text-3xl font-bold mb-2">
          {kand.tulsidas.name}{" "}
          <span className="font-devanagari font-normal text-[var(--muted)]">
            ({kand.tulsidas.nameOriginal})
          </span>
        </h1>
        <p className="text-[var(--muted)]">
          Ramcharitmanas verses with Hindi meaning &amp; English translation
        </p>
        <div className="flex items-center gap-4 mt-2">
          <p className="text-sm text-[var(--muted)]">
            {data.kand.totalDohas} Dohas · {totalVerses} verses
          </p>
          <ContinueReading kandSlug={kandSlug} />
        </div>
        {seo && (
          <p className="mt-4 text-sm leading-relaxed text-[var(--muted)] max-w-3xl">
            {seo.summary}
          </p>
        )}

        <Link
          href={`/${kandSlug}/paath`}
          className="inline-flex items-center gap-2 mt-4 px-4 py-2 rounded-lg text-sm font-medium bg-[var(--accent)] text-white hover:opacity-90 transition-opacity"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
          </svg>
          Read the full {kand.tulsidas.name} paath
        </Link>
      </div>

      <VersionSwitch
        tulsidas={
          <section aria-label={`${kand.tulsidas.name} dohas`}>
            <div className="grid gap-3 animate-stagger">
              {data.dohaGroups.map((group) => (
                <Link
                  key={group.dohaNumber}
                  href={`/${kandSlug}/doha/${group.dohaNumber}`}
                  className="card p-4 hover:border-[var(--accent)] transition-colors group"
                >
                  <div className="flex items-center justify-between gap-4">
                    <div className="min-w-0">
                      <h3 className="font-medium group-hover:text-[var(--accent)] transition-colors">
                        {dohaTitle(group.dohaNumber, group.label)}
                      </h3>
                      <p className="text-sm text-[var(--muted)] truncate font-devanagari mt-0.5">
                        {group.verses[0]?.original.split("\n")[0] ?? ""}
                      </p>
                      <p className="text-xs text-[var(--muted)] mt-0.5">
                        {group.verses.length} verse{group.verses.length > 1 ? "s" : ""}
                      </p>
                    </div>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-[var(--muted)] group-hover:text-[var(--accent)] flex-shrink-0">
                      <polyline points="9 18 15 12 9 6" />
                    </svg>
                  </div>
                </Link>
              ))}
            </div>

            {sargaNumbers.length > 0 && (
              <section className="mt-12 pt-8 border-t border-[var(--card-border)]">
                <h2 className="text-xl font-semibold mb-1">
                  {kand.valmiki.name} — Valmiki Ramayana (Sanskrit)
                </h2>
                <p className="text-sm text-[var(--muted)] mb-4">
                  The same Kand in Maharshi Valmiki&apos;s original Sanskrit, across{" "}
                  {kand.valmiki.totalUnits} sargas with English translation.
                </p>
                <div className="flex flex-wrap gap-2">
                  {sargaNumbers.map((n) => (
                    <Link
                      key={n}
                      href={`/${kandSlug}/sarga/${n}`}
                      className="text-sm px-3 py-1.5 rounded-md border border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors"
                    >
                      Sarga {n}
                    </Link>
                  ))}
                </div>
              </section>
            )}
          </section>
        }
        valmiki={
          <section aria-label={`${kand.valmiki.name} sargas`}>
            <h2 className="text-xl font-semibold mb-1">
              {kand.valmiki.name}{" "}
              <span className="font-devanagari font-normal text-[var(--muted)]">
                ({kand.valmiki.nameOriginal})
              </span>
            </h2>
            <p className="text-sm text-[var(--muted)] mb-4">
              {kand.valmiki.totalUnits} Sargas — Sanskrit shlokas with English translation
            </p>
            <div className="grid gap-3">
              {sargaNumbers.map((sargaNum) => (
                <Link
                  key={sargaNum}
                  href={`/${kandSlug}/sarga/${sargaNum}`}
                  className="card p-4 hover:border-[var(--accent)] transition-colors group"
                >
                  <div className="flex items-center justify-between">
                    <h3 className="font-medium group-hover:text-[var(--accent)] transition-colors">
                      Sarga {sargaNum}
                    </h3>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-[var(--muted)] group-hover:text-[var(--accent)]">
                      <polyline points="9 18 15 12 9 6" />
                    </svg>
                  </div>
                </Link>
              ))}
            </div>
          </section>
        }
      />

      {/* FAQ markup must be visible on the page for the rich result to qualify. */}
      <section className="mt-12 card p-6" aria-labelledby="kand-faq">
        <h2 id="kand-faq" className="text-xl font-semibold mb-4">
          Frequently asked about {kand.tulsidas.name}
        </h2>
        <div className="space-y-4">
          {faq.map((item) => (
            <div key={item.question}>
              <h3 className="font-medium">{item.question}</h3>
              <p className="text-sm text-[var(--muted)] mt-1">{item.answer}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
