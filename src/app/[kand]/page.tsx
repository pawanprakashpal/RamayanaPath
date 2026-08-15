import { notFound } from "next/navigation";
import Link from "next/link";
import type { Metadata } from "next";
import { getKandBySlug, getTulsidasKand, getValmikiTotalSargas, getValmikiSargaNumbers } from "@/lib/data";
import { getServerVersion } from "@/lib/version";
import ContinueReading from "@/components/navigation/ContinueReading";
import JsonLd from "@/components/seo/JsonLd";
import {
  BASE_URL,
  breadcrumbJsonLd,
  buildKandFaq,
  dohaTitle,
  faqPageJsonLd,
  getKandSeo,
} from "@/lib/seo";

interface KandPageProps {
  params: Promise<{ kand: string }>;
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
    alternates: { canonical: `/${kandSlug}` },
    openGraph: { type: "article", title, description: description.slice(0, 200), url: `/${kandSlug}` },
    twitter: { card: "summary_large_image", title, description: description.slice(0, 200) },
  };
}

export default async function KandPage({ params }: KandPageProps) {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);

  if (!kand) notFound();

  const [version, data, sargaNumbers] = await Promise.all([
    getServerVersion(),
    getTulsidasKand(kandSlug),
    getValmikiSargaNumbers(kandSlug),
  ]);

  const seo = getKandSeo(kandSlug);
  const totalVerses = data?.dohaGroups.reduce((sum, g) => sum + g.verses.length, 0) ?? 0;
  const faq = buildKandFaq(kand, data?.dohaGroups.length ?? 0, totalVerses);

  // Rendered on both version branches so every Kand page carries the same
  // schema and so crawlers always reach both texts from here.
  const seoBlocks = (
    <>
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
    </>
  );

  // FAQ markup must be visible on the page for the rich result to qualify.
  const faqSection = (
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
  );

  if (version === "tulsidas") {
    if (!data) notFound();

    return (
      <div>
        {seoBlocks}
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
        </div>

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
                    {group.verses[0]?.original.split('\n')[0] ?? ""}
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

        <OtherVersionLinks
          heading={`${kand.valmiki.name} — Valmiki Ramayana (Sanskrit)`}
          blurb={`The same Kand in Maharshi Valmiki's original Sanskrit, across ${kand.valmiki.totalUnits} sargas with English translation.`}
          links={sargaNumbers.map((n) => ({
            href: `/${kandSlug}/sarga/${n}`,
            label: `Sarga ${n}`,
          }))}
        />

        {faqSection}
      </div>
    );
  }

  // Valmiki version
  const totalSargas = await getValmikiTotalSargas(kandSlug);

  return (
    <div>
      {seoBlocks}
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">
          {kand.valmiki.name}{" "}
          <span className="font-devanagari font-normal text-[var(--muted)]">
            ({kand.valmiki.nameOriginal})
          </span>
        </h1>
        <p className="text-[var(--muted)]">
          Valmiki Ramayana — Sanskrit shlokas with English translation
        </p>
        <p className="text-sm text-[var(--muted)] mt-2">{totalSargas} Sargas</p>
        {seo && (
          <p className="mt-4 text-sm leading-relaxed text-[var(--muted)] max-w-3xl">
            {seo.summary}
          </p>
        )}
      </div>

      <div className="grid gap-3">
        {Array.from({ length: totalSargas }, (_, i) => i + 1).map((sargaNum) => (
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

      {data && (
        <OtherVersionLinks
          heading={`${kand.tulsidas.name} — Tulsidas Ramcharitmanas (Awadhi)`}
          blurb={`The same Kand in Goswami Tulsidas's Awadhi retelling, across ${data.kand.totalDohas} dohas with Hindi meaning and English translation.`}
          links={data.dohaGroups.map((g) => ({
            href: `/${kandSlug}/doha/${g.dohaNumber}`,
            label: dohaTitle(g.dohaNumber, g.label),
          }))}
        />
      )}

      {faqSection}
    </div>
  );
}

/**
 * Compact link grid to the other recension. Without it the inactive version's
 * pages have no inbound internal links at all — the version toggle is a cookie,
 * so a crawler only ever sees one of the two listings.
 */
function OtherVersionLinks({
  heading,
  blurb,
  links,
}: {
  heading: string;
  blurb: string;
  links: { href: string; label: string }[];
}) {
  if (links.length === 0) return null;

  // Cap the grid so a 362-doha Kand doesn't add thousands of anchors; the
  // primary listing above already links every unit of the active version.
  const MAX_LINKS = 140;
  const shown = links.slice(0, MAX_LINKS);

  return (
    <section className="mt-12 pt-8 border-t border-[var(--card-border)]" aria-labelledby="other-version">
      <h2 id="other-version" className="text-xl font-semibold mb-1">
        {heading}
      </h2>
      <p className="text-sm text-[var(--muted)] mb-4">{blurb}</p>
      <div className="flex flex-wrap gap-2">
        {shown.map((link) => (
          <Link
            key={link.href}
            href={link.href}
            className="text-sm px-3 py-1.5 rounded-md border border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors"
          >
            {link.label}
          </Link>
        ))}
        {links.length > shown.length && (
          <span className="text-sm px-3 py-1.5 text-[var(--muted)]">
            +{links.length - shown.length} more
          </span>
        )}
      </div>
    </section>
  );
}
