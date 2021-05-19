import unittest

import matplotlib_latex_bridge as mlb


class TestFunctions(unittest.TestCase):

    def test_letterpaper(self):
        self.assertEqual(mlb.formats.article_letterpaper_10pt_singlecolumn["textwidth"], 4.77)


if __name__ == '__main__':
    unittest.main()
