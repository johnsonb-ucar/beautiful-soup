module bgrid_prog_var_mod

--------------

module bgrid_prog_var_mod
-------------------------

::

        Contact:   B. Wyman
        Reviewers:
        Change history: WebCVS Log for bgrid_prog_var.f90

--------------

OVERVIEW
^^^^^^^^

::


        Initializes a derived-type variable that contains prognostic
        variables for the B-grid dynamical core.

::

        This modules defines and initializes a derived-type variable
        (prog_var_type) that contains the following prognostic fields:
          surface pressure, temperature, momentum, and tracers.

        The main initialization interface allocates storage for
        a prog_var_type variable. Additional interfaces allocate
        storage for separate fields. All array storage includes the
        halo region when the allocation is done.

        There are also operators and interfaces for performing some
        simple operations between prog_var_type variables.
         

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


      bgrid_horiz_mod
      bgrid_vert_mod
      bgrid_halo_mod
      bgrid_cold_start_mod
      fms_mod
      field_manager_mod
      tracer_manager_mod
    

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


      use bgrid_prog_var_mod [, only: prog_var_type, 
                                      prog_var_init,
                                      var_init,
                                      prog_var_times_scalar,
                                      prog_var_equals_scalar,
                                      prog_var_time_diff,
                                      open_prog_var_file,
                                      read_prog_var,
                                      write_prog_var   ]

      prog_var_type
           derived-type that contains horizontal and vertical
           grid sizes, and the prognostic variables for
           pressure, momentum, temperature, and tracers.
    
      prog_var_init
           initializes prog_var_type variable (all data arrays are set to zero)
    
      var_init
           initializes storage for real arrays (sets to zero)
    
      prog_var_times_scalar
           multiplies the prognostic variables within a prog_var_type
           variable by a constant real scalar
    
      prog_var_time_diff
           performs explicit time differencing
    
      prog_var_equals_scalar
           assigns a scalar to all prognostic variables in a prog_var_type
    
      open_prog_var_file
           opens the restart file for bgrid prognostic variables
    
      read_prog_var
           reads the restart file for bgrid prognostic variables
    
      write_prog_var
           reads the restart file for bgrid prognostic variables
    

--------------

PUBLIC DATA
^^^^^^^^^^^

::


   type prog_var_type

   --- integers (scalar) ---

        nlon = number of longitude points (first dimension)
               excludes halo points 
        nlat = number of latitude points (second dimension)
               excludes halo points
        nlev = number of vertical levels

        ntrace = number of tracers

        ilb = lower bound  (1st dimension) includes halo points
        iub = upper bound  (1st dimension) includes halo points
        jlb = lower bound  (2nd dimension) includes halo points
        jub = upper bound  (2nd dimension) includes halo points
        klb = lower bound  (3rd dimension)
        kub = upper bound  (3rd dimension)

   --- prognostic fields (real arrays) ---

        ps   = surface pressure
                 [real, dimension (ilb:iub, jlb:jub) ]
        pssl = surface pressure at eta=1 (sea level)
                 [real, dimension (ilb:iub, jlb:jub) ]

        u    = zonal wind component
                 [real, dimension (ilb:iub, jlb:jub, klb:kub) ]
        v    = meridional wind component
                 [real, dimension (ilb:iub, jlb:jub, klb:kub) ]
        t    = temperature
                 [real, dimension (ilb:iub, jlb:jub, klb:kub) ]
        r    = arbitrary number of tracers (includes specific humidity)
                 [real, dimension (ilb:iub, jlb:jub, klb:kub, 1:ntrace) ]

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::



   call prog_var_init ( Hgrid, nlev, ntrs, Vars )

     INPUT

        Hgrid   Derived-type variable containing horizontal grid constants.
                  [type(horiz_grid_type), see horiz_grid_mod]

        nlev    The number of full model levels for the prognostic variables.
                  [integer]

        ntrs    The total number of tracers.
                  [integer]

     INPUT/OUTPUT

        Vars    Derived-type variable containing the model's prognostic
                fields (see above).
                  [type(prog_var_type)]

   ---------------------------------------------------------------------


   The interface var_init can take several forms.

   var => var_init ( Hgrid )
   var => var_init ( Hgrid, kdim )
   var => var_init ( Hgrid, kdim, ntrace )

   var => var_init ( ilb, iub, jlb, jub )
   var => var_init ( ilb, iub, jlb, jub, kdim )
   var => var_init ( ilb, iub, jlb, jub, kdim, ntrace )

     INPUT

        Hgrid   Derived-type variable containing horizontal grid constants.
                  [type(horiz_grid_type), see horiz_grid_mod]

        ilb     Lower bound/index for first dimension.
                  [integer]

        iub     Upper bound/index for first dimension.
                  [integer]

        jlb     Lower bound/index for second dimension.
                  [integer]

        jub     Upper bound/index for second dimension.
                  [integer]

        kdim    The size of the third dimension (or level dimension).
                  [integer]

        ntrace  The size of the fourth dimension (or tracer dimension).
                  [integer]

     RETURNS

        The returned value is a pointer to memory.
        Fields that are initialized this way must be declared at pointers.

        Use the following syntax:

              real, pointer :: var(:,:) or var(:,:,:) or var(:,:,:,:)

   ---------------------------------------------------------------------


   call prog_var_times_scalar ( Var, scalar )

     INPUT/OUTPUT

        Var      prog_var_type which on output will have the
                 prognostic variable components (u,v,t,r,ps,pssl)
                 multiplied by scalar

     INPUT

        scalar   a real scalar quantity

   ---------------------------------------------------------------------


   call prog_var_equals_scalar ( Var, scalar )

     INPUT/OUTPUT

        Var      prog_var_type which on output will have the
                 prognostic variable components (u,v,t,r,ps,pssl)
                 multiplied by scalar

     INPUT

        scalar   a real scalar quantity

   ---------------------------------------------------------------------


   call prog_var_time_diff ( dt, Var_dt, Var, nt )

     INPUT

        dt      time step [real]

     INPUT/OUTPUT

        Var_dt  input value is the tendency for prognostic variables,
                the output value is zero [prog_var_type]

        Var     the prognostic variables, the input values are at time
                level n, and the output values are at time level n+1
                   [prog_var_type]

     OPTIONAL INPUT

        nt      number of tracers to be advanced in time, by default
                all tracers will be advanced from time n to n+1

   ---------------------------------------------------------------------


   call open_prog_var_file ( ix, jx, kx )

   OUTPUT

     ix, jx, kx   The 3-dimensional size of a prognostic field.
                    [integer]

   -------------------------------------------------------------


   call read_prog_var ( Hgrid, Var, eta, peta, fis, res )

   INPUT/OUTPUT
      Hgrid
      Var

   OUTPUT
      eta
      peta
      fis
      res

   -------------------------------------------------------------


   call write_prog_var ( Var, Hgrid, Vgrid, fis, res )

   INPUT
      Var
      Hgrid
      Vgrid
      fis
      res

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

::


        None.

--------------

KNOWN BUGS
^^^^^^^^^^

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


        Need routines to release allocated memory.
        These may be called prog_var_end and var_end.

--------------
