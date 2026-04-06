import { ImageResponse } from "next/og";

export const runtime = "edge";
export const alt = "RamayanaPath — Read the Ramayana with translations";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default function Image() {
  return new ImageResponse(
    (
      <div
        style={{
          background: "linear-gradient(135deg, #f97316 0%, #ea580c 50%, #c2410c 100%)",
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          fontFamily: "sans-serif",
        }}
      >
        <div
          style={{
            fontSize: 80,
            fontWeight: 700,
            color: "white",
            marginBottom: 16,
            letterSpacing: "-0.02em",
          }}
        >
          🙏 RamayanaPath
        </div>
        <div
          style={{
            fontSize: 32,
            color: "rgba(255,255,255,0.9)",
            textAlign: "center",
            maxWidth: 800,
            lineHeight: 1.4,
          }}
        >
          Read the Ramayana — Original verses with English &amp; Hindi translations
        </div>
        <div
          style={{
            fontSize: 22,
            color: "rgba(255,255,255,0.7)",
            marginTop: 24,
          }}
        >
          Tulsidas Ramcharitmanas • 7 Kands • 6,072 Verses
        </div>
      </div>
    ),
    { ...size }
  );
}
