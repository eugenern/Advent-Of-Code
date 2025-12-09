"""
Given a grid with paper rolls, count how many can be accessed by the forklift
"""

# -------
# imports
# -------

import sys

# ----------------
# count removable
# ----------------

def count_removable(grid):
    """
    given grid with paper rolls, repeatedly remove those that are adjacent to <4 rolls
    and count how many end up removed
    """
    count = 0
    found_accessible = True
    while found_accessible:
        found_accessible = False
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '@':
                    adj = 0
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if (
                                (k or l)
                                and i + k >= 0 and i + k < len(grid)
                                and j + l >= 0 and j + l < len(row)
                                and grid[i + k][j + l] == '@'
                            ):
                                adj += 1
                    if adj < 4:
                        count += 1
                        grid[i][j] = '.'
                        found_accessible = True

    return count

# ----
# read
# ----

def read(string):
    """
    get a row of the grid
    """
    return list(string)

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    grid = []
    for line in reader:
        grid.append(read(line))

    writer.write(str(count_removable(grid)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
