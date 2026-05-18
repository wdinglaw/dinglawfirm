import type { Metadata } from "next";
import PageIntro from "@/components/PageIntro";

export const metadata: Metadata = {
  title: "Approach - What to Expect in a Family Law Matter",
  description:
    "Learn the firm's process for divorce and custody matters in Santa Clara County, from consultation and planning through resolution.",
  alternates: { canonical: "/approach" },
};

const steps = [
  {
    title: "1. Initial Consultation",
    text: "We clarify your priorities, immediate risks, and procedural posture, then outline realistic options.",
  },
  {
    title: "2. Strategic Case Planning",
    text: "We identify key facts, documents, and deadlines, and build a tailored plan for negotiation or litigation.",
  },
  {
    title: "3. Focused Execution",
    text: "Filings, disclosures, settlement proposals, and hearings are prepared with detail and purpose.",
  },
  {
    title: "4. Practical Resolution",
    text: "We pursue durable outcomes that align with your legal position, family obligations, and long-term stability.",
  },
];

export default function ApproachPage() {
  return (
    <>
      <PageIntro
        eyebrow="What To Expect"
        title="A Calm, Strategic Process"
        description="Every case is different, but the framework is consistent: assess carefully, prepare thoroughly, and move with intention."
      />
      <section className="section-shell grid gap-4 md:grid-cols-2">
        {steps.map((step) => (
          <article key={step.title} className="rounded border border-line bg-white p-6 shadow-panel">
            <h2 className="font-display text-2xl text-ink">{step.title}</h2>
            <p className="mt-3 text-charcoal/85">{step.text}</p>
          </article>
        ))}
      </section>
    </>
  );
}
