# Solution for Advent of Code 2025, Day 7
# https://adventofcode.com/2025/day/7
import functools
from time import perf_counter


def part1(grid_dict, pos, down, left, right):
    # 8 directions using complex numbers (1 = right, -1 = left, 1j = down, -1j = up)
    # directions = [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]
    stack = [pos]
    count = 0

    while stack:
        next_pos = stack.pop(0) + down

        if next_pos not in grid_dict:
            continue

        if grid_dict.get(next_pos) == "^":
            # Only add if not already seen
            if next_pos + left not in stack:
                stack.append(next_pos + left)
            if next_pos + right not in stack:
                stack.append(next_pos + right)
            count += 1
        else:
            # Only add if not already seen
            if next_pos not in stack:
                stack.append(next_pos)

    return count


def part2(grid_dict, pos, down, left, right):
    # Use recursive DFS with memoization to count unique paths
    @functools.lru_cache
    def count_paths(current_pos):
        """Count all unique timeline paths from current position."""
        next_pos = current_pos + down
        # If out of bounds, this is one complete timeline
        if next_pos not in grid_dict:
            return 1

        if grid_dict.get(next_pos) == "^":
            # Quantum split: count paths from BOTH directions
            left_paths = count_paths(next_pos + left)
            right_paths = count_paths(next_pos + right)
            return left_paths + right_paths
        else:
            # Continue straight down
            return count_paths(next_pos)

    return count_paths(pos)


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()
    grid = data.splitlines()

    # Build a dictionary for the grid using complex numbers
    grid_dict = {col + row * 1j: char for row, line in enumerate(grid) for col, char in enumerate(line)}

    pos = [key for key, val in grid_dict.items() if val == "S"][0]
    down, left, right = 1j, -1, 1

    p1 = part1(grid_dict, pos, down, left, right)
    p2 = part2(grid_dict, pos, down, left, right)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
