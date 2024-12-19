from itertools import count
from time import time

data = open(0).read().strip()
# data = open('test.txt').read()
left_list, right_list = zip(
    *[(int(left), int(right)) for left, right in (line.split("   ") for line in data.splitlines())]
)

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

print("\033[1mPart1:\033[22m:", diff())
print("\033[1mPart2:\033[22m:", counting())

end_time = time()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
