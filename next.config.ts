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
    ];
  },
};

export default nextConfig;
