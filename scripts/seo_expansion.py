from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://dinglawgroup.com"
CALENDLY = "https://calendly.com/wdinglaw/consultation"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def legal_schema(extra: list[str] | None = None) -> str:
    knows = [
        "California family law",
        "divorce",
        "child custody",
        "child support",
        "spousal support",
        "property division",
        "domestic violence restraining orders",
        "high-asset divorce",
        "equity compensation in divorce",
    ]
    if extra:
        knows.extend(extra)
    data = {
        "@context": "https://schema.org",
        "@type": ["LegalService", "LocalBusiness"],
        "@id": f"{BASE}/#legalservice",
        "name": "Law Offices of Wenyu Ding",
        "url": BASE,
        "telephone": "+1-408-320-8182",
        "email": "wding@dinglawgroup.com",
        "image": f"{BASE}/assets/wenyu-ding-logo-small.jpg",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "1525 McCarthy Blvd, Ste 1077",
            "addressLocality": "Milpitas",
            "addressRegion": "CA",
            "postalCode": "95035-7451",
            "addressCountry": "US",
        },
        "areaServed": ["Milpitas", "San Jose", "Santa Clara County", "Bay Area", "Northern California"],
        "priceRange": "$$",
        "legalName": "Law Offices of Wenyu Ding",
        "knowsAbout": sorted(set(knows)),
    }
    return json.dumps(data, separators=(",", ":"))


def faq_schema(faqs: list[tuple[str, str]]) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    return json.dumps(data, separators=(",", ":"))


def breadcrumb_schema(items: list[tuple[str, str]]) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)
        ],
    }
    return json.dumps(data, separators=(",", ":"))


NAV = """<header class="site-header" aria-label="Main header">
    <div class="container nav-row">
      <a class="brand" href="/" aria-label="Law Offices of Wenyu Ding home"><span class="brand-mark"><img src="/assets/wenyu-ding-logo-small.jpg" alt="" width="44" height="44" /></span><span class="brand-copy"><span class="brand-name">Law Offices of Wenyu Ding</span><span class="brand-sub">California Family Law</span></span></a>
      <button class="mobile-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav id="site-nav" class="site-nav" data-menu aria-label="Primary">
        <a href="/">Home</a>
        <a href="/about.html">About</a>
        <a href="/practice-areas.html">Practice Areas</a>
        <a href="/san-jose-divorce-lawyer/">Divorce</a>
        <a href="/san-jose-child-custody-lawyer/">Custody</a>
        <a href="/spousal-support-attorney-santa-clara-county/">Support</a>
        <a href="/high-asset-divorce.html">High-Asset Divorce</a>
        <a href="/insights.html">Insights</a>
        <a href="/reviews-recognition.html">Reviews &amp; Recognition</a>
        <a class="btn" href="/consultation.html">Contact / Schedule</a>
      </nav>
    </div>
  </header>"""


FOOTER = """<footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand-block"><h3>Law Offices of Wenyu Ding</h3><p class="footer-descriptor">Bay Area family law counsel</p><p>1525 McCarthy Blvd, Ste 1077, Milpitas, CA 95035-7451</p><p><a href="tel:4083208182">408-320-8182</a> | <a href="mailto:wding@dinglawgroup.com">wding@dinglawgroup.com</a></p></div>
      <div><h3>Main Practice Pages</h3><p><a href="/san-jose-divorce-lawyer/">Divorce</a></p><p><a href="/san-jose-child-custody-lawyer/">Child Custody</a></p><p><a href="/spousal-support-attorney-santa-clara-county/">Support</a></p><p><a href="/property-division-lawyer-california/">Property Division</a></p><p><a href="/high-asset-divorce.html">High-Asset Divorce</a></p></div>
      <div><h3>Local Pages</h3><p><a href="/milpitas-family-law-attorney/">Milpitas Family Law</a></p><p><a href="/san-jose-family-law-attorney/">San Jose Family Law</a></p><p><a href="/santa-clara-county-divorce-lawyer/">Santa Clara County Divorce</a></p><p><a href="/sunnyvale-divorce-attorney.html">Sunnyvale Divorce</a></p><p><a href="/palo-alto-divorce-attorney.html">Palo Alto Divorce</a></p></div>
      <div><h3>Resources</h3><p><a href="/insights.html">Insights</a></p><p><a href="/reviews-recognition.html">Reviews &amp; Recognition</a></p><p><a href="/consultation.html">Consultation</a></p><p><a href="/contact.html">Contact</a></p><p><a href="/privacy.html">Privacy Policy</a></p><p><a href="/disclaimer.html">Disclaimer</a></p></div>
    </div>
    <div class="container footer-bottom">Attorney advertising. Prior outcomes, reviews, or recognition do not guarantee similar results. Information on this site is not legal advice and does not create an attorney-client relationship. A consultation and signed engagement agreement are required before legal advice or representation begins. See <a href="/disclaimer.html">Disclaimer</a> and <a href="/privacy.html">Privacy Policy</a>.</div>
  </footer>
  <div class="sticky-cta" aria-label="Quick contact options"><a href="tel:4083208182">Call</a><a href="/consultation.html">Schedule</a><a href="/contact.html">Contact</a></div>"""


def page(path: str, title: str, description: str, h1: str, kicker: str, body: str, faqs: list[tuple[str, str]] | None = None, extra_knows: list[str] | None = None) -> None:
    canonical = f"{BASE}/{path}".replace(".html/", ".html")
    if not path.endswith(".html") and not path.endswith("/"):
        canonical += "/"
    schema_parts = [legal_schema(extra_knows)]
    if faqs:
        schema_parts.append(faq_schema(faqs))
    schema_parts.append(breadcrumb_schema([("Home", BASE), ("Practice Areas", f"{BASE}/practice-areas.html"), (h1, canonical)]))
    scripts = "\n  ".join(f'<script type="application/ld+json">{s}</script>' for s in schema_parts)
    html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />
  <link rel="canonical" href="{esc(canonical)}" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{esc(canonical)}" />
  <meta property="og:site_name" content="Law Offices of Wenyu Ding" />
  <meta property="og:image" content="{BASE}/assets/wenyu-ding-logo-small.jpg" />
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inclusive+Sans:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/assets/styles.css?v=20260708-seo-expansion" />
  {scripts}
</head>
<body>
  <a class="skip-link" href="#main-content">Skip to content</a>
  {NAV}
  <main id="main-content">
    <section class="subpage-hero"><div class="container"><p class="kicker">{esc(kicker)}</p><h1>{esc(h1)}</h1><p class="muted intro-copy">{esc(description)}</p><p class="hero-actions"><a class="btn" href="{CALENDLY}" target="_blank" rel="noopener">Schedule a Consultation</a><a class="btn-outline" href="/contact.html">Contact the Firm</a></p><p class="microcopy">Contacting the firm or scheduling a consultation does not create an attorney-client relationship.</p></div></section>
    {body}
    {faq_html(faqs or [])}
    {cta_html()}
  </main>
  {FOOTER}
  <script src="/assets/main.js"></script>
</body>
</html>"""
    out = ROOT / path
    if path.endswith("/"):
        out = out / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_doc, encoding="utf-8")


def section(title: str, paragraphs: list[str]) -> str:
    content = "\n".join(f"          <p>{esc(p)}</p>" for p in paragraphs)
    return f"""<section class="card section">
        <h2>{esc(title)}</h2>
{content}
      </section>"""


def faq_html(faqs: list[tuple[str, str]]) -> str:
    if not faqs:
        return ""
    items = "\n".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faqs)
    return f"""<section class="section section-quiet"><div class="container faq-wrap"><div class="section-heading compact"><p class="kicker">FAQ</p><h2>Common questions.</h2></div><div class="faq-list">{items}</div></div></section>"""


def cta_html() -> str:
    return f"""<section class="section"><div class="container"><div class="cta-band final-cta"><div><p class="kicker">Schedule a Paid Consultation</p><h2>Discuss your family law matter with an attorney.</h2><p class="muted">Discuss your family law matter with an attorney and receive practical next steps based on your situation. Representation begins only after conflict clearance and a signed agreement.</p></div><p class="hero-actions"><a class="btn" href="{CALENDLY}" target="_blank" rel="noopener">Schedule Consultation</a><a class="btn-outline" href="/contact.html">Contact the Firm</a></p></div></div></section>"""


COMMON_FAQS = [
    ("Is this page legal advice?", "No. It is general information about California family law. A consultation is needed to evaluate your facts."),
    ("Does contacting the firm create an attorney-client relationship?", "No. Representation begins only after conflict clearance, a signed engagement agreement, and any required retainer."),
    ("Do you serve Santa Clara County?", "Yes. The firm is based in Milpitas and serves clients in San Jose, Santa Clara County, and the Bay Area."),
    ("Can these issues be resolved without trial?", "Often, yes. Settlement, mediation, and negotiated orders may be possible depending on the facts, disclosure, and the other party's position."),
    ("What should I prepare for a consultation?", "Bring or summarize court papers, deadlines, current orders, financial records, custody schedules, and the questions you need answered first."),
]


PRACTICE_PAGES = [
    ("divorce-attorney-san-jose.html", "San Jose Divorce Attorney | Law Offices of Wenyu Ding", "San Jose divorce attorney for custody, support, property division, disclosures, temporary orders, and Silicon Valley compensation issues.", "San Jose Divorce Attorney", "Divorce Attorney San Jose", ["filing for divorce", "temporary orders", "financial disclosures", "settlement strategy"]),
    ("child-custody-attorney-san-jose.html", "San Jose Child Custody Attorney | Parenting Plans", "San Jose child custody attorney for parenting schedules, legal custody, physical custody, move-away concerns, and Santa Clara County hearing preparation.", "San Jose Child Custody Attorney", "Child Custody Attorney San Jose", ["parenting plans", "custody mediation", "move-away requests", "child safety concerns"]),
    ("child-support-attorney-santa-clara-county.html", "Child Support Attorney Santa Clara County | Guideline Support", "Santa Clara County child support attorney for guideline support, variable income, bonuses, RSUs, add-on expenses, and modification issues.", "Child Support Attorney in Santa Clara County", "Child Support", ["guideline child support", "variable income", "bonus income", "childcare expenses"]),
    ("spousal-support-attorney-san-jose.html", "San Jose Spousal Support Attorney | Alimony Strategy", "San Jose spousal support attorney for temporary support, long-term support, income analysis, bonuses, and support modification issues.", "San Jose Spousal Support Attorney", "Spousal Support", ["temporary spousal support", "long-term support", "earning capacity", "support modification"]),
    ("property-division-attorney-san-jose.html", "San Jose Property Division Attorney | California Community Property", "San Jose property division attorney for California community property, separate property, tracing, reimbursements, real estate, and retirement division.", "San Jose Property Division Attorney", "Property Division", ["community property", "separate property", "tracing", "reimbursement claims"]),
    ("high-asset-divorce-silicon-valley.html", "High-Asset Divorce Attorney Silicon Valley | Complex Property", "Silicon Valley high-asset divorce attorney for RSUs, options, bonuses, startup equity, business interests, real estate, support, and disclosure strategy.", "High-Asset Divorce Attorney in Silicon Valley", "High-Asset Divorce", ["high-asset divorce", "startup equity", "business interests", "Bay Area real estate"]),
    ("rsu-stock-option-divorce-lawyer.html", "RSU and Stock Option Divorce Lawyer | Bay Area Equity Compensation", "Bay Area divorce lawyer for RSUs, stock options, vesting schedules, startup equity, support, and California property characterization issues.", "RSU and Stock Option Divorce Lawyer", "Equity Compensation Divorce", ["RSUs", "stock options", "vesting schedules", "startup equity"]),
    ("business-owner-divorce-attorney.html", "Business Owner Divorce Attorney | California Family Law", "California business owner divorce attorney for closely held companies, valuation issues, income analysis, goodwill, and settlement structure.", "Business Owner Divorce Attorney", "Business Owner Divorce", ["business valuation", "closely held companies", "goodwill", "owner income"]),
    ("domestic-violence-restraining-order-attorney.html", "Domestic Violence Restraining Order Attorney | San Jose DVRO", "San Jose domestic violence restraining order attorney for DVRO requests, responses, evidence organization, custody issues, and hearing preparation.", "Domestic Violence Restraining Order Attorney", "DVRO Attorney", ["DVRO", "restraining orders", "hearing preparation", "custody safety issues"]),
    ("move-away-custody-attorney.html", "Move-Away Custody Attorney | California Relocation Cases", "California move-away custody attorney for relocation disputes, parenting plans, school logistics, travel schedules, and Santa Clara County custody strategy.", "Move-Away Custody Attorney", "Move-Away Custody", ["relocation custody", "parenting schedules", "school logistics", "travel plans"]),
    ("prenuptial-agreement-attorney.html", "Prenuptial Agreement Attorney | San Jose and Silicon Valley", "Prenuptial agreement attorney for Silicon Valley professionals addressing financial disclosures, separate property, equity compensation, real estate, and business interests.", "Prenuptial Agreement Attorney", "Prenuptial Agreements", ["prenuptial agreements", "financial disclosures", "separate property", "equity compensation"]),
    ("postnuptial-transmutation-agreement-attorney.html", "Postnuptial and Transmutation Agreement Attorney | San Jose", "San Jose postnuptial and transmutation agreement attorney for title changes, separate property, community property, real estate, and marital agreement review.", "Postnuptial and Transmutation Agreement Attorney", "Postnuptial Agreements", ["postnuptial agreements", "transmutation agreements", "title changes", "marital property"]),
    ("post-judgment-modification-attorney.html", "Post-Judgment Modification Attorney | Santa Clara County", "Santa Clara County post-judgment modification attorney for support changes, parenting schedule updates, move-away issues, and changed circumstances.", "Post-Judgment Modification Attorney", "Post-Judgment Modifications", ["post-judgment modification", "changed circumstances", "support changes", "custody modification"]),
    ("enforcement-family-court-orders-attorney.html", "Family Court Order Enforcement Attorney | Santa Clara County", "Santa Clara County family court order enforcement attorney for custody, support, property, reimbursement, and compliance disputes after orders are entered.", "Family Court Order Enforcement Attorney", "Order Enforcement", ["enforcement", "contempt considerations", "support arrears", "custody compliance"]),
]


def practice_body(h1: str, focus: list[str]) -> str:
    focus_text = ", ".join(focus)
    return f"""<section class="section"><div class="container content-layout"><article class="article-body">
      <p>{esc(h1)} matters often require early organization, careful documentation, and a practical understanding of how California family law principles apply to the specific facts. The Law Offices of Wenyu Ding provides attorney-led representation for clients in San Jose, Milpitas, Santa Clara County, and the Bay Area.</p>
      <p>Many local matters involve demanding work schedules, dual-income households, Bay Area housing costs, equity compensation, and parenting logistics. Strategy should account for those realities without turning every disagreement into unnecessary litigation.</p>
      {section("How We Help", [
          "The firm helps clients identify urgent issues, gather relevant records, understand procedural deadlines, prepare negotiation positions, and decide when court intervention may be necessary.",
          f"Typical work may involve {focus_text}, financial disclosures, settlement planning, hearing preparation, and drafting orders or agreements that are clear enough to implement.",
          "The approach is calm, practical, and litigation-aware. Even when settlement is the goal, the factual record should be organized so the client's position can be explained clearly if the case reaches court.",
      ])}
      {section("Common Issues", [
          "Common issues include incomplete documents, unclear communication, disputed timelines, income volatility, parenting-schedule conflicts, expense allocation, and uncertainty about what a proposed agreement actually requires.",
          "California law generally requires full and accurate disclosure in divorce-related financial matters. Depending on the facts, discovery, subpoenas, valuation work, or targeted document requests may be needed.",
          "No single checklist can resolve every family law problem. The useful strategy depends on the court posture, available documents, financial realities, and the client's goals.",
      ])}
      {section("Santa Clara County and Bay Area Relevance", [
          "Santa Clara County family law matters are shaped by local court procedures, hearing calendars, mediation expectations, and the practical realities of Silicon Valley households.",
          "For many clients, compensation may include salary, bonuses, RSUs, options, deferred compensation, or startup equity. Housing, school schedules, and commute patterns can also influence realistic custody and settlement options.",
      ])}
      {section("Related Services", [
          "Related pages include San Jose divorce, child custody, support, property division, high-asset divorce, RSU and stock option divorce, domestic violence restraining orders, and prenuptial or postnuptial agreements.",
          "This page is informational only. A consultation is needed to evaluate the specific facts, documents, deadlines, and possible next steps in your matter.",
      ])}
      <p><a class="text-link" href="/san-jose-divorce-lawyer/">Divorce</a> | <a class="text-link" href="/san-jose-child-custody-lawyer/">Custody</a> | <a class="text-link" href="/property-division-lawyer-california/">Property Division</a> | <a class="text-link" href="/high-asset-divorce.html">High-Asset Divorce</a></p>
    </article><aside class="card"><h2>Consultation Focus</h2><p>Bring current orders, pleadings, income records, asset documents, messages, deadlines, and a short list of decisions that need attention first.</p><p><a class="btn" href="{CALENDLY}" target="_blank" rel="noopener">Schedule Consultation</a></p></aside></div></section>"""


LOCAL_PAGES = [
    ("milpitas-family-law-attorney.html", "Milpitas Family Law Attorney | Law Offices of Wenyu Ding", "Milpitas family law attorney for divorce, custody, support, property division, DVROs, and marital agreements near the firm's South Bay office.", "Milpitas Family Law Attorney", "Milpitas Family Law", "Milpitas clients often need practical local counsel close to work, home, and Santa Clara County court processes."),
    ("san-jose-family-law-attorney.html", "San Jose Family Law Attorney | Divorce, Custody, Support", "San Jose family law attorney for divorce, child custody, support, property division, high-asset divorce, and temporary orders in Santa Clara County.", "San Jose Family Law Attorney", "San Jose Family Law", "San Jose families may face complex housing, school, commute, and compensation issues that should be reflected in family law strategy."),
    ("santa-clara-county-divorce-attorney.html", "Santa Clara County Divorce Attorney | Law Offices of Wenyu Ding", "Santa Clara County divorce attorney for filings, disclosures, temporary orders, settlement planning, custody, support, and property division.", "Santa Clara County Divorce Attorney", "Santa Clara County Divorce", "Santa Clara County cases require attention to local filing practice, court calendars, mediation expectations, and practical settlement sequencing."),
    ("sunnyvale-divorce-attorney.html", "Sunnyvale Divorce Attorney | Silicon Valley Family Law", "Sunnyvale divorce attorney for professionals handling custody, support, property division, RSUs, options, real estate, and Santa Clara County court issues.", "Sunnyvale Divorce Attorney", "Sunnyvale Divorce", "Sunnyvale divorce matters often involve technology-sector schedules, equity compensation, school logistics, and expensive housing decisions."),
    ("cupertino-family-law-attorney.html", "Cupertino Family Law Attorney | Divorce and Custody", "Cupertino family law attorney for divorce, custody, support, property division, college-bound family planning, and Silicon Valley compensation issues.", "Cupertino Family Law Attorney", "Cupertino Family Law", "Cupertino families may need careful custody and financial planning around schools, professional schedules, property values, and long-term support concerns."),
    ("santa-clara-divorce-attorney.html", "Santa Clara Divorce Attorney | Family Law Representation", "Santa Clara divorce attorney for custody, support, property division, domestic violence restraining orders, and high-asset family law issues.", "Santa Clara Divorce Attorney", "Santa Clara Divorce", "Santa Clara clients often balance family court issues with demanding professional schedules, local schools, real estate, and complex compensation."),
    ("los-gatos-high-asset-divorce-attorney.html", "Los Gatos High-Asset Divorce Attorney | Complex Property", "Los Gatos high-asset divorce attorney for real estate, business interests, RSUs, options, support, and California property division strategy.", "Los Gatos High-Asset Divorce Attorney", "Los Gatos High-Asset Divorce", "Los Gatos high-asset divorce matters may involve valuable real estate, business interests, investment accounts, and support issues requiring careful documentation."),
    ("palo-alto-divorce-attorney.html", "Palo Alto Divorce Attorney | Equity Compensation and Property", "Palo Alto divorce attorney for professionals and founders addressing custody, support, RSUs, options, startup equity, real estate, and property division.", "Palo Alto Divorce Attorney", "Palo Alto Divorce", "Palo Alto divorce matters may involve startup equity, venture-backed compensation, high housing costs, and cross-county practical considerations."),
]


def local_body(city_context: str) -> str:
    return f"""<section class="section"><div class="container content-layout"><article class="article-body">
      <p>{esc(city_context)} The firm provides calm, attorney-led representation for divorce, custody, support, property division, domestic violence restraining order matters, and marital agreement issues.</p>
      {section("Relevant Practice Areas", [
          "Services include divorce planning, child custody and parenting schedules, child support, spousal support, property division, high-asset divorce, RSUs and stock options, business owner divorce, DVRO matters, and prenuptial or postnuptial agreements.",
          "The right path may involve negotiation, mediation, targeted court filings, or litigation readiness depending on the facts and deadlines.",
      ])}
      {section("Local Process Considerations", [
          "California law governs the family law issues, but local court procedures, filing requirements, hearing calendars, and settlement practices can affect timing and preparation.",
          "Clients should gather court papers, current orders, financial records, compensation documents, custody calendars, and written communications before the consultation when possible.",
      ])}
      {section("Internal Links", [
          "Review related pages on San Jose divorce, child custody, support, property division, high-asset divorce, RSUs and stock options, prenuptial agreements, and post-judgment modifications.",
          "This local page is not legal advice and should not be treated as a prediction of outcome in any case.",
      ])}
      <p><a class="text-link" href="/divorce-attorney-san-jose.html">Divorce Attorney</a> | <a class="text-link" href="/child-custody-attorney-san-jose.html">Child Custody</a> | <a class="text-link" href="/rsu-stock-option-divorce-lawyer.html">RSU Divorce</a> | <a class="text-link" href="/prenuptial-agreement-attorney.html">Prenuptial Agreements</a></p>
    </article><aside class="card"><h2>Local Consultation</h2><p>Consultations are paid and by appointment. Conflict clearance is required before representation can begin.</p><p><a class="btn" href="{CALENDLY}" target="_blank" rel="noopener">Schedule Consultation</a></p></aside></div></section>"""


ARTICLE_TOPICS = [
    ("what-happens-to-rsus-santa-clara-county-divorce", "What Happens to RSUs in a Santa Clara County Divorce?", "How restricted stock units may be addressed in Santa Clara County divorce, including characterization, vesting, support, and disclosure issues."),
    ("are-unvested-rsus-community-property-california", "Are Unvested RSUs Community Property in California?", "A general overview of how unvested RSUs may be analyzed in California divorce depending on grant purpose, timing, and facts."),
    ("how-bonuses-affect-support-california", "How Bonuses Affect Child and Spousal Support in California", "How bonus income may affect child support, spousal support, cash flow, and settlement planning in California family law matters."),
    ("divorce-startup-employees-stock-options", "Divorce for Startup Employees With Stock Options", "A Silicon Valley divorce overview for startup employees with stock options, liquidity uncertainty, valuation issues, and support concerns."),
    ("dividing-bay-area-real-estate-california-divorce", "Dividing Bay Area Real Estate in a California Divorce", "How Bay Area real estate can shape divorce strategy, including equity, refinance, buyout, sale, reimbursement, and support issues."),
    ("how-santa-clara-county-judges-evaluate-parenting-schedules", "How Santa Clara County Judges Evaluate Parenting Schedules", "Draft guidance on parenting schedules, stability, school logistics, communication, and child-focused custody preparation."),
    ("move-away-custody-cases-california", "Move-Away Custody Cases in California", "Draft guidance on California relocation custody disputes and the practical records parents should organize."),
    ("document-custody-issues-without-looking-unreasonable", "How to Document Custody Issues Without Looking Unreasonable", "Draft guidance on calm, useful custody documentation in California family law matters."),
    ("what-not-to-write-custody-text-messages", "What Not to Write in Custody Text Messages", "Draft guidance on communication discipline for parents involved in custody disputes."),
    ("preparing-child-custody-hearing-santa-clara-county", "Preparing for a Child Custody Hearing in Santa Clara County", "Draft guidance on custody hearing preparation, documents, declarations, and realistic requests."),
    ("what-happens-after-filing-divorce-santa-clara-county", "What Happens After Filing for Divorce in Santa Clara County?", "Draft guidance on response deadlines, disclosures, temporary orders, and settlement planning."),
    ("preliminary-declarations-disclosure-explained", "Preliminary Declarations of Disclosure Explained", "Draft guidance on California preliminary declarations of disclosure and why complete financial information matters."),
    ("what-to-bring-family-law-consultation", "What to Bring to a Family Law Consultation", "Draft checklist for documents, deadlines, and questions to prepare before a family law consultation."),
    ("temporary-orders-california-family-court", "Temporary Orders in California Family Court", "Draft guidance on requests for temporary custody, support, property control, and conduct orders."),
    ("prenuptial-agreements-silicon-valley-professionals", "Prenuptial Agreements for Silicon Valley Professionals", "Draft guidance on prenups involving RSUs, options, real estate, business interests, and financial disclosures."),
    ("rsus-stock-options-prenuptial-agreements", "RSUs and Stock Options in Prenuptial Agreements", "Draft guidance on equity compensation provisions in California prenuptial agreements."),
    ("postnuptial-vs-transmutation-agreements", "Postnuptial Agreements vs. Transmutation Agreements", "Draft guidance on different marital agreements and why title changes should be reviewed carefully."),
    ("why-financial-disclosures-matter-california-prenups", "Why Financial Disclosures Matter in California Prenups", "Draft guidance on disclosure practices and enforceability concerns in California prenuptial agreements."),
]


def article_body(title: str, full: bool) -> str:
    if full:
        paragraphs = [
            f"{title} is a common question for Bay Area families because divorce often touches compensation, parenting, housing, tax, and court timing at the same time. California family law is fact-specific, so the best starting point is usually a careful inventory rather than an immediate conclusion.",
            "The first step is to identify what records exist and what still needs to be requested. In financial matters, that may include paystubs, tax returns, W-2s, equity award agreements, vesting schedules, brokerage records, mortgage statements, retirement statements, and loan documents. In custody matters, that may include parenting calendars, school communications, medical records, travel records, and written communications between the parents.",
            "Santa Clara County and Silicon Valley cases often include practical issues that do not fit neatly into a generic checklist. Compensation may be variable. Housing may be expensive. Work schedules may involve travel, remote work, or intense product cycles. Parenting plans may need to account for school location, commute patterns, extracurricular activities, and communication boundaries.",
            "A useful legal strategy usually separates urgent issues from long-term issues. Temporary orders may be needed for custody, support, possession of property, or safety. At the same time, final settlement should be considered early so short-term positions do not create avoidable problems later.",
            "Disclosure matters. California law generally requires complete and accurate financial disclosure in divorce. Depending on the facts, incomplete disclosure can slow settlement, increase distrust, and create enforcement or set-aside issues later. Clients should avoid guessing about assets or income when documents can be gathered.",
            "Communication also matters. Written messages may become evidence. Parents and spouses should assume that texts, emails, and app messages could be reviewed out of context. Clear, brief, child-focused, and fact-based communication is often safer than reactive commentary.",
            "Settlement is often possible, but settlement works best when the record is organized. A proposal should address implementation details: dates, payment mechanics, tax forms, title transfers, refinancing deadlines, custody exchanges, holiday schedules, and what happens if a required step is delayed.",
            "Court may be necessary when the other side will not provide information, follow orders, or engage reasonably. Litigation should still be focused. The strongest filings usually identify the requested order, explain why it is needed, and attach documents that support the request without burying the court in irrelevant material.",
            "Clients should also think about timing. Some issues can be addressed immediately through temporary orders. Other issues may need discovery, expert input, property records, or compensation documents before a reliable position can be formed. Rushing a final agreement before the information is complete can create avoidable enforcement problems or leave important terms ambiguous.",
            "For financial topics, tax and liquidity should be considered with appropriate professional advice. A property division term that looks balanced on paper may function differently if one spouse receives illiquid assets, deferred compensation, or property that cannot be sold or refinanced on the expected timeline. The legal strategy should account for implementation, not just headline numbers.",
            "For custody topics, the most useful preparation is usually child-focused and specific. Courts generally need practical information about school routines, exchanges, communication, health needs, safety concerns, and each parent's ability to support a workable schedule. Broad criticism without documents or concrete examples is usually less helpful than a concise record tied to the requested order.",
            "For agreement topics, clear drafting matters. A durable order or settlement should explain who must do what, by when, how payment or transfer will occur, what documents must be signed, and how future disagreements will be handled. Ambiguous terms can create fresh conflict after the case was supposed to be resolved.",
            "This article is general information, not legal advice. A consultation is needed to evaluate the facts, documents, deadlines, and options in a specific Santa Clara County or California family law matter.",
        ]
    else:
        paragraphs = [
            "This draft article is a planned informational resource for California family law clients. It should be expanded with additional examples, internal links, and any jurisdiction-specific updates before publication as a full article.",
            "The final article should explain the legal issue in plain English, identify documents clients may need to gather, describe common mistakes, and connect the topic to related practice pages without promising an outcome.",
            "This page is a placeholder only and does not provide legal advice. A consultation is needed to evaluate any specific matter.",
        ]
    ps = "\n".join(f"<p>{esc(p)}</p>" for p in paragraphs)
    return f"""<section class="section"><div class="container content-layout"><article class="article-body"><p class="note">Updated July 8, 2026</p>{ps}<h2>Related resources</h2><p><a class="text-link" href="/rsu-stock-option-divorce-lawyer.html">RSU and Stock Option Divorce</a> | <a class="text-link" href="/high-asset-divorce-silicon-valley.html">High-Asset Divorce</a> | <a class="text-link" href="/child-custody-attorney-san-jose.html">Child Custody</a> | <a class="text-link" href="/consultation.html">Consultation</a></p></article><aside class="card"><h2>Informational only</h2><p>This article is not legal advice and does not create an attorney-client relationship.</p></aside></div></section>"""


def generate_reviews() -> None:
    body = f"""<section class="section"><div class="container content-layout"><article class="article-body">
      <p>The Law Offices of Wenyu Ding does not publish fabricated testimonials or invented review excerpts. Prospective clients may review public profile pages once approved URLs are added by the firm.</p>
      <section class="recognition-panel section"><div class="recognition-badge"><img src="/assets/client-champion-gold.webp" alt="Martindale-Hubbell Client Champion Gold Award badge" width="877" height="400" loading="lazy" /></div><div class="recognition-copy"><p class="kicker">Recognition</p><h2>Martindale-Hubbell Client Champion Award - Gold</h2><p>The Client Champion Gold recognition is referenced in the existing site content and badge asset. Reviews and recognition are provided for informational purposes only. Prior results, reviews, or recognition do not guarantee a similar outcome in any future matter.</p></div></section>
      <section class="card section"><h2>Client Review Links</h2><p>Approved public review/profile URLs should be added here when available.</p><ul class="list-tight"><li><!-- TODO: Add approved Martindale-Hubbell / Lawyers.com URL. -->Martindale-Hubbell / Lawyers.com profile</li><li><!-- TODO: Add approved Avvo URL. -->Avvo profile</li><li><!-- TODO: Add approved Google Business Profile URL. -->Google Business Profile</li></ul></section>
    </article><aside class="card"><h2>Ethics Note</h2><p>Reviews and recognition are informational only. No result can be guaranteed, and each matter depends on its own facts, law, documents, court posture, and available evidence.</p></aside></div></section>"""
    page("reviews-recognition.html", "Reviews & Recognition | Law Offices of Wenyu Ding", "Reviews and recognition information for the Law Offices of Wenyu Ding, including verified recognition and placeholders for approved profile links.", "Reviews and Recognition", "Client Review Links", body, COMMON_FAQS[:3], ["reviews", "recognition"])


def generate_articles() -> None:
    cards = []
    for i, (slug, title, desc) in enumerate(ARTICLE_TOPICS):
        full = i < 5
        path = f"insights/{slug}/"
        page(path, f"{title} | Law Offices of Wenyu Ding", desc, title, "Family Law Insights", article_body(title, full), COMMON_FAQS[:3], ["family law insights"])
        cards.append(f'<article class="insight-card"><p class="kicker">{"Full Article" if full else "Draft Stub"}</p><h2><a href="/{path}">{esc(title)}</a></h2><p>{esc(desc)}</p><p><a class="text-link" href="/{path}">Read article</a></p></article>')
    body = f"""<section class="subpage-hero"><div class="container"><p class="kicker">Family Law Insights</p><h1>Family Law Insights</h1><p class="muted intro-copy">Articles and practical guides about California family law, divorce, custody, support, property division, prenuptial agreements, and complex Silicon Valley family-law issues.</p></div></section><section class="section"><div class="container insight-grid">{''.join(cards)}</div></section>"""
    html_doc = f"""<!doctype html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><title>Family Law Insights | Law Offices of Wenyu Ding</title><meta name="description" content="Family law insights for California divorce, custody, support, property division, prenups, RSUs, and Silicon Valley family-law issues." /><link rel="canonical" href="{BASE}/insights.html" /><meta property="og:title" content="Family Law Insights | Law Offices of Wenyu Ding" /><meta property="og:description" content="Family law insights for California divorce, custody, support, property division, prenups, RSUs, and Silicon Valley family-law issues." /><meta property="og:type" content="website" /><meta property="og:url" content="{BASE}/insights.html" /><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" /><link rel="stylesheet" href="/assets/styles.css?v=20260708-seo-expansion" /><script type="application/ld+json">{legal_schema()}</script></head><body><a class="skip-link" href="#main-content">Skip to content</a>{NAV}<main id="main-content">{body}</main>{FOOTER}<script src="/assets/main.js"></script></body></html>"""
    (ROOT / "insights.html").write_text(html_doc, encoding="utf-8")
    (ROOT / "insights/index.html").write_text(html_doc, encoding="utf-8")


def update_homepage() -> None:
    p = ROOT / "index.html"
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "Strategic Family Law Attorney in Santa Clara County | Law Offices of Wenyu Ding",
        "San Jose Family Law Attorney | Milpitas Divorce Lawyer | Law Offices of Wenyu Ding",
    )
    text = text.replace(
        "Strategic California family law representation for divorce, custody, support, property division, DVROs, and marital agreements in San Jose, Milpitas, and the South Bay.",
        "San Jose family law attorney and Milpitas divorce lawyer for Santa Clara County custody, property division, support, DVROs, and Silicon Valley family law issues.",
    )
    text = text.replace(
        "Strategic family law representation in Santa Clara County.",
        "San Jose &amp; Milpitas Family Law Attorney for Divorce, Custody, Support, and Property Division",
    )
    text = text.replace(
        "Guidance for divorce, custody, support, property division, domestic violence restraining orders, and marital agreements in San Jose, Milpitas, and the South Bay.",
        "Boutique California family law representation for professionals, parents, and families navigating complex transitions throughout Santa Clara County and the Bay Area.",
    )
    if "sticky-cta" not in text:
        text = text.replace("  <script src=\"assets/main.js\"></script>\n</body>", f"  <div class=\"sticky-cta\" aria-label=\"Quick contact options\"><a href=\"tel:4083208182\">Call</a><a href=\"consultation.html\">Schedule</a><a href=\"contact.html\">Contact</a></div>\n  <script src=\"assets/main.js\"></script>\n</body>")
    p.write_text(text, encoding="utf-8")


def update_sitemap() -> None:
    urls = [
        "",
        "about.html",
        "practice-areas.html",
        "consultation.html",
        "contact.html",
        "reviews-recognition.html",
        "high-asset-divorce.html",
        "disclaimer.html",
        "privacy.html",
        "san-jose-divorce-lawyer/",
        "milpitas-family-law-attorney/",
        "san-jose-family-law-attorney/",
        "santa-clara-county-divorce-lawyer/",
        "san-jose-child-custody-lawyer/",
        "high-conflict-custody-lawyer-san-jose/",
        "high-asset-divorce-lawyer-san-jose/",
        "san-jose-prenup-postnup-lawyer/",
        "san-jose-transmutation-agreement-attorney/",
        "bay-area-divorce-rsus/",
        "santa-clara-county-family-law-attorney/",
        "child-custody-lawyer-san-jose/",
        "spousal-support-attorney-santa-clara-county/",
        "high-asset-divorce-lawyer-bay-area/",
        "domestic-violence-restraining-order-attorney-san-jose/",
        "property-division-lawyer-california/",
        "prenuptial-agreement-attorney-bay-area/",
        "insights.html",
    ]
    urls.extend(path for path, *_ in PRACTICE_PAGES)
    urls.extend(path for path, *_ in LOCAL_PAGES)
    urls.extend(f"insights/{slug}/" for slug, *_ in ARTICLE_TOPICS)
    body = "\n".join(f"  <url><loc>{BASE}/{u}</loc></url>" if u else f"  <url><loc>{BASE}/</loc></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n', encoding="utf-8")


def main() -> None:
    for path, title, desc, h1, kicker, focus in PRACTICE_PAGES:
        page(path, title, desc, h1, kicker, practice_body(h1, focus), COMMON_FAQS, focus)
    for path, title, desc, h1, kicker, context in LOCAL_PAGES:
        page(path, title, desc, h1, kicker, local_body(context), COMMON_FAQS, ["local family law", h1])
    generate_reviews()
    generate_articles()
    update_homepage()
    update_sitemap()


if __name__ == "__main__":
    main()
