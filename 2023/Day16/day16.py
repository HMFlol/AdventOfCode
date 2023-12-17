'''
Complex numbers explained at the bottom of this file
'''

from aocd import get_data
from time import time

data = get_data(day=16, year=2023)
data = open('test.txt').read()
data = data.strip().splitlines()

grid = {complex(x,y): val for y, row in enumerate(data) for x, val in enumerate(row)}
print(grid)

def startBlasting(startpos, startdir):
    nextlaser = [(startpos, startdir)]
    path = set() # set of (pos, dir) tuples of the path taken
    while nextlaser:
        # Get the current laser
        pos, dir = nextlaser.pop()
        # Skip adding the position and direction to the path set if it's already in the path set, as it's pointless (laser isn't going to do anything new)
        while not (pos, dir) in path:
            # Add the new position and direction to the path set
            path.add((pos, dir))
            pos += dir
            match grid.get(pos):
                case '|':
                    dir = 1j # hitting from left or right
                    nextlaser.append((pos, -dir)) # add a new laser with the opposite direction
                case '-':
                    dir = -1 # hitting from top or bottom
                    nextlaser.append((pos, -dir))  # add a new laser with the opposite direction
                case '/':
                    dir = -complex(dir.imag, dir.real)  # rotate + or - 90 degrees depending on directionality
                case '\\':
                    dir = complex(dir.imag, dir.real)  # rotate + or - 90 degrees depending on directionality
                case None:
                    break
        
    return len(set(pos for pos, _ in path)) - 1 # subtract 1 because we don't count the starting position

    '''
    The above method of handling rotations is cleaner and more efficient. I have an explanation of how the above complex statements work at the bottom of this file. However, this also works and is easier to understand.
    case '/':
        if dir.real:  # if moving horizontally
            dir *= -1j  # rotate -90 degrees
        else:  # if moving vertically
            dir *= 1j  # rotate 90 degrees
    case '\\':
        if dir.real:  # if moving horizontally
            dir *= 1j  # rotate 90 degrees
        else:  # if moving vertically
            dir *= -1j  # rotate -90 degrees
    '''


start_time = time()
# Part 1
print(f"Total (Part1):", startBlasting(-1, 1))

# Part 2
directions = [1, 1j, -1, -1j] # Define the directions
# Will do a list comprehension thingyof this later
positions_and_directions = [] # Create an empty list to store the tuples

for dir in directions: # Iterate over each direction
    for pos in grid: # Iterate over each position in the grid
        if pos - dir not in grid: # If the new position is not in the grid, add the tuple to the list, to get starting positions OFF of the grid with the direction to move in
            positions_and_directions.append((pos - dir, dir))

'''result = 0
# Apply the function startBlasting to each tuple in the list, and find the maximum result
# Iterate over each tuple in the list
for pos_dir in positions_and_directions:
    # Apply the startBlasting function to the tuple and update max_result if necessary
    result = max(result, startBlasting(*pos_dir))'''

# This works too and is better
result = max(map(lambda pos_dir: startBlasting(*pos_dir), positions_and_directions))

print(f"Total (Part2):", result)

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")

'''
In Python, complex numbers are used to represent 2D coordinates or directions. A complex number z is of the form x + yj, where x is the real part and y is the imaginary part. In the context of a 2D grid:

x corresponds to the column index (horizontal direction)
y corresponds to the row index (vertical direction)

In my code, I'm using complex numbers to represent directions:

1 represents a step to the right (increase the column index by 1)
-1 represents a step to the left (decrease the column index by 1)
1j represents a step down (increase the row index by 1)
-1j represents a step up (decrease the row index by 1)

You can add a complex number to a position to move in the direction represented by the complex number. For example, if pos is a position and dir is a direction, pos + dir is the position you get by moving from pos in the direction dir.

I'm also using complex multiplication to rotate directions:

Multiplying by 1j rotates a direction 90 degrees counterclockwise
Multiplying by -1j rotates a direction 90 degrees clockwise

For example, if dir is a direction, dir * 1j is the direction you get by rotating dir 90 degrees counterclockwise, and dir * -1j is the direction you get by rotating dir 90 degrees clockwise.

Once I get a firm grasp on this, navigating grids will be cake. 
'''
'''
HOW TO PRINT A GRID THAT USES COMPLEX NUMBERS INSTEAD OF X,Y COORDINATES
# Get the max row and column
max_row = int(max(key.imag for key in grid.keys()))
max_col = int(max(key.real for key in grid.keys()))

# Print the grid
for r in range(max_row + 1):
    for c in range(max_col + 1):
        print(grid.get(c + 1j * r, ' '), end='')
    print() 
'''
'''
The expression -complex(dir.imag, dir.real) is creating a new complex number and then negating it.

Here's how it works:

complex(dir.imag, dir.real): This creates a new complex number. The complex function takes two arguments: the real part and the imaginary part of the complex number. In this case, dir.imag and dir.real are being used as the real and imaginary parts, respectively. This effectively swaps the real and imaginary parts of dir.

-: This negates the complex number created in the previous step. Negating a complex number means changing the sign of both its real and imaginary parts.

The overall effect of -complex(dir.imag, dir.real) is to rotate the direction represented by dir by -90 degrees in the complex plane. This is because in the complex plane, swapping the real and imaginary parts of a complex number and then negating it corresponds to a -90 degrees rotation.

For example, if dir is 1 + 0j (which represents a direction to the right), -complex(dir.imag, dir.real) is -0 - 1j, which represents a direction downwards. This is a -90 degrees rotation from the original direction.
'''