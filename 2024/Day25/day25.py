# Solution for Advent of Code 2024, Day 25
# https://adventofcode.com/2024/day/25
from time import perf_counter


def get_heights(lines):
    """Return the heights of the locks and keys."""
    rot_lines = zip(*lines[::-1])

    heights = [sum(c == "#" for c in col) - 1 for col in rot_lines]

    return heights


def find_uniques(lock_heights, key_heights):
    """Return the unique combos of the locks and keys."""
    total = 0

    for lh in lock_heights:
        for kh in key_heights:
            if all(p + k <= 5 for p, k in zip(lh, kh)):
                total += 1

    return total


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()
    locksnkeys = data.split("\n\n")

    locks = [lock.splitlines() for lock in locksnkeys if lock.startswith("#")]
    keys = [key.splitlines() for key in locksnkeys if key.startswith(".")]

    lock_heights = [get_heights(lock) for lock in locks]
    key_heights = [get_heights(key) for key in keys]

    p1 = find_uniques(lock_heights, key_heights)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", "<3")

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
