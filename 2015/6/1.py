"""
Given instructions for displaying lights in a grid, determine how many lights end up lit
"""

# -------
# imports
# -------

import sys

# ----
# read
# ----

def read(string):
    """
    determine instruction's action
    and the two opposite corners of the rectangle to which the action applies
    """
    parts = string.split()
    action, corner_1_str, corner_2_str = parts[:-3], parts[-3], parts[-1]
    corner_1_x, corner_1_y = map(int, corner_1_str.split(','))
    corner_2_x, corner_2_y = map(int, corner_2_str.split(','))
    return action, corner_1_x, corner_1_y, corner_2_x, corner_2_y

# -----
# solve
# -----

def solve(reader):
    """
    create the lights grid, follow the instructions, and count all lit lights
    """
    grid = [[False for x in range(1000)] for y in range(1000)]

    for line in reader:
        action, corner_1_x, corner_1_y, corner_2_x, corner_2_y = read(line)
        for x in range(corner_1_x, corner_2_x + 1):
            for y in range(corner_1_y, corner_2_y + 1):
                grid[y][x] = not grid[y][x] if len(action) == 1 else action[1] == 'on'

    return sum(row.count(True) for row in grid)

# ----
# main
# ----

if __name__ == "__main__":
    print(solve(sys.stdin))
