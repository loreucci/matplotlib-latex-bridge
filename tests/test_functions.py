import sys
import unittest
if sys.version_info >= (3, 3):
    import unittest.mock as mock
else:
    import mock
if sys.version_info >= (3, 0):
    from io import StringIO
else:
    from io import BytesIO as StringIO

import matplotlib_latex_bridge as mlb
import matplotlib


class TestBasics(unittest.TestCase):

    def test_setup(self):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn)
        self.assertEqual(mlb.formats.article_letterpaper_10pt_singlecolumn["columnwidth"], mlb.get_default_figsize()[0])

    def test_set_default_figsize(self):
        mlb.set_default_figsize(w=10, h=20)
        w, h = mlb.get_default_figsize()
        self.assertEqual(w, 10)
        self.assertEqual(h, 20)
        self.assertEqual(matplotlib.rcParams["figure.figsize"][0], 10)
        self.assertEqual(matplotlib.rcParams["figure.figsize"][1], 20)

    def test_dpi_changed_savefig(self):
        dpi = matplotlib.rcParams["figure.dpi"]
        mlb.setup_page(dpi=200, **mlb.formats.article_letterpaper_10pt_singlecolumn)
        self.assertEqual(matplotlib.rcParams["figure.dpi"], dpi)
        self.assertEqual(matplotlib.rcParams["savefig.dpi"], 200)


class TestFigure(unittest.TestCase):

    def test_sizes(self):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_doublecolumn)

        fig = mlb.figure_textwidth()
        w, _ = fig.get_size_inches()
        self.assertAlmostEqual(w, mlb.formats.article_letterpaper_10pt_doublecolumn["textwidth"])

        fig = mlb.figure_columnwidth()
        w, _ = fig.get_size_inches()
        self.assertAlmostEqual(w, mlb.formats.article_letterpaper_10pt_doublecolumn["columnwidth"])

    def test_width_percentage(self):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_doublecolumn)

        fig = mlb.figure_textwidth(0.4)
        w, _ = fig.get_size_inches()
        self.assertAlmostEqual(w, mlb.formats.article_letterpaper_10pt_doublecolumn["textwidth"]*0.4)

        fig = mlb.figure_columnwidth(0.7)
        w, _ = fig.get_size_inches()
        self.assertAlmostEqual(w, mlb.formats.article_letterpaper_10pt_doublecolumn["columnwidth"]*0.7)

    @mock.patch('sys.stderr', new_callable=StringIO)
    def test_width_percentage_error(self, mock_stderr):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_doublecolumn)

        mlb.figure_columnwidth(0.5)
        self.assertNotIn("Invalid percentual width", mock_stderr.getvalue())

        mlb.figure_textwidth(1.2)
        self.assertIn("Invalid percentual width", mock_stderr.getvalue())


class TestLatex(unittest.TestCase):

    def test_format_from_latex(self):

        fmt = mlb.get_format_from_latex(documentclass="article",
                                        columns="twocolumn",
                                        papersize="letterpaper",
                                        fontsize=12)

        self.assertAlmostEqual(fmt["textwidth"], 6.49083)
        self.assertAlmostEqual(fmt["columnwidth"], 3.17621)
        self.assertAlmostEqual(fmt["fontsize"], 12)

    def test_special_characters(self):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_doublecolumn)
        fig = mlb.figure_textwidth()
        ax = fig.gca()
        ax.plot(range(10), range(10), label="#")

        ax.legend()
        with self.assertRaises(RuntimeError):
            mlb.savefig("shouldnotsave.png")


if __name__ == '__main__':
    unittest.main()
