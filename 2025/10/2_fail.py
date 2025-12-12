"""
Given indicator light diagrams, button wiring schematics, and joltage requirements,
calculate the fewest total button presses required to reach correct joltage levels

NOTE: this does not work for large inputs as the state tree explodes
"""

# -------
# imports
# -------

import sys

# ---------
# configure
# ---------

def configure(machine):
    """
    Given a machine's joltage requirements and button wiring schematics,
    calculate and return the least number of button presses needed to reach correct joltage
    """
    req_jolts, buttons = machine
    initial_jolts = (0,) * len(req_jolts)

    # format of state: current joltage levels, presses made
    initial_state = (initial_jolts, 0)
    visited = set()
    fringe = [initial_state]
    seen_presses = set()
    while fringe:
        jolts, presses = fringe[0]
        del fringe[0]
        if presses not in seen_presses:
            print(presses)
            seen_presses.add(presses)

        if jolts in visited or any(jolt > req_jolts[i] for i, jolt in enumerate(jolts)):
            visited.add(jolts)
            continue

        visited.add(jolts)

        if jolts == req_jolts:
            print(machine, presses)
            return presses

        for button in buttons:
            new_jolts_list = list(jolts)
            for to_inc in button:
                new_jolts_list[to_inc] += 1
            new_jolts = tuple(new_jolts_list)
            fringe.append((new_jolts, presses + 1))

    return -1

# ----
# read
# ----

def read(string):
    """
    get joltage requirements and button wiring schematic
    """
    jolt_str, buttons_strs = (machine := string.split())[-1], machine[1:-1]
    jolt = tuple(map(int, jolt_str[1:-1].split(',')))
    buttons = tuple(tuple(map(int, buttons_str[1:-1].split(','))) for buttons_str in buttons_strs)
    return jolt, buttons

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    """
    print(sum(map(configure, map(read, reader))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
