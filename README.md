# Loyola CS Systems Handbook

The Loyola University Chicago CS Systems Handbook is a Sphinx-based
documentation project that captures operational knowledge about department
systems, services, labs, and support workflows for students, faculty, and
staff.

Published site: <https://systemshandbook.cs.luc.edu/>

## What This Project Contains

This repository is the source for the handbook website, including:

- Department service documentation (`src/department_services/`)
- ITS-related service guides (`src/its_services/`)
- Dijkstra cluster documentation (`src/dijkstra/`)
- End-user how-to references (`src/how_to/`)

The docs entrypoint is `src/index.rst` (the landing page and navigation), and
Sphinx configuration lives in `src/conf.py`. Static assets such as the logo
live in `src/_static/`.

The site previously used Hugo (Docsy theme). That content was removed in
February 2025 and survives only in git history.

## Project Stack

- Python 3.13+
- Sphinx
- Sphinx Book Theme (`sphinx-book-theme`)
- MyST (`myst-parser`) for optional Markdown pages
- `uv` for environment/dependency management

## Quick Start

### 1) Prerequisites

- Python 3.13
- `uv`
- `make`

### 2) Bootstrap a Development Environment

```bash
make create-dev
```

This command syncs dependencies via `uv`.

### 3) Build the Documentation Locally

```bash
uv run make build-html
```

Generated HTML is written to `html/` (git-ignored). `uv run` makes sure
`sphinx-build` comes from the project environment.

### 4) Preview Locally

```bash
python3 -m http.server --directory html 8000
```

Then open <http://localhost:8000/>. Sphinx does not delete output for pages
you have removed, so run `rm -rf html` before building if you deleted or
renamed pages.

## Build and Release Process

The canonical build target is in `Makefile`:

```bash
uv run make build-html
```

Equivalent direct command:

```bash
uv run sphinx-build --write-all src html
```

The build target also reads the latest git tag, if any, to set the project
version.

Deployment uses GitHub Pages with GitHub Actions (there is no `gh-pages`
branch). The workflow at `.github/workflows/build.yml` runs on every push to
`main` and on manual dispatch. It installs dependencies with `uv`, builds the
site with `make build-html`, and publishes `html/` through
`actions/deploy-pages`. The custom domain is set in the repository's Pages
settings, which must use "GitHub Actions" as the source (Settings, Pages,
Build and deployment).

## Validation

There is no test suite and no lint or format hooks. The docs build is the
validation step; it should finish without warnings. To treat warnings as
errors:

```bash
uv run sphinx-build -W src html
```

## How to Continue Development

### Content updates

1. Add or edit `.rst` files under `src/`. Markdown (`.md`) pages are also
   supported through MyST.
2. Update relevant toctrees (usually in `src/index.rst`).
3. Build locally with `uv run make build-html` and check for warnings.

### Structural updates

- Keep section organization aligned with existing categories:
  `department_services`, `its_services`, `how_to`, and `dijkstra`.
- Ensure links and toctree entries remain relative and valid.
- Keep headings and formatting consistent with surrounding content.

### Dependency/tooling updates

- Modify `pyproject.toml` as needed.
- Refresh lock state with `uv` workflows.
- Re-run `make create-dev` after significant tooling changes.
- Theme and site options (logo, edit buttons, repository link) are set in
  `src/conf.py`.

## Repository Conventions

- Encoding/line endings: UTF-8 with LF (see `.editorconfig`)

See `AGENTS.md` for detailed instructions intended for autonomous coding agents.
