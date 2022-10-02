import os
# a basic tic tac toe game
board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#function for show board

def show_board(board):
    print("+---+---+---+")
    print("| ", end="")
    print(board[0][0], board[0][1], board[0][2], sep=" | ", end="")
    print(" | ")
    print("+---+---+---+")
    print("| ", end="")
    print(board[1][0], board[1][1], board[1][2], sep=" | ", end="")
    print(" | ")
    print("+---+---+---+")
    print("| ", end="")
    print(board[2][0], board[2][1], board[2][2], sep=" | ", end="")
    print(" | ")
    print("+---+---+---+")

    #function for winnner state
    
def winstates(board):
    if (board[0][0]==0 and board[0][1]==0 and board[0][2]==0) or (board[1][0]==0 and board[1][1]==0 and board[1][2]==0) or (board[2][0]==0 and board[2][1]==0 and board[2][2]==0) or (board[0][0]==0 and board[1][0]==0 and board[2][0]==0) or (board[0][1]==0 and board[1][1]==0 and board[2][1]==0) or (board[0][2]==0 and board[1][2]==0 and board[2][2]==0) or (board[0][0]==0 and board[1][1]==0 and board[2][2]==0) or (board[0][2]==0 and board[1][1]==0 and board[2][0]==0):
        return 1
    elif (board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X') or (board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X') or (board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X') or (board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X') or (board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X') or (board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X') or (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X') or (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='x'):
        return 1
    else:
        return 0

def play(board):
    i=0
    while i < 9: 
        x=input("position: ")
        if int(x) == 1:
            if i%2==0:
                if (board[2][0] == " "):
                    board[2][0] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[2][0] == " "):
                    board[2][0] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        elif int(x) == 2:
            if i%2==0:
                if (board[2][1] == " "):
                    board[2][1] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[2][1] == " "):
                    board[2][1] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        elif int(x) == 3:
            if i%2==0:
                if (board[2][2] == " "):
                    board[2][2] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[2][2] == " "):
                    board[2][2] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        elif int(x) == 4:
            if i%2==0:
                if (board[1][0] == " "):
                    board[1][0] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[1][0] == " "):
                    board[1][0] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        elif int(x) == 5:
            if i%2==0:
                if (board[1][1] == " "):
                    board[1][1] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[1][1] == " "):
                    board[1][1] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        elif int(x) == 6:
            if i%2==0:
                if (board[1][2] == " "):
                    board[1][2] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[1][2] == " "):
                    board[1][2] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        elif int(x) == 7:
            if i%2==0:
                if (board[0][0] == " "):
                    board[0][0] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[0][0] == " "):
                    board[0][0] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        elif int(x) == 8:
            if i%2==0:
                if (board[0][1] == " "):
                    board[0][1] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[0][1] == " "):
                    board[0][1] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        elif int(x) == 9:
            if i%2==0:
                if (board[0][2] == " "):
                    board[0][2] = 0
                else:
                    print("Invalid move! Try again")
                    i=i-1
            else:
                if (board[0][2] == " "):
                    board[0][2] = 'X'
                else:
                    print("Invalid move! Try again")
                    i=i-1
        else:
            print("Invalid Position! Try again")
            i=i-1
        i=i+1
        os.system("cls" if os.name=='nt' else "clear")
        show_board(board)
        if winstates(board):
            print("GAME OVER!")
            break

show_board(board)
play(board)
