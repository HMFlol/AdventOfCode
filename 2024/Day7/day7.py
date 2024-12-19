# Solution for Advent of Code 2024, Day 7
# https://adventofcode.com/2024/day/7

from time import time

# data = get_data(day=7, year=2024)
data = open(0).read().strip()
data = [list(map(int, line.replace(":", "").split())) for line in data.splitlines()]


# Part 1
def tester(target, numbers, part2=False):
    def test_loop(index, current):
        if index == len(numbers):
            return current == target

        next_num = numbers[index]

        # Add
        if test_loop(index + 1, current + next_num):
            return True

        # Multiply
        if test_loop(index + 1, current * next_num):
            return True

        # Concatenate, if Part2
        if part2:
            con = int(str(current) + str(next_num))
            if test_loop(index + 1, con):
                return True

        return False

    return test_loop(1, numbers[0])


start_time = time()

# Part 1
totalp1 = 0
totalp2 = 0

for line in data:
    target = line[0]
    numbers = line[1:]
    if tester(target, numbers):
        totalp1 += target
    if tester(target, numbers, True):
        totalp2 += target

print("Part1:", totalp1)
print("Part2:", totalp2)

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
