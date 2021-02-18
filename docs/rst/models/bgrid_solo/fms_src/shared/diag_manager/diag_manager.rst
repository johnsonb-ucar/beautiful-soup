module diag_manager_mod
-----------------------

.. container::

   **Contact:**  `Matt Harrison <mailto:mh@gfdl.noaa.gov>`__
   **Reviewers:** 
   **Change History:**  `WebCVS Log <http://www.gfdl.noaa.gov/fms-cgi-bin/cvsweb.cgi/FMS/>`__
   **Last Modified:** 2002/03/22 00:08:55

--------------

OVERVIEW
^^^^^^^^

<TT>diag_manager_mod</TT> is a set of simple calls for parallel diagnostics on distributed systems. It is geared toward
the writing of data in netCDF format.

.. container::

   <TT>diag_manager_mod</TT> provides a convenient set of interfaces for writing data to disk. It is built upon the
   parallel I/O interface
   `<TT>mpp_io</TT> <http://www.gfdl.noaa.gov/fms-cgi-bin/cvsweb.cgi/FMS/shared/mpp/models/bgrid_solo/fms_src/shared/mpp/mpp_io.html>`__.
   A single group of calls to the <TT>diag_manager_mod</TT> interfaces provides data to disk at any number of sampling
   and/or averaging intervals specified at run-time. Run-time specification of diagnostics are input through the
   diagnostics table, which is described in the
   `diag_table_tk <models/bgrid_solo/fms_src/shared/diag_manager/diag_table_tk.html>`__ documentation.
   <B>Features of <TT>diag_manager_mod</TT> include:</B> Simple, minimal API.
   Run-time choice of diagnostics.
   Self-describing files: comprehensive header information (metadata) in the file itself.
   Strong parallel write performance.
   Integrated netCDF capability: `netCDF <http://www.unidata.ucar.edu/packages/netcdf/>`__ is a data format widely used
   in the climate/weather modeling community. netCDF is considered the principal medium of data storage for
   <TT>diag_manager_mod</TT>. Raw unformatted fortran I/O capability is also available.
   Requires off-line post-processing: a tool for this purpose, <TT>mppnccombine</TT>, is available. GFDL users may use
   <TT>~hnv/pub/mppnccombine</TT>. Outside users may obtain the source
   `here <ftp://ftp.gfdl.gov/perm/hnv/mpp/mppnccombine.c>`__. It can be compiled on any C compiler and linked with the
   netCDF library. The program is free and is covered by the `GPL license <ftp://ftp.gfdl.gov/perm/hnv/mpp/LICENSE>`__.

| 
| 

--------------

OTHER MODULES USED
^^^^^^^^^^^^^^^^^^

.. container::

   ::

      time_manager_mod
            mpp_io_mod
               fms_mod
         diag_axis_mod
       diag_output_mod

--------------

PUBLIC INTERFACE
^^^^^^^^^^^^^^^^

.. container::

   ::

      use diag_manager_mod [, only:  send_data,
                                     register_diag_field,
                                     register_static_field,
                                     diag_manager_end,
                                     diag_manager_init,
                                     get_base_time,
                                     get_base_date,
                                     need_data ]

   `send_data <#send_data>`__:
      Send data over to output fields.
   `register_diag_field <#register_diag_field>`__:
      Register Diagnostic Field.
   `register_static_field <#register_static_field>`__:
      Register Static Field.
   `diag_manager_end <#diag_manager_end>`__:
      Exit Diagnostics Manager.
   `diag_manager_init <#diag_manager_init>`__:
      Initialize Diagnostics Manager.
   `get_base_time <#get_base_time>`__:
      Return base time for diagnostics.
   `get_base_date <#get_base_date>`__:
      Return base date for diagnostics.
   `need_data <#need_data>`__:
      Determine whether data is needed for the current model time step.

| 
| 

--------------

PUBLIC DATA
^^^^^^^^^^^

.. container::

   None.

--------------

PUBLIC ROUTINES
^^^^^^^^^^^^^^^

a. 

   .. rubric:: send_data
      :name: send_data

   **DESCRIPTION**
      send_data is overloaded for 1 to 3-d arrays. diag_field_id corresponds to the id returned from a previous call to
      register_diag_field. The field array is restricted to the computational range of the array. Optional argument
      is_in can be used to update sub-arrays of the entire field. Additionally, an optional logical or real mask can be
      used to apply missing values to the array. For the real mask, the mask is applied if the mask value is less than
      0.5. The weight array is currently not implemented.
   **INPUT**
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``diag_field_id   ``                                      |    [integer]                                              |
      |                                                           |    [integer]                                              |
      |                                                           |    [integer]                                              |
      |                                                           |    [integer]                                              |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``field   ``                                              |    [real]                                                 |
      |                                                           |    [real, dimension(:)]                                   |
      |                                                           |    [real, dimension(:,:)]                                 |
      |                                                           |    [real, dimension(:,:,:)]                               |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``time   ``                                               |    [time_type]                                            |
      |                                                           |    [time_type]                                            |
      |                                                           |    [time_type]                                            |
      |                                                           |    [time_type]                                            |
      +-----------------------------------------------------------+-----------------------------------------------------------+

b. 

   .. rubric:: register_diag_field
      :name: register_diag_field

   ::

       
      register_diag_field (module_name, field_name, axes, init_time, & long_name, units, missing_value, range)

   **DESCRIPTION**
      Return field index for subsequent calls to `send_data <#send_data>`__
   **INPUT**
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``module_name   ``                                        |    [character(len=*)]                                     |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``field_name   ``                                         |    [character(len=*)]                                     |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``axes   ``                                               |    [integer, dimension(:)]                                |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``init_time   ``                                          |    [time_type]                                            |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``long_name   ``                                          |    [character(len=*)]                                     |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``units   ``                                              |    [character(len=*)]                                     |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``missing_value   ``                                      |    [real]                                                 |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``range   ``                                              |    [real, dimension(2)]                                   |
      +-----------------------------------------------------------+-----------------------------------------------------------+

c. 

   .. rubric:: register_static_field
      :name: register_static_field

   ::

       
      register_static_field (module_name, field_name, axes, & long_name, units, missing_value, range, require)

   **DESCRIPTION**
      Return field index for subsequent call to send_data.
   **INPUT**
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``module_name   ``                                        |    [character(len=*)]                                     |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``field_name   ``                                         |    [character(len=*)]                                     |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``axes   ``                                               |    [integer, dimension(:)]                                |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``long_name   ``                                          |    [character(len=*)]                                     |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``units   ``                                              |    [character(len=*)]                                     |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``missing_value   ``                                      |    [real]                                                 |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``range   ``                                              |    [real, dimension(2)]                                   |
      +-----------------------------------------------------------+-----------------------------------------------------------+

d. 

   .. rubric:: diag_manager_end
      :name: diag_manager_end

   ::

      call diag_manager_end (time)

   **DESCRIPTION**
      Flushes diagnostic buffers where necessary. Close diagnostics files.
   **INPUT**
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``TIME   ``                                               |    [time_type]                                            |
      +-----------------------------------------------------------+-----------------------------------------------------------+

e. 

   .. rubric:: diag_manager_init
      :name: diag_manager_init

   ::

      call diag_manager_init ()

   **DESCRIPTION**
      Open and read diag_table. Select fields and files for diagnostic output.

f. 

   .. rubric:: get_base_time
      :name: get_base_time

   ::

      call get_base_time ()

   **DESCRIPTION**
      Return base time for diagnostics (note: base time must be >= model time).

g. 

   .. rubric:: get_base_date
      :name: get_base_date

   ::

      call get_base_date (year, month, day, hour, minute, second)

   **DESCRIPTION**
      Return date information for diagnostic reference time.

h. 

   .. rubric:: need_data
      :name: need_data

   ::

       
      need_data (diag_field_id,next_model_time)

   **DESCRIPTION**
      Determine whether data is needed for the current model time step. Since diagnostic data are buffered, the "next"
      model time is passed instead of the current model time. This call can be used to minimize overhead for complicated
      diagnostics.
   **INPUT**
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``inext_model_time   ``                                   | next_model_time = current model time + model time_step    |
      |                                                           |    [time_type]                                            |
      +-----------------------------------------------------------+-----------------------------------------------------------+
      | ``diag_field_id   ``                                      |    [integer]                                              |
      +-----------------------------------------------------------+-----------------------------------------------------------+

--------------

DATA SETS
^^^^^^^^^

.. container::

   None.

--------------

ERROR MESSAGES
^^^^^^^^^^^^^^

.. container::

   None.

--------------

REFERENCES
^^^^^^^^^^

.. container::

   None.

| 
| 

--------------

COMPILER SPECIFICS
^^^^^^^^^^^^^^^^^^

.. container::

   COMPILING AND LINKING SOURCE
      Any module or program unit using <TT>diag_manager_mod</TT> must contain the line

      ::

            use diag_manager_mod

      If netCDF output is desired, the cpp flag <TT>-Duse_netCDF</TT> must be turned on. The loader step requires an
      explicit link to the netCDF library (typically something like <TT>-L/usr/local/lib -lnetcdf</TT>, depending on the
      path to the netCDF library). `netCDF release 3 for fortran <http://www.unidata.ucar.edu/packages/netcdf/guidef>`__
      is required.

| 
| 

--------------

PRECOMPILER OPTIONS
^^^^^^^^^^^^^^^^^^^

.. container::

   PORTABILITY
      <TT>diag_manager_mod</TT> uses standard f90.

| 
| 

--------------

LOADER OPTIONS
^^^^^^^^^^^^^^

.. container::

   GFDL users can checkout diag_manager_mod using the cvs command <TT>setenv CVSROOT '/home/fms/cvs';cvs co
   diag_manager</TT>.

   ::

              ACQUIRING SOURCE

--------------

TEST PROGRAM
^^^^^^^^^^^^

.. container::

   None.

| 
| 

--------------

KNOWN BUGS
^^^^^^^^^^

.. container::

   None.

| 
| 

--------------

NOTES
^^^^^

.. container::

   None.

| 
| 

--------------

FUTURE PLANS
^^^^^^^^^^^^

.. container::

   None.

| 

--------------

.. container::

   `top <#TOP>`__
