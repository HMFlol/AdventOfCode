# Solution for Advent of Code 2024, Day 14
# https://adventofcode.com/2024/day/14
import re
from time import time

import numpy as np

WIDTH = 101
HEIGHT = 103


def safety(data):
    quads = [0, 0, 0, 0]

    for line in data.strip().splitlines():
        # grab the values with the same method as day13
        px, py, vx, vy = map(int, re.findall(r"(-?\d+)", line))
        # find next_x and next_y positions after 100 moves
        next_x = px + (vx * 100)
        next_y = py + (vy * 100)
        # % WIDTH and HEIGHT to keep the values within/wrapping the grid
        next_x = next_x % WIDTH
        next_y = next_y % HEIGHT
        # find the middle row and column of the grid
        mid_x = WIDTH // 2
        mid_y = HEIGHT // 2
        # if the next position is on the middle row or column, skip
        if next_x == mid_x or next_y == mid_y:
            continue
        # if the next position is in the top left quadrant, add 1 to that quadrant
        if next_x < mid_x and next_y < mid_y:
            quads[0] += 1
        # if the next position is in the top right quadrant, add 1 to that quadrant
        elif next_x > mid_x and next_y < mid_y:
            quads[1] += 1
        # if the next position is in the bottom left quadrant, add 1 to that quadrant
        elif next_x < mid_x and next_y > mid_y:
            quads[2] += 1
        # if the next position is in the bottom right quadrant, add 1 to that quadrant
        else:
            quads[3] += 1

    return quads[0] * quads[1] * quads[2] * quads[3]


def easteregg(data):
    positions, velocities = (
        np.array([list(map(int, re.findall(r"(-?\d+)", line)))[:2] for line in data.strip().splitlines()]),
        np.array([list(map(int, re.findall(r"(-?\d+)", line)))[2:] for line in data.strip().splitlines()]),
    )

    seconds = 0
    # Create the grid of 0s
    grid = np.zeros((HEIGHT, WIDTH), dtype=int)

    while True:
        seconds += 1
        # Calculate the new position after x seconds, modulo w and h to wrap
        new_positions = (positions + seconds * velocities) % [WIDTH, HEIGHT]
        # Get the unique positions and their counts
        _, counts = np.unique(new_positions, axis=0, return_counts=True)
        # If any position is occupied by more than 1 bot, continue to next iteration
        if np.any(counts > 1):
            continue
        # If all positions are unique, update the grid with the new positions
        for pos in new_positions:
            grid[pos[1], pos[0]] += 1
        # Print the grid for fun and return the number of seconds elapsed
        for row in grid:
            print("".join(map(str, row)).replace("0", ".").replace("1", "#"))
        return seconds


start_time = time()


data = open(0).read().strip()

print("Part1:", safety(data))
print("Part2:", easteregg(data))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
