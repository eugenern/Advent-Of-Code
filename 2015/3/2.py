"""
Given directions to traverse grid, count how many houses get visited
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
    cur_houses = [(0, 0), (0, 0)]
    visited = {cur_houses[0],}
    who_goes = 0
    for direction in directions:
        x_move = 1 if direction == '>' else -1 if direction == '<' else 0
        y_move = 1 if direction == '^' else -1 if direction == 'v' else 0
        cur_houses[who_goes] = (cur_houses[who_goes][0] + x_move, cur_houses[who_goes][1] + y_move)
        visited.add(cur_houses[who_goes])
        who_goes = int(not who_goes)

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
