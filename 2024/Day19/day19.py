# Solution for Advent of Code 2024, Day 19
# https://adventofcode.com/2024/day/19

import re
from functools import cache
from time import time

from aocd import get_data


@cache
def lets_towel(design):
    if not design:
        return 1
    return sum(design.startswith(pattern) and lets_towel(design[len(pattern) :]) for pattern in patterns)


start_time = time()


def load_data(use_test_data=False):
    if use_test_data:
        with open("test.txt") as f:
            return f.read()
    else:
        return get_data(day=19, year=2024)


data = load_data(use_test_data=0)
# Parsing stuff
patterns, designs = data.split("\n\n")[0].split(", "), data.split("\n\n")[1].split("\n")

makeable = [lets_towel(design) for design in designs]

print("Part1:", len([towel for towel in makeable if towel]))
print("Part2:", sum(makeable))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
