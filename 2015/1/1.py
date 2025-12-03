"""
Given instructions to go up and/or down floors, find the floor one ends up on
"""

# -------
# imports
# -------

import sys

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    instructions = reader.readline().rstrip()
    writer.write(str(instructions.count('(') - instructions.count(')')))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
