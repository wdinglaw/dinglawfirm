import type { Metadata } from "next";
import PageIntro from "@/components/PageIntro";
import ContactForm from "@/components/ContactForm";
import { site } from "@/data/site";

export const metadata: Metadata = {
  title: "Contact - Schedule a Family Law Consultation",
  description:
    "Contact the Law Offices of Wenyu Ding in San Jose to request a consultation for divorce, custody, support, and related family law matters.",
  alternates: { canonical: "/contact" },
};

export default function ContactPage() {
  return (
    <>
      <PageIntro
        eyebrow="Contact"
        title="Schedule a Consultation"
        description="Use the form below to request an appointment. Submissions do not create an attorney-client relationship."
      />
      <section className="section-shell grid gap-8 md:grid-cols-[1.2fr_0.8fr]">
        <div className="rounded border border-line bg-white p-6 shadow-panel md:p-8">
          <ContactForm />
        </div>
        <aside className="rounded border border-line bg-white p-6 shadow-panel md:p-8">
          <h2 className="font-display text-2xl text-ink">Office Information</h2>
          <p className="mt-4 text-sm text-charcoal/90">{site.location}</p>
          <p className="mt-3 text-sm">
            Phone: <a href={site.phoneLink} className="text-mutedBlue">{site.phoneDisplay}</a>
          </p>
          <p className="text-sm">
            Email: <a href={`mailto:${site.email}`} className="text-mutedBlue">{site.email}</a>
          </p>
          <p className="mt-5 text-sm text-charcoal/80">
            Consultations are by appointment only.
          </p>
        </aside>
      </section>
    </>
  );
}
