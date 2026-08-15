"use client";

import { useState } from "react";

interface Meaning {
  id: string;
  transliteration: string;
  hindiTranslation: string;
  translation: string;
}

interface PaathMeaningProps {
  kandSlug: string;
  dohaNumber: number;
  verseId: string;
}

// One fetch per doha group, shared across every verse in it and across
// expand/collapse cycles.
const cache = new Map<string, Promise<Meaning[]>>();

function loadGroup(kandSlug: string, dohaNumber: number): Promise<Meaning[]> {
  const key = `${kandSlug}:${dohaNumber}`;
  let pending = cache.get(key);
  if (!pending) {
    pending = fetch(`/api/meaning?kand=${encodeURIComponent(kandSlug)}&doha=${dohaNumber}`)
      .then((res) => {
        if (!res.ok) throw new Error("Failed");
        return res.json();
      })
      .then((data: { verses: Meaning[] }) => data.verses)
      .catch((err) => {
        cache.delete(key);
        throw err;
      });
    cache.set(key, pending);
  }
  return pending;
}

export default function PaathMeaning({ kandSlug, dohaNumber, verseId }: PaathMeaningProps) {
  const [meaning, setMeaning] = useState<Meaning | null>(null);
  const [status, setStatus] = useState<"idle" | "loading" | "error">("idle");

  function handleToggle(event: React.SyntheticEvent<HTMLDetailsElement>) {
    if (!event.currentTarget.open || meaning || status === "loading") return;

    setStatus("loading");
    loadGroup(kandSlug, dohaNumber)
      .then((verses) => {
        setMeaning(verses.find((v) => v.id === verseId) ?? null);
        setStatus("idle");
      })
      .catch(() => setStatus("error"));
  }

  return (
    <details className="group mt-3" onToggle={handleToggle}>
      <summary className="text-xs font-medium text-[var(--muted)] uppercase tracking-wider cursor-pointer select-none hover:text-[var(--foreground)] transition-colors">
        <span className="group-open:hidden">अर्थ / Meaning</span>
        <span className="hidden group-open:inline">छिपाएँ / Hide</span>
      </summary>

      {status === "loading" && (
        <p className="text-sm text-[var(--muted)] mt-3">Loading…</p>
      )}
      {status === "error" && (
        <p className="text-sm text-[var(--muted)] mt-3">
          Could not load the meaning. Please try again.
        </p>
      )}
      {meaning && (
        <>
          {meaning.transliteration && (
            <div className="verse-transliteration whitespace-pre-line mt-3">
              {meaning.transliteration}
            </div>
          )}
          {meaning.hindiTranslation && (
            <div className="verse-translation font-devanagari mt-3">
              {meaning.hindiTranslation}
            </div>
          )}
          {meaning.translation && (
            <div className="verse-translation mt-3">{meaning.translation}</div>
          )}
        </>
      )}
    </details>
  );
}
