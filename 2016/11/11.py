"""
Given a description of the locations of the generators and the microchips,
find the minimum number of steps to move all items to the top
"""

#!/usr/bin/env python3

# -------
# imports
# -------

import sys
from itertools import combinations, accumulate
from element_symbols_dict import element_symbols

# -----------
# global vars
# -----------

chips_to_gens = {}
HORIZON = 33 # user specified number of moves to try to match or beat
# at floor f and stack level s, all states in bad_states[f][s] are known to be bad paths
# unfortunately hardcoding in number of floors here
bad_states = tuple(tuple(set() for i in range(HORIZON + 1)) for j in range(4))

# ---
# run
# ---

def run(state, elevator, all_states, w, level):
    """
    recursively search through possible moves to find a way to get all items to top
    """
    w.write(str(state) + ' ' + str(elevator) + ' ' + str(level) + '\n')
    # base case: all microchips and generators are on the final floor
    if len(state[-1]) == len(chips_to_gens) * 2 and not any(state[:-1]):
        return level

    # if it's clearly impossible to move all first floor items in time
    # or the stack is already too deep, return 0 to indicate dead end
    lowest = next(i for i,v in enumerate(state) if v)
    if level + elevator - lowest + \
       sum(i * 2 - 3 if i > 1 else i
           for i in accumulate(
               len(v) + (1 if not j else 0) + (-1 if j == elevator - lowest else 0)
               for j, v in enumerate(state[lowest:-1])
               )
           ) > HORIZON:
        # store level and state in bad_states
        bad_states[elevator][level].add(state)
        return 0
    # best = 0 # ok as an original value because best will never be zero if the base case wasn't met
    # gather results of all possible paths and return the best one
    # iterate over all combinations of 1 or 2 items to move, try both up and down
    # first, try moving two items; use itertools.combinations() to avoid repeating pairs tried
    for item_1, item_2 in combinations(state[elevator], 2):
        if elevator != len(state) - 1: # must be below top floor to move up
            next_state = new_state(state, elevator, 1, {item_1, item_2})
            if not fried(next_state) and next_state not in all_states[elevator + 1] and \
               all(next_state not in bs for bs in bad_states[elevator + 1][2:level + 2]):
                temp = run(
                    next_state, elevator + 1,
                    all_states[:elevator + 1]
                        + (all_states[elevator + 1] | {next_state},)
                        + all_states[elevator + 2:],
                    w, level + 1
                    )
                # if (temp < best or not best) and temp:
                    # best = temp
                if temp:
                    return temp
        # must be above first floor and not cause a clearly invalid situation to move down
        if elevator and level + len(state) - elevator + 1 <= HORIZON:
            next_state = new_state(state, elevator, -1, {item_1, item_2})
            if not fried(next_state) and next_state not in all_states[elevator - 1] and \
               all(next_state not in bs for bs in bad_states[elevator - 1][2:level + 2]):
                temp = run(
                    next_state, elevator - 1,
                    all_states[:elevator - 1]
                        + (all_states[elevator - 1] | {next_state},)
                        + all_states[elevator:],
                    w, level + 1
                    )
                # if (temp < best or not best) and temp:
                    # best = temp
                if temp:
                    return temp
    # next, moving that item alone
    for item_1 in state[elevator]:
        if elevator != len(state) - 1: # must be below top floor to move up
            next_state = new_state(state, elevator, 1, {item_1})
            if not fried(next_state) and next_state not in all_states[elevator + 1] and \
               all(next_state not in bs for bs in bad_states[elevator + 1][2:level + 2]):
                temp = run(
                    next_state, elevator + 1,
                    all_states[:elevator + 1]
                        + (all_states[elevator + 1] | {next_state},)
                        + all_states[elevator + 2:],
                    w, level + 1
                    )
                # if (temp < best or not best) and temp:
                    # best = temp
                if temp:
                    return temp
        # must be above first floor and not cause a clearly invalid situation to move down
        if elevator and level + len(state) - elevator + 1 <= HORIZON:
            next_state = new_state(state, elevator, -1, {item_1})
            if not fried(next_state) and next_state not in all_states[elevator - 1] and \
               all(next_state not in bs for bs in bad_states[elevator - 1][2:level + 2]):
                temp = run(
                    next_state, elevator - 1,
                    all_states[:elevator - 1]
                        + (all_states[elevator - 1] | {next_state},)
                        + all_states[elevator:],
                    w, level + 1
                    )
                # if (temp < best or not best) and temp:
                    # best = temp
                if temp:
                    return temp
    # if best is still 0, this path of moves is no good and the return value will indicate this
    # if not best and level > 1:
    # 	# store level and state in bad_states
    # 	bad_states[elevator][level].add(state)
    # return best
    bad_states[elevator][level].add(state)
    return 0

# ---------
# new_state
# ---------

def new_state(state, elevator, direction, items):
    """
    return the state of the floors given items to move
    and direction to move in (expressed as the value of new floor - current floor)
    """
    # sacrificed flexibility for speed: only works w/ directions 1 and -1
    return state[:elevator + (direction - 1) // 2] + \
           (
                state[elevator + (direction - 1) // 2] ^ items,
                state[elevator + (direction + 1) // 2] ^ items
           ) + \
           state[elevator + (direction + 3) // 2:]

# -----
# fried
# -----

def fried(state):
    """
    given a possible state of the floors, determine whether any microchips will get fried
    """
    return any(item[-1] == 'M'
               and chips_to_gens[item] not in floor
               and any(poss_gen[-1] == 'G' for poss_gen in floor)
               for floor in state for item in floor)

# ----
# read
# ----

def read(line):
    """
    record which items are on the floor
    """
    words = line.split()
    for i in range(2, len(words)):
        if 'generator' in words[i]:
            symbol = element_symbols[words[i - 1]]
            yield symbol + 'G'
        elif 'microchip' in words[i]:
            symbol = element_symbols[words[i - 1].replace('-compatible', '')]
            chips_to_gens[symbol + 'M'] = symbol + 'G'
            yield symbol + 'M'

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    initial = tuple(frozenset(read(line)) for line in reader)
    elevator = 0
    out = run(
        initial, elevator,
        (frozenset(),) * elevator
            + (frozenset(initial),)
            + (frozenset(),) * (len(initial) - elevator - 1),
        writer, 0)
    writer.write(str(out) if out else 'Either unsatisfiable or all items are already on top floor')

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
