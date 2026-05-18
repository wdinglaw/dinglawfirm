import type { Metadata } from "next";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import { site } from "@/data/site";

const legalServiceSchema = {
  "@context": "https://schema.org",
  "@type": "LegalService",
  name: site.name,
  url: site.baseUrl,
  email: site.email,
  telephone: "+1-408-320-8182",
  areaServed: site.serviceAreas,
  address: {
    "@type": "PostalAddress",
    addressLocality: site.addressLocality,
    addressRegion: site.addressRegion,
    postalCode: site.postalCode,
    addressCountry: site.addressCountry,
  },
  founder: site.attorney,
  sameAs: [],
  serviceType: [
    "Divorce representation",
    "Child custody and visitation",
    "Child and spousal support",
    "Property division",
    "Domestic violence restraining orders",
    "Move-away and relocation disputes",
  ],
};

export const metadata: Metadata = {
  title: {
    default: "Family Law Attorney in San Jose | Law Offices of Wenyu Ding",
    template: "%s | Law Offices of Wenyu Ding",
  },
  description:
    "Boutique California family law representation for divorce, custody, support, and property matters in San Jose, Santa Clara County, and the Bay Area.",
  metadataBase: new URL(site.baseUrl),
  alternates: { canonical: "/" },
  openGraph: {
    title: "Law Offices of Wenyu Ding",
    description:
      "Strategic family law representation in San Jose and Santa Clara County for divorce, custody, support, and related disputes.",
    type: "website",
    locale: "en_US",
    url: site.baseUrl,
    siteName: site.name,
  },
  twitter: {
    card: "summary_large_image",
    title: "Law Offices of Wenyu Ding",
    description:
      "Strategic family law representation in San Jose and Santa Clara County.",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-image-preview": "large",
      "max-snippet": -1,
      "max-video-preview": -1,
    },
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:bg-white focus:px-4 focus:py-2">
          Skip to content
        </a>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(legalServiceSchema) }}
        />
        <Header />
        <main id="main-content">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
