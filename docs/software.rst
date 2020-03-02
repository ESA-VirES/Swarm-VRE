Software available
==================

This page introduces some of the key software provided.

Currently there are two Jupyter kernels:

 - Python
 - Octave

----


Python packages
---------------

To see the full list of packages and their version numbers, open a terminal and enter ``conda list``. The usual scientific Python packages including numpy, scipy, and matplotlib, are available. We also include some additional packages relevant to working with Swarm data. These include:

VirES software
``````````````

viresclient
  https://viresclient.readthedocs.io

  This is a programmatic interface to the VirES server, providing flexible access to Swarm data and model evaluations. Custom data sets can be built as CDF/CSV files, and directly as a pandas ``DataFrame`` or an xarray ``Dataset``

Swarm community software
````````````````````````

chaosmagpy
  https://github.com/ancklo/ChaosMagPy

pyamps
  https://pyamps.readthedocs.io

swarmpyfac
  http://swarmpyfac.readthedocs.org

ibp (Ionospheric bubble probability)
  https://gitext.gfz-potsdam.de/rother/ibp-model

Wider geomagnetism and space physics community software
```````````````````````````````````````````````````````

magpysv
  https://github.com/gracecox/MagPySV

apexpy
  https://github.com/aburrell/apexpy

General Python software
```````````````````````

pandas
  https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

xarray
  https://xarray.pydata.org

cartopy
  https://scitools.org.uk/cartopy

dask
  https://docs.dask.org

the HoloViz ecosystem
  https://holoviz.org

Tools to help with notebooks
`````````````````````````````

watermark
  https://github.com/rasbt/watermark

nbval
  https://github.com/computationalmodelling/nbval

nbdime
  https://github.com/jupyter/nbdime

nbgitpuller
  https://github.com/jupyterhub/nbgitpuller

----

We are open to suggestions for other packages and extensions, see e.g.:

  - https://github.com/mauhai/awesome-jupyterlab
  - http://heliopython.org/projects/
  - https://github.com/softwareunderground/awesome-open-geoscience

If the package can be installed trivially by conda or pip, and is actively maintained, then we can probably add it. In other cases, we can look into it but it will take more effort. This is a reason why we should push for software to be packaged using modern tools and follow `standards <https://github.com/heliophysicsPy/standards/blob/master/standards.md>`_.

----


Installing other packages
-------------------------

The default environment comes from a Docker image which is based on the "Jupyter Notebook Scientific Python Stack" (`jupyter/scipy-notebook <https://hub.docker.com/r/jupyter/scipy-notebook/>`_) - with our own extra software and configuration layered on top. This image is loaded when when your container starts (i.e. when you log in). It will spin down when you are not using it and restart when you access it again. If you try to install other software, it may not survive the container restart, depending on how you do it. In any case, you will only be affecting *your* environment. Probably you will run into problems trying to install and use other software if you don't fully understand what you are doing. In this case, if you are interested in having access to some particular software, please :doc:`contact us <help>` and we can consider adding the software to the default environment.

If you install some packages with ``conda install ...`` or ``pip install ...``, this will indeed install them and make them available to the default kernel. *However*, they will disappear the next time your container shuts down. When you have not been active for some period of time (<~hours), the container within which your environment is running will shut down. When you log in again, the environment is created anew from the image that everybody shares, so your modifications will no longer be present. This means that installing packages (& extensions) in this way is only sensible for briefly trying them out.

If you need access to a different collection of packages (e.g. you need a certain unsupported package, or different versions of what is available), then the way to achieve this is through creating an additional kernel, which you can then optionally use to execute scripts or notebooks, in place of the default kernel. This procedure is not covered in full here, but in short:

.. code-block:: bash

  conda create --prefix <kernelname> <packages>

will create the a new conda "environment" (see the existing ones with ``conda env list``). For example:

.. code-block:: bash

  conda create --prefix ~/envs/my_env ipykernel numpy

will create an environment stored within `~/envs/` and called 'my_env', with the packages ipykernel (this is required), and numpy. This kernel then needs to be *registered* with Jupyter:

.. code-block:: bash

  ~/envs/my_env/bin/python -m ipykernel install --user --name my_env --display-name "my_env"

The kernel should now be available to use from within notebooks, and you can also access the environment in a terminal with ``conda activate ~/envs/my_env``. Since we have stored it in the home directory, it will not be lost when the container shuts down. You can see what kernels are installed with ``jupyter kernelspec list``.
