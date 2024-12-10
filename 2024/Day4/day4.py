from time import time

from aocd import get_data

data = get_data(day=4, year=2024)
# data = open('test.txt').read()
grid = data.splitlines()


# Part 1
def searchxmas(grid):
    count = 0
    # All eight possible directions
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "X":
                for dx, dy in directions:
                    x, y = row, col
                    k = 0
                    while k < len("XMAS"):
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "XMAS"[k]:
                            x += dx
                            y += dy
                            k += 1
                        else:
                            break
                    if k == len("XMAS"):
                        count += 1
    return count


# Part 2
def searchx_mas(grid):
    count = 0
    # only need to check diagonal directions
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "A":
                counts = {"M": 0, "S": 0}
                for dx, dy in diagonals:
                    x, y = row + dx, col + dy
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] in counts:
                        counts[grid[x][y]] += 1
                # checking that the corners have 2 M's and 2 S's
                if counts["M"] == 2 and counts["S"] == 2:
                    # Diagonal from top-left to bottom-right
                    diag1 = grid[row - 1][col - 1] + grid[row][col] + grid[row + 1][col + 1]
                    # Diagonal from top-right to bottom-left
                    diag2 = grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1]
                    # checking that the diagonals are MAS or SAM and not SAS or MAM
                    if diag1 in ("MAS", "SAM") and diag2 in ("MAS", "SAM"):
                        count += 1

    return count


start_time = time()

print("Part1:", searchxmas(grid))
print("Part2:", searchx_mas(grid))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
