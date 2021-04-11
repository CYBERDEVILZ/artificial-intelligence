import os

puzzle = [1, 0, 3, 4, 2, 5, 7, 8, 6]
solved = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def check(puzzle):
    count=0
    for i in range(9):
        for j in range(i+1, 9):
            if j==9:
                break
            if puzzle[i]>puzzle[j] and puzzle[i]!=0 and puzzle[j]!=0:
                count+=1
    if (not count%2):
        return True
    else:
        return False

def zeroindex(puzzle):
    for i in range(9):
        if puzzle[i] == 0:
            return i
            break

def show_board(puzzle):
            print("""\n+---+---+---+
| {} | {} | {} |
+---+---+---+
| {} | {} | {} |
+---+---+---+
| {} | {} | {} |
+---+---+---+""".format(puzzle[0], puzzle[1], puzzle[2], puzzle[3], puzzle[4], puzzle[5], puzzle[6], puzzle[7], puzzle[8]))

def userplay(puzzle):
    print("\nPress W to swap UP, A to swap left, D to swap right and S to swap down")
    show_board(puzzle)
    while puzzle != solved:
        x = input("\nEnter your choice: ")
        index = zeroindex(puzzle)
        if x.lower() == 'w':
            if index - 3 < 0:
                os.system("cls")
                show_board(puzzle)
                print("\nINVALID MOVE")
            else:
                puzzle[index], puzzle[index-3] = puzzle[index-3], puzzle[index]
                os.system("cls")
                show_board(puzzle)
        
        elif x.lower() == 'a':
            if index % 3 == 0:
                os.system("cls")
                show_board(puzzle)
                print("\nINVALID MOVE")
            else:
                puzzle[index], puzzle[index-1] = puzzle[index-1], puzzle[index]
                os.system("cls")
                show_board(puzzle)

        elif x.lower() == 's':
            if index + 3 > 8:
                os.system("cls")
                show_board(puzzle)
                print("\nINVALID MOVE")
            else:
                puzzle[index], puzzle[index+3] = puzzle[index+3], puzzle[index]
                os.system("cls")
                show_board(puzzle)

        elif x.lower() == 'd':
            if index % 3 == 2:
                os.system("cls")
                show_board(puzzle)
                print("\nINVALID MOVE")
            else:
                puzzle[index], puzzle[index+1] = puzzle[index+1], puzzle[index]
                os.system("cls")
                show_board(puzzle)
        
        else:
            os.system("cls")
            show_board(puzzle)
            print("\nINVALID MOVE")
    
    print("\nCONGRATULATIONS!! YOU HAVE SOLVED THE PUZZLE!!\n")


userplay(puzzle)
