"""
Given a grid with paper rolls, count how many can be accessed by the forklift
"""

# -------
# imports
# -------

import sys

# ----------------
# count accessible
# ----------------

def count_accessible(grid):
    """
    given grid with paper rolls, count how many are adjacent to <4 rolls
    """
    count = 0
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

    writer.write(str(count_accessible(grid)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
