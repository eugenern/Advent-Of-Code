"""
Given indicator light diagrams, button wiring schematics, and joltage requirements,
calculate the fewest total button presses required to initialize all machines

NOTE: may want to redo this as BFS isn't necessary -- just go through all combinations of all sizes
of pressing buttons once each
"""

# -------
# imports
# -------

import sys

# ----------
# initialize
# ----------

def initialize(machine):
    """
    Given a machine's indicator light diagram and button wiring schematics,
    calculate and return the least number of button presses needed to initialize the machine
    """
    req_lights, buttons = machine
    initial_lights = (False,) * len(req_lights)

    # format of state: current lights, presses made
    initial_state = (initial_lights, 0)
    visited = set()
    fringe = [initial_state]
    while fringe:
        lights, presses = fringe[0]
        del fringe[0]

        if lights in visited:
            continue

        visited.add(lights)

        if lights == req_lights:
            return presses

        for button in buttons:
            new_lights_list = list(lights)
            for to_toggle in button:
                new_lights_list[to_toggle] = not new_lights_list[to_toggle]
            new_lights = tuple(new_lights_list)
            fringe.append((new_lights, presses + 1))

    return -1

# ----
# read
# ----

def read(string):
    """
    get indicator light diagram and button wiring schematic
    """
    lights_str, buttons_strs = (machine := string.split())[0], machine[1:-1]
    lights = tuple(c == '#' for c in lights_str[1:-1])
    buttons = tuple(tuple(map(int, buttons_str[1:-1].split(','))) for buttons_str in buttons_strs)
    return lights, buttons

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    """
    print(sum(map(initialize, map(read, reader))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
