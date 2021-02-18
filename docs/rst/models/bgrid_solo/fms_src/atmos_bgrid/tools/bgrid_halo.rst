module bgrid_halo_mod

--------------

module bgrid_halo_mod
---------------------

::

        Contact:   B. Wyman
        Reviewers:
        Change history: WebCVS Log for bgrid_halo.f90

--------------

OVERVIEW
^^^^^^^^

::


        Provides an interface for updating the B-grid dynamical core
        halo rows and columns, including the polar halo rows.
        See the notes section for a description of the polar 
        boundary condition.

::

        Additional interfaces are provided for updating the halo rows
        of horiz_grid_type derived-type variables and for setting
        fluxes at the sub-polar to zero.

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


       horiz_grid_mod
        utilities_mod
      mpp_domains_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


      use bgrid_halo_mod [, only: update_halo,
                                  horiz_grid_boundary,
                                  vel_flux_boundary,
                                  TEMP, UWND, VWND,
                                  SOUTH, NORTH, WEST, EAST, NOPOLE, POLEONLY ]

      update_halo
           Updates all requested rows in the halo region for a requested
           field of type: TEMP, UWND, or VWND.  By default all boundaries
           will be updated.  To update only specific boundaries use the
           public parameters: SOUTH, NORTH, WEST, EAST, NOPOLE, and POLEONLY.

      horiz_grid_boundary
           Updates the halo region for variables of derived-type horiz_grid_type.
           Should be called after horiz_grid_init.

      vel_flux_boundary
           Zeros the sub-polar row of fields on the velocity grid.
           This routine is needed by several dynamics routines for conservation,
           but should not normally be needed by the user.

      TEMP, UWND, VWND
           Integer parameters to be used as the "field" argument in
           interface update_halo.  The VWND value will result in a sign flip
           beyond the polar rows.  Data at auxilary mass flux points can
           also use these values: U-flux points use TEMP and V-flux points use
           either UWND or VWND depending whether a sign flip is desired.

      SOUTH, NORTH, WEST, EAST, NOPOLE, POLEONLY
           Integer parameters to be used as the optional "flags" argument to
           interface update_halo. NOPOLE and POLEONLY apply only to fields
           UWND and VWND.

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::



   call update_halo ( Hgrid, field, data [,flags] )

   INPUT
      field     Specifies which field/grid the data is on.
                You must use the publicly accessible parameters: TEMP, UWND, or VWND.
                See the description of these parameters above.
                   [integer,scalar]

   INPUT/OUTPUT
      Hgrid     The derived-type variable returned by a previous call to horiz_grid_init.
                See the module horiz_grid_mod for details.
                   [type(horiz_grid_type)]

      data      Data array on any valid grid, may have 2, 3, or 4 dimensions.
                The dimensions correspond to the x, y and z axes, and tracer number.
                   [real,dimension(:,:) or dimension(:,:,:) or dimension(:,:,:,:)]

   OPTIONAL INPUT
      flags     Integer flag that describes which halo regions should be updated.
                By default all halo regions are updated. The value of flags 
                should be some combination of the public parameter values
                SOUTH, NORTH, WEST, EAST, and NOPOLE. For example, to only
                update the north and east halo regions set flags=NORTH+EAST.
                The flag for NOPOLE suppresses the halo update of velocity at the poles.

                An additional flag POLEONLY may be used independently to 
                update only the north and south polar halo rows without updating
                the interior halo rows. This kind of update will require no
                processor to processor communication.
                   [integer,scalar]

   ------------------------------------------------------------------------


   call horiz_grid_boundary ( Hgrid )

   INPUT/OUTPUT
      Hgrid     The derived-type variable returned by a previous call to horiz_grid_init.
                See the module horiz_grid_mod for details.
                   [type(horiz_grid_type)]

   ------------------------------------------------------------------------


   call vel_flux_boundary ( Hgrid, data )

   INPUT
      Hgrid     The derived-type variable returned by a previous call to horiz_grid_init.
                See the module horiz_grid_mod for details.
                   [type(horiz_grid_type)]
   INPUT/OUTPUT
      data      Real data array on velocity grid, may have 2 or 3 dimensions.
                The dimensions correspond to the x, y and z axes.
                The data in the sub-polar row will be set to zero.
                   [real,dimension(:,:) or dimension(:,:,:)]

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

::


   Fatal errors in update_halo

       i dimension has wrong size
           The 1st (i) dimension of input/output argument data must
             have a size equal to Hgrid % isize (the entire i dimension).

       j dimension has wrong size
           The 2nd (j) dimension of input/output argument data must
             have a size equal to Hgrid % jsize (the entire j dimension).

       invalid value for flags
           The value of optional argument flags was invalid.  This can only 
             happen when the user specifies a value.  The value of flags should
             be set using the public module parameters, and must be in the
             following range: 0 < flags <= SOUTH+NORTH+WEST+EAST+NOPOLE+POLEONLY.

       invalid field
           The input argument "field" has an incorrect value.  Make sure
             you are using one of public parameters: TEMP, UWND, or VWND.

--------------

KNOWN BUGS
^^^^^^^^^^

::


        None.

--------------

NOTES
^^^^^

::

      At the north-south polar boundaries the following 
      boundary conditions are applied:

         a) Velocities at the poles are equal to zero

                u(i,p) = 0
                v(i,p) = 0

         b) Halo points along the north and south polar boundaries
            are set as follows:

                T(i,p+1/2) =  T(i,p-1/2)
                u(i,p+1)   =  u(i,p-1)
                v(i,p+1)   = -v(i,p-1)
         
            where p + # is a halo row and p - # is a row within 
            the computational domain.

      If there is no decomposition along the x-axis then the east-west
      boundaries are updated for global cyclic continuity.

      All other halo points are updated using MPP_UPDATE_DOMAINS.

--------------

FUTURE PLANS
^^^^^^^^^^^^

::


        None.

--------------
