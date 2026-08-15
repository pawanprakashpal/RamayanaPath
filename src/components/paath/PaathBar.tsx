"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useTts } from "@/components/verse/TtsProvider";
import { getProgress, saveProgress } from "@/components/verse/ReadingProgress";

interface PaathBarProps {
  kandSlug: string;
  /** Doha numbers in reading order. */
  dohaNumbers: number[];
  /**
   * Original text only. A paath is recited in the original, and shipping the
   * Hindi and English for every verse would double the page payload — the
   * per-verse buttons still read the translations.
   */
  ttsVerses: { id: string; original: string; translation: string }[];
}

export default function PaathBar({ kandSlug, dohaNumbers, ttsVerses }: PaathBarProps) {
  const { supported, speaking, playAll, stop } = useTts();
  const [currentIndex, setCurrentIndex] = useState(0);
  const [resumeAt, setResumeAt] = useState<number | null>(null);

  const total = dohaNumbers.length;
  const currentDoha = dohaNumbers[currentIndex] ?? dohaNumbers[0] ?? 0;
  const percent = total > 1 ? Math.round((currentIndex / (total - 1)) * 100) : 0;

  // Offer to resume only if the reader got somewhere meaningful last time.
  useEffect(() => {
    const saved = getProgress(kandSlug);
    if (saved !== null && saved > (dohaNumbers[0] ?? 0)) setResumeAt(saved);
  }, [kandSlug, dohaNumbers]);

  // Track which doha is in view.
  useEffect(() => {
    const sections = Array.from(
      document.querySelectorAll<HTMLElement>("[data-doha-index]")
    );
    if (sections.length === 0) return;

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
        if (!visible) return;
        const index = Number(visible.target.getAttribute("data-doha-index"));
        if (!Number.isNaN(index)) setCurrentIndex(index);
      },
      { rootMargin: "-80px 0px -70% 0px" }
    );

    sections.forEach((section) => observer.observe(section));
    return () => observer.disconnect();
  }, []);

  // Persist position, but not on every scroll tick.
  const lastSaved = useRef<number | null>(null);
  useEffect(() => {
    if (lastSaved.current === currentDoha) return;
    const handle = setTimeout(() => {
      lastSaved.current = currentDoha;
      saveProgress(kandSlug, currentDoha);
    }, 1000);
    return () => clearTimeout(handle);
  }, [currentDoha, kandSlug]);

  const scrollToDoha = useCallback((doha: number) => {
    document.getElementById(`doha-${doha}`)?.scrollIntoView({ behavior: "smooth", block: "start" });
  }, []);

  return (
    <div className="sticky top-16 z-30 -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 py-3 bg-[var(--background)]/95 backdrop-blur-sm border-b border-[var(--card-border)]">
      <div className="flex items-center justify-between gap-3 flex-wrap">
        <p className="text-sm text-[var(--muted)]" aria-live="polite">
          <span className="font-medium text-[var(--foreground)]">Doha {currentDoha}</span> of{" "}
          {dohaNumbers[total - 1]}
        </p>

        <div className="flex items-center gap-2">
          {resumeAt !== null && resumeAt !== currentDoha && (
            <button
              type="button"
              onClick={() => {
                scrollToDoha(resumeAt);
                setResumeAt(null);
              }}
              className="text-xs px-3 py-1.5 rounded-lg border border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors"
            >
              Resume from Doha {resumeAt}
            </button>
          )}

          {supported && (
            <button
              type="button"
              onClick={() => (speaking ? stop() : playAll(ttsVerses))}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-colors ${
                speaking
                  ? "bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-200 hover:bg-red-200 dark:hover:bg-red-800"
                  : "bg-[var(--accent)] text-white hover:opacity-90"
              }`}
            >
              {speaking ? (
                <>
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor" stroke="none">
                    <rect x="6" y="5" width="4" height="14" rx="1" />
                    <rect x="14" y="5" width="4" height="14" rx="1" />
                  </svg>
                  Stop
                </>
              ) : (
                <>
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="currentColor" stroke="none">
                    <polygon points="5 3 19 12 5 21 5 3" />
                  </svg>
                  Play Paath
                </>
              )}
            </button>
          )}
        </div>
      </div>

      <div
        className="mt-2 h-1 rounded-full bg-[var(--verse-bg)] overflow-hidden"
        role="progressbar"
        aria-valuenow={percent}
        aria-valuemin={0}
        aria-valuemax={100}
        aria-label="Paath progress"
      >
        <div
          className="h-full bg-[var(--accent)] transition-[width] duration-300"
          style={{ width: `${percent}%` }}
        />
      </div>
    </div>
  );
}
