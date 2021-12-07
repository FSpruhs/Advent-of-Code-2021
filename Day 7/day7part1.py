import statistics

with open('inputs/Day7.txt', 'r') as pz:
    lines = list(map(int, pz.read().split(',')))

median = statistics.median(lines)
solution = 0
for submarine in lines:
    solution += abs(submarine - median)

print(solution)
