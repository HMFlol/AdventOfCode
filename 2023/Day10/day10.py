from aocd import data
from collections import deque
"""
TIME STUFF
"""
import time
start_time = time.time()

# Parse test data
# grid = [list(line) for line in open('test.txt').read().split('\n')]
# Parse the input into a 2D grid
grid = [list(line) for line in data.split('\n')]

# Map each pipe symbol to the directions it allows movement in with DICTIONARIES!!!!!
pipes = {'|': [(1, 0), (-1, 0)], '-': [(0, 1), (0, -1)], 'L': [(0, 1), (-1, 0)], 'J': [(0, -1), (-1, 0)], '7': [(0, -1), (1, 0)], 'F': [(0, 1), (1, 0)], 'S': [(1, 0), (-1, 0), (0, 1), (0, -1)]}

# Find the starting position 'S' in the grid
start = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 'S'][0]

# Part 1
def loop(grid, start):
    # Initialize a set to keep track of visited positions
    visited = set()

    # Initialize a dictionary to store the maximum number of steps to each position
    distances = {start: 0}

    # Initialize a queue for BFS and add the starting position to it
    # deque is a list-like container with fast appends and pops on either end
    # Google told me to do this
    queue = deque([(start, 0)])

    # Using a Breadth First Search algorithm(this is a recursive algorithm that uses a queue to keep track of the nodes to visit)
    # It searches outwards in a circle from the starting point until it finds all the nodes in the loop
    while queue:
        (r, c), steps = queue.popleft()
        if (r, c) not in visited:
            visited.add((r, c))
            distances[(r, c)] = steps
            for dr, dc in pipes[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] in pipes:
                    # Check if the new position is connected to the current position by a valid pipe
                    if (-dr, -dc) in pipes[grid[nr][nc]]:
                        queue.append(((nr, nc), steps + 1))

    # Find the maximum distance from the starting point to any other node in the loop
    print(max(distances.values()))

loop(grid, start)


"""
TIME STUFF
"""
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total execution time: {elapsed_time:.6f} seconds")