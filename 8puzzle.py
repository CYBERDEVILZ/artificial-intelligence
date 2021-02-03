#try to solve the puzzle

puzzle=[[1, 2, 3], [4, 5, 6], [7, 0, 8]]
def zeroindex(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                k=i
                l=j
    return(k,l)

def show_board(puzzle):
    for i in range(3):
        for j in range(3):
            if j != 2:
                print("{}".format(puzzle[i][j]), end=' | ')
            else:
                print("{} | ".format(puzzle[i][j]), end='\n')

def check(puzzle):
    count=0
    for i in range(3):
        for j in range(3):
            x = puzzle[i][j]
            o=j+1
            for k in range(i, 3):
                for l in range(o, 3):
                    y = puzzle[k][l]
                    if x>y and x!=0 and y!=0:
                        count+=1
                o=0
    if (not count%2):
        print("solvable!")
        print(count)
    else:
        print("non solvable!")
        print(count)

def play(puzzle, k, l):
    print("press w for up, a for left, d for right, s for down")
    solved = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    while puzzle != solved:
        x=input("input: ")
        if x=='w':
            if k>0:
                puzzle[k][l] = puzzle[k-1][l]
                puzzle[k-1][l] = 0
                k=k-1
            else:
                print("move not valid!")
        
        if x=='s':
            if k<2:
                puzzle[k][l] = puzzle[k+1][l]
                puzzle[k+1][l] = 0
                k=k+1
            else:
                print("move not valid!")

        if x=='a':
            if l>0:
                puzzle[k][l] = puzzle[k][l-1]
                puzzle[k][l-1] = 0
                l=l-1
            else:
                print("move not valid!")

        if x=='d':
            if l<2:
                puzzle[k][l] = puzzle[k][l+1]
                puzzle[k][l+1] = 0
                l=l+1
            else:
                print("move not valid!")

        show_board(puzzle)
    print("board solved!!")

(k,l) = zeroindex(puzzle)
show_board(puzzle)
check(puzzle)
play(puzzle, k, l)
