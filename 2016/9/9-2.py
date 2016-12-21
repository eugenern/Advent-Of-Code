"""
Given a compressed sequence of characters, find the length of the decompressed file
"""

#!/usr/bin/env python3

# -------
# imports
# -------

import sys
import re

prog = re.compile(r'\((\d+)x(\d+)\)')

# ----------
# decompress
# ----------

def decompress(string):
	"""
	given something, do something
	"""
	count = 0
	match = prog.search(string)
	while match:
		count += match.start()
		num_chars, reps = int(match.group(1)), int(match.group(2))
		count += decompress(string[match.end():(match.end() + num_chars)]) * reps
		string = string[(match.end() + num_chars):]
		match = prog.search(string)
	count += len(string)
	return count

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	# NOTE: DON'T try to construct the decompressed sequence; use MATH to figure out the length
	for line in reader:
		count = decompress(line)
		writer.write(str(count))

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
