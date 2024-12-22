from time import perf_counter


def floor():
    return data.count("(") - data.count(")")


def neg():
    floor = 0
    for index, char in enumerate(data):
        floor += 1 if char == "(" else -1
        if floor == -1:
            return index


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()

    print("\033[1mPart1:\033[22m", floor())
    print("\033[1mPart2:\033[22m", neg())

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
