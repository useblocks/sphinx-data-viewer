# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.append(os.path.abspath("."))   # Example if `ub_theme` folder is in the same folder as the `conf.py` file

from ub_theme.conf import ub_html_theme_options

# -- Project information -----------------------------------------------------

project = 'Sphinx-Data-Viewer'
copyright = '2021, team useblocks'
author = 'team useblocks'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_data_viewer",
    'sphinxcontrib.plantuml',
    'sphinx_needs',
    'sphinx_immaterial',
    'sphinx_design',
    'sphinx_copybutton'
]

data_viewer_data = {
    "my_data": {
        "name": "Mario",
        "job": "plumber",
        "magic_tubes": [2, 7, 23, 43.5]
    }
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", "ub_theme/templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_immaterial'
html_title = 'Sphinx-Data-Viewer'
html_logo = '_static/sphinx-data-viewer-logo.svg'
html_favicon = '_static/sphinx-data-viewer-logo.svg'
html_theme_options = ub_html_theme_options
other_options = {
    "repo_url": "https://github.com/useblocks/sphinx-data-viewer",
    "repo_name": "sphinx-data-viewer",
    "repo_type": "github",
}
html_theme_options.update(other_options)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ["_static", "ub_theme/css", "ub_theme/js"]
html_css_files = ["ub-theme.css", "custom.css"]
html_js_files = ["ub-theme.js"]
