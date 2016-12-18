"""
Given a door ID, construct the door's password according to the algorithm described on the AoC website
"""

# -------
# imports
# -------

import sys
import hashlib

# -------------
# find_password
# -------------

def find_password(door_id):
	"""
	apply md5 hash to door_id + integer index and form the door's password
	"""
	index = 0
	password = ''

	while len(password) < 8:
		m = hashlib.md5((door_id + str(index)).encode())
		if all(map(lambda x: x == '0', m.hexdigest()[:5])):
			password += m.hexdigest()[5]
		index += 1

	return password

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	for line in reader:
		writer.write(find_password(line))

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
