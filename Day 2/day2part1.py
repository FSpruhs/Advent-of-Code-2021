with open('inputs/Day2.txt', 'r') as pz:
    lines = pz.read().split('\n')


depth = 0
horizontal = 0

for line in lines:
    splitLine = line.split()
    if splitLine[0] == 'forward':
        horizontal += int(splitLine[1])
    elif splitLine[0] == 'down':
        depth += int(splitLine[1])
    elif splitLine[0] == 'up':
        depth -= int(splitLine[1])

print(horizontal, depth, horizontal*depth)
