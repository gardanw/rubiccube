import unittest
import numpy as np

from Cube import Cube


class CubeYellowCrossTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube()
        self._cube.shuffle()
        self._cube.white_cross()
        self._cube.white_corners()
        self._cube.second_layer()

    def test_yellow_cross(self):
        self._cube.yellow_cross()
        np.testing.assert_array_equal(self._cube.cube[0, 0, 1], "2y")
        np.testing.assert_array_equal(self._cube.cube[0, 1, 0], "4y")
        np.testing.assert_array_equal(self._cube.cube[0, 1, 2], "6y")
        np.testing.assert_array_equal(self._cube.cube[0, 2, 1], "8y")


if __name__ == "__main__":
    unittest.main()
