# Solution for Advent of Code 2024, Day 17
# https://adventofcode.com/2024/day/17
import re
from time import time


# Part 1
def wtfprogram(rega, regb, regc, program):
    pointer = 0
    out = []

    while pointer < len(program) - 1:
        combo_op = [0, 1, 2, 3, rega, regb, regc]
        operand = program[pointer + 1]
        match program[pointer]:
            case 0:
                rega = rega >> combo_op[operand]
            case 1:
                regb = regb ^ operand
            case 2:
                regb = combo_op[operand] % 8
            case 3:
                if rega != 0:
                    pointer = operand
                    continue
            case 4:
                regb = regb ^ regc
            case 5:
                output = combo_op[operand] % 8
                out.append(output)
            case 6:
                regb = rega >> combo_op[operand]
            case 7:
                regc = rega >> combo_op[operand]
        pointer += 2

    return out


# Part 2
def wtflowest(program, ans):
    # Start with an index of 1 and a value of 0
    stack = [(1, 0)]
    for i, avalue in stack:
        # Check the next 8 values for a
        for a in range(avalue, avalue + 8):
            # Check if the value matches the last i elements of the program
            if wtfprogram(a, 0, 0, program) == program[-i:]:
                # If matched, increment the index and add the a value * 8 to the stack
                stack += [(i + 1, a * 8)]
                # If i is equal to the length of the program, a replica was found, return a
                if i == len(program):
                    return a
    # This portion is specific to my own program, but can be adapted easily
    """ if program == []:
        return ans
    for num in range(8):
        a = ans << 3 | num
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ c
        b = b ^ 6
        if b % 8 == program[-1]:
            sub = wtflowest(program[:-1], a)
            if sub is None:
                continue
            return sub """


start_time = time()


data = open(0).read().strip()
# Parsing stuff
rega, regb, regc, *program = map(int, re.findall(r"\d+", data))

print("Part1:", ",".join(map(str, wtfprogram(rega, regb, regc, program))))
print("Part2:", wtflowest(program, 0))

end_time = time()
print(f"Time: {end_time - start_time:.6f} seconds")
