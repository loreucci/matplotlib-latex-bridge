import unittest

import matplotlib_latex_bridge as mlb


class TestFunctions(unittest.TestCase):

    def test_letterpaper(self):
        self.assertEqual(mlb.formats.width_letterpaper_10pt, 4.77)


if __name__ == '__main__':
    unittest.main()
