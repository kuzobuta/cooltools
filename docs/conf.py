# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'cooltools'
copyright = '2019, cooltoolers'
author = 'cooltoolers'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'nbsphinx',
]

# Extension configuration
napoleon_google_docstring = False
# napoleon_use_param = False
# napoleon_use_ivar = True
napoleon_use_rtype = False

autodoc_mock_imports = [
    'numpy',
    'scipy',
    'cython',
    'matplotlib',
    'pandas',
    'h5py',
    'numba',
    'dask',
    'scikit-learn',
    'cooler',
    'click',
]

# Apparently, readthedocs looks for contents.rst by default if this isn't set.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# Notebook prolog and epilog
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base='docs') %}
.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::
        This page was generated from `{{ docname }}`__.

"""
nbsphinx_epilog = """
----

Generated by nbsphinx_ from a Jupyter_ notebook.

.. _nbsphinx: https://nbsphinx.readthedocs.io/
.. _Jupyter: https://jupyter.org/
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Style overrides ----------------------------------------------------------
# Place CSS in _static directory
# def setup(app):
#     app.add_stylesheet('theme_overrides.css')
