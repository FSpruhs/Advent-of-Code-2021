with open('inputs/Day5.txt', 'r') as pz:
    lines = pz.read().splitlines()


points = {}
for line in lines:
    left, right = line.split(' -> ')
    x1, y1 = left.split(',')
    x2, y2 = right.split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            points[(i, x1)] = points.get((i, x1), 0) + 1

    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            points[(y1, i)] = points.get((y1, i), 0) + 1

solution = 0
for i in points.items():
    if i[1] >= 2:
        solution += 1

print((solution))
