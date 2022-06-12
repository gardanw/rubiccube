import unittest
import numpy as np

from Cube import Cube


class CubeMoveTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube()

    def test_move_path(self):
        path = "dBFrlRrRddRdfRfRdBDUbFddBUDUfFduFLuBuBrBBdrDRuUrLr"
        self._cube.move(path)
        np.testing.assert_array_equal(
            self._cube.cube[0],
            np.array([["9r", "8g", "7b"], ["2b", "5y", "8w"], ["3b", "6r", "1y"]]),
        )
        np.testing.assert_array_equal(
            self._cube.cube[1],
            np.array([["9w", "2w", "7r"], ["2y", "5w", "2r"], ["9y", "4o", "3g"]]),
        )
        np.testing.assert_array_equal(
            self._cube.cube[2],
            np.array([["1b", "8o", "9o"], ["6b", "5g", "8b"], ["9b", "8y", "3y"]]),
        )
        np.testing.assert_array_equal(
            self._cube.cube[3],
            np.array([["7g", "4y", "1r"], ["4b", "5b", "6y"], ["3r", "2o", "9g"]]),
        )
        np.testing.assert_array_equal(
            self._cube.cube[4],
            np.array([["7y", "4g", "3o"], ["2g", "5r", "4r"], ["7o", "8r", "1w"]]),
        )
        np.testing.assert_array_equal(
            self._cube.cube[5],
            np.array([["7w", "6w", "3w"], ["4w", "5o", "6o"], ["1o", "6g", "1g"]]),
        )


if __name__ == "__main__":
    unittest.main()
