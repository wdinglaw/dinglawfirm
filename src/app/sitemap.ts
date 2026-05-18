import type { MetadataRoute } from "next";
import { site } from "@/data/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = [
    "",
    "/practice-areas",
    "/attorney-profile",
    "/approach",
    "/fees-consultation",
    "/faq",
    "/contact",
    "/san-jose-divorce-attorney",
    "/santa-clara-county-child-custody-attorney",
  ];

  const now = new Date();

  return routes.map((route) => ({
    url: `${site.baseUrl}${route}`,
    lastModified: now,
    changeFrequency: "weekly",
    priority: route === "" ? 1 : 0.8,
  }));
}
