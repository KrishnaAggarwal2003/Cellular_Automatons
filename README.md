# Cellular_Automatons
This Repository contains several Cellular Automatons that can show the accurate pattern described in the theory.

# 1-D Cellular Automata
## Theory
A 1-D cellular automaton is a simple computational model consisting of a row (1 dimension) of cells that evolve over discrete time steps. Each cell in the automaton can exist in a finite set of states, commonly two states such as `0` (dead) or `1` (alive). A small group of neighbouring cells determines the state of each cell. In 1-D CA, the neighbourhood usually consists of the cell itself and its immediate left and right neighbours i.e. the state in the next generation is decided by a 3-number series (possible 8 combinations). The model uses periodic boundary conditions.

## Wolfram elementary CA
This a well-known example in 1-D cellular automata where 256 rule sets are possible as the next state (0 or 1) could be decided by 8 possible combinations (cell and its immediate neighbours) i.e. 2**8 = 256. The rule could be from 0 to 255. The code will ask for the user's desired rule number and will be executed accordingly.

An example is shown below through a GIF:-
| ![Rule 110 CA](https://github.com/KrishnaAggarwal2003/Cellular_Automatons/blob/main/rule_110%20animation.gif) |
|:---:|
| Demo of Rule 110 Cellular Automaton |


# Convoy Game of Life
## Description
The **Convoy Game of Life** is a fascinating variation of the classic Game of Life developed by John Conway. The Convoy Game of Life is played on a grid of cells, where each cell can be in one of two states: **alive (1)** or **dead (0)**. The state of each cell evolves over discrete time steps based on a set of predefined rules.

A demo is shown below:-
| ![Game of Life](https://github.com/KrishnaAggarwal2003/Cellular_Automatons/blob/main/Game_of_life_animation.gif) |
|:---:|
| Convoy Game of Life CA |

# SIRS Model Simulations
## Description
1. The model would have: 
   
   - **Susceptible** = 0
   - **Infected** = 1<=>threshold 
   - **Recovered** = threshold  

   Then at `val == threshold`, the person would again become **susceptible** indicating the loop between the states
 
 2. The transition from **Susceptible to Infected** will be **probabilistic**, depending on the number of **infected neighbors**. The more the **infected** neighbours, the more the chance of infection.

4. The number of individuals will be categorized as:
   - Susceptible
   - Infected
   - Recovered

5. The analysis is done in 4 kinds of plots:
   
   - The GIF of the simulation showing the pattern of the cellular automata
   
   ![SIRS_simulation](https://github.com/user-attachments/assets/1c7074c7-140e-4402-a2d2-ecf3a9c2d668)

   - The grouped bar graph which shows the number of individuals in each category at the beginning and the end of the simulation

   ![bars](https://github.com/user-attachments/assets/ac4090c2-e380-4342-9dd1-089c135e33e5)
     
   - The seaborn scatter plots that visualize the number of individuals in the categories concerning the generations  
   
   ![categ](https://github.com/user-attachments/assets/9edfa427-1034-4eb9-9d91-37613470c9ce)

   - The line plots that compare between the number of individuals from all the categories, giving an idea of comparison between the categories.

   ![fina;](https://github.com/user-attachments/assets/ba1acb53-a39c-4a7b-9e7b-d527079c018c)




