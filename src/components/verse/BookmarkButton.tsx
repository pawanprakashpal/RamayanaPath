"use client";

import { useEffect, useState } from "react";
import type { Version } from "@/types";
import { isBookmarked, subscribeToBookmarks, toggleBookmark } from "@/lib/bookmarks";

interface BookmarkButtonProps {
  id: string;
  version: Version;
  kandSlug: string;
  label: string;
  href: string;
}

export default function BookmarkButton({ id, version, kandSlug, label, href }: BookmarkButtonProps) {
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    const sync = () => setSaved(isBookmarked(id));
    sync();
    return subscribeToBookmarks(sync);
  }, [id]);

  return (
    <button
      type="button"
      onClick={() => setSaved(toggleBookmark({ id, version, kand: kandSlug, label, href }))}
      aria-pressed={saved}
      aria-label={saved ? `Remove ${label} from bookmarks` : `Bookmark ${label}`}
      title={saved ? "Remove bookmark" : "Bookmark this"}
      className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium border transition-colors ${
        saved
          ? "border-[var(--accent)] text-[var(--accent)]"
          : "border-[var(--card-border)] text-[var(--muted)] hover:border-[var(--accent)] hover:text-[var(--accent)]"
      }`}
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="14"
        height="14"
        viewBox="0 0 24 24"
        fill={saved ? "currentColor" : "none"}
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden
      >
        <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
      </svg>
      {saved ? "Saved" : "Save"}
    </button>
  );
}
