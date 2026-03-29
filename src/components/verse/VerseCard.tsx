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

      {/* Transliteration — collapsible */}
      {verse.transliteration && (
        <details className="mb-4 group">
          <summary className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider cursor-pointer select-none hover:text-[var(--foreground)] transition-colors">
            <span className="group-open:hidden">Show Transliteration</span>
            <span className="hidden group-open:inline">Transliteration</span>
          </summary>
          <div className="verse-transliteration whitespace-pre-line mt-2">
            {verse.transliteration}
          </div>
        </details>
      )}

      {/* Hindi Translation */}
      {verse.hindiTranslation && (
        <div className="mb-4">
          <p className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider mb-1">
            हिन्दी अर्थ
          </p>
          <div className="verse-translation font-devanagari">{verse.hindiTranslation}</div>
        </div>
      )}

      {/* English Translation */}
      <div>
        <p className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider mb-1">
          English Translation
        </p>
        <div className="verse-translation">{verse.translation}</div>
      </div>
    </div>
  );
}
