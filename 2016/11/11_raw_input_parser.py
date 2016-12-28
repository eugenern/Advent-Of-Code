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
	words = line.split()
	floor = words[1]
	writer.write('loc(' + floor + ').\n')
	if prev:
		writer.write('above(' + floor + ',' + prev + ').\n')
	for i in range(2, len(words)):
		if 'generator' in words[i]:
			symbol = element_symbols[words[i - 1]]
			writer.write('generator(' + symbol + 'G).\n')
			writer.write('on(' + symbol + 'G,' + floor + ',0).\n')
		elif 'microchip' in words[i]:
			symbol = element_symbols[words[i - 1].replace('-compatible', '')]
			writer.write('microchip(' + symbol + 'M).\n')
			writer.write('corresponds(' + symbol + 'M,' + symbol + 'G).\n')
			writer.write('on(' + symbol + 'M,' + floor + ',0).\n')
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
	# didn't use next line b/c sacrificing flexibility for much-needed efficiency
	# writer.write('final(' + prev + ').\n')
	# assuming the first floor is always called 'first', the elevator will always start out on 'first'
	writer.write('elevator(first,0).\n')

# ----
# main
# ----

if __name__ == "__main__":
	form_input(sys.stdin, sys.stdout)
