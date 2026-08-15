import { NextRequest, NextResponse } from "next/server";
import { searchVerses } from "@/lib/search";
import type { Version } from "@/types";

// --- Rate limiter: 30 requests per minute per IP ---
const WINDOW_MS = 60_000;
const MAX_REQUESTS = 30;
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

setInterval(() => {
  const now = Date.now();
  for (const [ip, entry] of hits) {
    if (now > entry.resetAt) hits.delete(ip);
  }
}, 300_000);

const VALID_VERSIONS = new Set<string>(["all", "tulsidas", "valmiki"]);

export async function GET(req: NextRequest) {
  const ip = req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() || "unknown";
  if (isRateLimited(ip)) {
    return NextResponse.json({ error: "Too many requests" }, { status: 429 });
  }

  const { searchParams } = req.nextUrl;
  const q = (searchParams.get("q") ?? "").slice(0, 120);
  const versionParam = searchParams.get("version") ?? "all";
  const version = (VALID_VERSIONS.has(versionParam) ? versionParam : "all") as Version | "all";

  if (q.trim().length < 2) {
    return NextResponse.json({ hits: [], total: 0, query: q });
  }

  try {
    const outcome = await searchVerses(q, { version, limit: 40 });
    return NextResponse.json(
      { ...outcome, query: q },
      {
        headers: {
          // Same query, same corpus — the corpus only changes on redeploy.
          "Cache-Control": "public, max-age=300, s-maxage=86400",
        },
      }
    );
  } catch {
    return NextResponse.json({ error: "Search failed" }, { status: 500 });
  }
}
