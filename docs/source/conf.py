# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
import matplotlib_latex_bridge as mlb


# -- Project information -----------------------------------------------------

project = 'matplotlib-latex-bridge'
copyright = '2021, Lorenzo Vannucci'
author = 'Lorenzo Vannucci'

# The full version, including alpha/beta/rc tags
release = mlb.__version__


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    'sphinx.ext.autosectionlabel'
]

# to prefix sections labels with the document name
autosectionlabel_prefix_document = True

templates_path = ['_templates']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
