"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import VerseTypeBadge from "@/components/verse/VerseTypeBadge";
import type { VerseType } from "@/types";

type VersionFilter = "all" | "tulsidas" | "valmiki";

interface Hit {
  id: string;
  version: "tulsidas" | "valmiki";
  kandName: string;
  unitLabel: string;
  href: string;
  type: VerseType;
  original: string;
  transliteration: string;
  translation: string;
  hindiTranslation: string;
}

interface SearchResponse {
  hits: Hit[];
  total: number;
  reference?: { label: string; href: string };
  error?: string;
}

const FILTERS: { value: VersionFilter; label: string }[] = [
  { value: "all", label: "All" },
  { value: "tulsidas", label: "Ramcharitmanas" },
  { value: "valmiki", label: "Valmiki Ramayana" },
];

const EXAMPLES = ["Hanuman", "Sanjivani", "मंगल भवन", "Sundar Kand doha 1", "Jatayu"];

export default function SearchClient() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const initialQuery = searchParams.get("q") ?? "";

  const [query, setQuery] = useState(initialQuery);
  const [version, setVersion] = useState<VersionFilter>("all");
  const [result, setResult] = useState<SearchResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Keeps a slow response from overwriting a newer one.
  const requestId = useRef(0);

  const runSearch = useCallback(async (q: string, v: VersionFilter) => {
    if (q.trim().length < 2) {
      setResult(null);
      setError(null);
      setLoading(false);
      return;
    }

    const id = ++requestId.current;
    setLoading(true);
    setError(null);

    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(q)}&version=${v}`);
      if (id !== requestId.current) return;

      if (res.status === 429) {
        setError("Too many searches in a row. Give it a minute.");
        setResult(null);
        return;
      }
      if (!res.ok) throw new Error("Search failed");

      setResult(await res.json());
    } catch {
      if (id !== requestId.current) return;
      setError("Search is unavailable right now. Please try again.");
      setResult(null);
    } finally {
      if (id === requestId.current) setLoading(false);
    }
  }, []);

  // Debounce typing; refetch immediately when the version filter changes.
  useEffect(() => {
    const handle = setTimeout(() => runSearch(query, version), 250);
    return () => clearTimeout(handle);
  }, [query, version, runSearch]);

  // Keep ?q= in the URL so searches can be shared and reloaded.
  useEffect(() => {
    const handle = setTimeout(() => {
      const trimmed = query.trim();
      const target = trimmed ? `/search?q=${encodeURIComponent(trimmed)}` : "/search";
      router.replace(target, { scroll: false });
    }, 500);
    return () => clearTimeout(handle);
  }, [query, router]);

  const hasQuery = query.trim().length >= 2;

  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-3xl font-bold mb-2">Search Verses</h1>
      <p className="text-[var(--muted)] mb-8">
        Across 6,087 Ramcharitmanas verses and 20,214 Valmiki shlokas — original text,
        transliteration, Hindi meaning and English translation.
      </p>

      <div className="mb-4">
        <input
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for a name, phrase, or verse number…"
          aria-label="Search verses"
          autoFocus
          className="w-full px-4 py-3 rounded-lg border border-[var(--card-border)] bg-[var(--card-bg)] text-[var(--foreground)] placeholder:text-[var(--muted)] focus:outline-none focus:border-[var(--accent)] transition-colors"
        />
      </div>

      <div className="flex flex-wrap gap-2 mb-8">
        {FILTERS.map((filter) => (
          <button
            key={filter.value}
            type="button"
            onClick={() => setVersion(filter.value)}
            aria-pressed={version === filter.value}
            className={`text-sm px-3 py-1.5 rounded-md border transition-colors ${
              version === filter.value
                ? "border-[var(--accent)] text-[var(--accent)]"
                : "border-[var(--card-border)] text-[var(--muted)] hover:text-[var(--foreground)]"
            }`}
          >
            {filter.label}
          </button>
        ))}
      </div>

      {!hasQuery && (
        <div className="card p-8">
          <p className="text-[var(--muted)] mb-4">
            Type at least two characters. You can search in English, Devanagari, or
            transliteration — <span className="font-medium">Sanjivani</span> finds{" "}
            <span className="font-medium">sañjīvanī</span>.
          </p>
          <div className="flex flex-wrap gap-2">
            {EXAMPLES.map((example) => (
              <button
                key={example}
                type="button"
                onClick={() => setQuery(example)}
                className="text-sm px-3 py-1.5 rounded-md border border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors"
              >
                {example}
              </button>
            ))}
          </div>
        </div>
      )}

      {error && (
        <div className="card p-6 text-center">
          <p className="text-[var(--muted)]">{error}</p>
        </div>
      )}

      {hasQuery && !error && (
        <>
          {result?.reference && (
            <Link
              href={result.reference.href}
              className="card p-4 mb-6 flex items-center justify-between hover:border-[var(--accent)] transition-colors group"
            >
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--muted)] mb-1">
                  Go to verse
                </p>
                <p className="font-medium group-hover:text-[var(--accent)] transition-colors">
                  {result.reference.label}
                </p>
              </div>
              <span aria-hidden className="text-[var(--muted)] group-hover:text-[var(--accent)]">
                →
              </span>
            </Link>
          )}

          {loading && !result && (
            <p className="text-sm text-[var(--muted)]">Searching…</p>
          )}

          {result && (
            <>
              <p className="text-sm text-[var(--muted)] mb-4" aria-live="polite">
                {result.total === 0
                  ? "No verses matched."
                  : `${result.total} verse${result.total === 1 ? "" : "s"} matched${
                      result.total > result.hits.length ? ` — showing the top ${result.hits.length}` : ""
                    }.`}
                {loading && " Updating…"}
              </p>

              <div className="space-y-3">
                {result.hits.map((hit) => (
                  <Link
                    key={`${hit.version}-${hit.id}`}
                    href={hit.href}
                    className="card p-4 block hover:border-[var(--accent)] transition-colors group"
                  >
                    <div className="flex items-center gap-2 flex-wrap mb-2">
                      <VerseTypeBadge type={hit.type} />
                      <span className="text-xs text-[var(--muted)]">
                        {hit.kandName} · {hit.unitLabel}
                      </span>
                      <span className="text-xs text-[var(--muted)] ml-auto">
                        {hit.version === "tulsidas" ? "Ramcharitmanas" : "Valmiki"}
                      </span>
                    </div>
                    <p className="font-devanagari text-[var(--foreground)] whitespace-pre-line group-hover:text-[var(--accent)] transition-colors">
                      {hit.original}
                    </p>
                    {hit.translation && (
                      <p className="text-sm text-[var(--muted)] mt-2 line-clamp-3">
                        {hit.translation}
                      </p>
                    )}
                  </Link>
                ))}
              </div>
            </>
          )}
        </>
      )}
    </div>
  );
}
