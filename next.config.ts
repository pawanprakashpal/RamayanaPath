import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // The search route reads the verse JSON at runtime via a computed path, which
  // file tracing cannot follow — without this the data is missing in production.
  outputFileTracingIncludes: {
    "/api/search": ["./data/**/*.json"],
  },
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          { key: "X-Frame-Options", value: "DENY" },
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
        ],
      },
      // The three Cache-Control rules below overlap on purpose, broadest
      // first: a later rule wins for a key it repeats, so the icons and the
      // manifest keep their own lifetimes rather than the page one.
      {
        // Prerendered pages are served max-age=0, must-revalidate by default,
        // so the browser must ask the CDN again for a page it already holds -
        // and on a site read a page at a time, that is most of our traffic.
        // The verses do not change, so five minutes of browser cache costs
        // nothing and covers moving back and forth within a sitting.
        //
        // Kept deliberately short rather than hours: the HTML names the
        // fingerprinted JS chunks of the build that produced it, and a page
        // held too long after a deploy would be asking for chunks that have
        // moved on.
        source: "/:path((?!_next/|api/).*)",
        headers: [
          { key: "Cache-Control", value: "public, max-age=300, must-revalidate" },
        ],
      },
      {
        // Files in public/ are served with max-age=0, must-revalidate, so the
        // browser re-asks for the favicon on every page view. On a site people
        // read a page at a time that made icons and the manifest 11% of all
        // CDN requests - more than the entire JS bundle, which is fingerprinted
        // and cached for a year. These names are stable and the files almost
        // never change, so a month costs nothing and a changed icon still
        // arrives within one.
        source: "/:file(favicon.ico|favicon.svg|favicon-16x16.png|favicon-32x32.png|apple-touch-icon.png|android-chrome-192x192.png|android-chrome-512x512.png|ram-icon.png|ram-icon.svg)",
        headers: [
          { key: "Cache-Control", value: "public, max-age=2592000" },
        ],
      },
      {
        // Shorter, because the manifest changes more readily than an icon.
        source: "/manifest.json",
        headers: [
          { key: "Cache-Control", value: "public, max-age=86400" },
        ],
      },
    ];
  },
};

export default nextConfig;
