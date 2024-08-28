# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

from sphinx_data_viewer import __version__

project = "Sphinx-Data-Viewer"
copyright = "2024, team useblocks"
author = "team useblocks"
version = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_data_viewer",
    "sphinxcontrib.plantuml",
    "sphinx_needs",
    "sphinx_design",
    "sphinx_copybutton",
]

data_viewer_data = {
    "my_data": {"name": "Mario", "job": "plumber", "magic_tubes": [2, 7, 23, 43.5]}
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", "ub_theme/templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
html_title = f"Sphinx Data Viewer\nv{version}"
html_favicon = "_static/sphinx-data-viewer-logo-light.svg"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "light_logo": "sphinx-data-viewer-logo-light.svg",
    "dark_logo": "sphinx-data-viewer-logo-dark.svg",
    "source_repository": "https://github.com/useblocks/sphinx-data-viewer",
    "source_branch": "main",
    "source_directory": "docs/",
}
