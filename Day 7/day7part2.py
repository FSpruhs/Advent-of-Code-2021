with open('inputs/Day7.txt', 'r') as pz:
    lines = list(map(int, pz.read().split(',')))

finalFuel = 0
for position in range(max(lines)):
    fuel = 0
    for submarine in lines:
        fuel += (abs(submarine - position) *
        (abs(submarine - position) + 1)) // 2

    if (fuel < finalFuel) or finalFuel == 0:
        finalFuel = fuel

print(finalFuel)
