jug1 = int(input('Enter the jug1 value: '))                 # capacity of jug1
jug2 = int(input("Enter the jug2 value: "))                 # capacity of jug2
 
finalJug1 = int(input("Enter the final jug1 value: "))      # final jug1 values
finalJug2 = int(input("Enter the final jug2 value: "))      # final jug2 values
 
goalState = [finalJug1,finalJug2]                           # this is what we need
jugValues = [jug1,jug2]                                     # stores the capacity

openList   = []                                             # stores all the newly discovered possibilities.
closedList = []                                             # stores all the explored possibilites.

initialValue  = [0,0]
flag = 0
openList.append(initialValue)
a=openList.pop(0)

# Possible Operations Possible For This Problem:- 
#   1. Completely fill Jug1
#   2. Completely fill Jug2
#   3. Empty Jug1
#   4. Empty Jug2
#   5. Transfer from Jug1 to Jug2
#   6. Transfer from Jug2 to Jug1

while True:
    
    x = a[0]
    y = a[1]
    
    if x < jug1:                                            # Fill Jug1 Completely
        currentState1 = a.copy()                            
        currentState1[0] = jug1
        currentState1.append("FILL JUG1 COMPLETELY")
        print(currentState1[0:2], "<--- ss1")
        if currentState1[0:2] == goalState:
            print("solved!")
            print("\n")
            print(currentState1[2:])
            flag = 1
            break
        elif currentState1[:2] not in closedList:
            openList.append(currentState1)        
    
    if y < jug2:                                            # Fill Jug2 Completely
        currentState2 = a.copy()
        currentState2[1] = jug2                                  
        currentState2.append("FILL JUG2 COMPLETELY")
        print(currentState2[:2], "<--- ss2")
        if currentState2[0:2] == goalState:
            print("solved!")
            print("\n")
            print(currentState2[2:])
            flag = 1
            break
        elif currentState2[:2] not in closedList:
            openList.append(currentState2)                     
    
    if "emptying jug1":                                     # Empty Jug1 
        currentState3 = a.copy()
        currentState3[0] = 0
        currentState3.append("EMPTY JUG1")
        print(currentState3[:2], "<--- ss3")                                   
        if currentState3[:2] == goalState:
            print("solved!")
            print("\n")
            print(currentState3[2:])
            flag=1
            break
        elif currentState3[:2] not in closedList:
            openList.append(currentState3)                                    
    
    if "emptying jug2":                                     # Empty Jug2       
        currentState4 = a.copy()
        currentState4[1] = 0
        currentState4.append("EMPTY JUG2")
        print(currentState4[:2], "<--- ss4")                             
        if currentState4[:2] == goalState:
            print("solved!")
            print("\n")
            print(currentState4[2:])
            flag=1
            break
        elif currentState4[:2] not in closedList:
            openList.append(currentState4)        
            

    if x < jug1 and y > 0:                                  # Transfer from Jug2 to Jug1 
        currentState5 = a.copy()
        currentState5[0] = min(jug1, (x+y))
        currentState5[1] = max(0, (x+y)-jug1)
        currentState5.append("JUG2 TO JUG1")
        print(currentState5[:2], "<--- ss5")                          
        if currentState5[:2] == goalState:
            print("solved!")
            print("\n")
            print(currentState5[2:])
            flag = 1
            break
        elif currentState5[:2] not in closedList:
            openList.append(currentState5)        

    if y < jug2 and x > 0:                                  # Transfer from Jug1 to Jug2
        currentState6 = a.copy()
        currentState6[0] = max(0,(x+y)-jug2)
        currentState6[1] = min(jug2,(x+y))
        currentState6.append("JUG1 TO JUG2")
        print(currentState6[:2], "<--- ss6")                          
        if currentState6[:2] == goalState:
            print("solved!")
            print("\n")
            print(currentState6[2:])
            flag = 1
            break
        elif currentState6[:2] not in closedList:
            openList.append(currentState6)        

    closedList.append(a[:2])
    try:
        a = openList.pop(0) 
    except IndexError:
        print("No solution available!")
        break
   
