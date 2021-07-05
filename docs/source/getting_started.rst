Getting started
===============

The idea behing this library is that the user should only set the parameters for the current latex setup once and then
proceed to use matplotlib with minimal changes.

Basic Usage
-----------

The first step is to initialize the library by specifying:

- width of the text in inches
- width of the line in inches (might be different from text if using two columns)
- medium size of the font
- expected dpi of the images

While these informations can be specified manually, some presets are already present in the library
(see :ref:`formats:Formats` for a list of available presets).
By using these presets, the library can be initialized as follows:

.. code-block:: python

    import matplotlib_latex_bridge as mlb

    mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn)

After the library has been initialized, new figures should be created using two library functions that take care of
setting the right sizes:

.. code-block:: python

    fig = mlb.figure_textwidth()  # for full page images
    fig = mlb.figure_linewidth()  # for full column images

    plt.plot(...)

    fig.savefig("image.png")

Figures created like this should be included in the latex file without scaling:

.. code-block:: latex

    \begin{figure}
        \centering
        \includegraphics[scale=1]{image.png}
    \end{figure}


Customization
-------------

If there is no preset for your page format, or if you want more control over the size of the images generated,
you must manually specify the parameters for the :func:`matplotlib_latex_bridge.setup_page` function.

The ``textwidth`` and ``linewidth`` parameters are the width of the page and the column, respectively.
These two values are the same for single column documents, but they are different for multi-column environments.
The values for the current page layout can be found using the ``layouts`` latex package:

.. code-block:: latex

    \usepackage{layouts}

    \begin{document}

    textwidth: \printinunitsof{in}\prntlen{\textwidth}
    linewidth: \printinunitsof{in}\prntlen{\linewidth}

    \end{document}

The ``fontsize`` is the average text font, usually its value is set to the one
specified with the ``documentclass`` command, like in

.. code-block:: latex

    \documentclass[letterpaper, 10pt]{article}

A more fine-grained control over the font sizes can be achieved by using :func:`matplotlib_latex_bridge.set_font_sizes`
and :func:`matplotlib_latex_bridge.set_font_family`.

The ``dpi`` dipend on many factors, and a certain dpi may be a requirement for publication.
In general, a ``dpi`` >= 400 ensures a sharp image in most situations.