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
    count = 0
    all_sides = [read(line) for line in reader]

    # triple groups every 3 lines together
    for triple in zip(all_sides[::3], all_sides[1::3], all_sides[2::3]):
        # then we take each of the 3 lines and zip their elements together by index in line
        count += len(list(filter(triangle_possible, zip(*triple))))
    writer.write(str(count))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
