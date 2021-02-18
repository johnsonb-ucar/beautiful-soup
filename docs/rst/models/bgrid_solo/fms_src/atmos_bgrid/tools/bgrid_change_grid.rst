module bgrid_change_grid_mod

--------------

module bgrid_change_grid_mod
----------------------------

::

        Contact:   Bruce Wyman
        Reviewers:
        Change history: WebCVS Log for bgrid_change_grid.f90

--------------

OVERVIEW
^^^^^^^^

::


       Provides interfaces to interpolate between the B-grid mass and
       velocity grids.

::

       The interpolation to a grid box is performed using the (four) 
       grid boxes centered at it's corners.  The interfaces have been
       overloaded for area-weighted interpolation and simple
       equal-weighted (4-point) interpolation.

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


       bgrid_horiz_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


      use bgrid_change_grid_mod [,only:  mass_to_vel, vel_to_mass ]

      mass_to_vel
           Interpolates one field from the mass grid to the velocity grid.

      vel_to_mass
           Interpolates the velocity components from the velocity grid to
           the mass grid.

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::



   call mass_to_vel (Hgrid, fm, fv)
            OR
   call mass_to_vel        (fm, fv)

     INPUT

         Hgrid    horiz_grid_type (see horiz_grid_mod)
                  When this variable is present, area weighted averaging
                  is performed. When this variable is not present,
                  simple four-point averaging is performed.

         fm       2-d or 3-d real array located at mass points

     OUTPUT

         fv       2-d or 3-d real array located at velocity points


     NOTES

         1) No output value is calculated in the east-most and north-most rows.
         2) If the Hgrid interface is used, then the horizontal dimensions of
            the input/output arrays must be consistent with the size of the
            local data domain.
         3) The input and output arrays can be the same since a temporary array
            is used for the result.

   --------------------------------------------------------------------


   call vel_to_mass (Hgrid, u, v, um, vm, mask)
           OR
   call vel_to_mass        (u, v, um, vm, mask)

     INPUT

         Hgrid    horiz_grid_type (see horiz_grid_mod)
                  When this variable is present, area weighted averaging
                  is performed. When this variable is not present,
                  simple four-point averaging is performed.
      
         u, v     2-d or 3-d real arrays of velocity components array

     OUTPUT

         um, vm   2-d or 3-d real arrays averaged to mass points

     INPUT

         mask     2-d or 3-d topography mask array (real, 0. or 1.) located
                  at velocity points for the eta/step-mountain coordinate


     NOTES

         1) No output value is calculated in the west-most and south-most rows.
         2) If the Hgrid interface is used, then the horizontal dimensions of
            the input/output arrays must be consistent with the size of the
            local data domain.
         3) The input and output arrays can be the same since a temporary array
            is used for the result.

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


        The 2-d versions call the 3-d versions.

--------------

FUTURE PLANS
^^^^^^^^^^^^

::


        None.

--------------
