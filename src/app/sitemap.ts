import type { MetadataRoute } from "next";
import { getKandManifest, getTulsidasKand, getValmikiSargaNumbers } from "@/lib/data";
import { BASE_URL } from "@/lib/seo";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const manifest = await getKandManifest();
  const entries: MetadataRoute.Sitemap = [];
  const lastModified = new Date();

  // Home page
  entries.push({
    url: BASE_URL,
    lastModified,
    changeFrequency: "weekly",
    priority: 1,
  });

  for (const kand of manifest.kands) {
    // Kand overview page
    entries.push({
      url: `${BASE_URL}/${kand.slug}`,
      lastModified,
      changeFrequency: "monthly",
      priority: 0.9,
    });

    // Tulsidas doha pages — derived from the data so the sitemap can never
    // advertise a URL that 404s (or miss one that exists).
    if (kand.tulsidas.available) {
      // Full-text paath page — a primary landing target, so it ranks above
      // the individual doha pages.
      entries.push({
        url: `${BASE_URL}/${kand.slug}/paath`,
        lastModified,
        changeFrequency: "monthly",
        priority: 0.9,
      });

      const data = await getTulsidasKand(kand.slug);
      for (const group of data?.dohaGroups ?? []) {
        entries.push({
          url: `${BASE_URL}/${kand.slug}/doha/${group.dohaNumber}`,
          lastModified,
          changeFrequency: "monthly",
          priority: 0.7,
        });
      }
    }

    // Valmiki sarga pages
    if (kand.valmiki.available) {
      for (const sargaNumber of await getValmikiSargaNumbers(kand.slug)) {
        entries.push({
          url: `${BASE_URL}/${kand.slug}/sarga/${sargaNumber}`,
          lastModified,
          changeFrequency: "monthly",
          priority: 0.7,
        });
      }
    }
  }

  // Static pages
  entries.push({
    url: `${BASE_URL}/about`,
    lastModified,
    changeFrequency: "monthly",
    priority: 0.6,
  });

  entries.push({
    url: `${BASE_URL}/search`,
    lastModified,
    changeFrequency: "monthly",
    priority: 0.5,
  });

  entries.push({
    url: `${BASE_URL}/bookmarks`,
    lastModified,
    changeFrequency: "monthly",
    priority: 0.4,
  });

  return entries;
}
