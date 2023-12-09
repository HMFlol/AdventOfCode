from functools import reduce
from math import gcd
import time
# timer stuff
start_time = time.time()

# Open the file and break the two lines into time and dist
#with open('input.txt','r') as i:
#    lines = i.read().splitlines()
# THIS IS WAY BETTER - SKIP LINES WITH _
steps, _, *nodes = open('input.txt').read().splitlines()

# Extract steps and nodes
#steps = lines[0]
#nodes = lines[2:]

# Process nodes and stick in a dictionary
nodesdict = {}
# Also much better - use split to break the node into pos and targets and then split the targets into a list
for node in nodes:
    pos, targets = node.split(" = ")
    nodesdict[pos] = targets[1:-1].split(", ")

# This is what I had done... 
# for node in nodes:
#        nodeparts = node.split('=')
#        nodename = nodeparts[0].strip()
#        nodelr = nodeparts[1].strip().strip('()').split(', ')
#        nodesdict[nodename] = nodelr

def notspooky(steps, nodesdict):
    startnotspooky = time.time()
    # Initialize current node, step count
    curnode = 'AAA'
    stepcount = 0

    while curnode != 'ZZZ':
        # current step is the step at the current index. Will wrap when it gets to the end of the steps list - stepcoount will equal len(steps)
        step = steps[stepcount % len(steps)]
        curnode = nodesdict[curnode][0] if step == 'L' else nodesdict[curnode][1]
        stepcount +=1

    endnotspooky = time.time()
    print(f"Part 1 - No Spook: {stepcount}, Time: {endnotspooky - startnotspooky:.6f} seconds")

def spooky(steps, nodesdict):
    startspooky = time.time()
    # Initialize current nodes to all nodes that end with 'A' this time
    curnodes = [node for node in nodesdict if node.endswith('A')]
    stepcount = 0

    # Continue until all current nodes end with 'Z'
    while any(not node.endswith('Z') for node in curnodes):
        # Update current nodes based on steps
        for i in range(len(curnodes)):
            step = steps[stepcount % len(steps)]
            curnodes[i] = nodesdict[curnodes[i]][0] if step == 'L' else nodesdict[curnodes[i]][1]
        stepcount += 1\

    endspooky = time.time()
    print(f"Part 2 - No LCM. The scary part is how long this takes: {stepcount}, Time: {endspooky - startspooky:.6f} seconds")

def spookylcm(steps, nodesdict):
    startspookylcm = time.time()
    # Compute stepcoutns for all 'A' nodes
    stepcounts = []
    for node in nodesdict:
        # Initialize current nodes to all nodes that end with 'A' this time
        if node.endswith('A'):
            curnode = node
            stepcount = 0
            while not curnode.endswith('Z'):
                step = steps[stepcount % len(steps)]
                curnode = nodesdict[curnode][0] if step == 'L' else nodesdict[curnode][1]
                stepcount += 1
            stepcounts.append(stepcount)
    # Compute the least common multiple of the cycle lengths using the reduce function from functools and the gcd function from math
    # The math is explained here: https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
    # https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-135.php
    def lcm(stepcounts):
        return reduce((lambda x, y: int(x * y / gcd(x, y))), stepcounts)

    endspookylcm = time.time()
    print(f"Part 2 - LCM Jumpscare Edition - Boo Bitch!: {lcm(stepcounts)}, Time: {endspookylcm - startspookylcm:.6f} seconds")

# Call the functions
notspooky(steps, nodesdict)
spookylcm(steps, nodesdict)
#spooky(steps, nodesdict)


end_time = time.time()
elapsed_time = end_time - start_time

print(f"Total execution time: {elapsed_time:.6f} seconds")
