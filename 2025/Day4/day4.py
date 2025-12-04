# Solution for Advent of Code 2025, Day 4
# https://adventofcode.com/2025/day/4
from time import perf_counter


def part1(grid_dict, directions):
    accessible = 0
    for pos in grid_dict:
        # Count neighbours by checking if neighbor position exists in dict
        neighbor_count = sum((pos + d) in grid_dict for d in directions)
        if neighbor_count < 4:
            accessible += 1

    return accessible


def part2(grid_dict, directions):
    removed_list = []
    for pos in grid_dict:
        # Count neighbours by checking if neighbor position exists in dict
        neighbor_count = sum((pos + d) in grid_dict for d in directions)
        if neighbor_count < 4:
            removed_list.append(pos)

    # If there is stuff that can be removed, delete those keys and recurse
    if removed_list:
        for cell in removed_list:
            del grid_dict[cell]
        return len(removed_list) + part2(grid_dict, directions)

    return 0  # Base case: no more to remove


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()
    grid = data.splitlines()

    # Build a dictionary with ONLY "@" positions (Real = col, Imaginary = row)
    grid_dict = {col + row * 1j: char for row, line in enumerate(grid) for col, char in enumerate(line) if char == "@"}

    # 8 directions using complex numbers (1 = right, -1 = left, 1j = down, -1j = up)
    directions = [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]

    p1 = part1(grid_dict, directions)
    p2 = part2(grid_dict, directions)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
