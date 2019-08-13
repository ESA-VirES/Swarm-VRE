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


Useful external links
---------------------

- `Introduction to the JupyterLab interface (blog post) <https://towardsdatascience.com/jupyter-lab-evolution-of-the-jupyter-notebook-5297cacde6b>`_
- `Teaching and Learning with Jupyter (book) <https://jupyter4edu.github.io/jupyter-edu-book/>`_
- `Software Carpentry Python course (using JupyterLab) <https://swcarpentry.github.io/python-novice-gapminder/>`_
