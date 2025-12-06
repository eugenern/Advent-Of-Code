"""
Given a cephalopod math worksheet,
find the grand total sum of all the answers to the individual problems
"""

# -------
# imports
# -------

import sys
from math import prod

# ----
# read
# ----

def read(string):
    """
    get a list of either ints or operators
    """
    terms = string.split()
    if terms[0].isdecimal():
        return list(map(int, terms))
    return terms

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    terms = list(map(read, reader))

    writer.write(str(sum((sum if op[-1] == '+' else prod)(op[:-1]) for op in zip(*terms))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
