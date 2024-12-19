import re
from time import time

data = open(0).read().strip()
# data = open('test.txt').read()
# data = [line.split() for line in data.splitlines()]


def mul1():
    total = 0
    # Yay. I actually had to learn regex.. again. TIL if I put r in front of the string it's ACTUALLY legible.
    for num1, num2 in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data):
        total += int(num1) * int(num2)

    return total


def mul2():
    total = 0
    # Same as the first one, but with an added boolean check. Could likely consolidate into one function later.
    enabled = True
    for command, num1, num2 in re.findall(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", data):
        if command == "do()":
            enabled = True
        elif command == "don't()":
            enabled = False
        else:
            if enabled:
                total += int(num1) * int(num2)

    return total


start_time = time()

print("\033[1mPart1:\033[22m:", mul1())
print("\033[1mPart2:\033[22m:", mul2())

end_time = time()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
