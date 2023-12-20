from aocd import get_data
from time import time

data = get_data(day=1, year=2015)
# data = open('test.txt').read()
# data = [line.split() for line in data.splitlines()]

def floor():
    floor = 0
    for c, char in enumerate(data):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        
    return floor

def neg():
    floor = 0
    for c, char in enumerate(data):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return c + 1


start_time = time()

print(f"Total (Part1):", floor())
print(f"Total (Part2):", neg())

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")