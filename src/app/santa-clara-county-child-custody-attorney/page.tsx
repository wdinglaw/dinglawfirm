import type { Metadata } from "next";
import Link from "next/link";
import PageIntro from "@/components/PageIntro";

export const metadata: Metadata = {
  title: "Santa Clara County Child Custody Attorney",
  description:
    "Child custody and visitation representation in Santa Clara County, including move-away requests, temporary orders, and post-judgment modifications.",
  alternates: { canonical: "/santa-clara-county-child-custody-attorney" },
};

export default function SantaClaraCountyChildCustodyAttorneyPage() {
  return (
    <>
      <PageIntro
        eyebrow="Santa Clara County Custody"
        title="Santa Clara County Child Custody Attorney"
        description="Focused custody and visitation representation for parents addressing parenting plans, schedule disputes, and child-centered solutions."
      />
      <section className="section-shell grid gap-6 md:grid-cols-2">
        <article className="rounded border border-line bg-white p-6 shadow-panel">
          <h2 className="font-display text-2xl text-ink">Custody and visitation disputes</h2>
          <p className="mt-3 text-charcoal/90">
            Support includes temporary custody requests, visitation schedules, school and holiday planning, enforcement issues, and modification requests based on changed circumstances.
          </p>
        </article>
        <article className="rounded border border-line bg-white p-6 shadow-panel">
          <h2 className="font-display text-2xl text-ink">Move-away and relocation cases</h2>
          <p className="mt-3 text-charcoal/90">
            Move-away matters require careful evidence development and practical planning. Representation focuses on protecting stability and presenting persuasive, fact-driven proposals.
          </p>
        </article>
      </section>
      <section className="section-shell pt-0">
        <div className="rounded border border-line bg-white p-6 shadow-panel">
          <h2 className="font-display text-2xl text-ink">Next Steps</h2>
          <p className="mt-3 text-charcoal/90">
            Review the firm&apos;s <Link className="text-mutedBlue" href="/approach">approach</Link> and
            <Link className="ml-1 text-mutedBlue" href="/fees-consultation">consultation policy</Link>, or
            <Link className="ml-1 text-mutedBlue" href="/contact">request an appointment</Link>.
          </p>
        </div>
      </section>
    </>
  );
}
