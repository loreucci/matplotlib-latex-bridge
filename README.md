# matplotlib-latex-bridge

Functions and shortcuts to create latex-ready images from matplotlib.


## Basic usage

As a first step, the library should be initialized with these pieces of information:

 * width of the text in inches
 * width of the line in inches (might be different from text if using two columns)
 * medium size of the font
 * expected dpi of the images

The library contains some presets for the most common combinations of documentclasses, page sizes and fonts. As such,
the library can be initialized as follows:
```python
import matplotlib_latex_bridge as mlb

mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn)
```

If there is no preset for your page format, you can easily find the text and line width by adding these lines to your
latex document:
```latex
\usepackage{layouts}

\begin{document}

textwidth: \printinunitsof{in}\prntlen{\textwidth}
linewidth: \printinunitsof{in}\prntlen{\linewidth}
...

\end{document}
```

After the library has been initialized, new figures should be created using
```python
fig = mlb.figure_textwidth(heigth)  # for full page images
fig = mlb.figure_linewidth(heigth)  # for full column images

# code to plot

fig.savefig("image.png")
```

Figures created like this should be included in the latex file without scaling:
```latex
\begin{figure}
    \centering
    \includegraphics[scale=1]{image.png}
\end{figure}
```

## Font size control

A more fine-grained control over the size of the fonts used can be achieved by using
```python
mlb.set_font_sizes(small_size, medium_size, big_size)
```
The small size will be used for ticks and legends, medium for the labels of the axes and big for plot titles.