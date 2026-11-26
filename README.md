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

The docs entrypoint is `src/index.rst`, and Sphinx configuration lives in
`src/conf.py`.

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
make build-html
```

Generated HTML is written to `html/`.

## Build and Release Process

The canonical build target is in `Makefile`:

```bash
make build-html
```

Equivalent direct command:

```bash
sphinx-build --write-all src html
```

Deployment uses GitHub Pages with GitHub Actions (there is no `gh-pages`
branch). The workflow at `.github/workflows/build.yml` runs on every push to
`main` and on manual dispatch. It installs dependencies with `uv`, builds the
site with `make build-html`, and publishes `html/` through
`actions/deploy-pages`. The custom domain is set in the repository's Pages
settings, which must use "GitHub Actions" as the source.

## Validation

There is no test suite and no lint or format hooks. The docs build is the
validation step; it should finish without warnings:

```bash
make build-html
```

## How to Continue Development

### Content updates

1. Add or edit `.rst` files under `src/`.
2. Update relevant toctrees (usually in `src/index.rst` or section indexes).
3. Build locally with `make build-html`.

### Structural updates

- Keep section organization aligned with existing categories:
  `department_services`, `its_services`, `how_to`, and `dijkstra`.
- Ensure links and toctree entries remain relative and valid.
- Keep headings and formatting consistent with surrounding content.

### Dependency/tooling updates

- Modify `pyproject.toml` as needed.
- Refresh lock state with `uv` workflows.
- Re-run `make create-dev` after significant tooling changes.

## Repository Conventions

- Encoding/line endings: UTF-8 with LF (see `.editorconfig`)

See `AGENTS.md` for detailed instructions intended for autonomous coding agents.
