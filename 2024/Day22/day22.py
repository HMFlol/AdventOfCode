# Solution for Advent of Code 2024, Day 22
# https://adventofcode.com/2024/day/22
from collections import defaultdict
from time import perf_counter


def process_secrets(secret, cycles):
    """Returns the secret number after a certain number of iterations."""
    prices = []
    previous_ones = secret % 10
    prices.append({"price": previous_ones, "change": None})
    for _ in range(cycles):
        secret = (secret * 64 ^ secret) % 16777216
        secret = (secret // 32 ^ secret) % 16777216
        secret = (secret * 2048 ^ secret) % 16777216

        current_ones = secret % 10
        change = current_ones - previous_ones
        prices.append({"price": current_ones, "change": change})
        previous_ones = current_ones

    return secret, prices


def find_best_sequence(price_lists):
    """Finds the sequence of 4 price changes with the highest total price."""
    sequences = defaultdict(int)

    for pl in price_lists:
        seen = set()
        for i in range(len(pl) - 4):
            seq = (
                pl[i + 1]["change"],
                pl[i + 2]["change"],
                pl[i + 3]["change"],
                pl[i + 4]["change"],
            )
            if seq in seen:
                continue
            seen.add(seq)
            sequences[seq] += pl[i + 4]["price"]
    return max(sequences.values())


if __name__ == "__main__":
    start_time = perf_counter()
    data = [int(line) for line in open(0).read().strip().splitlines()]
    # Part 1
    p1, price_lists = zip(*(process_secrets(secret, 2000) for secret in data))
    p1 = sum(p1)
    # Part 2
    p2 = find_best_sequence(price_lists)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
