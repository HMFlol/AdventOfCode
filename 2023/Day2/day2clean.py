# Read the lines
with open('input.txt', 'r') as i:
    lines = i.readlines()

def cubes(mode):
    # Initialize sum and limits dictionary
    sum = 0
    limits = {'red': 12, 'green': 13, 'blue': 14}

    # Loop through each line
    for line in lines:
        # Split the line by colon to separate the game number and the rest
        game_info = line.split(':')
        parts = game_info[1].split(';')
        # Initialize a dictionary to hold the maximum quantities of each colour
        max = {'red': 0, 'green': 0, 'blue': 0}
        game_possible = True

        # Loop through each part of the game
        for part in parts:
            # Split the part by comma to get the sets
            sets = part.split(',')

            # Loop through each set
            for set in sets:
                # Split the set by space to get the quantity and the colour (e.g. "3 red" -> ["3", "red"]) and convert the quantity to an integer
                quantity, colour = set.strip().split()
                quantity = int(quantity)

                # If mode is game, check if the quantity exceeds the limit for the colour. If it does, set the game_possible flag to False and break the loop
                if mode == 'game':
                    if quantity > limits[colour]:
                        game_possible = False
                        break
                # If mode is power, check if the quantity is greater than the current maximum quantity for the colour. If it is, set the maximum quantity for the colour to the quantity
                elif mode == 'power':
                    if quantity > max[colour]:
                        max[colour] = quantity

        # If mode is game and the game is possible, add the game number to the sum. 
        if mode == 'game' and game_possible:
            game_number = int(game_info[0].split()[1].strip())
            sum += game_number
        # If mode is power, calculate the product of the maximum quantities and add it to the sum
        elif mode == 'power':
            product = max['red'] * max['green'] * max['blue']
            sum += product

    return sum

print(f"Part 1: {cubes('game')}")
print(f"Part 2: {cubes('power')}")