from __future__ import print_function
import matplotlib.pyplot as plt
import os
import sys
import re
import subprocess
import tempfile
import shutil


mlb_initialized = False
mlb_textwidth = 0.0
mlb_columnwidth = 0.0
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
        raise RuntimeError("setup_page must be called before using {caller}".format(caller=caller))


def adjust_size(w, h):
    """
    Adjust a given figure size with the current defaults

    If only one of the two values (or none of them) has been specified,
    this function will keep the default matplotlib ratio.

    :param w: input width
    :param h: input height
    :return: adjusted w, adjusted h
    """

    if w is None and h is None:
        if not mlb_initialized:
            w = mlb_defaultw
            h = mlb_defaulth
        else:
            w = mlb_columnwidth  # arbitrary
            h = mlb_defaulth / mlb_defaultw * w
    elif w is None:
        w = mlb_defaultw / mlb_defaulth * h
    elif h is None:
        h = mlb_defaulth / mlb_defaultw * w

    return w, h


# public API
def set_font_family(family='serif', usetex=True):
    """
    Set the default font to match latex

    Using LaTex to render text requires a working LaTeX installation.

    :param family: font family used in the document
    :param usetex: True if the LaTeX processor should be enabled to render text
    """
    plt.rc('font', family=family)
    # the next line replaces shutils.which (for python < 3.3)
    haslatex = any((os.access(os.path.join(path, "latex"), os.X_OK) and os.path.isfile(os.path.join(path, "latex")))
                   for path in os.environ["PATH"].split(os.pathsep))
    if usetex and not haslatex:
        print("Requested LaTeX rendering, but no LaTeX installation found, disabling", file=sys.stderr)
    plt.rc('text', usetex=usetex and haslatex)


def get_default_figsize():
    """
    Return the current figure size defaults

    :return: default width, default height
    """
    w = plt.rcParams["figure.figsize"][0]
    h = plt.rcParams["figure.figsize"][1]
    return w, h


def set_font_sizes(small=8, medium=10, big=12):
    """
    Set the default fonts for the figures

    Usually the medium size should correspond to the normal latex text font size.

    The small and big sizes can be omitted, and they will be computed according to the medium size.

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

    plt.rc('font', size=small)          # controls default text sizes
    plt.rc('axes', labelsize=medium)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=small)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=small)    # fontsize of the tick labels
    plt.rc('legend', fontsize=small)    # legend fontsize
    plt.rc('axes', titlesize=big)       # fontsize of the figure title


def set_default_figsize(w=None, h=None, dpi=400):
    """
    Set the default figure size

    This is the size that will be used by doing ``plt.figure()``.

    :param w: width
    :param h: height
    :param dpi: dpi
    """
    w, h = adjust_size(w, h)

    plt.rc('figure', figsize=(w, h))
    plt.rc('savefig', dpi=dpi)


def setup_page(textwidth, columnwidth, fontsize, dpi=400, usetex=True):
    """
    Setup the page defaults

    Using LaTex to render text requires a working LaTeX installation.

    :param textwidth: width of the text in inches
    :param columnwidth: widht of the line (column) in inches
    :param fontsize: default font size of the document
    :param dpi: dpi for generated images
    :param usetex: True if the LaTeX processor should be enabled to render text
    """

    global mlb_textwidth, mlb_columnwidth, mlb_initialized

    # set max widths for warnings
    mlb_textwidth = textwidth
    mlb_columnwidth = columnwidth

    # set default fonts
    set_font_sizes(medium=fontsize)

    # set defaults figuresize to columnwidth
    set_default_figsize(w=columnwidth, dpi=dpi)

    # use constrained layout
    plt.rc('figure.constrained_layout', use=True)

    # match latex fonts
    set_font_family(usetex=usetex)

    mlb_initialized = True


def figure_textwidth(widthp=1.0, height=None, **kwargs):
    """
    Creates a figure that fill the width of the page

    :param widthp: width of the figure as a percentage of the text width (between 0 and 1)
    :param height: height of the figure (optional)
    :param kwargs: arguments that will be forwarded to matplotlib.pyplot.figure()
    :return: the new figure (matplotlib.figure.Figure)
    """
    assert_initialized("figure_textwidth")

    if widthp <= 0 or widthp > 1:
        print("Invalid percentual width of the figure {widthp}, must be between 0 and 1".format(widthp=widthp),
              file=sys.stderr)
        widthp = 1.0

    w, h = adjust_size(widthp * mlb_textwidth, height)

    return plt.figure(figsize=(w, h), **kwargs)


def figure_columnwidth(widthp=1.0, height=None, **kwargs):
    """
    Creates a figure that fill the width of the line (column)

    :param widthp: width of the figure as a percentage of the line width (between 0 and 1)
    :param height:  height of the figure (optional)
    :param kwargs: arguments that will be forwarded to matplotlib.pyplot.figure()
    :return: the new figure (matplotlib.figure.Figure)
    """
    assert_initialized("figure_columnwidth")

    if widthp <= 0 or widthp > 1:
        print("Invalid percentual width of the figure {widthp}, must be between 0 and 1".format(widthp=widthp),
              file=sys.stderr)
        widthp = 1.0

    w, h = adjust_size(widthp * mlb_columnwidth, height)

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

    if mlb_columnwidth < w < mlb_textwidth:
        print("Requested width ({}) is larger that columnwidth ({})".format(w, mlb_columnwidth), file=sys.stderr)
    elif mlb_textwidth < w:
        print("Requested width ({}) is larger that textwidth ({})".format(w, mlb_textwidth), file=sys.stderr)

    return plt.figure(figsize=(w, h), **kwargs)


def get_format_from_latex(documentclass, columns=None, papersize=None, fontsize=None, otheroptions=None):
    """
    Get the format by invoking the LaTeX processor

    This functions compiles a sample file with the LaTeX processor and parse its output to get information about
    text and column widths and fontsize.

    The output of this function can be directly used to setup the page.

    Using this function requires a working LaTeX installation.

    :param documentclass: layout standard to use (ex. article, report, book, ...)
    :param columns: number of columns (ex. twocolumn)
    :param papersize: size of the paper (ex. a4paper, letterpaper, ...)
    :param fontsize: size of the font (ex. 10pt, 11pt, 12pt)
    :param otheroptions: comma-separated additional options
    :return: dictionary with textwidth, columnwidth and fontsize
    """

    # check for LaTeX
    haslatex = any((os.access(os.path.join(path, "latex"), os.X_OK) and os.path.isfile(os.path.join(path, "latex")))
                   for path in os.environ["PATH"].split(os.pathsep))

    if not haslatex:
        raise RuntimeError("No LaTeX installation found")

    # build file content
    options = ""
    if columns:
        options = options + str(columns) + ","
    if papersize:
        options = options + str(papersize) + ","
    if fontsize:
        if type(fontsize) != str:
            options = options + str(fontsize) + "pt,"
        else:
            options = options + fontsize + ","
    if otheroptions:
        options = otheroptions + otheroptions
    latex_file_content = r"\documentclass[{options}]{{{documentclass}}}".format(documentclass=documentclass,
                                                                                options=options) + \
                         r"""

\usepackage{layouts}

\begin{document}

textwidth: \printinunitsof{in}\prntlen{\textwidth}
\message{textwidth: \prntlen{\textwidth}^^J}

columnwidth: \printinunitsof{in}\prntlen{\columnwidth}
\message{columnwidth: \prntlen{\columnwidth}^^J}

\message{fontsize: \the\font^^J}

\end{document}
"""

    # create temporary directory to run latex
    tmpdir = tempfile.mkdtemp()

    # write latex file
    with open(tmpdir + "/file.tex", "w") as texfile:
        texfile.write(latex_file_content)

    # run latex
    latex_output = subprocess.check_output(["latex", "file.tex"], cwd=tmpdir).decode()

    shutil.rmtree(tmpdir)

    latex_output = latex_output.replace("\n", "")

    # find widths
    twr = re.compile(r"\\relax ([0-9]+\.[0-9]+)in")
    m = twr.findall(latex_output)

    if len(m) != 2:
        raise RuntimeError("Something went wrong with the execution of LaTeX")

    textwidth = float(m[0])
    columnwidth = float(m[1])

    # find font size
    fr = re.compile(r"fontsize:.*/([0-9]+\.?[0-9]*)")
    m = fr.search(latex_output)

    if m is None:
        raise RuntimeError("Something went wrong with the execution of LaTeX")

    fontsize = float(m.groups()[0])

    return {
        "textwidth": textwidth,
        "columnwidth": columnwidth,
        "fontsize": fontsize
    }
