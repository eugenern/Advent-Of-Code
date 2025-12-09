"""
Given instructions to go up and/or down floors, find the first time one visits floor -1
"""

# -------
# imports
# -------

import sys

# -----------------
# look_for_basement
# -----------------

def look_for_basement(instructions):
    """
    iterate through instructions and return when floor == -1
    """
    cur_floor = 0
    for i, instruction in enumerate(instructions):
        cur_floor += 1 if instruction == '(' else -1
        if cur_floor == -1:
            return i + 1

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    instructions = reader.readline().rstrip()
    writer.write(str(look_for_basement(instructions)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
