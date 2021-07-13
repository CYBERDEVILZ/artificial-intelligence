import time as t

puzzle=[]
solved=[1, 2, 3, 4, 5, 6, 7, 8, 0]
def zeroindex(puzzle):
    for i in range(9):
        if puzzle[i] == 0:
            return i
            break

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

def heuristic(puzzle):         #finds the heursitic value
    man_dist=sum(abs((val-1)%3 - i%3) + abs((val-1)//3 - i//3) for i, val in enumerate(puzzle) if val)
    return man_dist
        
def min_heuristics(lists):     #finds the minimum heuristic among a list of heurisitc values and returns it's position
    min=999999
    for i in range(len(lists)):
        if lists[i]<min:
            min=lists[i]
            index=i
    return(index)

def machineplay(puzzle):
    openlist=[]
    openLIST=[]
    closedlist=[]
    heuristicval=[]
    openlist.append(puzzle)
    x=[]
    x=openlist.pop(0)
    a=x[9]                                                          #stores the index of 0
    while x[:9]!=solved:
        if a%3!=0:                                                  #left
            statespace1=x.copy()
            temp=statespace1[a]
            statespace1[a]=statespace1[a-1]
            statespace1[a-1]=temp
            statespace1[9]=a-1
            statespace1.append("LEFT")
            
            if statespace1[:9] == solved:
                print("SOLVED!")
                print("The steps to solve are:- \n")
                print(", ".join(statespace1[10:]))
                break
            else:
                if statespace1[:9] not in closedlist and statespace1[:9] not in openLIST:
                    openlist.append(statespace1)    #for printing the steps
                    openLIST.append(statespace1[:9]) #to prevent loops
                    heuristicval.append(heuristic(statespace1[:9]))

        
        if a%3!=2:                                                  #right
            statespace2=x.copy()
            temp=statespace2[a]
            statespace2[a]=statespace2[a+1]
            statespace2[a+1]=temp
            statespace2[9]=a+1
            statespace2.append("RIGHT")
            
            if statespace2[:9] == solved:
                print("SOLVED!")
                print("The steps to solve are:- \n")
                print(", ".join(statespace2[10:]))
                break
            else:
                if statespace2[:9] not in closedlist and statespace2[:9] not in openLIST:
                    openlist.append(statespace2)
                    openLIST.append(statespace2[:9])
                    heuristicval.append(heuristic(statespace2[:9]))

        if a!=0 and a!=1 and a!=2:                                    #up
            statespace3=x.copy()
            temp=statespace3[a]
            statespace3[a]=statespace3[a-3]
            statespace3[a-3]=temp
            statespace3[9]=a-3
            statespace3.append("UP")
            
            if statespace3[:9] == solved:
                print("SOLVED!")
                print("The steps to solve are:- \n")
                print(", ".join(statespace3[10:]))
                break
            else:
                if statespace3[:9] not in closedlist and statespace3[:9] not in openLIST:
                    openlist.append(statespace3)
                    openLIST.append(statespace3[:9])
                    heuristicval.append(heuristic(statespace3[:9]))


        if a!=6 and a!=7 and a!=8:                                    #down
            statespace4=x.copy()
            temp=statespace4[a]
            statespace4[a]=statespace4[a+3]
            statespace4[a+3]=temp
            statespace4[9]=a+3
            statespace4.append("DOWN")
            if statespace4[:9] == solved:
                print("\nSOLVED!")
                print("\nThe steps to solve are:- ")
                print(", ".join(statespace4[10:]))
                break
            else:
                if statespace4[:9] not in closedlist and statespace4[:9] not in openLIST:
                    openlist.append(statespace4)
                    openLIST.append(statespace4[:9])
                    heuristicval.append(heuristic(statespace4[:9]))
        closedlist.append(x[:9])
        y=min_heuristics(heuristicval)
        tem=heuristicval.pop(y)
        x=openlist.pop(y)
        a=x[9]
    
    # print("SOLVED!")
    # print("CLOSED LIST:", len(closedlist), "nodes")

def show_board(puzzle):
            print("""\n+---+---+---+
| {} | {} | {} |
+---+---+---+
| {} | {} | {} |
+---+---+---+
| {} | {} | {} |
+---+---+---+""".format(puzzle[0], puzzle[1], puzzle[2], puzzle[3], puzzle[4], puzzle[5], puzzle[6], puzzle[7], puzzle[8]))


def enterBoard(puzzle):
    hmm = "n"
    while(hmm=="n"):
        print("\nEnter the board values with spaces: ")
        puzzle = list(map(int, input().split()))
        print("\nIs the following board correct?")
        show_board(puzzle)
        print('\n')
        hmm = input("[Y/N]: ").lower()
    return puzzle


puzzle = enterBoard(puzzle)
k=zeroindex(puzzle)
if check(puzzle):
    puzzle.append(k)
    # start_time=t.time()
    machineplay(puzzle)
    # end_time=t.time()
    # print("TOTAL TIME: ", (end_time-start_time), "seconds")

    
