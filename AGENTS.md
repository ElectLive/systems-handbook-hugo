# AGENTS.md

Practical guide for agentic coding assistants operating in this repository.

## Repository at a Glance
- Stack: Python + Sphinx documentation project (Sphinx Book Theme, MyST).
- Main content root: `src/`.
- Sphinx configuration: `src/conf.py`.
- Build artifact directory: `html/`.
- Dependency manager: `uv`.
- Python constraint: `>=3.13,<4.0`.

## Key Files
- `pyproject.toml`: project metadata and dependency constraints.
- `uv.lock`: locked dependency versions.
- `Makefile`: canonical setup and build commands.
- `.editorconfig`: indentation, encoding, newline, whitespace conventions.
- `.github/workflows/build.yml`: CI build + deploy workflow.
- `src/index.rst`: landing page and root toctrees (navigation).
- `src/conf.py`: Sphinx and Book Theme configuration.
- `src/_static/`: static assets (logo and favicon).

## Setup Commands

```bash
make create-dev
```

This runs `uv sync`.

## Build Commands
- Canonical documentation build:

```bash
uv run make build-html
```

- Equivalent direct build:

```bash
uv run sphinx-build --write-all src html
```

- Sphinx does not delete output for removed pages. Run `rm -rf html` before
  building if pages were deleted or renamed.

## Validation
- There are no tests, linters, or pre-commit hooks. Do not add them unless
  requested.
- The docs build is the validation step. It should finish with no warnings.

## Style Guidelines
- Keep changes scoped, minimal, and task-focused.
- Preserve current directory layout and document organization.
- `.rst` files: lowercase names with underscores, 3-space indentation in
  content blocks, consistent heading adornments within a file.
- Markdown pages (via MyST) are allowed alongside `.rst`.
- Keep toctree references relative and valid.
- Encoding: UTF-8. Line endings: LF. Trim trailing whitespace. End files
  with a newline.
- Python (`src/conf.py` only): 4-space indentation, 79-character lines.

## CI Behavior
- Workflow file: `.github/workflows/build.yml`.
- Triggered by pushes to `main` and manual dispatch.
- CI builds with `uv` and `make build-html`, then publishes `html/` with
  GitHub Pages actions (no `gh-pages` branch, no `ghp-import`).

## Agent Working Agreement
- Before finishing substantial changes, run `uv run make build-html` and
  confirm there are no warnings.
- Do not add new tooling (pytest/ruff/mypy/pre-commit/etc.) unless requested.
- Do not modify deployment behavior unless explicitly requested.
- Avoid committing generated artifacts (`html/`, `dist/`) unless required.
