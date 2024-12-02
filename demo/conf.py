# -- Project information
project = "Demo of atsphinx-revealjs-desktop"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = "0.0.0"

# -- General configuration
extensions = ["atsphinx.revealjs_desktop"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]
