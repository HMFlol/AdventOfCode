# Solution for Advent of Code 2025, Day 8
# https://adventofcode.com/2025/day/8
from collections import defaultdict
from time import perf_counter


def calculate_distances(points):
    # Calculate all Euclidean distances between points
    distances = []
    num_points = len(points)

    for i in range(num_points):
        for j in range(i + 1, num_points):
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            euclidean_dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
            distances.append((euclidean_dist, i, j))

    return sorted(distances)


def find(parent, x):
    # Find root with path compression.
    if x == parent[x]:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    # Union two sets.
    root_x = find(parent, x)
    root_y = find(parent, y)
    parent[root_x] = root_y


def get_group_sizes(parent):
    # Get sizes of all connected components.
    sizes = defaultdict(int)
    # Count members in each group.
    for x in parent:
        sizes[find(parent, x)] += 1
    # Return sizes of all groups.
    return list(sizes.values())


def part1(points, distances):
    # Calculate product of three largest groups after 1000 connections.
    parent = {i: i for i in range(len(points))}
    # Connect first 1000 closest pairs.
    for t in range(1000):
        _, i, j = distances[t]
        # Union the two points if they are not already connected.
        if find(parent, i) != find(parent, j):
            union(parent, i, j)
    # Get sizes of all groups and find the three largest.
    sorted_sizes = sorted(get_group_sizes(parent))

    return sorted_sizes[-1] * sorted_sizes[-2] * sorted_sizes[-3]


def part2(points, distances):
    # Find product of coordinates with all connections made.
    parent = {i: i for i in range(len(points))}
    connections = 0

    for _, i, j in distances:
        # Union the two points if they are not already connected and count the conneciton
        if find(parent, i) != find(parent, j):
            connections += 1
            union(parent, i, j)
            # If all points are connected, return the product of the x coordinates of the last two junction boxes
            if connections == len(points) - 1:
                return points[i][0] * points[j][0]


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()
    points = [tuple(map(int, line.split(","))) for line in data]
    distances = calculate_distances(points)

    p1 = part1(points, distances)
    p2 = part2(points, distances)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
