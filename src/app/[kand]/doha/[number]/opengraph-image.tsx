import { ImageResponse } from "next/og";
import { getDohaGroup, getKandBySlug } from "@/lib/data";
import { dohaTitle } from "@/lib/seo";
import { OG_CONTENT_TYPE, OG_SIZE, OgCard, loadOgFonts, ogClamp } from "@/lib/og";

export const alt = "Ramcharitmanas verse with English translation";
export const size = OG_SIZE;
export const contentType = OG_CONTENT_TYPE;

// Rendered on demand and cached at the edge — prerendering a card for each of
// the ~1,000 doha pages would dominate build time for little benefit.
export function generateStaticParams() {
  return [];
}

export default async function Image({
  params,
}: {
  params: Promise<{ kand: string; number: string }>;
}) {
  const { kand: kandSlug, number } = await params;
  const dohaNumber = parseInt(number, 10);
  const [kand, group, fonts] = await Promise.all([
    getKandBySlug(kandSlug),
    getDohaGroup(kandSlug, dohaNumber),
    loadOgFonts(),
  ]);

  const label = dohaTitle(dohaNumber, group?.label);
  const verse = group?.verses[0];

  return new ImageResponse(
    (
      <OgCard
        eyebrow={`${kand?.tulsidas.name ?? "Ramcharitmanas"} · ${kand?.tulsidas.nameOriginal ?? "श्रीरामचरितमानस"}`}
        original={ogClamp(verse?.original ?? "॥ श्रीरामचरितमानस ॥", 140)}
        translation={ogClamp(verse?.translation ?? "", 180)}
        badge={label}
      />
    ),
    { ...size, fonts }
  );
}
