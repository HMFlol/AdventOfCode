from aocd import get_data
from time import time
from collections import deque

data = get_data(day=21, year=2023)
# data = open('test.txt').read()
data = data.strip().splitlines()

grid = {complex(x,y): val for y, row in enumerate(data) for x, val in enumerate(row)}

start = next(x for x in grid if grid[x] == 'S') # Starting pos

dirs = [1, -1, 1j, -1j]  # north, south, east, west

size = len(data[0]) # Size of the grid
steps = 26501365

def iAmBfs(start, end):
    pos = {start} # Start at start (S)

    for _ in range(end): # Loop through the number of steps
        new_pos = set() # Set of new positions possible to move to
        for p in pos: # Loop through the current positions
            for dir in dirs: # Loop through the directions
                if p + dir in grid and grid[p + dir] in '.S': # If the new position is in the grid and is a garden plot or S
                    new_pos.add(p + dir) # Add the new position to the set of new positions
        pos = new_pos # Set the current positions to the new positions

    return len(pos) # Return the number of positionsstart

#def idkhonestly(grid, BIG_NUM):

start_time = time()

print(f"Total (Part1):", iAmBfs(start, 64))
#print(f"Total (Part2):", idkhonestly(grid, 26501365))

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")