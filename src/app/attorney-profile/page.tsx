import type { Metadata } from "next";
import PageIntro from "@/components/PageIntro";

export const metadata: Metadata = {
  title: "Attorney Profile - Wenyu Ding, Esq.",
  description:
    "Meet Wenyu Ding, Esq., founder and California family law attorney focused on divorce, custody, support, property division, and family law litigation.",
  alternates: { canonical: "/attorney-profile" },
};

export default function AttorneyProfilePage() {
  return (
    <>
      <PageIntro
        eyebrow="Attorney"
        title="Wenyu Ding, Esq."
        description="Founder and California Family Law Attorney"
      />
      <section className="section-shell">
        <article className="max-w-5xl rounded border border-line bg-white p-8 shadow-panel">
          <p className="leading-relaxed text-charcoal/90">
            Wenyu Ding is a California family law attorney and founder of the Law Offices of Wenyu Ding. His practice focuses on divorce, child custody and visitation, child and spousal support, property division, domestic violence restraining orders, and prenuptial and postnuptial agreements.
          </p>
          <p className="mt-5 leading-relaxed text-charcoal/90">
            Mr. Ding represents clients in both negotiated and contested family law matters, including cases involving high-conflict custody disputes, complex financial and disclosure issues, support claims, move-away requests, and the characterization and division of marital property. He works with professionals, business owners, dual-income households, and other clients facing legal disputes with significant personal and financial consequences.
          </p>
          <p className="mt-5 leading-relaxed text-charcoal/90">
            Mr. Ding has family law trial experience and has successfully obtained permanent restraining orders and orders awarding sole legal and physical custody. He approaches each matter with careful preparation, practical strategy, and close attention to the facts and circumstances affecting the client and the client’s family.
          </p>
          <p className="mt-5 leading-relaxed text-charcoal/90">
            Before establishing his own practice, Mr. Ding worked as a civil defense litigator representing corporate clients in matters involving complex tort claims and automobile accidents. This prior litigation experience strengthened his ability to analyze detailed factual records, evaluate risk, manage contested proceedings, and advocate effectively in court.
          </p>
          <p className="mt-5 leading-relaxed text-charcoal/90">
            Known for his direct communication and detail-driven approach, Mr. Ding works closely with clients to identify their priorities, understand their legal options, and develop a strategy suited to the circumstances of the case. He is committed to providing compassionate, fair, and effective representation while helping clients navigate difficult legal proceedings with greater clarity and confidence.
          </p>
          <p className="mt-5 leading-relaxed text-charcoal/90">
            Mr. Ding earned his Juris Doctor from the University of California, Davis School of Law and his Bachelor of Arts from the University of California, Berkeley. He is licensed to practice before the courts of the State of California and is an active member of the Santa Clara County Bar Association.
          </p>
          <p className="mt-5 leading-relaxed text-charcoal/90">
            Mr. Ding speaks English and conversational Mandarin Chinese, allowing him to communicate with clients from a range of cultural and linguistic backgrounds.
          </p>

          <div className="mt-8 grid gap-4 md:grid-cols-2">
            <section className="rounded border border-line bg-cream/60 p-5">
              <h2 className="font-display text-xl text-ink">Education</h2>
              <ul className="mt-3 list-disc space-y-1 pl-5 text-sm leading-relaxed text-charcoal/85">
                <li>Juris Doctor, University of California, Davis School of Law</li>
                <li>Bachelor of Arts, University of California, Berkeley</li>
              </ul>
            </section>
            <section className="rounded border border-line bg-cream/60 p-5">
              <h2 className="font-display text-xl text-ink">Bar Admission</h2>
              <ul className="mt-3 list-disc space-y-1 pl-5 text-sm leading-relaxed text-charcoal/85">
                <li>State Bar of California</li>
              </ul>
            </section>
            <section className="rounded border border-line bg-cream/60 p-5">
              <h2 className="font-display text-xl text-ink">Professional Association</h2>
              <ul className="mt-3 list-disc space-y-1 pl-5 text-sm leading-relaxed text-charcoal/85">
                <li>Santa Clara County Bar Association</li>
              </ul>
            </section>
            <section className="rounded border border-line bg-cream/60 p-5">
              <h2 className="font-display text-xl text-ink">Languages</h2>
              <ul className="mt-3 list-disc space-y-1 pl-5 text-sm leading-relaxed text-charcoal/85">
                <li>English</li>
                <li>Conversational Mandarin Chinese</li>
              </ul>
            </section>
            <section className="rounded border border-line bg-cream/60 p-5 md:col-span-2">
              <h2 className="font-display text-xl text-ink">Practice Areas</h2>
              <ul className="mt-3 columns-1 list-disc space-y-1 pl-5 text-sm leading-relaxed text-charcoal/85 md:columns-2">
                <li>Divorce and Legal Separation</li>
                <li>Child Custody and Visitation</li>
                <li>Move-Away and Relocation Matters</li>
                <li>Child Support</li>
                <li>Spousal Support</li>
                <li>Property and Asset Division</li>
                <li>Financial Disclosures</li>
                <li>Domestic Violence Restraining Orders</li>
                <li>Prenuptial Agreements</li>
                <li>Postnuptial Agreements</li>
                <li>Marital Settlement Agreements</li>
                <li>Family Law Litigation and Negotiation</li>
              </ul>
            </section>
          </div>
        </article>
      </section>
    </>
  );
}
