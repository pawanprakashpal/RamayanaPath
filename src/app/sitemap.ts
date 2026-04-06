import type { MetadataRoute } from "next";
import { getKandManifest } from "@/lib/data";

const BASE_URL = "https://ramayanpath.com";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const manifest = await getKandManifest();
  const entries: MetadataRoute.Sitemap = [];

  // Home page
  entries.push({
    url: BASE_URL,
    lastModified: new Date(),
    changeFrequency: "weekly",
    priority: 1,
  });

  // Kand listing pages + all doha pages
  for (const kand of manifest.kands) {
    // Kand overview page
    entries.push({
      url: `${BASE_URL}/${kand.slug}`,
      lastModified: new Date(),
      changeFrequency: "monthly",
      priority: 0.9,
    });

    // All doha pages for this kand
    if (kand.tulsidas.available) {
      for (let i = 0; i <= kand.tulsidas.totalUnits; i++) {
        entries.push({
          url: `${BASE_URL}/${kand.slug}/doha/${i}`,
          lastModified: new Date(),
          changeFrequency: "monthly",
          priority: 0.7,
        });
      }
    }
  }

  // Static pages
  entries.push({
    url: `${BASE_URL}/about`,
    lastModified: new Date(),
    changeFrequency: "monthly",
    priority: 0.6,
  });

  entries.push({
    url: `${BASE_URL}/search`,
    lastModified: new Date(),
    changeFrequency: "monthly",
    priority: 0.5,
  });

  entries.push({
    url: `${BASE_URL}/bookmarks`,
    lastModified: new Date(),
    changeFrequency: "monthly",
    priority: 0.4,
  });

  return entries;
}
