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
    columns = zip(*number_rows)
    # zip the columns and operators together
    equations = [([int(n) for n in col], op) for col, op in zip(columns, operators)]

    return calculate_equations(equations)


def part2(data):
    # Flip the data 90 degrees CCW so we can group by columns
    flipped = list(zip(*data.splitlines()))
    # Parse equations directly from flipped columns
    # Each equation is separated by all-space columns
    equations = []
    current_equation = []

    for col in flipped:
        if set(col) == {" "}:  # All-space column = separator
            if current_equation:
                # Parse the accumulated columns into numbers and operator
                # Each column has format: digits + operator, e.g., ('3', '6', '9', '+')
                numbers = [int("".join(c[:-1]).strip()) for c in current_equation]
                operator = current_equation[0][-1]  # Last char of first column
                equations.append((numbers, operator))
                current_equation = []
        else:
            current_equation.append(col)

    # Process the last equation (no trailing separator)
    if current_equation:
        numbers = [int("".join(c[:-1]).strip()) for c in current_equation]
        operator = current_equation[0][-1]
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
