import type { MetadataRoute } from "next";

/**
 * Crawlers are only ~3% of our requests, so this is not about request volume.
 * It is about Fast Origin Transfer, which is charged when an edge region has
 * to pull a page from the origin because it does not hold it.
 *
 * A reader hits a handful of popular pages that are already warm. A crawler
 * walks the sitemap - all 2,873 of them, most of which no region has cached -
 * so each one is a miss and an origin pull. That makes a crawler far more
 * expensive per request than a reader, and we were at 100% of the 10 GB
 * allowance with the project set to pause beyond it.
 *
 * Blocked below are the ones that take without giving back for this audience:
 * SEO tooling that only feeds its own subscribers, and search engines with
 * effectively no readership for a Hindi and English Ramayana site. PetalBot
 * alone was our single busiest crawler.
 *
 * Deliberately NOT blocked: Google, Bing, DuckDuckGo and Apple, which send
 * the readers; and the AI assistants that cite their sources, since someone
 * asking Claude or ChatGPT about a chaupai is exactly who this site is for.
 * Reversible - remove a name here and it resumes within a day.
 */
const FREELOADERS = [
  // Search engines with no meaningful readership for this site.
  "PetalBot",
  "Baiduspider",
  "Bytespider",
  // SEO tooling: crawls the whole site, sends nobody.
  "AhrefsBot",
  "SemrushBot",
  "DataForSeoBot",
  "MJ12bot",
  "DotBot",
  "BLEXBot",
  // Bulk corpus collection.
  "CCBot",
  "Amazonbot",
];

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      { userAgent: "*", allow: "/" },
      { userAgent: FREELOADERS, disallow: "/" },
    ],
    sitemap: "https://ramayanpath.com/sitemap.xml",
  };
}
