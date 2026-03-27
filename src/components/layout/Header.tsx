import Link from "next/link";
import { SITE_NAME } from "@/lib/constants";
import ThemeToggle from "@/components/ui/ThemeToggle";
import VersionSelector from "@/components/navigation/VersionSelector";

const KANDS = [
  { slug: "bal-kand", name: "Bal Kand", nameHindi: "बालकाण्ड", available: true },
  { slug: "ayodhya-kand", name: "Ayodhya Kand", nameHindi: "अयोध्याकाण्ड", available: true },
  { slug: "aranya-kand", name: "Aranya Kand", nameHindi: "अरण्यकाण्ड", available: true },
  { slug: "kishkindha-kand", name: "Kishkindha Kand", nameHindi: "किष्किन्धाकाण्ड", available: true },
  { slug: "sundar-kand", name: "Sundar Kand", nameHindi: "सुन्दरकाण्ड", available: true },
  { slug: "lanka-kand", name: "Lanka Kand", nameHindi: "लङ्काकाण्ड", available: true },
  { slug: "uttar-kand", name: "Uttar Kand", nameHindi: "उत्तरकाण्ड", available: true },
];

export default function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-[var(--card-border)] bg-[var(--background)]/95 backdrop-blur-sm">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-3 group">
            <div className="w-9 h-9 rounded-full bg-[#f97316] dark:bg-[#f97316] p-1.5 flex items-center justify-center">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/ram-icon.png" alt="Shree Ram" width="24" height="24" className="w-6 h-6" />
            </div>
            <span className="text-xl font-bold text-[var(--accent)] group-hover:text-[var(--accent-hover)] transition-colors">
              {SITE_NAME}
            </span>
          </Link>

          {/* Navigation */}
          <nav className="hidden md:flex items-center gap-6">
            <Link href="/" className="text-sm text-[var(--muted)] hover:text-[var(--foreground)] transition-colors">
              Home
            </Link>
            <KandsDropdown />
            <Link href="/bookmarks" className="text-sm text-[var(--muted)] hover:text-[var(--foreground)] transition-colors">
              Bookmarks
            </Link>
          </nav>

          {/* Controls */}
          <div className="flex items-center gap-3">
            <div className="hidden sm:block">
              <VersionSelector />
            </div>
            <ThemeToggle />
            <MobileMenu />
          </div>
        </div>

        {/* Mobile version selector */}
        <div className="sm:hidden pb-3">
          <VersionSelector />
        </div>
      </div>
    </header>
  );
}

function KandsDropdown() {
  return (
    <div className="relative group">
      <button className="flex items-center gap-1 text-sm text-[var(--muted)] hover:text-[var(--foreground)] transition-colors">
        Kands
        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="transition-transform group-hover:rotate-180">
          <polyline points="6 9 12 15 18 9" />
        </svg>
      </button>
      <div className="absolute left-1/2 -translate-x-1/2 top-full pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200">
        <div className="w-56 rounded-lg border border-[var(--card-border)] bg-[var(--card-bg)] shadow-lg p-2">
          {KANDS.map((kand) =>
            kand.available ? (
              <Link
                key={kand.slug}
                href={`/${kand.slug}`}
                className="flex items-center justify-between px-3 py-2 rounded-md text-sm hover:bg-[var(--verse-bg)] transition-colors"
              >
                <span>{kand.name}</span>
                <span className="font-devanagari text-xs text-[var(--muted)]">{kand.nameHindi}</span>
              </Link>
            ) : (
              <div
                key={kand.slug}
                className="flex items-center justify-between px-3 py-2 rounded-md text-sm opacity-40 cursor-default"
              >
                <span>{kand.name}</span>
                <span className="text-xs text-[var(--muted)]">Soon</span>
              </div>
            )
          )}
        </div>
      </div>
    </div>
  );
}

function MobileMenu() {
  return (
    <div className="md:hidden">
      <details className="relative">
        <summary className="p-2 rounded-lg hover:bg-[var(--verse-bg)] transition-colors cursor-pointer list-none">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <line x1="3" y1="12" x2="21" y2="12" />
            <line x1="3" y1="6" x2="21" y2="6" />
            <line x1="3" y1="18" x2="21" y2="18" />
          </svg>
        </summary>
        <nav className="absolute right-0 top-full mt-2 w-56 rounded-lg border border-[var(--card-border)] bg-[var(--card-bg)] shadow-lg p-2 z-50">
          <Link href="/" className="block px-3 py-2 rounded-md text-sm hover:bg-[var(--verse-bg)] transition-colors">
            Home
          </Link>
          <div className="my-1 border-t border-[var(--card-border)]" />
          <p className="px-3 py-1 text-xs font-medium text-[var(--muted)] uppercase tracking-wider">Kands</p>
          {KANDS.map((kand) =>
            kand.available ? (
              <Link
                key={kand.slug}
                href={`/${kand.slug}`}
                className="flex items-center justify-between px-3 py-2 rounded-md text-sm hover:bg-[var(--verse-bg)] transition-colors"
              >
                <span>{kand.name}</span>
                <span className="font-devanagari text-xs text-[var(--muted)]">{kand.nameHindi}</span>
              </Link>
            ) : (
              <div
                key={kand.slug}
                className="flex items-center justify-between px-3 py-2 rounded-md text-sm opacity-40 cursor-default"
              >
                <span>{kand.name}</span>
                <span className="text-xs text-[var(--muted)]">Soon</span>
              </div>
            )
          )}
          <div className="my-1 border-t border-[var(--card-border)]" />
          <Link href="/bookmarks" className="block px-3 py-2 rounded-md text-sm hover:bg-[var(--verse-bg)] transition-colors">
            Bookmarks
          </Link>
        </nav>
      </details>
    </div>
  );
}
