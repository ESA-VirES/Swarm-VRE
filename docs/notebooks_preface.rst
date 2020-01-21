Swarm Notebooks Overview
========================

.. warning::

  In development

.. note::

  The following pages are generated from the notebooks hosted at https://github.com/Swarm-DISC/Swarm_notebooks

  | ``TODO: link to launch on VRE`` https://vre.vires.services/
  | Choice: access them through a Jupyter extension to explore and add notebooks
  |   OR access them as read-only in ``shared`` folder
  |   OR pull the repo in with nbgitpuller

Notebook catalogue
------------------

These notebooks are organised according to a naming convention to categorise and allow for future development::

  01a__<nbname>   Theme 1, subject a
  01b__<nbname>   Theme 1, subject b
  01b1_<nbname>   Theme 1, subject b, addendum 1
  02a__<nbname>   Theme 2, subject a
  ...

Planned notebook names:

.. code-block:: none

  01a__Intro-Jupyter-Python.ipynb             DONE - pending updates (AS)

  02a__Intro-Swarm-viresclient.ipynb          DONE - pending updates (AS)
  02b__viresclient-Available-Data.ipynb       DONE - pending updates (AS)
  02c__viresclient-API.ipynb                  IN PROGRESS (LM)
  02d__viresclient-Large-Data-Volumes.ipynb   IN PROGRESS (AS)
  02e1_PlotExamples-Cartopy.ipynb             NOT CONFIRMED (MP/AS)
  02e2_PlotExamples-PeriodicAxes.ipynb        NOT CONFIRMED (MP/AS)
  02e3_PlotExamples-LinePlots.ipynb           NOT CONFIRMED (MP/AS)

  03a1_Demo-MAGx_LR_1B.ipynb                  DONE - pending updates (AS)
  03a2_Demo-MAGx_HR_1B.ipynb                  IN PROGRESS (MP/AS)
  03b__Demo-EFIx_LP_1B.ipynb                  DONE - pending updates (AS)
  03c__Demo-IPDxIRR_2F.ipynb                  DONE - pending updates (AS)
  03d__Demo-TECxTMS_2F.ipynb                  DONE - pending updates (AS)
  03e1_Demo-FAC_TMS_2F.ipynb                  IN PROGRESS (AS)
  03e__Demo-FACxTMS_2F.ipynb                  IN PROGRESS (AS)
  03f__Demo-EEFxTMS_2F.ipynb                  DONE - pending updates (AS)
  03g__Demo-IBIxTMS_2F.ipynb                  DONE - pending updates (AS)

  04a__Geomagnetic-Models.ipynb               NOT CONFIRMED

  05a__FAC-Algorithms.ipynb                   NOT CONFIRMED

Definitions:

.. code-block:: none

  DONE:           currently in Swarm_notebooks repository
  NOT CONFIRMED:  name could change / could be multiple notebooks

01: Generic grounding in Jupyter & Python
-----------------------------------------
.. code-block:: none

  01a__Intro-Jupyter-Python
  01b__<core lib demos>       (could do in the future)
  ...

02: Data access concept through VirES
-------------------------------------
.. code-block:: none

  02a__Intro-Swarm-viresclient             (config, basic data access and plotting)
  02b__viresclient-Available-Data-Models   (identifying available data, configuring models)
  02c__viresclient-API                     (further detail on interacting with viresclient)
  02d__viresclient-Large-Data-Volumes      (some strategies for working with larger data)
  02e1_PlotExamples....                    (more complex plot types)

Plot Examples to contain:

.. code-block:: none

  periodic axes (could be nice for the FAC demos)
  isolines (involves magnetic model calculation with eoxmagmod)
  statistics
  error intervals
  polar views

Refs:
  - https://github.com/pacesm/jupyter_notebooks/blob/master/Periodic%20Axis.ipynb
  - https://github.com/pacesm/jupyter_notebooks/blob/master/examples/CHAOS-6_Cartopy_Contours.ipynb

03: Demonstrate accessing each product
--------------------------------------
.. code-block:: none

  03a1_Demo-MAGx_LR_1B           (load and plot example of the data/product)
  etc... for each product/collection, using the official Swarm product names

04: Magnetic model comparisons
------------------------------
Demo different magnetic models, plotting etc, together with scientific discussion

.. code-block:: none

  04a__...

Refs:
  - https://github.com/smithara/viresclient_examples/blob/master/inspect_CHAOS_MMA.ipynb
  - https://github.com/smithara/viresclient_examples/blob/master/CHAOS_Core%2BStatic%2BMMA_residuals.ipynb
  - https://github.com/smithara/viresclient_examples/blob/master/model_residuals_and_cartopy.ipynb

05: FAC Demonstrations
----------------------
.. code-block:: none

  05a__FAC-Algorithms        (overview of algo choices and how to run them)
  05b__<FAC-algo1...> etc.



Beyond Swarm_notebooks
----------------------

These notebooks are demonstrations of the capabilities of Swarm data and the VirES/VRE platform. They are meant as a tutorial-like resource to help educate the community with showcases of certain tools (including Swarm-related Python packages). It is hoped that this will encourage the development of reproducible analyses as notebook repositories and of more generally applicable packages.
