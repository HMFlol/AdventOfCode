# Solution for Advent of Code 2024, Day 6
# https://adventofcode.com/2024/day/6

from aocd import get_data
from time import time

from copy import deepcopy

# data = get_data(day=6, year=2024)
data = open('test.txt').read()
data = data.strip().splitlines()

grid = {complex(x,y): val for x, row in enumerate(data) for y, val in enumerate(row)}

""" # How to print the grid with complex numbers
# Get the max row and column
max_row = int(max(key.imag for key in grid.keys()))
max_col = int(max(key.real for key in grid.keys()))

# Print it
for r in range(max_row + 1):
    for c in range(max_col + 1):
        print(grid.get(r + 1j * c, ' '), end='')
    print() """

startpos = [key for key, val in grid.items() if val == '^'][0]
pos = startpos
dir = -1

# N, E, S, W = -1, 1j, 1, -1j

# Pathing function - returns a set of all visited positions // loops count if loop_time is True
def pathing(grid, loop_time=False):
    pos, dir, path = startpos, -1, set()
    loop=False

    while True:
        if (pos, dir) in path: # If we've been here before break, or if detecting loops, loop=True first
            if loop_time:
                loop=True
            break
        path.add((pos, dir))
        next_pos = pos + dir
        match grid.get(next_pos):
            case '#':
                dir *= -1j # Turn right
            case None:
                break
            case _:
                pos = next_pos

    return {pos for pos, _ in path} if not loop_time else loop

# Part 2 loop finding
def find_loops(grid):
    path = pathing(grid)
    loops = 0

    for obstacle in path:
        new_grid = deepcopy(grid) # Making copy of the grid to check for loops one obstacle at a time
        new_grid[obstacle] = '#'
        loops += pathing(new_grid, loop_time=True)

    return loops


start_time = time()

print(f"Part1:", len(pathing(grid)))
print(f"Part2:", find_loops(grid))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
