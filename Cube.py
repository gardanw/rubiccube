import numpy as np
from myfunc.myfunc import *


class Cube:
    def __init__(self):
        up    = np.array([['1y', '2y', '3y'],
                          ['4y', '5y', '6y'],
                          ['7y', '8y', '9y']])
        down  = np.array([['1w', '2w', '3w'],
                          ['4w', '5w', '6w'],
                          ['7w', '8w', '9w']])
        right = np.array([['1g', '2g', '3g'],
                          ['4g', '5g', '6g'],
                          ['7g', '8g', '9g']])
        left  = np.array([['1b', '2b', '3b'],
                          ['4b', '5b', '6b'],
                          ['7b', '8b', '9b']])
        front = np.array([['1r', '2r', '3r'],
                          ['4r', '5r', '6r'],
                          ['7r', '8r', '9r']])
        back  = np.array([['1o', '2o', '3o'],
                          ['4o', '5o', '6o'],
                          ['7o', '8o', '9o']])

        self.cube = np.array([up, down, right, left, front, back])

        self.dict_cube = {'u': self.cube[0],
                          'd': self.cube[1],
                          'r': self.cube[2],
                          'l': self.cube[3],
                          'f': self.cube[4],
                          'b': self.cube[5]}

        self.moves = {'u': self.u,
                      'd': self.d,
                      'r': self.r,
                      'l': self.l,
                      'f': self.f,
                      'b': self.b}

    def u(self, prim=False):
        if prim:
            side_wall_move_p(self.cube[5][0, :],
                             self.cube[4][0, :],
                             self.cube[2][0, :],
                             self.cube[3][0, :])
            rotate_face_p(self.cube[0])
        else:
            side_wall_move(self.cube[5][0, :],
                           self.cube[4][0, :],
                           self.cube[2][0, :],
                           self.cube[3][0, :])
            rotate_face(self.cube[0])

    def d(self, prim=False):
        if prim:
            side_wall_move_p(self.cube[4][2, :],
                             self.cube[5][2, :],
                             self.cube[2][2, :],
                             self.cube[3][2, :])
            rotate_face_p(self.cube[1])
        else:
            side_wall_move(self.cube[4][2, :],
                           self.cube[5][2, :],
                           self.cube[2][2, :],
                           self.cube[3][2, :])
            rotate_face(self.cube[1])

    def r(self, prim=False):
        if prim:
            side_wall_move_p(self.cube[0][:, 2],
                             self.cube[1][:, 2],
                             self.cube[5][:, 0],
                             self.cube[4][:, 2],
                             rd=-1,
                             rr=-1)
            rotate_face_p(self.cube[2])
        else:
            side_wall_move(self.cube[0][:, 2],
                           self.cube[1][:, 2],
                           self.cube[5][:, 0],
                           self.cube[4][:, 2],
                           ru=-1,
                           rr=-1)
            rotate_face(self.cube[2])

    def l(self, prim=False):
        if prim:
            side_wall_move_p(self.cube[0][:, 0],
                             self.cube[1][:, 0],
                             self.cube[4][:, 0],
                             self.cube[5][:, 2],
                             ru=-1,
                             rl=-1)
            rotate_face_p(self.cube[3])
        else:
            side_wall_move(self.cube[0][:, 0],
                           self.cube[1][:, 0],
                           self.cube[4][:, 0],
                           self.cube[5][:, 2],
                           rd=-1,
                           rl=-1)
            rotate_face(self.cube[3])

    def f(self, prim=False):
        if prim:
            side_wall_move_p(self.cube[0][2, :],
                             self.cube[1][0, :],
                             self.cube[2][:, 0],
                             self.cube[3][:, 2],
                             ru=-1,
                             rd=-1)
            rotate_face_p(self.cube[4])
        else:
            side_wall_move(self.cube[0][2, :],
                           self.cube[1][0, :],
                           self.cube[2][:, 0],
                           self.cube[3][:, 2],
                           rl=-1,
                           rr=-1)
            rotate_face(self.cube[4])

    def b(self, prim=False):
        if prim:
            side_wall_move_p(self.cube[0][0, :],
                             self.cube[1][2, :],
                             self.cube[3][:, 0],
                             self.cube[2][:, 2],
                             rr=-1,
                             rl=-1)
            rotate_face_p(self.cube[5])
        else:
            side_wall_move(self.cube[0][0, :],
                           self.cube[1][2, :],
                           self.cube[3][:, 0],
                           self.cube[2][:, 2],
                           ru=-1,
                           rd=-1)
            rotate_face(self.cube[5])

    def move(self, path: str):
        for p in path:
            self.moves[p.lower()](prim=p.islower())

    def shuffle(self, i: int = 20):
        s = ''
        for _ in range(i):
            s += np.random.choice(['U', 'u', 'D', 'd', 'F', 'f', 'B', 'b', 'R', 'r', 'L', 'l'])
        self.move(s)
        return s

    def white_cross(self):
        for w in ['2w', '4w', '6w', '8w']:
            wrc = np.where(self.cube == w)
            match wrc[0][0]:
                case 0:
                    white_on_up(self, w)
                case 1:
                    white_on_down(self, w)
                case _:
                    white_on_side(self, w, wrc[0][0], wrc[1][0])
