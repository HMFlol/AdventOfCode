# Solution for Advent of Code 2024, Day 19
# https://adventofcode.com/2024/day/19
import re
from functools import cache
from time import perf_counter


@cache
def lets_towel(design):
    if not design:
        return 1
    return sum(design.startswith(pattern) and lets_towel(design[len(pattern) :]) for pattern in patterns)


start_time = perf_counter()

data = open(0).read().strip()
# Parsing stuff
patterns, designs = data.split("\n\n")[0].split(", "), data.split("\n\n")[1].split("\n")

makeable = [lets_towel(design) for design in designs]

print("\033[1mPart1:\033[22m", len([towel for towel in makeable if towel]))
print("\033[1mPart2:\033[22m", sum(makeable))

end_time = perf_counter()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
