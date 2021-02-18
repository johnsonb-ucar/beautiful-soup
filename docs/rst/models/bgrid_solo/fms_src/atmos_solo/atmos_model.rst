program atmos_model

--------------

program atmos_model
-------------------

::

        Contact:   B. Wyman
        Reviewers:
        Change history: WebCVS Log for solo/atmos_model.f90

--------------

OVERVIEW
^^^^^^^^

::


        A main program for running a stand-alone atmospheric model.

::

        This version is suitable for running a dry dynamical core (Held-Suarez
        benchmark, aka simple_physics) and shallow water models.

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

::


          atmosphere_mod
        time_manager_mod
        diag_manager_mod
                 fms_mod
       field_manager_mod
      tracer_manager_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

::


      This is a main program. There are no callable interfaces.

      A namelist interface called &main_nml must reside
      in file input.nml. See the details below.

--------------

NAMELIST
^^^^^^^^

::


   &main_nml

     current_time  The time (day,hour,minute,second) that the current
                   integration starts with.
                     [integer, dimension(4), default: current_time=0]

     override      Flag that determines whether the namelist variable
                   current_time should override the time in the
                   restart file INPUT/atmos_model.res. If the restart file
                   does not exist then override has not effect, the
                   value of current_date will be used.
                     [logical, default: override=false]

     days          The number of days that the current integration will
                   be run for.   [integer, default: days=0]

     hours         The number of hours that the current integration will
                   be run for.   [integer, default: hours=0]

     minutes       The number of minutes that the current integration will
                   be run for.   [integer, default: minutes=0]

     seconds       The number of seconds that the current integration will
                   be run for.   [integer, default: seconds=0]


     dt_atmos      Time step in seconds for the atmospheric model.
                   Must be specified.
                      [integer, default: dt_atmos=0]

     Notes:

       1) If no value is set for current_time (or default value specified)
          then the value from restart file "INPUT/atmos_model.res" will
          be used. If neither a namelist value or restart file value exist
          the program will fail.

       2) The actual run length will be the sum of days, hours,
          minutes, and seconds.  A run length of zero is not a valid option.

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

::


   FATAL ERRORS in program atmos_model

       dt_atmos has not been specified
           A value must be specified for variable "dt_atmos" in
           namelist &main_nml. See the namelist documentation for details.

       invalid base date - must have year = month = 0
           There is no calendar associated with this model.
           The base date retrieved from the diagnostics manager assumes
           that a year and month exist, this is not allowed.
           Set the base date year and month to zero in diag_table.

       initial time is greater than current time
           If a restart file is present, then the namelist value for either
           current_time or base time (from diag_table) was incorrectly set.

       run length must be multiple of atmosphere time step
           There must be an even number of atmospheric time steps for the
           requested run length.

   WARNINGS in program atmos_model

       final time does not match expected ending time
           This error should probably not occur because of checks done at
           initialization time.

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
