module bgrid_cold_start_mod

--------------

module bgrid_cold_start_mod
---------------------------

::

        Contact:   Bruce Wyman
        Reviewers:
        Change history: WebCVS Log for bgrid_cold_start.f90

--------------

OVERVIEW
^^^^^^^^

::


        Generates initial conditions for the B-grid dynamics core.

::

        Provides initial data (flow at rest) for all fields that
        are saved on the B-grid core restart file.

        The intended purpose of this module is to create initial data
        when running an idealized version of the model. However,
        there are options to generate (or read) realistic topography,
        but there is no way to generate a land-sea mask.

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


       bgrid_horiz_mod
        bgrid_halo_mod
        topography_mod
               fms_mod
         constants_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


      use bgrid_cold_start_mod [ ,only: cold_start_resol, cold_start ]

      cold_start_resol
           Returns the model resolution (read from namelist bgrid_cold_start_nml)
           to the calling program so that storage for the prognostic variables
           can be allocated.

      cold_start
           Generates initial data (flow at rest) for all fields saved on
           the B-grid dynamical core restart file.


      NOTES

         * A namelist interface called bgrid_cold_start_nml is read
           from file input.nml.

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::



   call cold_start_resol ( nx, ny, nz )

     OUTPUT

        nx     number of grid boxes along the longitude (x) axis

        ny     number of grid boxes along the latitude (y) axis

        nz     number of vertical model levels


     NOTES

        The values returned by this routine are from the namelist &bgrid_cold_start_nml.

   --------------------------------------------------------------------


   call cold_start ( Hgrid, eta, peta, fis, res, ps, pssl, u, v, t )

     INPUT/OUTPUT

        Hgrid   Horizontal grid constants (see horiz_grid_mod)

     OUTPUT

        eta     Values of sigma/eta at the interface between model levels.
                Must be dimensioned by the number of levels + 1.
                NOTE: This value corresponds to the "B" term when determining
                pressure (i.e., p = A + B*ps).
                   [real, dimension(:)]

        peta    Values of constant pressure at the interface between model levels.
                Must be dimensioned by the number of levels + 1.
                NOTE: This value corresponds to the "A" term when determining
                pressure (i.e., p = A + B*ps).
                   [real, dimension(:)]

        fis     geopotential height of the surface (m2/s2)
                   [real, dimension(:,:)]

        res     reciprocal of eta at the surface
                   [real, dimension(:,:)]

        ps      surface pressure (pascals)
                   [real, dimension(:,:)]

        pssl    surface pressure at eta=1. (pascals)
                   [real, dimension(:,:)]

        u       zonal wind component (m/s)
                   [real, dimension(:,:,:)]

        v       meridional wind component (m/s)
                   [real, dimension(:,:,:)]

        t       temperature (deg K)
                   [real, dimension(:,:,:)]

     NOTES

        The storage for all arguments must be allocated by the calling program.

--------------

NAMELIST
^^^^^^^^

::


    &bgrid_cold_start_nml

      nlon   = number of grid points along the longitude axis (1st dimension)
                 [integer, default: nlon = 0]

      nlat   = number of grid points along the latitude axis (2nd dimension)
                 [integer, default: nlat = 0]

      nlev   = number of vertical levels
                 [integer, default: nlev = 0]

      pref   = initial surface pressure in pascals
                 [real, default: pref = 1000.e2]

      tref   = initial temperature in deg kelvin
                 [real, default: tref = 255.]

      equal_vert_spacing  = Should the levels be equally spaced in sigma or
                            spaced using the formula of Smagorinski (1969).
                              [logical, default: equal_vert_spacing = .true.]

    NOTES

      1) If nlon, nlat, or nlev are not specified the program will terminate.
      2) There is no option for the hybrid or eta coordinate. 
         All vertical coordinates use the pure sigma system.

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

::


   FATAL errors in bgrid_cold_start_mod

       resolution not specified
           One of two possible problems may have occurred.
           1) Must specify values for namelist variables: nlon, nlat, nlev.
           2) If you expected to read a restart file, the restart was probably
              not found and the model has inadvertently tried to generate one.

       incorrect resolution in file topography.res
           The resolution read from the topography file does not agree with
           the resolution given by the namelist.

--------------

NOTES
^^^^^

::


     Initial data (momentum,temperature,surface pressure) are computed as:

            u  = 0.0
            v  = 0.0
            t  = tref
            ps = pref * exp( -fis / (tref * Rd) )

     where

         fis = geopotential height at surface (m2/s2)
         Rd  = dry gas constant
         tref, pref = namelist parameters

--------------

FUTURE PLANS
^^^^^^^^^^^^

::


      Coordinate development of this module with the "off-line" program
      for generating spin-up initial conditions.

--------------
