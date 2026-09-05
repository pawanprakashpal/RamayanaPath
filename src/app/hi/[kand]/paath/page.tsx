import { notFound } from "next/navigation";
import Link from "next/link";
import type { Metadata } from "next";
import { getKandBySlug, getTulsidasKand } from "@/lib/data";
import { BASE_URL, breadcrumbJsonLd, getKandSeo } from "@/lib/seo";
import { dohaTitleHi, languageAlternates, t } from "@/lib/i18n";
import JsonLd from "@/components/seo/JsonLd";
import TtsProvider from "@/components/verse/TtsProvider";
import PaathBar from "@/components/paath/PaathBar";
import PaathVerse from "@/components/paath/PaathVerse";

interface Props {
  params: Promise<{ kand: string }>;
}

const strings = t("hi");

function recitationTime(verseCount: number): string {
  const minutes = Math.round(verseCount / 2.5);
  if (minutes < 90) return strings.minutes(minutes);
  return strings.hours(Math.round(minutes / 30) / 2);
}

export async function generateStaticParams() {
  const { getKandManifest } = await import("@/lib/data");
  const manifest = await getKandManifest();
  return manifest.kands.filter((k) => k.tulsidas.available).map((k) => ({ kand: k.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);
  const data = await getTulsidasKand(kandSlug);
  if (!kand || !data) return {};

  const seo = getKandSeo(kandSlug);
  const name = kand.tulsidas.nameOriginal;
  const verseCount = data.dohaGroups.reduce((sum, g) => sum + g.verses.length, 0);

  const title = `${name} पाठ — सम्पूर्ण पाठ एक ही पृष्ठ पर, अर्थ सहित`;
  const description = `सम्पूर्ण ${name} पाठ — सभी ${kand.tulsidas.totalUnits} दोहे और ${verseCount} पद एक ही पृष्ठ पर, मूल अवधी में। किसी भी पद पर टैप करके हिन्दी अर्थ देखें।${
    seo?.paathNoteHi ? " प्रायः मंगलवार और शनिवार को पाठ किया जाता है।" : ""
  }`;

  return {
    title,
    description,
    keywords: [
      `${name} पाठ`,
      `${name} सम्पूर्ण पाठ`,
      `${name} अर्थ सहित`,
      `${kand.tulsidas.name} paath in Hindi`,
      "रामचरितमानस पाठ",
    ],
    alternates: {
      canonical: `/hi/${kandSlug}/paath`,
      languages: languageAlternates(`/${kandSlug}/paath`),
    },
    openGraph: { type: "article", title, description, url: `/hi/${kandSlug}/paath`, locale: "hi_IN" },
  };
}

export default async function HindiPaathPage({ params }: Props) {
  const { kand: kandSlug } = await params;
  const [kand, data] = await Promise.all([getKandBySlug(kandSlug), getTulsidasKand(kandSlug)]);

  if (!kand || !data) notFound();

  const seo = getKandSeo(kandSlug);
  const dohaNumbers = data.dohaGroups.map((g) => g.dohaNumber);
  const verseCount = data.dohaGroups.reduce((sum, g) => sum + g.verses.length, 0);
  const ttsVerses = data.dohaGroups.flatMap((g) =>
    g.verses.map((v) => ({ id: v.id, original: v.original, translation: "" }))
  );

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-8">
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "मुख्य पृष्ठ", path: "/hi" },
          { name: kand.tulsidas.nameOriginal, path: `/hi/${kandSlug}` },
          { name: `${kand.tulsidas.nameOriginal} पाठ`, path: `/hi/${kandSlug}/paath` },
        ])}
      />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "Chapter",
          name: `${kand.tulsidas.nameOriginal} — सम्पूर्ण पाठ`,
          position: kand.index,
          url: `${BASE_URL}/hi/${kandSlug}/paath`,
          inLanguage: ["awa", "hi"],
          abstract: seo?.summaryHi,
          isPartOf: {
            "@type": "Book",
            name: "श्रीरामचरितमानस",
            author: { "@type": "Person", name: "गोस्वामी तुलसीदास" },
            inLanguage: "awa",
            url: BASE_URL,
          },
        }}
      />

      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">{strings.paathHeading(kand.tulsidas.nameOriginal)}</h1>
        <p className="text-[var(--muted)]">
          {strings.completeText(kand.tulsidas.totalUnits, verseCount)}{" "}
          {strings.reciteTime(recitationTime(verseCount))} {strings.tapForMeaning}
        </p>
        {seo?.paathNoteHi && (
          <p className="mt-4 card p-4 text-sm leading-relaxed">{seo.paathNoteHi}</p>
        )}
        <div className="flex flex-wrap gap-4 mt-3 text-sm">
          <Link href={`/hi/${kandSlug}`} className="text-[var(--accent)] hover:underline">
            {strings.readDohaByDoha}
          </Link>
          <Link href={`/${kandSlug}/paath`} className="text-[var(--accent)] hover:underline">
            Read in English →
          </Link>
        </div>
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
                {dohaTitleHi(group.dohaNumber, group.label)}
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
