def findOneFourSevenEight(decode):
    global one, seven, four, eight
    for i in decode:
        if len(i) == 2:
            one = i
        if len(i) == 3:
            seven = i
        if len(i) == 4:
            four = i
        if len(i) == 7:
            eight = i
    decode.remove(one)
    decode.remove(seven)
    decode.remove(four)
    decode.remove(eight)
    return decode


def findThree(decode):
    global three, one
    for i in decode:
        if (len(i) == 5) and (one[0] in i) and (one[1] in i):
            three = i
    decode.remove(three)
    return decode


def findNine(decode):
    global nine, seven, four
    for i in decode:
        if (len(i) == 6) and (seven[0] in i) and (seven[1] in i) and\
                         (seven[2] in i) and (four[0] in i) and\
                         (four[1] in i) and (four[2] in i) and\
                         (four[3] in i):
            nine = i
    decode.remove(nine)
    return decode


def findTwo(decode, leftBottom):
    global two
    for i in decode:
        if (len(i) == 5) and (leftBottom in i):
            two = i
    decode.remove(two)
    return decode


def findFive(decode):
    global five
    for i in decode:
        if (len(i) == 5):
            five = i
    decode.remove(five)
    return decode


def findZero(decode):
    global zero, seven
    for i in decode:
        if (seven[0] in i) and (seven[1] in i) and (seven[2] in i):
            zero = i
    decode.remove(zero)
    return decode


def findLeftBottom():
    global eight, nine
    leftBottom = ''
    for i in eight:
        if i not in nine:
            leftBottom = i
    return leftBottom


def decodeCode(code):
    global zero, one, two, three, four, five, six, seven, eight, nine
    solution = ''
    for i in code:
        if (len(i) == 6) and (zero[0] in i) and (zero[1] in i) and\
           (zero[2] in i) and\
           (zero[3] in i) and (zero[4] in i) and (zero[5] in i):
            solution += '0'
        elif len(i) == 2:
            solution += '1'
        elif (len(i) == 5) and (two[0] in i) and (two[1] in i) and\
             (two[2] in i) and\
             (two[3] in i) and (two[4] in i):
            solution += '2'
        elif (len(i) == 5) and (three[0] in i) and (three[1] in i) and\
             (three[2] in i) and (three[3] in i) and (three[4] in i):
            solution += '3'
        elif len(i) == 4:
            solution += '4'
        elif (len(i) == 5) and (five[0] in i) and (five[1] in i) and\
             (five[2] in i) and\
             (five[3] in i) and (five[4] in i):
            solution += '5'
        elif (len(i) == 6) and (six[0] in i) and (six[1] in i) and\
             (six[2] in i) and\
             (six[3] in i) and (six[4] in i) and (six[5] in i):
            solution += '6'
        elif len(i) == 3:
            solution += '7'
        elif len(i) == 7:
            solution += '8'
        else:
            solution += '9'
    return int(solution)


with open('inputs/Day8.txt', 'r') as pz:
    lines = pz.read().splitlines()
summe = 0
for i in range(len(lines)):
    line = lines[i].split(' | ')
    decode, code = line[0], line[1]
    decode = decode.split(' ')
    code = code.split(' ')

    zero = ''
    one = ''
    two = ''
    three = ''
    four = ''
    five = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''

    decode = findOneFourSevenEight(decode)
    decode = findThree(decode)
    decode = findNine(decode)
    leftBottom = findLeftBottom()
    decode = findTwo(decode, leftBottom)
    decode = findFive(decode)
    decode = findZero(decode)
    six = decode[0]
    number = decodeCode(code)
    summe += number
print(summe)
