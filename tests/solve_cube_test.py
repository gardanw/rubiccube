import unittest
import numpy as np

from Cube import Cube


class CubeSolveTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube()
        self._cube.shuffle()

        up = np.array([["1y", "2y", "3y"], ["4y", "5y", "6y"], ["7y", "8y", "9y"]])
        down = np.array([["1w", "2w", "3w"], ["4w", "5w", "6w"], ["7w", "8w", "9w"]])
        right = np.array([["1g", "2g", "3g"], ["4g", "5g", "6g"], ["7g", "8g", "9g"]])
        left = np.array([["1b", "2b", "3b"], ["4b", "5b", "6b"], ["7b", "8b", "9b"]])
        front = np.array([["1r", "2r", "3r"], ["4r", "5r", "6r"], ["7r", "8r", "9r"]])
        back = np.array([["1o", "2o", "3o"], ["4o", "5o", "6o"], ["7o", "8o", "9o"]])

        self.cube_to_check = np.array([up, down, right, left, front, back])

    def test_solve_cube(self):
        self._cube.solve_cube()
        np.testing.assert_array_equal(self._cube.cube, self.cube_to_check)


if __name__ == "__main__":
    unittest.main()
