import { notFound } from "next/navigation";
import Link from "next/link";
import { getKandBySlug, getTulsidasKand, getValmikiTotalSargas } from "@/lib/data";
import { getServerVersion } from "@/lib/version";

interface KandLayoutProps {
  children: React.ReactNode;
  params: Promise<{ kand: string }>;
}

export default async function KandLayout({ children, params }: KandLayoutProps) {
  const { kand: kandSlug } = await params;
  const kand = await getKandBySlug(kandSlug);

  if (!kand) notFound();

  const isAvailable = kand.tulsidas.available || kand.valmiki.available;
  if (!isAvailable) notFound();

  const version = await getServerVersion();

  let sidebarItems: { label: string; href: string }[] = [];

  if (version === "tulsidas") {
    const data = await getTulsidasKand(kandSlug);
    if (data) {
      sidebarItems = data.dohaGroups.map((g) => ({
        label: g.label ?? `Doha ${g.dohaNumber}`,
        href: `/${kandSlug}/doha/${g.dohaNumber}`,
      }));
    }
  } else {
    const totalSargas = await getValmikiTotalSargas(kandSlug);
    for (let i = 1; i <= totalSargas; i++) {
      sidebarItems.push({
        label: `Sarga ${i}`,
        href: `/${kandSlug}/sarga/${i}`,
      });
    }
  }

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
      <div className="flex gap-8">
        {/* Sidebar */}
        <aside className="hidden lg:block w-64 flex-shrink-0">
          <div className="sticky top-24">
            <h2 className="text-sm font-semibold text-[var(--muted)] uppercase tracking-wider mb-3">
              {version === "tulsidas" ? kand.tulsidas.name : kand.valmiki.name}
            </h2>
            <nav className="space-y-1 max-h-[calc(100vh-8rem)] overflow-y-auto pr-2">
              {sidebarItems.map((item) => (
                <Link
                  key={item.href}
                  href={item.href}
                  className="block text-sm px-3 py-1.5 rounded-md text-[var(--muted)] hover:text-[var(--foreground)] hover:bg-[var(--verse-bg)] transition-colors"
                >
                  {item.label}
                </Link>
              ))}
            </nav>
          </div>
        </aside>

        {/* Main content */}
        <div className="flex-1 min-w-0">{children}</div>
      </div>
    </div>
  );
}
