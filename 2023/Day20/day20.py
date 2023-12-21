from aocd import get_data
from time import time
from collections import deque
from collections import defaultdict
import math

# TO BE REFACTORED LATER

# Load data
data = get_data(day=20, year=2023)
data = data.splitlines()

# Initialize modules
modules = {}

for line in data:
    module, dests = line.split(' -> ')
    dest = dests.split(', ')
    key = module.lstrip('%&')
    value = (module[0] if module[0] in "%&" else None, dest)
    modules[key] = value


def part1(modules):
    FLIP = set()
    MEM = defaultdict(dict)

    for dest in modules:
        MEM[dest] = {key: 'LOW' for key in modules if dest in modules[key][1]}
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
    return answer

def part2(modules):
    FLIP = set()
    MEM = defaultdict(dict)

    for dest in modules:
        MEM[dest] = {key: 'LOW' for key in modules if dest in modules[key][1]}

    
    (feed,) = [name for name, module in modules.items() if "rx" in module[1]]

    cycle_lengths = {}

    seen = {name: 0 for name, module in modules.items() if feed in module[1]}

    presses = 0

    while True:
        presses += 1 
        # Initialize the queue with the initial LOW pulse to the broadcaster module
        queue = deque([('broadcaster', 'LOW', dest) for dest in modules['broadcaster'][1]])

        while queue:
            source, pulse, module = queue.popleft()

            if module not in modules:
                continue

            type, dests = modules[module]

            if module == feed and pulse == 'HIGH':
                seen[source] += 1

                if source not in cycle_lengths:
                    cycle_lengths[source] = presses
                else:
                    assert presses == seen[source] * cycle_lengths[source]

                if all(seen.values()):
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = math.lcm(x, cycle_length)
                    return x

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


# Run part 1 and part 2
start_time = time()

print(f"Part 1 answer: {part1(modules)}")
print(f"Part 2 answer: {part2(modules)}")

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")