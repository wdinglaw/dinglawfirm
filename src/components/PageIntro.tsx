import { ReactNode } from "react";

type Props = {
  eyebrow?: string;
  title: string;
  description: ReactNode;
};

export default function PageIntro({ eyebrow, title, description }: Props) {
  return (
    <section className="border-b border-line bg-white">
      <div className="section-shell py-14">
        {eyebrow ? <p className="eyebrow">{eyebrow}</p> : null}
        <h1 className="mt-3 max-w-4xl font-display text-4xl leading-tight text-ink md:text-5xl">{title}</h1>
        <p className="mt-5 max-w-3xl text-lg leading-relaxed text-charcoal/85">{description}</p>
      </div>
    </section>
  );
}
