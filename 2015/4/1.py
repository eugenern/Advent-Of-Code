"""
Given a secret key, find the lowest positive int to append for md5 hash to start w/ 00000
"""

# -------
# imports
# -------

import sys
from hashlib import md5

# ------------
# find_number
# ------------

def find_number(key):
    """
    find lowest number that can be appended to key to produce md5 hash starting w/ 00000
    """
    found = False
    i = 0
    while not found:
        i += 1
        total_input = (key + str(i)).encode('utf-8')
        if md5(total_input, usedforsecurity=False).hexdigest().startswith('00000'):
            found = True

    return i

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    key = reader.readline().rstrip()
    writer.write(str(find_number(key)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
