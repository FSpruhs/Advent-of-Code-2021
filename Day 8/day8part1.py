with open('inputs/Day8.txt', 'r') as pz:
    lines = pz.read().splitlines()
    newLine = []
    for line in lines:
        newLine.append(line.split(' | '))

code = []
newCode = []
count = 0
for line in range(len(newLine)):
    code.append(newLine[line][1].split(' '))

for i in range(len(code)):
    for j in range(4):
        newCode.append(code[i][j])

for element in newCode:
    if (len(element) == 2) or (len(element) == 4) or (len(element) == 3) or\
         (len(element) == 7):
        count += 1

print(count)
