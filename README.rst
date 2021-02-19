##############
Beautiful Soup
##############

DAReS staff have been using `pandoc <https://pandoc.org/>`_ to convert the
DART documentation from HTML to reStructuredText.

The files output by pandoc must often be edited by hand to clean up conversion
artifacts. This is because pandoc has a specific set of syntax elements that it
represents in its `abstract syntax tree <https://pandoc.org/MANUAL.pdf>`_. 

This set of syntax elements limits what an output document can be composed of
-- e.g. titles, links, lists, code, literal strings, references, etc. -- and
DART's existing HTML documentation is composed of a much broader collection of
idiosyncratic expressions that pandoc isn't equipped to handle.

For example, when a FORTRAN namelist is described in the documentation it is
wrapped in a div with a namelist class. Pandoc doesn't have a corresponding
syntax expression for such a div, thus the conversion is lossy and the
resulting document always contains conversion artifacts.

The key to using pandoc to convert DART documentation from HTML to
reStructuredText is to preemptively translate DART's idiosyncratic expressions
into a subset of syntax expressions that pandoc is capable of understanding.

Python's `Beautiful Soup <https://www.crummy.com/software/BeautifulSoup/>`_
library is well-equipped for this preemptive translation. It can be used to
create functions to handle specific types of idiosyncratic expressions.

This repository tracks the progress of the software development for this
effort.

Installing the library
======================

You can use ``pip`` to install the library:

.. code-block::

   $ pip install beautifulsoup4

Running the scripts
===================

After the library is installed:

.. code-block::

   $ python test_functions.py

The script will read an input file,
``docs/html/observations/obs_converters/MODIS/MOD15A2_to_obs.html``, and will
create a separate output file,
``docs/html/observations/obs_converters/MODIS/modified_MOD15A2_to_obs.html``.

The files can be compared using your favorite diff tool. For example:

.. code-block::

   $ meld docs/html/observations/obs_converters/MODIS/MOD15A2_to_obs.html ./modified_MOD15A2_to_obs.html
