from __future__ import absolute_import

from .matplotlib_latex_bridge import setup_page,\
                                     set_font_sizes, set_font_family,\
                                     set_default_figsize, get_default_figsize,\
                                     figure_columnwidth, figure_textwidth, figure, \
                                     get_format_from_latex

import matplotlib_latex_bridge.formats

from .version import version as __version__
