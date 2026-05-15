import type { Metadata } from "next";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export const metadata: Metadata = {
  title: {
    default: "Law Offices of Wenyu Ding | Family Law Attorney in Santa Clara County",
    template: "%s | Law Offices of Wenyu Ding",
  },
  description:
    "Boutique California family law firm serving San Jose, Santa Clara County, and the Bay Area with strategic divorce and custody representation.",
  metadataBase: new URL("https://www.dinglawfirm.com"),
  alternates: { canonical: "/" },
  openGraph: {
    title: "Law Offices of Wenyu Ding",
    description:
      "Strategic family law representation for divorce, custody, support, and property issues in Santa Clara County and the Bay Area.",
    type: "website",
    locale: "en_US",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:bg-white focus:px-4 focus:py-2">
          Skip to content
        </a>
        <Header />
        <main id="main-content">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
