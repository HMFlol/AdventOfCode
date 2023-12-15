from aocd import get_data
from time import time

data = get_data(day=9, year=2023)
# data = open('test.txt').read()

# Part 1
def extrapolate(array):
    # all checks if all elements in an iterable are true. In this case, it checks if all numbers in the array are 0 and returns 0 if they are
    if all(x == 0 for x in array):
        return 0
    deltas = [y - x for x, y in zip(array, array[1:])] # Calculate differences between consecutive elements in the array
    diff = extrapolate(deltas) # Recursive call: extrapolate on the differences (deltas)
    
    return array[-1] + diff # Unwind the recursive calls - add the difference to the last element in the array and return it going up the stack

start_time = time()

print(f"Total (Part1):", sum(extrapolate(list(map(int, line.split()))) for line in data.splitlines()))
print(f"Total (Part2):", sum(extrapolate(list(map(int, line.split()))[::-1]) for line in data.splitlines()))

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")