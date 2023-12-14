'''Day 10 less bad'''
from aocd import get_data
from time import time
import re
from collections import deque

data = get_data(day=10, year=2023)

# data = open('test.txt').read()

grid = data.splitlines()

U, D, L, R = (-1, 0), (1, 0), (0, -1), (0, 1) # The UDLR technique. Is this a named thing or did I just make it up? I'm sure it's a named thing. I'm not that smart.
# Cooler way to do this imo, but then I have to account for using complex numbers later
# U, R, D, L = -1j, 1, 1j, -1

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
    if sr == len(grid) - 1 or U not in pipes[grid[sr + 1][sc]]:
        s_values -= set('|7F') # etc
    if sc == 0 or R not in pipes[grid[sr][sc - 1]]:
        s_values -= set('-J7') # etc
    if sc == len(grid[0]) - 1 or L not in pipes[grid[sr][sc + 1]]:
        s_values -= set('-LF') # etc
    
    assert len(s_values) == 1 # This should be 1 value at this point but just in case we messed up...
    [S] = s_values
    return S

def findLoop(grid, sr, sc, pipes):
    '''
    Finding the loop
    '''
    pr, pc = sr, sc # Set previous row and column to the starting position
    dr, dc = pipes[grid[sr][sc]][0] # Grab the starting direction from the pipes dict
    nr = pr + dr # Next row and column are the starting position plus the direction to move in
    nc = pc + dc
    
    loop = {(sr, sc)} # Track the loop starting from... start, in a set
    looplist = [(sr, sc)] # This list is used solely for shoelace + Picks Theorem. Could use a list for ray Casting as well but it's LITERALLY 1000x slower

    while (nr, nc) != (sr, sc): # While the next position is not the starting position
        loop.add((nr, nc)) # Add the next position to the loop
        looplist.append((nr, nc))
        for dr, dc in pipes[grid[nr][nc]]: # Grab the directions from the pipes dictionary for the next position
            # Check if the next position is the previous position, if not, set the previous position to the next position and break out of the loop
            if (nr + dr, nc + dc) != (pr, pc):
                pr = nr
                pc = nc
                nr += dr
                nc += dc
                break

    return loop, looplist

def nGrid(grid):
    '''
    Removing junk from the grid
    This can legit be done with this one liner instead of this nGrid funciton, but wanted to try both ways
    grid = [''.join(ch if (r,c) in loop else '.' for c, ch in enumerate(row)) for r, row in enumerate(grid)]
    '''
    ngrid = [] # Initialize a new grid

    for r, row in enumerate(grid): # Iterate over the rows of the grid
        nrow = '' # Initialize a new row
        for c, ch in enumerate(row): # Iterate over the characters in the row
            if (r, c) in loop: # If the cell is in the loop, add the original character to the new row
                nrow += ch
            else: # If the cell is not in the loop, add a dot to the new row
                nrow += '.'
        ngrid.append(nrow) # Add the new row to the new grid
    
    return ngrid

def rayCasting(grid):
    """
    This section will be for Ray Casting to determine how many cells are in the loop polygon
    There are many ways to do this. You can do it horizontally, using a regex (row = re.sub('L-*J|F-*7', '', row)) to remove the L_J and F_7 instances, then checking for crossing at |FL, or you can remove the regex entireley and only check for ILJ or I7F, which is simpler. 

    You can also do it diagonally, something like this:

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != '.':
                continue
            cr, cc = r - 1, c - 1
            within = False
            while cr >= 0 and cc >= 0:
                if grid[cr][cc] in '|-FJ':
                    within = not within
                cr -= 1
                cc -= 1
            if within:
                inloop += 1
    """
    inloop = 0

    for r, row in enumerate(grid): 
        within = False
        for c, ch in enumerate(row):
            if ch in '|LJ': # If ch is |, L, or J, flip within and if within is True and ch is a . add 1 to inloop
                within = not within
            if within and ch == '.':
                inloop += 1
    
    return inloop

def shoelacePick():
    """
    This section is for an answer using Shoelace Formula and Pick's Theorem
    """
    # Shoelace algorithm
    loop_length = len(looplist)
    shoelace_sum = sum(looplist[i][0] * (looplist[(i + 1) % loop_length][1] - looplist[i - 1][1]) for i in range(loop_length))
    shoelace_area = abs(shoelace_sum) // 2

    # Pick's theorem
    boundary_points = loop_length // 2
    interior_points = shoelace_area + 1 - boundary_points

    return interior_points

def floodFill():
    """
    This section is for an answer using Flood Fill
    First need to explode the grid by 3x3
    Then use Breadth First Fill to find the number of cells inside the loop
    """
    ng = []  # Initialize an empty list to store the new representation of the grid

    for row in grid:  # Iterate through each row in the original grid
        top = []  # Initialize lists to store the three rows of the subgrid
        mid = []
        bot = []

        for ch in row:  # Iterate through each character in the current row
            subgrid = [[False] * 3 for _ in range(3)]  # Initialize a 3x3 subgrid of boolean values, initially all False
            if ch != '.':  # If the character is not '.', update the subgrid based on certain conditions
                subgrid[1][1] = True  # Set the center of the subgrid to True
                if U in pipes[ch]:  # If 'U' is in the possible directions for the character, set the corresponding cell to True
                    subgrid[0][1] = True
                if D in pipes[ch]:
                    subgrid[2][1] = True
                if L in pipes[ch]:
                    subgrid[1][0] = True
                if R in pipes[ch]:
                    subgrid[1][2] = True

            top += subgrid[0]  # Extend the 'top' list with the first row of the subgrid
            mid += subgrid[1]  # Extend the 'mid' list with the second row of the subgrid
            bot += subgrid[2]  # Extend the 'bot' list with the third row of the subgrid

        ng += [top, mid, bot]  # Extend the new representation 'ng' with the three rows of the subgrid
    '''
    for row in ng:
        for wall in row:
            print('#' if wall else '.', end='')
        print()
    '''
    outside = {(0,0)}

    q = deque([(0,0)])

    while q:
        r, c = q.popleft()
        for nr, nc, in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < len(ng) and 0 <= nc < len(ng[nr]) and not ng[nr][nc] and (nr, nc) not in outside:
                outside.add((nr, nc))
                q.append((nr, nc))

    total = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (r, c) in loop:
                continue
            if (r * 3 + 1, c * 3 + 1) in outside:
                continue
            total += 1

    return total

starttime = time()

# findS
S = findS(grid, sr, sc, pipes)
# Replace S with the ONE TRUE PIPE
grid = [row.replace('S', S) for row in grid]
# Find the loop we need for everything
loop, looplist = findLoop(grid, sr, sc, pipes)

print(f"Total (Part1 - Loop Traversal):", len(loop) // 2)
# Part 2
# Replace the old grid with the new grid
grid = nGrid(grid)

# HRC
start = time()
result = rayCasting(grid)
end = time()
print(f"Total (Part2 - Horizontal Ray Casting): {result}, Finished in {end - start:.6f} seconds")

# Shoelace + Picks Theorem
start = time()
result = shoelacePick()
end = time()
print(f"Total (Part2 - Shoelace + Picks Theorem): {result}, Finished in {end - start:.6f} seconds")

# Flood Fill
start = time()
result = floodFill()
end = time()
print(f"Total (Part2 - Flood Fill): {result}, Finished in {end - start:.6f} seconds")

endtime = time()
print(f"Total execution time: {endtime - starttime:.6f} seconds")

'''
Create a mapping from your characters to pipe characters for funzies
Works fine in nGrid instead, but need to replace the relevant characters in the rayCasting function
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