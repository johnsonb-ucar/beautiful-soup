PROGRAM ``compare_states``
==========================

Contents
--------

-  `Overview <#overview>`__
-  `Namelist <#namelist>`__
-  `Modules used <#modules_used>`__
-  `Files <#files>`__
-  `References <#references>`__
-  `Error codes and conditions <#error_codes_and_conditions>`__

Overview
--------

Utility program to compare fields in two NetCDF files and print out the min and max values from each file and the min
and max of the differences between the two fields. The default is to compare all numeric variables in the files, but
specific variables can be specified in the namelist or in a separate file. The two input NetCDF filenames are read from
the console or can be echo'd into the standard input of the program.

If you want to restrict the comparison to only specific variables in the files, specify the list of field names to
compare either in the namelist, or put a list of fields, one per line, in a text file and specify the name of the text
file. Only data arrays can be compared, not character arrays, strings, or attribute values.

Namelist interface ``&compare_states_nml`` must be read from file ``input.nml``.

--------------

Namelist
--------

This namelist is read from the file ``input.nml``. Namelists start with an ampersand '&' and terminate with a slash '/'.
Character strings that contain a '/' must be enclosed in quotes to prevent them from prematurely terminating the
namelist.

::

   &compare_states_nml
      do_all_numeric_fields   = .true.
      fieldnames              = ''
      fieldlist_file          = ''
      fail_on_missing_field   = .true.
      only_report_differences = .true.
      debug                   = .false.
     /

| 

.. container::

   Item

Type

Description

do_all_numeric_fields

logical

If .true., all integer, float, and double variables in the NetCDF files will have their values compared. If .false. the
list of specific variables to be compared must be given either directly in the namelist in the ``fieldnames`` item, or
else the field names must be listed in an ASCII file, one name per line, and the name of that file is specified in
``fieldlist_file``.

fieldnames

character list

One or more names of arrays in the NetCDF files to be compared. Only read if ``do_all_numeric_fields`` is .false.

fieldlist_file

character

Name of a text file containing the fieldnames, one per line. It is an error to specify both the fieldnames namelist item
and this one. Only read if ``do_all_numeric_fields`` is .false.

fail_on_missing_field

logical

If .true. and any one of the field names is not found in both files it is a fatal error. If .false. a message is printed
about the missing field but execution continues.

only_report_differences

logical

If .true. only print the name of the variable being tested; skip printing the variable value min and max if the two
files are identical. If .false. print more details about both variables which differ and varibles with the same values.

debug

logical

If true print out debugging info.

| 

--------------

.. _modules_used:

Modules used
------------

::

   types_mod
   utilities_mod
   parse_args_mod

--------------

Files
-----

-  two NetCDF input files
-  compare_states.nml
-  field names text file (optionally)

--------------

References
----------

-  none

--------------

.. _error_codes_and_conditions:

Error codes and conditions
--------------------------

.. container:: errors

   +----------------+-------------------------------------------------+-------------------------------------------------+
   | Routine        | Message                                         | Comment                                         |
   +================+=================================================+=================================================+
   | compare_states | Only use single process                         | Only a single mpi process can be used with this |
   |                |                                                 | program                                         |
   +----------------+-------------------------------------------------+-------------------------------------------------+
   | compare_states | must specify data days and times                | If overwrite_data_time is true, the namelist    |
   |                |                                                 | must include the new day and time.              |
   +----------------+-------------------------------------------------+-------------------------------------------------+
   | compare_states | output_is_model_advance_file must be true to    | If overwrite_advance_time is true,              |
   |                | set advance time                                | output_is_model_advance_file must also be true. |
   +----------------+-------------------------------------------------+-------------------------------------------------+
   | compare_states | must specify advance days and times             | If overwrite_advance_time is true, the namelist |
   |                |                                                 | must include the new day and time.              |
   +----------------+-------------------------------------------------+-------------------------------------------------+
   | compare_states | overwrite_advance_time must be true if output   | If the incoming file does not have a model      |
   |                | file has advance time                           | advance time, the output cannot have one unless |
   |                |                                                 | the user gives one in the namelist, and sets    |
   |                |                                                 | overwrite_advance_time to true.                 |
   +----------------+-------------------------------------------------+-------------------------------------------------+
