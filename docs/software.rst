Software available
==================

This page introduces some of the key software provided.

Currently there are two Jupyter kernels:

 - Python
 - Octave


Python packages
---------------

To see the full list of packages and their version numbers, open a terminal and enter ``conda list``. The usual scientific Python packages including numpy, scipy, and matplotlib, are available. We also include some additional packages relevant to working with Swarm data. These include:

viresclient
  https://viresclient.readthedocs.io

  This is a programmatic interface to the VirES server, providing flexible access to Swarm data and model evaluations. Custom data sets can be built as CDF/CSV files, and directly as a pandas ``DataFrame`` or an xarray ``Dataset``

pandas
  https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

xarray
  https://xarray.pydata.org/

cartopy
  https://scitools.org.uk/cartopy/

dask
  https://docs.dask.org/


Installing other packages
-------------------------

The default environment comes from a docker image which is based on the "Jupyter Notebook Scientific Python Stack" (`jupyter/scipy-notebook <https://hub.docker.com/r/jupyter/scipy-notebook/>`_) - with our own extra software and configuration layered on top. This image is loaded when when your container starts (i.e. when you log in). It will spin down when you are not using it and restart when you access it again. If you try to install other software, it may not survive the container restart, depending on how you do it. In any case, you will only be affecting *your* environment.

tbc

Extensions
----------

tbc

https://github.com/mauhai/awesome-jupyterlab
