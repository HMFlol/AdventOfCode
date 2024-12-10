# Solution for Advent of Code 2024, Day 6
# https://adventofcode.com/2024/day/6

from time import time

from aocd import get_data

data = get_data(day=6, year=2024)
# data = open('test.txt').read()
data = data.strip().splitlines()

grid = {complex(x, y): val for y, row in enumerate(data) for x, val in enumerate(row)}

startpos = [key for key, val in grid.items() if val == "^"][0]
pos = startpos
dir = -1

# Define direction transitions
TURN_RIGHT = {
    -1j: 1,  # North -> East
    1: 1j,  # East -> South
    1j: -1,  # South -> West
    -1: -1j,  # West -> North
}


# Pathing function - returns a set of all visited positions // loops count if loop_time is True
def pathing(grid, loop_time=False):
    pos, dir, path = startpos, -1, set()

    while True:
        state = (pos, dir)
        if state in path:  # If seen break, or if detecting loops, loop=True first
            if loop_time:
                return True
            break
        path.add(state)
        next_pos = pos + dir  # Calculate next position
        match grid.get(next_pos):
            case "#":
                dir = TURN_RIGHT.get(dir, dir)  # Turn right
            case None:
                break
            case _:
                pos = next_pos

    return {pos for pos, _ in path} if not loop_time else False


# Part 2 loop finding
def find_loops(grid):
    path = pathing(grid)
    loops = 0

    for cell in path:
        grid[cell] = "#"
        loops += pathing(grid, loop_time=True)
        grid[cell] = "."

    return loops


start_time = time()

print("Part1:", len(pathing(grid)))
print("Part2:", find_loops(grid))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")

""" # How to print the grid with complex numbers
# Get the max row and column
max_row = int(max(key.imag for key in grid.keys()))
max_col = int(max(key.real for key in grid.keys()))

# Print the grid row by row
for r in range(max_row + 1):
    row_str = ''
    for c in range(max_col + 1):
        pos = complex(c, r)  # real=c (column), imag=r (row)
        row_str += grid.get(pos, ' ')
    print(row_str) """
