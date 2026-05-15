import type { Metadata } from "next";
import PageIntro from "@/components/PageIntro";
import { practiceAreas } from "@/data/site";

export const metadata: Metadata = {
  title: "Practice Areas",
  description: "Divorce, custody, support, property division, domestic violence restraining orders, and related family law services.",
};

export default function PracticeAreasPage() {
  return (
    <>
      <PageIntro
        eyebrow="Services"
        title="Practice Areas"
        description="Targeted family law representation focused on practical outcomes, careful preparation, and clear communication."
      />
      <section className="section-shell grid gap-4 md:grid-cols-2">
        {practiceAreas.map((area) => (
          <article key={area} className="rounded border border-line bg-white p-6 shadow-panel">
            <h2 className="font-display text-2xl text-ink">{area}</h2>
            <p className="mt-2 text-charcoal/85">
              Strategy and execution tailored to the facts, timeline, and court posture of your matter.
            </p>
          </article>
        ))}
      </section>
    </>
  );
}
