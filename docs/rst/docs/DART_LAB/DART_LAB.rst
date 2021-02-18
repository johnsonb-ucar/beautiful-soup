DART_LAB Tutorial
=================

Contents
========

-  `Overview <#overview>`__
-  `DART tutorial presentations <#dart_tutorial_presentations>`__
-  `Matlab hands-on exercises <#matlab_hands-on_exercises>`__

Overview
--------

The files in this directory contain PDF tutorial materials on DART, and Matlab exercises. See below for links to the PDF
files and a list of the corresponding matlab scripts.

This tutorial begins at a more introductory level than the materials in the tutorial directory, and includes hands-on
exercises at several points. In a workshop setting, these materials and exercises took about 1.5 days to complete.

--------------

.. _dart_tutorial_presentations:

DART tutorial presentations
---------------------------

Here are the PDF files for the presentation part of the tutorial:

-  `Section 1: <presentation/DART_LAB_Section01.pdf>`__ The basics in 1D.
-  `Section 2: <presentation/DART_LAB_Section02.pdf>`__ How should observations of a state variable impact an unobserved
   state variable? Multivariate assimilation.
-  `Section 3: <presentation/DART_LAB_Section03.pdf>`__ Sampling error and localization.
-  `Section 4: <presentation/DART_LAB_Section04.pdf>`__ The Ensemble Kalman Filter (Perturbed Observations).
-  `Section 5: <presentation/DART_LAB_Section05.pdf>`__ Adaptive Inflation.

--------------

.. _matlab_hands-on_exercises:

Matlab hands-on exercises
-------------------------

In the ``matlab`` subdirectory are a set of Matlab scripts and GUI (graphical user interface) programs which are
exercises that go with the tutorial. Each is interactive with settings that can be changed and rerun to explore various
options. A valid `Matlab <http://www.mathworks.com/products/matlab/>`__ license is needed to run these scripts.

The exercises use the following functions:

-  gaussian_product
-  oned_model
-  oned_ensemble
-  run_lorenz_63
-  run_lorenz_96
-  twod_ensemble

To run these, cd into the DART_LAB/matlab directory, start matlab, and type the names at the prompt.

--------------
