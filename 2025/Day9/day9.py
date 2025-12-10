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


def part2(tiles):
    """
    Find the largest axis-aligned rectangle using two vertices from the polygon that is completely contained within the polygon.

    APPROACH:
    1. Build a grid representation of the polygon using coordinate compression
    2. Use a scanline algorithm to mark which grid cells are inside the polygon
    3. Use 2D prefix sums for fast rectangle area queries
    4. Test all possible rectangles formed by pairs of polygon vertices
    """
    # STEP 1: Convert tiles to polygon vertices
    # Each tile coordinate becomes a vertex of our polygon
    points = []
    for tile in tiles:
        points.append((tile[0], tile[1]))

    # STEP 2: COORDINATE COMPRESSION
    # Problem: If coordinates range from 0 to 1,000,000, we can't make a 1M x 1M grid
    # Solution: Map coordinates to a smaller grid where only unique x/y values matter
    # Example: If x-coords are [5, 100, 500], we map them to grid indices [0, 1, 2]

    # Get all unique X and Y coordinates from vertices and sort them
    unique_x = sorted({p[0] for p in points})
    unique_y = sorted({p[1] for p in points})

    # Create mappings: actual coordinate → grid index
    x_map = {x: i for i, x in enumerate(unique_x)}
    y_map = {y: i for i, y in enumerate(unique_y)}

    # Grid dimensions: Number of "cells" between consecutive coordinates
    # If we have 4 unique x-values, we have 3 intervals (cells) between them
    cols = len(unique_x) - 1
    rows = len(unique_y) - 1

    # Create empty grid: 0 = outside polygon, 1 = inside polygon
    grid = [[0] * cols for _ in range(rows)]

    # STEP 3: Fill the grid using SCANLINE ALGORITHM
    # Key insight: For a polygon, a horizontal line crosses an odd number of
    # vertical edges when inside, and even number when outside

    # Create list of polygon edges by connecting consecutive vertices
    edges = []
    num_points = len(points)
    for i in range(num_points):
        p1 = points[i]
        p2 = points[(i + 1) % num_points]  # Connect last point back to first
        edges.append((p1, p2))

    # Process each horizontal "strip" (row) in our compressed grid
    for r in range(rows):
        # This row represents all y-values between unique_y[r] and unique_y[r+1]
        # Use the midpoint to test which edges intersect this horizontal strip
        mid_y = (unique_y[r] + unique_y[r + 1]) / 2.0

        # Find all VERTICAL edges that this horizontal line crosses
        intersecting_x = []
        for p1, p2 in edges:
            # Only consider vertical edges (both endpoints have same x-coordinate)
            if p1[0] == p2[0]:
                y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
                # Check if this strip's y-range intersects the edge's y-range
                if y_min < mid_y < y_max:
                    intersecting_x.append(p1[0])

        # Sort the x-coordinates where we cross vertical edges
        intersecting_x.sort()

        # POLYGON FILL RULE: Between pairs of crossings = inside the polygon
        # Cross 1st edge: entering polygon. Cross 2nd edge: exiting polygon.
        for k in range(0, len(intersecting_x), 2):
            x_start = intersecting_x[k]  # Enter polygon here
            x_end = intersecting_x[k + 1]  # Exit polygon here

            # Convert physical coordinates to grid column indices
            c_start = x_map[x_start]
            c_end = x_map[x_end]

            # Mark all grid cells in this row between c_start and c_end as "inside"
            for c in range(c_start, c_end):
                grid[r][c] = 1

    # STEP 4: Build 2D PREFIX SUM for fast rectangle queries
    # prefix[r][c] = total count of 1's in rectangle from (0,0) to (r-1,c-1)
    # This lets us query any rectangle sum in O(1) time instead of O(rows*cols)

    # Use (rows+1) x (cols+1) to avoid index-out-of-bounds when querying
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Build the prefix sum array using inclusion-exclusion principle
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            prefix[r][c] = (
                grid[r - 1][c - 1]  # Current cell
                + prefix[r - 1][c]  # Sum above
                + prefix[r][c - 1]  # Sum to left
                - prefix[r - 1][c - 1]
            )  # Subtract overlap (counted twice)

    def get_sum(r1, c1, r2, c2):
        """
        Get the sum of grid values in rectangle from (r1,c1) to (r2,c2) exclusive.

        Uses inclusion-exclusion principle on prefix sums.
        """
        return prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]

    # STEP 5: Test all rectangles formed by pairs of polygon vertices
    max_area = 0

    # Try every possible pair of vertices as opposite corners of a rectangle
    for i in range(len(points)):
        p1 = points[i]
        for j in range(i + 1, len(points)):
            p2 = points[j]

            # Form axis-aligned rectangle with p1 and p2 as opposite corners
            x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
            y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])

            # Convert physical coordinates to compressed grid indices
            c_start, c_end = x_map[x1], x_map[x2]
            r_start, r_end = y_map[y1], y_map[y2]

            # Calculate how many grid cells should be filled if rectangle is fully inside
            expected_count = (c_end - c_start) * (r_end - r_start)

            # Query how many grid cells are actually marked as "inside polygon"
            actual_count = get_sum(r_start, c_start, r_end, c_end)

            # If all cells in this rectangle are inside the polygon, it's valid!
            if actual_count == expected_count:
                # Calculate the physical area (in original coordinate space)
                # Add 1 because coordinates are inclusive (e.g., from x=0 to x=3 is 4 units)
                physical_area = abs(x2 - x1 + 1) * abs(y2 - y1 + 1)
                max_area = max(max_area, physical_area)

    return max_area  # Get the bounding box


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    tiles = [tuple(map(int, line.split(","))) for line in data]

    p1 = part1(tiles)
    p2 = part2(tiles)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
