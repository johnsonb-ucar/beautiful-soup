PROGRM OR MODULE name_of_thing
==============================

=================== ============================================================
|DART project logo| Jump to `DART Documentation Main Index <../../index.html>`__
=================== ============================================================

`NAMELIST <#Namelist>`__ / `MODULES USED <#ModulesUsed>`__ / `INTERFACES <#Interface>`__ / `FILES <#FilesUsed>`__ /
`REFERENCES <#References>`__ / `ERRORS <#Errors>`__ / `PLANS <#FuturePlans>`__ / `PRIVATE
COMPONENTS <#PrivateComponents>`__ / `TERMS OF USE <#Legalese>`__

Overview
--------

Explain in general terms what this is.

.. container:: top

   [`top <#>`__]

--------------

NAMELIST
--------

DART namelists are always read from file *input.nml*.

We adhere to the F90 standard of starting a namelist with an ampersand '&' and terminating with a slash '/' for all our
namelist input. Character strings that contain a '/' must be enclosed in quotes to prevent them from prematurely
terminating the namelist.

.. container:: namelist

   ::

      &NAMELIST_NML 
         name=value,
         name=value, 
         name=value
      /

Any comments about the namelist as a whole.

| 

.. container::

   Item

Type

Description

name

type

(often multi-line) description

| 
| 

.. container:: top

   [`top <#>`__]

--------------

MODULES USED
------------

::

   types_mod
   utilities_mod
   random_seq_mod
   time_manager_mod
   ensemble_manager_mod

.. container:: top

   [`top <#>`__]

--------------

PUBLIC INTERFACES
-----------------

*use this_module_name_mod, only :*

`subr/function name <#tag>`__

 

`name2 <#tag2>`__

 

`name3 <#tag3>`__

A note about documentation style. Optional arguments are enclosed in brackets *[like this]*.

| 

.. container:: routine

   *subroutine subroutine1(arg1, [, arg2])*
   ::

      real(r8),           intent(in) :: arg1
      real(r8), optional, intent(in) :: arg2

.. container:: indent1

   describe what this subroutine does.

   *arg1*

Describe arg1.

*arg2*

Describe optional arg2.

| 
| 

.. container:: routine

   *function function1(arg1)*
   ::

      logical,             :: function1
      integer, intent(in)  :: arg1

.. container:: indent1

   Describe function.

   *function1*

describe what this function returns

*arg1*

describe function argument

| 
| 

.. container:: type

   ::

      type bob_type
         private
         integer :: bob1
         integer :: bob2
      end type bob_type

.. container:: indent1

   describe bob

   Component

Description

bob1

Describe bob1.

bob2

Describe bob2.

| 
| 

.. container:: top

   [`top <#>`__]

--------------

FILES
-----

describe files used by code

.. container:: top

   [`top <#>`__]

--------------

REFERENCES
----------

-  author, title. publication, volume, pages.
   `doi: nn.yyyy/rest_of_number <http://dx.doi.org/nn.yyyy/rest_of_number>`__

.. container:: top

   [`top <#>`__]

--------------

ERROR CODES and CONDITIONS
--------------------------

.. container:: errors

   Routine

Message

Comment

subroutine_name

error message text

what it means to the end user.

KNOWN BUGS
----------

none at this time

.. container:: top

   [`top <#>`__]

--------------

FUTURE PLANS
------------

none at this time

.. container:: top

   [`top <#>`__]

--------------

PRIVATE COMPONENTS
------------------

no discussion

.. container:: top

   [`top <#>`__]

--------------

Terms of Use
------------

DART software - Copyright UCAR. This open source software is provided by UCAR, "as is", without charge, subject to all
terms of use at http://www.image.ucar.edu/DAReS/DART/DART_download

.. |DART project logo| image:: ../../images/Dartboard7.png
   :height: 70px
