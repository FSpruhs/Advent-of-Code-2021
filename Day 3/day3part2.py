with open('inputs/Day3.txt', 'r') as pz:
    lines = pz.read().split('\n')


def findMostCommon(lines, position):
    counterOne = 0
    counterZero = 0
    for line in lines:
        if line[position] == '1':
            counterOne += 1
        else:
            counterZero += 1
    if counterOne > counterZero:
        return '1'
    elif counterOne < counterZero:
        return '0'
    elif counterOne == counterZero:
        return '1'


def findMostUncommon(lines, position):
    counterOne = 0
    counterZero = 0
    for line in lines:
        if line[position] == '1':
            counterOne += 1
        else:
            counterZero += 1
    if counterOne < counterZero:
        return '1'
    elif counterOne > counterZero:
        return '0'
    elif counterOne == counterZero:
        return '0'


def deleteValues(lines, mostCommon, position):
    newLines = []
    for line in lines:
        if mostCommon == line[position]:
            newLines.append(line)
    return newLines


oxygen = lines
position = 0
while len(oxygen) > 1:
    mostCommon = findMostCommon(oxygen, position)
    oxygen = deleteValues(oxygen, mostCommon, position)
    position += 1

co2 = lines
position = 0
while len(co2) > 1:
    mostUncommon = findMostUncommon(co2, position)
    co2 = deleteValues(co2, mostUncommon, position)
    position += 1


print(int(oxygen[0], 2) * int(co2[0], 2))
