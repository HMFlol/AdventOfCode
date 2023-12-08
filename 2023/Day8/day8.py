from functools import reduce
from math import gcd
import time
# timer stuff
start_time = time.time()

# Open the file and break the two lines into time and dist
with open('input.txt','r') as i:
    lines = i.read().splitlines()

# Extract steps and nodes
steps = lines[0]
nodes = lines[2:]

# Process nodes and stick in a dictionary
nodesdict = {}
for node in nodes:
        nodeparts = node.split('=')
        nodename = nodeparts[0].strip()
        nodelr = nodeparts[1].strip().strip('()').split(', ')
        nodesdict[nodename] = nodelr

def notspooky(steps, nodesdict):

    cnode = 'AAA'

    stepcount = 0
    stepindex = 0

    while cnode != 'ZZZ':
        step = steps[stepindex]
        cnode = nodesdict[cnode][0] if step == 'L' else nodesdict[cnode][1]
        stepcount +=1
        # this updates the stepindex to the next step, wrapping around to the start of the steps list if needed with the % operator (gives the remainder)
        stepindex = (stepindex + 1) % len(steps)

    return stepcount

def spooky(steps, nodesdict):
    # Initialize current nodes to all nodes that end with 'A'
    cnodes = [node for node in nodesdict if node.endswith('A')]

    stepcount = 0
    stepindex = 0

    # Continue until all current nodes end with 'Z'
    while any(not node.endswith('Z') for node in cnodes):
        # Update current nodes based on steps
        for i in range(len(cnodes)):
            step = steps[stepindex]
            cnodes[i] = nodesdict[cnodes[i]][0] if step == 'L' else nodesdict[cnodes[i]][1]
        stepcount += 1
        stepindex = (stepindex + 1) % len(steps)

    return stepcount

def spookylcm(steps, nodesdict):
    # Compute cycle lengths for all 'A' nodes
    cycle_lengths = []
    for node in nodesdict:
        if node.endswith('A'):
            cnode = node
            cycle_length = 0
            while not cnode.endswith('Z'):
                step = steps[cycle_length % len(steps)]
                cnode = nodesdict[cnode][0] if step == 'L' else nodesdict[cnode][1]
                cycle_length += 1
            cycle_lengths.append(cycle_length)
    # Compute the least common multiple of the cycle lengths using the reduce function from functools and the gcd function from math
    # The math is explained here: https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
    # https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-135.php
    def lcm(cycle_lengths):
        return reduce((lambda x, y: int(x * y / gcd(x, y))), cycle_lengths)

    return(lcm(cycle_lengths))

# Call the functions
print(f"No Spook: {notspooky(steps, nodesdict)}")
print(f"Boo Bitch!: {spookylcm(steps, nodesdict)}")


end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution Time: {elapsed_time} seconds")
