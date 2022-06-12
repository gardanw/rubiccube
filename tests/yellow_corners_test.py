import unittest
import numpy as np

from Cube import Cube


class CubeYellowCornersTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube()
        self._cube.shuffle()
        self._cube.white_cross()
        self._cube.white_corners()
        self._cube.second_layer()
        self._cube.yellow_cross()

    def test_yellow_corners(self):
        self._cube.yellow_corners()
        np.testing.assert_array_equal(self._cube.cube[0, 0, 0], "1y")
        np.testing.assert_array_equal(self._cube.cube[0, 0, 2], "3y")
        np.testing.assert_array_equal(self._cube.cube[0, 2, 0], "7y")
        np.testing.assert_array_equal(self._cube.cube[0, 2, 2], "9y")


if __name__ == "__main__":
    unittest.main()
