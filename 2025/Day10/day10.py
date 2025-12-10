# Solution for Advent of Code 2025, Day 10
# https://adventofcode.com/2025/day/10
import re
from collections import deque
from time import perf_counter

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def part1(lights_off, lights_goal, buttons):
    """Find the minimum number of button presses to reach the goal light state using BFS."""
    queue = deque([(lights_off, 0)])
    visited = {lights_off}
    # BFS
    while queue:
        current_state, presses = queue.popleft()  # Current light state and presses made
        # Check if goal state is reached
        if current_state == lights_goal:
            return presses
        # Try pressing each button
        for button in buttons:
            new_state = list(current_state)
            # Toggle lights for the button pressed
            for pos in button:
                new_state[pos] = "#" if new_state[pos] == "." else "."
            # Normalize the state
            new_state = "".join(new_state)
            # If new state not visited, add to queue
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))


def part2_ilp(joltage_goal, buttons):
    """Solve the minimum button presses to reach the goal joltage using Integer Linear Programming. BFS was no bueno."""
    n_joltages = len(joltage_goal)
    n_buttons = len(buttons)

    # Build matrix A
    matrix_a = [[int(i in button) for button in buttons] for i in range(n_joltages)]

    # Objective: minimize sum of button presses
    c = [1] * n_buttons

    # Constraints: A*x = joltage_goal
    constraints = LinearConstraint(matrix_a, lb=joltage_goal, ub=joltage_goal)

    # Bounds: x >= 0, integer variables
    integrality = [1] * n_buttons  # 1 means integer variable
    bounds = Bounds(lb=[0] * n_buttons, ub=[np.inf] * n_buttons)

    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

    return int(sum(result.x)) if result.success else None


if __name__ == "__main__":
    start_time = perf_counter()
    data = open(0).read().strip().splitlines()

    machines = []
    # Get lights, buttons, and joltages for each machine
    for machine in data:
        lights = re.search(r"\[([^]]+)]", machine).group(1)
        buttons = [[int(x) for x in match.split(",")] for match in re.findall(r"\(([^)]+)\)", machine)]
        joltages = [int(x) for x in re.search(r"\{([^]]+)}", machine).group(1).split(",")]

        machines.append((lights, buttons, joltages))

    p1 = sum(part1("." * len(lights), lights, buttons) for lights, buttons, _ in machines)

    p2 = sum(part2_ilp(joltages, buttons) for _, buttons, joltages in machines)

    print("\033[1mPart1:\033[22m", p1)
    print("\033[1mPart2:\033[22m", p2)

    end_time = perf_counter()
    print(f"\033[2mTime: {end_time - start_time:.4f}s\033[22m")
