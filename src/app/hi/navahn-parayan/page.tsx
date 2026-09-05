import Link from "next/link";
import type { Metadata } from "next";
import JsonLd from "@/components/seo/JsonLd";
import ParayanPlan from "@/components/parayan/ParayanPlan";
import { BASE_URL, breadcrumbJsonLd, faqPageJsonLd } from "@/lib/seo";
import { languageAlternates } from "@/lib/i18n";

const PATH = "/navahn-parayan";

const TITLE = "नवरात्रि रामायण पाठ — नवाह्न पारायण के नौ विश्राम";
const DESCRIPTION =
  "श्रीरामचरितमानस का परम्परागत नवाह्न पारायण — नवरात्रि की नौ रातों में सम्पूर्ण मानस का पाठ। प्रत्येक दिन का विश्राम, दोहा संख्या सहित, और हिन्दी अर्थ के साथ पूरा पाठ।";

const FAQ = [
  {
    question: "नवाह्न पारायण क्या है?",
    answer:
      "नवाह्न पारायण अर्थात् नौ दिनों में सम्पूर्ण श्रीरामचरितमानस का पाठ। मानस में नौ विश्राम स्थल अंकित हैं, जिनके अनुसार प्रतिदिन एक भाग का पाठ किया जाता है। प्रायः यह नवरात्रि की नौ रातों में किया जाता है।",
  },
  {
    question: "नौ दिनों में मानस किस प्रकार विभाजित है?",
    answer:
      "पहले तीन दिन बालकाण्ड, चौथे से छठे दिन अयोध्याकाण्ड से अरण्यकाण्ड के आरम्भ तक, सातवें दिन शेष अरण्यकाण्ड और सम्पूर्ण किष्किन्धाकाण्ड, आठवें दिन सुन्दरकाण्ड और लंकाकाण्ड, तथा नवें दिन उत्तरकाण्ड की पूर्णाहुति तक।",
  },
  {
    question: "क्या तीस दिनों में भी पाठ किया जा सकता है?",
    answer:
      "हाँ। श्रीरामचरितमानस में मासपारायण के तीस विश्राम भी अंकित हैं, जिनके अनुसार एक महीने में पाठ पूर्ण किया जाता है। नवरात्रि में नवाह्न पारायण की परम्परा है।",
  },
  {
    question: "क्या पाठ का समय निश्चित होना चाहिए?",
    answer:
      "ग्रन्थ में कोई निश्चित नियम नहीं है। सामान्य परम्परा यह है कि नौ दिनों तक एक ही समय रखा जाए और प्रत्येक दिन का भाग एक ही बैठक में पूर्ण किया जाए।",
  },
];

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  keywords: [
    "नवाह्न पारायण",
    "नवरात्रि रामायण पाठ",
    "रामचरितमानस नौ दिन पाठ",
    "मानस विश्राम",
    "अखंड रामायण पाठ",
    "नवरात्रि मानस पाठ",
  ],
  alternates: { canonical: `/hi${PATH}`, languages: languageAlternates(PATH) },
  openGraph: { type: "article", title: TITLE, description: DESCRIPTION, url: `/hi${PATH}`, locale: "hi_IN" },
};

export default function HindiNavahnParayanPage() {
  return (
    <div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-12">
      <JsonLd
        data={breadcrumbJsonLd([
          { name: "मुख्य पृष्ठ", path: "/hi" },
          { name: "नवाह्न पारायण", path: `/hi${PATH}` },
        ])}
      />
      <JsonLd data={faqPageJsonLd(FAQ)} />
      <JsonLd
        data={{
          "@context": "https://schema.org",
          "@type": "HowTo",
          name: TITLE,
          description: DESCRIPTION,
          url: `${BASE_URL}/hi${PATH}`,
          inLanguage: "hi",
          totalTime: "P9D",
          step: [1, 2, 3, 4, 5, 6, 7, 8, 9].map((n) => ({
            "@type": "HowToStep",
            position: n,
            name: `${n}वाँ दिन`,
            url: `${BASE_URL}/hi${PATH}#day-${n}`,
          })),
        }}
      />

      <h1 className="text-3xl sm:text-4xl font-bold mb-3">नवरात्रि रामायण पाठ</h1>
      <p className="text-lg text-[var(--muted)] mb-4">
        नवाह्न पारायण — नवरात्रि की नौ रातों में सम्पूर्ण श्रीरामचरितमानस का पाठ।
      </p>

      <div className="card p-5 mb-8">
        <p className="text-sm leading-relaxed text-[var(--muted)]">
          श्रीरामचरितमानस में पाठ के लिए विश्राम स्थल स्वयं अंकित हैं। एक ओर तीस विश्रामों
          का मासपारायण है, जिससे एक महीने में पाठ पूर्ण होता है; दूसरी ओर नौ विश्राम, जिनसे
          ग्रन्थ नौ दिनों में बँट जाता है। नवरात्रि का पाठ इन्हीं नौ विश्रामों के अनुसार
          किया जाता है। नीचे प्रत्येक दिन का भाग दिया गया है — हिन्दी अर्थ सहित सम्पूर्ण
          पाठ से जुड़ा हुआ।
        </p>
      </div>

      <ParayanPlan lang="hi" />

      <section className="mt-12 card p-6" aria-labelledby="parayan-faq">
        <h2 id="parayan-faq" className="text-xl font-semibold mb-4">
          सामान्य प्रश्न
        </h2>
        <div className="space-y-4">
          {FAQ.map((item) => (
            <div key={item.question}>
              <h3 className="font-medium">{item.question}</h3>
              <p className="text-sm text-[var(--muted)] mt-1">{item.answer}</p>
            </div>
          ))}
        </div>
      </section>

      <p className="mt-8 text-sm">
        <Link href="/navahn-parayan" className="text-[var(--accent)] hover:underline">
          Read in English →
        </Link>
      </p>
    </div>
  );
}
