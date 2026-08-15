import { notFound } from "next/navigation";
import Link from "next/link";
import { getKandBySlug, getTulsidasKand, getValmikiSargaNumbers } from "@/lib/data";
import { dohaTitle } from "@/lib/seo";
import VersionSwitchedSidebar from "@/components/navigation/VersionSwitchedSidebar";

interface KandLayoutProps {
  children: React.ReactNode;
  params: Promise<{ kand: string }>;
}

// Every Kand is known up front, so the layout can be prerendered along with
// its doha and sarga pages.
export async function generateStaticParams() {
  const { getKandManifest } = await import("@/lib/data");
  const manifest = await getKandManifest();
  return manifest.kands.map((k) => ({ kand: k.slug }));
}

function SidebarNav({ items }: { items: { label: string; href: string }[] }) {
  return (
    <nav className="space-y-1 max-h-[calc(100vh-8rem)] overflow-y-auto pr-2">
      {items.map((item) => (
        <Link
          key={item.href}
          href={item.href}
          className="block text-sm px-3 py-1.5 rounded-md text-[var(--muted)] hover:text-[var(--foreground)] hover:bg-[var(--verse-bg)] transition-colors"
        >
          {item.label}
        </Link>
      ))}
    </nav>
  );
}

export default async function KandLayout({ children, params }: KandLayoutProps) {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);

  if (!kand) notFound();

  const isAvailable = kand.tulsidas.available || kand.valmiki.available;
  if (!isAvailable) notFound();

  const [data, sargaNumbers] = await Promise.all([
    getTulsidasKand(kandSlug),
    getValmikiSargaNumbers(kandSlug),
  ]);

  const dohaItems = (data?.dohaGroups ?? []).map((g) => ({
    label: dohaTitle(g.dohaNumber, g.label),
    href: `/${kandSlug}/doha/${g.dohaNumber}`,
  }));

  const sargaItems = sargaNumbers.map((n) => ({
    label: `Sarga ${n}`,
    href: `/${kandSlug}/sarga/${n}`,
  }));

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
      <div className="flex gap-8">
        {/* Sidebar */}
        <aside className="hidden lg:block w-64 flex-shrink-0">
          <div className="sticky top-24">
            <VersionSwitchedSidebar
              tulsidasName={kand.tulsidas.name}
              valmikiName={kand.valmiki.name}
              tulsidas={<SidebarNav items={dohaItems} />}
              valmiki={<SidebarNav items={sargaItems} />}
            />
          </div>
        </aside>

        {/* Main content */}
        <div className="flex-1 min-w-0">{children}</div>
      </div>
    </div>
  );
}
