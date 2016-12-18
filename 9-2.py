"""
Not yet complete
Given a compressed sequence of characters, find the length of the decompressed file
"""

# -------
# imports
# -------

import sys
import re

# ----------
# decompress
# ----------

def decompress(match):
	"""
	given something, do something
	"""
	dunno

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	# NOTE: DON'T try to construct the decompressed sequence; use MATH to figure out the length
	prog = re.compile(r'\((\d+)x(\d+)\)')
	for line in reader:
		count = 0
		match = prog.search(line)
		while match:
			count += match.start()
			num_chars, reps = int(match.group(1)), int(match.group(2))
			count += num_chars * reps
			line = line[(match.end() + num_chars):]
			match = prog.search(line)
		count += len(line)
		writer.write(str(count))

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
