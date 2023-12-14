'''
All essentially the same as p1
Moved the stuff into functions for moveing up and distance calc
Added func for 
'''

from aocd import get_data
from time import time
start_time = time()
data = get_data(day=14, year=2023)
#data = open('test.txt').read()
grid = data.splitlines()

grid = [list(r) for r in grid]

def spin(grid):
    return [list(x) for x in zip(*grid[::-1])]

def moveUp(grid):
    dr, dc = -1, 0
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'O':
                cr = r
                while cr > 0 and grid[cr + dr][c] == '.':
                    grid[cr][c] = '.'
                    grid[cr+dr][c] = 'O'
                    cr -= 1
    return grid

def distances(grid):
    distances = 0
    for r , row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'O':
                distances += len(grid) - r
    return distances

'''
Added math.
Count the cycles until we find a dupe grid
Then we can use the cycles to find the final grid state (happens at grid 119 it seems, for my input anyway)

'''
grids = {}
cycles = 1_000_000_000
cycle = 0
while cycle < cycles:
    cycle += 1
    for _ in range(4):
        grid = moveUp(grid)
        grid = spin(grid)
    neo = tuple(tuple(row) for row in grid) # Convert to tuple of tuples so we can hash it
    if neo in grids: # If we've seen it before
        print(f"Found dupe at cycle {cycle}") # For fun and visibility as to what's the haps
        cycle_length = cycle - grids[neo] # Calculate the cycle length (current cycle - cycle count when this was last seen)
        amt = (cycles - cycle) // cycle_length # Calculate how many cycles we can skip
        cycle += amt * cycle_length # Change cycle count by adding the amount we can skip
    grids[neo] = cycle # Add the grid to the dict with the cycle count as the value

# Then we calculate distance as in p1
distance = distances(grid)

print(f"Total (Part2):", distance)
end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")