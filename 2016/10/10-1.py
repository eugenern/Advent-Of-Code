"""
Given a list of microchip and bot instructions, find which bot is the one to compare two certain microchips
"""

#!/usr/bin/env python3

# -------
# imports
# -------

import sys
import re

# -----------
# global vars
# -----------

bots = [[] for i in range(209)] # hardcoding in the number of bots
give_tos = [[] for i in range(209)] # lists should be in format [give low to, bot or output, give high to, bot or output]
outputs = [[] for i in range(20)] # hardcoding in the number of outputs

# ---
# run
# ---

def run(chip_val1, chip_val2):
	"""
	transfer chips according to the instructions until a bot has both chips with the values that were passed in; return that bot
	"""
	return 0

# ---------
# add_instr
# ---------

def add_instr(instr):
	"""
	interpret an instruction and add its values to the relevant list
	"""
	words = instr.split()
	if words[0] == 'bot':
		# add to bot instr list
		give_tos[int(words[1])] = [int(words[6]), words[5], int(words[11]), words[10]]
	else:
		# give bot in bot list the chip
		bots[int(words[5])].append(int(words[1]))

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	# go line by line to build up an instruction list of lists where index is bot and list shows who to give chips
	# also fill a list of bots and their chip slots
	for line in reader:
		add_instr(line)
	output = str(run(61, 17))
	writer.write(output)

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
