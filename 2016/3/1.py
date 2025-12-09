"""
Given sets consisting of three side lengths,
determine how many sets could describe sides of a triangle
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
    return all(sides[i] < sides[(i + 1) % 3] + sides[(i + 2) % 3] for i in range(3))

# ----
# read
# ----

def read(string):
    """
    get a list of ints from the string
    """
    return list(map(int, string.split()))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(str(len(list(filter(triangle_possible, map(read, reader))))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
