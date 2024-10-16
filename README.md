# Cellular_Automatons
This Repository contains several Cellular Automatons that can show the accurate pattern described in the theory.

# 1-D Cellular Automata
## Theory
A 1-D cellular automaton is a simple computational model consisting of a row (1 dimension) of cells that evolve over discrete time steps. Each cell in the automaton can exist in a finite set of states, commonly two states such as `0` (dead) or `1` (alive). A small group of neighbouring cells determines the state of each cell. In 1-D CA, the neighbourhood usually consists of the cell itself and its immediate left and right neighbours i.e. the state in the next generation is decided by a 3-number series (possible 8 combinations). The model uses periodic boundary conditions.

## Wolfram elementary CA
This a well-known example in 1-D cellular automata where 256 rule sets are possible as the next state (0 or 1) could be decided by 8 possible combinations (cell and its immediate neighbours) i.e. 2**8 = 256. The rule could be from 0 to 255. The code will ask for the user's desired rule number and will be executed accordingly.

| An example is shown below through a GIF:-
| ![Rule 110 CA](https://github.com/KrishnaAggarwal2003/Cellular_Automatons/blob/main/rule_110%20animation.gif) |
|:---:|
| Demo of Rule 110 Cellular Automaton |








