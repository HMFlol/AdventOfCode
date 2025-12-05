# Solution for Advent of Code 2025, Day 5
# https://adventofcode.com/2025/day/5
from time import perf_counter


def sofresh(ing_id_ranges, ing_ids):
    count = 0

    for ing_id in ing_ids:
        if any(lower <= ing_id <= upper for lower, upper in ing_id_ranges):
            count += 1

    return count


def unique_ids(ing_id_ranges):
    unique_ids = {num for lower, upper in ing_id_ranges for num in range(lower, upper + 1)}

    return len(unique_ids)


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()

    ing_id_ranges, ing_ids = [line.split() for line in data.split("\n\n")]
    ing_ids = [int(s) for s in ing_ids]
    ing_id_ranges = [tuple(map(int, num.split("-"))) for num in ing_id_ranges]

    p1 = sofresh(ing_id_ranges, ing_ids)
    p2 = unique_ids(ing_id_ranges)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
