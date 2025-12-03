"""
Given directions to traverse grid, how many houses get visited
"""

# -------
# imports
# -------

import sys

# ------------
# count_houses
# ------------

def count_houses(directions):
    """
    iterate through directions and track how many houses get visited
    """
    # format of coord: x, y
    visited = set()
    cur_house = (0, 0)
    visited.add(cur_house)
    for direction in directions:
        if direction == '^':
            cur_house = (cur_house[0], cur_house[1] + 1)
        elif direction == 'v':
            cur_house = (cur_house[0], cur_house[1] - 1)
        elif direction == '>':
            cur_house = (cur_house[0] + 1, cur_house[1])
        elif direction == '<':
            cur_house = (cur_house[0] - 1, cur_house[1])
        visited.add(cur_house)

    return len(visited)

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    directions = reader.readline().rstrip()
    writer.write(str(count_houses(directions)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
