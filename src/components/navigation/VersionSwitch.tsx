"use client";

import { useEffect, useState } from "react";
import type { Version } from "@/types";
import { DEFAULT_VERSION, VERSION_COOKIE } from "@/lib/constants";

interface VersionSwitchProps {
  tulsidas: React.ReactNode;
  valmiki: React.ReactNode;
}

function readVersionCookie(): Version {
  const match = document.cookie.match(new RegExp(`(?:^|; )${VERSION_COOKIE}=([^;]*)`));
  const value = match?.[1];
  return value === "tulsidas" || value === "valmiki" ? value : DEFAULT_VERSION;
}

/**
 * Shows one recension's listing, chosen on the client. Reading the version
 * cookie on the server made this page dynamic — and these Kand pages earn most
 * of the site's impressions, so every one of those hits was a server render.
 * Both listings ship in the HTML, which also keeps every link crawlable.
 */
export default function VersionSwitch({ tulsidas, valmiki }: VersionSwitchProps) {
  const [version, setVersion] = useState<Version>(DEFAULT_VERSION);

  useEffect(() => {
    setVersion(readVersionCookie());
  }, []);

  return (
    <>
      <div hidden={version !== "tulsidas"}>{tulsidas}</div>
      <div hidden={version !== "valmiki"}>{valmiki}</div>
    </>
  );
}
