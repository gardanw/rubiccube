def rotate_face(face):
    face[:] = face.T
    face[:, [2, 0]] = face[:, [0, 2]]


def rotate_face_p(face):
    face[:, [2, 0]] = face[:, [0, 2]]
    face[:] = face.T


def side_wall_move(u, d, r, l, ru=1, rd=1, rr=1, rl=1):
    tu = u.copy()
    td = d.copy()
    tr = r.copy()
    tl = l.copy()
    u[:], d[:], r[:], l[:] = tl[::rl], tr[::rr], tu[::ru], td[::rd]


def side_wall_move_p(u, d, r, l, ru=1, rd=1, rr=1, rl=1):
    tu = u.copy()
    td = d.copy()
    tr = r.copy()
    tl = l.copy()
    u[:], d[:], r[:], l[:] = tr[::rr], tl[::rl], td[::rd], tu[::ru]


def white_on_up(cube, piece):
    match piece:
        case '2w':
            while cube.cube[0, 2, 1] != '2w':
                cube.u()
            cube.move('FF')
        case '4w':
            while cube.cube[0, 1, 0] != '4w':
                cube.u()
            cube.move('LL')
        case '6w':
            while cube.cube[0, 1, 2] != '6w':
                cube.u()
            cube.move('RR')
        case '8w':
            while cube.cube[0, 0, 1] != '8w':
                cube.u()
            cube.move('BB')


def white_on_down(cube, piece):
    match piece:
        case '2w':
            while cube.cube[1, 0, 1] != '2w':
                cube.d()
        case '4w':
            cube.f(prim=True)
            while cube.cube[1, 1, 0] != '4w':
                cube.d()
            cube.f()
        case '6w':
            cube.f(prim=True)
            cube.l(prim=True)
            while cube.cube[1, 1, 2] != '6w':
                cube.d()
            cube.l()
            cube.f()
        case '8w':
            pass


def white_on_side(cube, piece, side, row):
    if row == 2:
        match side:
            case 2:
                cube.r()
            case 3:
                cube.l()
            case 4:
                cube.f()
            case 5:
                cube.b()
    match piece:
        case '2w':
            path = 'D' if side == 2 else 'd' if side == 3 else '' if side == 4 else 'DD'
            cube.move(path)
            while cube.cube[side, 1, 0] != '2w':
                cube.r() if side == 2 else cube.l() if side == 3 else cube.f() if side == 4 else cube.b()
            cube.d(prim=True)
            cube.f() if side == 2 else cube.b() if side == 3 else cube.l() if side == 4 else cube.r()
            while cube.cube[1, 0, 1] != '2w':
                cube.d()
        case '4w':
            path = 'DD' if side == 2 else '' if side == 3 else 'D' if side == 4 else 'd'
            cube.move(path)
            while cube.cube[side, 1, 0] != '4w':
                cube.r() if side == 2 else cube.l() if side == 3 else cube.f() if side == 4 else cube.b()
            cube.d(prim=True)
            cube.f() if side == 2 else cube.b() if side == 3 else cube.l() if side == 4 else cube.r()
            while cube.cube[1, 1, 0] != '4w':
                cube.d()
        case '6w':
            path = '' if side == 2 else 'DD' if side == 3 else 'd' if side == 4 else 'D'
            cube.move(path)
            while cube.cube[side, 1, 0] != '6w':
                cube.r() if side == 2 else cube.l() if side == 3 else cube.f() if side == 4 else cube.b()
            cube.d(prim=True)
            cube.f() if side == 2 else cube.b() if side == 3 else cube.l() if side == 4 else cube.r()
            while cube.cube[1, 1, 2] != '6w':
                cube.d()
        case '8w':
            path = 'd' if side == 2 else 'D' if side == 3 else 'DD' if side == 4 else ''
            cube.move(path)
            while cube.cube[side, 1, 0] != '8w':
                cube.r() if side == 2 else cube.l() if side == 3 else cube.f() if side == 4 else cube.b()
            cube.d(prim=True)
            cube.f() if side == 2 else cube.b() if side == 3 else cube.l() if side == 4 else cube.r()
            while cube.cube[1, 2, 1] != '8w':
                cube.d()
