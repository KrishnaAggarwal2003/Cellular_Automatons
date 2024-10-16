import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

def eight_bit_binary(num):
  binary = []
  x = len(binary)
  
  while x<8:
    binary.append(num%2)
    num = num//2
    x+=1
  binary.reverse()
  
  cell_combinations = ['111','110','101','100','011','010','001','000']  
  rule_dict = dict(zip(cell_combinations , binary))
  
  return rule_dict

def grid_initialize(row_len , generation_time):
    initial_list = np.random.randint(0, 2, row_len)
    grid = np.zeros((generation_time, row_len), dtype=int)
    grid[0] = initial_list
    
    return grid

def rule_automaton(input_arr, binary_dict):
  output = []
  x = list(input_arr)
  for i in range(len(x)):
   # Periodic Boundary conditions
    if i==0:
      kernel = [x[len(x)-1] , x[i], x[i+1]]
    elif i==len(x)-1:
      kernel = [x[i-1] , x[i], x[0]]
    else:
      kernel = [x[i-1] , x[i], x[i+1]]

  # Rules
    kernel_str = ''.join(map(str, kernel))
    output.append(binary_dict[kernel_str])

  return np.array(output)


def update(frame, img, grid, generation_text, binary_dict):
    if frame > 0:
      grid[frame] = rule_automaton(grid[frame - 1], binary_dict=binary_dict)

    img.set_data(grid[:frame+1])  # Update the grid display up to the current frame

    generation_text.set_text(f"Generation: {frame}")
    return [img, generation_text]


def animation_maker(grid, generation_time, binary_dict):
    fig, ax = plt.subplots()
    generation_text = fig.text(0.80, 1.05, '', transform=ax.transAxes, color='black', fontsize=11, ha='left', va='top')

    img = ax.imshow(grid, cmap='cividis_r', interpolation='nearest', aspect='auto')
    ax.set_title(f"Rule {automaton_number} Cellular Automaton")
    
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, generation_text, binary_dict),
                              frames=generation_time, interval=100, repeat=True)

    plt.tight_layout()
    
# Display the animation
    plt.show()    
    
# Save the animation file
    ani.save(f"rule_{automaton_number} animation.gif", writer="Pillow")


if __name__ == '__main__':
    
    print("Taking the required inputs from the User")
    automaton_number = int(input("Enter the desired number for rule automaton: "))
    row_len = int(input("Enter the desired length for the 1-D row: "))    
    generation_time = int(input("Enter the number of generations: "))
    
    print("Starting of the Automaton")
    
    try:
     binary_dict = eight_bit_binary(num=automaton_number)
     grid = grid_initialize(row_len=row_len, generation_time=generation_time)
     animation_maker(grid=grid, generation_time=generation_time, binary_dict=binary_dict)
    
    except Exception as e:
        print(f"Some error occurred: {e}")
         
    