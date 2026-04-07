import { NextRequest, NextResponse } from "next/server";

const AZURE_KEY = process.env.AZURE_SPEECH_KEY;
const AZURE_REGION = process.env.AZURE_SPEECH_REGION || "eastus";

export async function POST(req: NextRequest) {
  if (!AZURE_KEY) {
    return NextResponse.json({ error: "TTS not configured" }, { status: 503 });
  }

  const { text, lang } = await req.json();

  if (!text || typeof text !== "string" || text.length > 3000) {
    return NextResponse.json({ error: "Invalid text" }, { status: 400 });
  }

  // Pick voice based on language
  const voice =
    lang === "english"
      ? "en-US-AndrewMultilingualNeural"
      : "hi-IN-MadhurNeural";

  const ssml = `
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="${lang === "english" ? "en-US" : "hi-IN"}">
      <voice name="${voice}">
        <prosody rate="${lang === "english" ? "0%" : "-10%"}">
          ${escapeXml(text)}
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
