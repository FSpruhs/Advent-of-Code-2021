with open('Day 2/puzzle.txt', 'r') as pz:
    lines = pz.read().split('\n')


depth = 0
horizontal = 0
aim = 0

for line in lines:
    splitLine = line.split()
    if splitLine[0] == 'forward':
        horizontal += int(splitLine[1])
        depth += aim * int(splitLine[1])
    elif splitLine[0] == 'down':
        aim += int(splitLine[1])
    elif splitLine[0] == 'up':
        aim -= int(splitLine[1])

print(horizontal, depth, horizontal*depth)
