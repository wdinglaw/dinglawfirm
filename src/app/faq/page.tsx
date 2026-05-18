import type { Metadata } from "next";
import PageIntro from "@/components/PageIntro";
import { faqs } from "@/data/site";

export const metadata: Metadata = {
  title: "FAQ - California Family Law",
  description: "Frequently asked questions on California divorce, custody, disclosures, consultation preparation, and legal fees.",
  alternates: { canonical: "/faq" },
};

const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: faqs.map((faq) => ({
    "@type": "Question",
    name: faq.question,
    acceptedAnswer: {
      "@type": "Answer",
      text: faq.answer,
    },
  })),
};

export default function FAQPage() {
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }} />
      <PageIntro
        eyebrow="FAQ"
        title="Frequently Asked Questions"
        description="General information for prospective family law clients in Santa Clara County and the Bay Area."
      />
      <section className="section-shell">
        <div className="grid gap-4">
          {faqs.map((faq) => (
            <article key={faq.question} className="rounded border border-line bg-white p-6 shadow-panel">
              <h2 className="font-display text-2xl text-ink">{faq.question}</h2>
              <p className="mt-3 text-charcoal/90">{faq.answer}</p>
            </article>
          ))}
        </div>
      </section>
    </>
  );
}
