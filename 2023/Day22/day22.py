from aocd import get_data
from time import time
from collections import defaultdict

data = get_data(day=22, year=2023)
# data = open('test.txt').read()
data = data.strip().splitlines()

bricks = [] # created a list of the bricks, sorted by z value
for line in data:
    coords = list(map(int, line.replace('~', ',').split(',')))
    bricks.append(coords)
bricks = sorted(bricks, key=lambda x: x[2]) # sort the bricks by z value

n = len(bricks) # how many bricks we have

'''
This will stack the bricks. For the first call, below the function, it defaults to none being skipped. 

Then, in the subsequent loop, imFalling(bricks.copy(), skip=i) is called with each brick being skipped once. This simulates the scenarios where each brick is removed from the system one at a time. The function checks to see if any of the remaining bricks fall due to the removal of the current brick.

The results of these simulations are stored in a list. The script then calculates the sum of the first and second elements of each tuple in the results list, which represent the total number of simulations where no bricks have fallen and the total number of fallen bricks, respectively.

We return a boolean value and the number of fallen bricks. If fallen is 0 (meaning no bricks have fallen), not fallen will be True. If fallen is any positive integer (meaning at least one brick has fallen), not fallen will be False.

So, the return not fallen, fallen statement is returning a tuple of two values: a boolean indicating whether no bricks have fallen, and the total number of fallen bricks.
'''

def imFalling(bricks, skip = None):
    tower = defaultdict(int) # track the x,y 
    fallen = 0

    for i, (x1,y1,z1, x2,y2,z2) in enumerate(bricks):
        if i == skip:
            continue

        brick = [] # building a brick
        for a in range(x1, x2+1): # building a brick
            for b in range(y1, y2+1): # building a brick
                brick.append((a, b)) # building a brick

        height = max(tower[a] for a in brick) + 1 # calculate new height for current brick (max positions covered in the tower + 1)
        for b in brick: # update z heights  - tower height plus the bricks height
            tower[b] = height + z2 - z1

        bricks[i] = (x1,y1,height, x2,y2,height+z2-z1) # update the new z coords for the brick

        fallen += height < z1 # if the height is less than the original z coord, the brick fell

    return not fallen, fallen # return the number that fell and did not fall. not fallen is part 1, fallen is part 2


start_time = time()

imFalling(bricks) # drop the bricks once to get their tower positions before we do stuff

results = [imFalling(bricks.copy(), skip=i) for i in range(n)]
'''
Test data results look like this:

[(False, 6), (True, 0), (True, 0), (True, 0), (True, 0), (False, 1), (True, 0)]

False = 0 and True =  1, so we can just sum the first and second elements of each tuple and get the total number of bricks that fell(if they did) (from False) as well as the total number of bricks we can remove and not have any bricks fall(True results).
'''
part1, part2 = map(sum, zip(*results)) 

print(f"Total (Part1): {part1}")
print(f"Total (Part2): {part2}")

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")