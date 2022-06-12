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
        case "2w":
            while cube.cube[0, 2, 1] != "2w":
                cube.u()
            cube.move("FF")
        case "4w":
            while cube.cube[0, 1, 0] != "4w":
                cube.u()
            cube.move("LL")
        case "6w":
            while cube.cube[0, 1, 2] != "6w":
                cube.u()
            cube.move("RR")
        case "8w":
            while cube.cube[0, 0, 1] != "8w":
                cube.u()
            cube.move("BB")


def white_on_down(cube, piece):
    match piece:
        case "2w":
            while cube.cube[1, 0, 1] != "2w":
                cube.d()
        case "4w":
            cube.f(prim=True)
            while cube.cube[1, 1, 0] != "4w":
                cube.d()
            cube.f()
        case "6w":
            cube.f(prim=True)
            cube.l(prim=True)
            while cube.cube[1, 1, 2] != "6w":
                cube.d()
            cube.l()
            cube.f()
        case "8w":
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
        case "2w":
            path = "D" if side == 2 else "d" if side == 3 else "" if side == 4 else "DD"
            cube.move(path)
            while cube.cube[side, 1, 0] != "2w":
                cube.r() if side == 2 else cube.l() if side == 3 else cube.f() if side == 4 else cube.b()
            cube.d(prim=True)
            cube.f() if side == 2 else cube.b() if side == 3 else cube.l() if side == 4 else cube.r()
            while cube.cube[1, 0, 1] != "2w":
                cube.d()
        case "4w":
            path = "DD" if side == 2 else "" if side == 3 else "D" if side == 4 else "d"
            cube.move(path)
            while cube.cube[side, 1, 0] != "4w":
                cube.r() if side == 2 else cube.l() if side == 3 else cube.f() if side == 4 else cube.b()
            cube.d(prim=True)
            cube.f() if side == 2 else cube.b() if side == 3 else cube.l() if side == 4 else cube.r()
            while cube.cube[1, 1, 0] != "4w":
                cube.d()
        case "6w":
            path = "" if side == 2 else "DD" if side == 3 else "d" if side == 4 else "D"
            cube.move(path)
            while cube.cube[side, 1, 0] != "6w":
                cube.r() if side == 2 else cube.l() if side == 3 else cube.f() if side == 4 else cube.b()
            cube.d(prim=True)
            cube.f() if side == 2 else cube.b() if side == 3 else cube.l() if side == 4 else cube.r()
            while cube.cube[1, 1, 2] != "6w":
                cube.d()
        case "8w":
            path = "d" if side == 2 else "D" if side == 3 else "DD" if side == 4 else ""
            cube.move(path)
            while cube.cube[side, 1, 0] != "8w":
                cube.r() if side == 2 else cube.l() if side == 3 else cube.f() if side == 4 else cube.b()
            cube.d(prim=True)
            cube.f() if side == 2 else cube.b() if side == 3 else cube.l() if side == 4 else cube.r()
            while cube.cube[1, 2, 1] != "8w":
                cube.d()


def corn_on_up(cube, piece):
    match piece:
        case "1w":
            while cube.cube[0, 2, 0] != "1w":
                cube.u()
            while cube.cube[1, 0, 0] != "1w":
                cube.move("luLU")
        case "3w":
            while cube.cube[0, 2, 2] != "3w":
                cube.u()
            while cube.cube[1, 0, 2] != "3w":
                cube.move("RUru")
        case "7w":
            while cube.cube[0, 0, 0] != "7w":
                cube.u()
            while cube.cube[1, 2, 0] != "7w":
                cube.move("LUlu")
        case "9w":
            while cube.cube[0, 0, 2] != "9w":
                cube.u()
            while cube.cube[1, 2, 2] != "9w":
                cube.move("ruRU")


def corn_on_down(cube, piece, row, column):
    match (row, column):
        case (0, 0):
            if piece != "1w":
                cube.move("luLU" * 3)
                corn_on_up(cube, piece)
        case (0, 2):
            if piece != "3w":
                cube.move("RUru" * 3)
                corn_on_up(cube, piece)
        case (2, 0):
            if piece != "7w":
                cube.move("LUlu" * 3)
                corn_on_up(cube, piece)
        case (2, 2):
            if piece != "9w":
                cube.move("ruRU" * 3)
                corn_on_up(cube, piece)


def corn_on_side(cube, piece, side, row, column):
    match (row, column):
        case (0, 0):
            match piece:
                case "1w":
                    while cube.cube[4, 0, 0] != "1w":
                        cube.u()
                    cube.move("FUfu")
                case "3w":
                    while cube.cube[2, 0, 0] != "3w":
                        cube.u()
                    cube.move("RUru")
                case "7w":
                    while cube.cube[3, 0, 0] != "7w":
                        cube.u()
                    cube.move("LUlu")
                case "9w":
                    while cube.cube[5, 0, 0] != "9w":
                        cube.u()
                    cube.move("BUbu")
        case (0, 2):
            match piece:
                case "1w":
                    while cube.cube[3, 0, 2] != "1w":
                        cube.u()
                    cube.move("luLU")
                case "3w":
                    while cube.cube[4, 0, 2] != "3w":
                        cube.u()
                    cube.move("fuFU")
                case "7w":
                    while cube.cube[5, 0, 2] != "7w":
                        cube.u()
                    cube.move("buBU")
                case "9w":
                    while cube.cube[2, 0, 2] != "9w":
                        cube.u()
                    cube.move("ruRU")
        case (2, 0):
            match side:
                case 2:
                    cube.move("fuFU")
                    corn_on_up(cube, piece)
                case 3:
                    cube.move("buBU")
                    corn_on_up(cube, piece)
                case 4:
                    cube.move("luLU")
                    corn_on_up(cube, piece)
                case 5:
                    cube.move("ruRU")
                    corn_on_up(cube, piece)
        case (2, 2):
            match side:
                case 2:
                    cube.move("BUbu")
                    corn_on_up(cube, piece)
                case 3:
                    cube.move("FUfu")
                    corn_on_up(cube, piece)
                case 4:
                    cube.move("RUru")
                    corn_on_up(cube, piece)
                case 5:
                    cube.move("LUlu")
                    corn_on_up(cube, piece)


def edge_on_up(cube, edge):
    match edge:
        case "4r":
            while cube.cube[0, 0, 1] != "4r":
                cube.u()
            path = "FufulUL"
            cube.move(path)
        case "4b":
            while cube.cube[0, 1, 2] != "4b":
                cube.u()
            path = "LulubUB"
            cube.move(path)
        case "4o":
            while cube.cube[0, 2, 1] != "4o":
                cube.u()
            path = "BuburUR"
            cube.move(path)
        case "4g":
            while cube.cube[0, 1, 0] != "4g":
                cube.u()
            path = "RurufUF"
            cube.move(path)


def edge_on_c_0(cube, edge, wall):
    match wall:
        case 2:
            if edge != "4g":
                path = "fUFURur"
                cube.move(path)
                edge_on_up(cube, edge)
        case 3:
            if edge != "4b":
                path = "bUBULul"
                cube.move(path)
                edge_on_up(cube, edge)
        case 4:
            if edge != "4r":
                path = "lULUFuf"
                cube.move(path)
                edge_on_up(cube, edge)
        case 5:
            if edge != "4o":
                path = "rURUBub"
                cube.move(path)
                edge_on_up(cube, edge)


def edge_on_c_1(cube, edge):
    match edge:
        case "4r":
            while cube.cube[2, 0, 1] != "4r":
                cube.u()
            path = "lULUFuf"
            cube.move(path)
        case "4b":
            while cube.cube[4, 0, 1] != "4b":
                cube.u()
            path = "bUBULul"
            cube.move(path)
        case "4o":
            while cube.cube[3, 0, 1] != "4o":
                cube.u()
            path = "rURUBub"
            cube.move(path)
        case "4g":
            while cube.cube[5, 0, 1] != "4g":
                cube.u()
            path = "fUFURur"
            cube.move(path)


def edge_on_c_2(cube, edge, wall):
    match wall:
        case 2:
            path = "BuburUR"
            cube.move(path)
            edge_on_up(cube, edge)
        case 3:
            path = "FufulUL"
            cube.move(path)
            edge_on_up(cube, edge)
        case 4:
            path = "RurufUF"
            cube.move(path)
            edge_on_up(cube, edge)
        case 5:
            path = "LulubUB"
            cube.move(path)
            edge_on_up(cube, edge)


def sort_yellow_cross(cube):
    while cube.cube[0, 0, 1] != "2y":
        cube.u()
    bottom_cross = [cube.cube[0, 1, 0], cube.cube[0, 1, 2], cube.cube[0, 2, 1]]
    match bottom_cross:
        case ["8y", "4y", "6y"] | ["6y", "8y", "4y"]:
            while [cube.cube[0, 1, 0], cube.cube[0, 1, 2], cube.cube[0, 2, 1]] != [
                "4y",
                "6y",
                "8y",
            ]:
                path = "LUUluLul"
                cube.move(path)
        case ["4y", "8y", "6y"] | ["8y", "6y", "4y"] | ["6y", "4y", "8y"]:
            while [cube.cube[0, 1, 0], cube.cube[0, 1, 2], cube.cube[0, 2, 1]] != [
                "8y",
                "6y",
                "4y",
            ]:
                path = "LUUluLul"
                cube.move(path)
            path = "uRUUruRur"
            cube.move(path)
