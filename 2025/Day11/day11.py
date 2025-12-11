# Solution for Advent of Code 2025, Day 11
# https://adventofcode.com/2025/day/11
from functools import cache
from time import perf_counter


def count_paths(devices, current, end, visited=frozenset()):
    # Base case
    if current == end:
        return 1
    # Mark current device as visited
    new_visited = visited | {current}
    # Count paths through all neighbours
    return sum(count_paths(devices, neighbour, end, new_visited) for neighbour in devices.get(current, []))


def count_paths_through_nodes(devices, start, end, required_nodes):
    """Count paths from start to end that visit all required_nodes."""

    @cache
    def dfs(current, remaining_required):
        # Base case: reached end
        if current == end:
            return 1 if not remaining_required else 0
        # Update remaining required nodes
        new_remaining = remaining_required - {current}
        # Count paths through neighbors
        return sum(dfs(neighbour, new_remaining) for neighbour in devices.get(current, []))

    return dfs(start, frozenset(required_nodes))


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    devices = {(parts := device.split(": "))[0]: parts[1].split(" ") for device in data}

    p1 = count_paths(devices, "you", "out")
    p2 = count_paths_through_nodes(devices, "svr", "out", {"dac", "fft"})

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
