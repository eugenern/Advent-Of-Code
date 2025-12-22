"""
Given a list of red tile positions, find the largest area of a rectangle
that can be formed with red tiles as two of its opposite corners
and is only comprised of red and/or green tiles

how to determine whether a rectangle or even a single point is part of the red/green region?
- creating a 99k x 99k grid is way too slow
- use "ray casting" / "crossing number" algorithm to check if a point is in the region
  - for each possible rect, use the opposite corners to get the perimeter tiles. i'll assume that if
    all tiles on the perimeter of the rectangle are red/green, then all tiles inside the rect must
    be as well. check every perimeter tile w/ the ray casting algo
"""

# -------
# imports
# -------

import sys
from itertools import combinations, chain, product

# ----------------------------------------------
# calculate rectangle area from opposite corners
# ----------------------------------------------

def calc_area(corners):
    """
    given opposite corners of a rectangle, calculate the area
    """
    return (abs(corners[0][0] - corners[1][0]) + 1) * (abs(corners[0][1] - corners[1][1]) + 1)

# ----
# read
# ----

def read(string):
    """
    get coordinates of red tile
    """
    return tuple(map(int, string.split(',')))

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    """
    reds = list(map(read, reader))
    all_red_x, all_red_y = map(set, zip(*reds))
    for corners in sorted(combinations(reds, 2), key=calc_area, reverse=True):
        lo_x, lo_y, hi_x, hi_y = \
            min(corners[0][0], corners[1][0]), min(corners[0][1], corners[1][1]), \
            max(corners[0][0], corners[1][0]), max(corners[0][1], corners[1][1])

        # check all points from lo_x to hi_x @ lo_y & hi_y, and from lo_y to hi_y @ lo_x & hi_x
        all_inside = True
        # note: don't know whether picking the smaller range is actually an optimization or not
        xs = (x for x in range(lo_x, hi_x + 1) if x in all_red_x) if hi_x - lo_x < len(all_red_x) \
             else (red_x for red_x in all_red_x if lo_x <= red_x <= hi_x)
        ys = (y for y in range(lo_y, hi_y + 1) if y in all_red_y) if hi_y - lo_y < len(all_red_y) \
             else (red_y for red_y in all_red_y if lo_y <= red_y <= hi_y)
        for x, y in chain(product(xs, (lo_y, hi_y)), product((lo_x, hi_x), ys)):
            inside = False
            for i, red in enumerate(reds):
                edge = (red, reds[(i + 1) % len(reds)])
                lo_edge_x, lo_edge_y, hi_edge_x, hi_edge_y = \
                    min(edge[0][0], edge[1][0]), min(edge[0][1], edge[1][1]), \
                    max(edge[0][0], edge[1][0]), max(edge[0][1], edge[1][1])
                # edge case: if point is directly on edge, inside is True
                if lo_edge_x == hi_edge_x == x and lo_edge_y <= y <= hi_edge_y \
                or lo_edge_y == hi_edge_y == y and lo_edge_x <= x <= hi_edge_x:
                    inside = True
                    break
                # cast a ray
                # edge case: edge & point have same y. check if edges before and after go up or down
                if lo_edge_y == hi_edge_y == y and x < lo_edge_x:
                    prev_red = reds[i - 1]
                    next_red = reds[(i + 2) % len(reds)]
                    if (prev_red[1] < y) != (next_red[1] < y):
                        inside = not inside
                elif x < lo_edge_x == hi_edge_x and lo_edge_y <= y <= hi_edge_y:
                    inside = not inside
            # after all edges checked, point is inside or outside
            if not inside:
                all_inside = False
                break
        if all_inside:
            print(corners, calc_area(corners))
            break

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
