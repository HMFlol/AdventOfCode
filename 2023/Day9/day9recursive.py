# Learning about recursion and how to use and parse aocd data
from aocd import data

def extrapolate(array):
    # all checks if all elements in an iterable are true. In this case, it checks if all numbers in the array are 0 and returns 0 if they are
    if all(x == 0 for x in array):
        return 0
    
    # Calculate differences between consecutive elements in the array
    deltas = [y - x for x, y in zip(array, array[1:])]
    # Recursive call: extrapolate on the differences (deltas)
    diff = extrapolate(deltas)

    # Unwind the recursive calls - add the difference to the last element in the array and return it going up the stack
    return array[-1] + diff

total = 0

"""for line in data.splitlines():
    nums = list(map(int, line.split()))
    total += extrapolate(nums)"""

# Line comprehension version!!
total = sum(extrapolate(list(map(int, line.split()))) for line in data.splitlines())

print(total)