# Solution for Advent of Code 2024, Day 18
# https://adventofcode.com/2024/day/18
from collections import deque
from time import time

import numpy as np
from aocd import get_data


def incoming_game(corruption, size, bytes):
    grid = np.full((size + 1, size + 1), ".", dtype=str)
    baddies = {*corruption[:bytes]}
    for cell in baddies:
        grid[cell[1], cell[0]] = "#"

    seen = {}
    stack = deque([(0, (0, 0))])

    while stack:
        score, (x, y) = stack.popleft()
        if (x, y) == (size, size):
            return score
        if (x, y) in seen and seen[(x, y)] <= score:
            continue
        seen[(x, y)] = score
        for newx, newy in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if 0 <= newx <= size and 0 <= newy <= size and grid[newx, newy] != "#":
                stack.append((score + 1, (newx, newy)))
    # For Part 2 / user_wins function
    return False


def user_wins(corruption, size, bytes):
    """# Linear search (~17s).

    grid = np.full((size + 1, size + 1), ".", dtype=str)

    for cell in corruption:
        grid[cell[1], cell[0]] = "#"
        seen = []
        stack = deque([(0, 0)])

        while stack:
            (x, y) = stack.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            for newx, newy in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                if 0 <= newx <= size and 0 <= newy <= size and grid[newx, newy] != "#":
                    stack.append((newx, newy))
        if (size, size) not in seen:
            return cell
    """
    # Binary search (~0.05s)
    corruption_len = len(corruption)
    # Will be somewhere between 1024, which has to have a path due to p1, and the length of the corruption list
    while bytes < corruption_len:
        mid = (bytes + corruption_len) // 2
        if incoming_game(corruption, size, mid):
            bytes = mid + 1
        else:
            corruption_len = mid

    x, y = corruption[bytes - 1]
    return f"{x},{y}"


start_time = time()


def load_data(use_test_data=False):
    if use_test_data:
        with open("test.txt") as f:
            return f.read()
    else:
        return get_data(day=18, year=2024)


data = load_data(use_test_data=0)
# Parsing stuff
lines = data.strip().split("\n")
corruption = [*map(eval, lines)]


print("Part1:", incoming_game(corruption, 70, 1024))
print("Part2:", user_wins(corruption, 70, 1024))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
