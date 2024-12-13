# Solution for Advent of Code 2024, Day 13
# https://adventofcode.com/2024/day/13

import re
from time import time

from aocd import get_data


# Part 1 + 2
def find_spend(section):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", section))
    # I swear I tried to use the above line initially and it didn't work.. I think I forgot the + in the regex :(
    """ pattern = r"Button A: X\\+(\\d+), Y\\+(\\d+)\nButton B: X\\+(\\d+), Y\\+(\\d+)\nPrize: X=(\\d+), Y=(\\d+)"
    match = re.findall(pattern, section)
    ax, ay, bx, by, px, py = map(int, match[0]) """
    big_px, big_py = px + 10**13, py + 10**13

    # Cramers Rule
    a_presses1 = (px * by - py * bx) / (ax * by - ay * bx)
    b_presses1 = (ax * py - ay * px) / (ax * by - ay * bx)

    a_presses2 = (big_px * by - big_py * bx) / (ax * by - ay * bx)
    b_presses2 = (ax * big_py - ay * big_px) / (ax * by - ay * bx)

    spend1 = int(a_presses1) * 3 + int(b_presses1) if a_presses1.is_integer() and b_presses1.is_integer() else 0
    spend2 = int(a_presses2) * 3 + int(b_presses2) if a_presses2.is_integer() and b_presses2.is_integer() else 0

    return spend1, spend2


start_time = time()


def load_data(use_test_data=False):
    if use_test_data:
        with open("test.txt") as f:
            return f.read()
    else:
        return get_data(day=13, year=2024)


data = load_data(use_test_data=0)

total_p1, total_p2 = 0, 0

for section in data.strip().split("\n\n"):
    spend1, spend2 = find_spend(section)
    total_p1 += spend1
    total_p2 += spend2

print("Part1:", total_p1)
print("Part2:", total_p2)

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
