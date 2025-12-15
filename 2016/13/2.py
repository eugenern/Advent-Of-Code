"""
Given the office designer's favorite number and a goal location, determine how many locations can be
reached within 50 steps from (1,1)
"""

#!/usr/bin/env python3

# -----
# solve
# -----

def solve(fav_num, max_steps, grid_dim):
    """
    create the office map and search for a path to goal
    """
    # True means wall, False means open space
    grid = [
        [bool(bin(x*x + 3*x + 2*x*y + y + y*y + fav_num).count('1') % 2)
         for x in range(grid_dim)]
        for y in range(grid_dim)]

    fringe = [((1, 1), 0)]
    visited = set()
    while fringe:
        loc, steps = fringe[0][0], fringe[0][1]
        x, y = loc
        del fringe[0]

        if y >= len(grid) or x >= len(grid[0]):
            raise ValueError('Exploration led to a cell outside the grid. Expand the grid')

        if loc in visited or steps > max_steps or x < 0 or y < 0 or grid[y][x]:
            continue

        visited.add(loc)
        fringe += [(new_loc, steps + 1)
                   for new_loc in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]]

    return len(visited)

# ----
# main
# ----

if __name__ == "__main__":
    print(solve(1364, 50, 50))
