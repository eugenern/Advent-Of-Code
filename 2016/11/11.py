"""
Given a description of the locations of the generators and the microchips, find the minimum number of steps to move all items to the top
"""

#!/usr/bin/env python3

# -------
# imports
# -------

import sys
from element_symbols_dict import element_symbols
from copy import deepcopy
from bisect import insort

# -----------
# global vars
# -----------

correspondings = {}
HORIZON = 11 # user specified number of moves to try to match or beat

# ---
# run
# ---

def run(state, elevator, all_states, w, level):
	"""
	recursively search through possible moves to find a way to get all items to top
	"""
	w.write(str(state) + ' ' + str(level) + '\n')
	# base case: all microchips and generators are on the final floor
	if len(state[-1]) == len(correspondings) * 2:
		return level

	# if the stack is too deep or it's clearly impossible to move all first floor items in time, return 0 to indicate dead end
	if level == HORIZON or state[0] and level + (len(state) - 1) * (2 * max(2, len(state[0])) - (len(state) - 1)) > HORIZON:
		return 0
	best = 0 # ok as an original value because best will never be zero if the base case wasn't met
	# gather results of all possible paths and return the best one
	# iterate over all combinations of 1 or 2 items to move, try both up and down
	for item_1 in state[elevator]:
		# first, try moving two items; avoid repeating pairs tried
		position = state[elevator].index(item_1)
		for item_2 in state[elevator][(position + 1):]:
			# same as above, try moving up and down
			if elevator != len(state) - 1: # must be below top floor to move up
				next_state = new_state(state, elevator, 1, item_1, item_2)
				if not fried(next_state) and next_state not in all_states:
					temp = run(next_state, elevator + 1, all_states + [next_state], w, level + 1)
					if (temp < best or not best) and temp:
						best = temp
					if temp and temp <= HORIZON:
						return temp
			if elevator != 0: # must be above first floor to move down
				next_state = new_state(state, elevator, -1, item_1, item_2)
				if not fried(next_state) and next_state not in all_states:
					temp = run(next_state, elevator - 1, all_states + [next_state], w, level + 1)
					if (temp < best or not best) and temp:
						best = temp
					if temp and temp <= HORIZON:
						return temp
		# next, moving that item alone
		if elevator != len(state) - 1: # must be below top floor to move up
			next_state = new_state(state, elevator, 1, item_1)
			if not fried(next_state) and next_state not in all_states:
				temp = run(next_state, elevator + 1, all_states + [next_state], w, level + 1)
				if (temp < best or not best) and temp:
					best = temp
				if temp and temp <= HORIZON:
					return temp
		if elevator != 0: # must be above first floor to move down
			next_state = new_state(state, elevator, -1, item_1)
			if not fried(next_state) and next_state not in all_states:
				temp = run(next_state, elevator - 1, all_states + [next_state], w, level + 1)
				if (temp < best or not best) and temp:
					best = temp
				if temp and temp <= HORIZON:
					return temp
	# if best is still 0, this path of moves is no good and the return value will indicate this
	return best

# ---------
# new_state
# ---------

def new_state(state, elevator, direction, *items):
	"""
	return the state of the floors given items to move and direction to move in (expressed as the value of new floor - current floor)
	"""
	new = deepcopy(state)
	for item in items:
		insort(new[elevator + direction], item)
		new[elevator].remove(item)
	return new

# -----
# fried
# -----

def fried(state):
	"""
	given a possible state of the floors, determine whether any microchips will get fried
	"""
	for floor in state:
		for item in floor:
			if item[-1] == 'M' and correspondings[item] not in floor and any(poss_gen[-1] == 'G' for poss_gen in floor):
				return True
	return False

# ----
# read
# ----

def read(line):
	"""
	record which items are on the floor
	"""
	items = []
	words = line.split()
	for i in range(2, len(words)):
		if 'generator' in words[i]:
			symbol = element_symbols[words[i - 1]]
			insort(items, symbol + 'G')
		elif 'microchip' in words[i]:
			symbol = element_symbols[words[i - 1].replace('-compatible', '')]
			insort(items, symbol + 'M')
			correspondings[symbol + 'M'] = symbol + 'G'
	return items

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	initial = []
	elevator = 0
	for line in reader:
		initial.append(read(line))
	out = str(run(initial, elevator, [initial], writer, 0))
	writer.write(out)

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
