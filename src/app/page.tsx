import Link from "next/link";
import { practiceAreas, site } from "@/data/site";

export default function HomePage() {
  return (
    <>
      <section className="border-b border-line bg-quiet-grid bg-grid">
        <div className="section-shell">
          <p className="eyebrow">Santa Clara County Family Law</p>
          <h1 className="mt-4 max-w-4xl font-display text-4xl leading-tight text-ink md:text-6xl">
            Strategic Family Law Representation for Silicon Valley Families
          </h1>
          <p className="mt-6 max-w-3xl text-lg leading-relaxed text-charcoal/90">
            Boutique divorce and custody counsel for clients who need clear advice, careful preparation, and practical solutions in Santa Clara County and the Bay Area.
          </p>
          <div className="mt-8 flex flex-wrap gap-4">
            <Link href="/contact" className="rounded bg-ink px-5 py-3 text-sm font-semibold text-white transition hover:bg-mutedBlue">
              Schedule a Consultation
            </Link>
            <Link href="/practice-areas" className="rounded border border-ink px-5 py-3 text-sm font-semibold text-ink transition hover:bg-white">
              View Practice Areas
            </Link>
          </div>
        </div>
      </section>

      <section className="border-b border-line bg-white">
        <div className="section-shell grid gap-6 md:grid-cols-2">
          <div>
            <p className="eyebrow">Focused Representation</p>
            <h2 className="mt-3 font-display text-3xl text-ink">Careful preparation with direct attorney involvement</h2>
          </div>
          <ul className="space-y-4 text-charcoal/90">
            <li>Family law-focused representation from intake through resolution.</li>
            <li>Direct communication with Wenyu Ding, Esq., not passed between multiple handlers.</li>
            <li>Realistic guidance designed to protect time, finances, and long-term stability.</li>
            <li>Strategic planning for negotiation, settlement, and litigation when needed.</li>
          </ul>
        </div>
      </section>

      <section className="border-b border-line bg-cream">
        <div className="section-shell">
          <p className="eyebrow">Practice Areas</p>
          <div className="mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            {practiceAreas.map((area) => (
              <article key={area} className="rounded border border-line bg-white p-5 shadow-panel">
                <h3 className="font-semibold text-ink">{area}</h3>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="border-b border-line bg-white">
        <div className="section-shell">
          <p className="eyebrow">Local Resources</p>
          <h2 className="mt-3 font-display text-3xl text-ink">Family law pages for San Jose and Santa Clara County</h2>
          <div className="mt-6 grid gap-4 md:grid-cols-2">
            <Link href="/san-jose-divorce-attorney" className="rounded border border-line bg-cream p-6 shadow-panel transition hover:border-mutedBlue">
              <h3 className="font-display text-2xl text-ink">San Jose Divorce Attorney</h3>
              <p className="mt-2 text-charcoal/85">
                Guidance on divorce strategy, filings, support, and property division for San Jose clients.
              </p>
            </Link>
            <Link href="/santa-clara-county-child-custody-attorney" className="rounded border border-line bg-cream p-6 shadow-panel transition hover:border-mutedBlue">
              <h3 className="font-display text-2xl text-ink">Santa Clara County Child Custody Attorney</h3>
              <p className="mt-2 text-charcoal/85">
                Support for custody, visitation, move-away requests, and modification matters.
              </p>
            </Link>
          </div>
        </div>
      </section>

      <section className="border-b border-line bg-white">
        <div className="section-shell grid gap-6 md:grid-cols-2">
          <div>
            <p className="eyebrow">Is This The Right Fit?</p>
            <h2 className="mt-3 font-display text-3xl text-ink">Thoughtful counsel for clients who value quality</h2>
          </div>
          <p className="text-lg leading-relaxed text-charcoal/90">
            This firm is best suited for clients who value preparation, responsiveness, and strategic legal guidance.
          </p>
        </div>
      </section>

      <section className="bg-ink text-white">
        <div className="section-shell">
          <p className="eyebrow !text-white/75">Next Step</p>
          <h2 className="mt-3 font-display text-4xl">Ready to discuss your situation?</h2>
          <p className="mt-4 max-w-3xl text-white/90">
            Consultations are by appointment only. Contact {site.attorney} to discuss timing, scope, and how to move forward with confidence.
          </p>
          <div className="mt-6 flex flex-wrap gap-4">
            <Link href="/contact" className="rounded bg-white px-5 py-3 text-sm font-semibold text-ink transition hover:bg-cream">
              Schedule a Consultation
            </Link>
            <a href={site.phoneLink} className="rounded border border-white px-5 py-3 text-sm font-semibold text-white transition hover:bg-white/10">
              Call {site.phoneDisplay}
            </a>
          </div>
        </div>
      </section>
    </>
  );
}
