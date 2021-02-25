CESM+DART setup
===============

Cesm+dart setup overview
------------------------

If you found your way to this file without reading more basic DART help files, please read those first. $DART/README is
a good place to find pointers to those files. This document gives specific help in setting up a CESM+DART assimilation
for the first time. Unless you just came from there, also see the ../{your_model(s)}/model_mod.html documentation about
the code-level interfaces and namelist values.

CESM context
^^^^^^^^^^^^

Most other models are either called by DART (low order models), or are run by DART via a shell script command (e.g.
WRF). In contrast, CESM runs its forecast, and then calls DART to do the assimilation. The result is that assimilation
set-up scripts for CESM components focus on modifying the set-up and build of CESM to accommodate DART's needs, such as
multi-instance forecasts, stopping at the assimilation times to run filter, and restarting with the updated model state.
The amount of modification of CESM depends on which version of CESM is being used. Later versions require fewer changes
because CESM has accommodated more of DART's needs with each CESM release. This release of DART focuses on selected CESM
versions from 1_2_1 onward, through CESM2 (June, 2017) and versions to be added later. Using this DART with other CESM
versions will quite possibly fail.

Since the ability to use DART has not been completely integrated into CESM testing, it is necessary to use some CESM
fortran subroutines which have been modified for use with DART. These must be provided to CESM through the SourceMods
mechanism. SourceMods for selected versions of CESM are available from the DART website. They can often be used as a
template for making a SourceMods for a different CESM version. If you have other CESM modifications, they must be merged
with the DART modifications.

CESM2
^^^^^

CESM2 (expected release May, 2017) has several helpful improvements, from DART's perspective.

-  Reduced number of subroutines in DART's SourceMods.
-  "Multi-instance" capability enables the ensemble forecasts DART needs.
-  Cycling capability, enabling multiple assimilation cycles in a single job, which reduces the frequency of waiting in
   the queue.
-  Removal of the short term archiver from the run script so that the MPI run doesn't need to idle while the single task
   archiver runs. This significantly reduces the core hours required.
-  CESM's translation of the short term archiver to python, and control of it to an xml file
   ($caseroot/env_archive.xml), so that DART modifications to the short term archiver are more straight-forward.
-  The creation of a new component class, "External Statistical Processing" ("esp"), of which DART is the first
   instance, integrates DART more fully into the CESM development, testing, and running environment. This is the same as
   the atm class, which has CAM as an instance. This will help make DART available in the most recent tagged CESM
   versions which have the most recent CESM component versions.

These have been exploited most fully in the CAM interfaces to DART, since the other components' interfaces still use
older CESMs. The cam-fv/shell_scripts can be used as a template for updating other models' scripting. The multi-cycling
capability, with the short- and long-term archivers running as separate jobs at the end, results in assimilation jobs
which rapidly fill the scratch space. Cam-fv's and pop's assimilate.csh scripts have code to remove older and unneeded
CESM restart file sets during the run. All of DART's output and user selected, restart file sets are preserved.

| DART's manhattan release includes the change to hard-wired input and output filenames in filter. Cam-fv's
  assimilate.csh renames these files into the CESM file format:
| $case.$component{_$instance}.$filetype.$date.nc.
| DART's hard-wired names are used as new filetypes, just like CESM's existing "r", "h0", etc. For example,
  preassim_mean.nc from a CAM assimilation named Test0 will be renamed
| Test0.cam.preassim_mean.2013-03-14-21600.nc
| The obs_seq files remain an exception to this renaming, since they are not in NetCDF format (yet).

CESM component combinations
---------------------------

CESM can be configured with many combinations of its components (CAM, CLM, POP, CICE, ...) some of which may be 'data'
components, which merely read in data from some external source and pass it to the other, active, components to use. The
components influence each other only through the coupler. There are several modes of assimilating observations in this
context.

Single-component assimilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first, and simplest, consists of assimilating relevant observations into one active component. Most/all of the rest
of the components are 'data'. For example, observations of the oceans can be assimilated into the POP model state, while
the atmospheric forcing of the ocean comes from CAM re-analysis files, and is not changed by the observations. A
variation of this is used by CAM assimilations. A CAM forecast usually uses an active land component (CLM) as well as an
active atmospheric component. Atmospheric observations are assimilated only into the CAM state, while the land state is
modified only through its interactions with CAM through the coupler. Each of these assimilations is handled by one of
$DART/models/{cam-fv, pop, clm, ...} If you want to use an unusual combination of active and data components, you may
need to (work with us to) modify the setup scripts.

==================== ====================
|CAM+DART flowchart| |POP+DART flowchart|
==================== ====================

Multi-component assimilation (aka "weakly coupled")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------+---------------------------------------------------------------------------------------+
| |Multi-component flowchart| | It's also possible to assimilate observations into multiple active components, but    |
|                             | restricting the impact of observations to only "their own" component. So in a         |
|                             | "coupled" CESM with active CAM and POP, atmospheric observations change only the CAM  |
|                             | model state while oceanic observations change only the POP model state. This mode     |
|                             | uses multiple DART models; cam-fv and pop in this example to make a filter for each   |
|                             | model.                                                                                |
+-----------------------------+---------------------------------------------------------------------------------------+

Cross-component assimilation (aka "strongly coupled")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------+---------------------------------------------------------------------------------------+
| |Cross-component flowchart| | Work is underway to enable the assimilation of all observations into multiple active  |
|                             | CESM components. So observations of the atmosphere would directly change the POP      |
|                             | state variables and vice versa. Some unresolved issues include defining the           |
|                             | "distance" between an observation in the atmosphere and a grid point in the ocean     |
|                             | (for localization), and how frequently to assimilate in CAM versus POP. This mode     |
|                             | will use code in this models/CESM directory.                                          |
+-----------------------------+---------------------------------------------------------------------------------------+

:doc:`../../cam-fv/model_mod`

$dart/models/{cesm components} organization
-------------------------------------------

.. container:: keepspace

   ======================== ===================================================================
   SCRIPT                   NOTES
   ======================== ===================================================================
   \                        
   $DART/models/**cam-fv**/ A 'model' for each CAM dynamical core (see note below this outline)
   model_mod.\*             The fortran interface between CAM-FV and DART
   shell_scripts/           
   no_assimilate.csh,...    **In**\ dependent_of_cesm_version
   cesm\ **1_5**/           
   setup_hybrid,...         **De**\ pendent on CESM version
   cesm\ **2_0**/           
   setup_hybrid,...         **De**\ pendent on CESM version
   \                        
   $DART/models/**pop**/    A 'model' for each ocean model (MOM may be interfaced next)
   model_mod.\*             The fortran interface between CAM-FV and DART
   shell_scripts/           
   no_assimilate.csh,...    **In**\ dependent_of_cesm_version
   cesm\ **1_5**/           
   setup_hybrid,...         **De**\ pendent on CESM version
   cesm\ **2_0**/           
   setup_hybrid,...         **De**\ pendent on CESM version
   ...                      
   ======================== ===================================================================

::

   For each CAM dynamical core "model", e.g. "cam-fv",  the scripts  in cesm#_# will handle:
      all CAM variants + vertical resolutions (*dy-core is NOT part of this.*):
          CAM5.5, CAM6, ...
          WACCM4, WACCM6, WACCM-X...
          CAM-Chem,
          ...
      all horizontal resolutions of its dy-core:
          1.9x2.5, 0.9x1.25, ..., for cam-fv
          ne30np4, ne0_CONUS,..., for cam-se

Assimilation set-up procedure
-----------------------------

Here is a list of steps to set up an assimilation from scratch, except that it assumes you have downloaded DART and
learned how to use it with low order models. Some of the steps can be skipped if you have a suitable replacement, as
noted.

| 

1.  Decide which component(s) you want to use as the assimilating model(s). (The rest of this example assumes that
    you're building a cam-fv assimilation.) Look in models/cam-fv/shell_scripts to see which CESM versions are
    supported.
2.  CESM: locate that version on your system, or check it out from http://www.cesm.ucar.edu/models/current.html
3.  Choose a start date for your assimilation. Choosing/creating the initial ensemble is a complicated issue.

    -  It's simpler for CAM assimilations. If you don't have an initial state and/or ensemble for this date, build a
       single instance of CESM (Fxxxx compset for cam-fv) and run it from the default Jan 1 start date until 2-4 weeks
       before your start date. Be sure to set the cam namelist variable inithist = 'ENDOFRUN' during the last stage, so
       that CAM will write an "initial" file, which DART needs.
    -  For ocean and land assimilations,which use an ensemble of data atmospheres, creating usable initial ensemble is a
       different process.

4.  Put the entire cam-fv restart file set (including the initial file) where it won't be scrubbed before you want to
    use it. Create a pseudo-ensemble by linking files with instance numbers in them to the restart file set (which has
    no instance number) using CESM/shell_scripts/link_ens_to_single.csh
5.  Choose the options in $dart/mkmf/mkmf.template that are best for your assimilation. These will not affect the CESM
    build, only filter.
6.  In models/cam-fv/work/input.nml, be sure to include all of your required obs_def_${platform}_mod.f90 file names in
    preprocess_nml:input_files. It's also useful to modify the rest of input.nml to make it do what you want for the
    first assimilation cycle. This input.nml will be copied to the $case_root directory and used by assimilate.csh.
7.  Build the DART executables using quickbuild.csh.
8.  Follow the directions in models/cam-fv/shell_scripts/cesm#_#/setup_hybrid to set up the assimilation and build of
    CESM. We recommend a tiny ensemble to start with, to more quickly test whether everything is in order.
9.  After convincing yourself that the CESM+DART framework is working with no_assimilate.csh, activate the assimilation
    by changing CESM's env_run.xml:DATA_ASSIMILATION_SCRIPT to use assimilate.csh.
10. After the first forecast+assimilation cycle finishes correctly, change the input.nml, env_run.xml and env_batch.xml
    to do additional cycle(s) without the perturbation of the initial state, and with using the just created restart
    files. You may also want to turn on the st_archive program. Instructions are in setup_hybrid and
    cam-fv/work/input.nml.
11. Finally, build a new case with the full ensemble, activate the assimilate.csh script and repeat the steps in step
    10.

Output directory
----------------

CESM's short term archiver (st_archive) is controlled by its ``env_archive.xml``. DART's setup scripts modify that file
to archive DART output along with CESM's. (See the :doc:`../../../docs/html/rma` for a description of DART's output).
DART's output is archived in ``$arch_dir/dart/{hist,rest,logs,...}``, where arch_dir is defined in
``setup_{hybrid,advanced}``, ``hist`` contains all of the state space and observation space output, and ``rest``
contains the inflation restart files.

+---------------------------------------+---------------------------------------+---------------------------------------+
| ::                                    | User                                  | Location of scripts and pass-through  |
|                                       |                                       | point for files during execution.     |
|    Central directory                  |                                       | Typically named according defining    |
|                                       |                                       | characteristics of a \*set\* of       |
|                                       |                                       | experiments; resolution, model, obs   |
|                                       |                                       | being assimilated, unique model state |
|                                       |                                       | variables, etc.                       |
+---------------------------------------+---------------------------------------+---------------------------------------+

| -->

The cam-XX assimilate.csh scripts also make a copy of the obs_seq.final files in a scratch space
($scratch/$case/Obs_seqs) which won't be removed by CESM's long term archiver, if that is run.

Helpful hints
-------------

Space requirements
------------------

Space requirements (Gb per ensemble member) for several CAM resolutions.

| 

There are, no doubt, things missing from these lists, so don't struggle too long before contacting dart'at'ucar.edu.

Useful terms found in this web page.

.. |CAM+DART flowchart| image:: ../../../docs/images/science_nuggets/CAM_only.png
   :width: 300px
   :height: 400px
.. |POP+DART flowchart| image:: ../../../docs/images/science_nuggets/POP_only.png
   :width: 550px
   :height: 400px
.. |Multi-component flowchart| image:: ../../../docs/images/science_nuggets/multi-component.png
   :height: 400px
.. |Cross-component flowchart| image:: ../../../docs/images/science_nuggets/cross-component.png
   :height: 400px
