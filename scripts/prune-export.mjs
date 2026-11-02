#!/usr/bin/env node
/** Run after `next build` with output: export. See build-cf-assets.mjs. */
import { rm } from "node:fs/promises";
import { pruneSegmentPayloads } from "./build-cf-assets.mjs";

const removed = await pruneSegmentPayloads("out");
console.log(`  pruned ${removed.toLocaleString()} segment payload files from out/`);

// The search index is written for a D1 loader that does not exist yet; the
// search Function answers without it. At 41 MB it is also over Pages' 25 MiB
// per-file limit, so leaving it in out/ would fail the whole deploy.
await rm("out/search/index.json", { force: true });
console.log("  removed out/search/index.json (over the per-file limit; unused until D1)");
