import { readFile } from "fs/promises";
import path from "path";

export const OG_SIZE = { width: 1200, height: 630 };
export const OG_CONTENT_TYPE = "image/png";

let fontCache: { name: string; data: ArrayBuffer; weight: 400 | 700; style: "normal" }[] | null = null;

/**
 * Devanagari glyphs render as tofu in Satori unless the font is supplied
 * explicitly, so the TTFs ship in public/fonts and are read at render time.
 */
export async function loadOgFonts() {
  if (fontCache) return fontCache;

  const dir = path.join(process.cwd(), "public", "fonts");
  const [regular, bold] = await Promise.all([
    readFile(path.join(dir, "NotoSansDevanagari-Regular.ttf")),
    readFile(path.join(dir, "NotoSansDevanagari-Bold.ttf")),
  ]);

  fontCache = [
    { name: "Noto Sans Devanagari", data: toArrayBuffer(regular), weight: 400, style: "normal" },
    { name: "Noto Sans Devanagari", data: toArrayBuffer(bold), weight: 700, style: "normal" },
  ];
  return fontCache;
}

function toArrayBuffer(buf: Buffer): ArrayBuffer {
  return buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength) as ArrayBuffer;
}

/** Keep OG text short enough that it never overflows the card. */
export function ogClamp(text: string, max: number): string {
  const flat = text.replace(/\s+/g, " ").trim();
  return flat.length <= max ? flat : `${flat.slice(0, max).trim()}…`;
}

interface OgCardProps {
  /** Small label above the verse — e.g. "Bal Kand · Ramcharitmanas". */
  eyebrow: string;
  /** Devanagari verse text, pre-clamped. */
  original: string;
  /** English translation snippet, pre-clamped. */
  translation: string;
  /** Bottom-left label — e.g. "Doha 1". */
  badge: string;
}

export function OgCard({ eyebrow, original, translation, badge }: OgCardProps) {
  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        background: "linear-gradient(135deg, #f97316 0%, #ea580c 55%, #c2410c 100%)",
        padding: 64,
        fontFamily: "Noto Sans Devanagari",
      }}
    >
      <div style={{ display: "flex", fontSize: 28, color: "rgba(255,255,255,0.85)", letterSpacing: "0.02em" }}>
        {eyebrow}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
        <div
          style={{
            display: "flex",
            fontSize: original.length > 90 ? 40 : 52,
            fontWeight: 700,
            color: "#ffffff",
            lineHeight: 1.5,
          }}
        >
          {original}
        </div>
        {translation && (
          <div
            style={{
              display: "flex",
              fontSize: 26,
              color: "rgba(255,255,255,0.88)",
              lineHeight: 1.45,
            }}
          >
            {translation}
          </div>
        )}
      </div>

      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <div
          style={{
            display: "flex",
            fontSize: 26,
            fontWeight: 700,
            color: "#c2410c",
            background: "#ffffff",
            padding: "10px 22px",
            borderRadius: 999,
          }}
        >
          {badge}
        </div>
        <div style={{ display: "flex", fontSize: 26, color: "rgba(255,255,255,0.9)" }}>
          ramayanpath.com
        </div>
      </div>
    </div>
  );
}
