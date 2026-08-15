import { Suspense } from "react";
import SearchClient from "@/components/search/SearchClient";

export default function SearchPage() {
  return (
    <Suspense
      fallback={
        // Mirrors the real header so the statically rendered HTML carries the
        // page's actual copy rather than a bare spinner.
        <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-12">
          <h1 className="text-3xl font-bold mb-2">Search Verses</h1>
          <p className="text-[var(--muted)] mb-8">
            Across 6,087 Ramcharitmanas verses and 20,214 Valmiki shlokas — original text,
            transliteration, Hindi meaning and English translation.
          </p>
          <div className="card p-8 text-center">
            <p className="text-[var(--muted)]">Loading search…</p>
          </div>
        </div>
      }
    >
      <SearchClient />
    </Suspense>
  );
}
