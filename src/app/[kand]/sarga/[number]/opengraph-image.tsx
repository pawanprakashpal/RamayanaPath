import { ImageResponse } from "next/og";
import { getKandBySlug, getValmikiSarga } from "@/lib/data";
import { OG_CONTENT_TYPE, OG_SIZE, OgCard, loadOgFonts, ogClamp } from "@/lib/og";

export const alt = "Valmiki Ramayana shloka with English translation";
export const size = OG_SIZE;
export const contentType = OG_CONTENT_TYPE;

// Rendered on demand — see the doha card for the same reasoning.
export function generateStaticParams() {
  return [];
}

export default async function Image({
  params,
}: {
  params: Promise<{ kand: string; number: string }>;
}) {
  const { kand: kandSlug, number } = await params;
  const sargaNumber = parseInt(number, 10);
  const [kand, sarga, fonts] = await Promise.all([
    getKandBySlug(kandSlug),
    getValmikiSarga(kandSlug, sargaNumber),
    loadOgFonts(),
  ]);

  const shloka = sarga?.shlokas[0];

  return new ImageResponse(
    (
      <OgCard
        eyebrow={`${kand?.valmiki.name ?? "Valmiki Ramayana"} · ${kand?.valmiki.nameOriginal ?? "वाल्मीकि रामायणम्"}`}
        original={ogClamp(shloka?.original ?? "॥ वाल्मीकि रामायणम् ॥", 140)}
        translation={ogClamp(sarga?.sarga.title ?? shloka?.translation ?? "", 180)}
        badge={`Sarga ${sargaNumber}`}
      />
    ),
    { ...size, fonts }
  );
}
