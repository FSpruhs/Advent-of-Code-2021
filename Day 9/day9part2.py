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
        return True
    else:
        return False


for i in range(ROWS):
    for j in range(COLUMNS):
        lowPoint = False
        if (i == 0) and (j == 0):
            lowPoint += checkPoint(False, True, False, True, i, j)
        elif (i == 0) and (j == COLUMNS-1):
            lowPoint += checkPoint(False, True, True, False, i, j)
        elif (i == ROWS-1) and (j == 0):
            lowPoint += checkPoint(True, False, False, True, i, j)
        elif (i == ROWS-1) and (j == COLUMNS-1):
            lowPoint += checkPoint(True, False, True, False, i, j)
        elif (i == 0):
            lowPoint += checkPoint(False, True, True, True, i, j)
        elif (j == 0):
            lowPoint += checkPoint(True, True, False, True, i, j)
        elif (i == ROWS-1):
            lowPoint += checkPoint(True, False, True, True, i, j)
        elif (j == COLUMNS-1):
            lowPoint += checkPoint(True, True, True, False, i, j)
        else:
            lowPoint += checkPoint(True, True, True, True, i, j)
        if lowPoint:
            print(i, j)


