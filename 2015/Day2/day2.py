from aocd import get_data
from time import time

data = get_data(day=2, year=2015)
# data = open('test.txt').read()
data = [line.split('x') for line in data.splitlines()]

for line in data:
    num1, num2, num3 = line
    print(num1, num2, num3)



start_time = time()

#print(f"Total (Part1):", floor())
#print(f"Total (Part2):", neg())

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")