import type { Metadata } from "next";
import PageIntro from "@/components/PageIntro";
import { faqs } from "@/data/site";

export const metadata: Metadata = {
  title: "FAQ",
  description: "Frequently asked questions about California divorce, custody, disclosures, fees, and representation.",
};

export default function FAQPage() {
  return (
    <>
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
