Figure management functions
=================================

.. currentmodule:: matplotlib_latex_bridge

Page setup
----------

This is the main function that have to be called everytime the library is used.

.. autofunction:: setup_page

Font control
------------
To fine tune the font control, these functions can be called after :func:`matplotlib_latex_bridge.setup_page`.

.. autofunction:: set_font_sizes

.. autofunction:: set_font_family

Figure control
--------------
The default figure size can be changed or accessed after the initial setup by using these functions.

.. autofunction:: set_default_figsize

.. autofunction:: get_default_figsize

Figure generation
-----------------
These functions allow the creation of matplotlib figures using (or overriding) the default size specified
in the initial setup.

.. autofunction:: figure_columnwidth

.. autofunction:: figure_textwidth

.. autofunction:: figure
