with open('inputs/Day3.txt', 'r') as pz:
    lines = pz.read().split('\n')

gamma = ""
epsilon = ""

for position in range(0, 12):
    counterOne = 0
    counterZero = 0
    for line in lines:
        if line[position] == '1':
            counterOne += 1
        else:
            counterZero += 1
    if counterOne > counterZero:
        gamma += '1'
    else:
        gamma += '0'

for number in range(0, 12):
    if gamma[number] == '1':
        epsilon += '0'
    else:
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))
