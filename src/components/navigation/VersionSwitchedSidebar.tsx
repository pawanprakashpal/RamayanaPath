"use client";

import { useEffect, useState } from "react";
import type { Version } from "@/types";
import { DEFAULT_VERSION, VERSION_COOKIE } from "@/lib/constants";

interface VersionSwitchedSidebarProps {
  tulsidasName: string;
  valmikiName: string;
  tulsidas: React.ReactNode;
  valmiki: React.ReactNode;
}

function readVersionCookie(): Version {
  const match = document.cookie.match(new RegExp(`(?:^|; )${VERSION_COOKIE}=([^;]*)`));
  const value = match?.[1];
  return value === "tulsidas" || value === "valmiki" ? value : DEFAULT_VERSION;
}

/**
 * Picks the sidebar list on the client instead of the server. Reading the
 * version cookie in the layout opted every doha and sarga page out of static
 * generation; both lists are rendered on the server and one is hidden here, so
 * the pages stay fully static (and every link stays in the HTML for crawlers).
 */
export default function VersionSwitchedSidebar({
  tulsidasName,
  valmikiName,
  tulsidas,
  valmiki,
}: VersionSwitchedSidebarProps) {
  const [version, setVersion] = useState<Version>(DEFAULT_VERSION);

  useEffect(() => {
    setVersion(readVersionCookie());
  }, []);

  return (
    <>
      <h2 className="text-sm font-semibold text-[var(--muted)] uppercase tracking-wider mb-3">
        {version === "tulsidas" ? tulsidasName : valmikiName}
      </h2>
      <div hidden={version !== "tulsidas"}>{tulsidas}</div>
      <div hidden={version !== "valmiki"}>{valmiki}</div>
    </>
  );
}
