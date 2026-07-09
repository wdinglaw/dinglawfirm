# Law Offices of Wenyu Ding Website (Static)

This is a static HTML/CSS/JS website designed for GitHub Pages hosting.

## Folder structure

- `index.html`
- `about.html`
- `practice-areas.html`
- `high-asset-divorce.html`
- `consultation.html`
- `contact.html`
- `privacy.html`
- `disclaimer.html`
- `assets/styles.css`
- `assets/main.js`
- `assets/favicon.svg`
- `assets/images/placeholder-office.svg`

## How to preview locally

Use a local server instead of double-clicking `index.html`. Opening files directly with `file://` can expose local machine paths and can make directory-style links behave differently from the deployed site.

1. From the website root, run:
   ```bash
   python3 -m http.server 8000
   ```
2. Open `http://localhost:8000`.
3. Click through the navigation to verify all pages.

## Publish to GitHub Pages (easy steps)

1. Create a new GitHub repository.
2. Upload all files from the `site` folder to the repository root.
3. In GitHub, open `Settings` then `Pages`.
4. Under "Build and deployment":
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ (root)`
5. Save and wait about 1 to 5 minutes.
6. GitHub will show your live website URL.

## Edit firm content

- Update text directly in each `.html` file.
- Update colors, spacing, and typography in `assets/styles.css`.
- Update menu behavior in `assets/main.js`.
- Replace placeholder office image at `assets/images/placeholder-office.svg`.

## Update consultation scheduling links (Calendly)

In `consultation.html`, replace these URLs with your real links:

- `https://calendly.com/your-calendly-link/consultation`
- `https://calendly.com/your-calendly-link/advanced-consultation`

## Enable payment in Calendly (Stripe)

1. Log in to Calendly.
2. Go to Integrations and connect Stripe.
3. Open each consultation event type.
4. Enable payment collection for the event.
5. Save settings.

This site already states: "Payment is required at the time of scheduling." You only need to connect Stripe in Calendly.

## Form handling (Formspree placeholder)

Forms on `consultation.html` and `contact.html` use a placeholder action:

- `https://formspree.io/f/yourformid`

To activate:

1. Create a free Formspree account.
2. Create a new form and copy your endpoint ID.
3. Replace `yourformid` in both pages.
4. Submit a test message from the live site.

## Important legal note

Review all content before publishing to confirm compliance with California professional responsibility and attorney advertising rules.
