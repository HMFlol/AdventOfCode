# Read the lines
with open('input.txt', 'r') as i:
    lines = i.readlines()

# Part 1
def gameSum():
    # Initialize the sum of game numbers
    sum = 0

    # Run through each line
    for line in lines:
        # Split the line by colon to separate the game number and the rest
        game_info = line.split(':')
        
        # Get the game number from the first part (game_info[0])
        game_number = int(game_info[0].split()[1].strip())

        # Get the parts of the game from the second part (game_info[1])
        parts = game_info[1].split(';')

        # Initialize a flag for the game possibility (True by default because optimism - Will be set to False if the game is not possible)
        game_possible = True

        # Run through each part of the game
        for part in parts:
            # Dictionary to hold the limit for the number of each colour because I like dictionaries (could also be a list, eg. limits = [12, 13, 14]  I guess?)
            limits = {'red': 12, 'green': 13, 'blue': 14}

            # Split the part by comma to get the sets
            sets = part.split(',')

            # Run through each set
            for set in sets:
                # Split the set by space to get the quantity and the colour (e.g. "3 red" -> ["3", "red"]) and convert the quantity to an integer
                quantity, colour = set.strip().split()
                quantity = int(quantity)

                # Check if the quantity exceeds the limit for the colour
                if quantity > limits[colour]:
                    # If the quantity exceeds the limit, set the flag to False and break the loop
                    game_possible = False
                    break

        # If the game is possible, add its game number to the sum
        if game_possible:
            sum += game_number

    # Return the sum
    return sum

# Part 2 - very similar to Part 1 - maybe could have been combined into one function with a parameter for the power? I can do that later for funzies :D
def powerSum():
    # Initialize the sum of game numbers
    sum = 0

    # Run through each line
    for line in lines:
        # Split the line by colon to separate the game number and the rest
        game_info = line.split(':')

        # Get the parts of the game from the second part (game_info[1])
        parts = game_info[1].split(';')

        # Initialize a dictionary to store the maximum quantity of each color (again, dictionaries are cool.) Outside of the parts loop because we want to keep the maximum quantity of each color for the whole game
        max = {'red': 0, 'green': 0, 'blue': 0}

        # Run through each part of the game
        for part in parts:
            # Split the part by comma to get the sets (as in Part 1)
            sets = part.split(',')

            # Run through each set
            for set in sets:
                # Split the set by space to get the quantity and the color (e.g. "3 red" -> ["3", "red"]) and convert the quantity to an integer
                quantity, color = set.strip().split()
                quantity = int(quantity)

                # Update the maximum quantity of the color if the current quantity is greater
                if quantity > max[color]:
                    max[color] = quantity

        # Multiply the maximum quantities together and add the result to the sum
        product = max['red'] * max['green'] * max['blue']
        sum += product

    # Return the sum
    return sum

# Print the sum for Part 1
print(gameSum())
# Print the sum for Part 2
print(powerSum())