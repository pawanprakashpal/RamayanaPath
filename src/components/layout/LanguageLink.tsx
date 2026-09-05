"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

/**
 * Switches between the English page at the root and its Hindi counterpart
 * under /hi. Only home, Kand and paath pages exist in both, so anything else
 * points at the Hindi home rather than a URL that would 404.
 */
const KAND_SLUGS = new Set([
  "bal-kand",
  "ayodhya-kand",
  "aranya-kand",
  "kishkindha-kand",
  "sundar-kand",
  "lanka-kand",
  "uttar-kand",
]);

function hasHindiVersion(pathname: string): boolean {
  const parts = pathname.split("/").filter(Boolean);
  if (parts.length === 0) return true; // home
  if (!KAND_SLUGS.has(parts[0])) return false; // /about, /search, /bookmarks
  if (parts.length === 1) return true;
  if (parts.length === 2 && parts[1] === "paath") return true;
  // /{kand}/doha/{n} has a Hindi counterpart; /{kand}/sarga/{n} does not.
  return parts.length === 3 && parts[1] === "doha";
}

export default function LanguageLink() {
  const pathname = usePathname() || "/";
  const isHindi = pathname === "/hi" || pathname.startsWith("/hi/");

  let href: string;
  let label: string;

  if (isHindi) {
    href = pathname === "/hi" ? "/" : pathname.slice(3);
    label = "English";
  } else {
    href = hasHindiVersion(pathname) ? (pathname === "/" ? "/hi" : `/hi${pathname}`) : "/hi";
    label = "हिन्दी";
  }

  return (
    <Link
      href={href}
      hrefLang={isHindi ? "en" : "hi"}
      className="text-sm text-[var(--muted)] hover:text-[var(--foreground)] transition-colors"
    >
      {label}
    </Link>
  );
}
