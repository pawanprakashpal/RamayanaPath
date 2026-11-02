/**
 * Text to speech, proxied to Azure Speech. A Cloudflare Pages Function, which
 * is the Cloudflare equivalent of the Next route handler this replaces.
 *
 * The key stays server-side: AZURE_SPEECH_KEY is set in the Pages project's
 * environment variables, exactly as it was on Vercel.
 *
 * The rate limiter from the Next version is deliberately not carried over.
 * It kept counts in a Map in module scope, which worked because one server
 * handled many requests; Workers run as short-lived isolates spread across
 * the network, so a per-isolate Map would limit almost nothing while giving
 * the impression of a limit. Cloudflare's own rate limiting, configured on
 * the route, is the honest way to do this and can be turned on without code.
 */

const VALID_LANGS = new Set(["original", "hindi", "english"]);

function escapeXml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

export async function onRequestPost({ request, env }) {
  const key = env.AZURE_SPEECH_KEY;
  const region = env.AZURE_SPEECH_REGION || "eastus";

  if (!key) {
    return json({ error: "TTS not configured" }, 503);
  }

  let payload;
  try {
    payload = await request.json();
  } catch {
    return json({ error: "Invalid request" }, 400);
  }

  const { text, lang } = payload ?? {};
  if (!text || typeof text !== "string" || text.trim().length === 0 || text.length > 3000) {
    return json({ error: "Invalid text" }, 400);
  }

  const safeLang = VALID_LANGS.has(lang) ? lang : "original";
  const isEnglish = safeLang === "english";
  const voice = isEnglish ? "en-US-AndrewMultilingualNeural" : "hi-IN-MadhurNeural";

  const ssml = `
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="${isEnglish ? "en-US" : "hi-IN"}">
      <voice name="${voice}">
        <prosody rate="${isEnglish ? "0%" : "-10%"}">
          ${escapeXml(text.trim())}
        </prosody>
      </voice>
    </speak>`.trim();

  try {
    const res = await fetch(
      `https://${region}.tts.speech.microsoft.com/cognitiveservices/v1`,
      {
        method: "POST",
        headers: {
          "Ocp-Apim-Subscription-Key": key,
          "Content-Type": "application/ssml+xml",
          "X-Microsoft-OutputFormat": "audio-24khz-96kbitrate-mono-mp3",
          // Azure's speech endpoint requires a User-Agent and answers 400
          // without one. Node's fetch sent a default; a Worker's fetch sends
          // none, which is why the same request worked on Vercel and not here.
          "User-Agent": "RamayanaPath/1.0",
        },
        body: ssml,
      }
    );

    if (!res.ok) {
      // Azure says why in the body (wrong region, bad key, SSML it dislikes);
      // without it a 502 here is a guess. Nothing secret comes back in it.
      const detail = (await res.text().catch(() => "")).slice(0, 300);
      return json({ error: "Azure TTS failed", status: res.status, region, detail }, 502);
    }

    return new Response(res.body, {
      headers: {
        "Content-Type": "audio/mpeg",
        "Cache-Control": "public, max-age=86400",
      },
    });
  } catch {
    return json({ error: "TTS request failed" }, 502);
  }
}
