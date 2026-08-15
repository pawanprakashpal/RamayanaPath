import type { TulsidasVerse } from "@/types";
import VerseTypeBadge from "@/components/verse/VerseTypeBadge";
import VerseHighlight from "@/components/verse/VerseHighlight";
import PaathMeaning from "./PaathMeaning";

interface PaathVerseProps {
  verse: TulsidasVerse;
  kandSlug: string;
  dohaNumber: number;
}

/**
 * Reading-first verse: only the original text is rendered into the page. The
 * meaning loads when asked for — VerseCard opens the English translation by
 * default, which both breaks the flow when reciting and made the full-Kand
 * pages far too heavy to send over mobile data.
 */
export default function PaathVerse({ verse, kandSlug, dohaNumber }: PaathVerseProps) {
  return (
    <VerseHighlight verseId={verse.id}>
      <div className="flex items-start justify-between gap-4">
        <div className="verse-original whitespace-pre-line flex-1">{verse.original}</div>
        <div className="flex-shrink-0 pt-1">
          <VerseTypeBadge type={verse.type} />
        </div>
      </div>

      <PaathMeaning kandSlug={kandSlug} dohaNumber={dohaNumber} verseId={verse.id} />
    </VerseHighlight>
  );
}
