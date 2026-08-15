import { notFound } from "next/navigation";
import Link from "next/link";
import type { Metadata } from "next";
import { getKandBySlug, getTulsidasKand } from "@/lib/data";
import { BASE_URL, breadcrumbJsonLd, dohaTitle, getKandSeo } from "@/lib/seo";
import { languageAlternates, t } from "@/lib/i18n";
import JsonLd from "@/components/seo/JsonLd";

interface Props {
  params: Promise<{ kand: string }>;
}

const strings = t("hi");

export async function generateStaticParams() {
  const { getKandManifest } = await import("@/lib/data");
  const manifest = await getKandManifest();
  return manifest.kands.filter((k) => k.tulsidas.available).map((k) => ({ kand: k.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);
  if (!kand) return {};

  const seo = getKandSeo(kandSlug);
  const name = kand.tulsidas.nameOriginal;
  const title = `${name} — सम्पूर्ण पाठ, हिन्दी अर्थ सहित`;
  const description = `${name} (${kand.tulsidas.name}) के सभी ${kand.tulsidas.totalUnits} दोहे — मूल अवधी चौपाई, दोहा एवं सोरठा, प्रत्येक पद का हिन्दी अर्थ और अंग्रेज़ी अनुवाद सहित। ${seo?.summaryHi ?? ""}`;

  return {
    title,
    description: description.slice(0, 320),
    keywords: [
      name,
      `${name} अर्थ सहित`,
      `${name} पाठ`,
      `रामचरितमानस ${name}`,
      `${kand.tulsidas.name} in Hindi`,
    ],
    alternates: {
      canonical: `/hi/${kandSlug}`,
      languages: languageAlternates(`/${kandSlug}`),
    },
    openGraph: { type: "article", title, description: description.slice(0, 200), url: `/hi/${kandSlug}`, locale: "hi_IN" },
  };
}

export default async function HindiKandPage({ params }: Props) {
  const { kand: kandSlug } = await params;
  const [kand, data] = await Promise.all([getKandBySlug(kandSlug), getTulsidasKand(kandSlug)]);

  if (!kand || !data) notFound();

  const seo = getKandSeo(kandSlug);
  const totalVerses = data.dohaGroups.reduce((sum, g) => sum + g.verses.length, 0);

  return (
    <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-8">
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "मुख्य पृष्ठ", path: "/hi" },
          { name: kand.tulsidas.nameOriginal, path: `/hi/${kandSlug}` },
        ])}
      />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "Chapter",
          name: kand.tulsidas.nameOriginal,
          alternateName: kand.tulsidas.name,
          position: kand.index,
          url: `${BASE_URL}/hi/${kandSlug}`,
          inLanguage: "hi",
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

      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">{kand.tulsidas.nameOriginal}</h1>
        <p className="text-[var(--muted)]">{strings.kandSubtitle}</p>
        <p className="text-sm text-[var(--muted)] mt-2">
          {data.kand.totalDohas} {strings.dohas} · {totalVerses} {strings.verses}
        </p>
        {seo?.summaryHi && (
          <p className="mt-4 text-sm leading-relaxed text-[var(--muted)]">{seo.summaryHi}</p>
        )}

        <div className="flex flex-wrap items-center gap-3 mt-4">
          <Link
            href={`/hi/${kandSlug}/paath`}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium bg-[var(--accent)] text-white hover:opacity-90 transition-opacity"
          >
            {strings.readPaath} →
          </Link>
          <Link href={`/${kandSlug}`} className="text-sm text-[var(--accent)] hover:underline">
            Read in English →
          </Link>
        </div>
      </div>

      <div className="grid gap-3">
        {data.dohaGroups.map((group) => (
          <Link
            key={group.dohaNumber}
            href={`/${kandSlug}/doha/${group.dohaNumber}`}
            className="card p-4 hover:border-[var(--accent)] transition-colors group"
          >
            <h2 className="font-medium group-hover:text-[var(--accent)] transition-colors">
              {dohaTitle(group.dohaNumber, group.label)}
            </h2>
            <p className="text-sm text-[var(--muted)] truncate mt-0.5">
              {group.verses[0]?.original.split("\n")[0] ?? ""}
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
}
