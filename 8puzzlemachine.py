import copy
puzzle=[[1, 2, 3], [5, 6, 0], [7, 8, 4]]

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
        return True
    else:
        return False

def machineplay(puzzle):
    solved = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    openlist=[]
    closedlist=[]
    openlist.append(puzzle)
    x=[]
    i=0
    x=openlist.pop(0)
    y=x
    a=x[3]
    b=x[4]
    while y[0:3] != solved:
        if a>0:                                               #up
            statespace1 = copy.deepcopy(y)
            temp = statespace1[a][b]
            statespace1[a][b] = statespace1[a-1][b]
            statespace1[a-1][b] = temp
            statespace1[3] = (a-1)
            statespace1[4] = (b)
            statespace1.append("UP")
            if statespace1[0:3] == solved:
                print(statespace1[0:3])
                print(statespace1[5:])
                break            
            if statespace1 not in closedlist:
                openlist.append(statespace1)
                print(statespace1[0:3], "ss1")

        if a<2:                                                 #down
            statespace2 = copy.deepcopy(y)
            temp = statespace2[a][b]
            statespace2[a][b] = statespace2[a+1][b]
            statespace2[a+1][b] = temp
            statespace2[3] = (a+1)
            statespace2[4] = (b)
            statespace2.append("DOWN")
            if statespace2[0:3] == solved:
                print(statespace2[0:3])
                print(statespace2[5:])
                break
            if statespace2 not in closedlist:
                openlist.append(statespace2)
                print(statespace2[0:3], "ss2")

        if b>0:                                                 #left
            statespace3 = copy.deepcopy(y)
            temp = statespace3[a][b]
            statespace3[a][b] = statespace3[a][b-1]
            statespace3[a][b-1] = temp          
            statespace3[3] = (a)
            statespace3[4] = (b-1)
            statespace3.append("LEFT")
            if statespace3[0:3] == solved:
                print(statespace3[0:3])
                print(statespace3[5:])
                break  
            if statespace3 not in closedlist:
                openlist.append(statespace3)
                print(statespace3[0:3], "ss3")

        if b<2:                                                 #right
            statespace4 = copy.deepcopy(y)
            temp = statespace4[a][b]
            statespace4[a][b] = statespace4[a][b+1]
            statespace4[a][b+1] = temp
            statespace4[3] = (a)
            statespace4[4] = (b+1)
            statespace4.append("RIGHT")
            if statespace4[0:3] == solved:
                print(statespace4[0:3])
                print(statespace4[5:])
                break
            if statespace4 not in closedlist:
                openlist.append(statespace4)
                print(statespace4[0:3], "ss4")
        
        closedlist.append(x)
        x=openlist.pop(0)
        y=x
        a=x[3]
        b=x[4]
    print("solved")


(k,l)=zeroindex(puzzle)
puzzle.append(k)
puzzle.append(l)
if check(puzzle):
    machineplay(puzzle)
else:
    print("not solvable")
