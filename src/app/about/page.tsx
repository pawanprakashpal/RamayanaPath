import type { Metadata } from "next";
import Link from "next/link";
import { SITE_NAME } from "@/lib/constants";

export const metadata: Metadata = {
  title: "About",
  description:
    "About RamayanaPath — a free, open-source project to make the Ramayana accessible with original verses, Hindi meanings, and English translations.",
  alternates: { canonical: "/about" },
};

export default function AboutPage() {
  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-3xl font-bold mb-2">{SITE_NAME}</h1>
      <p className="font-devanagari text-lg text-[var(--accent)] mb-8">
        ॥ श्रीरामचरितमानस ॥
      </p>

      <div className="prose dark:prose-invert max-w-none space-y-8">
        {/* Mission */}
        <section>
          <h2 className="text-xl font-semibold mb-3">Our Mission</h2>
          <p className="text-[var(--muted)] leading-relaxed">
            RamayanaPath is a free, open-source project dedicated to making the Ramayana
            accessible to everyone. We provide the original verses alongside Hindi meanings
            and English translations so readers worldwide can experience this timeless epic
            in its authentic form.
          </p>
        </section>

        {/* What We Offer */}
        <section>
          <h2 className="text-xl font-semibold mb-3">What We Offer</h2>
          <div className="grid sm:grid-cols-2 gap-4">
            <div className="card p-5">
              <h3 className="font-medium text-[var(--accent)] mb-2">Tulsidas Ramcharitmanas</h3>
              <p className="text-sm text-[var(--muted)]">
                The complete text of Goswami Tulsidas&apos;s 16th-century masterpiece in Awadhi,
                with all 7 Kands and over 6,000 verses — including Chaupais, Dohas, Chhands,
                Shlokas, and Sorathas.
              </p>
            </div>
            <div className="card p-5">
              <h3 className="font-medium text-[var(--accent)] mb-2">Valmiki Ramayana</h3>
              <p className="text-sm text-[var(--muted)]">
                The original Sanskrit epic by Maharshi Valmiki — the Adi Kavya (first poem)
                and foundational text of the Ramayana tradition. Coming soon with full
                Sarga-by-Sarga coverage.
              </p>
            </div>
          </div>
        </section>

        {/* Content Details */}
        <section>
          <h2 className="text-xl font-semibold mb-3">Content at a Glance</h2>
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-[var(--card-border)]">
                  <th className="text-left py-2 pr-4 font-medium">Kand</th>
                  <th className="text-left py-2 pr-4 font-medium font-devanagari">नाम</th>
                  <th className="text-right py-2 font-medium">Verses</th>
                </tr>
              </thead>
              <tbody className="text-[var(--muted)]">
                {[
                  { name: "Bal Kand", hindi: "बालकाण्ड", slug: "bal-kand", verses: "1,951" },
                  { name: "Ayodhya Kand", hindi: "अयोध्याकाण्ड", slug: "ayodhya-kand", verses: "1,622" },
                  { name: "Aranya Kand", hindi: "अरण्यकाण्ड", slug: "aranya-kand", verses: "326" },
                  { name: "Kishkindha Kand", hindi: "किष्किन्धाकाण्ड", slug: "kishkindha-kand", verses: "190" },
                  { name: "Sundar Kand", hindi: "सुन्दरकाण्ड", slug: "sundar-kand", verses: "343" },
                  { name: "Lanka Kand", hindi: "लङ्काकाण्ड", slug: "lanka-kand", verses: "785" },
                  { name: "Uttar Kand", hindi: "उत्तरकाण्ड", slug: "uttar-kand", verses: "855" },
                ].map((kand) => (
                  <tr key={kand.slug} className="border-b border-[var(--card-border)]">
                    <td className="py-2 pr-4">
                      <Link href={`/${kand.slug}`} className="text-[var(--accent)] hover:underline">
                        {kand.name}
                      </Link>
                    </td>
                    <td className="py-2 pr-4 font-devanagari">{kand.hindi}</td>
                    <td className="py-2 text-right">{kand.verses}</td>
                  </tr>
                ))}
                <tr className="font-medium">
                  <td className="py-2 pr-4" colSpan={2}>Total</td>
                  <td className="py-2 text-right">6,072</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        {/* Each Verse Includes */}
        <section>
          <h2 className="text-xl font-semibold mb-3">Each Verse Includes</h2>
          <ul className="space-y-2 text-[var(--muted)]">
            <li className="flex items-start gap-2">
              <span className="text-[var(--accent)] mt-0.5">&#x2022;</span>
              <span><strong>Original text</strong> in Devanagari script (Awadhi/Sanskrit)</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-[var(--accent)] mt-0.5">&#x2022;</span>
              <span><strong>IAST transliteration</strong> with proper diacritics for pronunciation</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-[var(--accent)] mt-0.5">&#x2022;</span>
              <span><strong>Hindi meaning</strong> (हिन्दी अर्थ) explaining the verse in modern Hindi</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-[var(--accent)] mt-0.5">&#x2022;</span>
              <span><strong>English translation</strong> for global accessibility</span>
            </li>
          </ul>
        </section>

        {/* Sources */}
        <section>
          <h2 className="text-xl font-semibold mb-3">Sources &amp; References</h2>
          <p className="text-[var(--muted)] leading-relaxed mb-3">
            We take accuracy seriously. Our text and structure are verified against
            authoritative editions:
          </p>
          <ul className="space-y-2 text-[var(--muted)]">
            <li className="flex items-start gap-2">
              <span className="text-[var(--accent)] mt-0.5">&#x2022;</span>
              <span>
                <strong>Gita Press, Gorakhpur</strong> — The gold standard for
                Ramcharitmanas text, numbering, and verse classification
              </span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-[var(--accent)] mt-0.5">&#x2022;</span>
              <span>
                <strong>IIT Kanpur</strong> —{" "}
                <a
                  href="https://www.ramcharitmanas.iitk.ac.in/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[var(--accent)] hover:underline"
                >
                  Ramcharitmanas
                </a>
                {" &amp; "}
                <a
                  href="https://www.valmiki.iitk.ac.in/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[var(--accent)] hover:underline"
                >
                  Valmiki Ramayanam
                </a>
                {" "}digital text repositories
              </span>
            </li>
          </ul>
        </section>

        {/* Open Source */}
        <section>
          <h2 className="text-xl font-semibold mb-3">Open Source</h2>
          <p className="text-[var(--muted)] leading-relaxed">
            RamayanaPath is open source. The complete codebase and verse data are available on{" "}
            <a
              href="https://github.com/pawanprakashpal/RamayanaPath"
              target="_blank"
              rel="noopener noreferrer"
              className="text-[var(--accent)] hover:underline"
            >
              GitHub
            </a>
            . Contributions, corrections, and suggestions are welcome.
          </p>
        </section>

        {/* Closing */}
        <section className="card p-6 text-center">
          <p className="font-devanagari text-lg text-[var(--accent)] mb-2">
            सियाराम मय सब जग जानी। करउँ प्रनाम जोरि जुग पानी॥
          </p>
          <p className="text-sm text-[var(--muted)] italic">
            Knowing the whole world to be pervaded by Sita and Rama, I make my obeisance with folded hands.
          </p>
        </section>
      </div>
    </div>
  );
}
