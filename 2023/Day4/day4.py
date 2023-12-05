# Read the lines
with open('input.txt', 'r') as r:
    lines = r.readlines()

# Matching all on its own
def get_match(line):
    # Get the two sets of numbers from the card line and convert them to sets of integers (nset1 and nset2)
    nums = line.split(':')[1].split('|')
    nset1 = set([int(num) for num in nums[0].split()])
    nset2 = set([int(num) for num in nums[1].split()])
    # Match is the number of numbers that are in both sets (the intersection of the two sets)
    match = len(nset1 & nset2)
    return match

# Part 1
def score(lines):
    # Initialize the total score
    total_score = 0
    # Iterate over each card line
    for line in lines:
        # Get the match for the card line
        match = get_match(line)
        if match > 0:
            # Score is 2 to the power of the number of numbers that are in both sets (the intersection of the two sets)
            total_score += 2 ** (match - 1)

    return total_score 

# Part 2
def cards(lines):
    # Create a dictionary to store the card lines by card number (key = card number, value = list of card lines)
    cards_dict = {}
    for line in lines:
        card_num = int(line.split(':')[0].split()[-1])
        if card_num not in cards_dict:
            cards_dict[card_num] = []
        cards_dict[card_num].append(line)

    # Initialize a counter for each card number (key = card number, value = number of cards)
    card_counts = {card_num: 1 for card_num in cards_dict.keys()}

    # The number of OG cards is the number of cards in the dictionary
    total_cards = len(cards_dict)
    # Loop through each card number in ascending order
    for card_num in sorted(cards_dict.keys()):
        # Get the match for the card line
        match = get_match(cards_dict[card_num][0])
        # Add the number of cards that can be made from the card line to the total number of cards
        # for i in range(1, match + 1): if match is 0, this loop will not run
        for i in range(1, match + 1):
            # If the card number + i is not in the dictionary, add it to the dictionary and set its count to 0
            if card_num + i in cards_dict:
                # If the card number + i is in the dictionary, add the number of cards that can be made from the card line to the total number of cards for the card number + i
                card_counts[card_num + i] += card_counts[card_num]
                # Add the number of cards that can be made from the card line to the total number of cards
                total_cards += card_counts[card_num]

    return total_cards

print(f"Part 1: {score(lines)}")
print(f"Part 2: {cards(lines)}")