"""
This module solves the Advent of Code puzzle for day 23, year 2023.
"""
from time import time

from aocd import get_data

data = get_data(day=23, year=2023)
"""with open("test.txt", "r", encoding="utf-8") as file:
    data = file.read()"""
data = data.strip().splitlines()

grid = {complex(x, y): val for x, row in enumerate(data) for y, val in enumerate(row)}

start = next(x for x in grid if grid[x] == ".")
end = next(x for x in reversed(grid) if grid[x] == ".")

points = [start, end]

for pos, ch in grid.items():
    if ch == "#":
        continue
    BRANCHES = 0
    for d in [-1, 1, 1j, -1j]:
        npos = pos + d
        if npos in grid and grid[npos] != "#":
            BRANCHES += 1
    if BRANCHES >= 3:
        points.append(pos)

dirs = {
    "^": [-1],  # North
    "v": [1],  # South
    "<": [-1j],  # West
    ">": [1j],  # East
    ".": [-1, 1, 1j, -1j],  # All directions
}


def solve(part):
    """
    solve the puzzle obvs
    """
    graph = {pt: {} for pt in points}

    for spos in points:
        stack = [(0, spos)]
        seen = {spos}

        while stack:
            n, current_pos = stack.pop()
            if n != 0 and current_pos in points:
                graph[spos][current_pos] = n
                continue

            directions = dirs[grid[current_pos]] if part == 1 else [-1, 1, 1j, -1j]
            for direction in directions:
                next_pos = current_pos + direction
                if next_pos in grid and grid[next_pos] != "#" and next_pos not in seen:
                    stack.append((n + 1, next_pos))
                    seen.add(next_pos)

    seen = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m

    return dfs(start)


start_time = time()

print(f"Total (Part1): {solve(1)}")
print(f"Total (Part2): {solve(2)}")

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")
