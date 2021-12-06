with open('inputs/Day6.txt', 'r') as pz:
    lines = list(map(int, pz.read().split(',')))

DAYS = 256

lanternfish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for number in lines:
    lanternfish[number] += 1

for day in range(DAYS):
    lanternfishNew = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in lanternfish.keys():
        lanternfishNew[fish-1] = lanternfish[fish]
    for fish in lanternfishNew:
        if fish == -1:
            lanternfishNew[8] = lanternfishNew[-1]
            lanternfishNew[6] += lanternfishNew[-1]
    del lanternfishNew[-1]
    lanternfish = lanternfishNew

solution = 0
for fish in lanternfish:
    solution += lanternfish[fish]

print(solution)
