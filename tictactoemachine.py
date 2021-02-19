import random
board=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

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

def winstates(board):
    if (board[0][0]==0 and board[0][1]==0 and board[0][2]==0) or (board[1][0]==0 and board[1][1]==0 and board[1][2]==0) or (board[2][0]==0 and board[2][1]==0 and board[2][2]==0) or (board[0][0]==0 and board[1][0]==0 and board[2][0]==0) or (board[0][1]==0 and board[1][1]==0 and board[2][1]==0) or (board[0][2]==0 and board[1][2]==0 and board[2][2]==0) or (board[0][0]==0 and board[1][1]==0 and board[2][2]==0) or (board[0][2]==0 and board[1][1]==0 and board[2][0]==0):
        return 'h'
    elif (board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X') or (board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X') or (board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X') or (board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X') or (board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X') or (board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X') or (board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X') or (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='x'):
        return 'm'
    else:
        return 0

def machplay(board, p):
    flag=0
    glag=0
    gulag=0
    x=[]
    if board[1][1] ==' ':
        board[1][1] = 'X'
    else:
        if p < 1:
            if board[0][0] ==' ':
                x.append(1)
            if board[0][2] == ' ':
                x.append(2)
            if board[2][0] == ' ':
                x.append(3)
            if board[2][2] == ' ':
                x.append(4)
            y=random.randint(0, len(x)-1)
            a=x[y]
            if a==1:
                board[0][0] = 'X'
            elif a==2:
                board[0][2] = 'X'
            elif a==3:
                board[2][0] = 'X'
            else:
                board[2][2] = 'X'
        
        else:
            for b in range(3):
                for c in range(3):
                    if board[b][c] == ' ':
                        board[b][c] = 'X'
                        if winstates(board)=='m':
                            flag=1
                            break
                        else:
                            board[b][c] = ' '
                if flag==1:
                    break
            if flag==0:
                for d in range(3):
                    for e in range(3):
                        if board[d][e] == ' ':
                            board[d][e] = 0
                            if winstates(board)=='h':
                                board[d][e] = 'X'
                                glag=1
                                break
                            else:
                                board[d][e] = ' '
                    if glag==1:
                        break
            
            if flag ==0 and glag==0:
                for f in range(3):
                    for g in range(3):
                        if board[f][g] == ' ':
                            board[f][g] = 'X'
                            gulag=1
                            break
                    if gulag==1:
                        break

def play(board):
    i=0
    p=0
    while i < 5:
        show_board(board)
        x=input("position: ")
        if int(x) == 1:
            if board[2][0] == " ":
                board[2][0] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        elif int(x) == 2:
            if board[2][1] == " ":
                board[2][1] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        elif int(x) == 3:
            if board[2][2] == " ":
                board[2][2] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        elif int(x) == 4:
            if board[1][0] == " ":
                board[1][0] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        elif int(x) == 5:
            if board[1][1] == " ":
                board[1][1] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        elif int(x) == 6:
            if board[1][2] == " ":
                board[1][2] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        elif int(x) == 7:
            if board[0][0] == " ":
                board[0][0] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        elif int(x) == 8:
            if board[0][1] == " ":
                board[0][1] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        elif int(x) == 9:
            if board[0][2] == " ":
                board[0][2] = 0
                show_board(board)
            else:
                print("Invalid Move!")
                continue
        else:
            print("Invalid Position!")
            continue
        i+=1
        if i < 5:
            if winstates(board) == 'h':
                break
            machplay(board, p)
            p+=1
            if winstates(board) == 'm':
                break
    show_board(board)
        


play(board)
