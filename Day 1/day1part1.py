with open('part1.txt', 'r') as pz:
    lines = pz.read().split('\n')
lines = list(map(int, lines))
solution = 0

for value in range(len(lines) - 3):
    solution += 1


print((solution))
print(len(lines) - 3)
