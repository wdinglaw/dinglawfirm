import type { Metadata } from "next";
import Link from "next/link";
import PageIntro from "@/components/PageIntro";

export const metadata: Metadata = {
  title: "Fees and Consultation",
  description:
    "Consultation and fee information for family law representation in Santa Clara County, including appointment policy and retainer expectations.",
  alternates: { canonical: "/fees-consultation" },
};

export default function FeesConsultationPage() {
  return (
    <>
      <PageIntro
        eyebrow="Engagement"
        title="Fees and Consultation"
        description="Consultations are by appointment only. The firm offers clear expectations regarding scope, process, and billing before representation begins."
      />
      <section className="section-shell">
        <article className="max-w-4xl rounded border border-line bg-white p-8 shadow-panel">
          <h2 className="font-display text-2xl text-ink">Consultation Policy</h2>
          <p className="mt-3 text-charcoal/90">
            Consultations are scheduled by appointment only after a basic conflict check and matter screening. Consultation time is reserved for focused legal analysis and next-step planning.
          </p>

          <h2 className="mt-8 font-display text-2xl text-ink">Fees and Retainers</h2>
          <p className="mt-3 text-charcoal/90">
            Retainers and legal fees depend on the expected scope of representation, urgency, procedural posture, and complexity of the issues involved. You will receive clear terms regarding billing structure and engagement conditions before representation begins.
          </p>

          <h2 className="mt-8 font-display text-2xl text-ink">Limited-Scope Services</h2>
          <p className="mt-3 text-charcoal/90">
            Limited-scope representation may be available for appropriate matters, such as targeted hearing preparation or settlement support, when the requested scope is clearly defined.
          </p>

          <Link href="/contact" className="mt-8 inline-block rounded bg-ink px-5 py-3 text-sm font-semibold text-white transition hover:bg-mutedBlue">
            Request a Consultation
          </Link>
        </article>
      </section>
    </>
  );
}
