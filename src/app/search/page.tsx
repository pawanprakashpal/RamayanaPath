"use client";

import { useState } from "react";

export default function SearchPage() {
  const [query, setQuery] = useState("");

  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-3xl font-bold mb-8">Search Verses</h1>

      <div className="mb-8">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for verses by keyword..."
          className="w-full px-4 py-3 rounded-lg border border-[var(--card-border)] bg-[var(--card-bg)] text-[var(--foreground)] placeholder:text-[var(--muted)] focus:outline-none focus:border-[var(--accent)] transition-colors"
        />
      </div>

      {!query && (
        <div className="card p-8 text-center">
          <p className="text-[var(--muted)]">
            Enter a keyword to search across all available verses.
          </p>
          <p className="text-sm text-[var(--muted)] mt-2">
            Search works across original text, transliteration, and translations.
          </p>
        </div>
      )}

      {query && (
        <div className="card p-8 text-center">
          <p className="text-[var(--muted)]">
            Search functionality coming soon. Try browsing the verses directly.
          </p>
        </div>
      )}
    </div>
  );
}
