import type { BaseVerse } from "@/types";
import VerseTypeBadge from "./VerseTypeBadge";
import SpeakButton from "./SpeakButton";
import VerseHighlight from "./VerseHighlight";

interface HindiVerseCardProps {
  verse: BaseVerse;
  verseLabel?: string;
}

/**
 * Hindi-reader ordering: the meaning a Hindi speaker came for is open, and the
 * English translation is the one tucked away. VerseCard does the reverse.
 */
export default function HindiVerseCard({ verse, verseLabel }: HindiVerseCardProps) {
  return (
    <VerseHighlight verseId={verse.id}>
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <VerseTypeBadge type={verse.type} />
          {verseLabel && <span className="text-xs text-[var(--muted)]">{verseLabel}</span>}
        </div>
        <SpeakButton
          verseId={verse.id}
          original={verse.original}
          hindiTranslation={verse.hindiTranslation}
          translation={verse.translation}
        />
      </div>

      <div className="mb-4">
        <div className="verse-original whitespace-pre-line">{verse.original}</div>
      </div>

      {verse.hindiTranslation && (
        <details className="group mb-4" open>
          <summary className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider cursor-pointer select-none hover:text-[var(--foreground)] transition-colors">
            <span className="group-open:hidden">हिन्दी अर्थ देखें</span>
            <span className="hidden group-open:inline">हिन्दी अर्थ</span>
          </summary>
          <div className="verse-translation mt-2">{verse.hindiTranslation}</div>
        </details>
      )}

      {verse.transliteration && (
        <details className="group mb-4">
          <summary className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider cursor-pointer select-none hover:text-[var(--foreground)] transition-colors">
            <span className="group-open:hidden">रोमन लिप्यंतरण देखें</span>
            <span className="hidden group-open:inline">रोमन लिप्यंतरण</span>
          </summary>
          <div className="verse-transliteration whitespace-pre-line mt-2">
            {verse.transliteration}
          </div>
        </details>
      )}

      {verse.translation && (
        <details className="group">
          <summary className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider cursor-pointer select-none hover:text-[var(--foreground)] transition-colors">
            <span className="group-open:hidden">अंग्रेज़ी अनुवाद देखें</span>
            <span className="hidden group-open:inline">अंग्रेज़ी अनुवाद</span>
          </summary>
          <div className="verse-translation mt-2">{verse.translation}</div>
        </details>
      )}
    </VerseHighlight>
  );
}
