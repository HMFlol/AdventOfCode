# Read the lines
with open('input.txt', 'r') as i:
    lines = i.readlines()

# Join the lines into a single string
input = ''.join(lines)

# Part 1
def parts(input):
    # Parse the input into a 2D array
    grid = [list(line) for line in input.split('\n')]

    # Define the directions to check
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Initialize the sum of part numbers
    total_sum = 0

    # Initialize the list of numbers and their positions
    numbers = []

    # Iterate over each cell in the grid (i = row, j = column)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell contains a digit and the previous cell in the same row is not a digit
            if grid[i][j].isdigit() and (j == 0 or not grid[i][j - 1].isdigit()):
                # Gather all adjacent digits to form the number
                number = ''
                start_j = j
                while j < len(grid[i]) and grid[i][j].isdigit():
                    number += grid[i][j]
                    j += 1

                # Store the number along with its position (number, row, start column, end column)
                numbers.append((int(number), i, start_j, j - 1))

    # Iterate over the list of numbers and their positions
    for number, i, start_j, end_j in numbers:
        # Check the eight surrounding cells of the first and last digit for symbols
        found_symbol = False
        for dx, dy in directions:
            if found_symbol:
                break
            for dj in range(start_j, end_j + 1):
                nx, ny = i + dx, dj + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and not grid[nx][ny].isdigit() and grid[nx][ny] != '.':
                    # If a surrounding cell contains a symbol, add the number to the sum of part numbers
                    total_sum += number
                    found_symbol = True
                    break

    return total_sum

# Part 2
def gears(input):
    # Parse the input into a 2D array
    grid = [list(line) for line in input.split('\n') if line]
    # Define the directions to check using list comprehension... I need to study this more. I don't understand it yet but it's cool!
    # Functionally the same as directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx != 0 or dy != 0]
    # Initialize the dictionary of symbol numbers (key = symbol(*) position, value = set of numbers adjacent to the symbol)
    symbol_numbers = {}

    # Find the numbers adjacent to each '*' symbol
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            # Finds a digit
            if grid[i][j].isdigit():
                # Mark the start of the number
                start_j = j
                # Find the end of the number
                while j < len(grid[i]) and grid[i][j].isdigit():
                    j += 1
                # Convert the number to an integer and add it to the set of numbers adjacent to the symbol
                number = int(''.join(grid[i][start_j:j]))
                # Check the eight surrounding cells of the first and last digit for symbols
                for dx, dy in directions:
                    for dj in range(start_j, j):
                        nx, ny = i + dx, dj + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] == '*':
                            # If a surrounding cell contains a symbol, add the number to the set of numbers adjacent to the symbol
                            symbol_numbers.setdefault((nx, ny), set()).add(number)
                            break
                    else:
                        continue
                    break
            else:
                # If the cell is not a digit, move to the next cell
                j += 1

    # Multiply the numbers adjacent to each '*' symbol and add them to the sum
    total_sum = 0
    for numbers in symbol_numbers.values():
        # If there are exactly two numbers adjacent to the symbol, multiply them and add the product to the sum
        if len(numbers) == 2:
            numbers = list(numbers)
            total_sum += numbers[0] * numbers[1]

    return total_sum

# Print the total sum for part 1
print(f"Part 1: {parts(input)}")
#Print the total sum for part 2
print(f"Part 2: {gears(input)}")