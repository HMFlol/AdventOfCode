from aocd import get_data
from time import time
start_time = time()
data = get_data(day=10, year=2023)
# data = open('test.txt').read()
grid = data.splitlines()

U, D, L, R = (-1, 0), (1, 0), (0, -1), (0, 1)

pipes = {'|': (U, D), '-': (L, R), 'L': (U, R), 'J': (U, L), '7': (D, L), 'F': (D, R), '.': ()}

# Find the starting position 'S' in the grid
start = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == 'S']

sr, sc = start[0]
# Find the actual pipe shape of S
s_values = set(pipes) - {'.'}
# If we are in row 0 or pip above doesn't have D movement, remove the values that don't have U movement
if sr == 0 or D not in pipes[grid[sr - 1][sc]]:
    s_values -= set('|LJ')
if sr == len(grid) - 1 or U not in pipes[grid[sr + 1][sc]]:
    s_values -= set('|7F') # etc
if sc == 0 or R not in pipes[grid[sr][sc - 1]]:
    s_values -= set('-J7') # etc
if sc == len(grid[0]) - 1 or L not in pipes[grid[sr][sc + 1]]:
    s_values -= set('-LF') # etc

assert len(s_values) == 1 # This should be 1 value at this point but just in case we messed up...
[S] = s_values
# Replace S with the ONE TRUE PIPE
grid = [row.replace('S', S) for row in grid]

# Part 1
loop = {(sr, sc)} # Track the loop starting from... start, in a set
pr, pc = sr, sc # Set previous row and column to the starting position
dr, dc = pipes[grid[sr][sc]][0] # Grab the starting direction from the pipes dict
nr = pr + dr # Next row and column are the starting position plus the direction to move in
nc = pc + dc

while (nr, nc) != (sr, sc): # While the next position is not the starting position
    loop.add((nr, nc)) # Add the next position to the loop
    for dr, dc in pipes[grid[nr][nc]]: # Grab the directions from the pipes dictionary for the next position
        # Check if the next position is the previous position, if not, set the previous position to the next position and break out of the loop
        if (nr + dr, nc + dc) != (pr, pc):
            pr = nr
            pc = nc
            nr += dr
            nc += dc
            break

# Part 2
# Remove junk from grid. Anything not in loop is now .
grid = [''.join(ch if (r,c) in loop else '.' for c, ch in enumerate(row)) for r, row in enumerate(grid)]

inloop = 0

# Hoizontal Ray Casting
for r, row in enumerate(grid): 
    within = False
    for c, ch in enumerate(row):
        if ch in '|LJ': # If ch is |, L, or J, flip within and if within is True and ch is a . add 1 to inloop
            within = not within
        if within and ch == '.':
            inloop += 1

print(f"Total (Part1 - Loop Traversal):", len(loop) // 2)
print(f"Total (Part1 - Loop Traversal):", inloop)

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")