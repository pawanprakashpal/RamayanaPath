import Link from "next/link";

interface PrevNextNavProps {
  prevHref?: string;
  nextHref?: string;
  prevLabel?: string;
  nextLabel?: string;
}

export default function PrevNextNav({ prevHref, nextHref, prevLabel, nextLabel }: PrevNextNavProps) {
  return (
    <div className="flex items-center justify-between mt-8 pt-6 border-t border-[var(--card-border)]">
      {prevHref ? (
        <Link
          href={prevHref}
          className="flex items-center gap-2 text-sm text-[var(--accent)] hover:text-[var(--accent-hover)] transition-colors"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="15 18 9 12 15 6" />
          </svg>
          {prevLabel ?? "Previous"}
        </Link>
      ) : (
        <div />
      )}

      {nextHref ? (
        <Link
          href={nextHref}
          className="flex items-center gap-2 text-sm text-[var(--accent)] hover:text-[var(--accent-hover)] transition-colors"
        >
          {nextLabel ?? "Next"}
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="9 18 15 12 9 6" />
          </svg>
        </Link>
      ) : (
        <div />
      )}
    </div>
  );
}
