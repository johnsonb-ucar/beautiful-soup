module horiz_interp_mod
-----------------------

.. container::

   **Contact:**  `Bruce Wyman <mailto:bw@gfdl.noaa.gov>`__
   **Reviewers:** 
   **Change History:**  `WebCVS Log <http://www.gfdl.noaa.gov/fms-cgi-bin/cvsweb.cgi/FMS/>`__
   **Last Modified:** 2002/06/06 17:58:37

--------------

OVERVIEW
^^^^^^^^

Performs spatial interpolation between rectangular latitude/longitude grids.

.. container::

   The interpolation algorithm uses a scheme that conserves the area-weighed integral of the input field. The domain of
   the output field must lie within the domain of the input field.
