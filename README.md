# matplotlib-latex-bridge

Functions and shortcuts to create latex-ready images from matplotlib.


## Quickstart

Initialize the library using one of the presets provided:

```python
import matplotlib_latex_bridge as mlb

mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn)
```
Create a new figure and use it as normal:
```python
fig = mlb.figure_textwidth()  # for full page images
fig = mlb.figure_linewidth()  # for full column images

plt.plot(...)

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
