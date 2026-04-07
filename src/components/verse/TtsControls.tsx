"use client";

import { useTts, type TtsLang } from "./TtsProvider";

interface TtsControlsProps {
  verses: { id: string; original: string; hindiTranslation?: string; translation: string }[];
}

const LANG_OPTIONS: { value: TtsLang; label: string }[] = [
  { value: "original", label: "Original" },
  { value: "hindi", label: "हिन्दी" },
  { value: "english", label: "English" },
];

export default function TtsControls({ verses }: TtsControlsProps) {
  const { supported, speaking, lang, setLang, playAll, stop } = useTts();

  if (!supported) return null;

  return (
    <div className="flex items-center gap-3 flex-wrap">
      {/* Language selector */}
      <div className="flex items-center rounded-lg border border-[var(--card-border)] overflow-hidden text-xs">
        {LANG_OPTIONS.map((opt) => (
          <button
            key={opt.value}
            onClick={() => { stop(); setLang(opt.value); }}
            className={`px-2.5 py-1.5 transition-colors ${
              lang === opt.value
                ? "bg-[var(--accent)] text-white"
                : "text-[var(--muted)] hover:bg-[var(--verse-bg)]"
            }`}
          >
            {opt.label}
          </button>
        ))}
      </div>

      {/* Play All / Stop */}
      <button
        onClick={() => speaking ? stop() : playAll(verses)}
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
            Play All
          </>
        )}
      </button>
    </div>
  );
}
