import matplotlib
import matplotlib.pyplot as plt


mlb_initialized = False
mlb_textwidth = 0.0
mlb_linewidth = 0.0
mlb_defaultw = 6.4
mlb_defaulth = 4.8


# helper functions
def assert_initialized(caller):
    """
    Check if the library has been initialized

    :param caller: name of the caller
    :raise RuntimeError if the library has not been initialized
    """
    if not mlb_initialized:
        raise RuntimeError(f"setup_page must be called before using {caller}")


def adjust_size(w, h):
    """
    Adjust a given figure size with the current defaults

    If only one of the two values (or none of them) has been specified, this function will keep the default matplotlib ratio.

    :param w: input width
    :param h: input height
    :return: adjusted w, adjusted h
    """

    if w is None and h is None:
        if not mlb_initialized:
            w = mlb_defaultw
            h = mlb_defaulth
        else:
            w = mlb_linewidth  # arbitrary
            h = mlb_defaulth / mlb_defaultw * w
    elif w is None:
        w = mlb_defaultw / mlb_defaulth * h
    elif h is None:
        h = mlb_defaulth / mlb_defaultw * w

    return w, h


# public API
def set_font_family(family='serif'):
    """
    Set the default font to match latex

    :param family: font family used in the document
    """
    plt.rc('font', family=family)
    plt.rc('text', usetex=True)


def get_default_figsize():
    """
    Return the current figure size defaults

    :return: default width, default height
    """
    w = matplotlib.rcParams["figure.figsize"][0]
    h = matplotlib.rcParams["figure.figsize"][1]
    return w, h


def set_font_sizes(small=8, medium=10, big=12):
    """
    Set the default fonts for the figures

    Usually the medium size correspond to the normal latex text font size.

    :param small: used for ticks and legends
    :param medium: used for the labels of the axes
    :param big: used for plot titles
    """

    # medium size default is 10
    if medium is None:
        medium = 10

    # small and big sizes are scaled from medium
    if small is None:
        small = int(8 * medium / 10)

    if big is None:
        big = int(12 * medium / 10)

    matplotlib.rc('font', size=small)          # controls default text sizes
    matplotlib.rc('axes', labelsize=medium)    # fontsize of the x and y labels
    matplotlib.rc('xtick', labelsize=small)    # fontsize of the tick labels
    matplotlib.rc('ytick', labelsize=small)    # fontsize of the tick labels
    matplotlib.rc('legend', fontsize=small)    # legend fontsize
    matplotlib.rc('axes', titlesize=big)       # fontsize of the figure title


def set_default_figsize(w=None, h=None, dpi=400):
    """
    Set the default figure size

    This is the size that will be used by doing ``plt.figure()``.

    :param w: width
    :param h: height
    :param dpi: dpi
    """
    w, h = adjust_size(w, h)

    matplotlib.rc('figure', figsize=(w, h), dpi=dpi)


def setup_page(textwidth, linewidth, fontsize, dpi=400):
    """
    Setup the page defaults

    :param textwidth: width of the text in inches
    :param linewidth: widht of the line (column) in inches
    :param fontsize: default font size of the document
    :param dpi: dpi for generated images
    """

    global mlb_textwidth, mlb_linewidth, mlb_initialized

    # set max widths for warnings
    mlb_textwidth = textwidth
    mlb_linewidth = linewidth

    # set default fonts
    set_font_sizes(medium=fontsize)

    # set defaults figuresize to linewidth
    set_default_figsize(w=linewidth, dpi=dpi)

    # use constrained layout
    plt.rc('figure.constrained_layout', use=True)

    # match latex fonts
    set_font_family()

    mlb_initialized = True


def figure_textwidth(height=None, **kwargs):
    """
    Creates a figure that fill the width of the page

    :param height: height of the figure (optional)
    :param kwargs: arguments that will be forwarded to matplotlib.pyplot.figure()
    :return: the new figure (matplotlib.figure.Figure)
    """
    assert_initialized("figure_textwidth")

    w, h = adjust_size(mlb_textwidth, height)

    return plt.figure(figsize=(w, h), **kwargs)


def figure_linewidth(height=None, **kwargs):
    """
    Creates a figure that fill the width of the line (column)

    :param height:  height of the figure (optional)
    :param kwargs: arguments that will be forwarded to matplotlib.pyplot.figure()
    :return: the new figure (matplotlib.figure.Figure)
    """
    assert_initialized("figure_linewidth")

    w, h = adjust_size(mlb_linewidth, height)

    return plt.figure(figsize=(w, h), **kwargs)


def figure(width=None, height=None, **kwargs):
    """
    Creates a figure with a custom size

    This function will print a warning if the figure width exceeds the width of the page or the line.

    :param width: width of the figure (optional)
    :param height: height of the figure (optional)
    :param kwargs: arguments that will be forwarded to matplotlib.pyplot.figure()
    :return: the new figure (matplotlib.figure.Figure)
    """
    assert_initialized("figure")

    w, h = adjust_size(width, height)

    if mlb_linewidth < w < mlb_textwidth:
        print(f"matplotlib-latex-bridge warning: requested width ({w}) is larger that linewidth ({mlb_linewidth})")
    elif mlb_textwidth < w:
        print(f"matplotlib-latex-bridge warning: requested width ({w}) is larger that textwidth ({mlb_textwidth})")

    return plt.figure(figsize=(w, h), **kwargs)
