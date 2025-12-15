"""
Given a list of dimensions for rect prisms, calculate total surface area + slack area
"""

# -------
# imports
# -------

import sys

# ------------------------
# calculate_area_and_slack
# ------------------------

def calculate_area_and_slack(ln, wd, ht):
    """
    calculate surface area of rect prism + extra slack area
    """
    sa = 2 * ((lw := ln * wd) + (lh := ln * ht) + (wh := wd * ht))
    slack = min(lw, lh, wh)
    return sa + slack

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
    writer.write(str(sum(calculate_area_and_slack(*read(line.rstrip())) for line in reader)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
