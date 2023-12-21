from aocd import get_data
from time import time
from collections import deque

data = get_data(day=21, year=2023)
# data = open('test.txt').read()
data = data.strip().splitlines()

grid = {complex(x,y): val for y, row in enumerate(data) for x, val in enumerate(row)}

S = next(x for x in grid if grid[x] == 'S') # Starting pos

dirs = [1, -1, 1j, -1j]  # north, south, east, west

def iAmBfs(grid, end):
    q = deque([(S, 0)])  # Initialize queue with starting position and steps
    seen = {S}
    ans = set()

    while q:
        pos, steps = q.popleft()
        if steps % 2 == 0:
            ans.add(pos) # Adding only the even steps to get rid of back and forth movement
        if steps == end:
            continue
        for dir in dirs:
            new_pos = pos + dir
            if new_pos in grid and grid[new_pos] in '.S' and new_pos not in seen:
                seen.add(new_pos)
                q.append((new_pos, steps + 1))

    return len(ans)


start_time = time()

print(f"Total (Part1):", iAmBfs(grid, 64))
# print(f"Total (Part2):", iAmBfsInfinite(grid, 26501365))

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")