"""
Start over after failed attempt in 2016.
Given a description of the locations of the generators and the microchips,
find the minimum number of steps to move all items to the top
"""

#!/usr/bin/env python3

# -------
# imports
# -------

import sys
from itertools import combinations, chain

# -----------------
# create next state
# -----------------

def create_next_state(state, elevator_change, items):
    """
    Given a state, how many floors to move up/down, and items to move, return the new state
    """
    floors_items, elevator, steps = state
    new_elevator = elevator + elevator_change
    new_floors_items = tuple(floor_items ^ items if floor in {elevator, new_elevator}
                             else floor_items
                             for floor, floor_items in enumerate(floors_items))
    return (new_floors_items, new_elevator, steps + 1)

# --------------
# is state fried
# --------------

def is_fried(floors_items):
    """
    Given a state of item positions, check whether a microchip will get fried
    """
    return any(item[-1] == 'm'
               and item[:-1] + 'g' not in floor
               and any(other_item[-1] == 'g' for other_item in floor)
               for floor in floors_items for item in floor)

# ---------------------
# convert to comparable
# ---------------------

def convert_to_comparable(floors_items, elevator):
    """
    Given a state of item and elevator positions,
    convert it to a structure that's functionally equivalent
    """
    # keep elevator position and make an unordered collection of (m-floor, g-floor) for each element
    # maybe a dict to map (m-floor, g-floor) values to frequency in state
    # first, create a dict mapping elements to location tuple
    # then create a dict mapping location tuples to frequencies and return it w/ elevator position
    # hmm, but i want result to be hashable. use frozenset?
    elems_to_locs = {}
    for i, floor in enumerate(floors_items):
        for item in floor:
            elem, item_type = item[:-1], item[-1]
            if elem in elems_to_locs:
                elems_to_locs[elem][0 if item_type == 'm' else 1] = i
            else:
                elems_to_locs[elem] = [i, -1] if item_type == 'm' else [-1, i]

    locs_to_freqs = {}
    for loc in elems_to_locs.values():
        tuple_loc = tuple(loc)
        locs_to_freqs[tuple_loc] = locs_to_freqs.get(tuple_loc, 0) + 1

    return (frozenset(locs_to_freqs.items()), elevator)

# -----------------
# is state complete
# -----------------

def is_complete(floors_items):
    """
    Given a state of elevator and item positions, return whether the goal state has been achieved
    """
    return not any(floors_items[:-1]) # all floors empty except last

# ----
# read
# ----

def read(string):
    """
    Given a description of what items are on this floor, return a tuple of items
    """
    items = []
    for i, word in enumerate(words := string.split()):
        if 'microchip' in word or 'generator' in word:
            items.append(words[i - 1].replace('-compatible', '') + word[0])

    return frozenset(items)

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    writer a writer
    """
    # format of state: (items on each floor) + elevator position + steps taken so far
    state = (tuple(map(read, reader)),) + (0, 0)
    visited = set()
    fringe = [state]
    while fringe:
        floors_items, elevator, steps = (cur_state := fringe[0])
        del fringe[0]

        # check if state was already visited or fries a chip and skip if so
        comparable = convert_to_comparable(floors_items, elevator)
        if comparable in visited or is_fried(floors_items):
            visited.add(comparable)
            continue

        visited.add(comparable)

        if is_complete(floors_items):
            print(steps)
            break

        # add possible next states to fringe: combos of 2 items up/down, single item up/down
        for items_sizes in chain(combinations(floors_items[elevator], r) for r in range(1, 3)):
            for items in items_sizes:
                elevator_changes = \
                    ([1] if elevator < len(floors_items) - 1 else []) + ([-1] if elevator else [])
                for elevator_change in elevator_changes:
                    fringe.append(create_next_state(cur_state, elevator_change, frozenset(items)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
