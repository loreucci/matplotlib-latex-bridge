import unittest

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

    def setUp(self):
        mlb.setup_page(**mlb.formats.article_letterpaper_10pt_singlecolumn)
        mlb.figure()


if __name__ == '__main__':
    unittest.main()
