import Link from "next/link";
import { SITE_NAME } from "@/lib/constants";

export default function Footer() {
  return (
    <footer className="border-t border-[var(--card-border)] mt-auto">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="text-center sm:text-left">
            <p className="text-sm text-[var(--muted)]">
              {SITE_NAME} — Read the Ramayana with devotion
            </p>
            <p className="text-xs text-[var(--muted)] mt-1">
              Original verses from Tulsidas Ramcharitmanas & Valmiki Ramayana
            </p>
            <div className="flex items-center gap-3 mt-2 justify-center sm:justify-start">
              <Link href="/about" className="text-xs text-[var(--accent)] hover:underline">About</Link>
              <span className="text-[var(--card-border)]">|</span>
              <a href="https://github.com/pawanprakashpal/RamayanaPath" target="_blank" rel="noopener noreferrer" className="text-xs text-[var(--accent)] hover:underline">GitHub</a>
            </div>
          </div>
          <div className="text-xs text-[var(--muted)] text-center sm:text-right">
            <p>Verses are in the public domain. Translations provided for educational purposes.</p>
            <p className="mt-1">
              Texts sourced from{" "}
              <a href="https://www.valmiki.iitk.ac.in/" target="_blank" rel="noopener noreferrer" className="underline hover:text-[var(--foreground)]">
                IIT Kanpur Valmiki Ramayanam
              </a>
              {" & "}
              <a href="https://www.ramcharitmanas.iitk.ac.in/" target="_blank" rel="noopener noreferrer" className="underline hover:text-[var(--foreground)]">
                IIT Kanpur Ramcharitmanas
              </a>
            </p>
            <p className="mt-1 text-[var(--muted)]">
              Use <kbd className="px-1 py-0.5 rounded bg-[var(--verse-bg)] text-[10px]">←</kbd> <kbd className="px-1 py-0.5 rounded bg-[var(--verse-bg)] text-[10px]">→</kbd> arrow keys to navigate between dohas
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
