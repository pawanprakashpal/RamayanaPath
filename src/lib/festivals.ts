/**
 * The festivals the home page greets, with the window during which each is
 * shown. Dates follow the lunar calendar and are entered by hand each year;
 * a festival with no window for the current year simply does not appear.
 *
 * Windows are inclusive and in the reader's local time. Navratri runs the
 * nine nights up to Vijayadashami; Diwali is shown from Dhanteras through
 * Bhai Dooj, since the homecoming is read in the days around the night.
 */
export type Festival = {
  key: "navratri" | "diwali";
  from: string; // YYYY-MM-DD
  to: string;   // YYYY-MM-DD
};

export const FESTIVALS: Festival[] = [
  { key: "navratri", from: "2026-10-11", to: "2026-10-20" },
  { key: "diwali",   from: "2026-11-06", to: "2026-11-10" },
  { key: "navratri", from: "2027-09-30", to: "2027-10-09" },
  { key: "diwali",   from: "2027-10-26", to: "2027-10-30" },
];

export function festivalOn(date: Date): Festival["key"] | null {
  const y = date.getFullYear();
  const m = String(date.getMonth() + 1).padStart(2, "0");
  const d = String(date.getDate()).padStart(2, "0");
  const today = `${y}-${m}-${d}`;
  for (const f of FESTIVALS) {
    if (today >= f.from && today <= f.to) return f.key;
  }
  return null;
}
