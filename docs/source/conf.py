# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('../../src'))

# No more mocking needed since we have real dependencies installed!

# -- Project information -----------------------------------------------------
project = 'VCS Metrics'
copyright = '2024, Harsh Dubey, Chulwoo Pack'
author = 'Harsh Dubey, Chulwoo Pack'
release = '1.0.2'
version = '1.0.2'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    # Re-enable now that we have real dependencies
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# Napoleon settings
napoleon_google_style = True
napoleon_numpy_style = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Type hints settings - now that we have real dependencies
typehints_fully_qualified = False
always_document_param_types = True
typehints_document_rtype = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'torch': ('https://pytorch.org/docs/stable/', None),
}

# Auto-generate summary pages
autosummary_generate = True

# Custom CSS
def setup(app):
    app.add_css_file('custom.css')
    #pass

# HTML theme options
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#0d9488',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# HTML context
html_context = {
    "display_github": True,
    "github_user": "yourusername",
    "github_repo": "vcs-metrics",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

# Additional HTML settings
html_title = f"{project} v{version}"
html_short_title = "VCS Metrics"
html_favicon = None

# Show source links
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# Output file base name for HTML help builder
htmlhelp_basename = 'VCSMetricsdoc'