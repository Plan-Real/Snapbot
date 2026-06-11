# Snapbot Project Page

Project page for **"Snapbot: Enabling Dynamic Human Robot Interactions for Real-Time Computational Photography"** (HRI '24 Companion).

- Paper: [ACM DL — 10.1145/3610978.3640712](https://doi.org/10.1145/3610978.3640712)
- Code: [Plan-Real/Snapbot](https://github.com/Plan-Real/Snapbot)

## Structure

- `index.html` — the entire page content
- `static/images/` — paper figures, festival deployment photos, social preview, favicon
- `static/pdfs/paper.pdf` — the camera-ready paper (embedded in the page viewer)
- `static/css`, `static/js` — template assets (Bulma + carousel)

## Deploying on GitHub Pages

The page is self-contained static HTML. Either:

1. **Project site from this folder** — copy `page/` contents to the repo root of a
   `plan-real.github.io`-style repo, or
2. **From this repo** — publish the `page/` folder with a GitHub Actions
   `actions/upload-pages-artifact` step (Settings → Pages → Source: GitHub Actions), or
   move/symlink it to `docs/` and select "Deploy from a branch" → `/docs`.

If the final URL differs from `https://plan-real.github.io/Snapbot/`, update the
`og:url`, `og:image`, `twitter:image`, `citation_pdf_url` and JSON-LD URLs in `index.html`.

## Credits

Built with the [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template)
(adopted from the [Nerfies](https://nerfies.github.io) project page).
Licensed under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).
