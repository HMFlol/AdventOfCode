import sys

# Open the file 'test.txt' in read mode ('r') and read all lines into a list
with open('input.txt', 'r') as r:
    lines = r.readlines()

# Part 1 (works)
def process_categories_and_seeds(lines):
    # This function takes a number and a category, and converts the number based on the category
    def convert_number(num, category):
        # For each category, check if the number falls within the category's range
        for dest_start, src_start, length in category:
            if src_start <= num < src_start + length:
                # If it does, convert the number and return it
                return dest_start + (num - src_start)
        # If the number doesn't fall within any category's range, return it as is
        return num

    # Create a dictionary to store the categories and their respective values
    categories = {}
    current_category = None

    # Go through each line in the file
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if ":" in line:
            # If a line contains ':', it's defining a new category
            current_category, numbers = line.split(":")  # Split the line into category name and numbers
            numbers = numbers.strip()  # Remove leading and trailing whitespace from the numbers
            # If there are no numbers, store an empty list for this category; otherwise, store the numbers as a list of integers
            categories[current_category] = [] if not numbers else [list(map(int, numbers.split()))]
        elif line:
            # If the line is not empty and doesn't contain ':', it's adding more numbers to the current category
            categories[current_category].append(list(map(int, line.split())))

    # Get the seed values and the names of the categories
    seeds = categories.pop('seeds')[0]
    category_names = list(categories.keys())

    # Start with the minimum location being infinity (so any number we compare it to will be smaller)
    min_location = float('inf')

    # Go through each seed
    for seed in seeds:
        # Convert the seed based on each category
        for category_name in category_names:
            seed = convert_number(seed, categories[category_name])
        # If this seed's location is smaller than the current minimum, update the minimum
        min_location = min(min_location, seed)

    # Return the smallest location we found
    return min_location

# Part 2 (doesn't work - works for test but not actual input)
def process_seed_ranges(lines):
    # Create a dictionary to store the categories and their respective values
    categories = {}
    # Initialize the current category to None
    current_category = None

    # Iterate over each line in the input like in pt 1
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if ":" in line:  # If the line contains ":", it's defining a new category
            current_category, numbers = line.split(":")  # Split the line into category name and numbers
            numbers = numbers.strip()  # Remove leading and trailing whitespace from the numbers
            # If there are no numbers, store an empty list for this category; otherwise, store the numbers as a list of integers
            categories[current_category] = [] if not numbers else [list(map(int, numbers.split()))]
        elif line:  # If the line is not empty, it's adding more numbers to the current category
            categories[current_category].append(list(map(int, line.split())))

    # Extract the seed ranges and the maps from the categories
    seeds = categories.pop('seeds')[0]
    inputs = list(categories.values())

    # Initialize the list of seed ranges
    seed_ranges = []
    # Iterate over pairs of numbers in the seeds list
    for i in range(0, len(seeds), 2):
        # Each pair of numbers represents a range, so add it to the list of seed ranges
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

    # Iterate over each map
    for m in inputs:
        # Initialize the list of new ranges
        new_ranges = []
        # While there are still seed ranges to process
        while len(seed_ranges) > 0:
            # Pop a seed range from the list
            s, e = seed_ranges.pop()
            # Iterate over each range in the map
            for map_start, map_end, length in m:
                # Calculate the overlap of the seed range with the map range
                os = max(s, map_end)
                oe = min(e, map_end + length)
                # If the seed range overlaps with the map range
                if os < oe:
                    # Add the corresponding range in the destination space to the list of new ranges
                    new_ranges.append((os - map_end + map_start, oe - map_end + map_start))
                    # If there is a part of the seed range before the overlap, add it back to the list of seed ranges for further processing
                    if os > s:
                        seed_ranges.append((s, os))
                    # If there is a part of the seed range after the overlap, add it back to the list of seed ranges for further processing
                    if e > oe:
                        seed_ranges.append((oe, e))
                    break  # We've processed this seed range, so we can move on to the next one
            else:
                # If the seed range doesn't overlap with any map range, add it to the list of new ranges as is
                new_ranges.append((s, e))
        # Replace the list of seed ranges with the list of new ranges for the next iteration
        seed_ranges = new_ranges

    return min(seed_ranges)[0]

# Call the functions
print(f"Part 1: {process_categories_and_seeds(lines)}")
print(f"Part 2: {process_seed_ranges(lines)}")