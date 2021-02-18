module atmosphere_mod

--------------

module atmosphere_mod
---------------------

::


        Contact:   Bruce Wyman
        Reviewers:
        Change history: WebCVS Log for solo/atmosphere.f90

--------------

OVERVIEW
^^^^^^^^

::


        Atmospheric driver for the dry B-grid dynamical core and Held-Suarez
        benchmark (aka simple_phyhsics).

::

        This module provides a standard interface to the B-grid dynamical
        core and B-grid interface to the simple physics.
        A similar interface for the spectral dynamical core exists that
        may be easily switched with this interface.

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


      bgrid_horiz_mod
      bgrid_vert_mod
      bgrid_prog_var_mod
      bgrid_halo_mod
      bgrid_grid_change_mod
      bgrid_core_driver_mod
      hs_forcing_mod
      time_manager_mod
      fms_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


     use atmosphere_mod [,only: atmosphere_init,       atmosphere_end,
                                atmosphere,
                                atmosphere_resolution, atmosphere_boundary,
                                get_atmosphere_axes  ]

     NOTES

        1)  Optional namelist interface &atmosphere_nml may be
            read from file input.nml.
                                   

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::


   call atmosphere_init ( Time_init, Time, Time_step )

   DESCRIPTION
      Initialization call for running the bgrid dynamical with the
      Held-Suarez GCM forcing.

   INPUT
      Time_init   The initial (or base) time.  [time_type]

      Time        The current time.  [time_type]

      Time_step   The atmospheric model/physics time step.  [time_type]




   call atmosphere_end

   DESCRIPTION
      Termination call for the bgrid dynamical with Held-Suarez
      GCM forcing.  There are no arguments to this routine.




   call atmosphere ( Time )

   DESCRIPTION
      Advances the B-grid prognostic variables one time step forward.
      The dynamical core, Held-Suarez forcing, diagnostics, and time
      differencing are all called.  This routine should only be called
      once per time step.

   INPUT
      Time    The current time.  [time_type]

   NOTE
      The prognostic variables are stored in a private derived-type 
      variabledefined in the header section of this module.

   ---------------------------------------------------------------------

   call get_atmosphere_axes ( axes )

   OUTPUT

      axes        axis identifiers for the atmospheric grids
                  The size of axes at least 1 but not greater than 4.
                  The axes returned are ordered (/ x, y, p_full, p_half /).
                    [integer, dimension(:)]




   call atmosphere_resolution ( nlon, nlat [, global] )

   DESCRIPTION
      Returns the resolution of compute domain for either the
      current processor or the global domain.

   OUTPUT
      nlon   The number of longitude points in the compute domain.
                [integer]

      nlat   The number of latitude points in the compute domain.
                [integer]

   OPTIONAL INPUT

      global  Flag that specifies whether the returned compute domain size is
              for the global grid (TRUE) or for the current processor (FALSE).
                 [logical, default: FALSE]
              



   call atmosphere_boundary ( blon, blat [, global] )

   DESCRIPTION
      Returns the grid box edges of compute domain for either the
      current processor or the global domain.

   OUTPUT
      blon    The west-to-east longitude edges of grid boxes (in radians).
                 [real, dimension(nlon+1)]

      blat    The south-to-north latitude edges of grid boxes (in radians).
                 [real, dimension(nlat+1)]

   OPTIONAL INPUT
      global  Flag that specifies whether the returned grid box edges are
              for the global grid (TRUE) or for the current processor (FALSE).
                 [logical, default: FALSE]
              
   NOTE
      The size of the output arguments, blon and blat, must be +1 more than the
      output arguments for call atmosphere_resolution, nlon+1 and nlat+1, respectively.

--------------

NAMELIST
^^^^^^^^

::


   &atmosphere_nml

    physics_window  The number of "i" and "j" rows processed each time
                    the modular physics is called. To process the entire
                    domain use physics_window = 0,0.
                       [integer, default: physics_window = 0,0]

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

::


   FATAL errors from get_atmosphere_axes in atmosphere_mod

       size of argument is incorrect
           The size of the argument to get_atmosphere_axes must be
           between 1 and 4.

--------------
