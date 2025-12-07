"""
Given a tachyon manifold diagram, calculate how many times the beam will split
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
    get a list of the locations of each splitter in the row
    """
    splitters = set()
    for i, c in enumerate(string):
        if c == '^' or c == 'S':
            splitters.add(i)
    return splitters

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    splits = 0
    beams = read(reader.readline())
    for line in reader:
        splitters = read(line)
        new_beams = set()
        for beam in beams:
            if beam in splitters:
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
                splits += 1
            else:
                new_beams.add(beam)
        beams = new_beams

    writer.write(str(splits))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
