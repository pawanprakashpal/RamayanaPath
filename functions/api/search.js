/**
 * Search is the one thing that does not survive the move to a static site.
 *
 * On Vercel it built an index of 26,301 verses in server memory and matched
 * against it. That cannot be done in a Cloudflare Worker: the free plan allows
 * 10ms of CPU per request, and simply parsing the index costs far more than
 * that. The index is also 40MB, so bundling it is out regardless.
 *
 * The right fix is Cloudflare D1 - SQLite with FTS5, free at this size - where
 * the matching happens inside the database and the Worker only issues the
 * query and formats the answer, which fits the CPU budget comfortably. Until
 * that is built, this says so plainly rather than timing out or returning an
 * empty result that looks like "no matches".
 *
 * Everything else on the site works: all 2,873 pages, the meanings panel and
 * text to speech.
 */

export function onRequestGet() {
  return new Response(
    JSON.stringify({
      hits: [],
      total: 0,
      error:
        "Search is not available on this deployment yet. Every verse is still " +
        "reachable by browsing a Kand.",
    }),
    {
      status: 503,
      headers: {
        "Content-Type": "application/json",
        "Cache-Control": "no-store",
      },
    }
  );
}
