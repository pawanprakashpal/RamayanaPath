import type { BaseVerse } from "@/types";
import VerseTypeBadge from "./VerseTypeBadge";

interface VerseCardProps {
  verse: BaseVerse;
  verseLabel?: string;
}

export default function VerseCard({ verse, verseLabel }: VerseCardProps) {
  return (
    <div className="verse-card">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <VerseTypeBadge type={verse.type} />
          {verseLabel && (
            <span className="text-xs text-[var(--muted)]">{verseLabel}</span>
          )}
        </div>
      </div>

      {/* Original text */}
      <div className="mb-4">
        <div className="verse-original whitespace-pre-line">{verse.original}</div>
      </div>

      {/* Transliteration */}
      <div className="mb-4">
        <p className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider mb-1">
          Transliteration
        </p>
        <div className="verse-transliteration whitespace-pre-line">
          {verse.transliteration}
        </div>
      </div>

      {/* Translation */}
      <div>
        <p className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider mb-1">
          English Translation
        </p>
        <div className="verse-translation">{verse.translation}</div>
      </div>
    </div>
  );
}
