# Read the lines
with open('input.txt', 'r') as i:
    lines = i.readlines()

# Join the lines into a single string
input_str = ''.join(lines)

def sum_part_numbers(input_str):
    # Parse the input into a 2D array
    grid = [list(line) for line in input_str.split('\n')]

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

# Call the function with the input
total_sum = sum_part_numbers(input_str)

# Print the total sum
print(total_sum)
