with open('inputs/Day6.txt', 'r') as pz:
    lines = list(map(int, pz.read().split(',')))

DAYS = 256

for i in range(DAYS):
    for j in range(len(lines)):
        if lines[j] != 0:
            lines[j] -= 1
        else:
            lines[j] = 6
            lines.append(8)

print(len(lines))
