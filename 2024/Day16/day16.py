# Solution for Advent of Code 2024, Day 16
# https://adventofcode.com/2024/day/16
from collections import defaultdict
from heapq import heappop, heappush
from time import time

from aocd import get_data


def maze_score(grid):
    # Find starting position marked S
    (start,) = [pos for pos in grid if grid[pos] == "S"]
    # Start facing east
    tie = 0
    heap = [(0, tie, start, 1, 0, 0, [start])]
    min_score = defaultdict(lambda: float("inf"))
    seen = []
    best = float("inf")

    while heap:
        score, _, pos, dir, steps, turns, path = heappop(heap)
        if score > min_score[pos, dir]:
            continue
        else:
            min_score[pos, dir] = score

        if grid.get(pos) == "E" and score <= best:
            best = score
            seen += path

        for new_dir in [1, -1, 1j, -1j]:
            new_pos = pos + new_dir
            if grid.get(new_pos) in {".", "E"}:
                new_steps = steps + 1
                new_turns = turns + (dir != new_dir)
                new_score = new_steps + new_turns * 1000
                tie += 1
                heappush(heap, (new_score, tie, new_pos, new_dir, new_steps, new_turns, path + [new_pos]))

    return best, len(set(seen))


start_time = time()


def load_data(use_test_data=False):
    if use_test_data:
        with open("test.txt") as f:
            return f.read()
    else:
        return get_data(day=16, year=2024)


data = load_data(use_test_data=1)

data = data.strip().splitlines()

grid = {col + row * 1j: val for row, line in enumerate(data) for col, val in enumerate(line)}

# Parsing stuff
p1, p2 = maze_score(grid)

print("Part1:", p1)
print("Part2:", p2)

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
