from aocd import get_data
from time import time
start_time = time()
data = get_data(day=14, year=2023)
data = open('test.txt').read()
grid = data.splitlines()

grid = [list(r) for r in grid]

N, S, E, W = (-1, 0), (1, 0),  (0, 1), (0, -1)

# Part 1
dr, dc = N
# Move 'O' characters north
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == 'O':
            # Move north until we hit a wall or another 'O'
            cr = r
            while cr > 0 and grid[cr + dr][c] == '.':
                grid[cr][c] = '.'
                grid[cr+dr][c] = 'O'
                cr -= 1

# print('\n'.join(''.join(row) for row in grid))

distances = 0
dlist = []
for r , row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == 'O':
            distances += len(grid) - r
            dlist.append(len(grid) - r)


print(f"Total (Part1):", distances)

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")