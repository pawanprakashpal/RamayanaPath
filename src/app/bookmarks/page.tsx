"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import type { Bookmark } from "@/types";

export default function BookmarksPage() {
  const [bookmarks, setBookmarks] = useState<Bookmark[]>([]);

  useEffect(() => {
    const stored = localStorage.getItem("ramayana-bookmarks");
    if (stored) {
      setBookmarks(JSON.parse(stored));
    }
  }, []);

  const removeBookmark = (id: string) => {
    const updated = bookmarks.filter((b) => b.id !== id);
    setBookmarks(updated);
    localStorage.setItem("ramayana-bookmarks", JSON.stringify(updated));
  };

  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-3xl font-bold mb-8">Bookmarks</h1>

      {bookmarks.length === 0 ? (
        <div className="card p-8 text-center">
          <p className="text-[var(--muted)] mb-4">No bookmarks yet.</p>
          <p className="text-sm text-[var(--muted)]">
            Click the bookmark icon on any verse to save it here for easy access.
          </p>
          <Link
            href="/"
            className="inline-block mt-4 px-4 py-2 rounded-lg bg-[var(--accent)] text-white hover:bg-[var(--accent-hover)] transition-colors"
          >
            Start Reading
          </Link>
        </div>
      ) : (
        <div className="space-y-3">
          {bookmarks.map((bookmark) => (
            <div key={bookmark.id} className="card p-4 flex items-center justify-between">
              <div>
                <p className="font-medium">{bookmark.label}</p>
                <p className="text-xs text-[var(--muted)] capitalize">{bookmark.version} version</p>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={() => removeBookmark(bookmark.id)}
                  className="text-sm text-red-500 hover:text-red-700 transition-colors"
                >
                  Remove
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
