#!/usr/bin/env node
/** Run after `next build` with output: export. See build-cf-assets.mjs. */
import { pruneSegmentPayloads } from "./build-cf-assets.mjs";
const removed = await pruneSegmentPayloads("out");
console.log(`  pruned ${removed.toLocaleString()} segment payload files from out/`);
