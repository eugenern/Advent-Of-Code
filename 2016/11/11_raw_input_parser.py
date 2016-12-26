"""
Given a description of the locations of the generators and the microchips, form the input to solve the problem in clingo syntax
"""

#!/usr/bin/env python3

# -------
# imports
# -------

import sys
from element_symbols_dict import element_symbols

# -----
# parse
# -----

def parse(line, writer):
	"""
	each line will contain information about which floor its describing and what objects are on that floor initially
	parse the line to form more clingo-friendly facts
	"""
	# NOTE: eventually want to have some way to indicate the order of the floors, like an 'above' predicate or something
	# ALSO: have to be able to associate generators with their matching microchips
	words = line.split()
	floor = words[1]
	writer.write('loc(' + floor + ').\n')
	for i in range(2, len(words)):
		if 'generator' in words[i]:
			item = element_symbols[words[i - 1]] + 'G'
			writer.write('generator(' + item + ').\n')
			writer.write('on(' + item + ', ' + floor + ', 0).\n')
		if 'microchip' in words[i]:
			item = element_symbols[words[i - 1].replace('-compatible', '')] + 'M'
			writer.write('microchip(' + item + ').\n')
			writer.write('on(' + item + ', ' + floor + ', 0).\n')

# ----------
# form_input
# ----------

def form_input(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	for line in reader:
		parse(line, writer)
	# assuming the first floor is always called 'first', the elevator will always start out on 'first'
	writer.write('elevator(first, 0).')

# ----
# main
# ----

if __name__ == "__main__":
	form_input(sys.stdin, sys.stdout)
