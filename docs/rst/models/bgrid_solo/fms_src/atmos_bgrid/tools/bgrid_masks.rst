module bgrid_masks_mod

--------------

module bgrid_masks_mod
----------------------

::

        Contact:   Bruce Wyman
        Reviewers:
        Change history: WebCVS Log for bgrid_masks.f90

--------------

OVERVIEW
^^^^^^^^

::


        Provides a data structure for three-dimensional masks used
        to define the step-mountain/eta coordinate topography.

::

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


      bgrid_horiz_mod
      bgrid_vert_mod
      bgrid_halo_mod
      fms_mod
      mpp_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


      use bgrid_masks_mod [, only: grid_mask_type, mask_type,
                                   grid_masks_init ]

      grid_mask_type, mask_type
           Data structures that contain the 3d step-mountain topography masks
           and 2d indexing for the lowest model level.

      grid_masks_init
           Initializes data with the grid_mask_type.

--------------

DATA TYPES
^^^^^^^^^^

::

      type grid_mask_type
         type(mask_type) :: Tmp, Vel
         logical :: sigma
      end type grid_mask_type

      Tmp = grid masking values for the temperature/mass grid
      Vel = grid masking values for the velocity/momentum grid
      sigma = logical flag that specific whether vertical coordinate is
                the step-mountain (eta) or sigma coordinate

      type mask_type
         real,    pointer, dimension(:,:,:) :: mask 
         integer, pointer, dimension(:,:)   :: kbot 
         integer                            :: kbotmin 
      end type mask_type

      mask  = step-mountain topography mask (0.0 or 1.0) for
                mass (height) grid points
      kbot  = lowest model level above ground

      note:  for the sigma coordinate, mask = 1.0 everywhere, and
             kbot = number of vertical model levels

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

::



   Mask = grid_masks_init ( Hgrid, Vgrid, res )

   INPUT
      Vgrid     The derived-type variable returned by a previous call to vert_grid_init.
                   [type(vert_grid_type)]

      res       Reciporal of eta at the surface (i.e., the model interface that
                coincides with the step-mountain height). Note: for sigma
                coordinate model res=1. everywhere.
                   [real, dimension(:,:)]

   INPUT/OUTPUT
      Hgrid     The derived-type variable returned by a previous call to horiz_grid_init.
                   See the module horiz_grid_mod for details.
                   [type(horiz_grid_type)]

   RETURNS
      Mask      The derived-type variable containing grid masking arrays.
                   [type(grid_mask_type)]

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

::


    There are no error messages printed by this module.

--------------

KNOWN BUGS
^^^^^^^^^^

::


        None.

--------------

NOTES
^^^^^

::


      The interface grid_masks_init prints a message to STDOUT that
      describes the type of vertical coordinate that was initialized.

      If the eta coordinate is detected, a note of caution is printed.
      The eta coordinate is currently not supported.

      These messages are probably more appropiately printed from
      module bgrid_vert_mod (maybe in a future version).

--------------

FUTURE PLANS
^^^^^^^^^^^^

::


        None.

--------------
