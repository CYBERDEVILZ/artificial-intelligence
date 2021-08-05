# imports
import math
import os

# Global variables
huPlayer = 'O'
aiPlayer = 'X'
inValidEntry = False
running = True
gameover = False
who = "ai"
realBoard = [
    [" ", " ", " ", ],
    [" ", " ", " ", ],
    [" ", " ", " ", ]
]


# helping functions
def inputHandler():
    choice = int(input("position: "))
    print('\n')
    global inValidEntry
    inValidEntry = False
    play = Game()
    play.turn(huPlayer, choice-1)

    if play.checkWin(huPlayer):
        play.gameOver(huPlayer)

    elif (not play.gameDraw() and not inValidEntry):
        play.aiPlays(realBoard)
        if play.checkWin(aiPlayer):
            play.gameOver(aiPlayer)

    elif play.gameDraw():
        play.gameOver("no one")


# Classes
class Board:
    def __init__(self):
        self.realBoard = realBoard
        self.invalidEntry = False

    def generate(self):

        print("+---+---+---+")
        print("| ", end="")
        print(realBoard[0][0], realBoard[0][1], realBoard[0][2], sep=" | ", end="")
        print(" | ")
        print("+---+---+---+")
        print("| ", end="")
        print(realBoard[1][0], realBoard[1][1], realBoard[1][2], sep=" | ", end="")
        print(" | ")
        print("+---+---+---+")
        print("| ", end="")
        print(realBoard[2][0], realBoard[2][1], realBoard[2][2], sep=" | ", end="")
        print(" | ")
        print("+---+---+---+")

    def prompt(self):
        answer = input("\nDo you like to play more? (Y/N): ")
        print("")
        if(answer.lower() == "y"):
            return True
        else:
            return False

    def resetGame(self):
        global realBoard
        realBoard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def emptySquares(self):
        for i in range(3):
            for j in range(3):
                if(realBoard[i][j] == " "):
                    return True
        return False


class Game(Board):
    def __init__(self):
        super().__init__()
        self.bestScore = -100000
        self.bestMove = [0, 0]
        self.alpha = -100000
        self.beta = 100000

    def turn(self, player, square):
        row = 2 - math.floor(square / 3)
        col = square % 3
        if square<9 and square>0:

            if realBoard[row][col] == " ":
                realBoard[row][col] = player

        else:
            global inValidEntry
            inValidEntry = True
            print("Invalid Entry. Try again!")

    def checkWin(self, player):
        if((player == aiPlayer) and ((realBoard[0][0] == 'X' and realBoard[0][1] == 'X' and realBoard[0][2] == 'X') or (realBoard[1][0] == 'X' and realBoard[1][1] == 'X' and realBoard[1][2] == 'X') or (realBoard[2][0] == 'X' and realBoard[2][1] == 'X' and realBoard[2][2] == 'X') or (realBoard[2][0] == 'X' and realBoard[1][0] == 'X' and realBoard[0][0] == 'X') or (realBoard[2][1] == 'X' and realBoard[1][1] == 'X' and realBoard[0][1] == 'X') or (realBoard[2][2] == 'X' and realBoard[1][2] == 'X' and realBoard[0][2] == 'X') or (realBoard[2][2] == 'X' and realBoard[1][1] == 'X' and realBoard[0][0] == 'X') or (realBoard[2][0] == 'X' and realBoard[1][1] == 'X' and realBoard[0][2] == 'X'))):
            return True

        if((player == huPlayer) and ((realBoard[0][0] == 'O' and realBoard[0][1] == 'O' and realBoard[0][2] == 'O') or (realBoard[1][0] == 'O' and realBoard[1][1] == 'O' and realBoard[1][2] == 'O') or (realBoard[2][0] == 'O' and realBoard[2][1] == 'O' and realBoard[2][2] == 'O') or (realBoard[2][0] == 'O' and realBoard[1][0] == 'O' and realBoard[0][0] == 'O') or (realBoard[2][1] == 'O' and realBoard[1][1] == 'O' and realBoard[0][1] == 'O') or (realBoard[2][2] == 'O' and realBoard[1][2] == 'O' and realBoard[0][2] == 'O') or (realBoard[2][2] == 'O' and realBoard[1][1] == 'O' and realBoard[0][0] == 'O') or (realBoard[2][0] == 'O' and realBoard[1][1] == 'O' and realBoard[0][2] == 'O'))):
            return True

        return False

    def gameOver(self, player):
        global who
        if(player == huPlayer):
            who = "hu"
        elif(player == aiPlayer):

            who = "ai"
        elif(player == "no one"):

            who = "none"
        global gameover
        gameover = True

    def gameDraw(self):
        for squares in realBoard:
            for square in squares:
                if(square == " "):
                    return False

        return True

    def aiPlays(self, board):
        self.bestScore = -100000
        self.bestMove = [0, 0]
        self.alpha = -100000
        self.beta = 100000
        for i in range(3):
            for j in range(3):
                if realBoard[i][j] == " ":
                    realBoard[i][j] = "X"
                    self.score = self.minimax(
                        0, False, self.alpha, self.beta)
                    realBoard[i][j] = " "
                    if self.score > self.bestScore:
                        self.bestScore = self.score
                        self.bestMove[0] = i
                        self.bestMove[1] = j

        realBoard[self.bestMove[0]][self.bestMove[1]] = "X"

    def minimax(self, depth, maximize, alpha, beta):
        self.result = "a"
        if(self.checkWin(aiPlayer)):
            self.result = 10
            return 10 - depth

        elif(self.checkWin(huPlayer)):
            self.result = 10
            return -10 + depth

        elif(self.result == "a" and not self.emptySquares()):
            self.result = 0
            return 0

        if(maximize):
            newBestScore = -100000
            self.flag = 0
            for i in range(3):
                for j in range(3):
                    if realBoard[i][j] == " ":
                        realBoard[i][j] = "X"
                        newScore = self.minimax(
                            depth + 1, False, self.alpha, self.beta)
                        realBoard[i][j] = " "
                        newBestScore = max(newBestScore, newScore)
                        self.alpha = max(self.alpha, newBestScore)
                        # if(self.beta <= self.alpha):
                        #     self.flag = 1
                        #     break
                # if(self.flag):
                #     break

            return newBestScore

        else:
            newBestScore = 100000
            self.nflag = 0
            for i in range(3):
                for j in range(3):
                    if realBoard[i][j] == " ":
                        realBoard[i][j] = "O"
                        newScore = self.minimax(
                            depth + 1, True, self.alpha, self.beta)
                        realBoard[i][j] = " "
                        newBestScore = min(newBestScore, newScore)
                        self.beta = min(self.beta, newBestScore)
                        # if(self.beta <= self.alpha):
                        #     self.nflag = 1
                        #     break
                # if(self.nflag):
                #     break

            return newBestScore


play = Game()
board = Board()


while(running):
    gameover = False
    play.generate()
    inputHandler()
    # os.system("cls")
    # print(realBoard)
    if(gameover):
        play.generate()
        if(who == "hu"):
            print(
                "\t\nTHE HUMAN HAS WON!! Wait.. How is that even possible!? Your code's buggy then")
        elif(who == "ai"):
            print(
                "\t\nTHE A.I. HAS WON!! Better Luck Next Time\t\n")

        elif(who == "none"):
            print("\t\nGood! You managed to DRAW with the A.I.\t\n")
        running = play.prompt()
        play.resetGame()
