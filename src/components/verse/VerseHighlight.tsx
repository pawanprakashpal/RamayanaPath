"use client";

import { useEffect, useRef } from "react";
import { useTts } from "./TtsProvider";

interface VerseHighlightProps {
  verseId: string;
  children: React.ReactNode;
}

export default function VerseHighlight({ verseId, children }: VerseHighlightProps) {
  const { speaking, currentVerseId } = useTts();
  const ref = useRef<HTMLDivElement>(null);
  const isActive = speaking && currentVerseId === verseId;

  useEffect(() => {
    if (isActive && ref.current) {
      ref.current.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }, [isActive]);

  return (
    <div
      ref={ref}
      className={`verse-card ${isActive ? "tts-active" : ""}`}
    >
      {children}
    </div>
  );
}
