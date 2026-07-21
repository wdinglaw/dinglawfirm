import Link from "next/link";
import { site } from "@/data/site";

const links = [
  ["Home", "/"],
  ["About", "/about.html"],
  ["Divorce", "/san-jose-divorce-lawyer/"],
  ["Child Custody", "/san-jose-child-custody-lawyer/"],
  ["Support", "/spousal-support-attorney-santa-clara-county/"],
  ["Prenuptial Agreements", "/san-jose-prenup-postnup-lawyer/"],
  ["Insights", "/insights.html"],
  ["Contact", "/contact.html"],
] as const;

export default function Header() {
  return (
    <header className="border-b border-line bg-cream/95 backdrop-blur">
      <div className="mx-auto flex w-full max-w-7xl flex-col gap-4 px-6 py-5 md:flex-row md:items-center md:justify-between md:px-8">
        <div>
          <Link href="/" className="font-display text-2xl text-ink">
            {site.name}
          </Link>
          <p className="mt-1 text-sm text-charcoal/80">California Family Law</p>
        </div>
        <nav aria-label="Primary">
          <ul className="flex flex-wrap items-center gap-3 text-sm text-charcoal md:justify-end lg:gap-4 xl:gap-5">
            {links.map(([label, href]) => (
              <li key={href}>
                <Link href={href} className="transition hover:text-mutedBlue">
                  {label}
                </Link>
              </li>
            ))}
            <li>
              <a
                href="https://calendly.com/wdinglaw/consultation"
                className="rounded bg-ink px-4 py-2 font-semibold text-white transition hover:bg-mutedBlue"
                target="_blank"
                rel="noopener"
              >
                Schedule a Consultation
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
}
