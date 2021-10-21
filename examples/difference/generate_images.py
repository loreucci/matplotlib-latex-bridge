import numpy as np
import matplotlib.pyplot as plt

import matplotlib_latex_bridge as mlb


if __name__ == '__main__':

    x = np.linspace(-5, 5, 200)
    y = np.sin(x)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("time (s)")
    plt.ylabel("amplitude")
    plt.title("waveform")
    plt.savefig("default.png")

    mlb.setup_page(**mlb.formats.article_letterpaper_10pt_doublecolumn)

    mlb.figure_columnwidth()
    plt.plot(x, y)
    plt.xlabel("time (s)")
    plt.ylabel("amplitude")
    plt.title("waveform")
    plt.savefig("mlb.png")
