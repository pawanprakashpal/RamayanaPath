"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { getProgress } from "@/components/verse/ReadingProgress";

interface ContinueReadingProps {
  kandSlug: string;
}

export default function ContinueReading({ kandSlug }: ContinueReadingProps) {
  const [doha, setDoha] = useState<number | null>(null);

  useEffect(() => {
    setDoha(getProgress(kandSlug));
  }, [kandSlug]);

  if (doha === null) return null;

  return (
    <Link
      href={`/${kandSlug}/doha/${doha}`}
      className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium bg-[var(--accent)] text-white hover:opacity-90 transition-opacity animate-fade-in"
    >
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <polygon points="5 3 19 12 5 21 5 3" />
      </svg>
      Continue from Doha {doha}
    </Link>
  );
}
