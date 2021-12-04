with open('inputs/Day4.txt', 'r') as pz:
    lines = pz.read().split('\n')


class Board:
    def __init__(self):
        self.playboard = [[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]]

    def createBoard(self, rows):
        run = 0
        for i in range(5):
            for j in range(5):
                self.playboard[i][j] = int(rows[run])
                run += 1

    def printBoard(self):
        for row in range(5):
            print(self.playboard[row])

    def setNumber(self, number):
        for i in range(5):
            for j in range(5):
                if number == self.playboard[i][j]:
                    self.playboard[i][j] = 'X'

    def checkBoard(self):
        return self.checkCol() or self.checkRow()

    def checkCol(self):
        for i in range(5):
            if (self.playboard[0][i] == 'X') and \
               (self.playboard[1][i] == 'X') and \
               (self.playboard[2][i] == 'X') and \
               (self.playboard[3][i] == 'X') and \
               (self.playboard[4][i] == 'X'):
               return True
        return False

    def checkRow(self):
        for i in range(5):
            if (self.playboard[i][0] == 'X') and \
               (self.playboard[i][1] == 'X') and \
               (self.playboard[i][2] == 'X') and \
               (self.playboard[i][3] == 'X') and \
               (self.playboard[i][4] == 'X'):
               return True
        return False

    def calcAOCScore(self, number):
        score = 0
        for i in range(5):
            for j in range(5):
                if self.playboard[i][j] != 'X':
                    score += self.playboard[i][j]
        return score * number


class Match:
    def __init__(self, board):
        self.board = board

    def play(self, turns):
        matchTurn = 0
        for turn in range(len(turns)):
            if not self.board.checkBoard():
                self.board.setNumber(turns[turn])
                matchTurn += 1
            else:
                score = self.board.calcAOCScore(turns[turn-1])
                return matchTurn, score

    def playAOCScore(self, turns, turnBefore):
        for turn in range(turnBefore):
            self.board.setNumber(turns[turn])
        return self.board.calcAOCScore(turns[turn-1])


numbersDrawn = lines[0].split(',')
numbersDrawn = list(map(int, numbersDrawn))
finalScore = 0
finalTurn = 0
for line in range(2, len(lines), 6):
    row1 = lines[line].split()
    row2 = lines[line + 1].split()
    row3 = lines[line + 2].split()
    row4 = lines[line + 3].split()
    row5 = lines[line + 4].split()
    rows = row1 + row2 + row3 + row4 + row5
    board = Board()
    board.createBoard(rows)
    match = Match(board)
    turn, score = match.play(numbersDrawn)
    if turn > finalTurn:
        turnBefore = finalTurn
        finalTurn = turn
        finalScore = score
        matchNumber = line


row1 = lines[matchNumber].split()
row2 = lines[matchNumber + 1].split()
row3 = lines[matchNumber + 2].split()
row4 = lines[matchNumber + 3].split()
row5 = lines[matchNumber + 4].split()
rows = row1 + row2 + row3 + row4 + row5
board = Board()
board.createBoard(rows)
match = Match(board)
print(match.playAOCScore(numbersDrawn, turnBefore))
print(match.play(numbersDrawn))
