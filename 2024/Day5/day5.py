# Solution for Advent of Code 2024, Day 5
# https://adventofcode.com/2024/day/5

from aocd import get_data
from time import time

data = get_data(day=5, year=2024)
# data = open('test.txt').read()
rules, updates = [line.split() for line in data.split("\n\n")]
rules, updates = ([rule.split("|") for rule in rules], [update.split(",") for update in updates])

# Part 1
def updates1():
    total = 0
    # Iterating over each "page" in updates, reversing the order of the pair and checking if it exists in rules. If so, it's a violation, and we go to the next set of updates. If not, we add the middle number to the total.
    for update in updates:
        pair_exists = False
        for num1 in range(len(update)):
            for num2 in range(num1 + 1, len(update)):
                if [update[num2], update[num1]] in rules:
                    pair_exists = True
                    break
            if pair_exists:
                break
        if not pair_exists:
            m_index = len(update)//2
            total += int(update[m_index])
    
    return total

# Part 2
def updates2():
    def dfs(num):
        if num in visited:
            return
        visited.add(num)
        for num2 in [num2 for [num1,num2] in rules if num1 == num and num2 in update]: # Iterate over all num2 of the page 
            dfs(num2) # Resursively visit each num2
        sorted_update.append(num) # Append the page to the sorted_update list

    total = 0
    # Find the baddies first
    for update in updates:
        sorted_update = []
        visited = set()
        pair_exists = False
        for num1 in range(len(update)):
            for num2 in range(num1 + 1, len(update)):
                if [update[num2], update[num1]] in rules:
                    pair_exists = True
                    break
            if pair_exists:
                break

        if pair_exists:
            # Sort the update according to the rules using topological sort.  
            for num in update:
                dfs(num) # Perform DFS to sort the update topologically
            m_index = len(sorted_update)//2
            total += int(sorted_update[m_index])

    return total

start_time = time()

print(f"Part1:", updates1())
print(f"Part2:", updates2())

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")