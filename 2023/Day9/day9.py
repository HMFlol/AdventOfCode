import time
# timer stuff
start_time = time.time()

# Open the file and break the two lines into time and dist
sequences = [list(map(int, line.split())) for line in open('input.txt').read().splitlines()]

# Part 1
def seq(sequences):
    starttime = time.time()
    # Final results
    results = []
    for sequence in sequences:
        # Store the current sequence
        diffs = [sequence]
        # While the last sequence in diffs is not all 0s...
        while not all(x == 0 for x in diffs[-1]):
            # Append the difference between each pair of numbers in the last sequence in diffs
            diffs.append([b - a for a, b in zip(diffs[-1], diffs[-1][1:])])
        # Once it's all 0 append a 0 to the last sequence in diffs
        diffs[-1].append(0)
        # For each sequence in diffs starting with the second to last(the last sequence is all 0) and going backwards or up to the first sequence...
        for i in range(len(diffs) - 2, -1, -1):
            # Append the sum of the last number in the current sequence and the last number in the sequence under or after it
            diffs[i].append(diffs[i][-1] + diffs[i+1][-1])
        # Append the last number in the first sequence in diffs to results
        results.append(diffs[0][-1])

    endtime = time.time()

    print(f"Part 1: {sum(results)}, Time: {endtime - starttime:.6f} seconds")

# Part 2
def revseq(sequences):
    starttime = time.time()

    results = []
    for sequence in sequences:
        # Just reverse the sequence and voila! Everything else is the same.
        sequence = sequence[::-1]
        diffs = [sequence]
        while not all(x == 0 for x in diffs[-1]):
            diffs.append([b - a for a, b in zip(diffs[-1], diffs[-1][1:])])
        diffs[-1].append(0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][-1] + diffs[i+1][-1])
        results.append(diffs[0][-1])

    endtime = time.time()

    print(f"Part 2: {sum(results)}, Time: {endtime - starttime:.6f} seconds")

# Call the functions
seq(sequences)
revseq(sequences)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Total execution time: {elapsed_time:.6f} seconds")