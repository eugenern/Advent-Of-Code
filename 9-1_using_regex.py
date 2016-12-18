"""
Given a compressed sequence of characters, find the length of the decompressed file
"""

# -------
# imports
# -------

import sys
import re

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	for line in reader:
		final = ''
		prog = re.compile(r'\((\d+)x(\d+)\)')
		match = prog.search(line)
		while match:
			final += line[:match.start()]
			num_chars, reps = int(match.group(1)), int(match.group(2))
			final += line[match.end():(match.end() + num_chars)] * reps
			line = line[(match.end() + num_chars):]
			match = prog.search(line)
		final += line
		writer.write(str(len(final)))

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
