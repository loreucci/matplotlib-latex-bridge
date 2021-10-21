import numpy as np
import matplotlib.pyplot as plt

import matplotlib_latex_bridge as mlb


if __name__ == '__main__':

    mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn)

    x = np.linspace(-5, 5, 200)
    y = np.sin(x)

    mlb.figure_textwidth()
    plt.plot(x, y)
    plt.xlabel("time (s)")
    plt.ylabel("amplitude")
    plt.title("waveform")
    plt.savefig("textwidth.png")

    mlb.figure_columnwidth()
    plt.plot(x, y)
    plt.xlabel("time (s)")
    plt.ylabel("amplitude")
    plt.title("waveform")
    plt.savefig("columnwidth.png")
