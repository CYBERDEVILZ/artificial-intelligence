import time as t

puzzle = [1, 0, 3, 4, 2, 5, 7, 8, 6]

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


def machineplay(puzzle):
    print("\nSOLVING...")
    print("EVALUATING DIFFERENT STATESPACES...")
    solved=[1, 2, 3, 4, 5, 6, 7, 8, 0]
    openlist=[]
    openLIST=[]
    closedlist=[]
    openlist.append(puzzle)
    x=[]
    x=openlist.pop(0)
    a=x[9]
    while x[:9]!=solved:
        if a%3!=0:                                                  #left
            statespace1=x.copy()
            temp=statespace1[a]
            statespace1[a]=statespace1[a-1]
            statespace1[a-1]=temp
            statespace1[9]=a-1
            print(statespace1[:9])
            statespace1.append("LEFT")
            if statespace1[:9] == solved:
                print("\nSOLVED!")
                print("\nThe steps are..")
                print(statespace1[10:])
                break
            else:
                if statespace1[:9] not in closedlist and statespace1[:9] not in openLIST:
                    openlist.append(statespace1)
                    openLIST.append(statespace1[:9])
        
        if a%3!=2:                                                  #right
            statespace2=x.copy()
            temp=statespace2[a]
            statespace2[a]=statespace2[a+1]
            statespace2[a+1]=temp
            statespace2[9]=a+1
            print(statespace2[:9])
            statespace2.append("RIGHT")
            if statespace2[:9] == solved:
                print("\nSOLVED!")
                print("\nThe steps are..")
                print(statespace2[10:])
                break
            else:
                if statespace2[:9] not in closedlist and statespace2[:9] not in openLIST:
                    openlist.append(statespace2)
                    openLIST.append(statespace2[:9])
        if a!=0 and a!=1 and a!=2:                                    #up
            statespace3=x.copy()
            temp=statespace3[a]
            statespace3[a]=statespace3[a-3]
            statespace3[a-3]=temp
            statespace3[9]=a-3
            print(statespace3[:9])
            statespace3.append("UP")
            if statespace3[:9] == solved:
                print("\nSOLVED!")
                print("\nThe steps are..")
                print(statespace3[10:])
                break
            else:
                if statespace3[:9] not in closedlist and statespace3[:9] not in openLIST:
                    openlist.append(statespace3)
                    openLIST.append(statespace3[:9])

        if a!=6 and a!=7 and a!=8:                                    #down
            statespace4=x.copy()
            temp=statespace4[a]
            statespace4[a]=statespace4[a+3]
            statespace4[a+3]=temp
            statespace4[9]=a+3
            print(statespace4[:9])
            statespace4.append("DOWN")
            if statespace4[:9] == solved:
                print("\nSOLVED!")
                print("\nThe steps are..")
                print(statespace4[10:])
                break
            else:
                if statespace4[:9] not in closedlist and statespace4[:9] not in openLIST:
                    openlist.append(statespace4)
                    openLIST.append(statespace4[:9])
        closedlist.append(x[:9])
        x=openlist.pop(0)
        a=x[9]
    
    print("\nCLOSED LIST:", len( closedlist), "nodes")


k=zeroindex(puzzle)
if check(puzzle):
    puzzle.append(k)
    start_time=t.time()
    machineplay(puzzle)
    end_time=t.time()
    print("TOTAL TIME: ", (end_time-start_time), "seconds\n")
    