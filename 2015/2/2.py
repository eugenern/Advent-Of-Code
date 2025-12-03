"""
Given a list of dimensions for rect prisms, calculate total volume + smallest perimeters
"""

# -------
# imports
# -------

import sys

# --------------------------
# calculate_perim_and_volume
# --------------------------

def calculate_perim_and_volume(ln, wd, ht):
    """
    calculate smallest perimeter in rect prism + volume
    """
    perim = 2 * min(ln + wd, ln + ht, wd + ht)
    vol = ln * wd * ht
    return perim + vol

# ----
# read
# ----

def read(string):
    """
    get length, width, height
    """
    return map(int, string.split('x'))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(str(sum(calculate_perim_and_volume(*read(line.rstrip())) for line in reader)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
