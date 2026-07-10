import { site } from "@/data/site";

const footerEmail = "intake@dinglawgroup.com";

export default function Footer() {
  return (
    <footer className="border-t border-line bg-white">
      <div className="section-shell py-12">
        <div className="grid gap-8 md:grid-cols-2">
          <div>
            <p className="font-display text-xl text-ink">{site.name}</p>
            <p className="mt-2 text-sm text-charcoal/80">{site.location}</p>
            <p className="mt-4 text-sm">
              Phone: <a className="text-mutedBlue" href={site.phoneLink}>{site.phoneDisplay}</a>
            </p>
            <p className="text-sm">
              Email: <a className="text-mutedBlue" href={`mailto:${footerEmail}`}>{footerEmail}</a>
            </p>
          </div>
          <div className="text-sm leading-relaxed text-charcoal/80">
            <p>
              This website is attorney advertising. The information on this website is for general informational purposes only and does not constitute legal advice. Viewing this website or contacting the firm does not create an attorney-client relationship. An attorney-client relationship is formed only after a written engagement agreement is signed.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
}
