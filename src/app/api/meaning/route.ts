import { NextRequest, NextResponse } from "next/server";
import { getDohaGroup } from "@/lib/data";

/**
 * Meanings for one doha group, fetched when a reader expands a verse on the
 * paath page. Inlining them for all seven Kands cost up to 1.3MB gzipped per
 * page for text most readers never open.
 */
export async function GET(req: NextRequest) {
  const { searchParams } = req.nextUrl;
  const kand = searchParams.get("kand") ?? "";
  const doha = Number(searchParams.get("doha"));

  if (!/^[a-z-]{1,40}$/.test(kand) || !Number.isInteger(doha) || doha < 0 || doha > 999) {
    return NextResponse.json({ error: "Invalid request" }, { status: 400 });
  }

  const group = await getDohaGroup(kand, doha);
  if (!group) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  return NextResponse.json(
    {
      verses: group.verses.map((v) => ({
        id: v.id,
        transliteration: v.transliteration,
        hindiTranslation: v.hindiTranslation ?? "",
        translation: v.translation,
      })),
    },
    {
      // The text only changes on redeploy.
      headers: { "Cache-Control": "public, max-age=3600, s-maxage=604800" },
    }
  );
}
