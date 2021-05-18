import matplotlib

from .formats import width_letterpaper_10pt


def set_font_sizes(small=8, medium=10, big=12):

    # medium size default is 10
    if medium is None:
        medium = 10

    # small and big sizes are scaled from medium
    if small is None:
        small = int(8 * medium / 10)

    if big is None:
        big = int(12 * medium / 10)

    matplotlib.rc('font', size=small)          # controls default text sizes
    matplotlib.rc('axes', titlesize=small)     # fontsize of the axes title
    matplotlib.rc('axes', labelsize=medium)    # fontsize of the x and y labels
    matplotlib.rc('xtick', labelsize=small)    # fontsize of the tick labels
    matplotlib.rc('ytick', labelsize=small)    # fontsize of the tick labels
    matplotlib.rc('legend', fontsize=small)    # legend fontsize
    matplotlib.rc('axes', titlesize=big)       # fontsize of the figure title


def set_default_figsize(w=None, h=None, dpi=400):

    if w is None and h is None:
        w = 6.4
        h = 4.8
    elif w is None:
        w = 6.4 / 4.8 * h
    elif h is None:
        h = 4.8 / 6.4 * w

    matplotlib.rc('figure', figsize=(w, h), dpi=dpi)


def get_figsize(w=None, h=None):

    if w is None:
        w = matplotlib.rcParams["figure.figsize"][0]

    if h is None:
        h = matplotlib.rcParams["figure.figsize"][1]

    return w, h


def match_latex_font():

    matplotlib.rc('font', family='serif')
    matplotlib.rc('text', usetex=True)


def init(linewidth=width_letterpaper_10pt, font_medium=10):

    set_font_sizes(medium=font_medium)
    set_default_figsize(w=linewidth)

    matplotlib.rc('figure.constrained_layout', use=True)  # use constrained layout

    match_latex_font()


init()
