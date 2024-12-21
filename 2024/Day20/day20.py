# Solution for Advent of Code 2024, Day 20
# https://adventofcode.com/2024/day/20
from collections import deque
from time import perf_counter


def get_relative_positions(max_distance):
    """Generate all relative positions within a given Manhattan distance along with their distances."""
    return [
        ((dx + dy * 1j), abs(dx) + abs(dy))
        for dx in range(-max_distance, max_distance + 1)
        for dy in range(-max_distance, max_distance + 1)
        if 0 < abs(dx) + abs(dy) <= max_distance
    ]


def bfs(grid, start):
    """BFS to get all positions with distances from the start."""
    seen = {start: 0}
    stack = deque([start])
    while stack:
        pos = stack.popleft()
        dist = seen[pos]
        for dir in (-1, 1, 1j, -1j):
            next_pos = pos + dir
            if next_pos in grid and next_pos not in seen:
                seen[next_pos] = dist + 1
                stack.append(next_pos)
    return seen


def cheats(seen, relative_positions):
    """Count the number of shortcuts based on the relative positions and Manhattan distance."""
    shorties = 0
    for pos, dist in seen.items():
        for rel, man_dist in relative_positions:
            next_pos = pos + rel
            next_pos_dist = seen.get(next_pos)
            if next_pos_dist is not None:
                shortcut_distance = next_pos_dist - dist - man_dist
                if shortcut_distance >= 100:
                    shorties += 1
    return shorties


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()
    # Parsing the grid
    grid = {
        col + row * 1j: val for row, line in enumerate(data.splitlines()) for col, val in enumerate(line) if val != "#"
    }
    # Find start and end positions
    start = next(pos for pos in grid if grid[pos] == "S")
    # Perform BFS once
    seen = bfs(grid, start)
    # Precompute relative positions for both parts
    rel_pos_part1 = get_relative_positions(2)
    rel_pos_part2 = get_relative_positions(20)
    # Count shortcuts for Part 1 and Part 2
    shorties1 = cheats(seen, rel_pos_part1)
    shorties2 = cheats(seen, rel_pos_part2)

    print("\033[1mPart1:\033[22m", shorties1)
    print("\033[1mPart2:\033[22m", shorties2)
    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
