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
from os import path, makedirs
from textwrap import dedent

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
print(f"Detected branchname {branchname}")
if branchname not in ["master", "staging"]:
    branchname = "staging"
print(f"For Swarm_notebooks, using branchname {branchname}")


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
    'sphinx.ext.mathjax',
    'sphinx_comments'
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
    'navigation_depth': 2,
    'collapse_navigation':False
}
# Use sphinx-comments to add GitHub-connected comments to each page through utteranc.es
# as well as hypothes.is overlays
comments_config = {
#    "utterances": {
#       "repo": "ESA-VirES/Swarm-VRE",
#       "optional": "config",
#       "issue-term": "pathname",
#       "theme": "github-light",
#       "crossorigin": "anonymous"
#    },
   "hypothesis": True
}

# -- Generate rst files that embed notebooks from Treebeard as iframes -------

def create_notebook_rst_files(branchname):
    """Generates .rst files under ./Swarm_notebooks/ that link to Treebeard"""

    # Titles (to use in docs) and : notebook source names
    # Also check Swarm_notebooks.rst to insert the links in the toctree
    # Generate this list from the notebooks.json in Swarm_notebooks:
    #
    # with open('notebooks.json') as f:
    #     data = json.load(f)
    # notebooks = {}
    # for item in data["notebooks"]:
    #     nbname = path.split(item["path"])[-1]
    #     nbtitle = item["name"]
    #     notebooks[nbtitle] = nbname
    #     group = item["group"]
    #     notebook_groups[group] = notebook_groups.get(group, []) + [nbname]
    #
    notebooks = {
        'Intro to Jupyter & Python': '01a__Intro-Jupyter-Python',
        'Pandas: plot stats, errors...': '01b1_Pandas-and-Plots',
        'Intro to Swarm viresclient': '02a__Intro-Swarm-viresclient',
        'Available data & models': '02b__viresclient-Available-Data',
        'viresclient API document': '02c__viresclient-API',
        'Working with large data': '02d__viresclient-Large-Data',
        'VirES template': '02z1__Template-Basic',
        'MAGx_LR_1B: 1Hz Magnetic': '03a1_Demo-MAGx_LR_1B',
        'MAGx_HR_1B: 50Hz Magnetic': '03a2_Demo-MAGx_HR_1B',
        'EFIx_LP_1B: 2Hz Langmuir probe': '03b__Demo-EFIx_LP_1B',
        'IPDxIRR_2F: 1Hz Plasma data': '03c__Demo-IPDxIRR_2F',
        'TECxTMS_2F: Total e-count': '03d__Demo-TECxTMS_2F',
        'FACxTMS_2F: (Single-sat) FAC': '03e1_Demo-FACxTMS_2F',
        'FAC_TMS_2F: (Dual) + 2D-plot': '03e2_Demo-FAC_TMS_2F',
        'EEFxTMS_2F: Equatorial field': '03f__Demo-EEFxTMS_2F',
        'IBIxTMS_2F: Bubble index': '03g__Demo-IBIxTMS_2F',
        'AEBS: Auroral electrojets LPL': '03h1_Demo-AEBS-AEJxLPL',
        'AEBS: Auroral electrojets LPS': '03h2_Demo-AEBS-AEJxLPS',
        'Model residuals through VirES': '04a1_Geomag-Models-VirES',
        'Forward eval + isolines': '04b1_Geomag-Models-eoxmagmod',
        'Ground observatories - FTP': '04c1_Geomag-Ground-Data-FTP',
        'Ground observatories - VirES': '04c2_Geomag-Ground-Data-VirES',
        'Polar region plots': '05a1_Polar-Region-Plots'
    }
    # These will be displayed without the Treebeard view
    notebooks_deprecated = [
        '04c1_Geomag-Ground-Data-FTP'
    ]

    # Create a directory ./Swarm_notebooks/
    filename_template = path.join(path.dirname(path.realpath(__file__)), "Swarm_notebooks", "{nbname}.rst")
    makedirs(path.dirname(filename_template), exist_ok=True)

    # Text to insert at top of each notebook page
    prolog = dedent("""
    .. warning::

        `THESE PAGES HAVE MOVED TO swarm.magneticearth.org <https://swarm.magneticearth.org>`_

    .. note::

        Please `get in touch <https://swarm-vre.readthedocs.io/en/latest/help.html>`_ if you would like a live demo or want some help! (or if you are able to contribute - ideas are also welcome!)

        | Notebook source: `Swarm-DISC/Swarm_notebooks <https://github.com/Swarm-DISC/Swarm_notebooks/tree/{branchname}/notebooks/{nbname}.ipynb>`_
        | Output views `generated by Treebeard <https://treebeard.io/admin/Swarm-DISC/Swarm_notebooks/{branchname}>`_
        | Notebook name: ``{nbname}.ipynb`` `(download .ipynb) <https://raw.githubusercontent.com/Swarm-DISC/Swarm_notebooks/{branchname}/notebooks/{nbname}.ipynb>`_

    .. raw:: html

        <a href="https://vre.vires.services/user-redirect/lab/tree/shared/Swarm_notebooks/notebooks/{nbname}.ipynb" target="_blank">
            <button type="button">
                <img src="../_static/vre_python_logo.svg.png" width=40></img>
                Launch on VRE!
            </button>
        </a>
    
    {nbtitle}
    """)
    treebeard_view = dedent("""
    .. raw:: html

        <p style="text-align:right">
        <a href="https://via.hypothes.is/https://api.treebeard.io/Swarm-DISC/Swarm_notebooks/{branchname}/notebooks/{nbname}.ipynb">
        <i class="fa fa-external-link-square fa-fw"></i> Fullscreen (highlight text to annotate) 
        </a>
        </p>
        <iframe
            src="https://api.treebeard.io/Swarm-DISC/Swarm_notebooks/{branchname}/notebooks/{nbname}.ipynb"
            frameborder="1" style="height: 1000px; width: 100%;"
        ></iframe>
    """)
    deprecated_notebook_view = dedent("""
    This notebook is no longer maintained. You can still view it at:
    https://github.com/Swarm-DISC/Swarm_notebooks/tree/{branchname}/notebooks/{nbname}.ipynb
    """)

    for nbtitle, nbname in notebooks.items():
        nbtitle_underlined = nbtitle + "\n" + "-"*len(nbtitle)
        page_template = prolog
        # if nbname in notebooks_deprecated:
        #     page_template = prolog + deprecated_notebook_view
        # else:
        #     page_template = prolog + treebeard_view
        filecontents = page_template.format(
            nbtitle=nbtitle_underlined, nbname=nbname, branchname=branchname
        )
        filename = filename_template.format(nbname=nbname)
        with open(filename, "w") as f:
            f.write(filecontents)

create_notebook_rst_files(branchname)