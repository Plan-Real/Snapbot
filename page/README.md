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

Deployment is automated by `.github/workflows/pages.yml`: every push to `master` that
touches `page/` uploads this folder as the Pages artifact and deploys it to
<https://plan-real.github.io/Snapbot/>. Settings → Pages → Source must be set to
**GitHub Actions**.

> Note: "Deploy from a branch" does not work for this repo — the legacy Pages build
> checks out submodules recursively and fails on `snapbot/snapbot_gym`, whose remote
> is not publicly reachable. The workflow above checks out without submodules.

If the final URL ever changes, update the `og:url`, `og:image`, `twitter:image`,
`citation_pdf_url` and JSON-LD URLs in `index.html`.

## Credits

Built with the [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template)
(adopted from the [Nerfies](https://nerfies.github.io) project page).
Licensed under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).
