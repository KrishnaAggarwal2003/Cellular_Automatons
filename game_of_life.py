import numpy as np
from operator import * 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image


def grid_initilization(grid_dim, pattern):
    
    if pattern == 'random':
     grid = np.random.choice([0,1], size=(grid_dim , grid_dim))
    
    elif pattern == 'oscillator':
        grid = np.zeros(shape=(grid_dim,grid_dim))
        N = int(grid_dim/2)
        grid[N-1][N] = 1
        grid[N][N] = 1
        grid[N+1][N] = 1
        
    elif pattern == 'glider':
       grid = np.zeros(shape=(grid_dim,grid_dim))
       grid[1][2] = 1
       grid[2][3] = 1
       grid[3][1:4] = 1     
    
    return grid   

def life_games(grid_matrix):
    cell_state = [0, 1]
    grid_size = grid_matrix.shape[0]

    new_grid = np.copy(grid_matrix)
    for i in range(grid_size):
        for j in range(grid_size):
            cell = grid_matrix[i][j]

            # Periodic Boundary conditions
            if i > 0 and j > 0 and i < grid_size - 1 and j < grid_size - 1:
                neighbours = [grid_matrix[i][j+1], grid_matrix[i][j-1],
                              grid_matrix[i+1][j], grid_matrix[i-1][j],
                              grid_matrix[i-1][j-1], grid_matrix[i+1][j+1],
                              grid_matrix[i+1][j-1], grid_matrix[i-1][j+1]]

            elif i == 0 and j == 0:
                neighbours = [grid_matrix[i][j+1], grid_matrix[i+1][j],
                              grid_matrix[i][grid_size-1], grid_matrix[grid_size-1][grid_size-1],
                              grid_matrix[grid_size-1][j], grid_matrix[grid_size-1][j+1],
                              grid_matrix[i+1][grid_size-1], grid_matrix[i+1][j+1]]

            elif i == 0 and j < grid_size - 1:
                neighbours = [grid_matrix[grid_size-1][j-1], grid_matrix[grid_size-1][j],
                              grid_matrix[grid_size-1][j+1], grid_matrix[i][j-1],
                              grid_matrix[i][j+1], grid_matrix[i+1][j-1],
                              grid_matrix[i+1][j], grid_matrix[i+1][j+1]]

            elif j == 0 and i < grid_size - 1:
                neighbours = [grid_matrix[i+1][grid_size-1], grid_matrix[i][grid_size-1],
                              grid_matrix[i][j+1], grid_matrix[i+1][j+1],
                              grid_matrix[i][j+1], grid_matrix[i-1][j+1],
                              grid_matrix[i+1][j], grid_matrix[i-1][j]]

            elif i == grid_size - 1 and j == grid_size - 1:
                neighbours = [grid_matrix[grid_size-1][j-1], grid_matrix[i-1][grid_size-1],
                              grid_matrix[0][grid_size-1], grid_matrix[grid_size-1][0],
                              grid_matrix[i-1][j-1], grid_matrix[i-1][0],
                              grid_matrix[0][j-1], grid_matrix[0][0]]

            elif i == grid_size - 1 and j < grid_size - 1:
                neighbours = [grid_matrix[0][j-1], grid_matrix[0][j],
                              grid_matrix[0][j+1], grid_matrix[i][j-1],
                              grid_matrix[i][j+1], grid_matrix[i-1][j-1],
                              grid_matrix[i-1][j], grid_matrix[i-1][j+1]]

            elif j == grid_size - 1 and i < grid_size - 1:
                neighbours = [grid_matrix[i+1][0], grid_matrix[i][0],
                              grid_matrix[i+1][j-1], grid_matrix[i+1][j],
                              grid_matrix[i][0], grid_matrix[i-1][0],
                              grid_matrix[i+1][j], grid_matrix[i-1][j]]

            # Count live neighbors before applying the Game of Life rules
            live_neighbours = neighbours.count(1)

            # Apply the Game of Life rules
            if cell == cell_state[1] and live_neighbours < 2:
                new_grid[i][j] = cell_state[0]
            elif cell == cell_state[1] and (live_neighbours == 2 or live_neighbours == 3):
                new_grid[i][j] = cell_state[1]
            elif cell == cell_state[1] and live_neighbours > 3:
                new_grid[i][j] = cell_state[0]
            elif cell == cell_state[0] and live_neighbours == 3:
                new_grid[i][j] = cell_state[1]

    return new_grid


def update(frame, img, grid, generation_text):
    new_grid = life_games(grid)
    img.set_data(new_grid)
    grid[:] = new_grid # Update the grid in place
    generation_text.set_text(f"Generation: {frame}")
    return [img, generation_text]

def animation_maker(grid , generation_time, pattern):
    fig, ax = plt.subplots(figsize=(6, 6))
    generation_text = fig.text(0.015, 1.035, '', transform=ax.transAxes, color='black', fontsize=11, ha='left', va='top')
    img = ax.imshow(grid, cmap='binary', interpolation='nearest')
    ax.set_title(f"Convoy Game of Life: {pattern} pattern", loc='right') 
    
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, generation_text), 
                              frames=generation_time, interval=200, repeat=True) 
    
    plt.tight_layout()
    # Display the animation
    plt.show()    
# Save the animation file
    ani.save(f"Game_of_life_animation.gif", writer="Pillow")  
    

if __name__ == "__main__":
    print("Taking required inputs from the user")    
    
    grid_dim = int(input("Enter the desired grid dimension: "))
    generation_time = int(input("Enter the no. of generations: "))
    pattern_selected = str(input("Enter the pattern: "))
    
    print("Starting the simulation")
    try:
     grid = grid_initilization(grid_dim=grid_dim, pattern="oscillator")
     animation_maker(grid=grid,generation_time=generation_time, pattern=pattern_selected)
    except Exception as e:
        print(f"Some error occured: {e}") 