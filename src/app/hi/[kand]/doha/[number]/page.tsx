import { notFound } from "next/navigation";
import Link from "next/link";
import type { Metadata } from "next";
import { getDohaGroup, getTulsidasKand, getKandBySlug } from "@/lib/data";
import { BASE_URL, breadcrumbJsonLd, excerpt } from "@/lib/seo";
import { dohaTitleHi, languageAlternates } from "@/lib/i18n";
import JsonLd from "@/components/seo/JsonLd";
import HindiVerseCard from "@/components/verse/HindiVerseCard";
import PrevNextNav from "@/components/navigation/PrevNextNav";
import TtsProvider from "@/components/verse/TtsProvider";
import TtsControls from "@/components/verse/TtsControls";
import ShareButton from "@/components/verse/ShareButton";
import BookmarkButton from "@/components/verse/BookmarkButton";
import KeyboardNav from "@/components/navigation/KeyboardNav";
import ReadingProgress from "@/components/verse/ReadingProgress";
import { bookmarkId } from "@/lib/bookmarks";

interface Props {
  params: Promise<{ kand: string; number: string }>;
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

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { kand: kandSlug, number } = await params;
  const dohaNumber = parseInt(number, 10);
  const kand = await getKandBySlug(kandSlug);
  const group = await getDohaGroup(kandSlug, dohaNumber);
  if (!kand || !group) return {};

  const label = dohaTitleHi(dohaNumber, group.label);
  const name = kand.tulsidas.nameOriginal;
  const firstVerse = group.verses[0];
  const path = `/${kandSlug}/doha/${dohaNumber}`;

  const title = `${name} ${label} — अर्थ सहित`;
  const description = firstVerse
    ? `${excerpt(firstVerse.original, 90)} — ${name} ${label}, श्रीरामचरितमानस। ${group.verses.length} पद, मूल अवधी पाठ, हिन्दी अर्थ और अंग्रेज़ी अनुवाद सहित।`
    : `${name} ${label} — श्रीरामचरितमानस, हिन्दी अर्थ सहित।`;

  return {
    title,
    description,
    keywords: [
      `${name} ${label}`,
      `${name} ${label} अर्थ`,
      `रामचरितमानस ${label}`,
      `${label} का अर्थ`,
      "रामचरितमानस अर्थ सहित",
    ],
    alternates: {
      canonical: `/hi${path}`,
      languages: languageAlternates(path),
    },
    openGraph: { type: "article", title, description, url: `/hi${path}`, locale: "hi_IN" },
  };
}

export default async function HindiDohaPage({ params }: Props) {
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

  const label = dohaTitleHi(dohaNumber, group.label);
  const name = kand.tulsidas.nameOriginal;

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-8">
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "मुख्य पृष्ठ", path: "/hi" },
          { name, path: `/hi/${kandSlug}` },
          { name: label, path: `/hi/${kandSlug}/doha/${dohaNumber}` },
        ])}
      />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "CreativeWork",
          name: `${name} ${label} — श्रीरामचरितमानस`,
          author: { "@type": "Person", name: "गोस्वामी तुलसीदास" },
          inLanguage: ["awa", "hi"],
          text: group.verses.map((v) => v.original).join("\n"),
          position: dohaNumber,
          isPartOf: {
            "@type": "Chapter",
            name,
            position: kand.index,
            url: `${BASE_URL}/hi/${kandSlug}`,
            isPartOf: {
              "@type": "Book",
              name: "श्रीरामचरितमानस",
              author: { "@type": "Person", name: "गोस्वामी तुलसीदास" },
              inLanguage: "awa",
              url: BASE_URL,
            },
          },
          url: `${BASE_URL}/hi/${kandSlug}/doha/${dohaNumber}`,
        }}
      />

      <TtsProvider>
        <div className="mb-8">
          <div className="flex items-start justify-between gap-4">
            <div>
              <p className="text-sm text-[var(--muted)] mb-1">{name}</p>
              <h1 className="text-2xl font-bold">{label}</h1>
            </div>
            <div className="flex items-center gap-2">
              <BookmarkButton
                id={bookmarkId("tulsidas", kandSlug, "doha", dohaNumber)}
                version="tulsidas"
                kandSlug={kandSlug}
                label={`${name} — ${label}`}
                href={`/hi/${kandSlug}/doha/${dohaNumber}`}
              />
              <ShareButton
                title={`${name} ${label}`}
                url={`/hi/${kandSlug}/doha/${dohaNumber}`}
              />
            </div>
          </div>
          <div className="flex items-center justify-between mt-2">
            <p className="text-sm text-[var(--muted)]">{group.verses.length} पद</p>
            <TtsControls
              verses={group.verses.map((v) => ({
                id: v.id,
                original: v.original,
                hindiTranslation: v.hindiTranslation,
                translation: v.translation,
              }))}
            />
          </div>
        </div>

        <div className="space-y-4 animate-stagger">
          {group.verses.map((verse, index) => (
            <HindiVerseCard
              key={verse.id}
              verse={verse}
              verseLabel={`${index + 1} / ${group.verses.length}`}
            />
          ))}
        </div>
      </TtsProvider>

      <PrevNextNav
        prevHref={prevDoha !== undefined ? `/hi/${kandSlug}/doha/${prevDoha}` : undefined}
        nextHref={nextDoha !== undefined ? `/hi/${kandSlug}/doha/${nextDoha}` : undefined}
        prevLabel={prevDoha !== undefined ? dohaTitleHi(prevDoha) : undefined}
        nextLabel={nextDoha !== undefined ? dohaTitleHi(nextDoha) : undefined}
        kandHref={`/hi/${kandSlug}`}
        kandLabel={`${name} — सभी दोहे`}
      />
      <KeyboardNav
        prevHref={prevDoha !== undefined ? `/hi/${kandSlug}/doha/${prevDoha}` : undefined}
        nextHref={nextDoha !== undefined ? `/hi/${kandSlug}/doha/${nextDoha}` : undefined}
      />
      <ReadingProgress kandSlug={kandSlug} dohaNumber={dohaNumber} />

      <p className="mt-8 text-sm">
        <Link href={`/${kandSlug}/doha/${dohaNumber}`} className="text-[var(--accent)] hover:underline">
          Read this doha in English →
        </Link>
      </p>
    </div>
  );
}
