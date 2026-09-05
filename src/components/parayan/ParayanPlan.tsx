import Link from "next/link";
import { getKandManifest } from "@/lib/data";
import { PARAYAN_DAYS, daySegments } from "@/lib/parayan";
import { dohaTitleHi, langPath, type Lang } from "@/lib/i18n";
import { dohaTitle } from "@/lib/seo";

interface ParayanPlanProps {
  lang: Lang;
}

const COPY = {
  en: {
    dayLabel: (n: number) => `Day ${n}`,
    vishram: "Traditional pause",
    readHere: "Read",
    sharedGroupNote:
      "The traditional pause falls partway through this doha, which we render as one page — so this day and its neighbour share that page.",
    dohas: "dohas",
  },
  hi: {
    dayLabel: (n: number) => `${n}वाँ दिन`,
    vishram: "विश्राम",
    readHere: "पढ़ें",
    sharedGroupNote:
      "परम्परागत विश्राम इस दोहे के बीच में पड़ता है, जिसे हम एक ही पृष्ठ पर देते हैं — इसलिए यह दिन और अगला दिन वह पृष्ठ साझा करते हैं।",
    dohas: "दोहे",
  },
} as const;

export default async function ParayanPlan({ lang }: ParayanPlanProps) {
  const manifest = await getKandManifest();
  const copy = COPY[lang];

  const lastDoha: Record<string, number> = {};
  const kandName: Record<string, string> = {};
  for (const k of manifest.kands) {
    lastDoha[k.slug] = k.tulsidas.totalUnits;
    kandName[k.slug] = lang === "hi" ? k.tulsidas.nameOriginal : k.tulsidas.name;
  }

  return (
    <ol className="space-y-4">
      {PARAYAN_DAYS.map((day) => {
        const segments = daySegments(day, lastDoha);
        const label = lang === "hi" ? day.titleHi : day.titleEn;
        const summary = lang === "hi" ? day.summaryHi : day.summaryEn;
        const vishram = lang === "hi" ? day.vishramHi : day.vishramEn;

        return (
          <li key={day.day} id={`day-${day.day}`} className="card p-5 scroll-mt-24">
            <div className="flex items-baseline gap-3 flex-wrap mb-1">
              <span className="text-xs font-semibold uppercase tracking-wider text-[var(--accent)]">
                {copy.dayLabel(day.day)}
              </span>
              <h3 className="text-lg font-semibold">{label}</h3>
            </div>

            <p className="text-sm text-[var(--muted)] mb-3">
              <span className="font-medium text-[var(--foreground)]">{copy.vishram}:</span>{" "}
              {vishram}
            </p>

            <p className="text-sm leading-relaxed text-[var(--muted)] mb-4">{summary}</p>

            <div className="flex flex-wrap gap-2">
              {segments.map((segment) => {
                const from =
                  lang === "hi" ? dohaTitleHi(segment.from) : dohaTitle(segment.from);
                const to = lang === "hi" ? dohaTitleHi(segment.to) : dohaTitle(segment.to);
                return (
                  <Link
                    key={`${day.day}-${segment.kand}`}
                    href={`${langPath(lang, `/${segment.kand}/paath`)}#doha-${segment.from}`}
                    className="text-sm px-3 py-1.5 rounded-md border border-[var(--card-border)] hover:border-[var(--accent)] hover:text-[var(--accent)] transition-colors"
                  >
                    {copy.readHere}: {kandName[segment.kand]} — {from} → {to}
                  </Link>
                );
              })}
            </div>

            {day.sharesGroup && (
              <p className="text-xs text-[var(--muted)] mt-3">{copy.sharedGroupNote}</p>
            )}
          </li>
        );
      })}
    </ol>
  );
}
