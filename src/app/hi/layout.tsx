/**
 * The root layout hard-codes <html lang="en">, and a nested layout cannot
 * change it. Marking the subtree lang="hi" is the correct signal for crawlers
 * and screen readers short of restructuring every route under a [lang]
 * segment — which would move the English URLs Google has already indexed.
 */
export default function HindiLayout({ children }: { children: React.ReactNode }) {
  return (
    <div lang="hi" className="font-devanagari">
      {children}
    </div>
  );
}
