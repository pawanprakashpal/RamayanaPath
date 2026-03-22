import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getDohaGroup, getTulsidasKand, getKandBySlug } from "@/lib/data";
import VerseCard from "@/components/verse/VerseCard";
import PrevNextNav from "@/components/navigation/PrevNextNav";

interface DohaPageProps {
  params: Promise<{ kand: string; number: string }>;
}

export async function generateMetadata({ params }: DohaPageProps): Promise<Metadata> {
  const { kand: kandSlug, number } = await params;
  const dohaNumber = parseInt(number, 10);
  const kand = await getKandBySlug(kandSlug);
  const group = await getDohaGroup(kandSlug, dohaNumber);
  if (!kand || !group) return {};
  const title = group.label ?? `Doha ${dohaNumber}`;
  return {
    title: `${title} — ${kand.tulsidas.name}`,
    description: `Read ${title} of ${kand.tulsidas.name} from Tulsidas Ramcharitmanas with English translation.`,
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

  return (
    <div>
      {/* Page header */}
      <div className="mb-8">
        <p className="text-sm text-[var(--muted)] mb-1">{kand.tulsidas.name}</p>
        <h1 className="text-2xl font-bold">
          {group.label ?? `Doha ${dohaNumber}`}
        </h1>
        <p className="text-sm text-[var(--muted)] mt-1">
          {group.verses.length} verse{group.verses.length > 1 ? "s" : ""}
        </p>
      </div>

      {/* Verses */}
      <div className="space-y-4">
        {group.verses.map((verse, index) => (
          <VerseCard
            key={verse.id}
            verse={verse}
            verseLabel={`${index + 1} of ${group.verses.length}`}
          />
        ))}
      </div>

      {/* Navigation */}
      <PrevNextNav
        prevHref={prevDoha !== undefined ? `/${kandSlug}/doha/${prevDoha}` : undefined}
        nextHref={nextDoha !== undefined ? `/${kandSlug}/doha/${nextDoha}` : undefined}
        prevLabel={prevDoha !== undefined ? `Doha ${prevDoha}` : undefined}
        nextLabel={nextDoha !== undefined ? `Doha ${nextDoha}` : undefined}
        kandHref={`/${kandSlug}`}
        kandLabel={`All ${kand.tulsidas.name} Dohas`}
      />
    </div>
  );
}
