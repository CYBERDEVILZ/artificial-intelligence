jug1 = int(input('Enter the jug1 value: '))              # capacity of jug1
jug2 = int(input("Enter the jug2 value: "))              # capacity of jug2
 
finalJug1 = int(input("Enter the final jug1 value: "))   # final jug1 values
finalJug2 = int(input("Enter the final jug2 value: "))   # final jug2 values
 
goalState = [finalJug1,finalJug2]                        # this is what we need
jugValues = [jug1,jug2]                                  # stores the capacity

openList   = []           # stores all the newly discovered possibilities.
closedList = []           # stores all the explored possibilites.

initialValue  = [0,0]
flag = 0
openList.append(initialValue)
a=openList.pop(0)

while(len(openList)!=0 or a[:2]!=goalState):
    
    x=a[0]
    y=a[1]
    
    if x<jug1:
        currentState1 = a.copy()                                 # completely filling jug1
        currentState1[0] = jug1
        currentState1.append("FILL JUG1 COMPLETELY")
        print(currentState1[:2], "ss1")
        if currentState1[0:2] == goalState:
            print(currentState1[2:])
            flag=1
            print("solved!")
            break
        elif currentState1[:2] not in closedList:
            openList.append(currentState1)        
    
    if y<jug2:
        currentState2 = a.copy()
        currentState2[1] = jug2                                  # completely filling jug2
        currentState2.append("FILL JUG2 COMPLETELY")
        print(currentState2[:2], "ss2")
        if currentState2[0:2] == goalState:
            print(currentState2[2:])
            flag=1
            print("solved!")
            break
        elif currentState2[:2] not in closedList:
            openList.append(currentState2)                     
    
    if "emptying jug1": 
        currentState3 = a.copy()
        currentState3[0] = 0
        currentState3.append("EMPTY JUG1")
        print(currentState3[:2], "ss3")                                   # empty jug1
        if currentState3[:2] == goalState:
            print(currentState3[2:])
            flag=1
            print("solved!")
            break
        elif currentState3[:2] not in closedList:
            openList.append(currentState3)                                    
    
    if"emptying jug2":       
        currentState4 = a.copy()
        currentState4[1] = 0
        currentState4.append("EMPTY JUG2")
        print(currentState4[:2], "ss4")                             # empty jug2
        if currentState4[:2] == goalState:
            print(currentState4[2:])
            flag=1
            print("solved!")
            break
        elif currentState4[:2] not in closedList:
            openList.append(currentState4)        
            

    if x<jug1 and y>0:                                      # transfer from jug2 to jug1
        currentState5 = a.copy()
        currentState5[0] = min(jug1, (x+y))
        currentState5[1] = max(0, (x+y)-jug1)
        currentState5.append("JUG2 TO JUG1")
        print(currentState5[:2], "ss5")                          
        if currentState5[:2] == goalState:
            print(currentState5[2:])
            flag=1
            print("solved!")
            break
        elif currentState5[:2] not in closedList:
            openList.append(currentState5)        

    if y<jug2 and x>0:
        currentState6 = a.copy()
        currentState6[0] = max(0,(x+y)-jug2)
        currentState6[1] = min(jug2,(x+y))
        currentState6.append("JUG1 TO JUG2")
        print(currentState6[:2], "ss6")                          # transfer from jug1 to jug2
        if currentState6[:2] == goalState:
            print(currentState6[2:])
            flag=1
            print("solved!")
            break
        elif currentState6[:2] not in closedList:
            openList.append(currentState6)        

    closedList.append(a[:2])
    try:
        a = openList.pop(0) 
    except IndexError:
        print("No solution available!")
        break
   
