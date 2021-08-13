# 5. WATER JUG PROBLEM SOLVER (AI)  
   
- There are two water jugs :- **Jug1** and **Jug2** with their own volumes.
- Water can be poured into these **Jugs**. You cannot pour more water into the **Jugs** than the permitted volumes. But you can fill less.
- Initially both the Jugs are **emtpy**.
- A final state for the Jugs are decided. That is, how much water should be stored in **Jug1** and how much in **Jug2**.
- Our goal is to achieve the final state by using only the following permitted operations:- 
   * Fill **Jug1** completely
   * Fill **Jug2** Completely
   * Empty **Jug1**
   * Empty **Jug2**
   * Transfer water from **Jug1** to **Jug2**
   * Transfer water from **Jug2** to **Jug1**
- At any given time,  only **one operation** is allowed.
- Jugs can be filled and emptied any number of times. There is **no limit**.   
   
## FEED THE VALUES

![image](https://user-images.githubusercontent.com/55954313/129287894-ed3ed015-055d-4237-99f8-d814277abdd9.png)   
   
- **Jug1** can store a **maximum** of 3 units of water
- **Jug2** can store a **maximum** of 1 units of water
- Finally, **Jug1** must contain 2 units of water
- Finally, **Jug2** must contain 0 units of water   
   
## AI STARTS SOLVING

![image](https://user-images.githubusercontent.com/55954313/129288162-e5ce4b3b-3800-4950-8375-ff032d8e1272.png)   
   
If there is a solution, it prints **solved!**, else it prints **No solution available!**

## THE MINIMUM NUMBER OF STEPS   
   
The AI then prints the minimum number of steps it took to achieve the final state (if any)   
   
![image](https://user-images.githubusercontent.com/55954313/129288413-958bf521-7a3f-4910-a9ee-4f80f01fe349.png)   
   
In the above case, the solution makes perfect sense:-
1. FILL JUG1 COMPLETELY
   **Jug1** : 3   
   **Jug2** : 0   
   
2. JUG1 TO JUG2
   **Jug1** : 2   
   **Jug2** : 1 (as the **maximum volume** of **Jug2** is 1, it can store only 1 unit of water)   
   
3. EMPTY JUG2
   **Jug1** : 2   
   **Jug2** : 0 
Which is our final state   
---
