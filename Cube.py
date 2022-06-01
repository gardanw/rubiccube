import numpy as np


class Cube:
    @staticmethod
    def rotate_face(face):
        face[:] = face.T
        face[:, [2, 0]] = face[:, [0, 2]]

    @staticmethod
    def rotate_face_p(face):
        face[:, [2, 0]] = face[:, [0, 2]]
        face[:] = face.T

    @staticmethod
    def side_wall_move(u, d, r, l, ru=1, rd=1, rr=1, rl=1):
        tu = u.copy()
        td = d.copy()
        tr = r.copy()
        tl = l.copy()
        u[:], d[:], r[:], l[:] = tl[::rl], tr[::rr], tu[::ru], td[::rd]

    @staticmethod
    def side_wall_move_p(u, d, r, l, ru=1, rd=1, rr=1, rl=1):
        tu = u.copy()
        td = d.copy()
        tr = r.copy()
        tl = l.copy()
        u[:], d[:], r[:], l[:] = tr[::rr], tl[::rl], td[::rd], tu[::ru]

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
            self.side_wall_move_p(self.cube[5][0, :],
                                  self.cube[4][0, :],
                                  self.cube[2][0, :],
                                  self.cube[3][0, :])
            self.rotate_face_p(self.cube[0])
        else:
            self.side_wall_move(self.cube[5][0, :],
                                self.cube[4][0, :],
                                self.cube[2][0, :],
                                self.cube[3][0, :])
            self.rotate_face(self.cube[0])

    def d(self, prim=False):
        if prim:
            self.side_wall_move_p(self.cube[4][2, :],
                                  self.cube[5][2, :],
                                  self.cube[2][2, :],
                                  self.cube[3][2, :])
            self.rotate_face_p(self.cube[1])
        else:
            self.side_wall_move(self.cube[4][2, :],
                                self.cube[5][2, :],
                                self.cube[2][2, :],
                                self.cube[3][2, :])
            self.rotate_face(self.cube[1])

    def r(self, prim=False):
        if prim:
            self.side_wall_move_p(self.cube[0][:, 2],
                                  self.cube[1][:, 2],
                                  self.cube[5][:, 0],
                                  self.cube[4][:, 2],
                                  rd=-1,
                                  rr=-1)
            self.rotate_face_p(self.cube[2])
        else:
            self.side_wall_move(self.cube[0][:, 2],
                                self.cube[1][:, 2],
                                self.cube[5][:, 0],
                                self.cube[4][:, 2],
                                ru=-1,
                                rr=-1)
            self.rotate_face(self.cube[2])

    def l(self, prim=False):
        if prim:
            self.side_wall_move_p(self.cube[0][:, 0],
                                  self.cube[1][:, 0],
                                  self.cube[4][:, 0],
                                  self.cube[5][:, 2],
                                  ru=-1,
                                  rl=-1)
            self.rotate_face_p(self.cube[3])
        else:
            self.side_wall_move(self.cube[0][:, 0],
                                self.cube[1][:, 0],
                                self.cube[4][:, 0],
                                self.cube[5][:, 2],
                                rd=-1,
                                rl=-1)
            self.rotate_face(self.cube[3])

    def f(self, prim=False):
        if prim:
            self.side_wall_move_p(self.cube[0][2, :],
                                  self.cube[1][0, :],
                                  self.cube[2][:, 0],
                                  self.cube[3][:, 2],
                                  ru=-1,
                                  rd=-1)
            self.rotate_face_p(self.cube[4])
        else:
            self.side_wall_move(self.cube[0][2, :],
                                self.cube[1][0, :],
                                self.cube[2][:, 0],
                                self.cube[3][:, 2],
                                rl=-1,
                                rr=-1)
            self.rotate_face(self.cube[4])

    def b(self, prim=False):
        if prim:
            self.side_wall_move_p(self.cube[0][0, :],
                                  self.cube[1][2, :],
                                  self.cube[3][:, 0],
                                  self.cube[2][:, 2],
                                  rr=-1,
                                  rl=-1)
            self.rotate_face_p(self.cube[5])
        else:
            self.side_wall_move(self.cube[0][0, :],
                                self.cube[1][2, :],
                                self.cube[3][:, 0],
                                self.cube[2][:, 2],
                                ru=-1,
                                rd=-1)
            self.rotate_face(self.cube[5])

    def move(self, path: str):
        for p in path:
            self.moves[p.lower()](prim=p.islower())
