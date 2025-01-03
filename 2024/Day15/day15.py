# Solution for Advent of Code 2024, Day 15
# https://adventofcode.com/2024/day/15

from time import time


def warehouse(grid, moves):
    grid = {col + row * 1j: val for row, line in enumerate(grid) for col, val in enumerate(line)}
    moves = moves.replace("\n", "")
    (robot,) = [pos for pos in grid if grid[pos] == "@"]
    dirs = {"<": -1, ">": 1, "^": -1j, "v": 1j}

    for move in moves:
        boxline = []
        stack = [robot]
        for pos in stack:
            if grid[pos] == "#":  # Hit a wall
                break
            if grid[pos] == ".":  # Empty space or robot
                continue
            pos += dirs[move]
            boxline += [pos]
            stack += [pos]
        else:  # Do the moves if no wall was hit
            moved = set()
            for box in boxline[::-1]:
                if box in moved:
                    continue
                moved.add(box)
                grid[box], grid[box - dirs[move]] = grid[box - dirs[move]], grid[box]
            robot += dirs[move]

    final_positions = sum(pos for pos in grid if grid[pos] == "O")
    return int(final_positions.real + final_positions.imag * 100)


def embiggen(grid, moves):
    # Expanding the grid
    expand = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    expanded_grid = []

    for line in grid:
        expanded_line = "".join(expand.get(char, char) for char in line)
        expanded_grid.append(expanded_line)
    # Creating the new expanded grid
    grid = {col + row * 1j: val for row, line in enumerate(expanded_grid) for col, val in enumerate(line)}

    moves = moves.replace("\n", "")
    (robot,) = [pos for pos in grid if grid[pos] == "@"]
    dirs = {"<": -1, ">": 1, "^": -1j, "v": 1j}

    for move in moves:
        boxline = []
        stack = [robot]
        for pos in stack:
            if grid[pos] == "#":
                break
            if grid[pos] == ".":
                continue
            pos += dirs[move]
            boxline += [pos]
            stack += [pos]
            if dirs[move].imag and grid[pos] == "[":  # If movement is vertical and we hit the left side of a box
                stack += [pos + 1]  # Add right side of wide box
            if dirs[move].imag and grid[pos] == "]":  # Like above but for right side of box
                stack += [pos - 1]  # Add left side of wide box

        else:  # Do the moves if no wall was hit
            moved = set()
            for box in boxline[::-1]:
                if box in moved:
                    continue
                moved.add(box)
                grid[box], grid[box - dirs[move]] = grid[box - dirs[move]], grid[box]
            robot += dirs[move]

    final_positions = sum(pos for pos in grid if grid[pos] in "[")
    return int(final_positions.real + final_positions.imag * 100)


start_time = time()


data = open(0).read().strip()

# Parsing stuff
grid, moves = data.strip().split("\n\n")
grid = grid.strip().splitlines()


print("\033[1mPart1:\033[22m:", warehouse(grid, moves))
print("\033[1mPart2:\033[22m:", embiggen(grid, moves))

end_time = time()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
