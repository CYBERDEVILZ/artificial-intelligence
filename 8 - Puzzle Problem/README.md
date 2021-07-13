# Artificial Intelligence Python codes for solving puzzles.

### All the codes are written purely by me

---
# 1. 8 - PUZZLE PROBLEM
#### (8Puzzle_user.py)
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

# 2. 8 - PUZZLE PROBLEM SOLVER (AI)
#### (8PuzzleAI.py)
- Uses **BEST FIRST SEARCH** to find the optimum solution.
- Heuristic function used is **MANHATTAN DISTANCE**
- Feed the 8 - puzzle problem board values and it will spit out the steps.
- Solves the problem **blazing fast!**

## FEED THE BOARD VALUES

![image](https://user-images.githubusercontent.com/55954313/125405419-56e01f80-e3d5-11eb-9f4b-b43e8f282954.png)   

## THE SOLUTION

![image](https://user-images.githubusercontent.com/55954313/125405521-75deb180-e3d5-11eb-8354-ccb22fccaf0e.png)

---
