from aocd import data
from time import time

# data = open('test.txt').read()

data = data.strip().split('\n\n')

grids = []

for grid in data:
    lines = grid.split('\n')
    grids.append(lines)


def reflections(grids):
    total = 0
    # Check rows
    for grid in grids:
        # Check rows starting at second row 
        for row in range(1, len(grid)):
            # Up is the row above current and up and down is the current row and down
            up = grid[:row][::-1]
            down = grid[row:]
            # Trim up and down to be the same length (if up or down is already shorter it has no effect)
            up = up[:len(down)]
            down = down[:len(up)]
            # Check if up and down are the same (Trimmed to the same length and up is reversed so you can compare)
            if up == down:
                total += row * 100
        # Transpose the grid and do the same thing
        grid = list(zip(*grid))
        for col in range(1, len(grid)):
            up = grid[:col][::-1]
            down = grid[col:]
            
            up = up[:len(down)] 
            down = down[:len(up)]
        
            if up == down:
                total += col

    return total

def morereflections(grids):
    total = 0
    # Check rows
    for grid in grids:
        for row in range(1, len(grid)):
            up = grid[:row][::-1]
            down = grid[row:]
            
            badboy = 0
            # zip up and down to check two corresponding rows at a time
            for x, y in zip(up, down):
                # zip x and y to check two i-th characters at a time
                for a, b in zip(x, y):
                    if a != b:
                        badboy += 1
            # If there is only one badboy between two rows then it's the one we're looking for
            if badboy == 1:
                total += row * 100

        grid = list(zip(*grid))
        for col in range(1, len(grid)):
            up = grid[:col][::-1]
            down = grid[col:]
            
            badboy = 0
            for x, y in zip(up, down):
                for a, b in zip(x, y):
                    if a != b:
                        badboy += 1

            if badboy == 1:
                total += col

    return total

starttime = time()

total1 = reflections(grids)
total2 = morereflections(grids)

print(f"Total (Part1): {total1}")
print(f"Total (Part2): {total2}")

endtime = time()
print(f"Total execution time: {endtime - starttime:.6f} seconds")