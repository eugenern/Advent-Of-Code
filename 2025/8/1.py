"""
Given a list of junction box positions, connect the 1000 shortest paths between pairs
and return the product of the sizes of the 3 largest circuits (connected networks)

note: distance in 3-D space is sqrt((x'-x)^2 + (y'-y)^2 + (z'-z)^2)
note: math.dist() provides a generalized calculation
"""

# -------
# imports
# -------

import sys
from math import dist, prod
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

def solve(reader, writer, num_pairs):
    """
    reader a reader
    writer a writer
    """
    boxes = list(map(read, reader))
    circuits = [{box} for box in boxes]
    for box1, box2 in sorted(combinations(boxes, 2), key=lambda combo: dist(*combo))[:num_pairs]:
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

    circuits.sort(key=len, reverse=True)

    writer.write(str(prod(map(len, circuits[:3]))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout, 1000)
