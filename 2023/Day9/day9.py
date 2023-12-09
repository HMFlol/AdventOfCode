import time
# timer stuff
start_time = time.time()

# Open the file and break the two lines into time and dist
sequences = [list(map(int, line.split())) for line in open('input.txt').read().splitlines()]

def seq(sequences):
    starttime = time.time()

    results = []
    for sequence in sequences:
        diffs = [sequence]
        while not all(x == 0 for x in diffs[-1]):
            diffs.append([b - a for a, b in zip(diffs[-1], diffs[-1][1:])])
        diffs[-1].append(0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][-1] + diffs[i+1][-1])
        results.append(diffs[0][-1])

    endtime = time.time()

    print(f"Part 1: {sum(results)}, Time: {endtime - starttime:.6f} seconds")

def revseq(sequences):
    starttime = time.time()

    results = []
    for sequence in sequences:
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
