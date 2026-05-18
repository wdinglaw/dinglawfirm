import type { Metadata } from "next";
import Link from "next/link";
import PageIntro from "@/components/PageIntro";

export const metadata: Metadata = {
  title: "San Jose Divorce Attorney",
  description:
    "Strategic divorce representation in San Jose, California for custody, support, property division, and settlement planning.",
  alternates: { canonical: "/san-jose-divorce-attorney" },
};

export default function SanJoseDivorceAttorneyPage() {
  return (
    <>
      <PageIntro
        eyebrow="San Jose Family Law"
        title="San Jose Divorce Attorney"
        description="Boutique divorce counsel for clients in San Jose who need clear legal strategy, disciplined preparation, and practical resolution planning."
      />
      <section className="section-shell grid gap-6 md:grid-cols-2">
        <article className="rounded border border-line bg-white p-6 shadow-panel">
          <h2 className="font-display text-2xl text-ink">Divorce matters handled with precision</h2>
          <p className="mt-3 text-charcoal/90">
            Representation includes petition and response strategy, temporary orders, parenting plans, support analysis, property characterization, disclosures, and settlement structuring.
          </p>
        </article>
        <article className="rounded border border-line bg-white p-6 shadow-panel">
          <h2 className="font-display text-2xl text-ink">Built for high-responsibility clients</h2>
          <p className="mt-3 text-charcoal/90">
            This firm is often a fit for professionals and business owners who prioritize organization, responsiveness, and credible advocacy in Santa Clara County family court matters.
          </p>
        </article>
      </section>
      <section className="section-shell pt-0">
        <div className="rounded border border-line bg-white p-6 shadow-panel">
          <h2 className="font-display text-2xl text-ink">Related Services</h2>
          <p className="mt-3 text-charcoal/90">
            See the full <Link className="text-mutedBlue" href="/practice-areas">practice areas</Link> or
            <Link className="ml-1 text-mutedBlue" href="/contact">schedule a consultation</Link>.
          </p>
        </div>
      </section>
    </>
  );
}
