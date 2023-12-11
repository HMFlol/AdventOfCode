"""
First attempt inserting ACTUAL rows and columns like a silly guy
Couldn't really adjust for the much larger expansion in part 2
"""

from aocd import data
from itertools import combinations
import math

# Read the lines
with open('test.txt', 'r') as r:
    lines = r.readlines()
# join the lines into a single string
test = ''.join(lines)

grid = [list(line) for line in data.split('\n')]

# Get the rows of all .
alldotsr = []
for r, row in enumerate(grid):
    if all(ch == "." for ch in row):
        alldotsr.append(r)

# Get the columns of all .
alldotsc = []
for c, col in enumerate(zip(*grid)):
    if all(ch == "." for ch in col):
        alldotsc.append(c)

# Insert rows
for i in reversed(alldotsr):
    grid.insert(i+1, ['.' for _ in range(len(grid[0]))])

# Insert columns
for i in reversed(alldotsc):
    for row in grid:
        row.insert(i+1, '.')
        
# Get the hashes
hashes = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '#':
            hashes.append((r, c))

# Function to calculate Manhattan distance
def manhattanDist(pair):
    X1, Y1 = pair[0]
    X2, Y2 = pair[1]
    
    return math.fabs(X2 - X1) + math.fabs(Y2 - Y1)

upairs = combinations(hashes, 2)

dists = list(map(manhattanDist, upairs))

print(sum(dists))



