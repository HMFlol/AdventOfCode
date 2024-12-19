# Solution for Advent of Code 2024, Day 8
# https://adventofcode.com/2024/day/8

from itertools import combinations
from time import time

data = open(0).read().strip()
# data = open("test.txt").read()
data = data.strip().splitlines()

grid = {complex(col, row): val for row, line in enumerate(data) for col, val in enumerate(line)}

# row and col length
rows = int(max(pos.imag for pos in grid)) + 1
cols = int(max(pos.real for pos in grid)) + 1

# Yoink the antenna positions
antennas = {}
for pos, val in grid.items():
    if val != ".":
        antennas.setdefault(val, []).append(pos)


# Part 1
def antinodes(antennas):
    antinodes = set()
    for antenna in antennas.values():
        # Use combinations to grab the unique pairs without repetition
        for ant1, ant2 in combinations(antenna, 2):
            # Add an antinode in each direction
            antinodes.add(2 * ant1 - ant2)
            antinodes.add(2 * ant2 - ant1)
    # Return the number of antinodes within the grid
    return len([0 for pos in antinodes if 0 <= pos.imag < rows and 0 <= pos.real < cols])


# Part 2
def resonance(antennas):
    antinodes = set()
    for antenna in antennas.values():
        for ant1, ant2 in combinations(antenna, 2):
            # Find the difference and add all possible positions one way
            diff1 = ant2 - ant1
            pos1 = ant1
            while 0 <= pos1.imag < rows and 0 <= pos1.real < cols:
                antinodes.add(pos1)
                pos1 += diff1
            # And add them all the other way
            diff2 = ant1 - ant2
            pos2 = ant2
            while 0 <= pos2.imag < rows and 0 <= pos2.real < cols:
                antinodes.add(pos2)
                pos2 += diff2
    # Return the number of antinodes
    return len(antinodes)


start_time = time()

print("Part1:", antinodes(antennas))
print("Part2:", resonance(antennas))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
