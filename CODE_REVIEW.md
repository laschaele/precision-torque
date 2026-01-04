# Code review notes

## Navigation consistency
- Only `contact.html` marks the active navigation link with `aria-current="page"`, while other pages omit it, which makes screen reader navigation less clear and misses an opportunity for visual active states via CSS.
- Primary call-to-action targets differ between pages (`/contact.html` vs `/book.html`), so users may experience context switching; decide on a single booking path and standardize the header button everywhere.

## Internal link audit (relative vs. root-absolute)
- `about.html` mixes relative nav/footer links (`index.html`, `about.html`, `contact.html`, `blog/index.html`) with a single root-absolute link (`/services.html`), which can break if the page is rendered from a nested path; standardize them to root-absolute.
- `services.html` uses relative links in the header and footer (`index.html`, `about.html`, `blog/index.html`, `contact.html`, plus service detail links) rather than root-absolute, so URLs change meaning when browsed from subdirectories.
- Blog articles in `blog/` rely on `../` relative paths for nav/footer items and link back to `blog/index.html` via `index.html`, which requires careful directory depth awareness and makes migration harder; switch to leading-slash links.
- Site-wide recommendation: adopt root-absolute URLs (e.g., `/about.html`, `/services.html`, `/blog/index.html`, `/contact.html`) for all internal navigation/CTA/footer links, including blog posts, to keep behavior consistent regardless of the current path or any future routing changes.

## Performance and head hygiene
- Several pages (for example `index.html` and `about.html`) load Google Fonts without the `preconnect` hints used on `contact.html`, adding extra DNS/TLS latency.
- Consider moving repeated metadata (favicon, font links, stylesheet import) into a shared include/templating step to avoid duplication and drift.

## Structured data
- Structured data is defined on `contact.html` only; propagating a `LocalBusiness` JSON-LD block across main entry pages will improve consistency for search engines and rich results.

## Accessibility and forms
- Form helper copy in `contact.html` is visually helpful but not programmatically tied to inputs; associating helper text with `aria-describedby` and ensuring error states are conveyed would improve accessibility.

## Content clarity
- The homepage hero headings and service tiles are strong, but the blog/resource pages could benefit from concise excerpts and clear author/date metadata to build trust and scannability.
