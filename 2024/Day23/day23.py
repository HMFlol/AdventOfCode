# Solution for Advent of Code 2024, Day 23
# https://adventofcode.com/2024/day/23
from time import perf_counter

import networkx as nx


def find_triangles(conn_list):
    """Find the number of triangles in the graph using an adjacency list."""
    triangles = set()

    for c1 in conn_list:
        for c2 in conn_list[c1]:
            if c2 > c1:
                for c3 in conn_list[c2]:
                    if c3 > c2 and c3 in conn_list[c1] and any(c.startswith("t") for c in (c1, c2, c3)):
                        triangles.add((c1, c2, c3))

    return len(triangles)


def find_password(conn_list):
    """Find the maximum clique in the graph using networkx and join it, sorted, on , ."""
    networks = [{c} for c in conn_list]
    for n in networks:
        for c in conn_list:
            if all(d in conn_list[c] for d in n):
                n.add(c)

    return ",".join(sorted(max(networks, key=len)))


def find_triangles_nx(graph):
    """Find the number of triangles in the graph using networkx."""
    triangles_nx = [com for com in nx.enumerate_all_cliques(graph) if len(com) == 3]

    return len([triangle for triangle in triangles_nx if any(com.startswith("t") for com in triangle)])


def find_password_nx(graph):
    """Find the maximum clique in the graph using networkx and join it, sorted, on , ."""
    max_clique_nx = nx.find_cliques(graph)
    max_clique = max(max_clique_nx, key=len)

    return ",".join(sorted(max_clique))


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip()

    conn_list = {}
    graph = nx.Graph()
    for connection in data.splitlines():
        com1, com2 = connection.split("-")
        conn_list.setdefault(com1, []).append(com2)
        conn_list.setdefault(com2, []).append(com1)
        graph.add_edge(com1, com2)

    p1, p2 = find_triangles(conn_list), find_password(conn_list)
    # p1, p2 = find_triangles_nx(graph), find_password_nx(graph)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
