import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getDohaGroup, getTulsidasKand, getKandBySlug } from "@/lib/data";
import VerseCard from "@/components/verse/VerseCard";
import PrevNextNav from "@/components/navigation/PrevNextNav";
import JsonLd from "@/components/seo/JsonLd";
import { BASE_URL, breadcrumbJsonLd, dohaTitle, excerpt } from "@/lib/seo";
import { languageAlternates } from "@/lib/i18n";
import TtsProvider from "@/components/verse/TtsProvider";
import TtsControls from "@/components/verse/TtsControls";
import ShareButton from "@/components/verse/ShareButton";
import BookmarkButton from "@/components/verse/BookmarkButton";
import { bookmarkId } from "@/lib/bookmarks";
import KeyboardNav from "@/components/navigation/KeyboardNav";
import ReadingProgress from "@/components/verse/ReadingProgress";

interface DohaPageProps {
  params: Promise<{ kand: string; number: string }>;
}

export async function generateMetadata({ params }: DohaPageProps): Promise<Metadata> {
  const { kand: kandSlug, number } = await params;
  const dohaNumber = parseInt(number, 10);
  const kand = await getKandBySlug(kandSlug);
  const group = await getDohaGroup(kandSlug, dohaNumber);
  if (!kand || !group) return {};

  const label = dohaTitle(dohaNumber, group.label);
  const verseCount = group.verses.length;
  const firstVerse = group.verses[0];
  const path = `/${kandSlug}/doha/${dohaNumber}`;

  // Devanagari in the title captures Hindi-script queries; the trailing
  // keywords capture "meaning" / "translation" intent.
  const title = `${kand.tulsidas.name} ${label} (${kand.tulsidas.nameOriginal}) — Meaning & English Translation`;
  const description = firstVerse
    ? `${excerpt(firstVerse.original, 90)} — ${label} of ${kand.tulsidas.name}, Ramcharitmanas. ${verseCount} verse${verseCount > 1 ? "s" : ""} with original Awadhi text, Hindi meaning (अर्थ) and English translation.`
    : `${label} of ${kand.tulsidas.name} (${kand.tulsidas.nameOriginal}) — Ramcharitmanas verses with Hindi meaning and English translation.`;

  return {
    title,
    description,
    keywords: [
      `${kand.tulsidas.name} ${label}`,
      `${kand.tulsidas.name} ${label} meaning`,
      `Ramcharitmanas ${label}`,
      `${kand.tulsidas.nameOriginal} ${label}`,
      "Ramcharitmanas English translation",
      "Awadhi text with Hindi meaning",
    ],
    alternates: { canonical: path, languages: languageAlternates(path) },
    openGraph: {
      type: "article",
      title,
      description,
      url: path,
    },
    twitter: { card: "summary_large_image", title, description },
  };
}

export async function generateStaticParams() {
  const { getKandManifest } = await import("@/lib/data");
  const manifest = await getKandManifest();
  const params: { kand: string; number: string }[] = [];

  for (const kand of manifest.kands) {
    if (!kand.tulsidas.available) continue;
    const data = await getTulsidasKand(kand.slug);
    if (!data) continue;
    for (const group of data.dohaGroups) {
      params.push({ kand: kand.slug, number: String(group.dohaNumber) });
    }
  }

  return params;
}

export default async function DohaPage({ params }: DohaPageProps) {
  const { kand: kandSlug, number } = await params;
  const dohaNumber = parseInt(number, 10);

  if (isNaN(dohaNumber)) notFound();

  const [group, data, kand] = await Promise.all([
    getDohaGroup(kandSlug, dohaNumber),
    getTulsidasKand(kandSlug),
    getKandBySlug(kandSlug),
  ]);

  if (!group || !data || !kand) notFound();

  const dohaNumbers = data.dohaGroups.map((g) => g.dohaNumber);
  const currentIndex = dohaNumbers.indexOf(dohaNumber);
  const prevDoha = currentIndex > 0 ? dohaNumbers[currentIndex - 1] : undefined;
  const nextDoha = currentIndex < dohaNumbers.length - 1 ? dohaNumbers[currentIndex + 1] : undefined;

  const pageTitle = dohaTitle(dohaNumber, group.label);
  const pageUrl = `${BASE_URL}/${kandSlug}/doha/${dohaNumber}`;

  return (
    <div>
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "Home", path: "/" },
          { name: kand.tulsidas.name, path: `/${kandSlug}` },
          { name: pageTitle, path: `/${kandSlug}/doha/${dohaNumber}` },
        ])}
      />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "CreativeWork",
          name: `${kand.tulsidas.name} ${pageTitle} — Ramcharitmanas`,
          alternateName: `${kand.tulsidas.nameOriginal} ${pageTitle}`,
          author: { "@type": "Person", name: "Goswami Tulsidas" },
          inLanguage: ["awa", "hi", "en"],
          text: group.verses.map((v) => v.original).join("\n"),
          position: dohaNumber,
          isPartOf: {
            "@type": "Chapter",
            name: kand.tulsidas.name,
            alternateName: kand.tulsidas.nameOriginal,
            position: kand.index,
            url: `${BASE_URL}/${kandSlug}`,
            isPartOf: {
              "@type": "Book",
              name: "Ramcharitmanas",
              alternateName: "श्रीरामचरितमानस",
              author: { "@type": "Person", name: "Goswami Tulsidas" },
              inLanguage: "awa",
              url: BASE_URL,
            },
          },
          url: pageUrl,
        }}
      />

      <TtsProvider>
        {/* Page header */}
        <div className="mb-8">
          <div className="flex items-start justify-between">
            <div>
              <p className="text-sm text-[var(--muted)] mb-1">{kand.tulsidas.name}</p>
              <h1 className="text-2xl font-bold">
                {pageTitle}{" "}
                <span className="font-devanagari font-normal text-[var(--muted)]">
                  ({kand.tulsidas.nameOriginal})
                </span>
              </h1>
            </div>
            <div className="flex items-center gap-2">
              <BookmarkButton
                id={bookmarkId("tulsidas", kandSlug, "doha", dohaNumber)}
                version="tulsidas"
                kandSlug={kandSlug}
                label={`${kand.tulsidas.name} — ${pageTitle}`}
                href={`/${kandSlug}/doha/${dohaNumber}`}
              />
              <ShareButton title={`${pageTitle} — ${kand.tulsidas.name}`} url={`/${kandSlug}/doha/${dohaNumber}`} />
            </div>
          </div>
          <div className="flex items-center justify-between mt-2">
            <p className="text-sm text-[var(--muted)]">
              {group.verses.length} verse{group.verses.length > 1 ? "s" : ""}
            </p>
            <TtsControls verses={group.verses.map((v) => ({
              id: v.id,
              original: v.original,
              hindiTranslation: v.hindiTranslation,
              translation: v.translation,
            }))} />
          </div>
        </div>

        {/* Verses */}
        <div className="space-y-4 animate-stagger">
          {group.verses.map((verse, index) => (
            <VerseCard
              key={verse.id}
              verse={verse}
              verseLabel={`${index + 1} of ${group.verses.length}`}
            />
          ))}
        </div>
      </TtsProvider>

      {/* Navigation */}
      <PrevNextNav
        prevHref={prevDoha !== undefined ? `/${kandSlug}/doha/${prevDoha}` : undefined}
        nextHref={nextDoha !== undefined ? `/${kandSlug}/doha/${nextDoha}` : undefined}
        prevLabel={prevDoha !== undefined ? `Doha ${prevDoha}` : undefined}
        nextLabel={nextDoha !== undefined ? `Doha ${nextDoha}` : undefined}
        kandHref={`/${kandSlug}`}
        kandLabel={`All ${kand.tulsidas.name} Dohas`}
      />
      <KeyboardNav
        prevHref={prevDoha !== undefined ? `/${kandSlug}/doha/${prevDoha}` : undefined}
        nextHref={nextDoha !== undefined ? `/${kandSlug}/doha/${nextDoha}` : undefined}
      />
      <ReadingProgress kandSlug={kandSlug} dohaNumber={dohaNumber} />
    </div>
  );
}
