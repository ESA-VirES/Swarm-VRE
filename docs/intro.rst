Introduction
============

What is the VRE?
----------------

"VRE" refers to the "Virtual Research Environment" developed for ESA's *Swarm* mission. This is a cloud service to provide an interactive computational environment to help exploit data from *Swarm*. The system uses an open source system called "JupyterHub", and is integrated with the "VirES for Swarm" service. JupyterHub is a system which orchestrates a multi-user environment in the cloud where users can login to a programming environment called JupyterLab directly in the browser and have access to a common (as in, the same between users) set of software packages. VirES is a service which provides convenient and flexible access to Swarm data and models.

- VirES (**Vir**\ tual environments for **E**\ arth **S**\ cientists) web client: https://vires.services
- VRE (**V**\ irtual **R**\ esearch **E**\ nvironment) login: https://vre.vires.services
- viresclient Python package (i.e. integration with VirES, for Swarm data access): https://viresclient.readthedocs.io

JupyterLab runs in the cloud and enables you to login and run code directly through a web browser without any software needing to be installed on your machine. Data and software are all stored and executed in the cloud. Jupyter itself is language-agnostic, meaning that it is possible to use multiple different programming languages, although it has its roots in Python. We provide a curated software environment (i.e. a collection of installed packages) to support scientific activities related to *Swarm*, with the aim of reliably and easily sharing code between users and stimulating the development of open source software related to Swarm.

.. image:: images/VRE-viresclient.png
   :alt: Architecture of VirES & VRE

Swarm data can be explored graphically through the web client (https://vires.services), or programmatically through JupyterLab (via the Python package, `viresclient <https://viresclient.readthedocs.io/>`_). Both approaches access the **VirES server** which provides more convenient data access than by working with the original data files directly. These systems will be further integrated in the future.

.. image:: images/VRE_shortest_demo.gif

Getting access
--------------

You must first create a VirES account at https://vires.services - it is recommended to use a GitHub account to login, and to use your GitHub username as your VirES username. This will help with identifying user accounts and sharing code both within and outwith the VRE via GitHub. You can then access the VRE right away, either from the top pane of the VirES GUI (click on your username at the top right), or directly at https://vre.vires.services. To start using *viresclient* to access Swarm data, see `the associated documentation <https://viresclient.readthedocs.io/en/latest/installation.html#first-usage-configuration>`_.

Related links
-------------

- Official ESA Swarm website: https://earth.esa.int/web/guest/missions/esa-operational-eo-missions/swarm
- EOX VirES blog posts: https://eox.at/category/vires/
