# Website

This directory holds the [Hugo](https://gohugo.io/) source of the website built from [`data/`](../data).

**Just want to add or update an entry in the list?** You don't need anything here: edit the YAML files in `data/`
as explained in [CONTRIBUTING.md](../CONTRIBUTING.md). The site is rebuilt and deployed automatically.

What follows is only for those who want to preview the site locally.

## Requirements

[Hugo extended](https://gohugo.io/installation/), same version as in `.github/workflows/site.yml`.

## Commands

Run from the repository root:

| Command | Purpose |
| --- | --- |
| `hugo server --source hugo` | Local dev server on http://localhost:1313/, reloads on every change. Builds in memory, writes nothing to `hugo/public/`. Stop with Ctrl+C. |
| `hugo --source hugo --gc --minify` | One-off production build into `hugo/public/`, same as CI. `--gc` removes unused cached files from `hugo/resources/`, `--minify` compresses HTML, CSS and JS. |
