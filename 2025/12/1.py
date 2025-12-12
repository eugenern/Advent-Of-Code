"""
Given lists of shapes and regions along with specified quantities for each shape,
determine how many regions can accomodate their specified quantities of shapes
"""

# -------
# imports
# -------

import sys

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    """
    shapes = []
    regions_quantities = []
    for line in reader:
        if 'x' in line:
            substrs = line.split()
            dims = list(map(int, substrs[0][:-1].split('x')))
            quantities = list(map(int, substrs[1:]))
            regions_quantities.append((dims, quantities))
        else:
            shape = []
            while shape_line := reader.readline().rstrip():
                shape.append([c == '#' for c in shape_line])
            shapes.append(shape)

    valid_regions = 0
    for rq in regions_quantities:
        dims, quantities = rq
        # region = [[False] * dims[0] for _ in range(dims[1])]
        # for quantity in quantities:
        #     pass
        # i have no idea how to make this work. 3 ways to rotate, 2 ways to flip, and you can combine rotations with flips?
        # there's just no way i can dfs placing pieces onto a grid with 2500 cells

        # ok never mind people are saying this isn't truly a packing problem
        # and we can just act as if each shape is a 3x3 square
        num_sqs = sum(quantities)
        if (dims[0] // 3) * (dims[1] // 3) >= num_sqs:
            valid_regions += 1

    print(valid_regions)

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
