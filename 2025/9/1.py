"""
Given a list of red tile positions, find the largest area of a rectangle
that can be formed with red tiles as two of its opposite corners
"""

# -------
# imports
# -------

import sys
from itertools import combinations

# ----
# read
# ----

def read(string):
    """
    get coordinates of red tile
    """
    return tuple(map(int, string.split(',')))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(str(max(
        (abs(corners[0][0] - corners[1][0]) + 1) * (abs(corners[0][1] - corners[1][1]) + 1)
        for corners in combinations(map(read, reader), 2)
        )))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
