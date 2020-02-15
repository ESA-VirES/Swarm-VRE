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

# Identify current branch of these docs
# - should be "master" or "staging", to match both Swarm-VRE & Swarm_notebooks
# NB relies on this code executing from this file location
command_output = run("git rev-parse --abbrev-ref HEAD".split(),
                     check=True, capture_output=True, text=True)
branchname = command_output.stdout.strip("\n")
# The above doesn't work on readthedocs (it thinks it's always on master?)
# A quick hack to make it work, based on the output of pwd:
# /home/docs/checkouts/readthedocs.org/user_builds/swarm-vre/checkouts/staging/docs
command_output = run("pwd", capture_output=True, text=True)
workingdir = command_output.stdout.strip("\n")
if "readthedocs" in workingdir:
    if "staging" in workingdir:
        branchname = "staging"
    elif "master" in workingdir:
        branchname = "master"
print(f"Using branchname {branchname}")
# Fetch external notebook repository
# and switch to the branch to match the branch of these docs
if not path.exists("Swarm_notebooks"):
    run(["git", "clone",
         "https://github.com/Swarm-DISC/Swarm_notebooks.git",
         "Swarm_notebooks"],
        check=True)
    run(f"git -C Swarm_notebooks/ checkout {branchname}".split())
else:
    run(f"git -C Swarm_notebooks/ checkout {branchname}".split())
    run("git -C Swarm_notebooks/ pull".split())


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
        (`download .ipynb <{{
        "https://raw.githubusercontent.com/Swarm-DISC/Swarm_notebooks/master/"
        + nbname }}>`_)
    | `Alternative view with nbviewer <{{
        "https://nbviewer.jupyter.org/github/Swarm-DISC/Swarm_notebooks/tree/master/"
        + nbname }}>`_ - sometimes the formatting below can be messed up
        as it is processed by nbsphinx

    .. raw:: html

        <a href={{
            "https://vre.vires.services/user-redirect/lab/tree/shared/Swarm_notebooks/"
            + nbname }} target="_blank">
            <button type="button">
                <img src="../_static/vre_python_logo.svg.png" width=40></img>
                Launch on VRE!
            </button>
        </a>
"""
if branchname == "staging":
    nbsphinx_prolog += """\n
.. warning::

    | You are currently viewing the staging branch and links above are
        invalid. Instead use:
    | `Alternative view with nbviewer <{{
        "https://nbviewer.jupyter.org/github/Swarm-DISC/Swarm_notebooks/tree/staging/"
        + nbname }}>`_
    | `Download .ipynb <{{
        "https://raw.githubusercontent.com/Swarm-DISC/Swarm_notebooks/staging/"
        + nbname }}>`_
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
html_logo = '_static/vre_logo_light.svg'
# See https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    'navigation_depth': 1
}
