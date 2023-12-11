"""
Redid this using actual math to change the indexes after "inserting" rows and columns
The rest is essentially the same
"""
from aocd import data
from itertools import combinations
from time import time

starttime = time()

# Gridding
grid = [list(line) for line in data.split('\n')]

# Get the rows of all dots
all_dots_r = []
for r, row in enumerate(grid):
    if all(ch == "." for ch in row):
        all_dots_r.append(r)

# Get the columns of all dots
all_dots_c = []
for c, col in enumerate(zip(*grid)):
    if all(ch == "." for ch in col):
        all_dots_c.append(c)

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
                r_adjusted = get_index_after_inserts(r, all_dots_r)
                c_adjusted = get_index_after_inserts(c, all_dots_c)
                hashes.append((r_adjusted, c_adjusted))

    # Function to calculate Manhattan distance
    def manhattanDist(pair):
        X1, Y1 = pair[0]
        X2, Y2 = pair[1]
        
        return abs(X2 - X1) + abs(Y2 - Y1)

    upairs = combinations(hashes, 2)

    """
    Could also do this but the other way is a slick tool!
    
    upairs = []
    for i in range(len(hashes) - 1):
        for j in range(i + 1, len(hashes)):
            upairs.append((hashes[i], hashes[j]))
    """
    dists = list(map(manhattanDist, upairs))

    return sum(dists)

expansionp1 = 2
expansionp2 = 1000000

start = time()
print(f"Part 1: {calculate_sum_of_distances(expansionp1)}")
end = time()
print(f"Finished in {end - start:.6f} seconds")

start = time()
print(f"Part 2: {calculate_sum_of_distances(expansionp2)}")
end = time()
print(f"Finished in {end - start:.6f} seconds")

endtime = time()
print(f"Total execution time: {endtime - starttime:.6f} seconds")


