import unittest
import numpy as np

from Cube import Cube


class CubeRotateTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube()
        self._cube.shuffle()

    def test_first_layer(self):
        self._cube.white_cross()
        self._cube.white_corners()
        np.testing.assert_array_equal(
            self._cube.cube[1],
            np.array([["1w", "2w", "3w"], ["4w", "5w", "6w"], ["7w", "8w", "9w"]]),
        )


if __name__ == "__main__":
    unittest.main()
