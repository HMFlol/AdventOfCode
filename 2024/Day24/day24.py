# Solution for Advent of Code 2024, Day 24
# https://adventofcode.com/2024/day/24
from time import perf_counter

operations = {"AND": lambda a, b: a & b, "OR": lambda a, b: a | b, "XOR": lambda a, b: a ^ b}


def produce(wires_dict, gates_list):
    """Produce the output for the given wires_dict and gates_list and outputs."""
    gates_listc = gates_list.copy()
    outputs = {}

    while gates_listc:
        for w1, op, w2, out in gates_listc:
            if w1 in wires_dict and w2 in wires_dict:
                outputs[out] = operations[op](wires_dict[w1], wires_dict[w2])
                wires_dict[out] = outputs[out]
                gates_listc.remove((w1, op, w2, out))

    binary = "".join(str(outputs[key]) for key in sorted(outputs) if key.startswith("z"))
    converted_num = int(binary[::-1], 2)

    return converted_num


def find_baddies(gates_list):
    """Find the swapped gates/bad gates in the gates_list, based on the expected behavior/rules of a correctly implemented ripple carry adder."""
    """Gates represents a ripple carry adder circuit.
    z wires represent the carry bits in the adder.
    x and y wires represent the input bits.
    high_z represents the highest carry bit in the adder, which is also the final carry-out bit.

    Ripple Carry Adder Rules (for identifying potentially bad wires):

    1. Intermediate Carry Wires (z) Should Be XOR Results:
       - Any 'z' wire (except the final carry-out, high_z) should be the result of an XOR operation.
       - If a 'z' wire is produced by AND or OR directly, it's likely incorrect.

    2. XOR Primarily for Sum Bits:
       - XOR operations should primarily involve input wires ('x', 'y') and carry wires ('z') to calculate sum bits.
       - An XOR between other types of wires is suspicious.

    3. AND Typically Feeds into OR (except for x00):
       - The output of an AND gate (unless involving 'x00') should usually feed into an OR gate as part of carry generation.
       - If an AND result is used in any operation other than OR, it might indicate an error.

    4. Sum Bits (XOR Results) Should Not Directly Feed Carry Logic (OR):
       - The output of an XOR gate (representing a sum bit) should not be directly used as input to an OR gate that's part of the carry calculation.
    """
    z_wires = [out for _, _, _, out in gates_list if out.startswith("z")]
    high_z = max(z_wires, key=lambda x: int(x[1:]), default=None)
    baddies = set()

    for w1, op, w2, out in gates_list:
        if out.startswith("z") and op != "XOR" and out != high_z:
            baddies.add(out)
        if op == "XOR" and all(x[0] not in "xyz" for x in (w1, w2, out)):
            baddies.add(out)
        if op == "AND" and "x00" not in (w1, w2):
            if any((out in (sw1, sw2)) and subop != "OR" for sw1, subop, sw2, _ in gates_list):
                baddies.add(out)
        if op == "XOR":
            if any((out in (sw1, sw2)) and subop == "OR" for sw1, subop, sw2, _ in gates_list):
                baddies.add(out)

    return ",".join(sorted(baddies))


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()
    wires, gates = data.split("\n\n")

    wires_dict = {key: int(val) for key, val in (line.split(": ") for line in wires.splitlines())}
    gates_list = [tuple(line.replace("->", "").split()) for line in gates.splitlines()]

    p1 = produce(wires_dict, gates_list)
    p2 = find_baddies(gates_list)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
