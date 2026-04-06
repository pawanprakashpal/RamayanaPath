import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Search Verses",
  description: "Search across all verses of Tulsidas Ramcharitmanas — find chaupais, dohas, chhands by keyword.",
  alternates: { canonical: "/search" },
};

export default function SearchLayout({ children }: { children: React.ReactNode }) {
  return children;
}
