import type { Metadata } from "next";
import Link from "next/link";
import PageIntro from "@/components/PageIntro";
import { practiceAreas } from "@/data/site";

export const metadata: Metadata = {
  title: "Practice Areas - Divorce, Custody, Support, and Property Division",
  description:
    "Family law services in San Jose and Santa Clara County, including divorce, custody, support, domestic violence restraining orders, and property division.",
  alternates: { canonical: "/practice-areas" },
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
      <section className="section-shell pt-0">
        <div className="rounded border border-line bg-white p-6 shadow-panel">
          <h2 className="font-display text-2xl text-ink">Explore Local Family Law Topics</h2>
          <p className="mt-3 text-charcoal/90">
            For location-focused guidance, visit
            <Link className="ml-1 text-mutedBlue" href="/san-jose-divorce-attorney">San Jose Divorce Attorney</Link>
            and
            <Link className="ml-1 text-mutedBlue" href="/santa-clara-county-child-custody-attorney">Santa Clara County Child Custody Attorney</Link>.
          </p>
        </div>
      </section>
    </>
  );
}
