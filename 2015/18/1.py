"""
Given a grid of lights, find how many are lit after 100 steps of animation
"""

# ------------
# neighbors on
# ------------

def neighbors_on(grid, i, j):
    """
    Given a grid of lights and the position of a light, return how many neighbors are lit
    """
    on = 0
    if i > 0:
        on += grid[i - 1][j-1 if j > 0 else j : j+2 if j < len(grid[i])-1 else j+1].count(True)
    if i < len(grid) - 1:
        on += grid[i + 1][j-1 if j > 0 else j : j+2 if j < len(grid[i])-1 else j+1].count(True)
    if j > 0 and grid[i][j - 1]:
        on += 1
    if j < len(grid[i]) - 1 and grid[i][j + 1]:
        on += 1

    return on

# ------
# update
# ------

def update(grid):
    """
    Given a grid, move one step in animation and update grid values
    """
    new_grid = [[] for _ in range(len(grid))]
    for i, row in enumerate(grid):
        for j, light in enumerate(row):
            new_grid[i].append(False if neighbors_on(grid, i, j) not in {2, 3} else
                               True if neighbors_on(grid, i, j) == 3 else
                               light)

    return new_grid

# -----
# parse
# -----

def parse(line):
    """
    Given a line of the lights grid, turn it into a list of boolean values
    """
    return list(c == '#' for c in line.rstrip())

# -----
# solve
# -----

def solve(filepath, steps):
    """
    Given the path of a file containing valid input, return the solution
    """
    with open(filepath, encoding='utf-8') as file:
        grid = list(map(parse, file))

    for _ in range(steps):
        grid = update(grid)

    return sum(row.count(True) for row in grid)

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('sample_input', 4))
    print(solve('input', 100))
