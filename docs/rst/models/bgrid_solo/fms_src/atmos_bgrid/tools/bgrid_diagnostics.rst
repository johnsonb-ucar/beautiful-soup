module bgrid_diagnostics_mod

--------------

module bgrid_diagnostics_mod
----------------------------

::

        Contact:   Bruce Wyman
        Reviewers:
        Change history: WebCVS Log for bgrid_diagnostics.f90

--------------

OVERVIEW
^^^^^^^^

::


        Handles the archiving of B-grid prognostic variables and
        several other related diagnostics fields to NetCDF files.

::

        This version provides an interface to the general model diagnostics
        manager (diag_manager) which provides support for NetCDF and 
        distributed memory systems.  This also allows dynamical variables
        to be saved with variables from other parts of the (atmospheric) model.

        In this version the user control of file names, output interval,
        time averaging, packing, and many other features is handled through
        the diagnostics manager's input file called diag_table.

        One of the functions of this module is to initialize the atmospheric
        model's diagnostic axes. The axis identification returned by this
        module is then used throughout the atmospheric model wherever
        diagnostic fields are saved (e.g., the physics).

        A second function of this module is to initialize and save 
        the dynamical core's prognostic fields and time tendencies of the
        prognostic fields.

        The fields saved are:

           variables:   bk  vertical coordinate sigma/eta values
                        pk  vertical coordinate pressure values (pascals)
                     zsurf  height of the surface (m)
                       res  reciprocal of eta at the surface
                        ps  surface pressure (pascals)
                   
                     ucomp  zonal wind component (m/sec)
                     vcomp  meridional wind component (m/sec)
                      temp  temperature (deg_k)
                     omega  omega vertical velocity (pascals/sec)
                   tracers  multiple number of tracers fields

                      wspd  wind speed (m/s)
                       div  divergence (1/s)
                       vor  relative vorticity (1/s)

                   udt_dyn  zonal wind tendency for dynamics (m/s2)
                   vdt_dyn  meridional wind tendency for dynamics (m/s2)
                   tdt_dyn  temperature tendency for dynamics (deg_k/sec)
           tracers"_dt_dyn" tracers tendencies for dynamics

        NOTES

        1)  The static variables bk, pk, zsurf, and res do not vary
            in time, they are written once and have no time axis.

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


      bgrid_horiz_mod
      bgrid_vert_mod
      bgrid_masks_mod
      bgrid_prog_var_mod
      bgrid_change_grid_mod
      diag_manager_mod
      time_manager_mod
      fms_mod
      constants_mod
      field_manager_mod
      tracer_manager_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


   use bgrid_diagnostics_mod [, only: bgrid_diagnostics_init,
                                    bgrid_diagnostics,
                                    bgrid_diagnostics_tend  ]

       bgrid_diagnostics_init
            Must be called to initialize the module.
            Also, axis identifiers (for the diag_manager) are returned.
            The static fields, zsurf and res are saved to the output file.
    
       bgrid_diagnostics
            Should be called at the end of every time step.
            Outputs the prognostics variables, omega, wind speed, divergence,
            and vorticity.  The time passed to bgrid_diagnostics will used to
            determine if the output fields should be written.
    
       bgrid_diagnostics_tend
            Should be called every time step immediately after dynamics..
            Outputs the tendencies of the prognostics variables due to the
            dynamics. 
    

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::



   call bgrid_diagnostics_init ( Time, Hgrid, Vgrid, Var, fis, res,
                                      mass_axes, vel_axes )

    INPUT

      Time        The current time. [time_type]

      Hgrid       Derived-type variable containing horizontal grid constants
                  for the B-grid dynamical core.  [horiz_grid_type]

      Vgrid       Derived-type variable containing vertical grid constants
                  for the B-grid dynamical core.    [vert_grid_type]

      Var         Derived-type variable containing the model's prognostics
                  variables.    [prog_var_type]

      fis         Surface geopotential height, a static field that is passed
                  to the diagnostics manager and saved to the NetCDF file as a 
                  static field (i.e., no time axis).
                      [real, dimension(Hgrid%ilb:,Hgrid%jlb:)]

      res         Reciprocal of eta at the surface, saved to the NetCDF file
                  as a static field (i.e., no time axis).
                      [real, dimension(Hgrid%ilb:,Hgrid%jlb:)]

    OUTPUT

      mass_axes   Integer identifiers for the mass axes (x,y,pfull,phalf).
                      [integer, dimension(4)]

      vel_axes    Integer identifiers for the velocity axes (x,y,pfull,phalf).
                  Note that the vertical axes (pfull,phalf) will be the same
                  as for the mass axes.  [integer, dimension(4)]

    NOTES

     1) Arguments fis and res must have dimensions consistent with the
        dynamical core (in Hgrid), the storage can be allocated using
        module prog_var_mod.

     2) Static fields fis and res are written to the output (NetCDF) file
        if requested by the diagnostics manager.

   ------------------------------------------------------------------


   call bgrid_diagnostics ( Hgrid, Vgrid, Var, Masks, Time, omega )

    INPUT

      Hgrid       Derived-type variable containing horizontal grid constants
                  for the B-grid dynamical core.  [horiz_grid_type]

      Vgrid       Derived-type variable containing vertical grid constants
                  for the B-grid dynamical core.    [vert_grid_type]

      Var         Derived-type variable containing the model's prognostics
                  variables.    [prog_var_type]

      Masks       Derived-type variable containing grid mask information.
                    [grid_mask_type]
                  
      Time        The current time. [time_type]

      omega       Omega diagnostic (in Pascals/sec).
                      [real, dimension(Hgrid%ilb:,Hgrid%jlb:,:)]

   ------------------------------------------------------------------


   call bgrid_diagnostics_tend ( Hgrid, Var_dt, Masks, Time )

    INPUT

      Hgrid       Derived-type variable containing horizontal grid constants
                  for the B-grid dynamical core.  [horiz_grid_type]

      Var_dt      Derived-type variable containing the tendencies of the
                  model's prognostics variables.    [prog_var_type]

      Masks       Derived-type variable containing grid mask information.
                    [grid_mask_type]

      Time        The current time. [time_type]

--------------

DIAGNOSTIC FIELDS
^^^^^^^^^^^^^^^^^

::

   Diagnostic fields may be output to a netcdf file by specifying the
   module name dynamics and the desired field names (given below)
   in file diag_table. See the documentation for diag_manager.

::


   Diagnostic fields for module name: dynamics

      field name   field description
      ----------   -----------------

       bk          vertical coordinate eta value
       pk          vertical coordinate pressure value (Pascals)
       zsurf       height of the surface (m)
       res         reciprocal of eta at the surface

       ps          surface pressure (Pascals)
       ucomp       zonal wind component (m/s)
       vcomp       meridional wind component (m/s)
       temp        temperature (deg_k)

       omega       omega vertical velocity (pascals/sec)
       wspd        wind speed (m/s)
       div         divergence (1/s)
       vor         relative vorticity (1/s)

       ucomp_sq    zonal wind component squared (m2/s2)
       vcomp_sq    meridional wind component squared (m2/s2)
       temp_sq     temperature squared (deg_K**2)
       omega_sq    omega vertical velocity squared (Pa**2/s**2)
       ucomp_vcomp zonal times meridional wind components (m2/s2)
       omega_temp  omega vertical velocity times temperature (Pascals*deg_K/sec)

       udt_dyn     zonal wind tendency for dynamics (m/s2)
       vdt_dyn     meridional wind tendency for dynamics (m/s2)
       tdt_dyn     temperature tendency for dynamics (deg_k/sec)

       trname         tracers concentrations
       trname_dt_dyn  tracers tendencies for dynamics

   Notes:

      1) bk, pk, zsurf, res are static variables

      2) In this version, div, vor are recomputed for diagnostic

      3) The names for tracer tendencies are determined from the tracer names.
         The short names will be appended with "_dt_dyn", the long names are
         modified to indicated a tendency for dynamics, and the units are
         appended with "/s".

      4) All available diagnostic tracer fields will be printed to the logfile.

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


      None.

--------------
