import unittest
import numpy as np

from Cube import Cube


class CubeRotateTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube()
        self._cube.shuffle()

    def test_white_cross(self):
        self._cube.white_cross()
        w2 = np.where(self._cube.cube == '2w')
        np.testing.assert_array_equal(w2, np.array([np.array([1]), np.array([0]), np.array([1])]))
        w4 = np.where(self._cube.cube == '4w')
        np.testing.assert_array_equal(w4, np.array([np.array([1]), np.array([1]), np.array([0])]))
        w6 = np.where(self._cube.cube == '6w')
        np.testing.assert_array_equal(w6, np.array([np.array([1]), np.array([1]), np.array([2])]))
        w8 = np.where(self._cube.cube == '8w')
        np.testing.assert_array_equal(w8, np.array([np.array([1]), np.array([2]), np.array([1])]))


if __name__ == '__main__':
    unittest.main()
