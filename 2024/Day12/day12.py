# Solution for Advent of Code 2024, Day 12
# https://adventofcode.com/2024/day/12

from time import time

from aocd import get_data

# Problem things go here :)

start_time = time()


def find_regions(grid):
    visited = set()
    regions = []

    for cell, char in grid.items():
        if cell in visited:
            continue
        region = set()
        stack = [cell]
        while stack:
            pos = stack.pop()
            if grid.get(pos) == char and pos not in visited:
                visited.add(pos)
                region.add(pos)
                for dir in (-1, 1, 1j, -1j):
                    next_pos = pos + dir
                    if grid.get(next_pos) == char and next_pos not in visited:
                        stack.append(next_pos)
        regions.append(region)

    return regions


def calculate_edge_price(region, grid):
    area = len(region)
    edges = 0
    for cell in region:
        for dir in (-1, 1, 1j, -1j):
            next_cell = cell + dir
            if grid.get(next_cell) != grid.get(cell):
                edges += 1
    return area * edges


# Thanks HN
def calculate_side_price(region):
    area = len(region)
    corner_candidates = set()
    # Ensure these are the correct order either clockwise or counterclockwise
    offsets = ((-0.5 - 0.5j), (-0.5 + 0.5j), (0.5 + 0.5j), (0.5 - 0.5j))
    corners = 0

    for pos in region:
        for offset in offsets:
            corner_candidates.add(pos + offset)

    for corner in corner_candidates:
        # Adjacent positions around the corner
        adjacent_positions = [corner + offset for offset in offsets]
        # Check if adjacent positions are in the region
        config = [adj_pos in region for adj_pos in adjacent_positions]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        elif number == 3:
            corners += 1

    return area * corners


def load_data(use_test_data=False):
    if use_test_data:
        with open("test.txt") as f:
            return f.read()
    else:
        return get_data(day=12, year=2024)


data = load_data(use_test_data=1)

# Parsing stuff
data = data.strip().splitlines()

grid = {col + row * 1j: val for row, line in enumerate(data) for col, val in enumerate(line)}

regions = find_regions(grid)

print("Part1:", sum(calculate_edge_price(region, grid) for region in regions))
print("Part2:", sum(calculate_side_price(region) for region in regions))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
