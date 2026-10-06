#!/usr/bin/env node
/**
 * Guards the two mistakes that put us over the CDN request allowance.
 *
 * October 2026: the Hobby tier allows 1M CDN requests a month and we were
 * running at 1.02M. Bots were 3.4% of it and the API routes 0.2% - the spend
 * was our own pages, from two causes that are easy to reintroduce and silent
 * when you do:
 *
 *   1. A <Link> in a shared layout with Next's default prefetch. Header and
 *      Footer render on every one of 1,749 pages, so each default-prefetch
 *      link there fetches its target on every page view. /about was being
 *      requested as often as the homepage.
 *
 *   2. Pages and public/ files served max-age=0, must-revalidate, so a
 *      browser must ask again for something it already holds.
 *
 * Neither shows up in a build, a type check or a test. This does.
 *
 *   node scripts/check-request-budget.mjs           # source checks only
 *   node scripts/check-request-budget.mjs --live    # also check the live site
 *   node scripts/check-request-budget.mjs --live --url https://staging...
 */

import { readdir, readFile } from "node:fs/promises";
import { join, relative } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1");
const args = process.argv.slice(2);
const LIVE = args.includes("--live");
const URL_ARG = args[args.indexOf("--url") + 1];
const SITE = args.includes("--url") ? URL_ARG : "https://ramayanpath.com";

// Components rendered on every page. A default-prefetch Link here multiplies
// by the whole site, which is what makes it worth failing over.
const SHARED_LAYOUT = ["src/components/layout", "src/app/layout.tsx"];

// What each kind of response should be allowed to cache for.
const CACHE_RULES = [
  { path: "/", label: "home", min: 60, max: 3600 },
  { path: "/bal-kand", label: "kand page", min: 60, max: 3600 },
  { path: "/bal-kand/doha/1", label: "verse page", min: 60, max: 3600 },
  { path: "/about", label: "about", min: 60, max: 3600 },
  { path: "/favicon.svg", label: "favicon", min: 86400, max: Infinity },
  { path: "/manifest.json", label: "manifest", min: 3600, max: Infinity },
];

// A page should not need more than this many subresources. Ours sits near 28.
const ASSET_BUDGET = 40;

let failures = 0;
let warnings = 0;

function fail(what, detail) {
  failures++;
  console.log(`  FAIL  ${what}`);
  if (detail) console.log(`        ${detail}`);
}
function warn(what, detail) {
  warnings++;
  console.log(`  WARN  ${what}`);
  if (detail) console.log(`        ${detail}`);
}
function pass(what, detail) {
  console.log(`  ok    ${what}${detail ? `  (${detail})` : ""}`);
}

async function* walk(dir) {
  let entries;
  try {
    entries = await readdir(dir, { withFileTypes: true });
  } catch {
    return;
  }
  for (const e of entries) {
    const full = join(dir, e.name);
    if (e.isDirectory()) yield* walk(full);
    else if (/\.(tsx|jsx)$/.test(e.name)) yield full;
  }
}

/** Every <Link ...> opening tag, however many lines it spans. */
function linkTags(source) {
  return source.match(/<Link\b[^>]*>/gs) ?? [];
}

async function checkSharedLayoutPrefetch() {
  console.log("\nShared layout: <Link> prefetch");
  const files = [];
  for (const target of SHARED_LAYOUT) {
    const full = join(ROOT, target);
    if (target.endsWith(".tsx")) files.push(full);
    else for await (const f of walk(full)) files.push(f);
  }

  let checked = 0;
  for (const file of files) {
    let source;
    try {
      source = await readFile(file, "utf8");
    } catch {
      continue;
    }
    const tags = linkTags(source);
    if (!tags.length) continue;

    const offenders = tags.filter((t) => !/prefetch=\{false\}/.test(t));
    checked += tags.length;
    const name = relative(ROOT, file).replace(/\\/g, "/");

    if (offenders.length) {
      fail(
        `${name}: ${offenders.length} of ${tags.length} <Link> prefetch by default`,
        `these render on every page, so each one fetches its target on every page view. ` +
          `Add prefetch={false}. First: ${offenders[0].replace(/\s+/g, " ").slice(0, 90)}…`
      );
    } else {
      pass(`${name}: all ${tags.length} links prefetch={false}`);
    }
  }
  if (!checked) warn("no <Link> found in shared layout", "did the files move?");
}

function maxAgeOf(header) {
  const m = /max-age=(\d+)/.exec(header ?? "");
  return m ? Number(m[1]) : null;
}

async function checkLiveCaching() {
  console.log(`\nLive cache headers: ${SITE}`);
  for (const rule of CACHE_RULES) {
    let res;
    try {
      res = await fetch(SITE + rule.path, { redirect: "follow" });
    } catch (e) {
      fail(`${rule.label} (${rule.path}) unreachable`, String(e.message ?? e));
      continue;
    }
    if (!res.ok) {
      fail(`${rule.label} (${rule.path}) returned ${res.status}`);
      continue;
    }
    const cc = res.headers.get("cache-control");
    const age = maxAgeOf(cc);
    if (age === null) {
      fail(`${rule.label}: no max-age`, `cache-control: ${cc}`);
    } else if (age < rule.min) {
      fail(
        `${rule.label}: max-age=${age}, expected at least ${rule.min}`,
        `every view costs a CDN request at this setting. cache-control: ${cc}`
      );
    } else if (age > rule.max) {
      warn(`${rule.label}: max-age=${age}, higher than the ${rule.max} we intended`);
    } else {
      pass(`${rule.label}: max-age=${age}`);
    }
  }
}

async function checkFingerprintedAssets(html) {
  const chunk = /\/_next\/static\/[^"']+\.(?:js|css)/.exec(html)?.[0];
  if (!chunk) {
    warn("no fingerprinted asset found on the page to check");
    return;
  }
  const res = await fetch(SITE + chunk);
  const cc = res.headers.get("cache-control") ?? "";
  if (/immutable/.test(cc) && (maxAgeOf(cc) ?? 0) >= 2592000) {
    pass("fingerprinted assets immutable", cc);
  } else {
    fail(
      "fingerprinted assets are no longer immutable",
      `a broad Cache-Control rule has probably overridden them. cache-control: ${cc}`
    );
  }
}

async function checkPageWeight() {
  console.log(`\nRequests per page: ${SITE}`);
  let html;
  try {
    html = await (await fetch(SITE + "/")).text();
  } catch (e) {
    fail("could not fetch the homepage", String(e.message ?? e));
    return;
  }
  const scripts = html.match(/<script[^>]+src="/g)?.length ?? 0;
  const links = html.match(/<link[^>]+href="/g)?.length ?? 0;
  const imgs = html.match(/<img[^>]+src="/g)?.length ?? 0;
  const total = 1 + scripts + links + imgs;

  if (total > ASSET_BUDGET) {
    warn(
      `homepage needs ${total} requests, budget is ${ASSET_BUDGET}`,
      `${scripts} scripts, ${links} links, ${imgs} images`
    );
  } else {
    pass(`homepage needs ${total} requests`, `${scripts} scripts, ${links} links, ${imgs} images`);
  }

  await checkFingerprintedAssets(html);
}

console.log("CDN request budget check");
await checkSharedLayoutPrefetch();
if (LIVE) {
  await checkLiveCaching();
  await checkPageWeight();
} else {
  console.log("\n(skipping live checks - pass --live to include them)");
}

console.log(
  `\n${failures} failure(s), ${warnings} warning(s)` +
    (failures ? "\nThese cost CDN requests on every page view. See the notes at the top of this file." : "")
);
process.exit(failures ? 1 : 0);
