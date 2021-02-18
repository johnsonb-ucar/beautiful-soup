DART Documentation Main Index
=============================

Contents
========

-  `Overview <#overview>`__
-  `Software updates <#software_updates>`__
-  `User documentation and tutorials <#user_documentation_and_tutorials>`__
-  `Programs <#programs>`__
-  `Models <#models>`__
-  `Namelists <#namelists>`__
-  `Modules <#modules>`__
-  `Directory tree <#directory_tree_>`__
-  `Other documentation <#other_documentation>`__
-  `Complete list of all documentation <#complete_list_of_all_documentation>`__

Overview
--------

The Data Assimilation Research Testbed (DART) is a public-domain, community facility for doing research on and applying
ensemble data assimilation techniques over a variety of models and observation types. It includes many example models
and support for common observation types and for different filter types. It also includes material for teaching and
learning the basic principles of data assimilation.

DART strives to implement general solutions which work over a range of models and observation types, and to develop
theory-based algorithms that solve the many real problems encountered when doing ensemble data assimilation. The
algorithms in DART are tested on both simple one-dimensional models (e.g. the Lorenz series of models) as well as
full-up 3D NWP (Numerical Weather Prediction) models and GCMs (Global Climate Models). The basic Kalman filter code can
be written in a few lines. In practice, however, there are a variety of difficulties resulting from sampling error,
model bias, observation error, lack of model divergence, variations in observation density in space and time, etc. There
are tools built into the DART framework to address many of these problems.

This release of DART includes many new features. DART will now read directly from NetCDF files. If your model uses
NetCDF file format the model_to_dart and dart_to_model steps are no longer needed. Given that many jobs spend a large
percentage of time doing file I/O, this can be a significant speedup in the overall assimilation cycle. DART now
distributes the ensemble of model states across the MPI tasks, removing the hard memory limit that a single ensemble
member's data fit into the memory of a single task. This removes the memory limit for models at high resolution or with
nested grids. DART can assimilate forward operators computed outside of the filter process. Users can provide a table of
observations and state vector items along with a factor that can easily prevent one class of observations from impacting
another class of state vector data, and vice versa. The DART directory structure has been revamped to help users more
easily find the various utilities, tools, supported models, and observation types that come with the DART distribution.
The Matlab diagnostic routines have been rewritten to no longer require the external MEXNC toolbox. They now use the
intrinsic Matlab NetCDF functions.

To get started, look here:

-  Our extensive `web pages <http://www.image.ucar.edu/DAReS/>`__
-  The `release notes <html/Manhattan_release.html>`__ which include installation hints, a walk-through of building and
   running a model, and an overview of the diagnostics.
-  Documentation for the main assimilation program `filter </assimilation_code/programs/filter/filter.html>`__
-  Documentation for the other related programs that come with DART
-  Documentation for `observation types </observations/obs_converters/observations.html>`__ supported by DART
-  Documentation for the Matlab diagnostic tools
-  Discussion of `localization </assimilation_code/modules/assimilation/assim_tools_mod.html>`__,
   `inflation </assimilation_code/programs/filter/filter.html#Inflation>`__
-  The web pages specific to each model
-  The web pages specific to each observation type

The best way to get to know the DART software is to follow along while reading the tutorial documents in the
`DART_LAB <DART_LAB/DART_LAB.html>`__ and then the `DART/tutorial <tutorial/index.html>`__ directory.

The latest official release is named "Manhattan". See the extensive release notes
`Manhattan_release <html/Manhattan_release.html>`__ which include installation help, a walk-through of building and
running a model, and then examples of how to use the diagnostics to evaluate the success of the assimilation. See
`Manhattan_diffs_from_Lanai <html/Manhattan_diffs_from_Lanai.html>`__ for a brief summary of changes since Lanai,
including new functionality, new models and tools, and any non-backwards-compatible changes since the Lanai release.

Future releases of DART are expected to have substantial changes and will be less backwards compatible than has been
historically true with DART releases. New development will continue on a separate subversion branch.

Every source file in the DART system has a corresponding .html file that contains specifics for public interfaces in
each of the DART modules, for the executable programs which come with DART, and for how to interface new models into the
DART system.

The remainder of this page contains links to all the documentation for this DART release.

--------------

.. _software_updates:

Software updates
----------------

Updates to the release are now summarized in a file at the top level called `CHANGELOG </CHANGELOG>`__. The latest
updates are at the end of this file.

--------------

.. _user_documentation_and_tutorials:

User documentation and tutorials
--------------------------------

Start `here <http://www.image.ucar.edu/DAReS/>`__ if you are looking for DART User-level HTML documentation. DART comes
with an extensive set of documentation including release notes for each version, a walk-through on-line tutorial, and a
full set of pdf and framemaker tutorial materials.

The Manhattan `release notes <html/Manhattan_release.html>`__ include installation hints, a walk-through of building and
running a model, and an overview of the diagnostics. It also includes a list of new or changed models, observation
support, diagnostics, and non-backwards compatible changes.

For a shorter summary document of only the changes since the last release see
`Manhattan_diffs_from_Lanai <html/Manhattan_diffs_from_Lanai.html>`__. This may be more helpful for current DART users
who are looking for pointers to differences when they update.

Three tutorials, in PDF format, are available. The first is more introductory and interactive with `PDF documents and
Hands-On Matlab exercises <DART_LAB/DART_LAB.html>`__. The `full-fledged DART Tutorial <tutorial/index.html>`__ is more
of a workshop format, with multiple sections covering various parts of DART with suggested exercises at the end of most
sections.

All sections below this one are detailed information on the programming interfaces of all the DART modules, the namelist
details, the executable programs which are part of DART. For introductory materials, see the links above.

--------------

Programs
--------

DART contains many library functions and separate executable programs. The main DART executable is the ``filter``
program. Other programs generate data or format the diagnostic information.

The executable programs that come with DART include:

-  `filter </assimilation_code/programs/filter/filter.html>`__ - the main assimilation code
-  `perfect_model_obs </assimilation_code/programs/perfect_model_obs/perfect_model_obs.html>`__ - run a model to
   generate synthetic observation values
-  `create_obs_sequence </assimilation_code/programs/create_obs_sequence/create_obs_sequence.html>`__ - interactive
   program to generate observations
-  `create_fixed_network_seq </assimilation_code/programs/create_fixed_network_seq/create_fixed_network_seq.html>`__ -
   repeat a set of observations at multiple times
-  `obs_sequence_tool </assimilation_code/programs/obs_sequence_tool/obs_sequence_tool.html>`__ - general observation
   sequence file manipulation tool
-  `fill_inflation_restart.html </assimilation_code/programs/fill_inflation_restart/fill_inflation_restart.html>`__ -
   [deprecated] - initialize inflation files
-  `advance_time </assimilation_code/programs/advance_time/advance_time.html>`__ - increment calendar times, useful for
   scripting loops
-  `closest_member_tool </assimilation_code/programs/closest_member_tool/closest_member_tool.html>`__ - select DART
   restart file closest to mean
-  `integrate_model </assimilation_code/programs/integrate_model/integrate_model.html>`__ - wrapper for models called as
   subroutines
-  `preprocess </assimilation_code/programs/preprocess/preprocess.html>`__ - used during compiling
-  `mkmf </build_templates/mkmf.html>`__ - used to generate makefiles during compiling
-  `wakeup_filter </assimilation_code/programs/wakeup_filter/wakeup_filter.html>`__ - used when filter runs a parallel
   model advance
-  `system_simulation </assimilation_code/programs/system_simulation/system_simulation.html>`__ (sampling error
   correction) - generate the files used for Sampling Error Correction option

The diagnostic programs that process observations after being assimilated by DART include:

-  `oned/obs_diag </assimilation_code/programs/obs_diag/oned/obs_diag.html>`__ - low order model diagnostics
-  `threed_sphere/obs_diag </assimilation_code/programs/obs_diag/threed_sphere/obs_diag.html>`__ - full 3d model
   diagnostics
-  `obs_seq_to_netcdf </assimilation_code/programs/obs_seq_to_netcdf/obs_seq_to_netcdf.html>`__ - convert output obs
   sequence files into netcdf format
-  `obs_common_subset </assimilation_code/programs/obs_common_subset/obs_common_subset.html>`__ - select a common subset
   of obs from multiple files
-  `obs_selection </assimilation_code/programs/obs_selection/obs_selection.html>`__ - select a given set of obs from a
   longer sequence
-  `obs_seq_coverage </assimilation_code/programs/obs_seq_coverage/obs_seq_coverage.html>`__ - select a consistent set
   of obs through time
-  `obs_seq_verify </assimilation_code/programs/obs_seq_verify/obs_seq_verify.html>`__ - convert obs to a netcdf file
   formatted for forecast verification
-  `compare_states </assimilation_code/programs/compare_states/compare_states.html>`__ - compare fields within multiple
   restart files
-  `model_mod_check </assimilation_code/programs/model_mod_check/model_mod_check.html>`__ - development and testing tool
   during interface development
-  `PrecisionCheck </developer_tests/utilities/PrecisionCheck.html>`__ - compiler/platform check of Fortran real/integer
   precision

The executable programs that convert observations into DART format include:

-  `Observation Conversion Introduction </observations/obs_converters/observations.html>`__
-   
-  `AIRS data </observations/obs_converters/AIRS/AIRS.html>`__
-  `AURA temperature data </observations/obs_converters/AURA/convert_aura.f90>`__ (source)
-  `Aviso+/CMEMS along-track sea level anomalies </observations/obs_converters/AVISO/AVISO.html>`__
-  `Ameriflux tower data </observations/obs_converters/Ameriflux/level4_to_obs.html>`__
-  `CICE data </observations/obs_converters/cice/cice_to_obs.html>`__
-  `CHAMP data </observations/obs_converters/CHAMP/CHAMP_density_text_to_obs.f90>`__ (source)
-  `CNOFS data </observations/obs_converters/CNOFS/CNOFS_text_to_obs.f90>`__ (source)
-  `COSMOS groundwater data </observations/obs_converters/COSMOS/COSMOS_development.html>`__ (development format)
-  `COSMOS groundwater data </observations/obs_converters/COSMOS/COSMOS_to_obs.html>`__
-  `DWL doppler wind lidar data </observations/obs_converters/DWL/dwl_to_obs.html>`__
-  `Even Sphere data </observations/obs_converters/even_sphere/even_sphere.m>`__ (source)
-  `GITM data </observations/obs_converters/text_GITM/text_to_obs.f90>`__ (source)
-  `GPS Radio Occultation data </observations/obs_converters/gps/gps.html>`__
-  `Ground GPS Vtec data </observations/obs_converters/gnd_gps_vtec/gnd_gps_vtec_text_to_obs.f90>`__ (source)
-  `GSI data </observations/obs_converters/GSI2DART/gsi_to_dart.f90>`__ (source)
-  `GTSPP data </observations/obs_converters/GTSPP/GTSPP.html>`__
-  `MADIS data </observations/obs_converters/MADIS/MADIS.html>`__
-  `MIDAS TEC data </observations/obs_converters/MIDAS/MIDAS_to_obs.html>`__ (netcdf intermediate files)
-  `MODIS Snow data </observations/obs_converters/snow/snow_to_obs.html>`__ (source)
-  `MODIS data </observations/obs_converters/MODIS/MODIS_README.html>`__ (ORNL DAAC)
-  `NCEP prepbufr to source </observations/obs_converters/NCEP/prep_bufr/prep_bufr.html>`__
-  `NCEP ascii to obs_seq </observations/obs_converters/NCEP/ascii_to_obs/create_real_obs.html>`__
-  `Oklahoma Mesonet MDF data </observations/obs_converters/ok_mesonet/ok_mesonet.html>`__
-  `QuikSCAT data </observations/obs_converters/quikscat/QuikSCAT.html>`__
-  `ROMS data </observations/obs_converters/ROMS/convert_roms_obs.f90>`__ (source)
-  `Radar data </observations/obs_converters/radar/radar.html>`__
-  `SABER data </observations/obs_converters/SABER/convert_saber_cdf.f90>`__ (source)
-  `SSEC data </observations/obs_converters/SSEC/SSEC.html>`__
-  `SSUSI data </observations/obs_converters/SSUSI/convert_f16_edr_dsk.html>`__
-  `source/text data </observations/obs_converters/text/text_to_obs.html>`__
-  `Tropical Cyclone ATCF reports </observations/obs_converters/tropical_cyclone/tc_to_obs.html>`__ (source)
-  `Total Precipitable Water obs </observations/obs_converters/tpw/tpw.html>`__ (source)
-  `little-r data </observations/obs_converters/var/littler_tf_dart.html>`__
-  `3DVAR radar data </observations/obs_converters/var/rad_3dvar_to_dart.html>`__
-  `var obs data </observations/obs_converters/var/var.html>`__
-  `World Ocean Database data </observations/obs_converters/WOD/WOD.html>`__

--------------

Models
------

DART comes with several models which can be used to learn about data assimilation, to do actual experiments with real
observations, or to use as a template for adding additional models to DART.

All models in the DART project have individual documentation pages, which can be found here (if an html document is not
available, the link is to the .f90 source):

Currently Manhattan has support for many of our larger models such as WRF, POP, CAM, CICE, CLM, ROMS, MPAS_ATM, ... and
all lower models such as lorenz_96. Models previously available on Lanai can still be used with DART
`classic <https://svn-dares-dart.cgd.ucar.edu/DART/releases/classic/>`__.

**Supported in Manhattan**

-  `9var </models/9var/model_mod.html>`__ (html)
-  `bgrid_solo </models/bgrid_solo/model_mod.html>`__ (html)
-  `CAM-FV </models/cam-fv/model_mod.html>`__ (html)
-  `cice </models/cice/model_mod.f90>`__ (source)
-  `CLM </models/clm/model_mod.html>`__ (html)
-  `forced_lorenz_96 </models/forced_lorenz_96/model_mod.html>`__ (html)
-  `Lorenz_04 </models/lorenz_04/model_mod.html>`__ (html)
-  `Lorenz_63 </models/lorenz_63/model_mod.html>`__ (html)
-  `Lorenz_84 </models/lorenz_84/model_mod.html>`__ (html)
-  `Lorenz_96 </models/lorenz_96/model_mod.html>`__ (html)
-  `Lorenz_96_2scale </models/lorenz_96_2scale/model_mod.f90>`__ (source)
-  `MPAS_atm </models/mpas_atm/model_mod.html>`__ (html)
-  `null_model </models/null_model/model_mod.html>`__ (html)
-  `POP </models/POP/model_mod.html>`__ (html)
-  `ROMS </models/ROMS/model_mod.html>`__ (html)
-  `simple_advection </models/simple_advection/model_mod.html>`__ (html)
-  `template </models/template/model_mod.html>`__
-  `WRF </models/wrf/model_mod.html>`__ (html)

**Supported in Classic**

-  `AM2 </models/am2/model_mod.f90>`__ (source)
-  `COAMPS </models/coamps/model_mod.html>`__ (html)
-  `COAMPS_nest </models/coamps_nest/model_mod.f90>`__ (source)
-  `dynamo </models/dynamo/model_mod.f90>`__ (source)
-  `forced_barot </models/forced_barot/model_mod.f90>`__ (source)
-  `GITM </models/gitm/model_mod.html>`__ (html)
-  `ikeda </models/ikeda/model_mod.html>`__ (html)
-  `MITgcm_annulus </models/MITgcm_annulus/model_mod.f90>`__ (source)
-  `MITgcm_ocean </models/MITgcm_ocean/model_mod.html>`__ (html)
-  `MPAS_ocn </models/mpas_ocn/model_mod.html>`__ (html)
-  `NAAPS </models/NAAPS/model_mod.f90>`__ (source)
-  `NCOMMAS </models/NCOMMAS/model_mod.html>`__ (html)
-  `NOAH </models/noah/model_mod.html>`__ (html)
-  `pe2lyr </models/pe2lyr/model_mod.html>`__ (html)
-  `Rose </models/rose/model_mod.f90>`__ (source)
-  `SQG </models/sqg/model_mod.html>`__ (html)
-  `TIEgcm </models/tiegcm/model_mod.f90>`__ (source)

--------------

Namelists
---------

Generally read from the file ``input.nml``. We adhere to the F90 standard of starting a namelist with an ampersand '&'
and terminating with a slash '/'.

Namelists for Programs:

-  `&closest_member_tool_nml </assimilation_code/programs/closest_member_tool/closest_member_tool.html#Namelist>`__
-  `&compare_states_nml </assimilation_code/programs/compare_states/compare_states.html#Namelist>`__
-  `&filter_nml </assimilation_code/programs/filter/filter.html#Namelist>`__
-  `&full_error_nml </assimilation_code/programs/system_simulation/system_simulation.html#Namelist>`__ (system
   simulation)
-  `&model_mod_check_nml </assimilation_code/programs/model_mod_check/model_mod_check.html#Namelist>`__
-  `&obs_common_subset_nml </assimilation_code/programs/obs_common_subset/obs_common_subset.html#Namelist>`__
-  `&obs_diag_nml </assimilation_code/programs/obs_diag/oned/obs_diag.html#Namelist>`__ (oned)
-  `&obs_diag_nml </assimilation_code/programs/obs_diag/threed_sphere/obs_diag.html#Namelist>`__ (threed_sphere)
-  `&obs_loop_nml </assimilation_code/programs/obs_loop/obs_loop.nml>`__
-  `&obs_selection_nml </assimilation_code/programs/obs_selection/obs_selection.html#Namelist>`__
-  `&obs_seq_coverage_nml </assimilation_code/programs/obs_seq_coverage/obs_seq_coverage.html#Namelist>`__
-  `&obs_seq_to_netcdf_nml </assimilation_code/programs/obs_seq_to_netcdf/obs_seq_to_netcdf.html#Namelist>`__
-  `&obs_seq_verify_nml </assimilation_code/programs/obs_seq_verify/obs_seq_verify.html#Namelist>`__
-  `&obs_sequence_tool_nml </assimilation_code/programs/obs_sequence_tool/obs_sequence_tool.html#Namelist>`__
-  `&perfect_model_obs_nml </assimilation_code/programs/perfect_model_obs/perfect_model_obs.html#Namelist>`__
-  `&preprocess_nml </assimilation_code/programs/preprocess/preprocess.html#Namelist>`__

Namelists for Observation Conversion Programs:

-  `&convert_airs_L2_nml </observations/obs_converters/AIRS/AIRS.html#Namelist>`__
-  `&convert_L2b_nml </observations/obs_converters/quikscat/QuikSCAT.html#Namelist>`__
-  `&convert_tpw_nml </observations/obs_converters/tpw/tpw.html#Namelist>`__
-  `&COSMOS_development_nml </observations/obs_converters/COSMOS/COSMOS_development.html#Namelist>`__
-  `&COSMOS_to_obs_nml </observations/obs_converters/COSMOS/COSMOS_to_obs.html#Namelist>`__
-  `&convert_cosmic_gps_nml </observations/obs_converters/gps/gps.html#Namelist>`__
-  `&level4_to_obs_nml </observations/obs_converters/Ameriflux/level4_to_obs.html#Namelist>`__
-  `&MIDAS_to_obs_nml </observations/obs_converters/MIDAS/MIDAS_to_obs.html#Namelist>`__
-  `&MOD15A2_to_obs_nml </observations/obs_converters/MODIS/MOD15A2_to_obs.html#Namelist>`__
-  `&ncepobs_nml </observations/obs_converters/NCEP/ascii_to_obs/create_real_obs.html#Namelist>`__
-  `&tc_to_obs_nml </observations/obs_converters/tropical_cyclone/tc_to_obs.html#Namelist>`__
-  `&rad_3dvar_to_dart_nml </observations/obs_converters/var/rad_3dvar_to_dart.html#Namelist>`__
-  `&wod_to_obs_nml </observations/obs_converters/WOD/WOD.html#Namelist>`__

Namelists for Modules:

-  `&assim_model_mod_nml </assimilation_code/modules/assimilation/assim_model_mod.html#Namelist>`__
-  `&assim_tools_mod_nml </assimilation_code/modules/assimilation/assim_tools_mod.html#Namelist>`__
-  `&cov_cutoff_mod_nml </assimilation_code/modules/assimilation/cov_cutoff_mod.html#Namelist>`__
-  `&ensemble_manager_mod_nml </assimilation_code/modules/utilities/ensemble_manager_mod.html#Namelist>`__
-  `&location_mod_nml </assimilation_code/location/channel/location_mod.html#Namelist>`__ (channel)
-  `&location_mod_nml </assimilation_code/location/column/location_mod.nml>`__ (column)
-  `&location_mod_nml </assimilation_code/location/threed_cartesian/location_mod.html#Namelist>`__ (threed_cartesian)
-  `&location_mod_nml </assimilation_code/location/threed_sphere/location_mod.html#Namelist>`__ (threed_sphere)
-  `&mpi_utilities_mod_nml </assimilation_code/modules/utilities/mpi_utilities_mod.html#Namelist>`__
-  `&obs_def_gps_mod_nml </observations/forward_operators/obs_def_gps_mod.html#Namelist>`__
-  `&obs_def_ocean_mod_nml </observations/forward_operators/obs_def_ocean_mod.nml>`__
-  `&obs_def_radar_mod_nml </observations/forward_operators/obs_def_radar_mod.html#Namelist>`__
-  `&obs_def_tower_mod_nml </observations/forward_operators/obs_def_tower_mod.nml>`__
-  `&obs_def_tpw_mod_nml </observations/forward_operators/obs_def_tpw_mod.nml>`__
-  `&obs_kind_mod_nml </assimilation_code/modules/observations/obs_kind_mod.html#Namelist>`__
-  `&obs_sequence_mod_nml </assimilation_code/modules/observations/obs_sequence_mod.html#Namelist>`__
-  `&reg_factor_mod_nml </assimilation_code/modules/assimilation/reg_factor_mod.html#Namelist>`__
-  `&smoother_mod_nml </assimilation_code/modules/assimilation/smoother_mod.html#Namelist>`__
-  `&schedule_mod_nml </assimilation_code/modules/utilities/schedule_mod.html#Namelist>`__
-  `&utilities_mod_nml </assimilation_code/modules/utilities/utilities_mod.html#Namelist>`__

Namelists for Models:

-  9var `&model_nml </models/9var/model_mod.html#Namelist>`__
-  bgrid_solo `&model_nml </models/bgrid_solo/model_mod.html#Namelist>`__
-  cam `&model_nml </models/cam-fv/model_mod.html#Namelist>`__
-  clm `&model_nml </models/clm/model_mod.html#Namelist>`__
-  coamps `&model_nml </models/coamps/model_mod.html#Namelist>`__
-  coamps_nest `&model_nml </models/coamps_nest/model_mod.html#Namelist>`__
-  forced_lorenz_96 `&model_nml </models/forced_lorenz_96/model_mod.html#Namelist>`__
-  ikeda `&model_nml </models/ikeda/model_mod.html#Namelist>`__
-  lorenz_04 `&model_nml </models/lorenz_04/model_mod.html#Namelist>`__
-  lorenz_63 `&model_nml </models/lorenz_63/model_mod.html#Namelist>`__
-  lorenz_84 `&model_nml </models/lorenz_84/model_mod.html#Namelist>`__
-  lorenz_96 `&model_nml </models/lorenz_96/model_mod.html#Namelist>`__
-  lorenz_96_2scale `&model_nml </models/lorenz_96_2scale/model_mod.html#Namelist>`__
-  MITgcm_ocean `&create_ocean_obs_nml </models/MITgcm_ocean/create_ocean_obs.html#Namelist>`__
-  MITgcm_ocean `&model_nml </models/MITgcm_ocean/model_mod.html#Namelist>`__
-  mpas_atm `&model_nml </models/mpas_atm/model_mod.html#Namelist>`__
-  mpas_ocn `&model_nml </models/mpas_ocn/model_mod.html#Namelist>`__
-  NAAPS `&model_nml </models/NAAPS/model_mod.nml>`__
-  NAAPS `&model_mod_check_nml </models/NAAPS/model_mod_check.nml>`__
-  NCOMMAS `&model_nml </models/NCOMMAS/model_mod.html#Namelist>`__
-  NCOMMAS `&ncommas_vars_nml </models/NCOMMAS/model_mod.html#Namelist>`__
-  noah `&model_nml </models/noah/model_mod.html#Namelist>`__
-  null_model `&model_nml </models/null_model/model_mod.html#Namelist>`__
-  POP `&model_nml </models/POP/model_mod.html#Namelist>`__
-  ROMS `&model_nml </models/ROMS/model_mod.html#Namelist>`__
-  simple_advection `&model_nml </models/simple_advection/model_mod.html#Namelist>`__
-  sqg `&model_nml </models/sqg/model_mod.html#Namelist>`__
-  template `&model_nml </models/template/model_mod.html#Namelist>`__
-  wrf `&model_nml </models/wrf/model_mod.html#Namelist>`__
-  wrf `&replace_wrf_fields_nml </models/wrf/WRF_DART_utilities/replace_wrf_fields.html#Namelist>`__
-  wrf `&wrf_dart_obs_preprocess_nml </models/wrf/WRF_DART_utilities/wrf_dart_obs_preprocess.html#Namelist>`__

--------------

Modules
-------

All modules in the DART project have individual documentation pages, which can be found here:

Assimilation Modules

-  `assimilation_code/modules/assimilation/adaptive_inflate_mod </assimilation_code/modules/assimilation/adaptive_inflate_mod.html>`__
-  `assimilation_code/modules/assimilation/assim_tools_mod </assimilation_code/modules/assimilation/assim_tools_mod.html>`__
-  `assimilation_code/modules/assimilation/assim_model_mod </assimilation_code/modules/assimilation/assim_model_mod.html>`__
-  `assimilation_code/modules/assimilation/assim_tools_mod </assimilation_code/modules/assimilation/assim_tools_mod.html>`__
-  `assimilation_code/modules/assimilation/cov_cutoff_mod </assimilation_code/modules/assimilation/cov_cutoff_mod.html>`__
-  `assimilation_code/modules/assimilation/filter_mod </assimilation_code/modules/assimilation/filter_mod.html>`__
-  `assimilation_code/modules/assimilation/obs_model_mod </assimilation_code/modules/assimilation/obs_model_mod.html>`__
-  `assimilation_code/modules/assimilation/quality_control.f90 </assimilation_code/modules/assimilation/quality_control_mod.f90>`__
   (source)
-  `assimilation_code/modules/assimilation/reg_factor_mod </assimilation_code/modules/assimilation/reg_factor_mod.html>`__
-  `assimilation_code/modules/assimilation/sampling_error_correction_mod.f90 </assimilation_code/modules/assimilation/sampling_error_correction_mod.f90>`__
   (source)
-  `assimilation_code/modules/assimilation/smoother_mod </assimilation_code/modules/assimilation/smoother_mod.html>`__

Location Modules

-  `assimilation_code/location/annulus/location_mod.f90 </assimilation_code/location/annulus/location_mod.f90>`__
   (source)
-  `assimilation_code/location/channel/location_mod </assimilation_code/location/channel/location_mod.html>`__
-  `assimilation_code/location/column/location_mod.f90 </assimilation_code/location/column/location_mod.f90>`__ (source)
-  `assimilation_code/location/oned/location_mod </assimilation_code/location/oned/location_mod.html>`__
-  `assimilation_code/location/threed/location_mod.f90 </assimilation_code/location/threed/location_mod.f90>`__ (source)
-  `assimilation_code/location/threed_cartesian/location_mod </assimilation_code/location/threed_cartesian/location_mod.html>`__
-  `assimilation_code/location/threed_cartesian/xyz_location_mod.f90 </assimilation_code/location/threed_cartesian/xyz_location_mod.f90>`__
   (source)
-  `assimilation_code/location/threed_sphere/location_mod </assimilation_code/location/threed_sphere/location_mod.html>`__
-  `assimilation_code/location/twod/location_mod.f90 </assimilation_code/location/twod/location_mod.f90>`__ (source)
-  `assimilation_code/location/twod_annulus/location_mod.f90 </assimilation_code/location/twod_annulus/location_mod.f90>`__
   (source)
-  `assimilation_code/location/twod_sphere/location_mod.f90 </assimilation_code/location/twod_sphere/location_mod.f90>`__
   (source)

Observation Modules

-  `assimilation_code/modules/observations/DEFAULT_obs_kind_mod </assimilation_code/modules/observations/DEFAULT_obs_kind_mod.html>`__
-  `assimilation_code/modules/observations/forward_operator_mod.f90 </assimilation_code/modules/observations/forward_operator_mod.f90>`__
   (source)
-  `assimilation_code/modules/observations/obs_kind_mod </assimilation_code/modules/observations/obs_kind_mod.html>`__
-  `assimilation_code/modules/observations/obs_sequence_mod </assimilation_code/modules/observations/obs_sequence_mod.html>`__

I/O Modules

-  `assimilation_code/modules/io/dart_time_io_mod.f90 </assimilation_code/modules/io/dart_time_io_mod.f90>`__ (source)
-  `assimilation_code/modules/io/direct_netcdf_mod.f90 </assimilation_code/modules/io/direct_netcdf_mod.f90>`__ (source)
-  `assimilation_code/modules/io/io_filenames_mod.f90 </assimilation_code/modules/io/io_filenames_mod.f90>`__ (source)
-  `assimilation_code/modules/io/single_file_io_mod.f90 </assimilation_code/modules/io/single_file_io_mod.f90>`__
   (source)
-  `assimilation_code/modules/io/state_structure_mod.f90 </assimilation_code/modules/io/state_structure_mod.f90>`__
   (source)
-  `assimilation_code/modules/io/state_vector_io_mod.f90 </assimilation_code/modules/io/state_vector_io_mod.f90>`__
   (source)

Utilities Modules

-  `assimilation_code/modules/utilities/assert_mod.f90 </assimilation_code/modules/utilities/assert_mod.f90>`__ (source)
-  `assimilation_code/modules/utilities/cray_win_mod.f90 </assimilation_code/modules/utilities/cray_win_mod.f90>`__
   (source)
-  `assimilation_code/modules/utilities/distributed_state_mod.f90 </assimilation_code/modules/utilities/distributed_state_mod.f90>`__
   (source)
-  `assimilation_code/modules/utilities/ensemble_manager_mod </assimilation_code/modules/utilities/ensemble_manager_mod.html>`__
-  `assimilation_code/modules/utilities/obs_impact_mod.f90 </assimilation_code/modules/utilities/obs_impact_mod.f90>`__
   (source)
-  `assimilation_code/modules/utilities/parse_args_mod.f90 </assimilation_code/modules/utilities/parse_args_mod.f90>`__
   (source)
-  `assimilation_code/modules/utilities/mpi_utilities_mod </assimilation_code/modules/utilities/mpi_utilities_mod.html>`__
-  `assimilation_code/modules/utilities/random_seq_mod </assimilation_code/modules/utilities/random_seq_mod.html>`__
-  `assimilation_code/modules/utilities/schedule_mod </assimilation_code/modules/utilities/schedule_mod.html>`__
-  `assimilation_code/modules/utilities/sort_mod.f90 </assimilation_code/modules/utilities/sort_mod.f90>`__ (source)
-  `assimilation_code/modules/utilities/time_manager_mod </assimilation_code/modules/utilities/time_manager_mod.html>`__
-  `assimilation_code/modules/utilities/types_mod </assimilation_code/modules/utilities/types_mod.html>`__
-  `assimilation_code/modules/utilities/utilities_mod </assimilation_code/modules/utilities/utilities_mod.html>`__

Example Model Module

-  `models/POP/dart_pop_mod </models/POP/dart_pop_mod.html>`__

Forward Operators Modules

-  `observations/forward_operators/DEFAULT_obs_def_mod </observations/forward_operators/DEFAULT_obs_def_mod.html>`__
-  `observations/forward_operators/DEFAULT_obs_def_mod </observations/forward_operators/DEFAULT_obs_def_mod.html>`__
-  `observations/forward_operators/obs_def_1d_state_mod </observations/forward_operators/obs_def_1d_state_mod.html>`__
-  `observations/forward_operators/obs_def_AIRS_mod.f90 </observations/forward_operators/obs_def_AIRS_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_altimeter_mod.f90 </observations/forward_operators/obs_def_altimeter_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_AOD_mod.f90 </observations/forward_operators/obs_def_AOD_mod.f90>`__ (source)
-  `observations/forward_operators/obs_def_AURA_mod.f90 </observations/forward_operators/obs_def_AURA_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_cice_mod.f90 </observations/forward_operators/obs_def_cice_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_cloud_mod.f90 </observations/forward_operators/obs_def_cloud_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_CO_Nadir_mod.f90 </observations/forward_operators/obs_def_CO_Nadir_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_COSMOS_mod.f90 </observations/forward_operators/obs_def_COSMOS_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_cwp_mod.f90 </observations/forward_operators/obs_def_cwp_mod.f90>`__ (source)
-  `observations/forward_operators/obs_def_dew_point_mod </observations/forward_operators/obs_def_dew_point_mod.html>`__
-  `observations/forward_operators/obs_def_dwl_mod.f90 </observations/forward_operators/obs_def_dwl_mod.f90>`__ (source)
-  `observations/forward_operators/obs_def_eval_mod.f90 </observations/forward_operators/obs_def_eval_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_gps_mod </observations/forward_operators/obs_def_gps_mod.html>`__
-  `observations/forward_operators/obs_def_gts_mod.f90 </observations/forward_operators/obs_def_gts_mod.f90>`__ (source)
-  `observations/forward_operators/obs_def_GWD_mod.f90 </observations/forward_operators/obs_def_GWD_mod.f90>`__ (source)
-  `observations/forward_operators/obs_def_metar_mod.f90 </observations/forward_operators/obs_def_metar_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_mod </observations/forward_operators/obs_def_mod.html>`__
-  `observations/forward_operators/obs_def_ocean_mod </observations/forward_operators/obs_def_ocean_mod.html>`__
-  `observations/forward_operators/obs_def_pe2lyr_mod.f90 </observations/forward_operators/obs_def_pe2lyr_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_QuikSCAT_mod.f90 </observations/forward_operators/obs_def_QuikSCAT_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_radar_mod </observations/forward_operators/obs_def_radar_mod.html>`__
-  `observations/forward_operators/obs_def_radiance_mod.f90 </observations/forward_operators/obs_def_radiance_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_reanalysis_bufr_mod.f90 </observations/forward_operators/obs_def_reanalysis_bufr_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_rel_humidity_mod.f90 </observations/forward_operators/obs_def_rel_humidity_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_SABER_mod.f90 </observations/forward_operators/obs_def_SABER_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_simple_advection_mod.f90 </observations/forward_operators/obs_def_simple_advection_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_sqg_mod.f90 </observations/forward_operators/obs_def_sqg_mod.f90>`__ (source)
-  `observations/forward_operators/obs_def_surface_mod.f90 </observations/forward_operators/obs_def_surface_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_TES_nadir_mod.f90 </observations/forward_operators/obs_def_TES_nadir_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_tower_mod.f90 </observations/forward_operators/obs_def_tower_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_tpw_mod.f90 </observations/forward_operators/obs_def_tpw_mod.f90>`__ (source)
-  `observations/forward_operators/obs_def_upper_atm_mod.f90 </observations/forward_operators/obs_def_upper_atm_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_vortex_mod.f90 </observations/forward_operators/obs_def_vortex_mod.f90>`__
   (source)
-  `observations/forward_operators/obs_def_wind_speed_mod.f90 </observations/forward_operators/obs_def_wind_speed_mod.f90>`__
   (source)

--------------

.. _directory_tree_:

Directory tree
--------------

NOTE: 'work', 'matlab', and 'shell_scripts' directory names have been removed from this list.

::

     |--assimilation_code
     |  |--location
     |  |  |--annulus
     |  |  |--channel
     |  |  |--column
     |  |  |--oned
     |  |  |--threed
     |  |  |--threed_cartesian
     |  |  |--threed_sphere
     |  |  |--twod
     |  |  |--twod_annulus
     |  |  |--twod_sphere
     |  |--modules
     |  |  |--assimilation
     |  |  |--io
     |  |  |--observations
     |  |  |--utilities
     |  |--programs
     |  |  |--advance_time
     |  |  |--closest_member_tool
     |  |  |--compare_states
     |  |  |  |--work
     |  |  |--compute_error
     |  |  |--create_fixed_network_seq
     |  |  |--create_obs_sequence
     |  |  |--fill_inflation_restart
     |  |  |--filter
     |  |  |--gen_sampling_err_table
     |  |  |  |--work
     |  |  |--integrate_model
     |  |  |--model_mod_check
     |  |  |--obs_common_subset
     |  |  |--obs_diag
     |  |  |  |--oned
     |  |  |  |--threed_cartesian
     |  |  |  |--threed_sphere
     |  |  |--obs_impact_tool
     |  |  |--obs_loop
     |  |  |--obs_selection
     |  |  |--obs_seq_coverage
     |  |  |--obs_seq_to_netcdf
     |  |  |--obs_sequence_tool
     |  |  |--obs_seq_verify
     |  |  |--perfect_model_obs
     |  |  |--preprocess
     |  |  |--system_simulation
     |  |  |  |--final_full_precomputed_tables
     |  |  |  |--work
     |  |  |--wakeup_filter
     |  |--scripts
     |--build_templates
     |--developer_tests
     |  |--forward_operators
     |  |--harnesses
     |  |  |--filename_harness
     |  |  |--read_transpose_write
     |  |--io
     |  |  |--work
     |  |--location
     |  |  |--annulus
     |  |  |  |--test
     |  |  |--channel
     |  |  |  |--test
     |  |  |--column
     |  |  |  |--test
     |  |  |--oned
     |  |  |  |--test
     |  |  |--threed
     |  |  |  |--test
     |  |  |--threed_cartesian
     |  |  |  |--test
     |  |  |--threed_sphere
     |  |  |  |--test
     |  |  |--twod
     |  |  |  |--test
     |  |  |--twod_annulus
     |  |  |  |--test
     |  |  |--twod_sphere
     |  |     |--test
     |  |--mpi_utilities
     |  |  |--tests
     |  |--obs_sequence
     |  |  |--data
     |  |  |--work
     |  |--random_seq
     |  |  |--test
     |  |--reg_factor
     |  |--time_manager
     |  |--utilities
     |     |--work
     |--diagnostics
     |  |--matlab
     |     |--deprecated
     |     |--private
     |--docs
     |  |--DART_LAB
     |  |  |--matlab
     |  |  |  |--private
     |  |  |--presentation
     |  |--Graphs
     |  |--html
     |  |  |--boilerplate
     |  |  |--design
     |  |  |--history
     |  |--images
     |  |--tutorial
     |--observations
        |--forward_operators
        |  |--test
        |--obs_converters
           |--AIRS
           |  |--data
           |  |--output
           |--Ameriflux
           |--AURA
           |  |--data
           |--AVISO
           |--CHAMP
           |--cice
           |  |--data
           |--CNOFS
           |--COSMOS
           |  |--data
           |--DWL
           |  |--data
           |--even_sphere
           |--gnd_gps_vtec
           |--gps
           |  |--cosmic
           |  |  |--20071001
           |  |--matlab
           |--GPSPW
           |  |--data
           |--GTSPP
           |  |--data
           |  |--matlab
           |--MADIS
           |  |--data
           |--MIDAS
           |  |--data
           |--MODIS
           |  |--data
           |--NCEP
           |  |--ascii_to_obs
           |  |--prep_bufr
           |     |--blk_ublk
           |     |--convert_bufr
           |     |--data
           |     |  |--201012
           |     |--docs
           |     |  |--Reason_codes
           |     |--exe
           |     |--lib
           |     |--src
           |--obs_error
           |--ok_mesonet
           |  |--data
           |--quikscat
           |  |--data
           |--radar
           |  |--examples
           |--ROMS
           |  |--data
           |--SABER
           |  |--data
           |  |--progs
           |--snow
           |  |--data
           |--SSEC
           |  |--data
           |--SSUSI
           |  |--data
           |--text
           |  |--data
           |--text_GITM
           |--tpw
           |  |--data
           |  |--doc
           |--tropical_cyclone
           |  |--data
           |--utilities
           |  |--oned
           |  |--threed_sphere
           |--var
           |  |--3DVAR_OBSPROC
           |  |--data
           |--WOD
              |--data
            

::

    
     |--models
        |--9var
        |--am2
        |--bgrid_solo
        |  |--fms_src
        |  |  |--atmos_bgrid
        |  |  |  |--driver
        |  |  |  |  |--solo
        |  |  |  |--model
        |  |  |  |--tools
        |  |  |--atmos_param
        |  |  |  |--hs_forcing
        |  |  |--atmos_shared
        |  |  |  |--tracer_driver
        |  |  |  |--vert_advection
        |  |  |--atmos_solo
        |  |  |--shared
        |  |     |--axis_utils
        |  |     |--constants
        |  |     |--diag_manager
        |  |     |--fft
        |  |     |--field_manager
        |  |     |--fms
        |  |     |--horiz_interp
        |  |     |--mpp
        |  |     |--platform
        |  |     |--sat_vapor_pres
        |  |     |--time_manager
        |  |     |--topography
        |  |     |--tracer_manager
        |  |     |--udunits
        |  |     |--utilities
        |  |--test
        |--cam-fv
        |  |--deprecated
        |  |--doc
        |  |--shell_scripts
        |     |--cesm1_5
        |     |--cesm2_0
        |--cam-old
        |  |--deprecated
        |  |--doc
        |  |--full_experiment
        |  |--perfect_model
        |--CESM
        |  |--doc
        |     |--CESM_DART_assim_modes
        |--cice
        |--clm
        |  |--datm
        |  |--docs
        |--cm1
        |--coamps
        |  |--doc
        |  |--externals
        |  |  |--obs_def
        |  |--templates
        |--coamps_nest
        |  |--doc
        |  |--externals
        |  |  |--obs_def
        |  |--shell_scripts
        |  |  |--COAMPS_RESTART_SCRIPTS
        |  |  |--TEMPLATES
        |  |--templates
        |  |  |--EXPERIMENT_EXAMPLE
        |--dynamo
        |  |--data
        |--ECHAM
        |--forced_barot
        |  |--obs
        |--forced_lorenz_96
        |--gitm
        |  |--GITM2
        |  |  |--src
        |  |--python
        |  |--testdata1
        |--ikeda
        |--LMDZ
        |--lorenz_04
        |--lorenz_63
        |--lorenz_84
        |--lorenz_96
        |  |--tests
        |--lorenz_96_2scale
        |--MITgcm_annulus
        |--MITgcm_ocean
        |  |--inputs
        |--model_mod_tools
        |--mpas_atm
        |  |--data
        |--mpas_ocn
        |  |--data
        |--NAAPS
        |--NCOMMAS
        |  |--docs
        |--noah
        |  |--ensemble_source
        |  |--forcing
        |  |--templates
        |--null_model
        |--PBL_1d
        |--pe2lyr
        |--POP
        |--ROMS
        |  |--data
        |  |--doc
        |--rose
        |--simple_advection
        |--sqg
        |--template
        |--tiegcm
        |--wrf
           |--experiments
           |  |--Radar
           |     |--IC
           |     |  |--sounding_perturbation
           |     |--obs
           |--namelist
           |--PERTURB
           |  |--3DVAR-COVAR
           |--regression
           |  |--CONUS-V2
           |  |--CONUS-V3
           |  |--Global-V3
           |  |--Radar
           |  |--WRF
           |--WRF_BC
           |--WRF_DART_utilities
         

--------------

.. _other_documentation:

Other documentation
-------------------

Additional documentation which didn't fit neatly into the other categories.

-  `Manhattan release notes <html/Manhattan_release.html>`__
-  `Brief summary of Manhattan differences from Lanai <html/Manhattan_diffs_from_Lanai.html>`__
-  `MPI intro <html/mpi_intro.html>`__
-  `Filter 'async' modes <html/filter_async_modes.html>`__
-  `mkmf </build_templates/mkmf.html>`__
-  `DART Tutorial <tutorial/index.html>`__
-  `DART_LAB <DART_LAB/DART_LAB.html>`__

--------------

.. _complete_list_of_all_documentation:

Complete list of all documentation
----------------------------------

The kitchen sink - quick links to all existing html docs plus all model_mod source files in the DART distribution tree:

-  `models/9var/model_mod.html </models/9var/model_mod.html>`__
-  `AIRS.html </observations/obs_converters/AIRS/AIRS.html>`__
-  `models/am2/model_mod.f90 </models/am2/model_mod.f90>`__
-  `convert_aura.f90 </observations/obs_converters/AURA/convert_aura.f90>`__
-  `AVISO.html </observations/obs_converters/AVISO/AVISO.html>`__
-  `level4_to_obs.html </observations/obs_converters/Ameriflux/level4_to_obs.html>`__
-  `models/CESM/doc/setup_guidelines.html </models/CESM/doc/setup_guidelines.html>`__
-  `CHAMP_density_text_to_obs.f90 </observations/obs_converters/CHAMP/CHAMP_density_text_to_obs.f90>`__
-  `CNOFS_text_to_obs.f90 </observations/obs_converters/CNOFS/CNOFS_text_to_obs.f90>`__
-  `models/coamps_nest/model_mod.f90 </models/coamps_nest/model_mod.f90>`__
-  `COSMOS_development.html </observations/obs_converters/COSMOS/COSMOS_development.html>`__
-  `COSMOS_to_obs.html </observations/obs_converters/COSMOS/COSMOS_to_obs.html>`__
-  `DART_LAB.html </docs/DART_LAB/DART_LAB.html>`__
-  `DEFAULT_obs_def_mod.html </observations/forward_operators/DEFAULT_obs_def_mod.html>`__
-  `DEFAULT_obs_kind_mod.html </assimilation_code/modules/observations/DEFAULT_obs_kind_mod.html>`__
-  `dwl_to_obs.html </observations/obs_converters/DWL/dwl_to_obs.html>`__
-  `even_sphere.m </observations/obs_converters/even_sphere/even_sphere.m>`__
-  `text_GITM/text_to_obs.f90 </observations/obs_converters/text_GITM/text_to_obs.f90>`__
-  `gsi_to_dart.f90 </observations/obs_converters/GSI2DART/gsi_to_dart.f90>`__
-  `GTSPP.html </observations/obs_converters/GTSPP/GTSPP.html>`__
-  `gnd_gps_vtec_text_to_obs.f90 </observations/obs_converters/gnd_gps_vtec/gnd_gps_vtec_text_to_obs.f90>`__
-  `Lanai_diffs_from_Kodiak.html </docs/html/Lanai_diffs_from_Kodiak.html>`__
-  `Lanai_release.html </docs/html/Lanai_release.html>`__
-  `models/lorenz_96_2scale/model_mod.f90 </models/lorenz_96_2scale/model_mod.f90>`__
-  `MADIS.html </observations/obs_converters/MADIS/MADIS.html>`__
-  `MIDAS/MIDAS_to_obs.html </observations/obs_converters/MIDAS/MIDAS_to_obs.html>`__
-  `models/MITgcm_annulus/model_mod.f90 </models/MITgcm_annulus/model_mod.f90>`__
-  `models/MITgcm_ocean/create_ocean_obs </models/MITgcm_ocean/create_ocean_obs.html>`__
-  `models/MITgcm_ocean/model_mod.html </models/MITgcm_ocean/model_mod.html>`__
-  `models/MITgcm_ocean/trans_pv_sv.html </models/MITgcm_ocean/trans_pv_sv.html>`__
-  `models/MITgcm_ocean/trans_sv_pv.html </models/MITgcm_ocean/trans_sv_pv.html>`__
-  `snow_to_obs.html </observations/obs_converters/snow/snow_to_obs.html>`__
-  `MODIS/MOD15A2_to_obs.html </observations/obs_converters/MODIS/MOD15A2_to_obs.html>`__
-  `MODIS/MODIS_README.html </observations/obs_converters/MODIS/MODIS_README.html>`__
-  `Manhattan_diffs_from_Lanai.html </docs/html/Manhattan_diffs_from_Lanai.html>`__
-  `Manhattan_getting_started.html </docs/html/Manhattan_getting_started.html>`__
-  `Manhattan_release.html </docs/html/Manhattan_release.html>`__
-  `NCEP prepbufr to source.html </observations/obs_converters/NCEP/prep_bufr/prep_bufr.html>`__
-  `NCEP/ascii_to_obs/create_real_obs.html </observations/obs_converters/NCEP/ascii_to_obs/create_real_obs.html>`__
-  `NCEP/prep_bufr/prep_bufr.html </observations/obs_converters/NCEP/prep_bufr/prep_bufr.html>`__
-  `models/NCOMMAS/dart_to_ncommas.html </models/NCOMMAS/dart_to_ncommas.html>`__
-  `models/NCOMMAS/model_mod.html </models/NCOMMAS/model_mod.html>`__
-  `models/NCOMMAS/ncommas_to_dart.html </models/NCOMMAS/ncommas_to_dart.html>`__
-  `models/POP/dart_pop_mod </models/POP/dart_pop_mod.html>`__
-  `models/POP/model_mod.html </models/POP/model_mod.html>`__
-  `models/POP/model_mod_check.html </models/POP/model_mod_check.html>`__
-  `PrecisionCheck.html </developer_tests/utilities/PrecisionCheck.html>`__
-  `ROMS.html </observations/obs_converters/ROMS/ROMS.html>`__
-  `models/ROMS/model_mod.html </models/ROMS/model_mod.html>`__
-  `models/rose/model_mod.f90 </models/rose/model_mod.f90>`__
-  `convert_saber_cdf.f90 </observations/obs_converters/SABER/convert_saber_cdf.f90>`__
-  `SSEC.html </observations/obs_converters/SSEC/SSEC.html>`__
-  `SSUSI/convert_f16_edr_dsk.html </observations/obs_converters/SSUSI/convert_f16_edr_dsk.html>`__
-  `models/tiegcm/model_mod.f90 </models/tiegcm/model_mod.f90>`__
-  `tpw.html </observations/obs_converters/tpw/tpw.html>`__
-  `tc_to_obs.html </observations/obs_converters/tropical_cyclone/tc_to_obs.html>`__
-  `DART Tutorial <tutorial/index.html>`__
-  `WOD.html </observations/obs_converters/WOD/WOD.html>`__
-  `adaptive_inflate_mod.html </assimilation_code/modules/assimilation/adaptive_inflate_mod.html>`__
-  `advance_time.html </assimilation_code/programs/advance_time/advance_time.html>`__
-  `assert_mod.f90 </assimilation_code/modules/utilities/assert_mod.f90>`__
-  `assim_model_mod.html </assimilation_code/modules/assimilation/assim_model_mod.html>`__
-  `assim_tools_mod.html </assimilation_code/modules/assimilation/assim_tools_mod.html>`__
-  `models/bgrid_solo/model_mod.html </models/bgrid_solo/model_mod.html>`__
-  `bitwise_considerations.html </docs/html/bitwise_considerations.html>`__
-  `boilerplate.html </docs/html/boilerplate/boilerplate.html>`__
-  `models/cam-fv/model_mod.html </models/cam-fv/model_mod.html>`__
-  `models/cam-old/cam_to_dart.html </models/cam-old/cam_to_dart.html>`__
-  `models/cam-old/dart_to_cam.html </models/cam-old/dart_to_cam.html>`__
-  `models/cam-old/model_mod </models/cam-old/model_mod.html>`__
-  `channel/location_mod.html </assimilation_code/location/channel/location_mod.html>`__
-  `cice_to_obs.html </observations/obs_converters/cice/cice_to_obs.html>`__
-  `models/cice/model_mod.f90 </models/cice/model_mod.f90>`__
-  `models/clm/model_mod.html </models/clm/model_mod.html>`__
-  `closest_member_tool.html </assimilation_code/programs/closest_member_tool/closest_member_tool.html>`__
-  `models/cm1/model_mod.html </models/cm1/model_mod.html>`__
-  `models/coamps/model_mod.html </models/coamps/model_mod.html>`__
-  `compare_states.html </assimilation_code/programs/compare_states/compare_states.html>`__
-  `compute_error.html </assimilation_code/programs/compute_error/compute_error.html>`__
-  `cov_cutoff_mod.html </assimilation_code/modules/assimilation/cov_cutoff_mod.html>`__
-  `cray_win_mod.f90 </assimilation_code/modules/utilities/cray_win_mod.f90>`__
-  `create_fixed_network_seq.html </assimilation_code/programs/create_fixed_network_seq/create_fixed_network_seq.html>`__
-  `create_obs_sequence.html </assimilation_code/programs/create_obs_sequence/create_obs_sequence.html>`__
-  `dart_time_io_mod.f90 </assimilation_code/modules/io/dart_time_io_mod.f90>`__
-  `direct_netcdf_mod.f90 </assimilation_code/modules/io/direct_netcdf_mod.f90>`__
-  `distributed_state.html </docs/html/distributed_state.html>`__
-  `distributed_state_mod.f90 </assimilation_code/modules/utilities/distributed_state_mod.f90>`__
-  `models/dynamo/model_mod.f90 </models/dynamo/model_mod.f90>`__
-  `ensemble_manager_mod.html </assimilation_code/modules/utilities/ensemble_manager_mod.html>`__
-  `adaptive_inflate_mod.f90 </assimilation_code/modules/assimilation/adaptive_inflate_mod.f90>`__
-  `fill_inflation_restart.html </assimilation_code/programs/fill_inflation_restart/fill_inflation_restart.html>`__
-  `filter.html </assimilation_code/programs/filter/filter.html>`__
-  `filter_async_modes.html </docs/html/filter_async_modes.html>`__
-  `filter_mod.html </assimilation_code/modules/assimilation/filter_mod.html>`__
-  `models/forced_barot/model_mod.f90 </models/forced_barot/model_mod.f90>`__
-  `models/forced_lorenz_96/model_mod.html </models/forced_lorenz_96/model_mod.html>`__
-  `forward_operator.html </docs/html/forward_operator.html>`__
-  `forward_operator_mod.f90 </assimilation_code/modules/observations/forward_operator_mod.f90>`__
-  `gen_sampling_err_table.html </assimilation_code/programs/gen_sampling_err_table/gen_sampling_err_table.html>`__
-  `generating_ensemble_ics.html </docs/html/generating_ensemble_ics.html>`__
-  `generating_obs_sequence.html </docs/html/generating_obs_sequence.html>`__
-  `models/gitm/dart_to_gitm.html </models/gitm/dart_to_gitm.html>`__
-  `models/gitm/gitm_to_dart.html </models/gitm/gitm_to_dart.html>`__
-  `models/gitm/model_mod.html </models/gitm/model_mod.html>`__
-  `gps.html </observations/obs_converters/gps/gps.html>`__
-  `history/Fiji_release.html </docs/html/history/Fiji_release.html>`__
-  `history/Guam_release.html </docs/html/history/Guam_release.html>`__
-  `history/I_diffs_from_workshop.html </docs/html/history/I_diffs_from_workshop.html>`__
-  `history/Iceland_release.html </docs/html/history/Iceland_release.html>`__
-  `history/Jamaica_diffs_from_I.html </docs/html/history/Jamaica_diffs_from_I.html>`__
-  `history/Jamaica_release.html </docs/html/history/Jamaica_release.html>`__
-  `history/Kodiak_release.html </docs/html/history/Kodiak_release.html>`__
-  `history/PostI_diffs_from_I.html </docs/html/history/PostI_diffs_from_I.html>`__
-  `history/Post_Iceland_release.html </docs/html/history/Post_Iceland_release.html>`__
-  `history/hawaii_release.html </docs/html/history/hawaii_release.html>`__
-  `history/pre_guam_release.html </docs/html/history/pre_guam_release.html>`__
-  `history/pre_hawaii_release.html </docs/html/history/pre_hawaii_release.html>`__
-  `history/pre_j_release.html </docs/html/history/pre_j_release.html>`__
-  `models/ikeda/model_mod.html </models/ikeda/model_mod.html>`__
-  `integrate_model.html </assimilation_code/programs/integrate_model/integrate_model.html>`__
-  `io_filenames_mod.f90 </assimilation_code/modules/io/io_filenames_mod.f90>`__
-  `location_mod.html </assimilation_code/location/location_mod.html>`__
-  `models/lorenz_04/model_mod.html </models/lorenz_04/model_mod.html>`__
-  `models/lorenz_63/model_mod.html </models/lorenz_63/model_mod.html>`__
-  `lorenz_63_example.html </docs/html/lorenz_63_example.html>`__
-  `models/lorenz_84/model_mod.html </models/lorenz_84/model_mod.html>`__
-  `models/lorenz_96/model_mod.html </models/lorenz_96/model_mod.html>`__
-  `mkmf.html </build_templates/mkmf.html>`__
-  `model_mod_check.html </assimilation_code/programs/model_mod_check/model_mod_check.html>`__
-  `models/mpas_atm/model_mod.html </models/mpas_atm/model_mod.html>`__
-  `models/mpas_atm/mpas_dart_obs_preprocess.html </models/mpas_atm/mpas_dart_obs_preprocess.html>`__
-  `models/mpas_ocn/model_mod.html </models/mpas_ocn/model_mod.html>`__
-  `models/mpas_ocn/model_to_dart.html </models/mpas_ocn/model_to_dart.html>`__
-  `mpi_intro.html </docs/html/mpi_intro.html>`__
-  `mpi_utilities_mod.html </assimilation_code/modules/utilities/mpi_utilities_mod.html>`__
-  `netcdf_inflation_files.html </docs/html/netcdf_inflation_files.html>`__
-  `models/noah/dart_to_noah.html </models/noah/dart_to_noah.html>`__
-  `models/noah/model_mod.html </models/noah/model_mod.html>`__
-  `models/noah/noah_to_dart.html </models/noah/noah_to_dart.html>`__
-  `models/null_model/model_mod.html </models/null_model/model_mod.html>`__
-  `obs_common_subset.html </assimilation_code/programs/obs_common_subset/obs_common_subset.html>`__
-  `obs_def_1d_state_mod.html </observations/forward_operators/obs_def_1d_state_mod.html>`__
-  `obs_def_AIRS_mod.f90 </observations/forward_operators/obs_def_AIRS_mod.f90>`__
-  `obs_def_AOD_mod.f90 </observations/forward_operators/obs_def_AOD_mod.f90>`__
-  `obs_def_AURA_mod.f90 </observations/forward_operators/obs_def_AURA_mod.f90>`__
-  `obs_def_COSMOS_mod.f90 </observations/forward_operators/obs_def_COSMOS_mod.f90>`__
-  `obs_def_CO_Nadir_mod.f90 </observations/forward_operators/obs_def_CO_Nadir_mod.f90>`__
-  `obs_def_GWD_mod.f90 </observations/forward_operators/obs_def_GWD_mod.f90>`__
-  `obs_def_QuikSCAT_mod.f90 </observations/forward_operators/obs_def_QuikSCAT_mod.f90>`__
-  `obs_def_SABER_mod.f90 </observations/forward_operators/obs_def_SABER_mod.f90>`__
-  `obs_def_TES_nadir_mod.f90 </observations/forward_operators/obs_def_TES_nadir_mod.f90>`__
-  `obs_def_altimeter_mod.f90 </observations/forward_operators/obs_def_altimeter_mod.f90>`__
-  `obs_def_cice_mod.f90 </observations/forward_operators/obs_def_cice_mod.f90>`__
-  `obs_def_cloud_mod.f90 </observations/forward_operators/obs_def_cloud_mod.f90>`__
-  `obs_def_cwp_mod.f90 </observations/forward_operators/obs_def_cwp_mod.f90>`__
-  `obs_def_dew_point_mod.html </observations/forward_operators/obs_def_dew_point_mod.html>`__
-  `obs_def_dwl_mod.f90 </observations/forward_operators/obs_def_dwl_mod.f90>`__
-  `obs_def_eval_mod.f90 </observations/forward_operators/obs_def_eval_mod.f90>`__
-  `obs_def_gps_mod.html </observations/forward_operators/obs_def_gps_mod.html>`__
-  `obs_def_gts_mod.f90 </observations/forward_operators/obs_def_gts_mod.f90>`__
-  `obs_def_metar_mod.f90 </observations/forward_operators/obs_def_metar_mod.f90>`__
-  `obs_def_mod.html </observations/forward_operators/obs_def_mod.html>`__
-  `obs_def_ocean_mod.html </observations/forward_operators/obs_def_ocean_mod.html>`__
-  `obs_def_pe2lyr_mod.f90 </observations/forward_operators/obs_def_pe2lyr_mod.f90>`__
-  `obs_def_radar_mod.html </observations/forward_operators/obs_def_radar_mod.html>`__
-  `obs_def_radiance_mod.f90 </observations/forward_operators/obs_def_radiance_mod.f90>`__
-  `obs_def_reanalysis_bufr_mod.f90 </observations/forward_operators/obs_def_reanalysis_bufr_mod.f90>`__
-  `obs_def_rel_humidity_mod.f90 </observations/forward_operators/obs_def_rel_humidity_mod.f90>`__
-  `obs_def_simple_advection_mod.f90 </observations/forward_operators/obs_def_simple_advection_mod.f90>`__
-  `obs_def_sqg_mod.f90 </observations/forward_operators/obs_def_sqg_mod.f90>`__
-  `obs_def_surface_mod.f90 </observations/forward_operators/obs_def_surface_mod.f90>`__
-  `obs_def_tower_mod.f90 </observations/forward_operators/obs_def_tower_mod.f90>`__
-  `obs_def_tpw_mod.f90 </observations/forward_operators/obs_def_tpw_mod.f90>`__
-  `obs_def_upper_atm_mod.f90 </observations/forward_operators/obs_def_upper_atm_mod.f90>`__
-  `obs_def_vortex_mod.f90 </observations/forward_operators/obs_def_vortex_mod.f90>`__
-  `obs_def_wind_speed_mod.f90 </observations/forward_operators/obs_def_wind_speed_mod.f90>`__
-  `obs_diag/oned/obs_diag.html </assimilation_code/programs/obs_diag/oned/obs_diag.html>`__
-  `obs_diag/threed_cartesian/obs_diag.html </assimilation_code/programs/obs_diag/threed_cartesian/obs_diag.html>`__
-  `obs_diag/threed_sphere/obs_diag.html </assimilation_code/programs/obs_diag/threed_sphere/obs_diag.html>`__
-  `obs_impact_mod.html </assimilation_code/modules/utilities/obs_impact_mod.f90>`__
-  `obs_impact_tool.html </assimilation_code/programs/obs_impact_tool/obs_impact_tool.html>`__
-  `obs_kind_mod.html </assimilation_code/modules/observations/obs_kind_mod.html>`__
-  `obs_model_mod.html </assimilation_code/modules/assimilation/obs_model_mod.html>`__
-  `obs_selection.html </assimilation_code/programs/obs_selection/obs_selection.html>`__
-  `obs_seq_coverage.html </assimilation_code/programs/obs_seq_coverage/obs_seq_coverage.html>`__
-  `obs_seq_to_netcdf.html </assimilation_code/programs/obs_seq_to_netcdf/obs_seq_to_netcdf.html>`__
-  `obs_seq_verify.html </assimilation_code/programs/obs_seq_verify/obs_seq_verify.html>`__
-  `obs_sequence_mod.html </assimilation_code/modules/observations/obs_sequence_mod.html>`__
-  `obs_sequence_tool.html </assimilation_code/programs/obs_sequence_tool/obs_sequence_tool.html>`__
-  `observations.html </observations/obs_converters/observations.html>`__
-  `ok_mesonet.html </observations/obs_converters/ok_mesonet/ok_mesonet.html>`__
-  `oned/location_mod.html </assimilation_code/location/oned/location_mod.html>`__
-  `parse_args_mod.f90 </assimilation_code/modules/utilities/parse_args_mod.f90>`__
-  `models/pe2lyr/model_mod.html </models/pe2lyr/model_mod.html>`__
-  `perfect_model_obs.html </assimilation_code/programs/perfect_model_obs/perfect_model_obs.html>`__
-  `preprocess.html </assimilation_code/programs/preprocess/preprocess.html>`__
-  `QuikSCAT.html </observations/obs_converters/quikscat/QuikSCAT.html>`__
-  `radar.html </observations/obs_converters/radar/radar.html>`__
-  `random_seq_mod.html </assimilation_code/modules/utilities/random_seq_mod.html>`__
-  `reg_factor_mod.html </assimilation_code/modules/assimilation/reg_factor_mod.html>`__
-  `restart_file_tool.html </assimilation_code/programs/restart_file_tool/restart_file_tool.html>`__
-  `running_lorenz_63.html </docs/html/running_lorenz_63.html>`__
-  `sampling_error_correction_mod.f90 </assimilation_code/modules/assimilation/sampling_error_correction_mod.f90>`__
-  `schedule_mod.html </assimilation_code/modules/utilities/schedule_mod.html>`__
-  `models/simple_advection/model_mod.html </models/simple_advection/model_mod.html>`__
-  `single_file_io_mod.f90 </assimilation_code/modules/io/single_file_io_mod.f90>`__
-  `smoother_mod.html </assimilation_code/modules/assimilation/smoother_mod.html>`__
-  `snow_to_obs.html </observations/obs_converters/snow/snow_to_obs.html>`__
-  `sort_mod.f90 </assimilation_code/modules/utilities/sort_mod.f90>`__
-  `text_to_obs.html </observations/obs_converters/text/text_to_obs.html>`__
-  `models/sqg/model_mod.html </models/sqg/model_mod.html>`__
-  `state_structure.html </docs/html/state_structure.html>`__
-  `state_structure_mod.f90 </assimilation_code/modules/io/state_structure_mod.f90>`__
-  `state_vector_io_mod.f90 </assimilation_code/modules/io/state_vector_io_mod.f90>`__
-  `system_simulation.html </assimilation_code/programs/system_simulation/system_simulation.html>`__
-  `models/template/model_mod.html </models/template/model_mod.html>`__
-  `template.html </docs/html/boilerplate/template.html>`__
-  `threed_cartesian/location_mod.html </assimilation_code/location/threed_cartesian/location_mod.html>`__
-  `threed_sphere/location_mod.html </assimilation_code/location/threed_sphere/location_mod.html>`__
-  `models/tiegcm/model_mod.html </models/tiegcm/model_mod.html>`__
-  `time_manager_mod.html </assimilation_code/modules/utilities/time_manager_mod.html>`__
-  `tpw.html </observations/obs_converters/tpw/tpw.html>`__
-  `tc_to_obs.html </observations/obs_converters/tropical_cyclone/tc_to_obs.html>`__
-  `tutorial/index.html </docs/tutorial/index.html>`__
-  `types_mod.html </assimilation_code/modules/utilities/types_mod.html>`__
-  `utilities_mod.html </assimilation_code/modules/utilities/utilities_mod.html>`__
-  `littler_tf_dart.html </observations/obs_converters/var/littler_tf_dart.html>`__
-  `rad_3dvar_to_dart.html </observations/obs_converters/var/rad_3dvar_to_dart.html>`__
-  `var.html </observations/obs_converters/var/var.html>`__
-  `vertical_conversion.html </docs/html/vertical_conversion.html>`__
-  `wakeup_filter.html </assimilation_code/programs/wakeup_filter/wakeup_filter.html>`__
-  `models/wrf/WRF_DART_utilities/dart_to_wrf.html </models/wrf/WRF_DART_utilities/dart_to_wrf.html>`__
-  `models/wrf/WRF_DART_utilities/replace_wrf_fields.html </models/wrf/WRF_DART_utilities/replace_wrf_fields.html>`__
-  `models/wrf/WRF_DART_utilities/wrf_dart_obs_preprocess.html </models/wrf/WRF_DART_utilities/wrf_dart_obs_preprocess.html>`__
-  `models/wrf/model_mod.html </models/wrf/model_mod.html>`__
-  `models/wrf/shell_scripts/advance_model.html </models/wrf/shell_scripts/advance_model.html>`__
-  `xyz_location_mod.html </assimilation_code/location/threed_cartesian/xyz_location_mod.f90>`__

--------------
