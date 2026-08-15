import type { Bookmark } from "@/types";

const STORAGE_KEY = "ramayana-bookmarks";
const CHANGE_EVENT = "ramayana-bookmarks-changed";

export function readBookmarks(): Bookmark[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return [];
    const parsed: unknown = JSON.parse(raw);
    if (!Array.isArray(parsed)) return [];
    return parsed.filter(isBookmark).sort((a, b) => b.timestamp - a.timestamp);
  } catch {
    return [];
  }
}

function writeBookmarks(bookmarks: Bookmark[]): void {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(bookmarks));
    // Keeps the header count, the bookmarks page and any open button in sync.
    window.dispatchEvent(new CustomEvent(CHANGE_EVENT));
  } catch {
    // Storage full or unavailable — nothing useful to do.
  }
}

function isBookmark(value: unknown): value is Bookmark {
  if (typeof value !== "object" || value === null) return false;
  const b = value as Record<string, unknown>;
  return (
    typeof b.id === "string" &&
    typeof b.label === "string" &&
    typeof b.href === "string" &&
    typeof b.kand === "string" &&
    (b.version === "tulsidas" || b.version === "valmiki") &&
    typeof b.timestamp === "number"
  );
}

export function isBookmarked(id: string): boolean {
  return readBookmarks().some((b) => b.id === id);
}

/** Adds the bookmark, or removes it if already saved. Returns the new state. */
export function toggleBookmark(bookmark: Omit<Bookmark, "timestamp">): boolean {
  const existing = readBookmarks();
  const found = existing.find((b) => b.id === bookmark.id);

  if (found) {
    writeBookmarks(existing.filter((b) => b.id !== bookmark.id));
    return false;
  }

  writeBookmarks([{ ...bookmark, timestamp: Date.now() }, ...existing]);
  return true;
}

export function removeBookmark(id: string): void {
  writeBookmarks(readBookmarks().filter((b) => b.id !== id));
}

export function clearBookmarks(): void {
  writeBookmarks([]);
}

export function subscribeToBookmarks(listener: () => void): () => void {
  window.addEventListener(CHANGE_EVENT, listener);
  // Fires when another tab writes to localStorage.
  window.addEventListener("storage", listener);
  return () => {
    window.removeEventListener(CHANGE_EVENT, listener);
    window.removeEventListener("storage", listener);
  };
}

export function exportBookmarks(): string {
  return JSON.stringify(
    { version: 1, exportedAt: new Date().toISOString(), bookmarks: readBookmarks() },
    null,
    2
  );
}

export interface ImportResult {
  added: number;
  skipped: number;
}

/** Merges an exported file into the current set, keeping existing entries. */
export function importBookmarks(json: string): ImportResult {
  const parsed: unknown = JSON.parse(json);
  const incoming =
    Array.isArray(parsed)
      ? parsed
      : (parsed as { bookmarks?: unknown })?.bookmarks;

  if (!Array.isArray(incoming)) throw new Error("Unrecognised bookmarks file");

  const valid = incoming.filter(isBookmark);
  if (valid.length === 0) throw new Error("No bookmarks found in that file");

  const existing = readBookmarks();
  const seen = new Set(existing.map((b) => b.id));
  const added = valid.filter((b) => !seen.has(b.id));

  writeBookmarks([...added, ...existing].sort((a, b) => b.timestamp - a.timestamp));

  return { added: added.length, skipped: valid.length - added.length };
}

/** Stable id so the same passage is never bookmarked twice. */
export function bookmarkId(version: string, kandSlug: string, unitType: string, unit: number): string {
  return `${version}:${kandSlug}:${unitType}:${unit}`;
}
