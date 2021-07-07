# matplotlib-latex-bridge

[![Documentation Status](https://readthedocs.org/projects/matplotlib-latex-bridge/badge/?version=latest)](https://matplotlib-latex-bridge.readthedocs.io/en/latest/?badge=latest)

This library provides a set of functions and shortcuts to create latex-ready images with matplotlib.

This library is not a replacement for matplotib, it can just be used to set sensible settings in order to have figures with readable text and with a font size that is consistent both among various figures and with the rest of the text in the document.

Example:

![example](https://github.com/loreucci/matplotlib-latex-bridge/raw/master/mlb-example.png)


## Quickstart

Initialize the library using one of the presets provided:

```python
import matplotlib_latex_bridge as mlb

mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn)
```
Create a new figure and use it as normal:
```python
mlb.figure_textwidth()  # for full page images
mlb.figure_linewidth()  # for full column images

plt.plot(...)  # use matplotlib as normal

fig.savefig("image.png")
```
Include it in the latex file without scaling:
```latex
\begin{figure}
    \centering
    \includegraphics[scale=1]{image.png}
\end{figure}
```
That's it!

For more options please refer to the [online documentation](https://matplotlib-latex-bridge.readthedocs.io).