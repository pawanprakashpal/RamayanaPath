"use client";

import { useEffect } from "react";

interface ReadingProgressProps {
  kandSlug: string;
  dohaNumber: number;
}

const STORAGE_KEY = "ramayanpath-progress";

export function saveProgress(kandSlug: string, dohaNumber: number) {
  try {
    const data = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
    data[kandSlug] = dohaNumber;
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  } catch {
    // localStorage unavailable
  }
}

export function getProgress(kandSlug: string): number | null {
  try {
    const data = JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
    return data[kandSlug] ?? null;
  } catch {
    return null;
  }
}

export default function ReadingProgress({ kandSlug, dohaNumber }: ReadingProgressProps) {
  useEffect(() => {
    saveProgress(kandSlug, dohaNumber);
  }, [kandSlug, dohaNumber]);

  return null;
}
