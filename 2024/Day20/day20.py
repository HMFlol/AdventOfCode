# Solution for Advent of Code 2024, Day 20
# https://adventofcode.com/2024/day/20
from collections import deque
from itertools import combinations
from time import perf_counter


def get_relative_positions(max_distance):
    # Generate all relative positions within a given Manhattan distance
    deltas = []
    for dx in range(-max_distance, max_distance + 1):
        for dy in range(-max_distance, max_distance + 1):
            if 0 < abs(dx) + abs(dy) <= max_distance:
                deltas.append(dx + dy * 1j)
    return deltas


def cheats(grid, radius):
    # BFS to get all positions with distances from the start
    start = next(pos for pos in grid if grid[pos] == "S")
    end = next(pos for pos in grid if grid[pos] == "E")
    seen = {start: 0}
    stack = deque([(start, 0)])

    while stack:
        pos, dist = stack.popleft()
        if pos == end:
            break
        for dir in (-1, 1, 1j, -1j):
            next_pos = pos + dir
            if next_pos in grid and next_pos not in seen:
                seen[next_pos] = dist + 1
                stack.append((next_pos, dist + 1))

    # Get all relative positions for Part 1 and Part 2
    relative_positions = get_relative_positions(radius)
    shorties = 0

    for pos in seen:
        # Check shortcuts within a radius of 2 for Part 1 or 20 for Part 2
        for rel in relative_positions:
            next_pos = pos + rel
            if next_pos in seen:
                man_dist = abs(rel.real) + abs(rel.imag)
                shortcut_distance = seen[next_pos] - seen[pos] - man_dist
                if shortcut_distance >= 100:
                    shorties += 1

    return shorties

    # Can do the same thing using combinations (with some small changes when calling the function), but takes 4x longer
    # shorties1 = 0
    # shorties2 = 0
    #
    # for (pos1, dist1), (pos2, dist2) in combinations(seen.items(), 2):
    #     man_dist = abs(pos1.real - pos2.real) + abs(pos1.imag - pos2.imag)
    #     if man_dist <= 2:
    #         shortcut_distance = dist2 - dist1 - man_dist
    #         if shortcut_distance >= 100:
    #             shorties1 += 1
    #     if man_dist <= 20:
    #         shortcut_distance = dist2 - dist1 - man_dist
    #         if shortcut_distance >= 100:
    #             shorties2 += 1

    # return shorties1, shorties2


start_time = perf_counter()

data = open(0).read().strip()
# Parsing stuff
grid = {col + row * 1j: val for row, line in enumerate(data.splitlines()) for col, val in enumerate(line) if val != "#"}

print("\033[1mPart1:\033[22m", cheats(grid, 2))
print("\033[1mPart2:\033[22m", cheats(grid, 20))

end_time = perf_counter()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
