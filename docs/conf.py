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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from subprocess import run
from os import path

# Fetch external notebook repository
if not path.exists("Swarm_notebooks"):
    run(["git", "clone",
         "https://github.com/Swarm-DISC/Swarm_notebooks.git",
         "Swarm_notebooks"],
        check=True)
else:
    run(["git", "-C", "Swarm_notebooks/", "pull"])


# -- Project information -----------------------------------------------------

project = 'Swarm VRE'
copyright = '2019, EOX'
author = 'EOX'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'nbsphinx',
    'sphinx.ext.mathjax',
]
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- nbsphinx configuration - see https://nbsphinx.readthedocs.io ------------
nbsphinx_prolog = """
{% set nbpath = env.doc2path(env.docname, base=None) %}
{% set nbname = '/'.join(nbpath.split('/')[1:]) %}
.. note::

    | Notebook source repo: https://github.com/Swarm-DISC/Swarm_notebooks
    | Notebook name: ``{{ nbname }}``
    | `Download as .ipynb (right click and save as) <{{
        "https://raw.githubusercontent.com/Swarm-DISC/Swarm_notebooks/master/"
        + nbname }}>`_
    | (TODO: VRE access link)
"""
nbsphinx_execute = 'never'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = '_static/vre_logo.svg'
# See https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    'navigation_depth': 1
}
