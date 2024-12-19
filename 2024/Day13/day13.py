# Solution for Advent of Code 2024, Day 13
# https://adventofcode.com/2024/day/13

import re
from time import time


# Part 1 + 2
def find_spend(section, add=0):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", section))
    px, py = px + add, py + add

    # Cramers Rule
    a_presses = (px * by - py * bx) / (ax * by - ay * bx)
    b_presses = (ax * py - ay * px) / (ax * by - ay * bx)

    return int(a_presses) * 3 + int(b_presses) if a_presses.is_integer() and b_presses.is_integer() else 0


start_time = time()


data = open(0).read().strip()

print("Part1:", sum(find_spend(section) for section in data.strip().split("\n\n")))
print("Part2:", sum(find_spend(section, 10**13) for section in data.strip().split("\n\n")))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
