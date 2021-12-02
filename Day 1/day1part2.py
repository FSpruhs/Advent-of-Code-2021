with open('part2.txt', 'r') as pz:
    lines = pz.read().split('\n')
lines = list(map(int, lines))
solution = 0


for count in range(1, len(lines) - 2):
    sum1, sum2 = (0, 0)
    sum1 = lines[count-1] + lines[count] + lines[count+1]
    sum2 = lines[count] + lines[count+1] + lines[count+2]
    print(sum1, sum2)
    if sum1 < sum2:
        solution += 1

print(solution)
