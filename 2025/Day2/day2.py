# Solution for Advent of Code 2025, Day 2
# https://adventofcode.com/2025/day/2
from time import perf_counter


def is_repeated_twice(s, length):
    # Number needs to be even for a sequence to be repeated exactly twice
    if length % 2 != 0:
        return False

    # Find the middle as sequence length should be half the total length
    half = length // 2

    # Break the number in half and check the halves. Return True if they are identical, or else False
    first_half = s[:half]
    second_half = s[half:]

    return first_half == second_half


def is_repeated(s, length):
    # Sequence length has to be a divisor of the overall length and less than that full length, indicated it repeats at least twice
    # Iterate through those
    for seq_len in range(1, length):
        # See if the sequence length is a divisor of total length
        if length % seq_len == 0:
            # Calculate how many times it would need to repeat
            reps = length // seq_len
            # Based on the above, get the potential sequence
            sequence = s[:seq_len]
            # Check if the sequence, repeated x (reps) times matches the original number and return True if so
            if sequence * reps == s:
                return True

    return False


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().split(",")

    # Split the input into ranges on the comma, then into tuples
    ranges = [tuple(map(int, line.split("-"))) for line in data]

    p1 = 0
    p2 = 0

    # Iterate through the ranges, and check each number in the range
    for nums in ranges:
        start_num = nums[0]
        end_num = nums[1]
        for num in range(start_num, end_num + 1):
            # Convert to str for comparison, length stuff, etc. Get the length here as well.. no point in doing it twice twice
            s_num = str(num)
            num_length = len(s_num)
            if is_repeated_twice(s_num, num_length):
                # If method returns True add the number to the total
                p1 += num
            if is_repeated(s_num, num_length):
                p2 += num

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
