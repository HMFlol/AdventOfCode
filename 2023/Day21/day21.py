from aocd import get_data
from time import time
from collections import deque

data = get_data(day=21, year=2023)
# data = open('test.txt').read()
data = data.strip().splitlines()

grid = {complex(x,y): val for x, row in enumerate(data) for y, val in enumerate(row)}

start = next(x for x in grid if grid[x] == 'S') # Starting pos

dirs = [-1, 1, 1j, -1j]  # north, south, east, west

size = len(data[0]) # Size of the grid
steps = 26501365

def p1stuff(start, end):
    pos = {start} # Start at start (S)

    for _ in range(end): # Loop through the number of steps
        new_pos = set() # Set of new positions possible to move to
        for p in pos: # Loop through the current positions
            for dir in dirs: # Loop through the directions
                if p + dir in grid and grid[p + dir] in '.S': # If the new position is in the grid and is a garden plot or S
                    new_pos.add(p + dir) # Add the new position to the set of new positions
        pos = new_pos # Set the current positions to the new positions

    return len(pos) # Return the number of positionsstart

def p2stuffidk():
    grid_width = steps // size - 1

    odd = (grid_width // 2 * 2 + 1) ** 2
    even = ((grid_width + 1) // 2 * 2) ** 2

    odd_points = p1stuff(start, size * 2 + 1)
    even_points = p1stuff(start, size * 2)

    corner_t = p1stuff(complex(size - 1, start.imag), size - 1)
    corner_r = p1stuff(complex(start.real, 0), size - 1)
    corner_b = p1stuff(complex(0, start.imag), size - 1)
    corner_l = p1stuff(complex(start.real, size - 1), size - 1)

    small_tr = p1stuff(complex(size - 1, 0), size // 2 - 1)
    small_tl = p1stuff(complex(size - 1, size - 1), size // 2 - 1)
    small_br = p1stuff(complex(0, 0), size // 2 - 1)
    small_bl = p1stuff(complex(0, size - 1), size // 2 - 1)

    large_tr = p1stuff(complex(size - 1, 0), size * 3 // 2 - 1)
    large_tl = p1stuff(complex(size - 1, size - 1), size * 3 // 2 - 1)
    large_br = p1stuff(complex(0, 0), size * 3 // 2 - 1)
    large_bl = p1stuff(complex(0, size - 1), size * 3 // 2 - 1)

    return(
    odd * odd_points +
    even * even_points +
    corner_t + corner_r + corner_b + corner_l +
    (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) +
    grid_width * (large_tr + large_tl + large_br + large_bl)
)



start_time = time()

print(f"Total (Part1):", p1stuff(start, 64))
print(f"Total (Part2):", p2stuffidk())

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")