import Link from "next/link";

interface PrevNextNavProps {
  prevHref?: string;
  nextHref?: string;
  prevLabel?: string;
  nextLabel?: string;
  kandHref?: string;
  kandLabel?: string;
}

export default function PrevNextNav({ prevHref, nextHref, prevLabel, nextLabel, kandHref, kandLabel }: PrevNextNavProps) {
  return (
    <div className="mt-8 pt-6 border-t border-[var(--card-border)]">
      {/* Back to Kand overview */}
      {kandHref && (
        <div className="text-center mb-4">
          <Link
            href={kandHref}
            className="text-sm text-[var(--muted)] hover:text-[var(--foreground)] transition-colors"
          >
            {kandLabel ?? "Back to overview"}
          </Link>
        </div>
      )}

      {/* Prev / Next */}
      <div className="flex items-stretch justify-between gap-4">
        {prevHref ? (
          <Link
            href={prevHref}
            className="flex items-center gap-2 px-4 py-3 rounded-lg text-sm text-[var(--accent)] hover:bg-[var(--verse-bg)] transition-colors min-w-0"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="flex-shrink-0">
              <polyline points="15 18 9 12 15 6" />
            </svg>
            <span className="truncate">{prevLabel ?? "Previous"}</span>
          </Link>
        ) : (
          <div />
        )}

        {nextHref ? (
          <Link
            href={nextHref}
            className="flex items-center gap-2 px-4 py-3 rounded-lg text-sm text-[var(--accent)] hover:bg-[var(--verse-bg)] transition-colors min-w-0"
          >
            <span className="truncate">{nextLabel ?? "Next"}</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="flex-shrink-0">
              <polyline points="9 18 15 12 9 6" />
            </svg>
          </Link>
        ) : (
          <div />
        )}
      </div>
    </div>
  );
}
