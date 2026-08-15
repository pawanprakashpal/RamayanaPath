import { notFound } from "next/navigation";
import Link from "next/link";
import type { Metadata } from "next";
import { getKandBySlug, getTulsidasKand } from "@/lib/data";
import { BASE_URL, breadcrumbJsonLd, dohaTitle, getKandSeo } from "@/lib/seo";
import { languageAlternates } from "@/lib/i18n";
import JsonLd from "@/components/seo/JsonLd";
import TtsProvider from "@/components/verse/TtsProvider";
import PaathBar from "@/components/paath/PaathBar";
import PaathVerse from "@/components/paath/PaathVerse";

interface PaathPageProps {
  params: Promise<{ kand: string }>;
}

/**
 * Rough recitation time at ~2.5 verses a minute, which puts Sundar Kand a
 * little over two hours — in line with how long a paath actually takes.
 */
function formatRecitationTime(verseCount: number): string {
  const minutes = Math.round(verseCount / 2.5);
  if (minutes < 90) return `${minutes} minutes`;
  const hours = Math.round(minutes / 30) / 2;
  return `${hours} hours`;
}

export async function generateStaticParams() {
  const { getKandManifest } = await import("@/lib/data");
  const manifest = await getKandManifest();
  return manifest.kands
    .filter((k) => k.tulsidas.available)
    .map((k) => ({ kand: k.slug }));
}

export async function generateMetadata({ params }: PaathPageProps): Promise<Metadata> {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);
  const data = await getTulsidasKand(kandSlug);
  if (!kand || !data) return {};

  const name = kand.tulsidas.name;
  const verseCount = data.dohaGroups.reduce((sum, g) => sum + g.verses.length, 0);
  const path = `/${kandSlug}/paath`;

  const seo = getKandSeo(kandSlug);
  const title = `${name} Paath (${kand.tulsidas.nameOriginal}) — Full Text in One Page`;
  const description = `Complete ${name} paath — all ${kand.tulsidas.totalUnits} dohas and ${verseCount} verses on a single page in the original Awadhi, with Hindi meaning and English translation on tap.${
    seo?.paathNote ? " Traditionally recited on Tuesdays and Saturdays." : ""
  } Continuous audio recitation and saved reading position.`;

  return {
    title,
    description,
    keywords: [
      `${name} paath`,
      `${name} full text`,
      `${name} complete`,
      `${kand.tulsidas.nameOriginal} पाठ`,
      `${name} paath in Hindi`,
      `read ${name} online`,
      "Ramcharitmanas paath",
    ],
    alternates: { canonical: path, languages: languageAlternates(path) },
    openGraph: { type: "article", title, description, url: path },
    twitter: { card: "summary_large_image", title, description },
  };
}

export default async function PaathPage({ params }: PaathPageProps) {
  const { kand: kandSlug } = await params;
  const [kand, data] = await Promise.all([
    getKandBySlug(kandSlug),
    getTulsidasKand(kandSlug),
  ]);

  if (!kand || !data) notFound();

  const seo = getKandSeo(kandSlug);
  const dohaNumbers = data.dohaGroups.map((g) => g.dohaNumber);
  const verseCount = data.dohaGroups.reduce((sum, g) => sum + g.verses.length, 0);

  // Original text only — see the note on PaathBar's ttsVerses prop.
  const ttsVerses = data.dohaGroups.flatMap((g) =>
    g.verses.map((v) => ({ id: v.id, original: v.original, translation: "" }))
  );

  return (
    <div>
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "Home", path: "/" },
          { name: kand.tulsidas.name, path: `/${kandSlug}` },
          { name: `${kand.tulsidas.name} Paath`, path: `/${kandSlug}/paath` },
        ])}
      />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "Chapter",
          name: `${kand.tulsidas.name} Paath — complete text`,
          alternateName: kand.tulsidas.nameOriginal,
          position: kand.index,
          url: `${BASE_URL}/${kandSlug}/paath`,
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
        }}
      />

      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">
          {kand.tulsidas.name} Paath{" "}
          <span className="font-devanagari font-normal text-[var(--muted)]">
            ({kand.tulsidas.nameOriginal})
          </span>
        </h1>
        <p className="text-[var(--muted)]">
          Complete text — {kand.tulsidas.totalUnits} dohas, {verseCount} verses, one page.
          About {formatRecitationTime(verseCount)} to recite. Tap any verse for its Hindi
          meaning and English translation.
        </p>
        {seo?.paathNote && (
          <p className="mt-4 card p-4 text-sm leading-relaxed max-w-3xl">{seo.paathNote}</p>
        )}
        {seo && (
          <p className="mt-3 text-sm leading-relaxed text-[var(--muted)] max-w-3xl">
            {seo.summary}
          </p>
        )}
        <p className="mt-3 text-sm">
          <Link href={`/${kandSlug}`} className="text-[var(--accent)] hover:underline">
            Read doha by doha instead →
          </Link>
        </p>
      </div>

      <TtsProvider>
        <PaathBar kandSlug={kandSlug} dohaNumbers={dohaNumbers} ttsVerses={ttsVerses} />

        <div className="mt-6 space-y-8">
          {data.dohaGroups.map((group, index) => (
            <section
              key={group.dohaNumber}
              id={`doha-${group.dohaNumber}`}
              data-doha-index={index}
              className="scroll-mt-32"
            >
              <h2 className="text-sm font-semibold text-[var(--muted)] uppercase tracking-wider mb-3">
                {dohaTitle(group.dohaNumber, group.label)}
              </h2>
              <div className="space-y-3">
                {group.verses.map((verse) => (
                  <PaathVerse
                    key={verse.id}
                    verse={verse}
                    kandSlug={kandSlug}
                    dohaNumber={group.dohaNumber}
                  />
                ))}
              </div>
            </section>
          ))}
        </div>
      </TtsProvider>
    </div>
  );
}
