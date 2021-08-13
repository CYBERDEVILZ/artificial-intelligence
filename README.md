![](https://img.shields.io/static/v1?label=OPEN-SOURCED&message=Yes&color=blueviolet)

# Artificial Intelligence Python codes for solving puzzles and problems.

## NOTE

This repository was created solely to discuss the various Artificial Intelligence codes in Python that can be used to solve puzzles and problems. If you have any idea or algorithm, please feel free to update this repository as it will help all of us to grow as a community.

---

# 1. TIC-TAC-TOE (TWO USERS)   
   
- A basic two user playable Tic-Tac-Toe game that uses your numpad as the position markers.   
- Players take turn by turn to position their mark.   
- The game does not have a GUI as of now. It is a console version.

## INTERFACE

## Numpad Keys For Placing The Mark
![image](https://user-images.githubusercontent.com/55954313/125397562-b9ccb900-e3cb-11eb-83f9-a3f32b04927f.png)   


## Tic-Tac-Toe Board  

![image](https://user-images.githubusercontent.com/55954313/125396594-6148ec00-e3ca-11eb-96c6-59ce6d054445.png)   

## Positioning Your Mark

![image](https://user-images.githubusercontent.com/55954313/125396793-a4a35a80-e3ca-11eb-852d-03664844486d.png)   

![image](https://user-images.githubusercontent.com/55954313/125397021-fd72f300-e3ca-11eb-8634-3ecea78cbed1.png)

## Game Over

![image](https://user-images.githubusercontent.com/55954313/125398061-74f55200-e3cc-11eb-9bdc-2ba0b786980a.png)

---

# 2. TIC-TAC-TOE (USER vs AI)   
   
- Instead of another user, the machine will play against you.
- Developed using basic algorithm and some Tic-Tac-Toe tricks
- I have played against it a thousand times and the highest I have gone is a DRAW.
- GIVE IT A TRY. CAN YOU BEAT IT?   

## INTERFACE

## Numpad Keys For Placing The Mark
![image](https://user-images.githubusercontent.com/55954313/125397562-b9ccb900-e3cb-11eb-83f9-a3f32b04927f.png)   

## You Will Go First
![image](https://user-images.githubusercontent.com/55954313/125399778-ad962b00-e3ce-11eb-9178-8fd3e08489af.png)

## Immediately The AI Plays
![image](https://user-images.githubusercontent.com/55954313/125399936-ddddc980-e3ce-11eb-85f3-1d5272b8ac64.png)

## Play Until One Wins...
![image](https://user-images.githubusercontent.com/55954313/125400018-f817a780-e3ce-11eb-8ef0-19d4bbc96618.png)

## ... Or It's A Draw
![image](https://user-images.githubusercontent.com/55954313/125400132-29907300-e3cf-11eb-88d9-eff0ea78f5ec.png)

---

# 3. 8 - PUZZLE PROBLEM   
   
- There are 9 cells arranged in a 3x3 grid. Eight of them are numbered from 1 - 8 and one is left blank (in my case, I have numbered it to 0).
- The rule of this game is to swap the blank cell with its adjacent cell and arrange the cells in ascending order (with the blank space in the last cell).   
  #### That is, convert this...   
  
  ![image](https://user-images.githubusercontent.com/55954313/125402163-b5a39a00-e3d1-11eb-9466-2bc1c7bdef15.png)   
  
  #### To this...   
  
  ![image](https://user-images.githubusercontent.com/55954313/125401360-ad972a80-e3d0-11eb-81e2-7ea72e4e05df.png)   
  
## KEYBOARD BINDINGS

### A - LEFT
### S - DOWN
### D - RIGHT
### W - UP

## GOAL STATE

![image](https://user-images.githubusercontent.com/55954313/125401360-ad972a80-e3d0-11eb-81e2-7ea72e4e05df.png)  

## TRY SOLVING THE PUZZLE. IF STUCK, THEN LOOK MY NEXT TOPIC :)

---

# 4. 8 - PUZZLE PROBLEM SOLVER (AI)   
   
- Uses **BEST FIRST SEARCH** to find the optimum solution.
- Heuristic function used is **MANHATTAN DISTANCE**
- Feed the 8 - puzzle problem board values and it will spit out the steps.
- Solves the problem **blazing fast!**

## FEED THE BOARD VALUES

![image](https://user-images.githubusercontent.com/55954313/125405419-56e01f80-e3d5-11eb-9f4b-b43e8f282954.png)   

## THE SOLUTION

![image](https://user-images.githubusercontent.com/55954313/125405521-75deb180-e3d5-11eb-8354-ccb22fccaf0e.png)

---

# 5. WATER JUG PROBLEM SOLVER (AI)  
   
- There are two water jugs :- **Jug1** and **Jug2** with their own volumes.
- Water can be poured into these Jugs. You cannot pour more water into the Jugs than the permitted volumes. But you can fill less.
- Initially both the Jugs are emtpy.
- A final state for the Jugs are decided. That is, how much water should be stored in Jug1 and how much in Jug2.
- Our goal is to achieve the final state by using only the following permitted operations:- 
   * Fill Jug1 completely
   * Fill Jug2 Completely
   * Empty Jug1
   * Empty Jug2
   * Transfer water from Jug1 to Jug2
   * Transfer water from Jug2 to Jug1
- At any given time,  only one operation is allowed.
- Jugs can be filled and emptied any number of times. There is no limit.   
   
## FEED THE VALUES

![image](https://user-images.githubusercontent.com/55954313/129287894-ed3ed015-055d-4237-99f8-d814277abdd9.png)   
   
- Jug1 can store a maximum of 3 units of water
- Jug2 can store a maximum of 1 units of water
- Finally, Jug1 must contain 2 units of water
- Finally, Jug2 must contain 0 units of water   
   
## AI STARTS SOLVING

![image](https://user-images.githubusercontent.com/55954313/129288162-e5ce4b3b-3800-4950-8375-ff032d8e1272.png)   
   
If there is a solution, it prints **solved!**, else it prints **No solution available!**

## THE MINIMUM NUMBER OF STEPS   
   
The AI then prints the minimum number of steps it took to achieve the final state (if any)   
   
![image](https://user-images.githubusercontent.com/55954313/129288413-958bf521-7a3f-4910-a9ee-4f80f01fe349.png)

---

