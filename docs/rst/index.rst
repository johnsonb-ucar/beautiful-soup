.. DART Documentation documentation master file, created by
   sphinx-quickstart on Fri Nov 20 11:01:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the DART documentation
=================================

.. toctree::
   :maxdepth: 1
   :caption: Tutorial

   /docs/rst/docs/tutorial/index
   /docs/rst/docs/DART_LAB/DART_LAB

.. toctree::
   :maxdepth: 1
   :caption: Background

   /docs/rst/docs/html/bitwise_considerations
   /docs/rst/docs/html/mpi_intro
   /docs/rst/docs/html/netcdf_inflation_files
   /docs/rst/docs/html/state_structure

.. toctree::
   :maxdepth: 1
   :caption: Build Templates
   
   /docs/rst/build_templates/mkmf

.. toctree::
   :maxdepth: 1
   :caption: Latest Release

   /docs/rst/docs/html/Manhattan_release

.. toctree::
   :maxdepth: 1
   :caption: Prior Releases

   /docs/rst/docs/html/Lanai_release
   /docs/rst/docs/html/history/Kodiak_release
   /docs/rst/docs/html/history/Jamaica_release
   /docs/rst/docs/html/history/Iceland_release
   /docs/rst/docs/html/history/hawaii_release
   /docs/rst/docs/html/history/Guam_release
   /docs/rst/docs/html/history/Fiji_release

.. toctree::
   :maxdepth: 1
   :caption: Models

   /docs/rst/models/LMDZ/README
   /docs/rst/models/ECHAM/README
   /docs/rst/models/null_model/README
   /docs/rst/models/coamps_nest/README
   /docs/rst/models/POP/README
   /docs/rst/models/pe2lyr/model_mod
   /docs/rst/models/lorenz_63/README
   /docs/rst/models/9var/README
   /docs/rst/models/gitm/README
   /docs/rst/models/simple_advection/README
   /docs/rst/models/lorenz_96/README
   /docs/rst/models/ikeda/model_mod
   /docs/rst/models/coamps/model_mod
   /docs/rst/models/PBL_1d/README
   /docs/rst/models/ROMS/README
   /docs/rst/models/lorenz_84/README
   /docs/rst/models/mpas_ocn/model_mod
   /docs/rst/models/template/model_mod
   /docs/rst/models/cam-fv/README
   /docs/rst/models/sqg/model_mod
   /docs/rst/models/rose/README
   /docs/rst/models/mpas_atm/README
   /docs/rst/models/forced_lorenz_96/README
   /docs/rst/models/wrf/README
   /docs/rst/models/cam-old/README
   /docs/rst/models/cice/README
   /docs/rst/models/am2/README
   /docs/rst/models/cm1/README
   /docs/rst/models/lorenz_04/README
   /docs/rst/models/CESM/README
   /docs/rst/models/bgrid_solo/README
   /docs/rst/models/noah/README
   /docs/rst/models/FESOM/README
   /docs/rst/models/NCOMMAS/model_mod
   /docs/rst/models/wrf_hydro/README
   /docs/rst/models/tiegcm/model_mod
   /docs/rst/models/lorenz_96_2scale/README
   /docs/rst/models/MITgcm_ocean/model_mod
   /docs/rst/models/clm/model_mod

.. toctree::
   :maxdepth: 1
   :caption: Assimilation Code

   /docs/rst/assimilation_code/location/channel/location_mod
   /docs/rst/assimilation_code/location/location_mod
   /docs/rst/assimilation_code/location/oned/location_mod
   /docs/rst/assimilation_code/location/threed_cartesian/location_mod
   /docs/rst/assimilation_code/location/threed_sphere/location_mod
   /docs/rst/assimilation_code/programs/obs_seq_verify/obs_seq_verify
   /docs/rst/assimilation_code/programs/wakeup_filter/wakeup_filter
   /docs/rst/assimilation_code/programs/compare_states/compare_states
   /docs/rst/assimilation_code/programs/gen_sampling_err_table/gen_sampling_err_table
   /docs/rst/assimilation_code/programs/perturb_single_instance/perturb_single_instance
   /docs/rst/assimilation_code/programs/system_simulation/system_simulation
   /docs/rst/assimilation_code/programs/compute_error/compute_error
   /docs/rst/assimilation_code/programs/preprocess/preprocess
   /docs/rst/assimilation_code/programs/obs_impact_tool/obs_impact_tool
   /docs/rst/assimilation_code/programs/create_fixed_network_seq/create_fixed_network_seq
   /docs/rst/assimilation_code/programs/obs_loop/obs_loop
   /docs/rst/assimilation_code/programs/perfect_model_obs/perfect_model_obs
   /docs/rst/assimilation_code/programs/obs_selection/obs_selection
   /docs/rst/assimilation_code/programs/obs_sequence_tool/obs_sequence_tool
   /docs/rst/assimilation_code/programs/integrate_model/integrate_model
   /docs/rst/assimilation_code/programs/obs_diag/oned/obs_diag
   /docs/rst/assimilation_code/programs/obs_diag/threed_cartesian/obs_diag
   /docs/rst/assimilation_code/programs/obs_diag/threed_sphere/obs_diag
   /docs/rst/assimilation_code/programs/fill_inflation_restart/fill_inflation_restart
   /docs/rst/assimilation_code/programs/obs_seq_coverage/obs_seq_coverage
   /docs/rst/assimilation_code/programs/advance_time/advance_time
   /docs/rst/assimilation_code/programs/model_mod_check/model_mod_check
   /docs/rst/assimilation_code/programs/closest_member_tool/closest_member_tool
   /docs/rst/assimilation_code/programs/restart_file_tool/restart_file_tool
   /docs/rst/assimilation_code/programs/filter/filter
   /docs/rst/assimilation_code/programs/obs_keep_a_few/obs_keep_a_few
   /docs/rst/assimilation_code/programs/create_obs_sequence/create_obs_sequence
   /docs/rst/assimilation_code/programs/obs_seq_to_netcdf/obs_seq_to_netcdf
   /docs/rst/assimilation_code/programs/obs_common_subset/obs_common_subset
   /docs/rst/assimilation_code/modules/utilities/ensemble_manager_mod
   /docs/rst/assimilation_code/modules/utilities/random_seq_mod
   /docs/rst/assimilation_code/modules/utilities/mpi_utilities_mod
   /docs/rst/assimilation_code/modules/utilities/time_manager_mod
   /docs/rst/assimilation_code/modules/utilities/utilities_mod
   /docs/rst/assimilation_code/modules/utilities/types_mod
   /docs/rst/assimilation_code/modules/utilities/schedule_mod
   /docs/rst/assimilation_code/modules/observations/obs_kind_mod
   /docs/rst/assimilation_code/modules/observations/DEFAULT_obs_kind_mod
   /docs/rst/assimilation_code/modules/observations/obs_sequence_mod
   /docs/rst/assimilation_code/modules/assimilation/smoother_mod
   /docs/rst/assimilation_code/modules/assimilation/assim_tools_mod
   /docs/rst/assimilation_code/modules/assimilation/cov_cutoff_mod
   /docs/rst/assimilation_code/modules/assimilation/reg_factor_mod
   /docs/rst/assimilation_code/modules/assimilation/adaptive_inflate_mod
   /docs/rst/assimilation_code/modules/assimilation/obs_model_mod
   /docs/rst/assimilation_code/modules/assimilation/quality_control_mod
   /docs/rst/assimilation_code/modules/assimilation/filter_mod
   /docs/rst/assimilation_code/modules/assimilation/assim_model_mod

.. toctree::
   :maxdepth: 1
   :caption: To organize later with toctree directives

   /docs/rst/docs/html/Lanai_diffs_from_Kodiak
   /docs/rst/docs/html/filter_async_modes
   /docs/rst/docs/html/distributed_state
   /docs/rst/docs/html/Manhattan_getting_started
   /docs/rst/docs/html/rma
   /docs/rst/docs/html/Manhattan_diffs_from_Lanai
   /docs/rst/docs/html/forward_operator
   /docs/rst/docs/html/boilerplate/boilerplate
   /docs/rst/docs/html/boilerplate/template
   /docs/rst/docs/html/vertical_conversion
   /docs/rst/docs/html/history/pre_j_release
   /docs/rst/docs/html/history/PostI_diffs_from_I
   /docs/rst/docs/html/history/Jamaica_diffs_from_I
   /docs/rst/docs/html/history/I_diffs_from_workshop
   /docs/rst/docs/html/history/pre_hawaii_release
   /docs/rst/docs/html/history/pre_guam_release
   /docs/rst/docs/html/history/Post_Iceland_release
   /docs/rst/models/POP/dart_pop_mod
   /docs/rst/models/gitm/netcdf_to_gitm_blocks
   /docs/rst/models/gitm/gitm_blocks_to_netcdf
   /docs/rst/models/mpas_ocn/model_to_dart
   /docs/rst/models/mpas_atm/mpas_dart_obs_preprocess
   /docs/rst/models/wrf/WRF_DART_utilities/replace_wrf_fields
   /docs/rst/models/wrf/WRF_DART_utilities/wrf_dart_obs_preprocess
   /docs/rst/models/utilities/default_model_mod
   /docs/rst/models/cam-old/cam_to_dart
   /docs/rst/models/cam-old/dart_to_cam
   /docs/rst/models/CESM/doc/setup_guidelines
   /docs/rst/models/bgrid_solo/fms_src/atmos_shared/tracer_driver/atmos_radon
   /docs/rst/models/bgrid_solo/fms_src/atmos_shared/tracer_driver/atmos_sulfur_hex
   /docs/rst/models/bgrid_solo/fms_src/atmos_shared/tracer_driver/atmos_tracer_driver
   /docs/rst/models/bgrid_solo/fms_src/atmos_shared/tracer_driver/atmos_carbon_aerosol
   /docs/rst/models/bgrid_solo/fms_src/atmos_shared/tracer_driver/atmos_tracer_utilities
   /docs/rst/models/bgrid_solo/fms_src/atmos_shared/vert_advection/vert_advection
   /docs/rst/models/bgrid_solo/fms_src/shared/time_manager/time_manager
   /docs/rst/models/bgrid_solo/fms_src/shared/field_manager/field_manager
   /docs/rst/models/bgrid_solo/fms_src/shared/horiz_interp/horiz_interp
   /docs/rst/models/bgrid_solo/fms_src/shared/fms/fms
   /docs/rst/models/bgrid_solo/fms_src/shared/constants/constants
   /docs/rst/models/bgrid_solo/fms_src/shared/platform/platform
   /docs/rst/models/bgrid_solo/fms_src/shared/utilities/utilities
   /docs/rst/models/bgrid_solo/fms_src/shared/tracer_manager/tracer_manager
   /docs/rst/models/bgrid_solo/fms_src/shared/mpp/mpp_domains
   /docs/rst/models/bgrid_solo/fms_src/shared/mpp/mpp_io
   /docs/rst/models/bgrid_solo/fms_src/shared/mpp/mpp
   /docs/rst/models/bgrid_solo/fms_src/shared/fft/fft
   /docs/rst/models/bgrid_solo/fms_src/shared/sat_vapor_pres/sat_vapor_pres
   /docs/rst/models/bgrid_solo/fms_src/shared/topography/topography
   /docs/rst/models/bgrid_solo/fms_src/shared/topography/gaussian_topog
   /docs/rst/models/bgrid_solo/fms_src/shared/diag_manager/diag_manager
   /docs/rst/models/bgrid_solo/fms_src/shared/diag_manager/diag_table_tk
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_polar_filter
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_halo
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_horiz
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_cold_start
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_prog_var
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_diagnostics
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_integrals
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_change_grid
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_masks
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/tools/bgrid_vert
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/driver/solo/atmosphere
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/model/bgrid_core
   /docs/rst/models/bgrid_solo/fms_src/atmos_bgrid/model/bgrid_core_driver
   /docs/rst/models/bgrid_solo/fms_src/atmos_param/hs_forcing/hs_forcing
   /docs/rst/models/bgrid_solo/fms_src/atmos_solo/atmos_model
   /docs/rst/models/NCOMMAS/dart_to_ncommas
   /docs/rst/models/NCOMMAS/ncommas_to_dart
   /docs/rst/models/MITgcm_ocean/trans_pv_sv
   /docs/rst/models/MITgcm_ocean/trans_sv_pv
   /docs/rst/models/MITgcm_ocean/create_ocean_obs

.. toctree::
   :maxdepth: 1
   :caption: Developer Tests

   /docs/rst/developer_tests/location/location_mod
   /docs/rst/developer_tests/forward_operators/README
   /docs/rst/developer_tests/utilities/PrecisionCheck

.. toctree::
   :maxdepth: 1
   :caption: Observations

   /docs/rst/observations/forward_operators/obs_def_gps_mod
   /docs/rst/observations/forward_operators/obs_def_dew_point_mod
   /docs/rst/observations/forward_operators/obs_def_ocean_mod
   /docs/rst/observations/forward_operators/obs_def_1d_state_mod
   /docs/rst/observations/forward_operators/obs_def_radar_mod
   /docs/rst/observations/forward_operators/DEFAULT_obs_def_mod
   /docs/rst/observations/forward_operators/obs_def_mod
   /docs/rst/observations/forward_operators/obs_def_rttov_mod
   /docs/rst/observations/obs_converters/SSEC/SSEC
   /docs/rst/observations/obs_converters/GTSPP/GTSPP
   /docs/rst/observations/obs_converters/gps/gps
   /docs/rst/observations/obs_converters/GSI2DART/README
   /docs/rst/observations/obs_converters/WOD/WOD
   /docs/rst/observations/obs_converters/tpw/tpw
   /docs/rst/observations/obs_converters/ROMS/ROMS
   /docs/rst/observations/obs_converters/COSMOS/COSMOS_to_obs
   /docs/rst/observations/obs_converters/COSMOS/COSMOS_development
   /docs/rst/observations/obs_converters/var/littler_tf_dart
   /docs/rst/observations/obs_converters/var/rad_3dvar_to_dart
   /docs/rst/observations/obs_converters/var/var
   /docs/rst/observations/obs_converters/tropical_cyclone/tc_to_obs
   /docs/rst/observations/obs_converters/Ameriflux/level4_to_obs
   /docs/rst/observations/obs_converters/cice/cice_to_obs
   /docs/rst/observations/obs_converters/DWL/dwl_to_obs
   /docs/rst/observations/obs_converters/MIDAS/MIDAS_to_obs
   /docs/rst/observations/obs_converters/SST/SST
   /docs/rst/observations/obs_converters/MODIS/MOD15A2_to_obs
   /docs/rst/observations/obs_converters/MODIS/MODIS_README
   /docs/rst/observations/obs_converters/NCEP/prep_bufr/prep_bufr
   /docs/rst/observations/obs_converters/NCEP/ascii_to_obs/create_real_obs
   /docs/rst/observations/obs_converters/SSUSI/convert_f16_edr_dsk
   /docs/rst/observations/obs_converters/ok_mesonet/ok_mesonet
   /docs/rst/observations/obs_converters/snow/snow_to_obs
   /docs/rst/observations/obs_converters/text/text_to_obs
   /docs/rst/observations/obs_converters/radar/radar
   /docs/rst/observations/obs_converters/MADIS/MADIS
   /docs/rst/observations/obs_converters/quikscat/QuikSCAT
   /docs/rst/observations/obs_converters/AIRS/AIRS
   /docs/rst/observations/obs_converters/AVISO/AVISO
   