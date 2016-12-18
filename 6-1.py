"""
Given a repeated but corrupted message, recover the message
"""

# -------
# imports
# -------

import sys

# ---------
# most_freq
# ---------

def most_freq(column):
	"""
	find the value with the highest frequency in the tuple
	"""

	max_count = 0
	for char in set(column):
		if column.count(char) > max_count:
			real_char = char
			max_count = column.count(char)
	return real_char

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""

	message = ''
	messages = [line for line in reader]
	for column in zip(*messages):
		next_char = most_freq(column)
		message += next_char
	writer.write(message)

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
