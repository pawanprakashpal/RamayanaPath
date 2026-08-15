import Link from "next/link";
import type { KandManifestEntry } from "@/types";

interface KandCardProps {
  kand: KandManifestEntry;
}

const KAND_DESCRIPTIONS: Record<string, string> = {
  "bal-kand": "The childhood of Lord Rama — birth, education, marriage to Sita",
  "ayodhya-kand": "The exile of Rama — Kaikeyi's boon, departure to the forest",
  "aranya-kand": "Life in the forest — encounters with sages and demons, Sita's abduction",
  "kishkindha-kand": "Alliance with Sugriva — the search for Sita begins",
  "sundar-kand": "Hanuman's journey to Lanka — finding Sita, burning Lanka",
  "lanka-kand": "The great battle — Rama's army vs Ravana, victory of good over evil",
  "uttar-kand": "The return to Ayodhya — coronation, Rama Rajya",
};

export default function KandCard({ kand }: KandCardProps) {
  const isAvailable = kand.tulsidas.available || kand.valmiki.available;

  const content = (
    <div
      className={`card p-6 h-full flex flex-col ${
        isAvailable
          ? "hover:border-[#fb923c] hover:shadow-xl hover:-translate-y-1 hover:scale-[1.02] cursor-pointer transition-all duration-300 ease-out"
          : "opacity-50"
      }`}
    >
      {/* Status badge */}
      <div className="flex items-start justify-end mb-3">
        {!isAvailable && (
          <span className="text-xs px-2 py-0.5 rounded-full bg-[var(--verse-bg)] text-[var(--muted)]">
            Coming Soon
          </span>
        )}
        {isAvailable && (
          <span className="text-xs px-2 py-0.5 rounded-full bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200">
            Available
          </span>
        )}
      </div>

      {/* Names */}
      <h3 className="text-lg font-semibold mb-1">{kand.tulsidas.name}</h3>
      <p className="font-devanagari text-[var(--muted)] text-sm mb-3">
        {kand.tulsidas.nameOriginal}
      </p>

      {/* Description */}
      <p className="text-sm text-[var(--muted)] mb-4 flex-1">
        {KAND_DESCRIPTIONS[kand.slug] ?? ""}
      </p>

      {/* Stats */}
      <div className="flex gap-4 text-xs text-[var(--muted)] border-t border-[var(--card-border)] pt-3 mt-auto">
        <span>{kand.tulsidas.totalUnits} Dohas</span>
        <span>{kand.valmiki.totalUnits} Sargas</span>
      </div>
    </div>
  );

  if (!isAvailable) return content;

  return (
    <div className="h-full flex flex-col">
      <Link href={`/${kand.slug}`} className="flex-1">
        {content}
      </Link>
      {kand.tulsidas.available && (
        // Sits outside the card link — nesting an anchor inside another is invalid.
        <Link
          href={`/${kand.slug}/paath`}
          className="mt-2 text-center text-xs px-3 py-2 rounded-lg border border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors"
        >
          Read full paath →
        </Link>
      )}
    </div>
  );
}
