# Read the lines
with open('input.txt','r') as i:
    lines = i.readlines()

# Part
def digits1(line):
    # Find the first and last digits
    return int(
        next(char for char in line if char.isdigit()) + # First digit and add to...
        next(char for char in reversed(line) if char.isdigit()) # Last digit
    )

# Print the sum of all digits returned from the lines
print(sum(digits1(line) for line in lines))

def digits2(line):
    # A dictonary to replace written numbers with actual numbers
    # Amended many times to figure out what worked for the secret strings like "nineight".. tricky bugger
    d = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    # Replace the written words with their less stringy counterparts
    for word, digit in d.items():
        line = line.replace(word, digit)

    # Find the first and last digits or spelled-out numbers
    return int(
        next(char for char in line if char.isdigit()) + # First digit and add to...
        next(char for char in reversed(line) if char.isdigit()) # Last digit
    )

# Print the sum of all digits returned from the lines
print(sum(digits2(line) for line in lines))
