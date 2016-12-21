"""
Given a list of IP addresses, determine how many of them support Transport Layer Snooping
"""

# -------
# imports
# -------

import sys
import re

# -----
# check
# -----

def check(iters):
	"""
	given iterators over the hypernet sequences and over the other parts, determine whether ABBAs are placed appropriately
	"""
	return check_hypernet(iters[0]) and check_other(iters[1])

# --------------
# check_hypernet
# --------------

def check_hypernet(seq_iter):
	"""
	given iterator over the hypernet sequences, check that there are no ABBAs
	"""
	return not any(filter(has_abba, seq_iter))

# -----------
# check_other
# -----------

def check_other(seq_iter):
	"""
	given iterator over the other parts, check that there is at least one ABBA
	"""
	return any(filter(has_abba, seq_iter))

# --------
# has_abba
# --------

def has_abba(match_obj):
	"""
	given a match object, determine whether the matched sequence contains an ABBA
	"""
	seq = match_obj.group(0)
	return any(map(lambda x: seq[x] != seq[x + 1] and seq[x + 1] == seq[x + 2] and seq[x] == seq[x + 3], range(len(seq) - 3))) # faster because lazy
	# return list(filter(lambda x: seq[x] != seq[x + 1] and seq[x + 1] == seq[x + 2] and seq[x] == seq[x + 3], range(len(seq) - 3)))

# ----
# read
# ----

def read(string):
	"""
	get iterators for the hypernet sequences and the supernet sequences from the IP address
	"""
	return (re.finditer('(?<=\[)[a-z]+(?=\])', string), re.finditer('(?<=\])[a-z]+|[a-z]+(?=\[)', string))

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	# writer.write(str(len([line for line in reader if check(read(line))])))
	writer.write(str(len(list(filter(lambda line: check(read(line)), reader))))) # seems to be the faster option

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
