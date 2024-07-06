# solve the puzzle cube
from copy import deepcopy
import numpy as np
filename = 'input31.txt'
#filename = 'test31.txt'
TEST = False

with open(filename) as f:
    ls = f.read().strip()

moves = []
for c in ls:
    if c == "'":
        m = moves.pop()
        moves.append(m + c)
    else:
        moves.append(c)

# cube will be a set of 2D matrixes, layout as pictured, ULFRDB
cube = [[[2, 2, 2], [2, 2, 2], [2, 2, 2]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
        [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
        [[6, 6, 6], [6, 6, 6], [6, 6, 6]]]
# cube for testing
if TEST:
    cube = [[[1, 2, 3], [4, 5, 6], [1, 2, 3]],
        [[1, 2, 3], [4, 5, 6], [1, 2, 3]],
        [[1, 2, 3], [4, 5, 6], [1, 2, 3]],
        [[1, 2, 3], [4, 5, 6], [1, 2, 3]],
        [[1, 2, 3], [4, 5, 6], [1, 2, 3]],
        [[1, 2, 3], [4, 5, 6], [1, 2, 3]]]

faces = {'U':0, 'L':1, 'F':2, 'R':3, 'D':4, 'B':5}
face_list = ['U', 'L', 'F', 'R', 'D', 'B']

def printCube(cube):
    for row in cube[0]:
        line = ''.join(map(str, row))
        print(f"{line.center(13)}")
    print(f"{'up'.center(13)}")
    for y in range(3):
        line = []
        for face in range(1, 4):
            line.append(''.join(map(str, cube[face][y])))
        print('  '.join(line))
    print('left frnt rght')
    for row in cube[4]:
        line = ''.join(map(str, row))
        print(f"{line.center(13)}")
    print(f"{'down'.center(13)}")
    for row in cube[5]:
        line = ''.join(map(str, row))
        print(f"{line.center(13)}")
    print(f"{'back'.center(13)}")

def rotateFace(cube, new_cube, face, clockwise):
    array = np.array(cube[faces[face]])
    if clockwise:
        new_face = np.rot90(array, k=-1).tolist()
    else:
        new_face = np.rot90(array).tolist()
    for y in range(3):
        for x in range(3):
            new_cube[faces[face]][y][x] = new_face[y][x]

def up(cube, clockwise):
    new_cube = deepcopy(cube)
    if not clockwise:
        # update up
        rotateFace(cube, new_cube, 'U', clockwise)
        # update  left
        new_cube[1][0][0] = cube[5][0][0]
        new_cube[1][0][1] = cube[5][0][1]
        new_cube[1][0][2] = cube[5][0][2]
        # update front
        new_cube[2][0][0] = cube[1][0][0]
        new_cube[2][0][1] = cube[1][0][1]
        new_cube[2][0][2] = cube[1][0][2]
        # update right
        new_cube[3][0][0] = cube[2][0][0]
        new_cube[3][0][1] = cube[2][0][1]
        new_cube[3][0][2] = cube[2][0][2]
        # update back
        new_cube[5][0][0] = cube[3][0][0]
        new_cube[5][0][1] = cube[3][0][1]
        new_cube[5][0][2] = cube[3][0][2]
    else:
        # update up
        rotateFace(cube, new_cube, 'U', clockwise)
        # update  left
        new_cube[1][0][0] = cube[2][0][0]
        new_cube[1][0][1] = cube[2][0][1]
        new_cube[1][0][2] = cube[2][0][2]
        # update front
        new_cube[2][0][0] = cube[3][0][0]
        new_cube[2][0][1] = cube[3][0][1]
        new_cube[2][0][2] = cube[3][0][2]
        # update right
        new_cube[3][0][0] = cube[5][0][0]
        new_cube[3][0][1] = cube[5][0][1]
        new_cube[3][0][2] = cube[5][0][2]
        # update back
        new_cube[5][0][0] = cube[1][0][0]
        new_cube[5][0][1] = cube[1][0][1]
        new_cube[5][0][2] = cube[1][0][2]
    return(new_cube)
if TEST:
    print("Original cube")
    printCube(cube)
    cube = up(cube, True)
    print("After up clockwise")
    printCube(cube)
    cube = up(cube, False)
    print("After up counter-clockwise")
    printCube(cube)

def left(cube, clockwise):
    new_cube = deepcopy(cube)
    if not clockwise:
        # update left
        rotateFace(cube, new_cube, 'L', clockwise)
        # update up
        new_cube[0][0][0] = cube[2][0][0]
        new_cube[0][1][0] = cube[2][1][0]
        new_cube[0][2][0] = cube[2][2][0]
        # update  front
        new_cube[2][0][0] = cube[4][0][0]
        new_cube[2][1][0] = cube[4][1][0]
        new_cube[2][2][0] = cube[4][2][0]
        # update down
        new_cube[4][0][0] = cube[5][2][2]
        new_cube[4][1][0] = cube[5][1][2]
        new_cube[4][2][0] = cube[5][0][2]
        # update back
        new_cube[5][0][2] = cube[0][2][0]
        new_cube[5][1][2] = cube[0][1][0]
        new_cube[5][2][2] = cube[0][0][0]
    else:
        # update left
        rotateFace(cube, new_cube, 'L', clockwise)
        # update up
        new_cube[0][0][0] = cube[5][2][2]
        new_cube[0][1][0] = cube[5][1][2]
        new_cube[0][2][0] = cube[5][0][2]
        # update  front
        new_cube[2][0][0] = cube[0][0][0]
        new_cube[2][1][0] = cube[0][1][0]
        new_cube[2][2][0] = cube[0][2][0]
        # update down
        new_cube[4][0][0] = cube[2][0][0]
        new_cube[4][1][0] = cube[2][1][0]
        new_cube[4][2][0] = cube[2][2][0]
        # update back
        new_cube[5][0][2] = cube[4][2][0]
        new_cube[5][1][2] = cube[4][1][0]
        new_cube[5][2][2] = cube[4][0][0]
    return(new_cube)
if TEST:
    print("Original cube")
    printCube(cube)
    cube = left(cube, True)
    print("After left clockwise")
    printCube(cube)
    cube = left(cube, False)
    print("After left counter-clockwise")
    printCube(cube)

def front(cube, clockwise):
    new_cube = deepcopy(cube)
    if not clockwise:
        # update front
        rotateFace(cube, new_cube, 'F', clockwise)
        # update up
        new_cube[0][2][0] = cube[3][0][0]
        new_cube[0][2][1] = cube[3][1][0]
        new_cube[0][2][2] = cube[3][2][0]
        # update  left
        new_cube[1][0][2] = cube[0][2][2]
        new_cube[1][1][2] = cube[0][2][1]
        new_cube[1][2][2] = cube[0][2][0]
        # update down
        new_cube[4][0][0] = cube[1][0][2]
        new_cube[4][0][1] = cube[1][1][2]
        new_cube[4][0][2] = cube[1][2][2]
        # update right
        new_cube[3][0][0] = cube[4][0][2]
        new_cube[3][1][0] = cube[4][0][1]
        new_cube[3][2][0] = cube[4][0][0]
    else:
        # update front
        rotateFace(cube, new_cube, 'F', clockwise)
        # update up
        new_cube[0][2][0] = cube[1][2][2]
        new_cube[0][2][1] = cube[1][1][2]
        new_cube[0][2][2] = cube[1][0][2]
        # update  left
        new_cube[1][0][2] = cube[4][0][0]
        new_cube[1][1][2] = cube[4][0][1]
        new_cube[1][2][2] = cube[4][0][2]
        # update down
        new_cube[4][0][0] = cube[3][2][0]
        new_cube[4][0][1] = cube[3][1][0]
        new_cube[4][0][2] = cube[3][0][0]
        # update right
        new_cube[3][0][0] = cube[0][2][0]
        new_cube[3][1][0] = cube[0][2][1]
        new_cube[3][2][0] = cube[0][2][2]
    return(new_cube)
if TEST:
    print("Original cube")
    printCube(cube)
    cube = front(cube, True)
    print("After front clockwise")
    printCube(cube)
    cube = front(cube, False)
    print("After front counter-clockwise")
    printCube(cube)

def right(cube, clockwise):
    new_cube = deepcopy(cube)
    if not clockwise:
        # update right
        rotateFace(cube, new_cube, 'R', clockwise)
        # update up
        new_cube[0][0][2] = cube[5][2][0]
        new_cube[0][1][2] = cube[5][1][0]
        new_cube[0][2][2] = cube[5][0][0]
        # update  front
        new_cube[2][0][2] = cube[0][0][2]
        new_cube[2][1][2] = cube[0][1][2]
        new_cube[2][2][2] = cube[0][2][2]
        # update down
        new_cube[4][0][2] = cube[2][0][2]
        new_cube[4][1][2] = cube[2][1][2]
        new_cube[4][2][2] = cube[2][2][2]
        # update back
        new_cube[5][0][0] = cube[4][2][2]
        new_cube[5][1][0] = cube[4][1][2]
        new_cube[5][2][0] = cube[4][0][2]
    else:
        # update right
        rotateFace(cube, new_cube, 'R', clockwise)
        # update up
        new_cube[0][0][2] = cube[2][0][2]
        new_cube[0][1][2] = cube[2][1][2]
        new_cube[0][2][2] = cube[2][2][2]
        # update  front
        new_cube[2][0][2] = cube[4][0][2]
        new_cube[2][1][2] = cube[4][1][2]
        new_cube[2][2][2] = cube[4][2][2]
        # update down
        new_cube[4][0][2] = cube[5][2][0]
        new_cube[4][1][2] = cube[5][1][0]
        new_cube[4][2][2] = cube[5][0][0]
        # update back
        new_cube[5][0][0] = cube[0][2][2]
        new_cube[5][1][0] = cube[0][1][2]
        new_cube[5][2][0] = cube[0][0][2]
    return(new_cube)
if TEST:
    print("Original cube")
    printCube(cube)
    cube = right(cube, True)
    print("After right clockwise")
    printCube(cube)
    cube = right(cube, False)
    print("After right counter-clockwise")
    printCube(cube)

def down(cube, clockwise):
    new_cube = deepcopy(cube)
    if not clockwise:
        # update down
        rotateFace(cube, new_cube, 'D', clockwise)
        # update left
        new_cube[1][2][0] = cube[2][2][0]
        new_cube[1][2][1] = cube[2][2][1]
        new_cube[1][2][2] = cube[2][2][2]
        # update  front
        new_cube[2][2][0] = cube[3][2][0]
        new_cube[2][2][1] = cube[3][2][1]
        new_cube[2][2][2] = cube[3][2][2]
        # update right
        new_cube[3][2][0] = cube[5][2][0]
        new_cube[3][2][1] = cube[5][2][1]
        new_cube[3][2][2] = cube[5][2][2]
        # update back
        new_cube[5][2][0] = cube[1][2][0]
        new_cube[5][2][1] = cube[1][2][1]
        new_cube[5][2][2] = cube[1][2][2]
    else:
        # update down
        rotateFace(cube, new_cube, 'D', clockwise)
        # update left
        new_cube[1][2][0] = cube[5][2][0]
        new_cube[1][2][1] = cube[5][2][1]
        new_cube[1][2][2] = cube[5][2][2]
        # update  front
        new_cube[2][2][0] = cube[1][2][0]
        new_cube[2][2][1] = cube[1][2][1]
        new_cube[2][2][2] = cube[1][2][2]
        # update right
        new_cube[3][2][0] = cube[2][2][0]
        new_cube[3][2][1] = cube[2][2][1]
        new_cube[3][2][2] = cube[2][2][2]
        # update back
        new_cube[5][2][0] = cube[3][2][0]
        new_cube[5][2][1] = cube[3][2][1]
        new_cube[5][2][2] = cube[3][2][2]
    return(new_cube)
if TEST:
    print("Original cube")
    printCube(cube)
    cube = down(cube, True)
    print("After down clockwise")
    printCube(cube)
    cube = down(cube, False)
    print("After down counter-clockwise")
    printCube(cube)

def back(cube, clockwise):
    new_cube = deepcopy(cube)
    if not clockwise:
        # update back
        rotateFace(cube, new_cube, 'B', clockwise)
        # update  up
        new_cube[0][0][0] = cube[1][2][0]
        new_cube[0][0][1] = cube[1][1][0]
        new_cube[0][0][2] = cube[1][0][0]
        # update left
        new_cube[1][0][0] = cube[4][2][0]
        new_cube[1][1][0] = cube[4][2][1]
        new_cube[1][2][0] = cube[4][2][2]
        # update right
        new_cube[3][0][2] = cube[0][0][0]
        new_cube[3][1][2] = cube[0][0][1]
        new_cube[3][2][2] = cube[0][0][2]
        # update down
        new_cube[4][2][0] = cube[3][2][2]
        new_cube[4][2][1] = cube[3][1][2]
        new_cube[4][2][2] = cube[3][0][2]
    else:
        # update back
        rotateFace(cube, new_cube, 'B', clockwise)
        # update  up
        new_cube[0][0][0] = cube[3][0][2]
        new_cube[0][0][1] = cube[3][1][2]
        new_cube[0][0][2] = cube[3][2][2]
        # update left
        new_cube[1][0][0] = cube[0][0][2]
        new_cube[1][1][0] = cube[0][0][1]
        new_cube[1][2][0] = cube[0][0][0]
        # update right
        new_cube[3][0][2] = cube[4][2][2]
        new_cube[3][1][2] = cube[4][2][1]
        new_cube[3][2][2] = cube[4][2][0]
        # update down
        new_cube[4][2][0] = cube[1][0][0]
        new_cube[4][2][1] = cube[1][1][0]
        new_cube[4][2][2] = cube[1][2][0]
    return(new_cube)
if TEST:
    print("Original cube")
    printCube(cube)
    cube = back(cube, True)
    print("After back clockwise")
    printCube(cube)
    cube = back(cube, False)
    print("After back counter-clockwise")
    printCube(cube)

for move in moves:
    if move == "F":
        cube = front(cube, True)
    elif move == "F'":
        cube = front(cube, False)
    elif move == "L":
        cube = left(cube, True)
    elif move == "L'":
        cube = left(cube, False)
    elif move == "R":
        cube = right(cube, True)
    elif move == "R'":
        cube = right(cube, False)
    elif move == "U":
        cube = up(cube, True)
    elif move == "U'":
        cube = up(cube, False)
    elif move == "D":
        cube = down(cube, True)
    elif move == "D'":
        cube = down(cube, False)
    elif move == "B":
        cube = back(cube, True)
    elif move == "B'":
        cube = back(cube, False)
    else:
        print("Error: no move for", move)

total = 1
for y in range(3):
    for x in range(3):
        total *= cube[faces['F']][y][x]
print("Final front face product is", total)
