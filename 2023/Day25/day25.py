"""
This module solves the Advent of Code puzzle for day 24, year 2023.
"""
from time import time

import networkx as nx
from aocd import get_data

data = get_data(day=25, year=2023)
"""with open("test.txt", "r", encoding="utf-8") as file:
    data = file.read()"""
data = data.strip().splitlines()

g = nx.Graph()

for line in data:
    left, right = line.split(":")
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))


start_time = time()

"""print(f"Total (Part1): {totalp1}")
print(f"Total (Part2): {totalp2}")"""

end_time = time()
print(f"Total execution time: {end_time - start_time:.6f} seconds")
