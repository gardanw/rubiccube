import unittest
import numpy as np

from Cube import Cube


class CubeRotateTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube()
        self._cube.shuffle()
        self._cube.white_cross()
        self._cube.white_corners()

    def test_first_layer(self):
        self._cube.second_layer()
        np.testing.assert_array_equal(
            self._cube.cube[1],
            np.array([["1w", "2w", "3w"], ["4w", "5w", "6w"], ["7w", "8w", "9w"]]),
        )
        np.testing.assert_array_equal(
            self._cube.cube[2, 1],
            np.array(['4g', '5g', '6g'])
        )
        np.testing.assert_array_equal(
            self._cube.cube[3, 1],
            np.array(['4b', '5b', '6b'])
        )
        np.testing.assert_array_equal(
            self._cube.cube[4, 1],
            np.array(['4r', '5r', '6r'])
        )
        np.testing.assert_array_equal(
            self._cube.cube[5, 1],
            np.array(['4o', '5o', '6o'])
        )


if __name__ == "__main__":
    unittest.main()