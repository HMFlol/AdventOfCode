import time
import math
# timer stuff
start_time = time.time()

# Open the file and break the two lines into time and dist
times, dists = open('input.txt').read().split("\n")

# Get those digits
times = [int(t) for t in times.split()[1:]]
dists = [int(d) for d in dists.split()[1:]]

# Cool trick!
#print(sum([b*(100-b) > 100 for b in range(100)]))

# Part 1
def numways(time, dist):
    # Initialize a list to store the number of ways to get to each destination
    numways = []
    # Iterate over each time and distance pair and calculate the number of ways to get to the destination, zip() is used to iterate over both lists at the same time
    for time, dist in zip(time, dist):
        # button * (time = button) > dist for whatever the range of time is
        # So, if time = 1 and dist = 1, then 1 * (1 - 1) > 1 is False
        # If time = 2 and dist = 1, then 1 * (2 - 1) > 1 is False, but 2 * (2 - 1) > 1 is True
        # This will give the number of ways to win, which is appended to the list
        ways = sum([b*(time-b) > dist for b in range(time)])
        numways.append(ways)


    result = 1 # Cuz you can't start multiplying with 0 and you gotta start somewhere ya know what I mean dog? (づ￣ 3￣)づ
    for ways in numways:
        result *= ways

    return result

# Part 2    
def part2(time, dist):  
    # Convert the lists of digits to integers
    time = int(''.join(map(str, time)))
    dist = int(''.join(map(str, dist)))
    # same as p1 but no loop needed, just the one calculation
    ways = sum([b*(time-b) > dist for b in range(time)])
    # Solve the quadratic equation to get the number of ways to win LOLOLOLOL
    # alpha = (-time + math.sqrt(time*time - 4*dist)) / -2
    # beta = (-time - math.sqrt(time*time - 4*dist)) / -2
    # ways = sum(1 for i in range(math.ceil(alpha), math.floor(beta)+1))

    return ways

# Call the functions
print(f"Part 1: {numways(times, dists)}")
print(f"Part 2: {part2(times, dists)}")
# Or, you can do this and use the exact same function for both parts
# print(f"Part 2: {numways([int(''.join(map(str, times)))], [int(''.join(map(str, dists)))])}")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution Time: {elapsed_time} seconds")
