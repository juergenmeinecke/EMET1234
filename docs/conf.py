# docs/conf.py
from __future__ import annotations

import datetime

# -- Project information -----------------------------------------------------
project = "EMET1234"
author = "Your Name"
copyright = f"{datetime.datetime.now().year}, {author}"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.mathjax",        # LaTeX math in .rst (and MyST markdown)
    "myst_nb",                   # render .ipynb as pages
    "sphinx.ext.autosectionlabel",
]

# If you want to reference headings across files without duplicates warnings:
autosectionlabel_prefix_document = True

# Recognize these source file types
source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "myst-nb",
    # ".md": "myst-nb",  # uncomment if you also want Markdown pages
}

master_doc = "index"

exclude_patterns = [
    "_build",
    "**/.ipynb_checkpoints",
    ".DS_Store",
    "Thumbs.db",
]

# -- MyST-NB / notebooks -----------------------------------------------------
# Keep builds deterministic and fast: do not execute notebooks during the Sphinx build.
nb_execution_mode = "off"

# Optional: show tracebacks nicely if a notebook *is* executed in the future
nb_execution_show_tb = True

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"  # built-in (no extra install)

# If you later install a nicer theme, you can switch to e.g.:
# html_theme = "furo"
# html_theme = "sphinx_rtd_theme"

# If you have a _static folder for CSS/images, keep this; otherwise it's harmless.
html_static_path = ["_static"]

# Copy these folders verbatim into the built site root (so URLs are stable):
#   /lecture_notes/<file>.pdf
#   /data/<file>.csv
html_extra_path = [
    "lecture_notes",
    "data",
]

# -- MathJax tweaks (optional) ----------------------------------------------
# Usually you can leave this alone. Uncomment if you want custom macros.
# mathjax3_config = {
#     "tex": {"macros": {"R": r"\mathbb{R}"}},
# }

