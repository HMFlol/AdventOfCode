'''
Using some of HNs method of sorting the grid, rather than my sorting method in P1.
Also moved things into functions.
'''
from aocd import get_data
from time import time
start_time = time()
data = get_data(day=14, year=2023)
#data = open('test.txt').read()
grid = tuple(data.splitlines())
#list(x) for x in zip(*grid[::-1])]
    
def moveUp():
    global grid
    #print('\n'.join(grid) + '\n')
    grid = tuple(map("".join, zip(*grid[::-1])))
    #print('\n'.join(grid) + '\n')
    grid = tuple("#".join(["".join(sorted(tuple(group))) for group in row.split("#")]) for row in grid)
    #print('\n'.join(grid) + '\n')
    '''grid = tuple(row[::-1] for row in grid)
    print('\n'.join(grid) + '\n')'''
    

def distances():
    distances = 0
    for r , row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'O':
                distances += len(grid) - r
    return distances

'''
Added math.
Count the cycles until we find a dupe grid
Then we can use the cycles to find the final grid state (happens at grid 119 it seems, for my input anyway)

'''
grids = {}
cycles = 1_000_000_000
cycle = 0
while cycle < cycles:
    cycle += 1
    for _ in range(4):
        moveUp()
    neo = tuple(tuple(row) for row in grid) # Convert to tuple of tuples so we can hash it
    if neo in grids: # If we've seen it before
        print(f"dupe ", cycle)
        cycle_length = cycle - grids[neo] # Calculate the cycle length (current cycle - cycle count when this was last seen)
        amt = (cycles - cycle) // cycle_length # Calculate how many cycles we can skip
        cycle += amt * cycle_length # Change cycle count by adding the amount we can skip
    grids[neo] = cycle # Add the grid to the dict with the cycle count as the value

# Then we calculate distance as in p1
distance = distances()

print(f"Total (Part2):", distance)
end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")