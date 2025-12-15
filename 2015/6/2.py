"""
Given instructions for displaying lights in a grid,
determine the total brightness across the whole grid
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
    create the lights grid, follow the instructions, and sum up total brightness
    """
    grid = [[0 for x in range(1000)] for y in range(1000)]

    for line in reader:
        action, corner_1_x, corner_1_y, corner_2_x, corner_2_y = read(line)
        for x in range(corner_1_x, corner_2_x + 1):
            for y in range(corner_1_y, corner_2_y + 1):
                if len(action) == 1:
                    grid[y][x] += 2
                elif action[1] == 'on':
                    grid[y][x] += 1
                elif grid[y][x] > 0:
                    grid[y][x] -= 1

    return sum(map(sum, grid))

# ----
# main
# ----

if __name__ == "__main__":
    print(solve(sys.stdin))
