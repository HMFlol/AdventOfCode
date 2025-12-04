# Solution for Advent of Code 2025, Day 4
# https://adventofcode.com/2025/day/4
from time import perf_counter

"""def print_grid(grid_dict):
    Print grid_dict in a readable format.
    if not grid_dict:
        return

    # Find dimensions
    max_row = int(max(pos.imag for pos in grid_dict))
    max_col = int(max(pos.real for pos in grid_dict))

    # Print row by row
    for row in range(max_row + 1):
        line = ""
        for col in range(max_col + 1):
            line += grid_dict.get(col + row * 1j, " ")
        print(line)
    print()  # Empty line after grid
    """


def part1(grid_dict, directions):
    accessible = 0
    for pos, char in grid_dict.items():
        if char == "@":
            # Count neighbours that are also "@" using sum with generator
            neighbor_count = sum(grid_dict.get(pos + d) == "@" for d in directions)
            if neighbor_count < 4:
                accessible += 1

    return accessible


def part2(grid_dict, directions):
    removed_list = []
    for pos, char in grid_dict.items():
        if char == "@":
            # Count neighbours that are also "@" using sum with a generator
            neighbor_count = sum(grid_dict.get(pos + d) == "@" for d in directions)
            if neighbor_count < 4:
                removed_list.append(pos)
    # If there is stuff that can be removed, replace it with "." and call part 2 again, adding the number of removed cells because math
    if removed_list:
        for cell in removed_list:
            grid_dict[cell] = "."
        return len(removed_list) + part2(grid_dict, directions)

    return 0  # Base case: no more to remove


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()
    grid = data.splitlines()

    # Build a dictionary mapping complex positions to characters (Real = col, Imaginary = row)
    grid_dict = {col + row * 1j: char for row, line in enumerate(grid) for col, char in enumerate(line)}

    # 8 directions using complex numbers (1 = right, -1 = left, 1j = down, -1j = up)
    directions = [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]

    p1 = part1(grid_dict, directions)
    p2 = part2(grid_dict, directions)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
