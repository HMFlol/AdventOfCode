# Solution for Advent of Code 2024, Day 11
# https://adventofcode.com/2024/day/11

import functools
from time import time


@functools.cache  # Use cache to store the results of the function
def stonecalc(stone, blinks):
    # When blinks = 0 we have finished recursing and have a valid stone, so we return 1
    if blinks == 0:
        return 1
    # if stone = 0 it becomes 1 with one fewer blink
    elif stone == 0:
        newstones = stonecalc(1, blinks - 1)
    # if the length of the stone number is even
    # split it in half and recurse on both halves with one fewer blink
    elif len(str(stone)) % 2 == 0:
        middle = len(str(stone)) // 2
        left = int(str(stone)[:middle])
        right = int(str(stone)[middle:])
        newstones = stonecalc(left, blinks - 1) + stonecalc(right, blinks - 1)
    # else multiply the stone by 2024 and recruse with one fewer blink
    else:
        newstones = stonecalc(stone * 2024, blinks - 1)

    return newstones


start_time = time()

data = open(0).read().strip()

data = [int(num) for num in data.split()]

p1 = sum(stonecalc(stone, 25) for stone in data)
p2 = sum(stonecalc(stone, 75) for stone in data)

print("Part1:", p1)
print("Part2:", p2)

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
