# Solution for Advent of Code 2024, Day 10
# https://adventofcode.com/2024/day/10

from time import time

from aocd import get_data


# Part 1
def trailhead_scores(grid):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    trailheads = [pos for pos, val in grid.items() if val == "0"]

    score = 0

    for trailhead in trailheads:
        stack = [(trailhead, 0)]
        visited = {trailhead}

        while stack:
            pos, height = stack.pop()
            if height == 9:
                score += 1
                continue

            for dir in directions:
                next_pos = pos + complex(*dir)
                if next_pos in grid and grid[next_pos] == str(height + 1) and next_pos not in visited:
                    visited.add(next_pos)
                    stack.append((next_pos, height + 1))
                    print(visited)

    return score


# Part 2
def trailhead_scores2(grid):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    trailheads = [pos for pos, val in grid.items() if val == "0"]

    score = 0

    for trailhead in trailheads:
        stack = [(trailhead, 0)]

        while stack:
            pos, height = stack.pop()
            if height == 9:
                score += 1
                continue

            for dir in directions:
                next_pos = pos + complex(*dir)
                if next_pos in grid and grid[next_pos] == str(height + 1):
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

grid = {complex(col, row): val for row, line in enumerate(data) for col, val in enumerate(line)}

print("Part1:", trailhead_scores(grid))
print("Part2:", trailhead_scores2(grid))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
