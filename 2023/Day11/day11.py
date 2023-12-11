"""
Redid this using actual math to change the indexes after "inserting" rows and columns
The rest is essentially the same
"""
from aocd import data
from itertools import combinations
import math

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

def calculate_sum_of_distances(expansion):
    # Get the indices of the empty rows and columns
    def get_index_after_inserts(index, empty_indices):
        return index + sum(1 for i in empty_indices if i < index) * (expansion - 1)
            
    # Get the hashes
    hashes = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                # Adjust the coordinates to account for the inserted rows and columns
                r_adjusted = get_index_after_inserts(r, alldotsr)
                c_adjusted = get_index_after_inserts(c, alldotsc)
                hashes.append((r_adjusted, c_adjusted))

    # Function to calculate Manhattan distance
    def manhattanDist(pair):
        X1, Y1 = pair[0]
        X2, Y2 = pair[1]
        
        return math.fabs(X2 - X1) + math.fabs(Y2 - Y1)

    upairs = combinations(hashes, 2)

    dists = list(map(manhattanDist, upairs))

    return sum(dists)

expansionp1 = 2
expansionp2 = 1000000

print(calculate_sum_of_distances(expansionp1))
print(calculate_sum_of_distances(expansionp2))



