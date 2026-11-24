"""Render the static homepage for GitHub Pages or create a local preview."""
import argparse
import json
import re
import shutil
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "    <!-- BEGIN TESTIMONIALS -->"
END = "    <!-- END TESTIMONIALS -->"
STYLE = '  <link rel="stylesheet" href="/assets/testimonials.css" />\n'
SCRIPT = '  <script src="/assets/testimonials.js" defer></script>\n'
DISCLAIMER = (
    "Testimonials reflect individual client experiences and do not constitute a "
    "guarantee, warranty, or prediction regarding the outcome of any legal matter."
)


def render_rating(score):
    star = "M8 0.7 10.2 5.3 15.3 6 11.6 9.6 12.5 14.7 8 12.3 3.5 14.7 4.4 9.6 0.7 6 5.8 5.3Z"
    stars = "".join(
        f'<path d="{star}" transform="translate({offset} 0)"/>'
        for offset in range(0, score * 18, 18)
    )
    return (
        '            <p class="testimonial-rating">\n'
        f'              <svg viewBox="0 0 88 16" width="88" height="16" aria-hidden="true" focusable="false">{stars}</svg>\n'
        f'              <span>{score}/5</span>\n'
        '            </p>\n'
    )


def render_card(entry, number, preview):
    name = escape(entry["name"])
    area = escape(entry["practice_area"])
    paragraphs = "\n".join(
        f"              <p>{escape(paragraph)}</p>"
        for paragraph in entry["paragraphs"]
    )
    score = 5 if preview and entry.get("illustrative") is True else entry.get("rating")
    rating = render_rating(score) if type(score) is int and 1 <= score <= 5 else ""
    return f"""          <article class="card testimonial-card" aria-labelledby="testimonial-name-{number}">
            <h3 id="testimonial-name-{number}">{name}</h3>
            <p class="muted testimonial-area">{area}</p>
{rating}            <blockquote class="testimonial-quote" id="testimonial-quote-{number}">
{paragraphs}
            </blockquote>
            <button class="testimonial-toggle" type="button" hidden aria-expanded="false" aria-controls="testimonial-quote-{number}" aria-describedby="testimonial-name-{number}">Read more</button>
          </article>"""


def render_section(entries, preview):
    if not entries:
        return ""
    cards = "\n".join(render_card(entry, index, preview) for index, entry in enumerate(entries, 1))
    note = (
        '          <p class="testimonial-preview-note">Private development preview</p>\n'
        if preview else ""
    )
    disclaimer = "" if preview else f'        <p class="microcopy">{DISCLAIMER}</p>\n'
    return f"""
    <section id="testimonials" class="section section-light" aria-labelledby="testimonials-heading">
      <div class="container">
        <div class="section-heading">
{note}          <h2 id="testimonials-heading">What Our Clients Say</h2>
          <p class="muted">Thoughtful guidance, careful preparation, and practical advice through life's most challenging transitions.</p>
        </div>
        <div class="testimonials-grid">
{cards}
        </div>
{disclaimer}      </div>
    </section>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data", type=Path, help="Path to a JSON array of testimonial entries.")
    parser.add_argument("--preview", type=Path, help="New, local preview directory outside the repository.")
    args = parser.parse_args()

    source = ROOT / "index.html"
    page = source.read_text(encoding="utf-8").replace(STYLE, "").replace(SCRIPT, "")
    entries = json.loads(args.data.read_text(encoding="utf-8"))
    if not args.preview:
        entries = [
            entry for entry in entries
            if entry.get("status") == "published" and entry.get("illustrative") is False
        ]
    section = render_section(entries, args.preview)
    page, count = re.subn(
        re.escape(START) + ".*?" + re.escape(END),
        lambda _: f"{START}\n{section}{END}",
        page,
        flags=re.DOTALL,
    )
    if count != 1:
        parser.error("Expected one testimonials insertion point in index.html.")
    if section:
        page = page.replace("</head>", STYLE + "</head>", 1)
        page = page.replace("</body>", SCRIPT + "</body>", 1)

    if args.preview:
        target = args.preview.resolve()
        if target.is_relative_to(ROOT):
            parser.error("The private preview must be outside the repository.")
        target.mkdir(parents=True)
        shutil.copytree(ROOT / "assets", target / "assets")
        page = page.replace("</head>", '  <meta name="robots" content="noindex, nofollow" />\n</head>', 1)
        (target / "index.html").write_text(page, encoding="utf-8")
    else:
        source.write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
