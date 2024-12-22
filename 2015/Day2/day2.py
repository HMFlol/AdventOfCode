from time import perf_counter


def square_feet(line):
    l, w, h = line
    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def ribbon_length(line):
    l, w, h = line
    return 2 * min(l + w, w + h, h + l) + l * w * h


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().split()
    data = [list(map(int, x.split("x"))) for x in data]

    print("\033[1mPart1:\033[22m", sum(square_feet(line) for line in data))
    print("\033[1mPart2:\033[22m", sum(ribbon_length(line) for line in data))

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
