with open('inputs/Day9.txt', 'r') as pz:
    lines = pz.read().splitlines()

ROWS = 100
COLUMNS = 100


def checkPoint(up, down, left, right, row, col):
    number = int(lines[i][j])
    points = []
    check = True
    if up:
        points.append(int(lines[row-1][col]))
    if down:
        points.append(int(lines[row+1][col]))
    if left:
        points.append(int(lines[row][col-1]))
    if right:
        points.append(int(lines[row][col+1]))

    for point in points:
        if number >= point:
            check = False

    if check:
        return number + 1
    else:
        return 0


solution = 0
for i in range(ROWS):
    for j in range(COLUMNS):
        print(i, j, lines[i][j])
        if (i == 0) and (j == 0):
            solution += checkPoint(False, True, False, True, i, j)
        elif (i == 0) and (j == COLUMNS-1):
            solution += checkPoint(False, True, True, False, i, j)
        elif (i == ROWS-1) and (j == 0):
            solution += checkPoint(True, False, False, True, i, j)
        elif (i == ROWS-1) and (j == COLUMNS-1):
            solution += checkPoint(True, False, True, False, i, j)
        elif (i == 0):
            solution += checkPoint(False, True, True, True, i, j)
        elif (j == 0):
            solution += checkPoint(True, True, False, True, i, j)
        elif (i == ROWS-1):
            solution += checkPoint(True, False, True, True, i, j)
        elif (j == COLUMNS-1):
            solution += checkPoint(True, True, True, False, i, j)
        else:
            solution += checkPoint(True, True, True, True, i, j)

print(solution)
