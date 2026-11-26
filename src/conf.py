# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Loyola University Chicago CS Systems Handbook"
html_title = "Loyola University Chicago CS Systems Handbook"
copyright = "2025, Nicholas M. Synovic"
author = "Nicholas M. Synovic"
release = open("_version", "r").readline()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_logo = "_static/loyola-ramblers-logo.svg"
html_favicon = "_static/loyola-ramblers-logo.svg"
html_theme_options = {
    "repository_url": "https://github.com/LoyolaChicagoBooks/systems-handbook-hugo",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "repository_branch": "main",
    "path_to_docs": "src",
}
