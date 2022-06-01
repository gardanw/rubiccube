import numpy as np


class Cube:
    def __init__(self):
        up = np.array([['1y', '2y', '3y'], ['4y', '5y', '6y'], ['7y', '8y', '9y']])
        down = np.array([['1w', '2w', '3w'], ['4w', '5w', '6w'], ['7w', '8w', '9w']])
        right = np.array([['1g', '2g', '3g'], ['4g', '5g', '6g'], ['7g', '8g', '9g']])
        left = np.array([['1b', '2b', '3b'], ['4b', '5b', '6b'], ['7b', '8b', '9b']])
        front = np.array([['1r', '2r', '3r'], ['4r', '5r', '6r'], ['7r', '8r', '9r']])
        back = np.array([['1o', '2o', '3o'], ['4o', '5o', '6o'], ['7o', '8o', '9o']])

        self.cube = np.array([up, down, right, left, front, back])

        self.dict_cube = {'u': self.cube[0], 'd': self.cube[1], 'r': self.cube[2], 'l': self.cube[3], 'f': self.cube[4],
                          'b': self.cube[5]}
