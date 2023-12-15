from aocd import get_data
from time import time

data = get_data(day=15, year=2023)
#data = open('test.txt').read()
strings = data.split(',')

# Lens calc function since I was using the same code in 3 spots
def lensCalc(label):
    lens = 0
    for c in label:
        lens = (lens + ord(c)) * 17 % 256
    return lens

# Part 1
def hash(strings):
    result = 0

    for string in strings:
        lens = lensCalc(string)
        result += lens

    return result

# Part 2
def fpower(strings):
# Making a bunch of boxes
    boxes = [dict() for _ in range(256)] # Replaced array of arrays with array of dicts
    # Using match here is slick. I didn't know about it until I saw it in the solutions.
    '''
    for string in strings:
        match string.strip('-').split('='):
            case [l, f]: boxes[lensCalc(l)][l] = int(f)
            case [l]:    boxes[lensCalc(l)].pop(l, 0)
    '''
    for string in strings:
        if "-" in string:
            label = string[:-1]
            lens = lensCalc(label)
            boxes[lens].pop(label, 0) # remove label from box at index lens
        else:
            label, focal = string[:-2], string[-1]
            lens = lens = lensCalc(label)
            boxes[lens][label] = int(focal) # add label to box at index lens

    fpower = sum(box_idx * l_slot * focal for box_idx, box in enumerate(boxes, 1) for l_slot, focal in enumerate(box.values(), 1))

    return fpower

start_time = time()

print(f"Total (Part1):", hash(strings))
print(f"Total (Part2):", fpower(strings))

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")


'''
Initial fpower function used an array of arrays which required extra steps.
Using an array of dicts, as above, allows for a much simpler solution.
The above function is doing the same thing as below but with much fewer steps.

def fpower(strings):
# Making a bunch of boxes
    boxes = [[] for _ in range(256)]

    for string in strings:
        if "-" in string:
            label = string[:-1]
            lens = lensCalc(label)
            boxminus = boxes[lens] # Get the box at index lens
            boxminus = [lens for lens in boxminus if lens[0] != label] # Make a new 'box' of all lenses that DON'T have the label that we want to remove
            boxes[lens] = boxminus # Put the new 'box' back in the boxes list at the lens index, sans label
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

    fpower = sum((box_idx + 1) * (l_slot + 1) * int(focal) for box_idx, box in enumerate(boxes) for l_slot, (_, focal) in enumerate(box))
'''