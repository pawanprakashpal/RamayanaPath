import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getValmikiSarga, getKandBySlug, getValmikiTotalSargas } from "@/lib/data";
import VerseCard from "@/components/verse/VerseCard";
import PrevNextNav from "@/components/navigation/PrevNextNav";

interface SargaPageProps {
  params: Promise<{ kand: string; number: string }>;
}

export async function generateMetadata({ params }: SargaPageProps): Promise<Metadata> {
  const { kand: kandSlug, number } = await params;
  const sargaNumber = parseInt(number, 10);
  const kand = await getKandBySlug(kandSlug);
  const sarga = await getValmikiSarga(kandSlug, sargaNumber);
  if (!kand || !sarga) return {};
  return {
    title: `Sarga ${sargaNumber}: ${sarga.sarga.title} — ${kand.valmiki.name}`,
    description: `Read Sarga ${sargaNumber} of ${kand.valmiki.name} from Valmiki Ramayana with English translation.`,
  };
}

export async function generateStaticParams() {
  const { getKandManifest } = await import("@/lib/data");
  const manifest = await getKandManifest();
  const params: { kand: string; number: string }[] = [];

  for (const kand of manifest.kands) {
    if (!kand.valmiki.available) continue;
    // For now, only generate params for sargas that have data files
    // In production, this would enumerate all sarga files
    params.push({ kand: kand.slug, number: "1" });
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

  if (!sarga || !kand) notFound();

  return (
    <div>
      {/* Page header */}
      <div className="mb-8">
        <p className="text-sm text-[var(--muted)] mb-1">{kand.valmiki.name}</p>
        <h1 className="text-2xl font-bold">
          Sarga {sargaNumber}: {sarga.sarga.title}
        </h1>
        <p className="font-devanagari text-[var(--muted)]">{sarga.sarga.titleSanskrit}</p>
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
