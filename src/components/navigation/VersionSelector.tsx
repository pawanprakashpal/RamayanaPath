"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import type { Version } from "@/types";
import { VERSION_LABELS, DEFAULT_VERSION, VERSION_COOKIE } from "@/lib/constants";

export default function VersionSelector() {
  const [version, setVersion] = useState<Version>(DEFAULT_VERSION);
  const router = useRouter();

  useEffect(() => {
    const match = document.cookie.match(new RegExp(`${VERSION_COOKIE}=([^;]+)`));
    if (match) {
      setVersion(match[1] as Version);
    }
  }, []);

  const handleChange = (newVersion: Version) => {
    setVersion(newVersion);
    document.cookie = `${VERSION_COOKIE}=${newVersion}; path=/; max-age=31536000; SameSite=Lax`;
    router.refresh();
  };

  return (
    <div className="flex items-center gap-1 rounded-lg bg-[var(--verse-bg)] p-1">
      {(Object.entries(VERSION_LABELS) as [Version, string][]).map(([key, label]) => (
        <button
          key={key}
          onClick={() => handleChange(key)}
          className={`px-3 py-1.5 text-sm rounded-md transition-colors ${
            version === key
              ? "bg-[var(--accent)] text-white font-medium"
              : "hover:bg-[var(--card-bg)] text-[var(--muted)]"
          }`}
        >
          {label}
        </button>
      ))}
    </div>
  );
}
