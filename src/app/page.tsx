import { getAvailableKands } from "@/lib/data";
import KandCard from "@/components/home/KandCard";

export default async function HomePage() {
  const kands = await getAvailableKands();

  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12">
      {/* Hero */}
      <div className="text-center mb-12">
        <h1 className="text-4xl sm:text-5xl font-bold mb-4">
          <span className="text-[var(--accent)]">Ramayana</span>Path
        </h1>
        <p className="font-devanagari text-2xl text-[var(--muted)] mb-4">
          श्रीरामचरितमानस
        </p>
        <p className="text-lg text-[var(--muted)] max-w-2xl mx-auto">
          Read the epic Ramayana with original verses and English translations.
          Choose between Tulsidas&apos;s Ramcharitmanas and Valmiki&apos;s Sanskrit original.
        </p>
      </div>

      {/* Kand Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {kands.map((kand) => (
          <KandCard key={kand.slug} kand={kand} />
        ))}
      </div>

      {/* Info section */}
      <div className="mt-16 text-center">
        <div className="card max-w-3xl mx-auto p-8">
          <h2 className="text-xl font-semibold mb-4">Two Versions, One Epic</h2>
          <div className="grid sm:grid-cols-2 gap-6 text-left">
            <div>
              <h3 className="font-medium text-[var(--accent)] mb-2">Tulsidas Ramcharitmanas</h3>
              <p className="text-sm text-[var(--muted)]">
                Written in Awadhi (Hindi) in the 16th century by Goswami Tulsidas.
                The most widely recited version in North India, composed in Chaupai
                and Doha verse forms.
              </p>
            </div>
            <div>
              <h3 className="font-medium text-[var(--accent)] mb-2">Valmiki Ramayana</h3>
              <p className="text-sm text-[var(--muted)]">
                The original Sanskrit epic by Maharshi Valmiki, considered the Adi Kavya
                (first poem). Composed in Shloka metre, it is the foundational text
                of the Ramayana tradition.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
