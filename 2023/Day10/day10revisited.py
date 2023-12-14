'''Day 10 less bad'''
from aocd import get_data
import time
import re

data = get_data(day=10, year=2023)

# data = open('test.txt').read()

grid = data.splitlines()

U = (-1, 0)
D = (1, 0)
L = (0, -1)
R = (0, 1)

pipes = {'|': (U, D), '-': (L, R), 'L': (U, R), 'J': (U, L), '7': (D, L), 'F': (D, R), '.': ()}

start = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == 'S']

sr, sc = start[0]

def findS(grid, sr, sc, pipes):
    '''
    Set this to begin to track what S is. First time I did this I set 'S' : (U,D,L,R), which worked for part 1 (if using BFS anyway), but in part 2 makes finding the actual loop SEEMINGLY impossible because it's not a valid pipe shape
    '''
    s_values = set(pipes) - {'.'}
    # If we are in row 0 or pip above doesn't have D movement, remove the values that don't have U movement
    if sr == 0 or D not in pipes[grid[sr - 1][sc]]:
        s_values -= set('|LJ')
    # etc
    if sr == len(grid) - 1 or U not in pipes[grid[sr + 1][sc]]:
        s_values -= set('|7F')
    # etc
    if sc == 0 or R not in pipes[grid[sr][sc - 1]]:
        s_values -= set('-J7')
    # etc
    if sc == len(grid[0]) - 1 or L not in pipes[grid[sr][sc + 1]]:
        s_values -= set('-LF')
    # This should be 1 value at this point but just in case we messed up...
    assert len(s_values) == 1

    [S] = s_values

    return S

def findLoop(grid, sr, sc, pipes):
    # Set previous row and column to the starting position
    pr, pc = sr, sc
    # Grab the starting direction from the pipes dict
    dr, dc = pipes[grid[sr][sc]][0]
    # Next row and column are the starting position plus the direction to move in
    nr = pr + dr
    nc = pc + dc
    # Track the loop starting from... start
    loop = {(sr, sc)}
    # While the next position is not the starting position
    while (nr, nc) != (sr, sc):
        # Add the next position to the loop
        loop.add((nr, nc))
        # Grab the directions from the pipes dictionary for the next position
        for dr, dc in pipes[grid[nr][nc]]:
            # Check if the next position is the previous position, if not, set the previous position to the next position and break out of the loop
            if (nr + dr, nc + dc) != (pr, pc):
                pr = nr
                pc = nc
                nr += dr
                nc += dc
                break
    return loop

# One liner to do the nGrid funciton below - removing junk from the grid, essentially
# grid = [''.join(ch if (r,c) in loop else '.' for c, ch in enumerate(row)) for r, row in enumerate(grid)]

def nGrid(grid):
    # Initialize a new grid
    ngrid = []

    # Iterate over the rows of the grid
    for r, row in enumerate(grid):
        # Initialize a new row
        nrow = ''
        # Iterate over the characters in the row
        for c, ch in enumerate(row):
            # If the cell is in the loop, add the original character to the new row
            if (r, c) in loop:
                nrow += ch
            # If the cell is not in the loop, add a dot to the new row
            else:
                nrow += '.'
        # Add the new row to the new grid
        ngrid.append(nrow)
    
    return ngrid

def rayTracing(grid):
    """
    This section will be for horizontal ray tracing to determine how many cells are in the loop polygon
    """
    inloop = 0

    for r, row in enumerate(grid):
        # remove any L_J or F_7 as they don't matter due to travelling along pipes 
        row = re.sub('L-*J|F-*7', '', row)
        within = False
        # If ch is |, F, or L, flip within and if within is True and ch is a . add 1 to inloop
        for c, ch in enumerate(row):
            if ch in '|FL':
                within = not within
            if within and ch == '.':
                inloop += 1
    
    return inloop

starttime = time.time()

# findS
S = findS(grid, sr, sc, pipes)
# Replace S with the ONE TRUE PIPE
grid = [row.replace('S', S) for row in grid]
# Find the loop we need for everything
loop = findLoop(grid, sr, sc, pipes)

print(f"Total (Part1):", len(loop) // 2)
# Part 2
# Replace the old grid with the new grid
grid = nGrid(grid)

print(f"Total (Part2): {rayTracing(grid)}")

endtime = time.time()
print(f"Total execution time: {endtime - starttime:.6f} seconds")

'''
Create a mapping from your characters to pipe characters for funzies
Works just fine instead of the above
'''
'''
pipe_chars = {'J': '┘', 'L': '└', '7': '┐', 'F': '┌'}

# Replace cells not in the loop with dots and cells in the loop with pipe characters
for r in range(len(grid)):
    row = list(grid[r])  # Convert string to list for mutable operations
    for c in range(len(row)):
        if (r, c) in loop:
            row[c] = pipe_chars.get(row[c], row[c])  # Replace with pipe character if possible
        else:
            row[c] = '.'  # Replace with dot
    grid[r] = ''.join(row)  # Convert list back to string and update grid

# Print the new grid
for row in grid:
    print(row)
'''