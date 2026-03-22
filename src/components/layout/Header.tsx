import Link from "next/link";
import { SITE_NAME } from "@/lib/constants";
import ThemeToggle from "@/components/ui/ThemeToggle";
import VersionSelector from "@/components/navigation/VersionSelector";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-[var(--card-border)] bg-[var(--background)]/95 backdrop-blur-sm">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-3 group">
            <span className="text-2xl" aria-hidden="true">🙏</span>
            <span className="text-xl font-bold text-[var(--accent)] group-hover:text-[var(--accent-hover)] transition-colors">
              {SITE_NAME}
            </span>
          </Link>

          {/* Navigation */}
          <nav className="hidden md:flex items-center gap-6">
            <Link href="/" className="text-sm text-[var(--muted)] hover:text-[var(--foreground)] transition-colors">
              Home
            </Link>
            <Link href="/bal-kand" className="text-sm text-[var(--muted)] hover:text-[var(--foreground)] transition-colors">
              Bal Kand
            </Link>
            <Link href="/sundar-kand" className="text-sm text-[var(--muted)] hover:text-[var(--foreground)] transition-colors">
              Sundar Kand
            </Link>
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

            {/* Mobile menu button */}
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
        <nav className="absolute right-0 top-full mt-2 w-48 rounded-lg border border-[var(--card-border)] bg-[var(--card-bg)] shadow-lg p-2 z-50">
          <Link href="/" className="block px-3 py-2 rounded-md text-sm hover:bg-[var(--verse-bg)] transition-colors">
            Home
          </Link>
          <Link href="/bal-kand" className="block px-3 py-2 rounded-md text-sm hover:bg-[var(--verse-bg)] transition-colors">
            Bal Kand
          </Link>
          <Link href="/sundar-kand" className="block px-3 py-2 rounded-md text-sm hover:bg-[var(--verse-bg)] transition-colors">
            Sundar Kand
          </Link>
          <Link href="/bookmarks" className="block px-3 py-2 rounded-md text-sm hover:bg-[var(--verse-bg)] transition-colors">
            Bookmarks
          </Link>
        </nav>
      </details>
    </div>
  );
}
