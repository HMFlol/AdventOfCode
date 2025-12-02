# Solution for Advent of Code 2025, Day 1
# https://adventofcode.com/2025/day/1
from time import perf_counter


def part1(pos, moves):
    count = 0

    for dir, amt in moves:
        pos = (pos - amt) % 100 if dir == "L" else (pos + amt) % 100

        if pos == 0:
            count += 1

    return count


def part2(pos, moves):
    count = 0

    for dir, amt in moves:
        if dir == "L":
            count += amt // 100
            if pos != 0 and pos - (amt % 100) <= 0:
                count += 1
            pos = (pos - amt) % 100
        else:
            count += amt // 100
            if pos != 0 and pos + (amt % 100) >= 100:
                count += 1
            pos = (pos + amt) % 100

    return count


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    moves = [(line[0], int(line[1:])) for line in data]

    p1 = part1(50, moves)
    p2 = part2(50, moves)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
