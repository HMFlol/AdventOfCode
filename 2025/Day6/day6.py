# Solution for Advent of Code 2025, Day 6
# https://adventofcode.com/2025/day/6
from time import perf_counter


def calculate_equations(equations):
    """Calculate the result of all equations."""
    result = 0
    for nums, op in equations:
        cur_equation = 0 if op == "+" else 1
        for num in nums:
            if op == "*":
                cur_equation *= num
            else:  # op == "+"
                cur_equation += num
        result += cur_equation
    return result


def part1(data):
    # split the data into lines
    lines = [line.split() for line in data.strip().splitlines()]
    # split the lines into number rows and operators
    number_rows, operators = lines[:-1], lines[-1]
    # zip the number rows and operators together
    equations = []
    for number_list, operator in zip(zip(*number_rows), operators):
        numbers = [int(n) for n in number_list]
        operator = operator
        equations.append((numbers, operator))

    return calculate_equations(equations)


def part2(data):
    # flip the data 90 degrees ccw so we can group by columns
    flipped = list(zip(*data.splitlines()))
    # Split columns into groups separated by all-space columns
    groups = []
    group = []

    for col in flipped:
        # if the column is all spaces, append the group and reset it
        if set(col) == {" "}:
            if group:  # Only append non-empty groups
                groups.append(group)
                group = []
        else:
            group.append(col)
    # Don't forget the last group
    groups.append(group)

    # Parse each group into an equation
    equations = []
    # for each group, remove the last character (operator) and join the rest into a number
    for group in groups:
        numbers = [int("".join(line[:-1]).strip()) for line in group]
        operator = group[0][-1]
        equations.append((numbers, operator))

    return calculate_equations(equations)


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read()

    p1 = part1(data)
    p2 = part2(data)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
