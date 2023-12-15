from aocd import get_data
from time import time
start_time = time()
data = get_data(day=15, year=2023)
#data = open('test.txt').read()
strings = data.split(',')

result = 0

# Lens calc function since I was using the same code in 3 spots
def lensCalc(label):
    lens = 0
    for c in label:
        lens = (lens + ord(c)) * 17 % 256
    return lens

# Part 1
for string in strings:
    lens = lensCalc(string)
    result += lens

# Part 2
# Making a bunch of boxes
boxes = [[] for _ in range(256)]

for string in strings:
    if "-" in string:
        label = string[:-1]
        lens = lensCalc(label)
        box = boxes[lens] # Get the box at index lens
        box = [lens for lens in box if lens[0] != label] # Make a new list, including only the lenses that DON'T have the label that we can then pop back in, effectively removing the lens with the given label
        boxes[lens] = box # Put the box back in the boxes list at the lens index
    else:
        label, focal = string[:-2], string[-1]
        lens = lens = lensCalc(label)
        box = boxes[lens] # Get the box at index lens
        exists = [i for i, lens in enumerate(box) if lens[0] == label] # Get the index of the lens with the given label, if it exists
        if exists: # If exists is not empty
            box[exists[0]] = (label, focal) # Replace the 'box' at the given index with the new label
        else:
            box.append((label, focal)) # If it doesn't exist, just append it
        boxes[lens] = box # Put the box back in the boxes list at the lens index

fpower = 0
for b, box in enumerate(boxes):
    for l, lens in enumerate(box, start=1):
        label, focal = lens
        fpower += (b + 1) * l * int(focal)

print(f"Total (Part1):", result)
print(f"Total (Part2):", fpower)

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")