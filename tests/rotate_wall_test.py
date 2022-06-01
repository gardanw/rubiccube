import unittest
import numpy as np

from Cube import Cube


class CubeRotateTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube()

    def test_up_move(self):
        self._cube.u()
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['7y', '4y', '1y'], ['8y', '5y', '2y'], ['9y', '6y', '3y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['7w', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1o', '2o', '3o'], ['4g', '5g', '6g'], ['7g', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1r', '2r', '3r'], ['4b', '5b', '6b'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1g', '2g', '3g'], ['4r', '5r', '6r'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1b', '2b', '3b'], ['4o', '5o', '6o'], ['7o', '8o', '9o']]))
        self._cube.u(prim=True)
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['7y', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['7w', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7g', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7o', '8o', '9o']]))

    def test_down_move(self):
        self._cube.d()
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['7y', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['7w', '4w', '1w'], ['8w', '5w', '2w'], ['9w', '6w', '3w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7o', '8o', '9o']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7g', '8g', '9g']]))
        self._cube.d(prim=True)
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['7y', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['7w', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7g', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7o', '8o', '9o']]))

    def test_right_move(self):
        self._cube.r()
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3r'], ['4y', '5y', '6r'], ['7y', '8y', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '7o'], ['4w', '5w', '4o'], ['7w', '8w', '1o']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['7g', '4g', '1g'], ['8g', '5g', '2g'], ['9g', '6g', '3g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3w'], ['4r', '5r', '6w'], ['7r', '8r', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['9y', '2o', '3o'], ['6y', '5o', '6o'], ['3y', '8o', '9o']]))
        self._cube.r(prim=True)
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['7y', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['7w', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7g', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7o', '8o', '9o']]))

    def test_left_move(self):
        self._cube.l()
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['9o', '2y', '3y'], ['6o', '5y', '6y'], ['3o', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1r', '2w', '3w'], ['4r', '5w', '6w'], ['7r', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7g', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['7b', '4b', '1b'], ['8b', '5b', '2b'], ['9b', '6b', '3b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1y', '2r', '3r'], ['4y', '5r', '6r'], ['7y', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '7w'], ['4o', '5o', '4w'], ['7o', '8o', '1w']]))
        self._cube.l(prim=True)
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['7y', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['7w', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7g', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7o', '8o', '9o']]))

    def test_front_move(self):
        self._cube.f()
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['9b', '6b', '3b']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['7g', '4g', '1g'], ['4w', '5w', '6w'], ['7w', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['7y', '2g', '3g'], ['8y', '5g', '6g'], ['9y', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '1w'], ['4b', '5b', '2w'], ['7b', '8b', '3w']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['7r', '4r', '1r'], ['8r', '5r', '2r'], ['9r', '6r', '3r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7o', '8o', '9o']]))
        self._cube.f(prim=True)
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['7y', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['7w', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7g', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7o', '8o', '9o']]))

    def test_back_move(self):
        self._cube.b()
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['3g', '6g', '9g'], ['4y', '5y', '6y'], ['7y', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['1b', '4b', '7b']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '9w'], ['4g', '5g', '8w'], ['7g', '8g', '7w']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['3y', '2b', '3b'], ['2y', '5b', '6b'], ['1y', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['7o', '4o', '1o'], ['8o', '5o', '2o'], ['9o', '6o', '3o']]))
        self._cube.b(prim=True)
        np.testing.assert_array_equal(self._cube.cube[0],
                                      np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['7y', '8y', '9y']]))
        np.testing.assert_array_equal(self._cube.cube[1],
                                      np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['7w', '8w', '9w']]))
        np.testing.assert_array_equal(self._cube.cube[2],
                                      np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7g', '8g', '9g']]))
        np.testing.assert_array_equal(self._cube.cube[3],
                                      np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7b', '8b', '9b']]))
        np.testing.assert_array_equal(self._cube.cube[4],
                                      np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7r', '8r', '9r']]))
        np.testing.assert_array_equal(self._cube.cube[5],
                                      np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7o', '8o', '9o']]))


if __name__ == '__main__':
    unittest.main()
