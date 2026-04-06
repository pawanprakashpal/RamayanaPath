import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Bookmarks",
  description: "Your saved bookmarks from Tulsidas Ramcharitmanas and Valmiki Ramayana verses.",
  alternates: { canonical: "/bookmarks" },
};

export default function BookmarksLayout({ children }: { children: React.ReactNode }) {
  return children;
}
