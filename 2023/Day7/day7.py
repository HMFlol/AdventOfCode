# timer stuff
import time
start_time = time.perf_counter()

# Open the file and break into hand and bid
with open('test.txt', 'r') as lines:
    hands = [(hand, int(bid)) for hand, bid in (line.split() for line in lines)]

def jacks(hands):
    # Assign better numbers to the cards for sorting
    # Can also do it lexographically eg "T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    def type(hand):
        # Count the number of each card in the hand
        counts = [hand.count(card) for card in set(hand)]
        sorted_counts = sorted(counts, reverse=True)
        # Check for five of a kind
        if sorted_counts == [5]:
            return 6
        # Check for four of a kind
        if sorted_counts == [4, 1]:
            return 5
        # Check for full house
        if sorted_counts == [3, 2]:
            return 4
        # Check for three of a kind
        if sorted_counts == [3, 1, 1]:
            return 3
        # Check for two pair
        if sorted_counts == [2, 2, 1]:
            return 2
        # Check for one pair
        if sorted_counts == [2, 1, 1, 1]:
            return 1
        # High card
        return 0

    # Get the strength of the hand and return the type and strength for sorting by the hands.sort lambda function
    def tiebreak(hand):
        # Assign the strength of each card in the hand to a list
        strength = []
        # For each card in the hand, append the value of the card to the list
        for card in hand:
            strength.append(values.get(card, card))
        # Return the type of the hand and the strength of the hand
        print(type(hand), strength)
        return type(hand), strength
    # Sort the hands by the tiebreak function (type and strength)
    hands.sort(key=lambda hand: tiebreak(hand[0]))
    # To see what's actually happening for fun
    print("Sorted Hands:")
    for rank, (hand, bid) in enumerate(hands, start=1):
        print(f"Rank: {rank}, Hand: {hand}, Bid: {bid}")

    total_winnings = 0
    for rank, (hand, bid) in enumerate(hands, start=1):
        total_winnings += rank * bid

    return total_winnings

def jokers(hands):
    # Changed J to 0
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 0, "Q": 12, "K": 13, "A": 14}
    def type(hand):
        # Count the number of 'J's in the hand
        jokers = hand.count("J")
        # If the hand contains only 'J's, return 6 (five of a kind)
        if jokers == 5:
            return 6
        # Count the number of each card in the hand, not jokers
        counts = [hand.count(card) for card in set(hand) if card != "J"]
        # If there are jokers, add their count to the count of the most common card
        if jokers > 0:
            max_count = counts.index(max(counts))
            counts[max_count] += jokers
        sorted_counts = sorted(counts, reverse=True)
        # Check for five of a kind
        if sorted_counts == [5]:
            return 6
        # Check for four of a kind
        if sorted_counts == [4, 1]:
            return 5
        # Check for full house
        if sorted_counts == [3, 2]:
            return 4
        # Check for three of a kind
        if sorted_counts == [3, 1, 1]:
            return 3
        # Check for two pair
        if sorted_counts == [2, 2, 1]:
            return 2
        # Check for one pair
        if sorted_counts == [2, 1, 1, 1]:
            return 1
        # High card
        return 0

    def tiebreak(hand):
        strength = []
        for card in hand:
            strength.append(values.get(card, card))
        return type(hand), strength

    hands.sort(key=lambda hand: tiebreak(hand[0]))

    total_winnings = 0
    for rank, (hand, bid) in enumerate(hands, start=1):
        total_winnings += rank * bid

    return total_winnings
# Call the functions
print(f"Part 1: {(jacks(hands))}")
print(f"Part 2: {(jokers(hands))}")

# More timing stuff
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Execution Time: {elapsed_time} seconds")
