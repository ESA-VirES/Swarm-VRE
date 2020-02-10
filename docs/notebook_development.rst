Notebook development
====================

.. warning::

  In development. Recommendations may change. If you have comments, please `open an issue <https://github.com/ESA-VirES/Swarm-VRE/issues>`_

.. note::

  This page provides practical instructions for how to work with notebooks, specifically using the VRE, but most of the advice applies anywhere. Particular tools and approaches are recommended, though for brevity we do not expound the rationale in detail - we try to point you to the best practices and popular solutions. This guide is a work in progress and any contributions are welcome (`contact us <help.html>`_).

  - Sources:

    - `The Turing Way <https://the-turing-way.netlify.com/>`_
    - `Creating Reproducible Data Science Projects <https://towardsdatascience.com/creating-reproducible-data-science-projects-1fa446369386>`_
    - https://github.com/rdanotebooksbof/outline/blob/master/SummaryFromBoFMeeting.md
    - https://mg.readthedocs.io/git-jupyter.html
    - ... and more

  - Assumed knowledge:

    - how to use git
    - ...

Related notebook repositories
-----------------------------

.. list-table:: Notebook repositories
   :header-rows: 1
   :widths: 7 5 5

   *  -  Name (GitHub Link)
      -  View (nbviewer)
      -  Launch/interact (VRE)
   *  -  `Swarm-DISC/Swarm_notebooks <https://github.com/Swarm-DISC/Swarm_notebooks>`_
      -  .. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
            :target: https://nbviewer.jupyter.org/github/Swarm-DISC/Swarm_notebooks
      -  .. image:: https://img.shields.io/badge/interact-VRE-blue
            :target: https://vre.vires.services/user-redirect/lab/tree/shared/Swarm_notebooks/
   *  -  `smithara/viresclient_examples <https://github.com/smithara/viresclient_examples>`_
      -  .. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
            :target: https://nbviewer.jupyter.org/github/smithara/viresclient_examples
      -  (to do: nbgitpuller link)
   *  -  `pacesm/jupyter_notebooks <https://github.com/pacesm/jupyter_notebooks>`_
      -  .. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
            :target: https://nbviewer.jupyter.org/github/pacesm/jupyter_notebooks
      -  (to do: nbgitpuller link)
   *  - `MagneticEarth/IAGA_SummerSchool2019 <https://github.com/MagneticEarth/IAGA_SummerSchool2019>`_
      - .. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
           :target: https://nbviewer.jupyter.org/github/MagneticEarth/IAGA_SummerSchool2019/
      - (to do: nbgitpuller link)


.. note::

  **Viewing:**

  Sometimes notebooks won't render directly on the GitHub website (or are slow). Try `nbviewer <https://nbviewer.jupyter.org/>`_ instead (see the "Render" links above).

  *Swarm_notebooks* are also rendered on the following pages of this site.

  **Interacting:**

  *Swarm_notebooks* are pre-loaded on the VRE in the shared directory. In this case they are read-only, which means that you can still edit and execute them, but you can't save changes directly.

  Other notebooks must be manually loaded as below (though will soon be made easier easier using nbgitpuller)

Notebooks can be uploaded to JupyterLab using the "Upload" button (which means you must first download the notebooks to your computer from GitHub). To easily access a full repository, open a command line console and use git:

To clone a repository to your working space::

    git clone https://github.com/Swarm-DISC/Swarm_notebooks.git

(this will clone it into ``Swarm_notebooks`` within your current directory)

To clear any changes you made and fetch the latest version, from within ``Swarm_notebooks`` run::

    git fetch
    git reset --hard origin/master


What are notebooks?
-------------------

"Jupyter notebooks [..] allow data scientists to include their original code and interactive visuals alongside a detailed research or analysis output. This allows others to not only understand your analysis but also the story of how you got there, allowing the reader to interact directly with the data and insights." `(source) <https://towardsdatascience.com/creating-reproducible-data-science-projects-1fa446369386>`_

  - Exploratory messing-around (`example <https://github.com/smithara/viresclient_examples>`_)

    - won't be very tidy and reproducibility is low
    - easy way to quickly store your ideas for later or share with somebody else

  - Demonstrations and documentation (`example <http://heliopython.org/gallery/generated/gallery/index.html>`_)

    - used to demonstrate how to use a particular package / system
    - good way to showcase something and can be part of a wider documentation

  - Tutorials (scientific or otherwise) (`example <https://github.com/MagneticEarth/IAGA_SummerSchool2019>`_)

    - ordered and informative with focus on the teaching element
    - can be used as a resource for an in-person workshop
    - for a deep dive, read `Teaching and Learning with Jupyter <https://jupyter4edu.github.io/jupyter-edu-book/>`_

  - Reproducible scientific analysis (example?)

    - high quality scientific content
    - portability and reproducibility is most important
    - can be supplementary material for a publication

.. todo::

  **Problems with notebooks**: problems with: version control, integration with IDEs, testing and CI, linting, PEP8 compliance. These issues are actively being worked on by the data science community and will likely be resolved by Jupyter extensions.

Writing a notebook
------------------

Preamble
++++++++

 The top of the notebook should contain the following things to orientate the user:

- *Short* introduction to what the notebook contains, including links to related notebooks & relevant resources. You may also consider a table of contents.
- List of non-standard requirements for the notebook: e.g. data accessed by the notebook; additional packages to be installed. In the context of the VRE, *non-standard* here refers to anything not supported by the VRE currently (we can then investigate supporting these if appropriate). For a more sophisticated setup, consider a `requirements.txt`_ and/or `environment.yml`_ to specify packages (and versions).
- Import all modules used in the notebook, and specify data file paths (use `pathlib <https://docs.python.org/3/library/pathlib.html#basic-use>`_ for platform-agnostic paths). This will make it clear what other resources (outside the notebook) are required to run it - if you can run this first code cell, you should be able to run the rest.

.. _`requirements.txt`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _`environment.yml`: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Example:

.. todo::

  point to real example


Out-of-order execution...
+++++++++++++++++++++++++

.. todo::

  why/how to avoid this and problems with it

Flow of variables and the namespace (local/global)...
+++++++++++++++++++++++++++++++++++++++++++++++++++++

Use functions to avoid crowding the global namespace - i.e. reduce the occurrence of variables which are only needed within one cell, and build functions that can easily be understood from their name and docstring and can be re-used elsewhere. If a function is particularly useful (can be used in multiple notebooks), move it into an importable Python module, or even to a core package (e.g. viresclient).

.. todo:: diagram showing progress of a tool from notebook (usable by this notebook) to src+notebook (usable by any notebook in this repository) to package+notebook (usable by anybody) -- increasing maturity

.. todo::

  handling software, data dependencies

.. todo:: more style guidance

.. todo:: specific examples and ``Swarm_notebooks`` as best-practice reference



Creating a notebook repository
------------------------------

Notebooks of a certain theme should be collected together in a git repository hosted on GitHub (or equivalents). For an example, see the `materials used at the IAGA Summer School 2019 <https://github.com/MagneticEarth/IAGA_SummerSchool2019>`_. This provides a central location where anyone can contribute, and it can easily be redeployed to any computing environment.

When to create a repository? If you have more than one notebook, it is better to keep them in a repository - this gives you a way to track changes and backup your work as well as making it easy to share by just pointing to a URL. You may choose to keep a repository of assorted notebooks under your GitHub account to manage and share small experiments and code snippets - these could be moved to a more documented thematic repository later. If you have a `portable & reproducible analysis <https://the-turing-way.netlify.com/reproducibility/03/definitions>`_ to share (e.g. supplementary material to a publication), this is perfect for it's own dedicated repository. When there is more than one contributor (or you want to signal that contributions are welcome), use a repository under a GitHub organisation (e.g. `Swarm-DISC <https://github.com/Swarm-DISC/>`_, `MagneticEarth <https://github.com/MagneticEarth/>`_, or your institution's) - add to an existing repository if your notebooks fit the scope.

If the resource is intended to be public eventually, it is easier to make it public from the beginning (i.e. hosting it in an open repository on GitHub). This makes it easy to invite collaborators, provides a consistent workflow to save effort re-tooling later, and prevents inadvertently using non-open components that would delay the release. There are also a number of services available to aid development (plumbed into GitHub) which are available for free to public repositories. If there are issues blocking this initially (e.g. legal), you can still use a private GitHub repository with limited invited collaborators, which will be easy to make public later. Perhaps what you are working on right now is difficult to make public, but you can also consider releasing old projects - it is worth the effort to `make public what you can <https://the-turing-way.netlify.com/open_research/05/opennotebooks.html>`_.

.. todo:: license recommendations

1. `Create a new repo on GitHub <https://github.com/new>`_

   - Choose a name that identifies the scope, e.g. Swarm_notebooks, IAGA_SummerSchool2019, viresclient_examples
   - Choose a license
   - Add a README - written in `markdown (.md) <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>`_ (easier) or `reStructuredText (.rst) <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_
   - Choose a .gitignore
   - Follow the instructions to clone it locally

2. Keep the README updated as the project evolves. This is the first point of call for someone coming across your repository so try to keep it brief yet informative.

   - List contributors, contact info, instructions for contributing
   - Provide instructions for using the notebooks (any external data or software required?)
   - Describe the contents of the notebooks (consider a table of contents)
   - Add *badges* at the top of the README - see `Repository badges`_

3. Add notebooks following a naming convention:

     - If the repository is a tutorial, number them in sequence: ``01_introduction.ipynb, 02_first_steps.ipynb``
     - If there will be several similar experimentative notebooks, append/prepend author initials and dates: ``1_exploratory_analysis_AS_2019-01-01.ipynb``
     - `[More info] <https://www.svds.com/jupyter-notebook-best-practices-for-data-science/>`_

4. If there are files other than notebooks, use a structure like:

.. code-block:: none

  .
  ├── LICENSE
  ├── README.md
  ├── environment.yml
  ├── data
  │    ├── ...           <- Small volumes of data that cannot be robustly accessed in another way
  │                       - For larger data, see below
  ├── notebooks
  │    ├── ...           <- Jupyter notebooks
  └── src
       ├── __init__.py   <- Makes src a Python module
       ├── ...           <- Shared module for this project
                          - This can include functions/classes used in more than one notebook
                          - TODO: Instructions for importing from here

`[More info on this structure] <https://drivendata.github.io/cookiecutter-data-science/#directory-structure>`_


.. todo:: Handling version control `(like this?) <https://mg.readthedocs.io/git-jupyter.html>`_... with nbdime?

.. todo:: making portable with env/reqs specification

.. todo:: handling software and data deps (internal/external ...)

.. todo:: automated testing (Travis-CI / on VRE infrastructure)

Dealing with data
+++++++++++++++++

.. todo:: explain options:

- Go to the source - pull in from somewhere else (with initial build script, or within notebook)
- Git-LFS
- Institutional/external server (with some guarantee that it will remain accessible in the same format...)
- Cloud bucket (EOX could provide this as a service?) and using intake

Repository badges
+++++++++++++++++

"Badges" provide at-a-glance info and dynamic links for metadata, tools to interact with the code, information from services monitoring code health etc.

.. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
    :target: https://nbviewer.jupyter.org/github/smithara/IAGA_SummerSchool2019/tree/master/notebooks/

`NBViewer <https://nbviewer.jupyter.org/>`_ renders notebooks better than GitHub

Markdown::

  [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/smithara/IAGA_SummerSchool2019/tree/master/notebooks/)

reStructuredText::

  .. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
     :target: https://nbviewer.jupyter.org/github/smithara/IAGA_SummerSchool2019/tree/master/notebooks/

.. todo::

  create VRE badge for nbgitpuller: https://shields.io/ https://jupyterhub.github.io/nbgitpuller/link.html

  reStructuredText::

    .. image:: https://img.shields.io/badge/interact-VRE-blue
       :target: https://vre.vires.services/user-redirect/lab/tree/shared/Swarm_notebooks/


Moving beyond notebooks
-----------------------

.. todo:: separate guidance on creating packages: PyPI, Readthedocs, Travis-CI etc.
