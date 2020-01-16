About Jupyter
=============

This page provides guidance regarding the use of Jupyter.

Terminology
-----------

Jupyter can be confusing! So here is a handy list of terms:

Project Jupyter
  The broader open source project and community.

  https://jupyter.org/

Jupyter Notebook
  A notebook document (file extension .ipynb) is a document that can be rendered in a web browser that can contain text, mathematics, images, *live code*, and other interactive elements. "Jupyter Notebook" can also refer to the web application that builds and runs such notebooks.

  https://jupyter-notebook.readthedocs.io/

JupterLab
  This is the evolution of the Jupyter Notebook software providing a richer interface. It is the default interface for the VRE when you first login.

  https://jupyterlab.readthedocs.io/

JupyterHub
  This software runs on servers to provide a multi-user system which automatically spawns and manages instances of JupyterLab/Notebook

  https://jupyterhub.readthedocs.io/

Jupyter kernel
  When used with reference to Jupyter, a "kernel" refers to the program which executes code cells within a notebook. Only one kernel at a time can be connected to a notebook. In the VRE we currently provide two kernels: Python 3.7 (with a number of packages installed), and Octave.

containers, images, and Docker
  A container *image* is a unit of software that holds everything needed to run some particular code. An image is loaded into a *container*, which is an isolated environment where your code can run with a dependable environment based on the image - this is a bit like a virtual machine. Docker is a software system for working with such containers. The environment that a particular image provides is specified by a *Dockerfile* (e.g. `jupyter/scipy-notebook <https://hub.docker.com/r/jupyter/scipy-notebook/dockerfile>`_).

  We employ our own Docker image which is built on top of `jupyter/scipy-notebook`, providing access to JupyterLab and a selection of software relevant to Swarm.

Quick tips
----------

There are some quirks about the behaviour of Jupyter that can be surprising and confusing:

 - There is often effectively *two* right-click menus. To access the other one, hold down shift and then right-click

    - This might vary between browsers and systems (?)
    - This is most noticeable when trying to copy and paste

 - When using the terminal, Ctrl+c and Ctrl+v will not copy and paste. They keyboard shortcuts for copy and paste are Ctrl+Insert and Shift+Insert (this is a normal Unix thing)

 - When using notebooks:

    - Press Ctrl+Enter to execute a cell
    - Press Shift+Enter to execute a cell and advance to the next one
    - There are many more keyboard shortcuts to learn that can help to manipulate notebooks faster
    - Be aware that the execution state of your notebook (i.e. the variables created/changed etc.) is affected by all the cell executions you have made. It is good practice to occasionally refactor and re-run cells in the correct order, and from a fresh un-executed state, as you are developing a notebook, so as to ensure that the notebook outputs will be the same when it is run from scratch. A common way to achieve this is to go to the menu, to Kernel / Restart Kernel and Run All Cells
    - You can switch which *kernel* the notebook is using to run code, by clicking on the kernel name e.g. "Python 3" at the top right of the notebook.

 - The default view when logging in is to load the "JupyterLab" interface. To get the old single-notebook view, go to the menu, to Help / Launch Classic Notebook. (This can be necessary for compatibility with some extensions which have not yet been ported to JupyterLab) This is simply a different *view* for interacting with the system - the software is otherwise identical.
 - Installing things, e.g. using `pip` or `conda` won't behave the same as on a normal machine. See :doc:`software` for more.
 - If you find other things, or otherwise struggling to achieve some task, please :doc:`contact us <help>`.


Useful external links
---------------------

- `Introduction to the JupyterLab interface (blog post) <https://towardsdatascience.com/jupyter-lab-evolution-of-the-jupyter-notebook-5297cacde6b>`_
- `Teaching and Learning with Jupyter (book) <https://jupyter4edu.github.io/jupyter-edu-book/>`_
- `Software Carpentry Python course (using JupyterLab) <https://swcarpentry.github.io/python-novice-gapminder/>`_

A few other examples of JupyterHub deployments:

- http://pangeo.io
- http://data8.org/
- https://www.egi.eu/services/notebooks/
- https://www.dataschool.io/cloud-services-for-jupyter-notebook/
