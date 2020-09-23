Software available
==================

This page introduces some of the key software provided. We build on top of the `Jupyter Notebook Scientific Python Stack <https://hub.docker.com/r/jupyter/scipy-notebook>`_ which provides a solid scientific Python environment (i.e. numpy, scipy, pandas, matplotlib...). We add some extra general-purpose Python packages and Jupyter extensions as well as specific packages from the research communities around Swarm. We are actively working towards including more community software. If you think there is an important package missing, please email ashley.smith@ed.ac.uk. For further information on relevant scientific Python packages, you may refer to:

 - `Python in Heliophysics Community <http://heliopython.org/projects/>`_
 - `Resen ("REproducable Software ENvironment" for geospace research) <https://ingeo.datatransport.org/home/resen/packages>`_
 - `Magnetic Earth (community resource for geomagnetism) <https://magneticearth.org/pages/software.html>`_
 - `Software Underground - geoscience software <https://github.com/softwareunderground/awesome-open-geoscience>`_
 - `Awesome JupyterLab - extensions <https://github.com/mauhai/awesome-jupyterlab>`_

To see the full list of installed packages and their version numbers, open a terminal and enter ``conda list``.

----

Python packages
---------------

VirES software (maintained by EOX)
``````````````````````````````````

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Package
     - Description
   * - `viresclient <https://github.com/ESA-VirES/VirES-Python-Client/>`_
     - Access to VirES server (download of Swarm products as pandas/xarray)
   * - `eoxmagmod <https://github.com/ESA-VirES/MagneticModel/>`_
     - Optimised forward evaluation of Swarm geomagnetic models

Swarm community software
````````````````````````

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Package
     - Description
   * - `chaosmagpy <https://github.com/ancklo/ChaosMagPy>`_
     - CHAOS model forward code and geomag modelling utilities
   * - `pyamps <https://github.com/klaundal/pyAMPS>`_
     - AMPS model forward code
   * - `swarmpyfac <https://github.com/Swarm-DISC/SwarmPyFAC>`_
     - Implementation of single-spacecraft FAC algorithm
   * - `ibp <https://gitext.gfz-potsdam.de/rother/ibp-model>`_
     - Ionospheric bubble probability forward code

Wider geomagnetism and space physics community software
```````````````````````````````````````````````````````

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Package
     - Description
   * - `magpysv <https://github.com/gracecox/MagPySV>`_
     - Generating secular variation time series from ground observatory data
   * - `apexpy <https://github.com/aburrell/apexpy>`_
     - Apex and quasi-dipole coordinate transformations
   * - `spacepy <https://github.com/spacepy/spacepy>`_
     - Tools for space physics

General Python software (highlights)
````````````````````````````````````

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Package
     - Description
   * - `pandas <https://pandas.pydata.org>`_
     - Powerful analysis tool built around dataframes
   * - `xarray <https://xarray.pydata.org>`_
     - For labelled multi-dimensional arrays
   * - `cartopy <https://scitools.org.uk/cartopy>`_
     - Geospatial data processing and maps
   * - `dask <https://docs.dask.org>`_
     - Flexible library for parallel computing
   * - `(holoviz ecosystem) <https://holoviz.org>`_
     - High level tools to simplify visualization

Tools to help with notebooks
`````````````````````````````

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Package
     - Description
   * - `watermark <https://github.com/rasbt/watermark>`_
     - Easily list package versions etc at notebook runtime
   * - `nbval <https://github.com/computationalmodelling/nbval>`_
     - Extends py.test to validate notebooks
   * - `nbdime <https://github.com/jupyter/nbdime>`_
     - Tools for diffing and merging of notebooks
   * - `nbgitpuller <https://github.com/jupyterhub/nbgitpuller>`_
     - Tool for distribution and syncing of notebook repositories

----

We are open to suggestions for other packages and extensions!
  

----

Installing other packages
-------------------------

The default environment comes from a Docker image which is based on the "Jupyter Notebook Scientific Python Stack" (`jupyter/scipy-notebook <https://hub.docker.com/r/jupyter/scipy-notebook/>`_) - with our own extra software and configuration layered on top. This image is loaded when your container starts (i.e. when you log in). It will spin down when you are not using it and restart when you access it again (in its original unmodified state). If you try to install other software, it may not survive the container restart, depending on how you do it. In any case, you will only be affecting *your* environment. Probably you will run into problems trying to install and use other software if you don't fully understand what you are doing. In this case, if you are interested in having access to some particular software, please :doc:`contact us <help>` and we can consider adding the software to the default environment.

If you install some packages with ``conda install ...`` or ``pip install ...``, this will indeed install them and make them available to the default kernel immediately. *However*, they will disappear the next time your container shuts down. When you have not been active for some period of time (<~hours), the container within which your environment is running will shut down. When you log in again, the environment is created anew from the image that everybody shares, so your modifications will no longer be present. This means that installing packages (& extensions) in this way is only sensible for briefly trying them out.

Managing custom environments
````````````````````````````

If you need access to a different collection of packages (e.g. you need a certain unsupported package, or different versions of what is available), then the way to achieve this is through creating an additional kernel, which you can then optionally use to execute scripts or notebooks, in place of the default kernel (the default one will remain available). This procedure is not covered in full here, but in short:

.. code-block:: bash

  conda create --prefix <kernelname> <packages>

will create the a new conda "environment" (see the existing ones with ``conda env list``).

.. note::

  See `the conda documentation <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-location>`_ for more information on this. Note that to create the environment we must use ``--prefix`` rather than ``--name`` to specify the exact location (choosing the home directory), otherwise the environment location will default to ``/opt/conda/envs/`` which is not permanent.

For example:

.. code-block:: bash

  conda create --prefix ~/envs/my_env ipykernel numpy

will create an environment stored within `~/envs/` and called 'my_env', with the packages ipykernel (this is required in order to work with Jupyter), and numpy. This kernel then needs to be *registered* with Jupyter:

.. code-block:: bash

  ~/envs/my_env/bin/python -m ipykernel install --user --name my_env --display-name "my_env"

The kernel should now be available to use from within notebooks, and you can also access the environment in a terminal with ``conda activate ~/envs/my_env``. Since we have stored it in the home directory, it will not be lost when the container shuts down. You can see what kernels are installed and visible to Jupyter with ``jupyter kernelspec list``. A new Python notebook launcher should be automatically added to the "New Launcher" panel, and the kernels can also be switched from within a running notebook by clicking the button normally labelled "Python 3" in the top right of the notebook view.

----

A note on reproducability
-------------------------

An important scenario which is not fully supported by the VRE is ensuring reproducability of code in the future. The VRE is an evolving service which provides a single software environment which is updated over time. As newer versions of packages are installed, we can not guarantee that your code will run exactly the same in the future - this depends on the packages you use and how their behaviours and interfaces change over time. Managing your own custom conda environment as described above is one way to mitigate against this. You may consider the VRE as an easy-to-access environment where you can quickly experiment with things, share demonstrations of your code, run tutorials etc. For a detailed introduction to reproducability, please refer to `The Turing Way <https://the-turing-way.netlify.app/introduction/introduction.html>`_. Another project which you may be interested in if you are working in geospace science is `Resen <https://ingeo.datatransport.org/home/resen>`_ which aims to tackle this issue of reproducability.

Aside from using a consistent software environment, input data must be identical between runs to ensure exact repeatability. VirES provides access to only the most recent available data and model versions. This means that it is not possible to reproduce older results when using viresclient. The product version numbers are available within the data objects returned by viresclient, so you should record these when documenting and publishing your results. If you want to be able to repeat your analysis identically in the future (using the same product versions), we recommend you store the interim data returned by viresclient so that you are no longer relying on the VirES server.