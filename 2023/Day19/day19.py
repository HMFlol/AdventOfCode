from aocd import get_data
from time import time
import re

# TO BE REFACTORED


data = get_data(day=19, year=2023)
data = open('test.txt').read()
workflows, parts = data.split("\n\n")

workflows1 = {}
for line in workflows.splitlines():
    name, line = line.split('{')
    workflows1[name] = [part.split(":") for part in line[:-1].split(',')]
'''workflows1 = {name: rules_str.strip('}').split(',') for workflow in workflows.splitlines() for name, rules_str in [workflow.split('{')]}'''
print(workflows1)
workflows2 = {}

for line in workflows.splitlines():
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows2[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        cmp = comparison[1]
        n = int(comparison[2:])
        workflows2[name][0].append((key, cmp, n, target))

parts = parts.splitlines()

def onlyParts():
    A_parts = []
    ans = 0

    for part in parts:
        x, m, a, s = [int(x) for x in re.findall("\d+", part)]  # Convert the numbers to integers and assign them to x, m, a, s
        flow = 'in'
        while True:
            if flow == 'A':
                # print(f'Part {part} is accepted')
                A_parts.append(part)
                break
            elif flow == 'R':
                # print(f'Part {part} is rejected')
                break
            for rule in workflows1[flow]:
                if ':' in rule:
                    condition, next_workflow = rule.split(':')
                    if eval(condition):  # Use eval() to evaluate the condition. eg. s<1351
                        flow = next_workflow
                        break
                else:
                    flow = rule

    for part in A_parts:
        x, m, a, s = [int(x) for x in re.findall("\d+", part)]
        ans += x + m + a + s

    return ans

# Thanks to hyper-neutrino for the solution to part 2. I was stuck on it for a while. It's a tree.
def onlyFlows(ranges, flow):
    if flow == "R":
        return 0
    if flow == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows2[flow]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += onlyFlows(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += onlyFlows(ranges, fallback)
            
    return total


start_time = time()

print(f"Total (Part1):", onlyParts())
print(f"Total (Part2):", onlyFlows({c: (1, 4000) for c in "xmas"}, 'in'))

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")