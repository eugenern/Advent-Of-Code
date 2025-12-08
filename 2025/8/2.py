"""
Given a list of junction box positions, connect boxes until circuit is complete
and return the product of the x-coords of the last 2 boxes to connect

note: distance in 3-D space is sqrt((x'-x)^2 + (y'-y)^2 + (z'-z)^2)
note: math.dist() provides a generalized calculation
"""

# -------
# imports
# -------

import sys
from math import dist
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

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    boxes = list(map(read, reader))
    circuits = [{box} for box in boxes]
    to_connect = sorted(combinations(boxes, 2), key=lambda combo: dist(*combo))
    connect_ind = 0
    while len(circuits) > 1:
        box1, box2 = to_connect[connect_ind]
        # pair has 2 boxes; possibilities:
        # both boxes are already in the same circuit: nothing happens
        # both boxes are already in different circuits: merge the sets and delete one
        ind1 = ind2 = -1
        for i, circuit in enumerate(circuits):
            if box1 in circuit:
                ind1 = i
                if ind2 != -1:
                    break
            if box2 in circuit:
                ind2 = i
                if ind1 != -1:
                    break

        if ind1 != ind2:
            circuits[ind1] |= circuits[ind2]
            del circuits[ind2]
            if len(circuits) == 1:
                writer.write(str(int(box1[0] * box2[0])))

        connect_ind += 1

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
