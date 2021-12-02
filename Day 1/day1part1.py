with open('inputs/Day1.txt', 'r') as pz:
    lines = pz.read().split('\n')
lines = list(map(int, lines))
solution = 0

for key, value in enumerate(lines):
    if key != 0:
        if lines[key] > lines[key-1]:
            solution += 1


print((solution))
