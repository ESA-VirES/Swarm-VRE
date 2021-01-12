Swarm Notebooks Overview
========================

.. note::

  The following pages are generated from the notebooks hosted at https://github.com/Swarm-DISC/Swarm_notebooks

  They can be explored interactively on the VRE:

  .. raw:: html

        <a href="https://vre.vires.services/user-redirect/lab/tree/shared/Swarm_notebooks/notebooks"
        target="_blank">
            <button type="button">
                <img src="_static/vre_python_logo.svg.png" width=40></img>
                Launch on VRE!
            </button>
        </a>

``Swarm_notebooks`` are a guide to the Swarm products and usage of related Python packages, providing demonstrations and replicable recipes to launch analyses of the data. You can browse them organised by theme on the left. In the long term these notebooks are intended to be a community-built resource and so we are open to all forms of contributions - check the README at https://github.com/Swarm-DISC/Swarm_notebooks

The notebook file names follow a naming convention to categorise and allow for future development::

  01a__<nbname>.ipynb   Theme 1, subject a
  01b__<nbname>.ipynb   Theme 1, subject b
  01b1_<nbname>.ipynb   Theme 1, subject b, addendum 1
  02a__<nbname>.ipynb   Theme 2, subject a
  ...

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
   *  -  `pacesm/jupyter_notebooks <https://github.com/pacesm/jupyter_notebooks>`_
      -  .. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
            :target: https://nbviewer.jupyter.org/github/pacesm/jupyter_notebooks
      -  .. image:: https://img.shields.io/badge/nbgitpuller-VRE-blue
            :target: https://vre.vires.services/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fpacesm%2Fjupyter_notebooks&urlpath=lab%2Ftree%2F%2F&branch=master
   *  - `MagneticEarth/IAGA_SummerSchool2019 <https://github.com/MagneticEarth/IAGA_SummerSchool2019>`_
      - .. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
           :target: https://nbviewer.jupyter.org/github/MagneticEarth/IAGA_SummerSchool2019/
      - .. image:: https://img.shields.io/badge/nbgitpuller-VRE-blue
            :target: https://vre.vires.services/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FMagneticEarth%2FIAGA_SummerSchool2019&urlpath=lab%2Ftree%2FIAGA_SummerSchool2019%2F&branch=master
   *  - `klaundal/notebooks <https://github.com/klaundal/notebooks>`_
      - .. image:: https://img.shields.io/badge/render-nbviewer-orange.svg
           :target: https://nbviewer.jupyter.org/github/klaundal/notebooks
      - .. image:: https://img.shields.io/badge/nbgitpuller-VRE-blue
            :target: https://vre.vires.services/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fklaundal%2Fnotebooks&urlpath=lab%2Ftree%2Fnotebooks%2F&branch=master

**Viewing:** Sometimes notebooks won't render directly on the GitHub website (or are slow). Try `nbviewer <https://nbviewer.jupyter.org/>`_ instead (see the "Render" links above). *Swarm_notebooks* are also rendered on the following pages of this site.

**Interacting with Swarm_notebooks:** These are pre-loaded on the VRE in the shared directory. In this case they are read-only, which means that you can still edit and execute them, but you can't save changes directly. On the other hand, clicking their icons in the Launcher in JupyterLab will create an editable copy of them. External notebooks can be loaded manually through the JupyterLab interface, or through git or *nbgitpuller*.

**nbgitpuller:** The "nbgitpuller" links above will automatically pull in external repositories and open them on the VRE. If you are familiar with git then you might instead clone the repository manually, as there is `automatic merging behaviour <https://jupyterhub.github.io/nbgitpuller/topic/automatic-merging.html>`_ which may not do what you want. This tool is useful for easily sharing resources with other people (for example, distributing resources for a class). You can craft your own links using the `nbgitpuller link generator <https://jupyterhub.github.io/nbgitpuller/link?hub=https://vre.vires.services/&repo=https://github.com/Swarm-DISC/Swarm_notebooks>`_ where you should set the JupyterHub URL as ``https://vre.vires.services/``.


