import type { VerseType } from "@/types";
import { VERSE_TYPE_LABELS, VERSE_TYPE_COLORS } from "@/lib/constants";

interface VerseTypeBadgeProps {
  type: VerseType;
}

export default function VerseTypeBadge({ type }: VerseTypeBadgeProps) {
  return (
    <span className={`inline-block text-xs font-medium px-2 py-0.5 rounded-full ${VERSE_TYPE_COLORS[type]}`}>
      {VERSE_TYPE_LABELS[type]}
    </span>
  );
}
