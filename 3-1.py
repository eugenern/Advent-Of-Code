"""
Given sets consisting of three side lengths, determine how many sets could describe sides of a triangle
"""

# -------
# imports
# -------

import sys

# -----------------
# triangle_possible
# -----------------

def triangle_possible(sides):
	"""
	given an array of three sides, determine whether they can make up a triangle
	"""
	return max(sides) < sum([sides[i] for i in range(len(sides)) if i != sides.index(max(sides))])

# ----
# read
# ----

def read(string):
	"""
	get a list of ints from the string
	"""
	return [int(side) for side in string.split()]

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	# count = 0
	# for line in reader:
	# 	if triangle_possible(read(line)):
	# 		count += 1
	# writer.write(str(count))

	writer.write(str([triangle_possible(read(line)) for line in reader].count(True)))
	# writer.write(str(len(list(filter(triangle_possible, [read(line) for line in reader])))))

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
