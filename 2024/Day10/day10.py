# Solution for Advent of Code 2024, Day 10
# https://adventofcode.com/2024/day/10

from time import time


# Part 1 + 2
def trailhead_scores(grid, part1=True):
    trailheads = [pos for pos, val in grid.items() if val == 0]

    score = 0

    for trailhead in trailheads:
        visited = {trailhead} if part1 else set()
        stack = [(trailhead, 0)]

        while stack:
            pos, height = stack.pop()
            if height == 9:
                score += 1
                continue

            for dir in (1, -1, 1j, -1j):
                next_pos = pos + dir
                if grid.get(next_pos) == height + 1 and next_pos not in visited:
                    visited.add(next_pos) if part1 else None
                    stack.append((next_pos, height + 1))

    return score


start_time = time()


data = open(0).read().strip()

# Parsing stuff
data = data.strip().splitlines()

grid = {col + row * 1j: int(val) for row, line in enumerate(data) for col, val in enumerate(line)}


print("\033[1mPart1:\033[22m", trailhead_scores(grid))
print("\033[1mPart2:\033[22m", trailhead_scores(grid, False))

end_time = time()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
