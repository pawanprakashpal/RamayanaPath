import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getValmikiSarga, getKandBySlug, getValmikiTotalSargas, getValmikiSargaNumbers } from "@/lib/data";
import VerseCard from "@/components/verse/VerseCard";
import PrevNextNav from "@/components/navigation/PrevNextNav";
import JsonLd from "@/components/seo/JsonLd";
import BookmarkButton from "@/components/verse/BookmarkButton";
import { bookmarkId } from "@/lib/bookmarks";
import { BASE_URL, breadcrumbJsonLd, excerpt } from "@/lib/seo";

interface SargaPageProps {
  params: Promise<{ kand: string; number: string }>;
}

export async function generateMetadata({ params }: SargaPageProps): Promise<Metadata> {
  const { kand: kandSlug, number } = await params;
  const sargaNumber = parseInt(number, 10);
  const kand = await getKandBySlug(kandSlug);
  const sarga = await getValmikiSarga(kandSlug, sargaNumber);
  if (!kand) return {};

  const path = `/${kandSlug}/sarga/${sargaNumber}`;

  if (!sarga) {
    return {
      title: `${kand.valmiki.name} Sarga ${sargaNumber} — Valmiki Ramayana`,
      alternates: { canonical: path },
      robots: { index: false, follow: true },
    };
  }

  const title = `${kand.valmiki.name} Sarga ${sargaNumber} (${kand.valmiki.nameOriginal}) — Sanskrit Shloka with English Translation`;
  const firstShloka = sarga.shlokas[0];
  const description = `${sarga.sarga.title}. Sarga ${sargaNumber} of ${kand.valmiki.name}, Valmiki Ramayana — ${sarga.shlokas.length} Sanskrit shlokas in Devanagari with English translation${firstShloka?.hindiTranslation ? " and Hindi meaning" : ""}. ${firstShloka ? excerpt(firstShloka.original, 70) : ""}`;

  return {
    title,
    description,
    keywords: [
      `${kand.valmiki.name} Sarga ${sargaNumber}`,
      `Valmiki Ramayana Sarga ${sargaNumber}`,
      `${kand.valmiki.nameOriginal} सर्ग ${sargaNumber}`,
      "Valmiki Ramayana Sanskrit shloka with English translation",
      "Ramayana Sanskrit text",
    ],
    alternates: { canonical: path },
    openGraph: { type: "article", title, description, url: path },
    twitter: { card: "summary_large_image", title, description },
  };
}

export async function generateStaticParams() {
  const { getKandManifest } = await import("@/lib/data");
  const manifest = await getKandManifest();
  const params: { kand: string; number: string }[] = [];

  for (const kand of manifest.kands) {
    if (!kand.valmiki.available) continue;
    for (const sargaNumber of await getValmikiSargaNumbers(kand.slug)) {
      params.push({ kand: kand.slug, number: String(sargaNumber) });
    }
  }

  return params;
}

export default async function SargaPage({ params }: SargaPageProps) {
  const { kand: kandSlug, number } = await params;
  const sargaNumber = parseInt(number, 10);

  if (isNaN(sargaNumber)) notFound();

  const [sarga, kand, totalSargas] = await Promise.all([
    getValmikiSarga(kandSlug, sargaNumber),
    getKandBySlug(kandSlug),
    getValmikiTotalSargas(kandSlug),
  ]);

  if (!kand) notFound();

  if (!sarga) {
    return (
      <div className="text-center py-16">
        <p className="text-sm text-[var(--muted)] mb-2">{kand.valmiki.name}</p>
        <h1 className="text-2xl font-bold mb-4">Sarga {sargaNumber}</h1>
        <div className="card max-w-md mx-auto p-8">
          <p className="text-4xl mb-4">🙏</p>
          <h2 className="text-lg font-semibold mb-2">Coming Soon</h2>
          <p className="text-[var(--muted)] text-sm">
            The Valmiki Ramayana translation is being prepared. Currently, the complete
            Tulsidas Ramcharitmanas with all 5,809 verses is available.
          </p>
          <p className="text-[var(--muted)] text-sm mt-3">
            Switch to <span className="font-medium text-[var(--accent)]">Tulsidas</span> version
            using the toggle above to read this Kand.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div>
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "Home", path: "/" },
          { name: kand.valmiki.name, path: `/${kandSlug}` },
          { name: `Sarga ${sargaNumber}`, path: `/${kandSlug}/sarga/${sargaNumber}` },
        ])}
      />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "CreativeWork",
          name: `${kand.valmiki.name} Sarga ${sargaNumber} — ${sarga.sarga.title}`,
          alternateName: sarga.sarga.titleSanskrit || undefined,
          author: { "@type": "Person", name: "Maharshi Valmiki" },
          inLanguage: ["sa", "en"],
          text: sarga.shlokas.map((s) => s.original).join("\n"),
          position: sargaNumber,
          isPartOf: {
            "@type": "Chapter",
            name: kand.valmiki.name,
            alternateName: kand.valmiki.nameOriginal,
            position: kand.index,
            url: `${BASE_URL}/${kandSlug}`,
            isPartOf: {
              "@type": "Book",
              name: "Valmiki Ramayana",
              alternateName: "वाल्मीकि रामायणम्",
              author: { "@type": "Person", name: "Maharshi Valmiki" },
              inLanguage: "sa",
              url: BASE_URL,
            },
          },
          url: `${BASE_URL}/${kandSlug}/sarga/${sargaNumber}`,
        }}
      />

      {/* Page header */}
      <div className="mb-8">
        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="text-sm text-[var(--muted)] mb-1">{kand.valmiki.name}</p>
            <h1 className="text-2xl font-bold">
              Sarga {sargaNumber}: {sarga.sarga.title}
            </h1>
          </div>
          <BookmarkButton
            id={bookmarkId("valmiki", kandSlug, "sarga", sargaNumber)}
            version="valmiki"
            kandSlug={kandSlug}
            label={`${kand.valmiki.name} — Sarga ${sargaNumber}`}
            href={`/${kandSlug}/sarga/${sargaNumber}`}
          />
        </div>
        <p className="font-devanagari text-[var(--muted)]">
          {sarga.sarga.titleSanskrit || `${kand.valmiki.nameOriginal} · सर्ग ${sargaNumber}`}
        </p>
        <p className="text-sm text-[var(--muted)] mt-1">
          {sarga.shlokas.length} shloka{sarga.shlokas.length > 1 ? "s" : ""}
        </p>
      </div>

      {/* Shlokas */}
      <div className="space-y-4">
        {sarga.shlokas.map((shloka) => (
          <VerseCard
            key={shloka.id}
            verse={shloka}
            verseLabel={`Shloka ${shloka.number}`}
          />
        ))}
      </div>

      {/* Navigation */}
      <PrevNextNav
        prevHref={sargaNumber > 1 ? `/${kandSlug}/sarga/${sargaNumber - 1}` : undefined}
        nextHref={sargaNumber < totalSargas ? `/${kandSlug}/sarga/${sargaNumber + 1}` : undefined}
        prevLabel={sargaNumber > 1 ? `Sarga ${sargaNumber - 1}` : undefined}
        nextLabel={sargaNumber < totalSargas ? `Sarga ${sargaNumber + 1}` : undefined}
      />
    </div>
  );
}
