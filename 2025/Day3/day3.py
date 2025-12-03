# Solution for Advent of Code 2025, Day 3
# https://adventofcode.com/2025/day/3
from time import perf_counter


def many_digits(bank, size):
    bigboy = []
    bank_len = len(bank)
    index = 0

    for digits_remaining in range(size, 0, -1):
        # Make sure we know how many digits we have to leave for the rest of the number
        end = bank_len - digits_remaining + 1
        # Find the max digit in the current range of available digits and find it's index
        max_digit = "0"
        best_index = -1

        for i in range(index, end):
            if bank[i] > max_digit:
                max_digit = bank[i]
                best_index = i
                # If it's a 9 we found the best digit and break early
                if max_digit == "9":
                    break
        # Add the best digit we found to the bigboy list and move the index up
        bigboy.append(max_digit)
        index = best_index + 1
    # Join the list into a string and convert to int and return it!
    result = int("".join(bigboy))
    return result


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    p1 = 0
    p2 = 0

    for bank in data:
        p1 += many_digits(bank, 2)
        p2 += many_digits(bank, 12)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
