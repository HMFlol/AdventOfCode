# Solution for Advent of Code 2025, Day 9
# https://adventofcode.com/2025/day/9
from time import perf_counter


def part1(tiles):
    rectangles = []
    num_tiles = len(tiles)

    for i in range(num_tiles):
        for j in range(i + 1, num_tiles):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            rectangle = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
            rectangles.append(rectangle)

    return max(rectangles)


def part2(tiles, edges):
    pass


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    tiles = [tuple(map(int, line.split(","))) for line in data]

    edges = []
    # build edges of the polygon by creating tuples of the points in order
    for i in range(len(tiles)):
        start = tiles[i]
        end = tiles[(i + 1) % len(tiles)]
        edges.append((start, end))

    p1 = part1(tiles)
    p2 = part2(tiles, edges)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", "p2")

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
