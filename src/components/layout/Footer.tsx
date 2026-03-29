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
              Original verses from Tulsidas Ramcharitmanas &amp; Valmiki Ramayana
            </p>
          </div>
          <div className="text-xs text-[var(--muted)] text-center sm:text-right">
            <p>Verses are in the public domain. Translations provided for educational purposes.</p>
            <p className="mt-1">
              Sanskrit texts sourced from{" "}
              <a href="https://www.valmiki.iitk.ac.in/" target="_blank" rel="noopener noreferrer" className="underline hover:text-[var(--foreground)]">
                IIT Kanpur Valmiki Ramayanam
              </a>
              {" "}&amp;{" "}
              <a href="https://www.ramcharitmanas.iitk.ac.in/" target="_blank" rel="noopener noreferrer" className="underline hover:text-[var(--foreground)]">
                IIT Kanpur Ramcharitmanas
              </a>
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
