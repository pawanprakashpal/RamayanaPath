import { notFound } from "next/navigation";
import Link from "next/link";
import type { Metadata } from "next";
import { getKandBySlug, getTulsidasKand, getValmikiTotalSargas } from "@/lib/data";
import { getServerVersion } from "@/lib/version";

interface KandPageProps {
  params: Promise<{ kand: string }>;
}

export async function generateMetadata({ params }: KandPageProps): Promise<Metadata> {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);
  if (!kand) return {};
  return {
    title: `${kand.tulsidas.name} — Read Ramayana`,
    description: `Read ${kand.tulsidas.name} (${kand.tulsidas.nameOriginal}) of Tulsidas Ramcharitmanas — ${kand.tulsidas.totalUnits} dohas with original Awadhi verses, Hindi meanings, and English translations.`,
    alternates: {
      canonical: `/${kandSlug}`,
    },
  };
}

export default async function KandPage({ params }: KandPageProps) {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);

  if (!kand) notFound();

  const version = await getServerVersion();

  if (version === "tulsidas") {
    const data = await getTulsidasKand(kandSlug);
    if (!data) notFound();

    return (
      <div>
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-2">{kand.tulsidas.name}</h1>
          <p className="font-devanagari text-xl text-[var(--muted)]">{kand.tulsidas.nameOriginal}</p>
          <p className="text-sm text-[var(--muted)] mt-2">{data.kand.totalDohas} Dohas</p>
        </div>

        <div className="grid gap-3">
          {data.dohaGroups.map((group) => (
            <Link
              key={group.dohaNumber}
              href={`/${kandSlug}/doha/${group.dohaNumber}`}
              className="card p-4 hover:border-[var(--accent)] transition-colors group"
            >
              <div className="flex items-center justify-between gap-4">
                <div className="min-w-0">
                  <h3 className="font-medium group-hover:text-[var(--accent)] transition-colors">
                    {group.label ?? `Doha ${group.dohaNumber}`}
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
      </div>
    );
  }

  // Valmiki version
  const totalSargas = await getValmikiTotalSargas(kandSlug);

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">{kand.valmiki.name}</h1>
        <p className="font-devanagari text-xl text-[var(--muted)]">{kand.valmiki.nameOriginal}</p>
        <p className="text-sm text-[var(--muted)] mt-2">{totalSargas} Sargas</p>
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
    </div>
  );
}
