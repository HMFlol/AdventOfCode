# Solution for Advent of Code 2024, Day 18
# https://adventofcode.com/2024/day/18
from collections import deque
from time import time


def incoming_game(corruption, size, bytes):
    seen = {*corruption[:bytes]}
    stack = deque([(0, (0, 0))])

    while stack:
        score, (x, y) = stack.popleft()
        if (x, y) == (size, size):
            return score
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for newx, newy in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if 0 <= newx <= size and 0 <= newy <= size:
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


data = open(0).read().strip()
# Parsing stuff
lines = data.strip().split("\n")
corruption = [*map(eval, lines)]

if len(corruption) > 30:
    size = 70
    bytesize = 1024
else:
    size = 6
    bytesize = 12


print("\033[1mPart1:\033[22m:", incoming_game(corruption, size, bytesize))
print("\033[1mPart2:\033[22m:", user_wins(corruption, size, bytesize))

end_time = time()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
