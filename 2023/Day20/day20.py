from aocd import get_data
from time import time
from collections import deque
from collections import defaultdict

data = get_data(day=20, year=2023)
#data = open('test.txt').read()
data = data.splitlines()

modules = {}

# Initialize the state of each module
FLIP = set()
MEM = defaultdict(dict)

for line in data:
    module, dests = line.split(' -> ')
    dest = dests.split(', ')
    key = module.lstrip('%&')
    value = (module[0] if module[0] in "%&" else None, dest)
    modules[key] = value

    for dest in dest:
        MEM[dest][key] = 'LOW'

# Initialize the count of HIGH and LOW pulses
hi = lo = 0

for _ in range(1000):
    lo += 1 
    # Initialize the queue with the initial LOW pulse to the broadcaster module
    queue = deque([('broadcaster', 'LOW', dest) for dest in modules['broadcaster'][1]])

    while queue:
        source, pulse, module = queue.popleft()
        
        if pulse == "LOW":
            lo += 1
        else:
            hi += 1

        if module not in modules:
            continue

        type, dests = modules[module]

        if type == '%': # Flip-flop logic
            if pulse == 'HIGH':
                continue
            elif module not in FLIP and pulse == 'LOW':
                FLIP.add(module)
                pulse = 'HIGH'
            else:
                FLIP.discard(module)
                pulse = 'LOW'
        elif type == '&': # Conjunction logic
            MEM[module][source] = pulse
            if all(value == 'HIGH' for value in MEM[module].values()):
                pulse = 'LOW'
            else:
                pulse = 'HIGH'
        
        for dest in dests: # Add the pulse to each destination module
            queue.append((module, pulse, dest))

answer = lo * hi
print(answer)

start_time = time()

# print(f"Total (Part1):", shoelacePick(False))
# print(f"Total (Part2):", shoelacePick(True))

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")