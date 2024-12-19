# Solution for Advent of Code 2024, Day 9
# https://adventofcode.com/2024/day/9

from time import time


# Part 1
def checksum1(data):
    file_id = 0
    disk_map_list1 = []
    # Parsing into a usable list
    # First time through ran into an issue where double digit file_ids where being added as multiple single digits.. which worked for the test input, as it only goes to file_id 9, but not the real one.
    for index, num in enumerate(data):
        num = int(num)
        if index % 2 == 0:
            disk_map_list1.extend([str(file_id)] * num)
            file_id += 1
        else:
            disk_map_list1.extend(["."] * num)
    # Get all of the indices for all of the things first.. otherwise it's slow af
    digit_indices = [i for i, ch in enumerate(disk_map_list1) if ch.isdigit()]
    dot_indices = [i for i, ch in enumerate(disk_map_list1) if ch == "."]

    # Swap dots and digits
    while dot_indices and digit_indices and dot_indices[0] < digit_indices[-1]:
        leftmost_dot = dot_indices.pop(0)
        rightmost_digit = digit_indices.pop()

        # Swap positions
        disk_map_list1[leftmost_dot], disk_map_list1[rightmost_digit] = (
            disk_map_list1[rightmost_digit],
            disk_map_list1[leftmost_dot],
        )

    checksum = 0

    for index, num in enumerate(disk_map_list1):
        if num.isdigit():
            block_id = int(index) * int(num)
            checksum += block_id

    return checksum


# Part 2 - Credit to Hyperneutrino. This solution is much more elegant than mine.
def checksum2(data):
    files = {}
    dots = []

    file_id = 0
    pos = 0

    for index, char in enumerate(data):
        num = int(char)
        if index % 2 == 0:
            files[file_id] = (pos, num)
            file_id += 1
        else:
            if num != 0:
                dots.append((pos, num))
        pos += num

    while file_id > 0:
        file_id -= 1
        file_pos, file_length = files[file_id]
        for i, (dot_pos, dot_length) in enumerate(dots):
            if dot_pos >= file_pos:
                dots = dots[:i]
                break
            if file_length <= dot_length:
                files[file_id] = (dot_pos, file_length)
                if file_length == dot_length:
                    dots.pop(i)
                else:
                    dots[i] = (dot_pos + file_length, dot_length - file_length)
                break

    checksum = 0

    for fid, (pos, size) in files.items():
        for x in range(pos, pos + size):
            checksum += fid * x

    return checksum


start_time = time()


data = open(0).read().strip()

data = list(data)

print("\033[1mPart1:\033[22m:", checksum1(data))
print("\033[1mPart2:\033[22m:", checksum2(data))

end_time = time()
print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
