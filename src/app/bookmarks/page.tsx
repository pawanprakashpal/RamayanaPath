"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import type { Bookmark } from "@/types";
import {
  clearBookmarks,
  exportBookmarks,
  importBookmarks,
  readBookmarks,
  removeBookmark,
  subscribeToBookmarks,
} from "@/lib/bookmarks";

export default function BookmarksPage() {
  const [bookmarks, setBookmarks] = useState<Bookmark[]>([]);
  const [notice, setNotice] = useState<string | null>(null);
  const fileInput = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const sync = () => setBookmarks(readBookmarks());
    sync();
    return subscribeToBookmarks(sync);
  }, []);

  function handleExport() {
    const blob = new Blob([exportBookmarks()], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `ramayanapath-bookmarks-${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    URL.revokeObjectURL(url);
  }

  async function handleImport(event: React.ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0];
    if (!file) return;

    try {
      const { added, skipped } = importBookmarks(await file.text());
      setNotice(
        added === 0
          ? `Nothing new — all ${skipped} bookmark${skipped === 1 ? "" : "s"} were already saved.`
          : `Added ${added} bookmark${added === 1 ? "" : "s"}${skipped ? `, skipped ${skipped} already saved` : ""}.`
      );
    } catch (err) {
      setNotice(err instanceof Error ? err.message : "Could not read that file.");
    } finally {
      // Allow re-picking the same file.
      event.target.value = "";
    }
  }

  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-12">
      <div className="flex items-start justify-between gap-4 mb-2">
        <h1 className="text-3xl font-bold">Bookmarks</h1>
        {bookmarks.length > 0 && (
          <span className="text-sm text-[var(--muted)] pt-2">
            {bookmarks.length} saved
          </span>
        )}
      </div>
      <p className="text-[var(--muted)] mb-8">
        Saved on this device only. Export a copy to move them to another browser or phone.
      </p>

      <div className="flex flex-wrap gap-2 mb-6">
        <button
          type="button"
          onClick={handleExport}
          disabled={bookmarks.length === 0}
          className="text-sm px-3 py-1.5 rounded-lg border border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors disabled:opacity-40 disabled:hover:border-[var(--card-border)] disabled:hover:text-[var(--muted)]"
        >
          Export
        </button>
        <button
          type="button"
          onClick={() => fileInput.current?.click()}
          className="text-sm px-3 py-1.5 rounded-lg border border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors"
        >
          Import
        </button>
        <input
          ref={fileInput}
          type="file"
          accept="application/json,.json"
          onChange={handleImport}
          className="hidden"
        />
        {bookmarks.length > 0 && (
          <button
            type="button"
            onClick={() => {
              if (confirm(`Remove all ${bookmarks.length} bookmarks? This cannot be undone.`)) {
                clearBookmarks();
                setNotice(null);
              }
            }}
            className="text-sm px-3 py-1.5 rounded-lg border border-[var(--card-border)] text-[var(--muted)] hover:border-red-400 hover:text-red-500 transition-colors ml-auto"
          >
            Clear all
          </button>
        )}
      </div>

      {notice && (
        <div className="card p-4 mb-6 flex items-center justify-between gap-4">
          <p className="text-sm text-[var(--muted)]">{notice}</p>
          <button
            type="button"
            onClick={() => setNotice(null)}
            aria-label="Dismiss"
            className="text-sm text-[var(--muted)] hover:text-[var(--foreground)]"
          >
            ✕
          </button>
        </div>
      )}

      {bookmarks.length === 0 ? (
        <div className="card p-8 text-center">
          <p className="text-[var(--muted)] mb-4">No bookmarks yet.</p>
          <p className="text-sm text-[var(--muted)]">
            Tap <span className="font-medium text-[var(--foreground)]">Save</span> on any doha or
            sarga to keep it here.
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
            <div key={bookmark.id} className="card p-4 flex items-center justify-between gap-4">
              <Link href={bookmark.href} className="min-w-0 group">
                <p className="font-medium truncate group-hover:text-[var(--accent)] transition-colors">
                  {bookmark.label}
                </p>
                <p className="text-xs text-[var(--muted)]">
                  {bookmark.version === "tulsidas" ? "Ramcharitmanas" : "Valmiki Ramayana"}
                </p>
              </Link>
              <button
                type="button"
                onClick={() => removeBookmark(bookmark.id)}
                className="text-sm text-red-500 hover:text-red-700 transition-colors flex-shrink-0"
              >
                Remove
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
