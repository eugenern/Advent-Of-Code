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

def parse(line, prev, writer):
	"""
	each line will contain information about which floor its describing and what objects are on that floor initially
	parse the line to form more clingo-friendly facts
	"""
	# NOTE: have to be able to associate generators with their matching microchips
	words = line.split()
	floor = words[1]
	writer.write('loc(' + floor + ').\n')
	if prev:
		writer.write('above(' + floor + ', ' + prev + ').\n')
	for i in range(2, len(words)):
		if 'generator' in words[i]:
			item = element_symbols[words[i - 1]] + 'G'
			writer.write('generator(' + item + ').\n')
			writer.write('on(' + item + ', ' + floor + ', 0).\n')
		if 'microchip' in words[i]:
			item = element_symbols[words[i - 1].replace('-compatible', '')] + 'M'
			writer.write('microchip(' + item + ').\n')
			writer.write('on(' + item + ', ' + floor + ', 0).\n')
	return floor

# ----------
# form_input
# ----------

def form_input(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	prev = ''
	for line in reader:
		prev = parse(line, prev, writer)
	writer.write('final(' + prev + ').\n')
	# assuming the first floor is always called 'first', the elevator will always start out on 'first'
	writer.write('elevator(first, 0).\n')

# ----
# main
# ----

if __name__ == "__main__":
	form_input(sys.stdin, sys.stdout)
