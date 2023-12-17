from aocd import get_data
from time import time
from heapq import heappop, heappush # used for priority queue - https://docs.python.org/3/library/heapq.html

data = get_data(day=17, year=2023)
# data = open('test.txt').read()
data = data.strip().splitlines()

grid = {complex(x,y): int(val) for y, row in enumerate(data) for x, val in enumerate(row)}
end = [*grid][-1]

def shorty(min, max): # min and max are the range of steps we can take
    q = [(0,0,0,1), (0,0,0,1j)] # starting heat, id, pos, dir
    path = set() # keep track of where we have been
    id = 0 # unique id's 

    while q:
        heat, _, pos, dir = heappop(q) # pop heat, pos and dir from q
        if pos == end: # if we are at the bottom corner retur heat
            return heat
        if (pos, dir) in path: # if we have been here before, skip to the next thing in the q
            continue
        path.add((pos, dir)) # otherwise, add this pos and dir to the path

        for dir in [dir*1j, -dir*1j]: # turning left and right
            for steps in range(min, max+1): # range of steps we can take
                if pos + dir * steps in grid: # if our position + direction * steps we can  take is actually in the grid and not out of bounds...
                    totalheat = sum(grid[pos + dir*j] for j in range(1, steps+1)) # sum up the heat of all positions along the path from the current position to the end position
                    heappush(q, (heat+totalheat, (id:=id+1), pos + dir*steps, dir)) #  push a new state to the priority q, with the total heat cost of the path, a unique id, the new position, and the current directions.  := is the walrus operator, which assigns a value to a variable and returns that value.  It's used here to increment the id variable and return the new value.
        
start_time = time()

print(f"Total (Part1):", shorty(1, 3))
print(f"Total (Part2):", shorty(4, 10))

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")
'''
The function shorty returns the correct heat number by using a priority queue to always process the state with the smallest heat (or cost) first, and by keeping track of visited states to avoid processing them again.

The heat of a state is the total cost of reaching the current position from the starting position. It's calculated by summing up the values in the grid at all positions along the path from the starting position to the current position.

When the function starts, it initializes the queue with two states representing the starting position, each with a heat of 0. Then it enters a loop that continues until the queue is empty.

In each iteration of the loop, it pops a state from the queue and checks if the current position is the end position. If it is, the function returns the heat of the current state, which represents the cost of the shortest path found.

If the current position is not the end position, the function generates new states by considering two possible directions of movement (a 90-degree rotation to the left and a 90-degree rotation to the right from the current direction) and a range of possible steps to move in each direction.

For each new state, it calculates the total heat of reaching the new position by summing up the values in the grid at all positions along the path from the current position to the new position. Then it pushes the new state onto the queue with the total heat, a unique identifier, the new position, and the current direction.

The heappop and heappush functions are used to pop and push states from and onto the queue, respectively. These functions ensure that the queue is always sorted in order of increasing total heat, so the state with the lowest total heat is always considered next. This is a characteristic of priority queues and is key to how the algorithm works.

So, by always processing the state with the smallest heat first and by keeping track of visited states to avoid processing them again, the function ensures that when it finds a path to the end position, it's the path with the smallest total heat, and it returns this heat as the result.
'''