from aocd import data
from time import time

starttime = time()
# data = open('test.txt').read().splitlines()
data = data.splitlines()

sdata = []

for line in data:
    springs, groups = line.split()
    groups = tuple(map(int, groups.split(','))) # This is a tuple because it's hashable and can be used as a key in a dictionary eg. memo = {}
    sdata.append((springs, groups))

def counting(springs, groups, memo):
    # If springs is empty, return 1 if groups is empty, 0 otherwise
    if springs == "":
        return 1 if groups == () else 0
    # If groups is empty, return 0 if there are any springs left, 1 otherwise
    if groups == ():
        return 0 if "#" in springs else 1
    # Check if result is already in memo
    if (springs, groups) in memo:
        return memo[(springs, groups)]
    # Otherwise, set total to 0
    total = 0
    # If the first character is . or ?, recurse with the rest of the string and the same groups. . or ? can match a group size of 0
    if springs[0] in '.?':
        total += counting(springs[1:], groups, memo)
    # If the first character is # or ?, if the first group size is less than or equal to the length of the springs, if there are no . in the first group size characters of the springs string, and if the character after group size length of characters is not #, recurse with the rest of the string and the groups with the first group removed
    if springs[0] in "#?":
        if groups[0] <= len(springs) and "." not in springs[:groups[0]] and (groups[0] == len(springs) or springs[groups[0]] != "#"):
            total += counting(springs[groups[0] + 1:], groups[1:], memo)
    # Store result in memo before returning
    memo[(springs, groups)] = total

    return total

def calculating(sdata, memo):
    total = 0
    for springs, groups in sdata:
        total += counting(springs, groups, memo)
    return total

total1 = calculating(sdata, {})
total2 = calculating([('?'.join([springs] * 5), groups * 5) for springs, groups in sdata], {})

print(f"Total arrangements (Part1): {total1}")
print(f"Total arrangements (Part2): {total2}")

endtime = time()
print(f"Total execution time: {endtime - starttime:.6f} seconds")