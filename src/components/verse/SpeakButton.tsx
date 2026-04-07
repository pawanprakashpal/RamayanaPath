"use client";

import { useTts } from "./TtsProvider";

interface SpeakButtonProps {
  verseId: string;
  original: string;
  hindiTranslation?: string;
  translation: string;
}

export default function SpeakButton({ verseId, original, hindiTranslation, translation }: SpeakButtonProps) {
  const { supported, speaking, currentVerseId, lang, speakVerse } = useTts();

  if (!supported) return null;

  const isActive = speaking && currentVerseId === verseId;
  const text = lang === "english" ? translation : lang === "hindi" ? (hindiTranslation || original) : original;

  return (
    <button
      onClick={() => speakVerse(verseId, text)}
      className={`p-1.5 rounded-md transition-colors ${
        isActive
          ? "text-[var(--accent)] bg-[var(--verse-bg)]"
          : "text-[var(--muted)] hover:text-[var(--foreground)] hover:bg-[var(--verse-bg)]"
      }`}
      title={isActive ? "Stop" : "Listen"}
      aria-label={isActive ? "Stop speaking" : "Listen to verse"}
    >
      {isActive ? (
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none">
          <rect x="6" y="5" width="4" height="14" rx="1" />
          <rect x="14" y="5" width="4" height="14" rx="1" />
        </svg>
      ) : (
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" />
          <path d="M15.54 8.46a5 5 0 0 1 0 7.07" />
        </svg>
      )}
    </button>
  );
}
