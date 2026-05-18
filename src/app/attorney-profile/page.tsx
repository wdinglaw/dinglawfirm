import type { Metadata } from "next";
import PageIntro from "@/components/PageIntro";

export const metadata: Metadata = {
  title: "Attorney Profile - Wenyu Ding, Esq.",
  description:
    "Meet Wenyu Ding, Esq., a San Jose family law attorney focused on strategic divorce and custody representation in Santa Clara County.",
  alternates: { canonical: "/attorney-profile" },
};

export default function AttorneyProfilePage() {
  return (
    <>
      <PageIntro
        eyebrow="Attorney"
        title="Wenyu Ding, Esq."
        description="Family law counsel grounded in preparation, discretion, and practical strategy."
      />
      <section className="section-shell">
        <article className="max-w-4xl rounded border border-line bg-white p-8 shadow-panel">
          <p className="leading-relaxed text-charcoal/90">
            Wenyu Ding, Esq. represents clients in California family law matters, including divorce, custody, support, property division, domestic violence restraining orders, and settlement negotiations. His practice is designed for clients who want direct attorney communication, thoughtful case planning, and clear expectations from the start.
          </p>
          <p className="mt-5 leading-relaxed text-charcoal/90">
            He works with clients throughout Santa Clara County and the Bay Area, with attention to the practical realities that shape each matter: timelines, court requirements, financial documentation, and family dynamics. Whether a case is expected to settle or proceed through contested hearings, his approach centers on careful preparation and disciplined decision-making.
          </p>
          <p className="mt-5 leading-relaxed text-charcoal/90">
            Clients choose the Law Offices of Wenyu Ding for focused representation and steady guidance during high-stakes transitions. The goal is not unnecessary conflict. The goal is to protect long-term interests with strategy, responsiveness, and credible advocacy.
          </p>
        </article>
      </section>
    </>
  );
}
