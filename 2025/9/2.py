"""
Given a list of red tile positions, find the largest area of a rectangle
that can be formed with red tiles as two of its opposite corners
and is only comprised of red and/or green tiles

note: i have no idea how to efficiently determine whether a rectangle or even a single point
is part of the red/green region, so i'll try to figure out a naive/brute force solution
Hmm, creating a 99k x 99k grid is way too slow. Need to figure out a better approach
New idea: check whether the perimeter of the rect is entirely reds/greens; if so, inside is as well
Wait no, how to mark the green tiles within the region?

Google search is talking about "ray casting" / "crossing number" algorithm
Ok, here's the plan: for each possible rect, we can easily get the four corners
And i'm going to make an assumption: if all tiles on the perimeter of the rectangle are red/green,
then all tiles inside the rect must be as well. check every point on the perim of the rect:
first, gather all
"""

# -------
# imports
# -------

import sys
from itertools import combinations

# ----
# read
# ----

def read(string):
    """
    get
    """
    return tuple(map(int, string.split(',')))

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    writer a writer
    """
    # NOTE: to index into grid, first provide y-val (which row) then x-val (which col)
    reds = list(map(read, reader))
    all_red_x, all_red_y = set(red[0] for red in reds), set(red[1] for red in reds)
    for corners in sorted(combinations(reds, 2),
                         key=lambda x: (abs(x[0][0] - x[1][0]) + 1) * (abs(x[0][1] - x[1][1]) + 1),
                         reverse=True):
        print(f'corners {corners}')
        # corners[0] = (corners[0][0], corners[0],[1]); corners[1] = (corners[1][0], corners[1][1])
        lo_x, lo_y, hi_x, hi_y = min(corners[0][0], corners[1][0]), \
                                 min(corners[0][1], corners[1][1]), \
                                 max(corners[0][0], corners[1][0]), \
                                 max(corners[0][1], corners[1][1])

        # check all points from lo_x to hi_x @ lo_y & hi_y, and from lo_y to hi_y @ lo_x & hi_x
        all_inside = True
        for y in [lo_y, hi_y]:
            for x in (red_x for red_x in all_red_x if lo_x <= red_x <= hi_x):
                # print(f'\tperim point {x}, {y}')
                inside = False
                for i, red in enumerate(reds):
                    edge = (red, reds[(i + 1) % len(reds)])
                    # print(f'\t\tedge {edge}')
                    # edge case: if point is directly on edge, inside is True
                    if edge[0][0] == edge[1][0] == x \
                    and min(edge[0][1], edge[1][1]) <= y <= max(edge[0][1], edge[1][1]) \
                    or edge[0][1] == edge[1][1] == y \
                    and min(edge[0][0], edge[1][0]) <= x <= max(edge[0][0], edge[1][0]):
                        # print('\t\t\tpoint is directly on edge')
                        inside = True
                        break
                    # cast a ray
                    # edge case: edge is on same y-val as point
                    if edge[0][1] == edge[1][1] == y and x < min(edge[0][0], edge[1][0]):
                        prev_red = reds[i - 1]
                        next_red = reds[(i + 2) % len(reds)]
                        # print(f'\t\t\tprev_red {prev_red} next_red {next_red}')
                        if (prev_red[1] < y) != (next_red[1] < y):
                            inside = not inside
                    elif x < edge[0][0] == edge[1][0] \
                    and min(edge[0][1], edge[1][1]) <= y <= max(edge[0][1], edge[1][1]):
                        # print('\t\t\tpoint passes through edge')
                        inside = not inside
                # after all edges checked, point is inside or outside
                if not inside:
                    all_inside = False
                    break
        if not all_inside:
            continue

        for x in [lo_x, hi_x]:
            for y in (red_y for red_y in all_red_y if lo_y <= red_y <= hi_y):
                # print(f'\tperim point {x}, {y}')
                inside = False
                for i, red in enumerate(reds):
                    edge = (red, reds[(i + 1) % len(reds)])
                    # print(f'\t\tedge {edge}')
                    # edge case: if point is directly on edge, inside is True
                    if edge[0][0] == edge[1][0] == x \
                    and min(edge[0][1], edge[1][1]) <= y <= max(edge[0][1], edge[1][1]) \
                    or edge[0][1] == edge[1][1] == y \
                    and min(edge[0][0], edge[1][0]) <= x <= max(edge[0][0], edge[1][0]):
                        # print('\t\t\tpoint is directly on edge')
                        inside = True
                        break
                    # cast a ray
                    # edge case: edge is on same y-val as point
                    if edge[0][1] == edge[1][1] == y and x < min(edge[0][0], edge[1][0]):
                        prev_red = reds[i - 1]
                        next_red = reds[(i + 2) % len(reds)]
                        # print(f'\t\t\tprev_red {prev_red} next_red {next_red}')
                        if (prev_red[1] < y) != (next_red[1] < y):
                            inside = not inside
                    elif x < edge[0][0] == edge[1][0] \
                    and min(edge[0][1], edge[1][1]) <= y <= max(edge[0][1], edge[1][1]):
                        # print('\t\t\tpoint passes through edge')
                        inside = not inside
                # after all edges checked, point is inside or outside
                if not inside:
                    all_inside = False
                    break
        if all_inside:
            print(
                corners,
                (abs(corners[0][0] - corners[1][0]) + 1) * (abs(corners[0][1] - corners[1][1]) + 1)
                )
            break

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
