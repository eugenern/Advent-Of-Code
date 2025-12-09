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
    santa_cur_house = (0, 0)
    robo_cur_house = (0, 0)
    visited.add(santa_cur_house)
    santas_turn = True
    for direction in directions:
        x_move = 1 if direction == '>' else -1 if direction == '<' else 0
        y_move = 1 if direction == '^' else -1 if direction == 'v' else 0
        if santas_turn:
            santa_cur_house = (santa_cur_house[0] + x_move, santa_cur_house[1] + y_move)
            visited.add(santa_cur_house)
        else:
            robo_cur_house = (robo_cur_house[0] + x_move, robo_cur_house[1] + y_move)
            visited.add(robo_cur_house)
        santas_turn = not santas_turn

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
