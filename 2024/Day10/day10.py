# Solution for Advent of Code 2024, Day 10
# https://adventofcode.com/2024/day/10

from time import time

from aocd import get_data


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


def load_data(use_test_data=False):
    if use_test_data:
        with open("test.txt") as f:
            return f.read()
    else:
        return get_data(day=10, year=2024)


data = load_data(use_test_data=1)

# Parsing stuff
data = data.strip().splitlines()

grid = {col + row * 1j: int(val) for row, line in enumerate(data) for col, val in enumerate(line)}


print("Part1:", trailhead_scores(grid))
print("Part2:", trailhead_scores(grid, False))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
