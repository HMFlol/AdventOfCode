from aocd import get_data
from time import time
from itertools import count    

data = get_data(day=1, year=2024)
# data = open('test.txt').read()
left_list, right_list = zip(*[(int(left), int(right)) for left, right in (line.split("   ") for line in data.splitlines())])

left_list = sorted(left_list)
right_list = sorted(right_list)

# Part 1
def diff():
    differences = [abs(left - right) for left, right in zip(left_list, right_list)] 

    return sum(differences)

# Part 2
def counting():
    total = 0
    for num in left_list:
        total += num * right_list.count(num)

    return total


start_time = time()

print(f"Part1:", diff())
print(f"Part2:", counting())

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")