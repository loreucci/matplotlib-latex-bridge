import unittest.mock
import io

import matplotlib_latex_bridge as mlb
import matplotlib


class TestBasics(unittest.TestCase):

    def test_setup(self):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn)
        self.assertEqual(mlb.formats.article_letterpaper_10pt_singlecolumn["linewidth"], mlb.get_default_figsize()[0])

    def test_set_default_figsize(self):
        mlb.set_default_figsize(w=10, h=20)
        w, h = mlb.get_default_figsize()
        self.assertEqual(w, 10)
        self.assertEqual(h, 20)
        self.assertEqual(matplotlib.rcParams["figure.figsize"][0], 10)
        self.assertEqual(matplotlib.rcParams["figure.figsize"][1], 20)

    def test_dpi_changed_savefig(self):
        dpi = matplotlib.rcParams["figure.dpi"]
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn, dpi=200)
        self.assertEqual(matplotlib.rcParams["figure.dpi"], dpi)
        self.assertEqual(matplotlib.rcParams["savefig.dpi"], 200)


class TestFigure(unittest.TestCase):

    def test_sizes(self):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_doublecolumn)

        fig = mlb.figure_textwidth()
        w, _ = fig.get_size_inches()
        self.assertAlmostEqual(w, mlb.formats.article_letterpaper_10pt_doublecolumn["textwidth"])

        fig = mlb.figure_linewidth()
        w, _ = fig.get_size_inches()
        self.assertAlmostEqual(w, mlb.formats.article_letterpaper_10pt_doublecolumn["linewidth"])

    def test_width_percentage(self):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_doublecolumn)

        fig = mlb.figure_textwidth(0.4)
        w, _ = fig.get_size_inches()
        self.assertAlmostEqual(w, mlb.formats.article_letterpaper_10pt_doublecolumn["textwidth"]*0.4)

        fig = mlb.figure_linewidth(0.7)
        w, _ = fig.get_size_inches()
        self.assertAlmostEqual(w, mlb.formats.article_letterpaper_10pt_doublecolumn["linewidth"]*0.7)

    @unittest.mock.patch('sys.stderr', new_callable=io.StringIO)
    def test_width_percentage_error(self, mock_stderr):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_doublecolumn)

        mlb.figure_linewidth(0.5)
        self.assertNotIn("Invalid percentual width", mock_stderr.getvalue())

        mlb.figure_textwidth(1.2)
        self.assertIn("Invalid percentual width", mock_stderr.getvalue())


if __name__ == '__main__':
    unittest.main()
