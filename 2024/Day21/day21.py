# Solution for Advent of Code 2024, Day 21
# https://adventofcode.com/2024/day/21
from collections import deque
from functools import cache
from itertools import product
from time import perf_counter


def make_keypad(keys):
    """Create the keypads."""
    keypad = {}
    for i, c in enumerate(keys):
        if c == " ":
            continue
        pos = (i // 3, i % 3)
        keypad[c] = pos
    return keypad


def keypad_bfs(keypad):
    """BFS to find the shortest paths to each key in the keypad."""
    seqs = {}
    dirs = [(-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")]
    for x in keypad:
        for y in keypad:
            if x == y:
                seqs[(x, y)] = ["A"]  # No movement needed if at A
                continue
            possible = []
            queue = deque([(keypad[x], "", 0)])
            optimal = []
            while queue:
                (r, c), path, dist = queue.popleft()
                if dist > optimal:
                    continue
                if (r, c) == keypad[y]:
                    possible.append(path + "A")
                    optimal = dist
                    continue
                # Check all directions
                for dr, dc, move in dirs:
                    nr, nc = r + dr, c + dc
                    # Bounds check
                    if (nr, nc) in keypad.values():
                        queue.append(((nr, nc), path + move, dist + 1))
            seqs[(x, y)] = possible
    return seqs


@cache
def get_length(seq, depth):
    """Get the length of the sequence."""
    if depth == 1:
        return sum(dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        length += min(get_length(subseq, depth - 1) for subseq in dir_seqs[(x, y)])
    return length


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()
    # Make the keypads
    numpad = make_keypad("789456123 0A")
    dirpad = make_keypad(" ^A<v>")
    # Get all of the optimal sequences of button presses for both pads
    num_seqs = keypad_bfs(numpad)
    dir_seqs = keypad_bfs(dirpad)
    # Get the lengths of the sequences for dirpad
    dir_lengths = {k: len(v[0]) for k, v in dir_seqs.items()}
    p1 = 0
    p2 = 0
    for code in data.splitlines():
        codenum = int(code[:-1])
        # Get the shortest path to press all keys
        presses = ["".join(x) for x in product(*(num_seqs[(x, y)] for x, y in zip("A" + code, code)))]
        # Get the min length of the sequence at x depth and ultiply the length by the num in the code
        p1 += codenum * min(get_length(seq, depth=2) for seq in presses)
        p2 += codenum * min(get_length(seq, depth=25) for seq in presses)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
