# Open the file 'test.txt' in read mode ('r') and read all lines into a list
with open('test.txt', 'r') as r:
    lines = r.readlines()

# Part 1 (works)
def process_categories_and_seeds(lines):
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
    # This function takes a start, length, and category, and splits and converts a range based on the category
    def split_and_convert_range(start, length, category):
        # Unpack the category into start, start, and length
        dest_start, src_start, src_length = category
        # Calculate the end of the category's range
        src_end = src_start + src_length - 1
        # Calculate the end of the input range
        end = start + length - 1

        # If the input range doesn't overlap with the category's range, return the input range as is
        if end < src_start or start > src_end:
            return [(start, length)]
        else:
            # If the input range does overlap with the category's range, we need to split it
            ranges = []

            # If there's a part of the input range before the category's range, add it to the output
            if start < src_start:
                ranges.append((start, src_start - start))

            # Convert the part of the input range that overlaps with the category's range
            converted_start = max(start, src_start)
            converted_end = min(end, src_end)
            converted_length = converted_end - converted_start + 1
            ranges.append((dest_start + (converted_start - src_start), converted_length))

            # If there's a part of the input range after the category's range, add it to the output
            if end > src_end:
                ranges.append((converted_end + 1, end - src_end))

            return ranges

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

    # Get the seed ranges
    seed_ranges = categories.pop('seeds')[0]

    # Merge all the categories into one list and sort it by the end value
    merged_categories = []
    for category in categories.values():
        merged_categories.extend(category)
    merged_categories.sort(key=lambda x: x[1])

    # Create a list of ranges from the seed ranges
    ranges = [(seed_ranges[i], seed_ranges[i+1]) for i in range(0, len(seed_ranges), 2)]

    # Go through each category
    for category in merged_categories:
        new_ranges = []
        for start, length in ranges:
            # Split and convert each range based on the current category
            new_ranges.extend(split_and_convert_range(start, length, category))
        ranges = new_ranges

    # Find the smallest start value from the final ranges
    min_location = min(ranges, key=lambda x: x[0])[0]

    return min_location

# Call the functions
print(f"Part 1: {process_categories_and_seeds(lines)}")
print(f"Part 2: {process_seed_ranges(lines)}")