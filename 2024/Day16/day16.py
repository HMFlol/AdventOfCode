# Solution for Advent of Code 2024, Day 16
# https://adventofcode.com/2024/day/16
from collections import defaultdict
from heapq import heappop, heappush
from time import time


def maze_score(grid):
    # Find starting position marked S
    (start,) = [pos for pos in grid if grid[pos] == "S"]
    # Tie breaker for the heap due to using complex numbers
    tie = 0
    heap = [(0, tie, start, 1, 0, 0, [start])]
    # Store the minimum score for each position and direction
    min_score = defaultdict(lambda: float("inf"))
    seen = []
    best = float("inf")

    while heap:
        score, _, pos, dir, steps, turns, path = heappop(heap)
        # If the score is higher than the minimum score for this position and direction, skip
        # Otherwise, update the minimum score
        if score > min_score[pos, dir]:
            continue
        else:
            min_score[pos, dir] = score
        # If we reached the end and the score is less than the best score, update the best score
        # and add the path to the seen list
        if grid.get(pos) == "E" and score <= best:
            best = score
            seen += path
        # Try moving in all four directions
        for new_dir in [1, -1, 1j, -1j]:
            new_pos = pos + new_dir
            # If valid, calculate new score and add it all, including the path, to the heap
            if grid.get(new_pos) in {".", "E"}:
                new_steps = steps + 1
                new_turns = turns + (dir != new_dir)
                new_score = new_steps + new_turns * 1000
                tie += 1
                heappush(heap, (new_score, tie, new_pos, new_dir, new_steps, new_turns, path + [new_pos]))

    return best, len(set(seen))


start_time = time()

data = open(0).read().strip()

data = data.strip().splitlines()

grid = {col + row * 1j: val for row, line in enumerate(data) for col, val in enumerate(line)}

# Parsing stuff
p1, p2 = maze_score(grid)

print("\033[1mPart1:\033[22m:", p1)
print("\033[1mPart2:\033[22m:", p2)

end_time = time()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
