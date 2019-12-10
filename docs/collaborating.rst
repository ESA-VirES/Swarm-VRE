Collaborating
=============

This page provides guidance on how to work on the VRE and collaborate with others.

The primary way to interact with Swarm data on the VRE is through Jupyter notebooks that will be pre-loaded into the environment, but which can also be found as GitHub repositories. It is expected that users can take these notebooks as starting examples for their own analyses and that in time this approach will evolve into community-developed resources.

It is worth considering the *information architecture* which is being developed here:

.. image:: images/SwarmInformationArchitecture.png

Swarm data and models are accessed from the "VirES server" using the "viresclient" Python package. This package can be used directly within a notebook as a data access step as part of a given analysis and/or visualisation in conjunction with other Python packages also available on the VRE. Alternatively some notebooks may use a package (e.g. SwarmPyFAC) which uses viresclient in the background to provide a higher level interface to a given task while hiding the complexity of the data access.

Current notebook repositories:

- https://github.com/smithara/viresclient_examples
- https://github.com/MagneticEarth/IAGA_SummerSchool2019
- https://github.com/pacesm/jupyter_notebooks
- ...

A more coherent set will be produced here:

- https://github.com/Swarm-DISC/Swarm_notebooks

This will be a more focussed guide introducing some products and how to work with them using best practices.

[Coming soon: guides for producing notebooks and packages]
