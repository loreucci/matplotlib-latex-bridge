import unittest

import matplotlib_latex_bridge as mlb


class TestFunctions(unittest.TestCase):

    def test_get_figsize(self):
        sz = mlb.get_figsize(h=2)
        self.assertEqual(sz, (4.77, 2))


if __name__ == '__main__':
    unittest.main()
