import Link from "next/link";
import { site } from "@/data/site";

const links = [
  ["Home", "/"],
  ["Practice Areas", "/practice-areas"],
  ["San Jose Divorce", "/san-jose-divorce-attorney"],
  ["Custody - Santa Clara County", "/santa-clara-county-child-custody-attorney"],
  ["Attorney Profile", "/attorney-profile"],
  ["Approach", "/approach"],
  ["Fees / Consultation", "/fees-consultation"],
  ["FAQ", "/faq"],
  ["Contact", "/contact"],
] as const;

export default function Header() {
  return (
    <header className="border-b border-line bg-cream/95 backdrop-blur">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-4 px-6 py-5 md:flex-row md:items-center md:justify-between md:px-8">
        <div>
          <Link href="/" className="font-display text-2xl text-ink">
            {site.name}
          </Link>
          <p className="mt-1 text-sm text-charcoal/80">Boutique California Family Law Counsel</p>
        </div>
        <nav aria-label="Primary">
          <ul className="flex flex-wrap gap-3 text-sm text-charcoal md:justify-end md:gap-5">
            {links.map(([label, href]) => (
              <li key={href}>
                <Link href={href} className="transition hover:text-mutedBlue">
                  {label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </header>
  );
}
