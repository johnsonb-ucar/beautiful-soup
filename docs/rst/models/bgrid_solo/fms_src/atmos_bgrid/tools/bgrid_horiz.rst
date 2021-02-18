module bgrid_horiz_mod

--------------

module bgrid_horiz_mod
----------------------

::

        Contact:   B. Wyman
        Reviewers:
        Change history: WebCVS Log for bgrid_horiz.f90

--------------

OVERVIEW
^^^^^^^^

::


        Initializes horizontal grid constants needed by the B-grid dynamical core
        and determines the domain decomposition for running on distributed
        memory machines. This routine calls the FMS mpp_domains package.
        A derived-type variable (horiz_grid_type) is returned that contains
        the grid constants and domain data types.

::


   The B-Grid
   ----------

   The B-grid can be visualized as two overlapping grids, one that
   contains momentum (u and v) and the other mass fields (surface
   pressure, temperature, and tracers). These separate grids are
   rectangular in shape, defined by longitudes along the x-axis and
   latitude along the y-axis.  The grids are diagonally shifted from
   each other, such that, the center of a momentum grid box is located
   at the corners where four mass grid boxes intersect.
   Horizontal indexing increases from west to east, and from south to north.
   Indexing is set up so that a velocity point with the same i,j is
   located to the north and east of the mass (temperature) point.


          T(i-1,j+1)            T(i,j+1)          T(i+1,j+1)         

                     v(i-1,j  )          v(i,j  )

          T(i-1,j  )            T(i,j  )          T(i+1,j  )          

                     v(i-1,j-1)          v(i,j-1)

          T(i-1,j-1)            T(i,j-1)          T(i+1,j-1)     

   For computational purposes, extra rows and columns of grid boxes
   are carried on the perimeter of the horizontal grid. These extra
   points are called halo points. The number of halo points along
   the west/east boundaries and south/north boundaries are specified
   as separate arguments when initializing the horizontal grid. The
   default is for one halo row along all boundaries. Because of the
   grid staggering, the global momentum grid does not use it's
   northernmost row.

   The interior grid (excluding halo points) is called the compute domain.
   The global size of the longitude axis (first dimension) can have an
   even or odd number of points.  The latitude axis (2nd dimension) should
   always be an even number of points.  When there is an even number of
   global latitude points, mass points will straddle the equator,
   while velocity points lie along the equator.

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


        mpp_domains_mod
          constants_mod
                fms_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


        use bgrid_horiz_mod [ ,only: horiz_grid_type,
                                     bgrid_type,
                                     horiz_grid_init,
                                     get_horiz_grid_size,
                                     get_horiz_grid_bound,
                                     update_np,  update_sp,
                                     TGRID, VGRID    ]

        bgrid_type,  horiz_grid_type
             Derived-type variables containing horizontal grid constants needed
             by the B-grid dynamical core (see below).

        horiz_grid_init
             Function that initializes/returns a variable of
             type (horiz_grid_type).

        get_horiz_grid_size
             Subroutine that returns the number of grid boxes along the x and 
             y axes of the temperature grid or velocity grid.  There is an
             option for returning either the global or local compute grid sizes.
             Usually used in conjunction with routine get_horiz_grid_bound.

        get_horiz_grid_bound
             Subroutine that returns the longitude and latitude boundaries (edges)
             of temperature or velocity grid boxes. There is an option for
             returning either the global or local compute grid edges.
             Routine get_horiz_grid_size is usually called first to get
             the axis sizes.

        update_np,  update_sp
             Logical functions that determine if the northern (or southern)
             halo rows for the local processor lie within the global halo
             rows (ie.e, need a polar boundary update).

        TGRID, VGRID
             Integer parameters to be used as the "grid" argument with interfaces
             get_horiz_grid_size, get_horiz_grid_bound, update_np, and update_sp.

--------------

PUBLIC DATA
^^^^^^^^^^^

TYPE bgrid_type
^^^^^^^^^^^^^^^

::

       is, ie        first, last x-axis index in the compute domain [integer,scalar]
       js, je        first, last y-axis index in the compute domain [integer,scalar]
       isg, ieg      first, last x-axis index in the global  domain [integer,scalar]
       jsg, jeg      first, last y-axis index in the global  domain [integer,scalar]
       dx            local grid spacing for x-axis (in meters) [real,dimension(ilb:iub,jlb:jub)]
       rdx           reciprocal of dx (1/m) [real,dimension(ilb:iub,jlb:jub)]
       dy            local grid spacing for y-axis (in meters) [real,scalar]
       rdy           reciprocal of dy (1/m) [real,scalar]
       area          area of a local grid box (in m2) [real,dimension(ilb:iub,jlb:jub)]
       rarea         reciprocal of area (1/m2) [real,dimension(ilb:iub,jlb:jub)]
       tph, tlm      latitude, longitude at the center of a local grid box (in radians)
                           [real,dimension(ilb:iub,jlb:jub)]
       aph, alm      actual latitude, longitude at the center of a local grid box (in radians)
                           [real,dimension(ilb:iub,jlb:jub)]
       blatg         latitude boundaries of grid boxes along the global y-axis (in radians)
                           [real,dimension(jsg:jeg+1)]
       blong         longitude boundaries grid boxes along the global x-axis (in radians)
                           [real,dimension(isg:ieg+1)]
       Domain        domain2D derived-type variable with halosize ihalo,jhalo
                           [type(domain2d)]
       Domain_nohalo domain2D derived-type variable without halos, used for outputting diagnostic fields
                           [type(domain2d)]

TYPE horiz_grid_type
^^^^^^^^^^^^^^^^^^^^

::

       Tmp          grid constants for the temperature/tracer/mass grid [type(bgrid_type)]
       Vel          grid constants for the u/v wind component grid [type(bgrid_type)]
       sinphv       sine of Vel%aph [real,dimension(ilb:iub,jlb:jub)]
       tanphv       tangent of Vel%aph [real,dimension(ilb:iub,jlb:jub)]
       nlon         number of longitude (x-axis) grid points in the global grid (no halo points)
                         [integer,scalar]
       nlat         number of latitude (y-axis) grid points in the global grid (no halo points)
                         [integer,scalar]
       isize, jsize size of arrays on the local processor's grid (including halo points)
                        Note: isize=iub-ilb+1, jsize=jub-jlb+1
                         [integer,scalar]
       ilb, iub     lower, upper bounds of local x-axis indexing [integer,scalar]
       jlb, jub     lower, upper bounds of local y-axis indexing [integer,scalar]
       ihalo, jhalo number of halo points along the east and west boundaries (ihalo) or
                        south and north boundaries (jhalo) [integer,scalar]
       dlm          grid spacing for x-axis (in radians) [real,scalar]
       dph          grid spacing for y-axis (in radians) [real,scalar]
       dlmd         grid spacing for x-axis (in degrees of longitude) [real,scalar]
       dphd         grid spacing for y-axis (in degrees of latitude) [real,scalar]
       decompx      indicates if the x-axis has been decomposed across processors [logical,scalar]
       channel      indicates if the channel model feature has been implemented (NOT RECOMMENDED)
                         [logical,scalar]

::

   NOTES:

      The local indexing variables: is, ie, js, je, ilb, iub, jlb, jub,
      are consistent with the global index values (isg, ieg, jsg, jeg).

      All local arrays (on either the temperature or velocity grid) have the same
      horizontal size [dimension(ilb:iub,jlb:jub)]. Due to the grid staggering,
      the northernmost velocity domains do not use the last j-row (jub).

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::

   Hgrid = horiz_grid_init ( nlon, nlat 
                             [, ihalo, jhalo, decomp, channel, tph0d, tlm0d] )

   INPUT
      nlon, nlat     The number of global longitude, latitude grid points (respectively)
                     for the mass/temperature grid.
                        [integer,scalar]

   OPTIONAL INPUT
      ihalo, jhalo   The number of halo points for the x and y axis
                     (both mass and velocity grids).
                        [integer, default: ihalo=1, jhalo=1]

      decomp         The domain decomposition for the x and y axis, where
                     decomp(1) = x-axis decomposition, decomp(2) = y-axis
                     decomposition. If decomp(1)*decomp(2) does not equal
                     the number of processors the model will fail.
                     If either or both decomp(1), decomp(2) is zero,
                     the rules below apply.
                        [integer,dimension(2), default: decomp=0,0]

      channel        Flag for running in channel model mode.
                     This option has not been recently used and is currently not supported.
                        [logical, default: channel=FALSE]

      tph0d,tlm0d    Latitude/longitude for shifting the position of the poles.
                     Set both to zero for no transformation (the default).
                     This option has not been recently used and is currently
                     not supported.
                        [real, default: tph0d=0., tlm0d=0.]

   RETURNED VALUE
                     Derived-type variable that contains all necessary horizontal grid information
                     and domain decomposition variables needed by the model.
                        [type(horiz_grid_type)]

   NOTES

      1) If decomp(1)=0 and decomp(2)>0, then decomp(1)=decomp(2)/(# PEs), or vice versa.
         The final decomposition must always satisfy: decomp(1)*decomp(2)=number of processors.
      2) If decomp(1)=decomp(2)=0, then one-dimensional decomposition of
         the y-axis will be used. If there is fewer than two rows per PE, then
         two-dimensional decomposition will be automatically implemented.

--------------

::

   call get_horiz_grid_size ( Hgrid, grid, nlon, nlat [, global] )

   INPUT
      Hgrid       The derived-type variable returned by a previous call to horiz_grid_init.
                     [type(horiz_grid_type)]

      grid        Specifies which grid (temperature or velocity) the returned grid size
                     will be for. Use the publicly accessible parameters: TGRID or VGRID.
                     [integer,scalar]

   OUTPUT
      nlon, nlat  The number of grid points along the x- and y-axis, respectively.
                  The returned values will be for either the global grid size or
                  the local processor's grid size depending on the value of optional
                  argument "global".
                     [integer,scalar]

   OPTIONAL INPUT
      global      Flag that determines if the returned values are for the global
                  grid (global=.TRUE.) or the local compute grid (global=.FALSE.).
                     [logical,scalar, default: FALSE]

--------------

::

   call get_horiz_grid_bound ( Hgrid, grid, blon, blat [, global] )

   INPUT
      Hgrid    The derived-type variable returned by a previous call to horiz_grid_init.
                  [type(horiz_grid_type)]

      grid     Specifies which grid (temperature or velocity) the returned grid boundaries
               will be for. Use the publicly accessible parameters: TGRID or VGRID.
                  [integer,scalar]

   OUTPUT
      blon     Longitude edges of grid boxes for either the global grid or the
               local processor's grid depending on the value of optional argument "global".
                  [real,dimension(nlon+1)]

      blat     Latitude edges of grid boxes for either the global grid or the
               local processor's grid depending on the value of optional argument "global".
                  [real,dimension(nlat+1)]

   OPTIONAL INPUT
      global   Flag that determines if the returned values are for the global
               grid (global=.TRUE.) or the local compute grid (global=.FALSE.).
                  [logical,scalar, default: FALSE]

--------------

::

   answer = update_np ( Hgrid, grid )

   INPUT
      Hgrid    The derived-type variable returned by a previous call to horiz_grid_init.
                  [type(horiz_grid_type)]

      grid     Specifies which grid (temperature or velocity) the returned value
               will be for. Use the publicly accessible parameters: TGRID or VGRID.
                  [integer,scalar]

   RETURNED VALUE
      Returns TRUE when the halo rows along the north boundary lie within
      global halo rows, otherwise FALSE is returned. Note that for single
      processor runs the returned value will always be TRUE.
          [logical]

--------------

::

   answer = update_sp ( Hgrid, grid )

   INPUT
      Hgrid    The derived-type variable returned by a previous call to horiz_grid_init.
                  [type(horiz_grid_type)]

      grid     Specifies which grid (temperature or velocity) the returned value
                  will be for. Use the publicly accessible parameters: TGRID or VGRID.
                  [integer,scalar]

   RETURNED VALUE
      Returns TRUE when the halo rows along the south boundary lie within
      global halo rows, otherwise FALSE is returned. Note that for single
      processor runs the returned value will always be TRUE.
          [logical]

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

::


   FATAL errors in horiz_grid_init

       negative halo size
             The halo input arguments must be >= 1.

       number of processor requested not compatible with grid
             The domain decomposition either requested or computed was
               not compatible with the resolution of the grid.
               If you requested a decomposition other than the default,
               check to make sure it is correct.
               Also, the number of processor you are running on may not be
               compatible with the resolution of the model.
               Otherwise there may be a code error.

       j halo size too big for decomposition
             Either decrease the halo size or decrease the decomposition
               of the y-axis. The later can be done by increasing the decomposition
               of the x-axis or decreasing the number of processors.

   FATAL errors in get_horiz_grid_bound

       invalid argument dimension for blon
             The size of the blon output argument must equal the
               number of longitude grid boxes plus one.

       invalid argument dimension for blat
             The size of the blat output argument must equal the
               number of latitude grid boxes plus one.

   FATAL errors in get_horiz_grid_size, get_horiz_grid_bound,
                    update_sp, update_np

       invalid grid
             The input argument "grid" has an incorrect value.
               Make sure you are using one of public parameters, TGRID or VGRID.

--------------

REFERENCES
^^^^^^^^^^

::


        None.

--------------

KNOWN BUGS
^^^^^^^^^^

::


      * The grid transformation option (tph0d, tlm0d) has not been
        extensively tested. If want to use this option check with
        the developer.

      * The channel model mode has not been extensively tested.

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
