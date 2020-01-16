Swarm Notebooks Overview
========================

.. warning::

  In development

.. note::

  The following pages are generated from the notebooks hosted at https://github.com/Swarm-DISC/Swarm_notebooks

  | ``TODO: link to launch on VRE`` https://vre.vires.services/
  | Choice: access them as read-only in ``shared`` folder OR pull the repo in with nbgitpuller

.. note::

    The repository has two main branches: the ``dev`` branch contains a history of commits *without* cell outputs, while the ``master`` branch contains the notebooks in an executed form with the outputs included (this is what is rendered on the following pages). Pull requests should be made against the ``dev`` branch with notebooks in a cleared state so as to maintain a clean version history. The ``master`` branch will subsequently be updated with the new changes included. This is in accordance with the guidance at https://mg.readthedocs.io/git-jupyter.html

These notebooks are organised according to a naming convention to categorise and allow for future development::

  01a__<nbname>   Theme 1, subject a
  01b__<nbname>   Theme 1, subject b
  01b1_<nbname>   Theme 1, subject b, addendum 1
  02a__<nbname>   Theme 2, subject a
  ...

01: Generic grounding in Jupyter & Python
-----------------------------------------
.. code-block:: none

  01a__Intro-Jupyter-Python   (in progress)
  01b__<core lib demos>       (could do in the future)
  ...

02: Data access concept through VirES
-------------------------------------
.. code-block:: none

  02a__Intro-Swarm-viresclient             (config, basic data access and plotting)
  02b__viresclient-Available-Data-Models   (identifying available data, configuring models)
  02c__viresclient-API                     (further detail on interacting with viresclient)
  02d__viresclient-Large-Data-Volumes

Refs:
  - https://github.com/smithara/viresclient_examples/blob/master/0_first_usage.ipynb
  - https://github.com/smithara/viresclient_examples/blob/master/1_what_is_available.ipynb
  - https://github.com/smithara/viresclient_examples/blob/master/model_details.ipynb
  - https://github.com/smithara/viresclient_examples/blob/master/large_data_volumes.ipynb


03: Demonstrations of accessing each data product
-------------------------------------------------
.. code-block:: none

  03a__Product-Demo-FAC
  03b__Product-Demo-xyz
  ... for each product/collection

Refs:
  - https://github.com/smithara/viresclient_examples/  basic_XYZ.ipynb


04: Magnetic model comparisons - Scientific notebooks
-----------------------------------------------------
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


Miscellaneous plotting demos
----------------------------

*Include as generic Python demos (01x..) OR fold into some of the above nbs?*

.. code-block:: none

  periodic axes
  isolines (involves magnetic model calculation with eoxmagmod)
  statistics
  error lines
  polar views

Refs:
  - https://github.com/pacesm/jupyter_notebooks/blob/master/Periodic%20Axis.ipynb
  - https://github.com/pacesm/jupyter_notebooks/blob/master/examples/CHAOS-6_Cartopy_Contours.ipynb


Beyond ``Swarm_notebooks``
--------------------------

These notebooks are demonstrations of the capabilities of Swarm data and the VirES/VRE platform. They are meant as a tutorial-like resource to help educate the community with showcases of certain tools (including Swarm-related Python packages). It is hoped that this will encourage the development of reproducible analyses as notebook repositories and of more generally applicable packages.
