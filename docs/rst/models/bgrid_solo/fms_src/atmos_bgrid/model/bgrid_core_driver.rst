module bgrid_core_driver_mod

--------------

module bgrid_core_driver_mod
----------------------------

::

        Contact:   B. Wyman
        Reviewers:
        Change history: WebCVS Log for bgrid_core_driver.f90

--------------

OVERVIEW
^^^^^^^^

::


        Provides high-level interfaces to the B-grid dynamical core
        that allow easy initialization, integration, and diagnostics.

::

        There is a namelist interface for initializing the optional
        arguments to subroutine bgrid_core_init.

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


      bgrid_core_mod
      bgrid_horiz_mod
      bgrid_vert_mod
      bgrid_prog_var_mod
      bgrid_halo_mod
      bgrid_diagnostics_mod
      bgrid_integrals_mod
      bgrid_conserve_energy_mod
      time_manager_mod
      fms_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


      use bgrid_core_driver_mod [ ,only: bgrid_dynam_type, 
                                         bgrid_core_driver_init,
                                         bgrid_core_driver,
                                         bgrid_core_driver_end,
                                         bgrid_core_time_diff,
                                         get_bottom_data,
                                         put_bottom_data   ]

      bgrid_dynam_type
           A defined-type variable that contains constants needed
           by the B-grid dynamical core (see bgrid_core_mod)

      bgrid_core_driver_init
           Initializes the B-grid dynamical core.
           This interface returns values for the "bgrid_dynam_type" and
           prog_var_type" derived-type variables. Also internally
           initialized are other B-grid derived-type variables for
           the horizontal and vertical grid constants.

      bgrid_core_driver
           A wrapper for integrating the dynamical core one (atmospheric) time step.
           Note that only the tendencies of prognostic variables are updated.

      bgrid_core_time_diff
           Performs the time differencing of the prognostics variables 
           and outputs diagnostics for the B-grid dynamical core.

      bgrid_core_driver_end
           A wrapper for terminating the dynamical core.

      get_bottom_data, put_bottom_data
           Routines for getting and putting data at the model level
           closest to the ground.


      NOTES

         * A namelist interface called bgrid_core_driver_nml is read
           from file input.nml.

--------------

PUBLIC DATA
^^^^^^^^^^^

::


   type (bgrid_dynam_type)

        See bgrid_core_mod for details.

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::



   call bgrid_core_driver_init ( Time_init, Time, Time_step, 
                                  Var, Var_dt, Dynam, phys_axes )

   DESCRIPTION
      Returns initialized/allocated values for the "bgrid_dynam_type"
      and "prog_var_type" derived-type variables. Also internally
      initialized are other B-grid derived-type variables for the
      horizontal and vertical grid constants.

   INPUT
      Time_init  The initial (or base) time.  [time_type]

      Time       The current time.  [time_type]

      Time_step  The atmospheric model/physics time step.  [time_type]

   INPUT/OUTPUT
      Var        A derived-type variable that contains the prognostic
                 variables for the B-grid dynamical core.
                 The returned values will have been initialized
                 by prog_var_mod (most likely read from a restart file).
                    [type(prog_var_type)]

      Var_dt     A derived-type variable that contains the prognostic
                 variable time tendencies. The returned value is zero.
                    [type(prog_var_type)]

      Dynam      A derived-type variable that contains almost everything
                 needed by the dynamical core.
                    [type(bgrid_dynam_type)]

   OUTPUT
      phys_axes  Axis identifiers as returned by the diagnostics manager
                 and needed for subsequent calls to the diagnostics manager.
                    [integer, dimension(4)]
                 




   call bgrid_core_driver ( Time_diag, Var, Var_dt, Dynam, omega )

   DESCRIPTION
      Updates the prognostic variable tendencies with the dynamical
      core tendencies for the current atmospheric time step.
      Also calls diagnostics routines for outputting the dynamical
      core tendencies.

   INPUT
      Time_diag  The diagnostics time, usually the current time + time step.
                    [type(time_type)]

      Var        A derived-type variable that contains the B-grid's
                 prognostic variables.
                    [type(prog_var_type)]

   INPUT/OUTPUT
      Var_dt     A derived-type variable that contains the TENDENCIES
                 for the B-grid's prognostic variables.
                    [type(prog_var_type)]

      Dynam      The derived-type variable returned by a previous call
                 to bgrid_core_driver_init (see above).
                    [type(bgrid_dynam_type)]

   OUTPUT
      omega      The omega diagnostic (from the thermodynamic equation) in
                 pascals per second. The array should have horizontal dimensions that
                 are consistent with the data domain of the B-grid dynamical core.
                     [real, dimension(ilb:,jlb:,:)]





   call bgrid_core_time_diff ( omega, Time_diag, Dynam, Var, Var_dt )

   DESCRIPTION
        Performs the time differencing of the prognostics variables 
        and outputs diagnostics for the B-grid dynamical core.

   INPUT
      omega      The pressure vertical velocity in Pascals/second.
                 This is only needed for diagnostic purposes.
                    [real, dimension(:,:,:)]

      Time_diag  The diagnostics time, usually the current time + time step.
                    [type(time_type)]

      Dynam      The derived-type variable returned by a previous call
                 to bgrid_core_driver_init (see above).
                    [type(bgrid_dynam_type)]

   INPUT/OUTPUT
      Var        The prognostic variables. The input quantities are at the
                 current and on output they are at the next time step.
                    [type(prog_var_type)]

      Var_dt     The time tendencies for the prognostic variables.
                 The output tendencies will have been set to zero.
                    [type(prog_var_type)]





   call bgrid_core_driver_end (Dynam)

   DESCRIPTION
      Termination routine for the B-grid dynamical core.

   INPUT
      Dynam   The derived-type variable returned by a previous call
              to bgrid_core_driver_init (see above).
                 [type(bgrid_dynam_type)]





   call get_bottom_data ( a, b, a_bot, b_bot, [, k_bot] )

   DESCRIPTION
      Given a pair of 3-dimensional model fields this interface returns
      the 2-dimensional fields at the model level closest to the ground.
      If optional argument "kbot" is NOT present the returned field
      will be the 2-d field at k = size(a,3).

   INPUT
      a, b            Three-dimension fields on the model grid.
                      The last dimension varies from the top of the atmosphere
                      towards the surface.
                         [real, dimension(:,:,:)]

   OUTPUT
      a_bot, b_bot    Data located at the model level closest to the ground.
                      Must have the same size as the first two dimensions of a and b.
                         [real, dimension(:,:)]

   OPTIONAL INPUT
      k_bot           The vertical index for the model level closest to
                      the ground. Must have the same size as a_bot and b_bot.
                         [integer, dimension(:,:)]





   call put_bottom_data ( a_bot, b_bot, a, b [, k_bot] )

   DESCRIPTION
      Puts 2-dimensional data given at the lowest model level
      into their 3-dimensional model fields.

   INPUT
      a_bot, b_bot   Data located at the model level closest to the ground.
                     This data will be inserted into arrays a and b.
                        [real, dimension(:,:)]

   INPUT/OUTPUT
      a, b           Three-dimension fields on the model grid.
                        [real, dimension(:,:,:)]

   OPTIONAL INPUT
      k_bot          The vertical index for the model level closest to
                     the ground. Must have the same size as a_bot and b_bot.
                        [integer, dimension(:,:)]

--------------

NAMELIST
^^^^^^^^

::


    &bgrid_core_driver_nml

       damp_scheme          Determines how horizontal damping coefficients
                            vary with latitude.
                               = 1, constant
                               = 2, varies as inverse of diagonal grid distance
                               = 3, varies as inverse of x-axis grid distance
                            Note: damp_scheme = 1 is recommended, 
                            damp_scheme = 2,3 is experimental.
                                [integer, default: damp_scheme = 1]
      
       damp_order_wind      The horizontal damping order for momentum,
       damp_order_temp      temperature, and default order for all
       damp_order_tracer    prognostic tracers. The damping order must be
                            an even number; damp_order = 0 turns off damping.
                               [integer, default: damp_order = 4]

       damp_coeff_wind      The horizontal damping coefficients for
       damp_coeff_temp      momentum, temperature, and default value for
       damp_coeff_tracer    all prognostic tracers. The coefficients are
                            expressed as non-dimensional values for the
                            second-order diffusion operator (range = 0,1).
                               [real, default: damp_coeff = 0.50]
    
       slope_corr_wind      The topography slope correction applied to horizontal
       slope_corr_temp      damping of momentum and temperature (including all
                            prognostic tracers).  The coefficients (with range = 0,1)
                            are expressed as arrays of size 4.  The first 3 values are
                            coefficients for the lowest 3 model layers, the last value
                            represents the remaining uppermost layers.  A NON-ZERO
                            value turns the correction ON.  Typical values might be
                            (/ .25, .50, .75, .95 /).
                              [real, dimension(4), default: slope_corr = 0.,0.,0.,0.]

       advec_order_wind     The advection order for momentum, temperature,
       advec_order_temp     and default order for all prognostic tracers.
       advec_order_tracer   The advection order must be an even number.
                              [integer, default: advec_order = 2]

       advec_coeff_wind     Coefficients for modified Euler-backward advection
       advec_coeff_temp     scheme for momentum, temperature, and all
       advec_coeff_tracer   prognostic tracers.
                            NOTE: advec_coeff=0 is the Euler-forward scheme which
                            is unstable, advec_coeff=1 is the Euler-backward scheme
                            which is highly dissipative.
                              [real, default: advec_coeff = 0.7]

       num_fill_pass        The number of successive passes applied in the tracer
                            borrowing/filling scheme.  This conservative scheme is
                            used to fill negative tracer values. It is applied in
                            both the vertical and horizontal directions.
                            Each successive pass should remove more negative values,
                            however an optimum number of passes is probably between 1-3.
                            This is applied after advection to all prognostic tracers.
                              [integer, default: num_fill_pass = 1]

       grid_sep_coeff      Coefficient to suppress grid-separation problem 
                           associated with the B-grid. Currently, this option has been
                           disabled within the model, so that this coefficient does nothing.
                              [real, default: grid_sep_coeff = 0.00]

       filter_option       Determines how polar filtering is performed.
                           filter_option = 0,  NO filtering
                                         = 1,  not implemented
                                         = 2,  filter horiz OMG/DIV,
                                               advec mass tendencies,
                                               and momentum
                              [integer, default: filter_option = 2]

       filter_weight       Weight applied to the polar filter that will
                           increase (or decrease) the strength of the standard
                           polar filter response function.
                           SS(new) = SS(std)**filter_weight, 
                           where SS(std) is the Arakawa and Lamb response function.
                              [integer, default: filter_weight = 1 ]

       ref_lat_filter      The reference latitude at which polar filtering
                           (in each hemisphere) will begin to be applied.
                           Setting this argument >= 90. will turn off
                           polar filtering.
                             [real, default: ref_lat_filter = 60.]

       num_sponge_levels   Number of uppermost model level where a band-pass
                           filter is applied to damp undesirable waves.
                           Currently num_sponge_levels > 1 is not allowed.
                           If num_sponge_levels = 0, no damping is done.
                             [integer, default: num_sponge_levels = 0 ]

       sponge_coeff_wind     Damping coefficients for the sponge layer(s) in
       sponge_coeff_temp     the uppermost model levels. Coefficients have been 
       sponge_coeff_tracer   normalized and must be in the range [0,1].
                             If num_sponge_levels = 0, the value of the coefficients
                             is ignored.  There is no option to specify coefficients
                             that vary with level, although currently 
                             num_sponge_levels > 1 is not allowed.
                                [real, default: sponge_coeff = 0.]

       halo                The number of halo rows along all (NEWS) boundaries.
                           There is currently no namelist option that allows unequal
                           halo boundary.  NOTE: Additional halo rows are not 
                           necessary when using higher order horizontal damping or
                           advection, and may in fact result in poorer cpu performance.
                              [integer, default, halo = 1]

       num_adjust_dt       The number of adjustment time steps for each advection
                           time step, where num_adjust_dt >= 1. 
                             [integer, default: num_adjust_dt = 3]

       num_advec_dt        The number of advection/dynamics time steps for each
                           atmospheric/physics time step, where num_advec_dt >= 1.
                             [integer, default: num_advec_dt = 1]

       decomp              The domain decomposition, where decomp(1) = x-axis
                           decomposition, decomp(2) = y-axis decomposition.
                           * If decomp(1)*decomp(2) does not equal the number
                             of processors the model will fail.
                           * If decomp(1)=decomp(2)=0 then default rules apply.
                           * By default, one-dimensional decomposition (in Y) is used.
                             When there is fewer than 2 points per processor, then 2-D
                             decomposition is used.
                               [integer, dimension(2), default: decomp = 0,0]

       do_conserve_energy  If TRUE the temperature tendency will be updated to
                           guarantee that the dynamical core conserves total energy.
                           The correction is applied to a uniform global value.
                             [logical, default: do_conserve_energy=.false.]

       verbose             Flag that control additional printed output.
                           Currently, this option is not being used.
                             [integer, default: verbose = 0]

    NOTES

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

::


        None.

--------------

NOTES
^^^^^

::


        None.

--------------

FUTURE PLANS
^^^^^^^^^^^^

::


        None.

--------------
