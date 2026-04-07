import { NextRequest, NextResponse } from "next/server";

const AZURE_KEY = process.env.AZURE_SPEECH_KEY;
const AZURE_REGION = process.env.AZURE_SPEECH_REGION || "eastus";

// --- Rate limiter: 20 requests per minute per IP ---
const WINDOW_MS = 60_000;
const MAX_REQUESTS = 20;
const hits = new Map<string, { count: number; resetAt: number }>();

function isRateLimited(ip: string): boolean {
  const now = Date.now();
  const entry = hits.get(ip);
  if (!entry || now > entry.resetAt) {
    hits.set(ip, { count: 1, resetAt: now + WINDOW_MS });
    return false;
  }
  entry.count++;
  return entry.count > MAX_REQUESTS;
}

// Clean up stale entries every 5 minutes
setInterval(() => {
  const now = Date.now();
  for (const [ip, entry] of hits) {
    if (now > entry.resetAt) hits.delete(ip);
  }
}, 300_000);

const VALID_LANGS = new Set(["original", "hindi", "english"]);

export async function POST(req: NextRequest) {
  if (!AZURE_KEY) {
    return NextResponse.json({ error: "TTS not configured" }, { status: 503 });
  }

  // Rate limit by IP
  const ip = req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() || "unknown";
  if (isRateLimited(ip)) {
    return NextResponse.json({ error: "Too many requests" }, { status: 429 });
  }

  const { text, lang } = await req.json();

  if (!text || typeof text !== "string" || text.trim().length === 0 || text.length > 3000) {
    return NextResponse.json({ error: "Invalid text" }, { status: 400 });
  }

  const safeLang = VALID_LANGS.has(lang) ? lang : "original";

  // Pick voice based on language
  const voice =
    safeLang === "english"
      ? "en-US-AndrewMultilingualNeural"
      : "hi-IN-MadhurNeural";

  const ssml = `
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="${safeLang === "english" ? "en-US" : "hi-IN"}">
      <voice name="${voice}">
        <prosody rate="${safeLang === "english" ? "0%" : "-10%"}">
          ${escapeXml(text.trim())}
        </prosody>
      </voice>
    </speak>`.trim();

  try {
    const res = await fetch(
      `https://${AZURE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1`,
      {
        method: "POST",
        headers: {
          "Ocp-Apim-Subscription-Key": AZURE_KEY,
          "Content-Type": "application/ssml+xml",
          "X-Microsoft-OutputFormat": "audio-24khz-96kbitrate-mono-mp3",
        },
        body: ssml,
      }
    );

    if (!res.ok) {
      return NextResponse.json(
        { error: "Azure TTS failed", status: res.status },
        { status: 502 }
      );
    }

    const audioBuffer = await res.arrayBuffer();

    return new NextResponse(audioBuffer, {
      headers: {
        "Content-Type": "audio/mpeg",
        "Cache-Control": "public, max-age=86400",
      },
    });
  } catch {
    return NextResponse.json({ error: "TTS request failed" }, { status: 502 });
  }
}

function escapeXml(str: string): string {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}
