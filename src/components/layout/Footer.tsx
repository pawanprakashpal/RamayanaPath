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
          <div className="text-xs text-[var(--muted)]">
            Verses are in the public domain. Translations provided for educational purposes.
          </div>
        </div>
      </div>
    </footer>
  );
}
