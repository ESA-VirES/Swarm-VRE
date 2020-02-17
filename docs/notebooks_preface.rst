Swarm Notebooks Overview
========================

.. warning::

  In development

.. note::

  The following pages are generated from the notebooks hosted at https://github.com/Swarm-DISC/Swarm_notebooks - they are also `viewable with nbviewer <https://nbviewer.jupyter.org/github/Swarm-DISC/Swarm_notebooks>`_.

  They can be explored interactively on the VRE:

  .. raw:: html

        <a href="https://vre.vires.services/user-redirect/lab/tree/shared/Swarm_notebooks/"
        target="_blank">
            <button type="button">
                <img src="_static/vre_python_logo.svg.png" width=40></img>
                Launch on VRE!
            </button>
        </a>


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

      [Introduction -general]
       - limited introductions to Python for data science
  01a__Intro-Jupyter-Python.ipynb             DONE - pending updates (AS)
  (?) 01b1_Pandas-and-Plots.ipynb             IN PROGRESS (AS)

      [Introduction -VirES]
       - how to interact with VirES
  02a__Intro-Swarm-viresclient.ipynb          DONE - pending updates (AS)
  02b__viresclient-Available-Data.ipynb       DONE - pending updates (AS)
  02c__viresclient-API.ipynb                  DONE - pending updates (LM)
  02d__viresclient-Large-Data.ipynb           DONE - pending updates (AS)
  02z1__Template-Basic                        DONE - pending updates (DS/AS)

      [VirES Demos]
       - demonstrations of each Swarm product (basic access and plotting)
  03a1_Demo-MAGx_LR_1B.ipynb                  DONE - pending updates (AS)
  03a2_Demo-MAGx_HR_1B.ipynb                  DONE - pending updates (AS)
  03b__Demo-EFIx_LP_1B.ipynb                  DONE - pending updates (AS)
  03c__Demo-IPDxIRR_2F.ipynb                  DONE - pending updates (AS)
  03d__Demo-TECxTMS_2F.ipynb                  DONE - pending updates (AS)
  03e1_Demo-FACxTMS_2F.ipynb                  DONE - pending updates (AS)
  03e2_Demo-FAC_TMS_2F.ipynb                  DONE - pending updates (AS)
  03f__Demo-EEFxTMS_2F.ipynb                  DONE - pending updates (AS)
  03g__Demo-IBIxTMS_2F.ipynb                  DONE - pending updates (AS)

      [Geomagnetic Models]
  04a1_Geomag-Models-VirES.ipynb              DONE - pending updates (AS)
  04b1_Geomag-Models-eoxmagmod.ipynb          DONE - pending updates (AS)

      [Ionosphere]
  05a1_Polar-Region-Plots.ipynb               DONE - pending updates (AS)

Definitions:

.. code-block:: none

  DONE:           currently in Swarm_notebooks repository
  NOT CONFIRMED:  name could change / could be multiple notebooks

04: Geomagnetic Models
----------------------
Demo different magnetic models, plotting etc, together with scientific discussion

Refs:
  - https://github.com/smithara/viresclient_examples/blob/master/inspect_CHAOS_MMA.ipynb
  - https://github.com/smithara/viresclient_examples/blob/master/CHAOS_Core%2BStatic%2BMMA_residuals.ipynb
  - https://github.com/smithara/viresclient_examples/blob/master/model_residuals_and_cartopy.ipynb

05: Ionosphere
--------------

- Plasma properties, currents (FAC, AEJ ...), auroral oval boundaries



Beyond Swarm_notebooks
----------------------

These notebooks are demonstrations of the capabilities of Swarm data and the VirES/VRE platform. They are meant as a tutorial-like resource to help educate the community with showcases of certain tools (including Swarm-related Python packages). It is hoped that this will encourage the development of reproducible analyses as notebook repositories and of more generally applicable packages.
